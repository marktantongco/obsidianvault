---
title: Zhipu-GLM
category: entities
tags:
  - tool
  - ai
  - llm
  - china
  - glm
  - free-tier
sources:
  - conversation:2026-07-09
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - skills/free-china-proxy-ops
summary: >-
  Zhipu AI GLM APIs including permanent free Flash tiers. GLM-4-Flash and
  GLM-4V-Flash offer zero-cost inference with rate limits. Accessible via
  OpenAI-compatible API endpoints. Direct reachable from non-CN networks.
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

# Zhipu-GLM

## Overview

Zhipu AI is a leading China AI company behind the GLM (General Language Model) series. Their key differentiator is **permanent free tiers** on the Flash variants — making them the most cost-effective option for testing and light production workloads in the China AI ecosystem.

## Key Facts

- **Origin**: China (Beijing, founded 2019)
- **API**: OpenAI-compatible (`https://open.bigmodel.cn/api/paas/v4`)
- **Free models**: GLM-4-Flash (text), GLM-4V-Flash (vision) — **permanently free**
- **Paid models**: GLM-4, GLM-4-Plus, GLM-4-AllTools, GLM-4V
- **Reachability**: Direct reachable from non-CN networks in most cases
- **Proxy strategy**: Direct-first per [[skills/free-china-proxy-ops]]

## Free Tier Details

| Model | Type | Rate Limit | Cost |
|-------|------|-----------|------|
| GLM-4-Flash | Text (128K context) | 100 RPM | **Free** |
| GLM-4V-Flash | Vision (8K context) | 100 RPM | **Free** |
| GLM-4 | Text (128K) | Pay-per-token | Paid |
| GLM-4-Plus | Enhanced text | Pay-per-token | Paid |

## Related

- [[skills/free-china-proxy-ops]] — Proxy operations for China AI APIs
- [[entities/DeepSeek]] — China LLM provider with competitive pricing
- [[entities/SiliconFlow]] — China AI inference hub with free small models
- [[entities/Owl-Agent]] — Proxy client for CN pool routing
