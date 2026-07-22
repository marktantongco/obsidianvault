---
title: Multi-Agent Vault Wiring
category: skills
tags: [obsidian, agents, symlink]
sources:
  - conversation:2026-07-09
  - https://github.com/Ar9av/obsidian-wiki
summary: Point every CLI agent skill tree and AGENTS bootstrap at one Obsidian vault via config + symlinks.
provenance: {extracted: 0.75, inferred: 0.25, ambiguous: 0.0}
base_confidence: 0.72
lifecycle: draft
lifecycle_changed: 2026-07-09
tier: core
created: 2026-07-09T09:57:44Z
updated: 2026-07-09T10:44:46Z
relationships:
  - target: "[[concepts/multi-agent-obsidian-wiki-synergy]]"
    type: implements
  - target: "[[concepts/Obsidian Wiki]]"
    type: uses
---

# Multi-Agent Vault Wiring

## Canonical paths
- Vault: `/home/x1/obsidianvault`
- Config: `~/.obsidian-wiki/config`
- Framework: `/home/x1/ai-workspace/obsidian-wiki` or pip package skills

## Steps
1. `obsidian-wiki setup --vault /path/to/vault`
2. Symlink skills from package/repo `.skills/*` into each agent `skills/` dir.
3. Symlink vault as `~/.<agent>/obsidian-vault`.
4. Point each agent's AGENTS/CLAUDE/GEMINI.md at `$VAULT/AGENTS.md`.
5. Host project AGENTS.md must require vault read every session.

## Compose with agentic-stack
- `.agent/` = session memory, lessons, permissions
- Vault = durable distilled knowledge
- Do not fork a second vault per agent

## Related
- [[concepts/multi-agent-obsidian-wiki-synergy]] · [[concepts/Obsidian Wiki]] · [[concepts/AI Agents]]

## Session notes (promoted 2026-07-09)

# Multi-agent vault wiring gotchas

## Finding
Point every CLI at **one** vault (`/home/x1/obsidianvault`) via `~/.obsidian-wiki/config`, skill symlinks into package/repo `.skills/`, and `~/.<agent>/obsidian-vault` symlinks. Host + vault `AGENTS.md` must require vault load every session.

## Gotchas
- `obsidian-wiki setup` can thin global config — re-add `OBSIDIAN_WIKI_REPO` / `OBSIDIAN_SOURCES_DIR` after setup.
- Setting `enabled-extensions` to only GPaste **disables Ubuntu Dock** — always keep `ubuntu-dock@ubuntu.com`.
- Prefer symlink skills over copies so upgrades propagate.

## Promote
Run wiki-ingest to merge into [[skills/multi-agent-vault-wiring]].
