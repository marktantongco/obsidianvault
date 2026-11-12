Process every unprocessed file in `_raw/inbox/` (and any unprocessed legacy captures directly in `_raw/`, excluding `_raw/index.md` and `_raw/_archived/`) per the **Ingest** job in `CLAUDE.md`.
Work one file at a time. After each file, state: file processed, pages created, pages updated, links added.
Move each processed raw file to `_raw/_archived/`, then run `python3 .claude/scripts/mark-processed.py _raw/_archived/<file> --created <pages> --updated <pages>` (writes canonical `.manifest.json`, stamps `processed: true`/`processed_at`, refreshes the `diff-inbox.sh` cursor), and refresh the `## Wiki (compounding layer)` section of `00-INDEX.md`.
Do not summarize the whole batch until finished.
