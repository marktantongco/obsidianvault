---
title: Free China Proxy Operations
category: skills
tags: [proxy, china, network, glm, deepseek]
sources:
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - conversation:2026-07-09
summary: Hybrid free China proxy ops for China AI APIs — direct-first, CN-only pool, real-host health (401=OK).
provenance: {extracted: 0.7, inferred: 0.3, ambiguous: 0.0}
base_confidence: 0.65
lifecycle: draft
lifecycle_changed: 2026-07-09
tier: supporting
created: 2026-07-09T09:57:44Z
updated: 2026-07-09T10:44:47Z
relationships:
  - target: "[[entities/Owl-Agent]]"
    type: uses
  - target: "[[entities/SiliconFlow]]"
    type: uses
---

# Free China Proxy Operations

## Context
China AI providers (GLM, MiniMax, DeepSeek, Kimi, SiliconFlow) sometimes need CN egress. Free public China proxies are scarce and flaky.

## Finding / Procedure
1. **Test direct first** — HTTP 200/401 means reachable without proxy.
2. **Never set global HTTP_PROXY** — breaks OAuth Western CLIs.
3. **CN-only pool** — Databay / Geonode CN / ProxyScrape country=cn / Proxifly CN.
4. **Health check real AI hosts** — accept 200/401/403 as success.
5. **Soft ban** — 3 fails before 90s ban; long timeouts (15–45s).
6. **Fallback** direct when pool exhausted.
7. Daily production use → budget $5–12/mo paid CN or HK/SG VPS hop.

## Metrics (free CN, typical)
- Success 20–40%, latency 1.5–10s, uptime often <24h per IP.

## Related
- [[entities/Owl-Agent]]
- [[entities/Zhipu-GLM]]
- [[entities/SiliconFlow]]
- [[concepts/multi-agent-obsidian-wiki-synergy]]

## Session notes (promoted 2026-07-09)

# Free China proxy direct-first rule

## Finding
1. Hit China AI hosts **direct** first (200/401 = reachable).
2. Never set system-wide `HTTP_PROXY` for AI CLIs (breaks OAuth).
3. Health-check real API hosts, not only httpbin.
4. Soft-fail free proxies (3 fails → ban); expect 20–40% success.
5. Owl-agent v4.1: china_only_fetch, try_direct_first_for_china.

## Promote
→ [[skills/free-china-proxy-ops]] · [[entities/Owl-Agent]]
