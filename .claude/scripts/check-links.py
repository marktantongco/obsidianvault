#!/usr/bin/env python3
"""Detect wikilink corruption produced by substring "linkifier" passes.

Read-only. Exit 1 if any defect is found, so `/lint` (or CI) fails loudly.

Classes:
  nested   [[a/[[a/Page|Page]]]]        a linkifier wrapped an existing link
  table    | [[a/Page|Page]] |          unescaped pipe splits the table cell
  welded   `~/.[[concepts/OpenCode|opencode]]/`   link welded into a path/code span
  delinked Name ^[inferred: no canonical note yet]   link demoted instead of stubbed

Usage: check-links.py [--summary] [--max 5] [PATH ...]
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP = {".git", ".obsidian", "node_modules", "_skills"}
NESTED = re.compile(r"!?\[\[[^\n\]]*\[\[")
TABLE_LINK = re.compile(r"!?\[\[([^\]\n]+)\]\]")
LINK = re.compile(r"!?\[\[[^\[\]\n]+\]\]")
DELINKED = re.compile(r"\^\[inferred: no canonical note yet\]")


def welded_in_span(line):
    """A link inside an inline code span that is welded to a path/URL char."""
    for span in re.finditer(r"`[^`\n]*`", line):
        seg = span.group(0)
        for m in LINK.finditer(seg):
            before = seg[m.start() - 1] if m.start() else "`"
            after = seg[m.end()] if m.end() < len(seg) else "`"
            if before in "/.:" or after in "/:" or seg[m.end():m.end() + 1] == ".":
                return True
    return False


def scan(paths, max_examples):
    hits = {"nested": [], "table": [], "welded": [], "delinked": []}
    for p in paths:
        try:
            text = p.read_text(errors="ignore")
        except OSError:
            continue
        rel = p.relative_to(ROOT) if p.is_relative_to(ROOT) else p
        for i, line in enumerate(text.splitlines(), 1):
            n = len(NESTED.findall(line))
            if n:
                hits["nested"].extend([f"{rel}:{i}: {line.strip()[:120]}"] * n)
            if line.strip().startswith("|"):
                t = sum(1 for m in TABLE_LINK.finditer(line) if re.search(r"(?<!\\)\|", m.group(1)))
                if t:
                    hits["table"].extend([f"{rel}:{i}: {line.strip()[:120]}"] * t)
            if welded_in_span(line):
                hits["welded"].append(f"{rel}:{i}: {line.strip()[:120]}")
            d = len(DELINKED.findall(line))
            if d:
                hits["delinked"].extend([f"{rel}:{i}: {line.strip()[:120]}"] * d)
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--max", type=int, default=3, help="examples printed per class")
    ap.add_argument("--summary", action="store_true")
    a = ap.parse_args()

    paths = [pathlib.Path(p) for p in a.paths] if a.paths else [
        p for p in ROOT.rglob("*.md") if not (set(p.parts) & SKIP)
    ]
    hits = scan(paths, a.max)
    total = sum(len(v) for v in hits.values())
    for cls, items in hits.items():
        print(f"{cls:9} {len(items):4}")
        if not a.summary:
            for line in items[: a.max]:
                print(f"          {line}")
    print(f"{'TOTAL':9} {total:4}  ({len(paths)} files)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
