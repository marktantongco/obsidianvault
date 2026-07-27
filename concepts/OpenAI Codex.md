---
title: OpenAI Codex
tags: [codex, openai, coding, cli]
type: concept
created: 2026-07-09
updated: 2026-07-24
lifecycle: verified
tier: supporting
source: project
---

# OpenAI Codex

## Overview

Codex CLI is a lightweight coding agent from OpenAI that runs locally on your computer. It integrates with ChatGPT and supports multiple models for code generation and assistance.

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
- Auth: `~/.codex/auth.json`
- Env: `~/.codex/.env`

## Features
- **Lightweight**: Minimal terminal-based agent
- **ChatGPT Integration**: Authenticated via OAuth with ChatGPT
- **Multiple Models**: GPT-4o, GPT-4, GPT-3.5-turbo
- **Desktop App**: Available for GUI usage
- **Auth Sharing**: jcode can reuse Codex auth via `trusted_external_sources` config

## Authentication

### OAuth (ChatGPT)
```bash
codex login
# Opens browser for ChatGPT authentication
```

### API Key
```bash
# Store key in ~/.codex/.env
echo "OPENAI_API_KEY=sk-..." >> ~/.codex/.env
```

## Auth File (`~/.codex/auth.json`)
```json
{
  "auth_mode": "apikey",
  "OPENAI_API_KEY": "sk-proj-..."
}
```

jcode can use this auth file directly via its `[auth]` config:
```toml
[auth]
trusted_external_source_paths = ["openai_codex_auth_json|/home/ubuntu/.codex/auth.json"]
```

## Usage

```bash
# Start interactive mode
codex

# Check version
codex --version

# One-shot prompt
codex -p "Write a React component"
```

## Integration with jcode
Codex's OpenAI API key can be shared with jcode through the external auth source mechanism, allowing jcode to use the same key without duplicating configuration.

## Related
- [[AI Agents]] — Agent ecosystem overview
- [[JCode]] — jcode can reuse Codex auth
- [[OpenCode]] — OpenCode CLI agent
