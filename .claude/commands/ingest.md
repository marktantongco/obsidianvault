Process every unprocessed file in `_raw/inbox/` (and any unprocessed legacy captures directly in `_raw/`, excluding `_raw/index.md` and `_raw/_archived/`) per the **Ingest** job in `CLAUDE.md`.
Work one file at a time. After each file, state: file processed, pages created, pages updated, links added.
Move each processed raw file to `_raw/_archived/`, mark `processed: true` and `processed_at: YYYY-MM-DD` in its frontmatter, regenerate `00-INDEX.md`, and update `.claude/inbox-manifest.json`.
Do not summarize the whole batch until finished.
