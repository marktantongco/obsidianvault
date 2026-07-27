---
title: JCode
tags: [jcode, daemon, proxy, web, coding-agent]
type: concept
created: 2026-07-24
updated: 2026-07-24
lifecycle: verified
tier: core
source: project
---

# JCode

## Overview

JCode is a three-tier AI coding agent stack consisting of a **daemon** (AI agent backend), a **proxy** (OpenAI-compatible API bridge), and a **web dashboard** for monitoring. It provides a local, self-hosted AI coding experience.

## Architecture

```
┌──────────────┐    ┌────────────────┐    ┌──────────────┐    ┌─────────────┐
│    Client    │───▶│  jcode-proxy   │───▶│ jcode-daemon  │───▶│ AI Providers │
│ (CLI/curl)   │    │   :8088        │    │   :1456       │    │ OpenAI/etc   │
└──────────────┘    └────────────────┘    └──────────────┘    └─────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  jcode-web   │
                    │  Dashboard   │
                    │   :3456       │
                    └──────────────┘
```

## Components

### 1. jcode-daemon (`:1456`)

The core AI agent service. Runs the `jcode` binary in server mode with a TCP gateway for HTTP access.

- **Binary**: `~/.local/bin/jcode` (symlink to `jcode-linux-x86_64.bin`)
- **Version**: `v0.55.0` (ece08710)
- **Config**: `~/.jcode/config.toml`
- **Socket**: Uses `/run/user/1000/jcode.sock` (Unix socket for CLI)
- **Gateway**: TCP on `127.0.0.1:1456` (enabled via `[gateway]` config)
- **Providers**: openai, openai-compatible, anthropic, gemini, opencode, opencode-go, and more

```bash
# Start the daemon
jcode serve

# Stop the daemon
jcode server stop

# Run a one-shot command
jcode --provider openai-compatible run "your prompt"

# Interactive mode
jcode
```

### 2. jcode-proxy (`:8088`)

An OpenAI-compatible API translation proxy written in Go. It sits between clients and the jcode-daemon, providing a standard OpenAI API interface.

- **Source**: `~/jcode-proxy/main.go`
- **Config**: `~/jcode-proxy/config.json`
- **Binary**: `~/jcode-proxy/jcode-proxy`
- **Port**: `:8088`

```json
{
  "listen_addr": ":8088",
  "upstream_url": "http://127.0.0.1:1456",
  "default_model": "jcode-default",
  "allowed_models": ["jcode-default", "gpt-4o", "claude-3-opus", "gemini-2.0-flash"],
  "api_keys": [],
  "provider_keys": {},
  "log_level": "info"
}
```

**Endpoints**:
- `POST /v1/chat/completions` — Chat completions
- `GET /v1/models` — List available models
- `GET /health` — Health check

```bash
curl http://localhost:8088/health
# {"status":"healthy","version":"1.0.0","uptime":"1m","upstream":"http://127.0.0.1:1456"}

curl http://localhost:8088/v1/models
# Lists available models
```

### 3. jcode-web (`:3456`)

A Next.js dashboard for monitoring all jcode services.

- **Source**: `~/jcode-web/`
- **Framework**: Next.js with TypeScript, Tailwind CSS
- **Features**:
  - Real-time service status (daemon + proxy)
  - System metrics and uptime
  - Proxy configuration viewer
  - Quick command reference
  - Architecture flow diagram

## Management

Use the `jcode.sh` management script:

```bash
# Start all services
./jcode.sh start all

# Status check
./jcode.sh status

# View logs
./jcode.sh logs jcode-daemon

# Smoke test
./jcode.sh smoke
```

## Provider Configuration

### OpenAI API (via API key)
```bash
jcode login --provider openai-compatible --api-key "sk-..." --api-base "https://api.openai.com/v1"
```
Key stored at: `~/.config/jcode/openai-compatible.env`

### OpenCode Zen
```bash
jcode login --provider opencode
```
Key stored at: `~/.config/jcode/opencode.env`

### OpenCode Go
```bash
jcode login --provider opencode-go
```
Key stored at: `~/.config/jcode/opencode-go.env`

## Config File (`~/.jcode/config.toml`)

Key configuration sections:

| Section | Purpose |
|---------|---------|
| `[gateway]` | TCP listener config (port, bind_addr) |
| `[provider]` | Model settings, failover, timeouts |
| `[providers]` | Provider-specific overrides |
| `[auth]` | External auth sources (e.g., Codex auth) |
| `[agents]` | Swarm agent behavior |
| `[websearch]` | Search engine config |
| `[features]` | Memory, swarm, mermaid toggles |

## Related
- [[Freebuff]] — Proxy manager ecosystem
- [[OpenCode]] — OpenCode CLI agent
- [[MiMo Code]] — MIMO CLI tool
