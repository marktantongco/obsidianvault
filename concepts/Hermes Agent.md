---
title: Hermes Agent
tags: [hermes, orchestrator, agents]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: core
---

# Hermes Agent

## Overview
Hermes Agent is the self-improving AI agent built by Nous Research. It's the only agent with a built-in learning loop.

## Version
v0.18.2 (2026.7.7.2)

## Installation
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## Location
- Home: `~/.hermes/hermes-agent/`
- Binary: `~/.hermes/hermes-agent/.venv/bin/hermes`
- Plugins: `~/.hermes/plugins/`
- Skills: `~/.hermes/skills/` (36 skills)

## Features
- **Persistent Memory**: Learns your projects, auto-generates skills
- **Multi-Platform**: Telegram, Discord, Slack, WhatsApp, Signal, CLI
- **Scheduled Automation**: Natural-language scheduling
- **Task Delegation**: Isolated subagents with own conversations
- **Web Search**: Browser automation, vision, image generation
- **Sandboxing**: Docker, SSH, Singularity, Modal backends

## Plugins Installed
1. **Hermes-OpenCode**: `~/.hermes/plugins/opencode/`
2. **Hermes-Claude**: `~/.hermes/plugins/code-bridge/`

## Usage
```bash
# Start interactive mode
hermes

# Check version
hermes --version

# List plugins
hermes plugins list
```

## Related
- [[AI Agents]]
- [[OpenCode]]
- [[Claude Code]]
