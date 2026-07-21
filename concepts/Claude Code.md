---
title: Claude Code
tags: [claude, anthropic, coding]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: core
---

# Claude Code

## Overview
Claude Code is an agentic coding tool from Anthropic that lives in your terminal, understands your codebase, and helps you code faster.

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

## Features
- Executes routine tasks
- Explains complex code
- Handles git workflows
- Natural language commands
- IDE integration (VS Code, Cursor, Windsurf)
- GitHub integration (@claude)

## Usage
```bash
# Start interactive mode
claude

# Check version
claude --version

# Login
claude login
```

## Configuration
API key stored in: `~/.claude/.env`

## Related
- [[AI Agents]]
- [[OpenCode]]
- [[Development Workflow]]
