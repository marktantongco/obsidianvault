---
title: Owl-Agent
category: entities
tags:
  - tool
  - ai
  - proxy
  - china
  - network
sources:
  - conversation:2026-07-09
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - skills/free-china-proxy-ops
summary: >-
  Resilient proxy client installed at ~/.owl-agent with a China-only proxy
  pool and RequestsWrapper. Provides try_direct_first_for_china and
  china_only_fetch modes. Designed to route AI API traffic to China-based
  providers (DeepSeek, Zhipu, SiliconFlow, MiniMax, Kimi) with automatic
  failover between direct and proxied connections.
provenance:
  extracted: 0.7
  inferred: 0.3
  ambiguous: 0.0
base_confidence: 0.65
lifecycle: draft
tier: supporting
created: 2026-07-09T09:57:44Z
updated: 2026-07-21T08:00:00Z
---

# Owl-Agent

## Overview

Owl-Agent is a resilient proxy client designed to route traffic to China-based AI providers through a curated China-only proxy pool. It implements the direct-first strategy defined in [[skills/free-china-proxy-ops]].

## Key Features (v4.1)

- **`china_only_fetch`** — Routes requests only through CN-proxied connections
- **`try_direct_first_for_china`** — Tests direct connection before using proxy pool
- **`RequestsWrapper`** — Transparent HTTP client with automatic proxy fallback

## Architecture

```
AI Client App
      │
      ▼
  Owl-Agent (RequestsWrapper)
      │
      ├── Direct → API Host (200/401/403 = reachable)
      │
      └── CN Proxy Pool
            ├── Databay (free)
            ├── Geonode CN (free)
            ├── ProxyScrape country=cn (free)
            └── Proxifly CN (free)
                  │
                  └── Health checks: accept 200/401/403 as success
```

## Proxy Pool Details

Per [[skills/free-china-proxy-ops]]:

- **Sources**: Databay, Geonode CN, ProxyScrape `country=cn`, Proxifly CN
- **Health check**: Accept HTTP 200/401/403 as success against real AI API hosts
- **Soft ban**: 3 failures → 90s ban
- **Timeouts**: 15–45s (long due to CN egress latency)
- **Fallback**: Direct when pool exhausted
- **Performance**: ~20–40% success rate, 1.5–10s latency, <24h uptime per free IP
- **Production recommendation**: Budget $5–12/mo for paid CN proxies or HK/SG VPS hop

## Related

- [[skills/free-china-proxy-ops]] — Proxy operations skill page
- [[entities/DeepSeek]] — China LLM provider
- [[entities/SiliconFlow]] — China AI inference hub
- [[entities/Zhipu-GLM]] — Zhipu AI GLM APIs
- [[concepts/multi-agent-obsidian-wiki-synergy]]
