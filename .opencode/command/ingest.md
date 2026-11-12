---
description: Ingest unprocessed raw notes into the compounding wiki (vault CLAUDE.md protocol)
---

Process every unprocessed file in `_raw/inbox/` (and any unprocessed legacy captures directly in `_raw/`, excluding `_raw/index.md` and `_raw/_archived/`) per the **Ingest** job in the vault root `CLAUDE.md`.

Work one file at a time. After each file, state: file processed, pages created, pages updated, links added.

Move each processed raw file to `_raw/_archived/`, then run `python3 .claude/scripts/mark-processed.py _raw/_archived/<file> --created <pages> --updated <pages>` — it writes the canonical `.manifest.json` entry, stamps `processed: true`/`processed_at` into the raw's frontmatter, and refreshes the `.claude/inbox-manifest.json` cursor used by `diff-inbox.sh`. Finish by refreshing the `## Wiki (compounding layer)` section of `00-INDEX.md` (leave the vault-wide sections to the index pass).

Prefer the Obsidian MCP write tools when available; fall back to direct file edits only if the REST endpoint is down. Do not summarize the whole batch until finished.
