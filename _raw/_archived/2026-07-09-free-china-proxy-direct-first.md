---
title: Free China proxy direct-first rule
tags: [proxy, china, owl-agent, network]
summary: Free CN proxies flaky; test direct (401=OK); CN-only pool; soft ban; never global HTTP_PROXY for OAuth CLIs.
project: AI-Second-Brain
capture_source: grok-session
sources:
  - "AI-Second-Brain session (2026-07-09)"
  - "/home/x1/Downloads/@ai/free-china-proxy-research.md"
base_confidence: 0.75
provenance:
  extracted: 0.6
  inferred: 0.4
lifecycle: draft
lifecycle_changed: 2026-07-09
created: 2026-07-09T10:00:20Z
---

# Free China proxy direct-first rule

## Finding
1. Hit China AI hosts **direct** first (200/401 = reachable).
2. Never set system-wide `HTTP_PROXY` for AI CLIs (breaks OAuth).
3. Health-check real API hosts, not only httpbin.
4. Soft-fail free proxies (3 fails → ban); expect 20–40% success.
5. Owl-agent v4.1: china_only_fetch, try_direct_first_for_china.

## Promote
→ [[skills/free-china-proxy-ops]] · [[entities/Owl-Agent]]
