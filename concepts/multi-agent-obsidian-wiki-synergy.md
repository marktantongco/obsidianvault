---
title: Multi-Agent Obsidian Wiki Synergy
category: concepts
tags: [obsidian, agents, wiki, multi-agent, configuration]
summary: How Ar9av/obsidian-wiki, the shared vault, and every CLI agent share one brain via config + symlinks.
lifecycle: draft
tier: core
created: 2026-07-09T00:00:00Z
updated: 2026-07-09T00:00:00Z
---

# Multi-Agent Obsidian Wiki Synergy

## Layers

1. **Framework (code/skills)** — `/home/x1/ai-workspace/obsidian-wiki` ([Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki))
2. **Config** — `~/.obsidian-wiki/config` → `OBSIDIAN_VAULT_PATH`
3. **Vault (compiled knowledge)** — `/home/x1/obsidianvault`
4. **Agent discovery** — each CLI has `skills/` symlinks into `.skills/` and `obsidian-vault` → vault

## Merge rules

| Source | Role | Do not |
|--------|------|--------|
| `obsidian-wiki` repo | Skill definitions, setup.sh, AGENTS bootstrap | Duplicate skills as copies |
| `~/.obsidian-wiki/config` | Single active vault pointer | Point agents at different vaults |
| `/home/x1/obsidianvault` | Canonical second brain | Fork per-agent vaults |
| `~/AGENTS.md` + `.agent/AGENTS.md` | Host project / agentic-stack brain | Replace wiki skills; **compose** with wiki |
| Per-agent `*/obsidian-vault` | Symlink only | Store unique notes there |

## Session bootstrap (all agents)

```
1. Read host AGENTS.md / CLAUDE.md
2. Resolve OBSIDIAN_VAULT_PATH
3. Read $VAULT/AGENTS.md
4. Skim hot.md
5. Use wiki-* skills as needed
```

## Related
- [[index]]
- Vault conventions in root `AGENTS.md`

## Current operational status (2026-07-09)
- `obsidian-wiki doctor`: **pass** (setup 2026.7.2, 12 agents)
- Canonical vault confirmed: `/home/x1/obsidianvault`
- Session bootstrap: host AGENTS.md + vault AGENTS.md + hot.md
- Ingest flywheel started from `Downloads/@ai` + session capture
