---
title: Claude Code
tags: [claude, anthropic, coding, cli]
type: concept
created: 2026-07-09
updated: 2026-07-24
lifecycle: verified
tier: core
source: project
---

# Claude Code

## Overview

Claude Code is an agentic coding tool from Anthropic that lives in your terminal, understands your codebase, and helps you code faster. It integrates with IDEs, GitHub, and can be bridged with other agents.

## Version
v2.1.205

## Installation
```bash
npm install -g @anthropic-ai/claude-code
```

## Location
- Binary: `~/.local/bin/claude`
- Config: `~/.claude/`
- Skills: `~/.claude/skills/` (37 skills)
- Agent Bridge: `~/.claude/agentic` → `~/ai-workspace/.agent/`
- Auth: `~/.claude/.env` (ANTHROPIC_API_KEY)

## Features
- **Task execution**: Runs routine coding tasks autonomously
- **Code explanation**: Explains complex codebases
- **Git workflows**: Manages branches, commits, PRs
- **Natural language**: Full NL command interface
- **IDE integration**: VS Code, Cursor, Windsurf
- **GitHub integration**: `@claude` in PRs/issues
- **Skills system**: 37 skills for enhanced capabilities

## Usage

```bash
# Interactive mode
claude

# One-shot prompt
claude -p "Explain this function"

# Review code
claude "Review this PR for security issues"

# Check version
claude --version

# Login (OAuth)
claude login
```

## Skills Integration
Skills are shared across agents via `~/.agents/skills/` and include:
- Wiki knowledge management
- Code review automation
- Research and web search
- Design and blueprint creation

## Bridge Integration
- **Hermes-Claude Bridge**: `~/.hermes/plugins/code-bridge/`
  - Enables Hermes orchestration of Claude Code
  - Task delegation from Hermes to Claude
  - Cross-agent handoff

## Configuration
API key stored in `~/.claude/.env`:
```
ANTHROPIC_API_KEY=sk-ant-...
```

## Related
- [[AI Agents]] — Agent ecosystem overview
- [[Hermes Agent]] — Hermes orchestration
- [[OpenCode]] — OpenCode worker agent
- [[JCode]] — jcode AI stack
