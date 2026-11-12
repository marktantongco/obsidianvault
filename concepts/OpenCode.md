---
title: OpenCode
tags: [opencode, coding, cli, terminal-agent]
type: concept
created: 2026-07-09
updated: 2026-11-13
lifecycle: verified
tier: core
source: project
---

# OpenCode

## Overview

OpenCode is a powerful terminal-based AI coding agent with an interactive TUI built with Bubble Tea. It supports multiple AI providers, session management, and extensive tool integration.

## Version
v1.17.16

## Installation
```bash
curl -fsSL https://opencode.ai/install | bash
```

## Location
- Binary: `~/.opencode/bin/opencode`
- Config: `~/opencode.json`
- Skills: `~/.opencode/skills/` (37 skills)
- Agent Bridge: `~/.opencode/agentic` → `~/ai-workspace/.agent/`

## Features
- **Interactive TUI** with Bubble Tea framework
- **Multiple AI providers**: OpenAI, Anthropic, Gemini, MiMo, OpenCode Zen, OpenCode Go
- **Session management** with resume capability
- **Tool integration**: file access, shell execution, web search, LSP
- **Skills system**: 37 installed skills covering wiki, research, code review
- **Agent bridging**: Hermes-OpenCode plugin for orchestration
- **File change tracking** with git awareness

## Providers Supported

| Provider | Config Location | Auth Method |
|----------|----------------|-------------|
| OpenAI | `~/.opencode/.env` | API Key |
| Anthropic | `~/.opencode/.env` | API Key |
| Gemini | `~/.opencode/.env` | API Key |
| MiMo | `~/.opencode/.env` | API Key |
| OpenCode Zen | `~/.opencode/.env` | API Key |
| OpenCode Go | `~/.opencode/.env` | API Key |

## Usage

```bash
# Start interactive mode
opencode

# Start with specific directory
opencode -c /path/to/project

# Non-interactive prompt
opencode -p "Explain this code"

# Use specific provider
opencode --provider openai

# Resume a session
opencode --resume
```

## Configuration (`~/opencode.json`)
```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["AGENTS.md", ".agent/AGENTS.md"]
}
```

## Skills Directory
Skills are symlinked from `~/.agents/skills/` and include:
- **wiki-query**, **wiki-capture**, **wiki-ingest** — Knowledge management
- **wiki-research**, **wiki-dashboard** — Research & visualization
- **deep-research**, **super-research** — Advanced web research
- **skill-creator**, **design-blueprint** — Development tools
- **modern-python-toolchain** — Python development
- And 30+ more skills

## Integration Points
- **Hermes Agent**: Bridged via `~/.hermes/plugins/opencode/`
- **Obsidian Vault**: Wiki skills for knowledge management
- **jcode**: Shares agentic-stack memory at `~/ai-workspace/.agent/`

## Related
- [[AI Agents]] — Agent ecosystem overview
- [[JCode]] — jcode AI coding stack
- [[Hermes Agent]] — Hermes orchestrator
- [[Claude Code]] — Claude Code reviewer
- [[skills/agent-setup-gotchas]] — config-schema and install failures

## Notes

- **2026-07-13 — free-model routing policy.** All 11 agents in `oh-my-openagent.json` and the agent fallback chains in `opencode.jsonc` were repointed at free-tier models so no agent defaults to a paid model (paid ids demoted to last-resort fallback). Standing user preference, verbatim: *"do not use models from nvidia or google only free models from 'opencode zen' free"*. Sources: `_raw/_archived/2026-07-13-opencode-free-model-config.md`, [[concepts/oh-my-openagent]].
- **2026-11-13 — policy re-verified against the Zen surface.** Free ids observed live: `big-pickle`, `mimo-v2.6-flash-free`, `deepseek-v4.1-flash-free`, `glm-5.3-flash-free`, `longcat-2.5-free`, `iceman-free`, `inkling-2-small-free`, `beam-free`, `flint-40b-free`, `nemotron-3.5-super-lightning-free`, `minimax-m3.1-flash-free`. The 2026-07 list (`nemotron-nano-9b-v2`, `gemma-4-31b-it`, `gemma-4-27b-it`, `lfm-2.5-1.2b`) no longer exists, so that table is historical only. Local routing goes through `owl-router` on `127.0.0.1:8080` (provider `owl-local`, model `owl-local/flint-40b-free`); the Zen free tier is metered per egress block and answers `FreeUsageLimitError` once exhausted, which the patched ingress falls back to local Ollama for.

> [!resolved] Superseded 2026-11-13: header claims (v1.17.16 / `~/opencode.json` / `~/.opencode/skills/`) are stale. Live state measured 2026-11-13: **v2.2.2**, sole config `~/.config/opencode/opencode.json` (a project-level `.opencode/opencode.json` overrides it), skills load from `~/.agents/skills/`. The 2026-11 dated claims below are authoritative; the header block is kept as history.
