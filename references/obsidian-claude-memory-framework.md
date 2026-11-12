---
title: Obsidian + Claude Memory Framework (source)
category: references
tags: [obsidian, claude, memory, karpathy, wiki, compounding]
relationships:
  - target: "[[skills/multi-agent-vault-wiring]]"
    type: related_to
  - target: "[[concepts/Obsidian Wiki]]"
    type: related_to
  - target: "[[concepts/multi-agent-obsidian-wiki-synergy]]"
    type: related_to
sources:
  - "_raw/inbox/2026-11-12-claude-memory-compounding-guide.md"
  - /home/x1/Downloads/@ai/obsidian-claude-code-memory-framework.md
summary: "Karpathy-style compounding memory for Claude Code/Obsidian — immutable raw inputs, maintained wiki knowledge, index cache, ingest/ask/lint loop."
provenance: {extracted: 0.95, inferred: 0.05, ambiguous: 0.0}
base_confidence: 0.8
lifecycle: draft
lifecycle_changed: 2026-11-12
tier: core
created: 2026-07-09T09:57:44Z
updated: 2026-11-12
---

# Obsidian + Claude Memory Framework (source)

## What It Covers
Compounding markdown "brain" for Claude Code: avoid per-session resets by accumulating decisions/knowledge in a vault. Raw sources stay immutable; derived knowledge is compiled into linked wiki pages; retrieval uses a compact index instead of whole-vault scans.

## Key Points
- **Three layers:** raw (immutable inputs) → wiki/knowledge (compiled, cross-linked, append-only notes) → output (deliverables).
- **Session start:** read schema/conventions → read index cache → answer from pointed pages (follow links as needed), not re-derivation.
- **Jobs:** Ingest (process inbox, match/create/update pages, add wikilinks/stubs, archive raw, update indexes/manifest) and Answer (index-first retrieval with citations). Lint for orphans/stubs/broken links/contradictions.
- **Efficiency:** token savings come from retrieval vs context-dumping; index stays compact while vault grows (pair with vector/cold archive only at larger scale).
- **Coexistence in this vault:** aligns with `AGENTS.md`, `index.md`/`00-INDEX.md`, `hot.md`/`log.md`, `_raw/` + `_raw/_archived/`, `.manifest.json`, v7.6 buckets (`01_WORK`–`06_STATE`) and domain folders (`concepts/`, `entities/`, `projects/`, `journal/`, `skills/`, `references/`, `synthesis/`), `.claude/commands/`, and Obsidian MCP/Git sync.

## Full Source
- Captured guide: [[_raw/inbox/2026-11-12-claude-memory-compounding-guide]] (immutable; `processed: false` until ingested/archived per protocol).

## Notes
### 2026-11-12 — integrated into vault (coexist)
- Added `.claude/commands/{ingest,ask,lint}.md`, `.claude/scripts/diff-inbox.sh`, `00-INDEX.md`, and `_raw/inbox/` support; appended compounding protocol to `AGENTS.md` to coexist with existing v7.6/wiki conventions.

## Related
- [[concepts/Obsidian Wiki]] · [[concepts/multi-agent-obsidian-wiki-synergy]] · [[skills/multi-agent-vault-wiring]] · [[AGENTS]]
