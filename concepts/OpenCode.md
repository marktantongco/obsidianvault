---
tags: [opencode, coding, cli]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: core
---

# OpenCode

## Overview
OpenCode is a powerful terminal-based AI coding agent. Built for the terminal.

## Version
v1.17.15

## Installation
```bash
curl -fsSL https://opencode.ai/install | bash
```

## Location
- Binary: `~/.opencode/bin/opencode`
- Config: `~/opencode.json`
- Skills: `~/.opencode/skills/` (37 skills)

## Features
- Interactive TUI with Bubble Tea
- Multiple AI provider support
- Session management
- Tool integration (file access, shell, web search)
- LSP integration
- File change tracking

## Usage
```bash
# Start interactive mode
opencode

# Start with specific directory
opencode -c /path/to/project

# Non-interactive prompt
opencode -p "Explain this code"
```

## Configuration
```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["AGENTS.md", ".agent/AGENTS.md"]
}
```

## Related
- [[AI Agents]]
- [[Claude Code]]
- [[Development Workflow]]
