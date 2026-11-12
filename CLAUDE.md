# work-brain (Obsidian Vault) — Compounding Memory Protocol

**Vault:** `~/Projects/obsidianvault` (git-backed, Obsidian + MCP). This file defines the compounding memory layer (Karpathy-style raw → wiki → output) adapted to coexist with this vault's existing v7.6 buckets and conventions (`AGENTS.md`, `_raw/`, `concepts/`, `journal/`, etc.).

You are the maintainer of this knowledge base. Two jobs:

## Job 1: Ingest
When asked to process `_raw/inbox/` (or `/ingest`), for each unprocessed file:
1. Read the file. Identify its type: person, project, decision, concept, or meeting.
2. Search `wiki/` for an existing page with the same entity (check title + `aliases` in frontmatter). Also check relevant v7.6 buckets (`01_WORK/`, `02_KNOWLEDGE/`, `04_RELATIONSHIP/`, `concepts/`, `entities/`, `journal/`, `projects/`) for an existing canonical page to avoid duplicates — prefer linking/updating the canonical page (or noting it) over creating a conflicting duplicate.
3. If a match exists in `wiki/`: append a new dated subsection under `## Notes` on that page. **Never overwrite existing content.** Update `updated:` in frontmatter.
4. If no match exists: create a new page in `wiki/<type-plural>/` (people, projects, decisions, concepts; meetings → `wiki/projects/` or `wiki/concepts/` as appropriate) using the wiki template below.
5. Add `[[wikilinks]]` to every other entity mentioned (person, project, concept). Create stub pages for entities that don't have one yet (title + `status: stub` frontmatter only).
6. Update the relevant `wiki/_moc/<domain>.md` (Map of Content): add a link to any new or updated page.
7. Move the raw file to `_raw/_archived/` (processed, not deleted) and add/update frontmatter: `processed: true` and `processed_at: YYYY-MM-DD` (and `superseded_by: [[path/to/page]]` when distilled into an existing canonical page).
8. Refresh the `## Wiki (compounding layer)` section of `00-INDEX.md` by walking frontmatter across `wiki/` (do not re-read full page bodies). `00-INDEX.md` is a **shared** vault-wide cache: leave its other sections (`Projects`, `Concepts`, `Knowledge`, `State`, `Skills/References`, `Raw / Inbox`) as the index pass wrote them, and only correct entries your own ingest made stale.
9. Update `.claude/inbox-manifest.json` for each processed file so change detection stays accurate.

> **Legacy coexistence:** `_raw/` is the vault's existing staging area (see `_raw/index.md`). New drops for this compounding workflow go in `_raw/inbox/`. Unprocessed captures already sitting directly in `_raw/` may be ingested the same way, then archived to `_raw/_archived/` per existing practice.

## Job 2: Answer
When asked a question (or `/ask`):
1. Read `00-INDEX.md` first — never read the whole vault.
2. From the index, identify 2–5 candidate pages. Read only those.
3. If those pages link to others you need, follow the links — don't grep the whole vault.
4. Answer, and cite which wiki pages you drew from. If the index doesn't cover it, say so — don't guess.

## Layers & rules
- **`_raw/inbox/`** (Layer 1 input): drop transcripts, pasted notes, emails here. Files are **immutable once saved**.
- **`_raw/_archived/`** (and legacy processed captures): archived raw files already ingested (not deleted).
- **`wiki/`** (Layer 2, compounding memory): Claude-maintained knowledge derived from raw. If wiki content is wrong, do **not** hand-edit history away — drop a correcting note into `_raw/inbox/` and let ingest reconcile.
- **`output/`** (Layer 3): finished deliverables pulled from the wiki.
- **Existing vault structure remains canonical:** v7.6 buckets (`01_WORK/`…`06_STATE/`), `_raw/`, `concepts/`, `entities/`, `journal/`, `projects/`, `.manifest.json`, `index.md`, `AGENTS.md`, Obsidian Git/MCP workflows all continue to work as before. The `wiki/output` layer compounds session memory and should cross-link (`[[wikilinks]]`) into canonical pages rather than replace them.

## Wiki page template (wiki/)
Every page in `wiki/` should have YAML frontmatter and an append-only Notes log:

```markdown
---
type: project          # person | project | decision | concept | meeting
status: active         # active | stub | archived
tags: []
aliases: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
summary: One-line summary for the index (cheap to read).
# Vault-aligned optional fields (use when helpful): title, category, lifecycle, tier, source, confidence
---

# Title

One-line summary Claude can put straight into an index without re-reading the page.

## Links
[[Related Entity]] · [[Another Entity]]

## Notes
### YYYY-MM-DD — source: _raw/_archived/<file>.md
What happened, decided, or learned. Short. Dated. Append-only.
```

## Conventions
- Every wiki page ends with a `## Notes` section listing dated entries — append-only log.
- Never delete a wikilink because the target page doesn't exist yet — create a stub instead.
- **Orphan pages** (zero backlinks) are a defect; flag them during `/lint`.
- **Contradictions** between a new raw note and an existing wiki page: don't silently overwrite. Add a callout:
  `> [!contradiction]` noting both claims and their source dates.
- Prefer `[[wikilinks]]` and keep summaries current so `00-INDEX.md` stays compact.
- To read/write this vault from agents, the Obsidian MCP (`vault_read`, `vault_write`, `vault_append`, `vault_patch`, `search_simple`, …) is available (see `AGENTS.md` / `obsidian-memory` skill).

## 00-INDEX.md format
Refresh your section by scanning `wiki/` frontmatter (type, status, title, summary/first line). The vault-wide index also carries the other buckets, owned by the index pass — edit only what your ingest changed:

```markdown
# Index — last regenerated YYYY-MM-DD

## Projects
- [[Page]] — status — short summary

## People
- ...

## Decisions
- ...

## Concepts
- ...

## Orphans (needs linking)
- none currently (or list)
```
