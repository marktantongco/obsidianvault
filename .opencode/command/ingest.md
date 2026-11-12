---
description: Ingest unprocessed raw notes into the compounding wiki (vault CLAUDE.md protocol)
---

Process every unprocessed file in `_raw/inbox/` (and any unprocessed legacy captures directly in `_raw/`, excluding `_raw/index.md` and `_raw/_archived/`) per the **Ingest** job in the vault root `CLAUDE.md`.

Work one file at a time. After each file, state: file processed, pages created, pages updated, links added.

Move each processed raw file to `_raw/_archived/`, mark `processed: true` and `processed_at: YYYY-MM-DD` in its frontmatter, regenerate `00-INDEX.md` from `wiki/` frontmatter, and record it in `.claude/inbox-manifest.json` with `python3 .claude/scripts/mark-processed.py _raw/_archived/<file>`.

Prefer the Obsidian MCP write tools when available; fall back to direct file edits only if the REST endpoint is down. Do not summarize the whole batch until finished.
