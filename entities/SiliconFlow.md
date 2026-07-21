---
title: SiliconFlow
category: entities
tags:
  - tool
  - ai
  - inference
  - china
  - free-tier
sources:
  - conversation:2026-07-09
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - skills/free-china-proxy-ops
summary: >-
  China AI inference hub with free small models and OpenAI-compatible API.
  Offers hosted access to dozens of open-source models (Qwen, LLaMA, GLM,
  etc.) with a free tier for light usage. Reachable direct from non-CN networks
  in most cases.
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

# SiliconFlow

## Overview

SiliconFlow is a China-based AI inference hub providing hosted access to a broad catalog of open-source models. It exposes an OpenAI-compatible API, making it a drop-in replacement for OpenAI clients. The free tier offers limited access to smaller models, making it useful for testing and light workloads.

## Key Facts

- **Origin**: China
- **API**: OpenAI-compatible (`https://api.siliconflow.cn/v1`)
- **Free tier**: Yes — limited access to small open-source models
- **Models hosted**: Qwen series, LLaMA variants, GLM series, Yi, DeepSeek, and 50+ others
- **Reachability**: Generally reachable direct from non-CN networks
- **Proxy strategy**: Direct-first per [[skills/free-china-proxy-ops]]

## Related

- [[skills/free-china-proxy-ops]] — Proxy operations for China AI APIs
- [[entities/DeepSeek]] — China LLM provider
- [[entities/Zhipu-GLM]] — Zhipu AI GLM APIs with free Flash tiers
- [[entities/Owl-Agent]] — Proxy client for CN pool routing
