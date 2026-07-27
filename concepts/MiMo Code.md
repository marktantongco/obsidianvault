---
title: MiMo Code
tags: [mimo, xiaomi, coding, cli]
type: concept
created: 2026-07-09
updated: 2026-07-24
lifecycle: verified
tier: supporting
source: project
---

# MiMo Code

## Overview

MiMo Code is an AI-powered coding assistant developed by Xiaomi, available as a CLI tool. It connects to the Xiaomi MiMo API platform with pay-as-you-go and token plan options.

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
- Proxy: `~/mimo-unified-proxy.py` (unified proxy on port :8877)

## Features
- **Direct API**: Connects to Xiaomi MiMo API Platform
- **Pay-as-you-go**: MiMo API usage-based billing
- **Token Plan**: Subscription-based token plans
- **Free Web Search**: 1000 free web search queries per day
- **Unified Proxy**: Can be routed through mimo-unified-proxy on `:8877`

## Usage

```bash
# Check version
mimo --version

# Start interactive mode
mimo

# Authenticate
mimo auth login

# One-shot prompt
mimo -p "Write a Python function"
```

## Proxy Integration

MIMO can be used through the unified proxy stack:

```bash
# Start the mimo-unified proxy
./freebuff.sh start mimo-unified

# The proxy runs on port 8877
# Routes requests to Xiaomi MiMo API
```

## Configuration

API keys are stored in `~/.opencode/.env`, `~/.claude/.env`, and `~/.hermes/hermes-agent/.env`:
```
MIMO_API_KEY=sk-...
```

## Related
- [[Freebuff]] — Proxy manager that includes mimo-unified
- [[AI Agents]] — Agent ecosystem overview
- [[OpenCode]] — OpenCode CLI agent
