#!/usr/bin/env python3
"""Update .claude/inbox-manifest.json for ingested raw files.

Usage (from vault root):
  python3 .claude/scripts/mark-processed.py _raw/inbox/file.md [more...]
  python3 .claude/scripts/mark-processed.py --mtime _raw/_archived/file.md
"""
import json, os, sys, time
from pathlib import Path

manifest = Path('.claude/inbox-manifest.json')
manifest.parent.mkdir(parents=True, exist_ok=True)
data = json.loads(manifest.read_text()) if manifest.exists() else {}

use_mtime = False
args = sys.argv[1:]
if args and args[0] == '--mtime':
    use_mtime = True
    args = args[1:]

for f in args:
    p = Path(f)
    if use_mtime and p.exists():
        data[str(p)] = os.path.getmtime(p)
    else:
        data[str(p)] = time.time()

manifest.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
print(f'updated {manifest} ({len(args)} entries)')
