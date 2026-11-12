Audit `wiki/` for: orphan pages (zero backlinks), stub pages older than 14 days, broken wikilinks (link target has no file), and any `[!contradiction]` callouts still unresolved.
Run `.claude/scripts/check-links.py --summary` first and report its counts: nested links, unescaped table pipes, welded paths and de-linked targets are linkifier regressions and it must exit 0.
Report as a checklist. Don't fix anything automatically — list the issues and wait for confirmation.
