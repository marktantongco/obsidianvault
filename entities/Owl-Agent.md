---
title: Owl-Agent
category: entities
tags:
  - tool
  - ai
  - proxy
  - china
  - network
  - scraping
  - http-client
sources:
  - conversation:2026-07-09
  - conversation:2026-07-23
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - skills/free-china-proxy-ops
  - ~/.owl-agent/DOCUMENTATION.md
  - ~/.owl-agent/proxy_defense.py
summary: >-
  Self-optimising HTTP scraping engine v4.2 with 50+ proxy sources, quality scoring,
  adaptive rate limiting, Redis state sharing, curl_cffi Chrome fingerprinting, and
  headless browser automation. Installed at ~/.owl-agent with CLI, Python API, MCP server,
  and integrations for OpenCode, Cline, Cursor, Warp, Claude Code, and Codex.
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.85
lifecycle: active
tier: core
created: 2026-07-09T09:57:44Z
updated: 2026-07-23T06:45:00Z
---

# Owl-Agent

## Overview

Owl-Agent is a **production-grade, self-optimising HTTP client** that combines 50+ proxy sources, quality scoring, adaptive rate limiting, Redis state sharing, curl_cffi Chrome fingerprinting, and agent-browser automation into a single, memory-efficient script.

**Location:** `~/.owl-agent/`  
**Version:** 4.2  
**License:** MIT

## Quick Start

```bash
# Test connection
~/.owl-agent/run.sh test

# Show proxy pool stats
~/.owl-agent/run.sh stats

# Fetch URL (direct)
~/.owl-agent/run.sh fetch https://api.github.com/users/octocat

# Fetch URL (via proxy)
~/.owl-agent/run.sh fetch --proxy https://httpbin.org/get
```

## Key Features (v4.2)

### Core Engine
- **Quality Scoring** — Weighted metrics for optimal proxy selection
- **Adaptive Rate Limiting** — Dynamic per-domain request adjustment
- **Circuit Breaker** — Stops hammering dead endpoints
- **LRU Cache** — Memory + disk persistence
- **Request Deduplication** — In-flight coalescing

### Fingerprint & Stealth
- **curl_cffi Chrome 110** — TLS handshake bypass
- **Retry-After Parsing** — Polite backoff compliance
- **Headless Browser** — JavaScript SPA rendering via agent-browser

### Proxy Management
- **ProxyBroker2** — 50+ sources with country filtering
- **Quality Scoring** — Picks best proxy for each target
- **Health Checks** — Automatic ban/recovery cycle

### Integrations
| Tool | Integration |
|------|-------------|
| [[concepts/OpenCode\|OpenCode]] | `~/.owl-agent/owl-agent.skill.json` |
| Cline (MCP) | `~/.owl-agent/mcp-server.py` |
| Cursor | `~/.owl-agent/commands.json` |
| Warp | `~/.owl-agent/warp-agent.yaml` |
| [[concepts/Claude Code\|Claude Code]] | `~/.claude/skills/owl-agent/` |
| Codex | CLI alias via `~/.owl-agent/run.sh` |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER LAYER                           │
│  OpenCode | Cline | Cursor | Warp | Claude Code | Codex│
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                 UNIFIED API INTERFACE                   │
│  CLI (run.sh) | Python Class | MCP Server | HTTP API   │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│               RESILIENT CLIENT CORE                    │
│  Cache │ Dedup │ Limiter │ Scorer │ Breaker │ Proxy   │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│              EXTERNAL DEPENDENCIES                     │
│  ProxyBroker2 | curl_cffi | httpx | aiohttp | Redis    │
└─────────────────────────────────────────────────────────┘
```

## Installation Status

Per [[SYSTEM-INSTALLATION-STATUS]]:

| Component | Status |
|-----------|--------|
| Core Script | ✅ Installed (`proxy_defense.py`) |
| CLI Wrapper | ✅ Installed (`run.sh`) |
| MCP Server | ✅ Installed (`mcp-server.py`) |
| OpenCode Skill | ✅ Installed |
| Cursor Commands | ✅ Installed |
| Warp Agent | ✅ Installed |
| Proxy Pool | ✅ 50 proxies loaded |
| Memory Optimized | ✅ 50% reduction applied |

## Commands

| Command | Description |
|---------|-------------|
| `~/.owl-agent/run.sh stats` | Show proxy pool statistics |
| `~/.owl-agent/run.sh test` | Test GitHub API connection |
| `~/.owl-agent/run.sh fetch <url>` | Fetch URL (direct connection) |
| `~/.owl-agent/run.sh fetch --proxy <url>` | Fetch URL (via proxy pool) |
| `~/.owl-agent/run.sh serve` | Start HTTP API server (port 8420) |
| `~/.owl-agent/run.sh help` | Show all commands |
| `~/.owl-agent/test_all.sh` | Run complete test suite |

## Python API

```python
from proxy_defense import ResilientClient

async with ResilientClient(
    use_curl_cffi=True,      # Chrome fingerprint
    countries=["US", "GB"],   # Country filter
    use_redis=True,           # State persistence
    cache_ttl=600,            # 10 min cache
    rate_limit=2.0,           # 2 req/s
) as client:
    resp = await client.request("GET", "https://api.github.com/users/octocat")
    print(f"Status: {resp.status}")
```

## Memory Optimization

Applied optimizations (v4.2):

| Setting | Before | After |
|---------|--------|-------|
| MAX_PROXY_CACHE | 100 | 50 |
| MAX_QUEUE_SIZE | 50 | 20 |
| MAX_CACHED_RESPONSES | 1000 | 500 |
| MAX_SCORE_HISTORY | 100 | 50 |
| CLEANUP_INTERVAL | 60s | 30s |

## Related

- [[skills/free-china-proxy-ops]] — China proxy operations skill
- [[SYSTEM-INSTALLATION-STATUS]] — System installation status
- [[entities/DeepSeek]] — China LLM provider
- [[entities/SiliconFlow]] — China AI inference hub
- [[entities/Zhipu-GLM]] — Zhipu AI GLM APIs
- [[concepts/MiMo Code]] — MiMoCode agent
- [[concepts/OpenCode]] — OpenCode CLI
- [[concepts/Claude Code]] — Claude Code agent
- [[concepts/MCP Servers]] — MCP server integration
- [[concepts/multi-agent-obsidian-wiki-synergy]] — Multi-agent vault wiring

## See Also

- `~/.owl-agent/README.md` — Quick start guide
- `~/.owl-agent/DOCUMENTATION.md` — Full documentation
- `~/.owl-agent/SUMMARY.md` — Setup summary
- `~/.owl-agent/mock_demo.py` — Interactive demo
