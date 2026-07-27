---
title: OpenCode
tags: [opencode, coding, cli, terminal-agent]
type: concept
created: 2026-07-09
updated: 2026-07-24
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
