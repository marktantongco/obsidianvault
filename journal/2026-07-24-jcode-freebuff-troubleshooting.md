---
title: JCode and Freebuff Troubleshooting Session
category: journal
tags: [troubleshooting, jcode, freebuff, proxy, rate-limit, html-fix]
sources:
  - session:2026-07-24
created: 2026-07-24T20:54:00.000Z
updated: 2026-07-24T20:54:00.000Z
summary: >-
  Troubleshooting session covering jcode 429 rate limits from OpenCode Zen, duplicate HTML div tags in kiro-proxy-ecosystem, and freebuff service launch failures.
provenance:
  extracted: 0.7
  inferred: 0.3
  ambiguous: 0.0
base_confidence: 0.75
lifecycle: draft
lifecycle_changed: 2026-07-24
---

# JCode and Freebuff Troubleshooting Session

*Session captured: 2026-07-24*

## Topics Covered

1. JCode connection issues (429 rate limits)
2. HTML duplicate div tag fix in kiro-proxy-ecosystem
3. Freebuff service launch failures

## Key Takeaways

### JCode Rate Limits (429 Errors)

JCode v0.56.0 configured with `default_provider = "openai-compatible"` hitting OpenCode Zen API directly. Free models (mimo-v2.5-free, laguna-s-2.1-free) experiencing rate limits:

```
endpoint: https://opencode.ai/zen/v1/chat/completions
status: 429 Too Many Requests
response: {"error":{"message":"Error from provider (Console): Provider rate limit exceeded"}}
```

**Root Cause**: OpenCode Zen applies rate limits on free-tier models. The `[providers]` section in `~/.jcode/config.toml` is empty — no alternative providers configured.

**Resolution Options**:
- Wait for rate limit reset (typically 1-24 hours)
- Configure alternative provider (e.g., local proxy on port 8877)
- Use paid models that bypass free-tier limits

### HTML Duplicate Div Tag Fix

Found duplicate `<div class="arch-svg-container">` tags in `/home/ubuntu/ai-workspace/kiro-proxy-ecosystem/index.html`:

```html
<!-- Lines 625-626 (before fix) -->
<div class="arch-svg-container">
<div class="arch-svg-container">
    <svg width="950" height="480" viewBox="0 0 950 480"...>
```

**Fix Applied**: Removed duplicate opening tag. Div count balanced (62 opening, 62 closing).

### Freebuff Service Status

| Service | Port | Status |
|---------|------|--------|
| codebuff-proxy | 3211 | NOT RUNNING |
| Freebuff2API | 8080 | RUNNING (PID 2084) |
| freebuff-proxy | 1455 | NOT RUNNING |
| jcode-daemon | 1456 | NOT RUNNING |
| jcode-proxy | 8088 | RUNNING (PID 2390) |
| mimo-unified | 8877 | NOT RUNNING |

**Freebuff2API Config** (`/home/ubuntu/ai-workspace/Freebuff2API/config.json`):
- Listen address: `:8080`
- Upstream: `https://www.codebuff.com`
- Request timeout: 15 minutes
- Auth tokens configured

## Decisions Made

- Fixed duplicate HTML div tags to resolve page rendering issues
- Diagnosed jcode rate limit issue as OpenCode Zen free-tier limitation

## Open Questions

- How to configure jcode to use local proxy (port 8877) instead of direct OpenCode Zen connection
- Why freebuff-proxy (port 1455) and codebuff-proxy (port 3211) fail to start
- Rate limit reset schedule for OpenCode Zen free models

## Related

- [[concepts/Freebuff|Freebuff]] — Unified proxy manager
- [[concepts/JCode|JCode]] — jcode ecosystem
- [[concepts/OpenCode|OpenCode]] — Terminal AI coding agent
- [[TROUBLESHOOTING|Troubleshooting]] — Common issues and solutions
- [[ERROR-LOG|Error Log]] — Recorded errors
