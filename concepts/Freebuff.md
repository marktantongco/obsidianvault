---
title: Freebuff
tags: [freebuff, proxy, manager, gateway]
type: concept
created: 2026-07-24
updated: 2026-07-24
lifecycle: verified
tier: core
source: project
---

# Freebuff

## Overview

Freebuff is a **unified proxy manager** that orchestrates multiple AI proxy services on the local machine. It manages the lifecycle (start, stop, build, test, smoke) of proxy bridges that connect AI clients to upstream providers.

Freebuff is the central nervous system for local AI routing — it ensures clients like Claude Code, OpenCode, jcode, and MIMO can reach their AI providers through the right proxy.

## Services Managed

| Service | Port | Type | Purpose |
|---------|------|------|---------|
| **codebuff-proxy** | `:3211` | Convex/Bun | Modern proxy with Convex backend |
| **Freebuff2API** | `:8080` | Go API Gateway | OpenAI-compatible API aggregator |
| **freebuff-proxy-ff** | `:1455` | Go Proxy | Ferdiunal's lightweight Go proxy |
| **mimo-unified** | `:8877` | Python | Unified proxy for MIMO ecosystem |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENTS                               │
│  OpenCode · Claude Code · jcode · MIMO · Codex          │
└──────────┬──────────┬──────────┬──────────┬─────────────┘
           │          │          │          │
           ▼          ▼          ▼          ▼
     ┌─────────┐ ┌────────┐ ┌────────┐ ┌──────────┐
     │codebuff │ │Freebuff│ │freebuff│ │mimo-     │
     │-proxy   │ │2API    │ │-proxy  │ │unified   │
     │:3211    │ │:8080   │ │:1455   │ │:8877     │
     └────┬────┘ └───┬────┘ └───┬────┘ └─────┬────┘
          │          │          │             │
          └──────────┴──────────┴─────────────┘
                         │
                         ▼
                ┌────────────────┐
                │  AI Providers   │
                │ OpenAI/Claude   │
                │ Gemini/MiMo/etc │
                └────────────────┘
```

## Management Script

The `freebuff.sh` script at the project root manages all proxies:

```bash
# Start all proxies
./freebuff.sh start all

# Start a specific proxy
./freebuff.sh start codebuff-proxy

# Check status of all proxies
./freebuff.sh status

# Stop all proxies
./freebuff.sh stop all

# Smoke test all endpoints
./freebuff.sh smoke

# View logs
./freebuff.sh logs codebuff-proxy
```

## Proxy Details

### codebuff-proxy (`:3211`)
- **Runtime**: Bun (JavaScript/TypeScript)
- **Backend**: Convex for state management
- **Project**: `~/codebuff-proxy/`
- **Logs**: `~/codebuff-proxy/logs/convex.log`

### Freebuff2API (`:8080`)
- **Runtime**: Go (compiled binary)
- **Config**: `~/Freebuff2API/config.json`
- **Logs**: `~/Freebuff2API/server.log`
- **Features**: API key management, provider routing, rate limiting

### freebuff-proxy-ff (`:1455`)
- **Runtime**: Go (compiled binary)
- **Config**: `~/freebuff-proxy/config.json`
- **Logs**: `~/freebuff-proxy/server.log`
- **Source**: `~/freebuff-proxy/cmd/freebuff-proxy/`

### mimo-unified (`:8877`)
- **Runtime**: Python 3
- **Script**: `~/mimo-unified-proxy.py` (also v2 variant)
- **Logs**: `/tmp/mimo-unified.log`

## Quick Start

```bash
# 1. Start all proxy services
./freebuff.sh start all
# Waits 15s then runs smoke tests

# 2. Check everything is running
./freebuff.sh status
# codebuff-proxy  🟢 :3211
# Freebuff2API    🟢 :8080
# freebuff-proxy  🟢 :1455
# mimo-unified    🟢 :8877

# 3. Use any proxy as OpenAI-compatible endpoint
export OPENAI_BASE_URL=http://localhost:3211
export OPENAI_API_KEY=your-key
```

## Related
- [[JCode]] — The jcode ecosystem (daemon, proxy, web dashboard)
- [[MiMo Code]] — MIMO CLI tool
- [[OpenCode]] — OpenCode CLI agent
