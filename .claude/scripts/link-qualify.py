#!/usr/bin/env python3
"""Qualify bare wikilinks safely: rewrite whole links only, escape table pipes,
stub missing targets. Never de-links, never touches text outside [[...]].

A linkifier that substitutes a page *name* wherever it appears is what broke
this vault (nested links, split tables, paths rewritten). This tool is the
opposite: it locates complete [[...]] tokens outside fenced blocks and inline
code, and rewrites only those tokens.

Rules
  bare name, one matching page      [[Page]]            -> [[bucket/Page]]
  bare name, several matches        left alone, reported as ambiguous
  qualified path that does not land  repaired from its basename when unique
  target has no page                 stub page created and linked (never removed)
  link on a table row                alias pipe escaped: [[a/Page\\|Page]]
  embed, glob, template placeholder  untouched
  frontmatter relationship targets   treated as links (they are)

Dry-run by default. --apply writes; stubbing is on for --apply and can be
turned off with --no-stub. Idempotent: a second run does nothing.

Usage: link-qualify.py [--apply] [--no-stub] [--stub-dir concepts]
                       [--root DIR] [--paths FILE ...]
"""
import argparse
import collections
import datetime
import pathlib
import re
import sys

SKIP_PARTS = {".git", ".obsidian", "_skills"}
GENERATED = {"index.md", "hot.md", "log.md"}   # written by the daily Action
PLACEHOLDER = ("{{", "}}", "<%", "%>")
LINK = re.compile(r"(!?)\[\[([^\[\]\n]+)\]\]")

STUB_TEMPLATE = """---
title: {name}
category: {folder}
tags: [stub, link-qualifier]
summary: Stub for a target pages already link to; created by link-qualify.
lifecycle: stub
tier: peripheral
source: system
confidence: low
---

# {name}

## Notes

### {date} — source: link qualifier
Linked from existing pages before a page existed. The vault stubs a missing
target instead of deleting the link, so this page holds the backlinks until
the subject is written up.
"""


class Index:
    def __init__(self, files, root):
        self.by_path, self.by_base = {}, collections.defaultdict(list)
        for p in files:
            rel = p.relative_to(root).as_posix()[:-3]
            self.by_path[rel.casefold()] = rel
            self.by_base[rel.split("/")[-1].casefold()].append(rel)

    @staticmethod
    def norm(target):
        return re.sub(r"\.md$", "", target.strip(), flags=re.I)

    def path_hit(self, target):
        return self.by_path.get(self.norm(target).casefold())

    def base_hits(self, target):
        return self.by_base.get(self.norm(target).split("/")[-1].casefold(), [])


def is_stub_name(name):
    return not any(tok in name for tok in PLACEHOLDER) and not any(c in name for c in "*<>")


def split_link(body):
    m = re.search(r"(?<!\\)\|", body)
    if not m:
        return body.strip(), None
    return body[:m.start()].strip(), body[m.end():].strip()


def outside_code(line):
    """Character ranges of `line` that are not inside an inline code span."""
    spans = [(m.start(), m.end()) for m in re.finditer(r"`[^`\n]*`", line)]
    keep, pos = [], 0
    for a, b in spans:
        keep.append((pos, a))
        pos = b
    keep.append((pos, len(line)))
    return [(a, b) for a, b in keep if a < b]


def fenced_lines(lines):
    out, f = [], False
    for l in lines:
        if l.lstrip().startswith(("```", "~~~")):
            out.append(True)
            f = not f
            continue
        out.append(f)
    return out


def qualify_line_simple(line, index, plan, stubs, stub_dir, allow_stub, where=""):
    """Rewrite [[...]] tokens that sit outside inline code; leave everything else."""
    if "[[" not in line:
        return line
    keep = outside_code(line)
    def in_code(idx):
        return not any(a <= idx < b for a, b in keep)

    out, i = [], 0
    for m in LINK.finditer(line):
        if in_code(m.start()):
            continue
        bang, body = m.group(1), m.group(2)
        # parse aliases split by an escaped pipe (table rows) as a real pipe
        target, alias = split_link(body.replace("\\|", "|"))
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
        new_target, action = target, None

        if bang or not is_stub_name(target) or index.path_hit(target):
            action = None
        elif "/" in target:
            hits = index.base_hits(target)
            if len(hits) == 1:
                new_target, action = hits[0], "repath"
            elif not hits:
                action = "missing-qualified"
        else:
            hits = index.base_hits(target)
            if len(hits) == 1:
                new_target, action = hits[0], "qualify"
            elif len(hits) > 1:
                action = "ambiguous"
            elif allow_stub:
                stubs.add(f"{stub_dir}/{target}")
                new_target, action = f"{stub_dir}/{target}", "stub"

        body_new = body
        if action in ("qualify", "repath", "stub"):
            body_new = new_target + (f"#{anchor}" if anchor else "") + (f"|{alias}" if alias else "")
        if line.lstrip().startswith("|"):
            body_new = re.sub(r"(?<!\\)\|", r"\\|", body_new)
        link_new = f"{bang}[[{body_new}]]"
        if action:
            shown = body_new if action in ("qualify", "repath", "stub") else body + " (left as is)"
            plan[action].append(f"{where}: [{body}] -> [{shown}]")
        if link_new != m.group(0):
            out.append(line[i:m.start()])
            out.append(link_new)
            i = m.end()
    out.append(line[i:])
    return "".join(out)


