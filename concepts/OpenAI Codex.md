---
tags: [codex, openai, coding]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: supporting
---

# OpenAI Codex

## Overview
Codex CLI is a lightweight coding agent from OpenAI that runs locally on your computer.

## Version
v0.143.0

## Installation
```bash
# npm
npm install -g @openai/codex

# Homebrew
brew install --cask codex

# Official script
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

## Location
- Binary: `~/.local/bin/codex`
- Config: `~/.codex/`

## Features
- Lightweight terminal-based agent
- ChatGPT integration
- Multiple model support
- Desktop app available

## Usage
```bash
# Start interactive mode
codex

# Check version
codex --version
```

## Related
- [[AI Agents]]
- [[OpenCode]]
