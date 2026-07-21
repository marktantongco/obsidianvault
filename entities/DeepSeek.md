---
title: DeepSeek
category: entities
tags:
  - tool
  - ai
  - llm
  - china
  - proxy
sources:
  - conversation:2026-07-09
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - skills/free-china-proxy-ops
summary: >-
  China LLM provider with competitive API pricing and international reach.
  DeepSeek-V2/V3 and DeepSeek-R1 models available via API. Direct access is
  generally reachable from non-CN networks (HTTP 200/401 = reachable without
  proxy). Fallback through CN proxy pool when needed.
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

# DeepSeek

## Overview

DeepSeek is a China-based LLM provider known for competitive API pricing and international reach. Offers the DeepSeek-V2/V3 chat models and DeepSeek-R1 reasoning model.

## Key Facts

- **Origin**: China (Hangzhou)
- **API**: OpenAI-compatible chat completions endpoint
- **Pricing**: ~$0.14/1M input tokens (DeepSeek-V2), significantly cheaper than GPT-4
- **Reachability**: Generally reachable direct from non-CN networks
- **Proxy strategy**: Direct-first — test `api.deepseek.com` before routing through CN proxy pool

## Proxy Behavior

Per [[skills/free-china-proxy-ops|Free China Proxy Operations]]:

1. **Test direct first** — HTTP 200/401/403 = reachable without proxy
2. **CN-only proxy pool** — Databay, Geonode CN, ProxyScrape `country=cn`, Proxifly CN
3. **Soft ban** — 3 fails before 90s ban; 15–45s timeouts
4. **Fallback** direct when pool exhausted

## Related

- [[skills/free-china-proxy-ops]] — Proxy operations for China AI APIs
- [[entities/SiliconFlow]] — China AI inference hub
- [[entities/Zhipu-GLM]] — Zhipu AI GLM APIs with free Flash tiers
- [[entities/Owl-Agent]] — Proxy client for CN pool routing
- [[concepts/multi-agent-obsidian-wiki-synergy]]
