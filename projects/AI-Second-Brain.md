---
title: AI Second Brain
tags: [project, setup, infrastructure]
type: project
created: 2026-07-09
updated: 2026-07-09
status: active
lifecycle: verified
tier: core
---

# AI Second Brain

## Goal
Set up a complete multi-agent AI development environment with shared knowledge base.

## Components Installed

### CLI Tools (6)
| Tool | Version | Status |
|------|---------|--------|
| [[OpenCode]] | v1.17.15 | Installed |
| [[MiMo Code]] | v0.1.5 | Installed |
| [[Claude Code]] | v2.1.205 | Installed |
| [[OpenAI Codex]] | v0.143.0 | Installed |
| [[Hermes Agent]] | v0.18.2 | Installed |
| [[Grok]] | v0.2.93 | Installed |

### Desktop Apps (2)
| App | Location | Status |
|-----|----------|--------|
| Obsidian | `~/Applications/Obsidian.AppImage` | Installed |
| Simplenote | `~/Applications/Simplenote/` | Installed |

### Wiki & Knowledge
| Component | Location | Status |
|-----------|----------|--------|
| obsidian-wiki | v2026.7.2 | Installed |
| Primary Vault | `~/obsidianvault/` | Created |
| llm-wiki | `~/obsidian-vaults/AI-Second-Brain/.wiki/` | Configured |

### Agent Bridges
| Bridge | Location | Status |
|--------|----------|--------|
| Hermes-OpenCode | `~/.hermes/plugins/opencode/` | Installed |
| Hermes-Claude | `~/.hermes/plugins/code-bridge/` | Installed |

### Unified Memory
| Component | Location | Status |
|-----------|----------|--------|
| agentic-stack | `~/ai-workspace/.agent/` | Created |
| Symlinks | All agents | Linked |

### Skills
| Agent | Skills Count |
|-------|--------------|
| OpenCode | 37 |
| Hermes | 36 |
| Claude | 37 |
| Agents | 37 |

## Timeline
- **2026-07-09**: Initial setup complete
  - All CLI tools installed
  - Desktop apps installed
  - Wiki system configured
  - Agent bridges installed
  - Unified memory created
  - Skills installed to all agents
  - API keys configured (OpenAI)

## Next Steps
- [ ] Configure additional API keys (Anthropic, Gemini)
- [ ] Test cross-agent workflows
- [ ] Build first project
- [ ] Set up daily wiki updates
- [ ] Configure Hermes plugins

## Files
- `~/.bashrc` — PATH entries
- `~/opencode.json` — OpenCode config
- `~/.opencode/.env` — OpenAI API key
- `~/.claude/.env` — OpenAI API key
- `~/.hermes/hermes-agent/.env` — OpenAI API key
- `~/.codex/.env` — OpenAI API key

## Related
- [[AI Agents]]
- [[Development Workflow]]
- [[Obsidian Wiki]]