def main():
    ap = argparse.ArgumentParser(description="Safely qualify wikilinks, escape table pipes, stub missing targets.")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--no-stub", action="store_true", help="report missing targets instead of creating stubs")
    ap.add_argument("--stub-dir", default="concepts", help="folder for new stubs (default: concepts)")
    ap.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parents[2]))
    ap.add_argument("--paths", nargs="*", help="limit to these files")
    ap.add_argument("--check", action="store_true",
                    help="CI mode: exit 1 if any link needs qualifying or the guard fails")
    ap.add_argument("--include-generated", action="store_true",
                    help="also rewrite index.md / hot.md / log.md, which the Action regenerates")
    a = ap.parse_args()

    root = pathlib.Path(a.root).resolve()
    all_files = [p for p in root.rglob("*.md") if not (set(p.parts) & SKIP_PARTS)]
    # the index must see generated pages so [[index]] / [[hot]] resolve; they are
    # only excluded from editing, since the Action rewrites them
    index = Index(all_files, root)
    files = all_files
    generated = [p for p in files if p.name in GENERATED]
    if not a.include_generated:
        files = [p for p in files if p.name not in GENERATED]
    if a.paths:
        wanted = {pathlib.Path(p).resolve() for p in a.paths}
        files = [p for p in files if p.resolve() in wanted]

    plan = collections.defaultdict(list)
    stubs = set()
    written = 0
    for p in files:
        lines = p.read_text(errors="ignore").split("\n")
        mask = fenced_lines(lines)
        changed = False
        for i, line in enumerate(lines):
            if mask[i] or "[[" not in line:
                continue
            new = qualify_line_simple(line, index, plan, stubs, a.stub_dir, not a.no_stub,
                                      f"{p.relative_to(root)}:{i + 1}")
            if new != line:
                lines[i] = new
                changed = True
        if changed:
            written += 1
            if a.apply:
                p.write_text("\n".join(lines))

    created = 0
    if a.apply and not a.no_stub:
        for rel in sorted(stubs):
            dest = root / f"{rel}.md"
            if dest.exists():
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            name = rel.split("/")[-1]
            dest.write_text(STUB_TEMPLATE.format(name=name, folder=rel.split("/")[0],
                                                 date=datetime.date.today().isoformat()))
            created += 1

    order = ["qualify", "repath", "stub", "ambiguous", "missing-qualified"]
    for k in order:
        if plan[k]:
            print(f"{k:18} {len(plan[k]):4}")
            for line in plan[k][:5]:
                print(f"                   {line}")
    changed = sum(len(plan[k]) for k in ("qualify", "repath", "stub"))
    flagged = sum(len(plan[k]) for k in ("ambiguous", "missing-qualified"))
    print(f"{'links changed':18} {changed:4}   left as is (flagged): {flagged}"
          f"   files touched: {written}   stubs created: {created}")
    if a.check:
        a.apply = False
    if generated and not a.include_generated:
        print(f"skipped {len(generated)} generated file(s) (index.md/hot.md/log.md); --include-generated to rewrite them")

    needs = changed + flagged + (len(stubs) if not a.no_stub else 0)
    if a.check:
        import subprocess
        guard = pathlib.Path(__file__).with_name("check-links.py")
        r = subprocess.run([sys.executable, str(guard), "--summary", str(root)],
                           capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode != 0:
            print("CHECK: FAIL (guard)")
            sys.exit(1)
        if needs:
            print(f"CHECK: FAIL ({needs} link(s) need qualifying)")
            sys.exit(1)
        print("CHECK: PASS")
    print("mode:", "APPLY" if a.apply else "DRY-RUN (nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
