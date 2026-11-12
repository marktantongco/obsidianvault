---
description: Audit the compounding wiki for orphans, stale stubs, broken links, contradictions
---

Audit `wiki/` for: orphan pages (zero backlinks), stub pages older than 14 days, broken wikilinks (link target has no file), and any `[!contradiction]` callouts still unresolved.

Also report index drift: pages present in `wiki/` but missing from `00-INDEX.md`, and index entries whose page no longer exists.

Report as a checklist. Don't fix anything automatically — list the issues and wait for confirmation.
