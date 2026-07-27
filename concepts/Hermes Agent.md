---
title: Hermes Agent
tags: [hermes, orchestrator, agents, nous-research]
type: concept
created: 2026-07-09
updated: 2026-07-24
lifecycle: verified
tier: core
source: project
---

# Hermes Agent

## Overview

Hermes Agent is the **self-improving AI agent** built by Nous Research. It's the only agent with a built-in learning loop — it persists memory across sessions, auto-generates skills from patterns, and orchestrates other agents through plugins.

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
- Agent Bridge: `~/.hermes/agentic` → `~/ai-workspace/.agent/`

## Features
- **Persistent Memory**: Learns your projects, auto-generates skills from repeated patterns
- **Multi-Platform**: Telegram, Discord, Slack, WhatsApp, Signal, CLI
- **Scheduled Automation**: Natural-language scheduling (e.g., "check weather every morning")
- **Task Delegation**: Isolated subagents with own conversations and state
- **Web Search**: Browser automation, vision, image generation
- **Sandboxing**: Docker, SSH, Singularity, Modal backends
- **Self-Improvement**: Learns from past sessions, generates new skills autonomously

## Plugins Installed

### 1. Hermes-OpenCode
- Location: `~/.hermes/plugins/opencode/`
- Files: `plugin.yaml`, `opencode_tool.py`, `SKILL.md`
- Purpose: Enables Hermes to delegate coding tasks to OpenCode

### 2. Hermes-Claude (Code Bridge)
- Location: `~/.hermes/plugins/code-bridge/`
- Files: `plugin.yaml`, `config.yml`, `skills/`
- Purpose: Enables Hermes to delegate code review tasks to Claude Code

## Usage

```bash
# Start interactive mode
hermes

# Check version
hermes --version

# List plugins
hermes plugins list

# Run a task
hermes "Break down this task: Build a React todo app"

# Schedule recurring task
hermes "Remind me to stand up every hour"
```

## Agent Bridging Architecture

```
┌──────────────────────────────────────────────────────┐
│                   HERMES (Orchestrator)              │
│  - Persistent memory & learning                     │
│  - High-level planning & task decomposition         │
│  - Delegates to specialist agents                   │
└────────┬─────────┬─────────┬─────────────────────────┘
         │         │         │
         ▼         ▼         ▼
   ┌─────────┐ ┌────────┐ ┌──────────────┐
   │ OpenCode│ │ Claude │ │ Other Tools  │
   │ (Code)  │ │(Review)│ │ (Search/etc) │
   └─────────┘ └────────┘ └──────────────┘
```

## Related
- [[AI Agents]] — Agent ecosystem overview
- [[OpenCode]] — OpenCode worker agent
- [[Claude Code]] — Claude Code reviewer
- [[JCode]] — jcode AI stack
