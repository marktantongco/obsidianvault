---
tags: [mimo, xiaomi, coding]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: supporting
---

# MiMo Code

## Overview
MiMo Code is an AI-powered coding assistant developed by Xiaomi, available as a CLI tool in the terminal.

## Version
v0.1.5

## Installation
```bash
# Official script (macOS/Linux)
curl -fsSL https://mimo.xiaomi.com/install | bash

# npm (Windows)
npm install -g @mimo-ai/cli
```

## Location
- Binary: `~/.local/bin/mimo`
- Config: `~/.config/mimo/`

## Features
- Direct redirection to Xiaomi MiMo API Platform
- Pay-as-you-go MiMo API support
- Token Plan subscription
- 1000 free web search queries per day

## Usage
```bash
# Check version
mimo --version

# Start interactive mode
mimo

# Authenticate
mimo auth login
```

## Related
- [[AI Agents]]
- [[OpenCode]]
