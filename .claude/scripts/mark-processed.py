#!/usr/bin/env python3
"""Record an ingested raw file in the vault's canonical manifest.

Canonical ledger : `.manifest.json`  -> sources[<path>] + stats + last_updated
Derived cursor   : `.claude/inbox-manifest.json` -> mtime only (used by diff-inbox.sh)

Both are written so the framework and the pre-existing vault pipeline stay in sync.

Usage (from vault root):
  python3 .claude/scripts/mark-processed.py _raw/_archived/file.md \
      [--created page.md,page.md] [--updated page.md] \
      [--source-type conversation|document|session] [--project ai-second-brain]
  python3 .claude/scripts/mark-processed.py --mtime _raw/_archived/file.md   # cursor only

The script also stamps `processed: true` / `processed_at: YYYY-MM-DD` into the
file's frontmatter when those keys are missing, so no manual edit is required.
"""
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CANONICAL = Path('.manifest.json')
CURSOR = Path('.claude/inbox-manifest.json')


def split_args(argv):
    opts = {'created': [], 'updated': [], 'source_type': None, 'project': None}
    files, use_mtime, i = [], False, 0
    while i < len(argv):
        a = argv[i]
        if a == '--mtime':
            use_mtime = True
        elif a == '--created':
            i += 1
            opts['created'] = [p.strip() for p in argv[i].split(',') if p.strip()]
        elif a == '--updated':
            i += 1
            opts['updated'] = [p.strip() for p in argv[i].split(',') if p.strip()]
        elif a == '--source-type':
            i += 1
            opts['source_type'] = argv[i]
        elif a == '--project':
            i += 1
            opts['project'] = argv[i]
        else:
            files.append(a)
        i += 1
    return files, use_mtime, opts


def stamp_frontmatter(p: Path):
    """Add processed: true / processed_at: <today> if absent. Returns True if changed."""
    text = p.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return False
    fm, changed = m.group(1), False
    today = datetime.now().astimezone().date().isoformat()
    if not re.search(r'^processed:\s*', fm, re.M):
        fm += '\nprocessed: true'
        changed = True
    if not re.search(r'^processed_at:\s*', fm, re.M):
        fm += f'\nprocessed_at: {today}'
        changed = True
    if changed:
        p.write_text(text[:m.start(1)] + fm + text[m.end(1):], encoding='utf-8')
    return changed


def rel(p: Path):
    try:
        return str(p.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(p)


def main():
    files, use_mtime, opts = split_args(sys.argv[1:])
    if not files:
        sys.exit(__doc__)

    cursor = json.loads(CURSOR.read_text()) if CURSOR.exists() else {}
    canonical = json.loads(CANONICAL.read_text()) if CANONICAL.exists() else {
        'version': '2026.7.2', 'sources': {}, 'stats': {}}
    sources = canonical.setdefault('sources', {})
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    for f in files:
        p = Path(f)
        key = rel(p)
        cursor[key] = os.path.getmtime(p) if (use_mtime and p.exists()) else time.time()
        if use_mtime or not p.exists():
            continue

        raw = p.read_bytes()
        entry = sources.get(key, {})
        entry.update({
            'ingested_at': now,
            'last_ingested': datetime.now(timezone.utc).isoformat(),
            'size_bytes': len(raw),
            'modified_at': datetime.fromtimestamp(
                os.path.getmtime(p), timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'content_hash': hashlib.sha256(raw).hexdigest(),
            'source_type': opts['source_type'] or entry.get('source_type', 'document'),
            'project': opts['project'] if opts['project'] is not None else entry.get('project'),
            'processed': True,
        })
        if opts['created']:
            entry['pages_created'] = opts['created']
            entry['pages_produced'] = opts['created']
        if opts['updated']:
            entry['pages_updated'] = opts['updated']
        sources[key] = entry
        if stamp_frontmatter(p):
            print(f'  stamped processed frontmatter: {key}')

    stats = canonical.setdefault('stats', {})
    stats['total_sources_ingested'] = len(sources)
    canonical['last_updated'] = now
    CANONICAL.write_text(json.dumps(canonical, indent=2, sort_keys=False) + '\n')
    CURSOR.parent.mkdir(parents=True, exist_ok=True)
    CURSOR.write_text(json.dumps(cursor, indent=2, sort_keys=True) + '\n')
    print(f'updated {CANONICAL} (sources: {len(sources)}) and cursor {CURSOR} '
          f'({len(files)} file(s))')


if __name__ == '__main__':
    main()
