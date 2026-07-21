---
title: ai-wanderer (ai-free-swap)
category: entities
tags:
  - tool
  - ai
  - proxy
  - free-tier
  - router
sources:
  - conversation:2026-07-14
  - journal/2026-07-14-system-admin-tool-installs
summary: >-
  Free-tier proxy router (v0.2.0) installed via pipx from
  github.com/sshnaidm/ai-wanderer. OpenAI/Anthropic-compatible endpoint with
  automatic provider fallback between free tiers. Command: ai-free-swap.
  Configured as secondary fallback behind FreeHive gateway.
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.8
lifecycle: draft
tier: peripheral
created: 2026-07-14
updated: 2026-07-21
---

# ai-wanderer (ai-free-swap)

## Overview

ai-wanderer (command: `ai-free-swap`) is a free-tier proxy router that provides an OpenAI/Anthropic-compatible API endpoint with automatic provider fallback. It sits between AI agents and multiple free-tier AI providers, routing requests to whichever provider has available quota.

On this system, it is configured as a **secondary fallback** behind the primary [[concepts/FreeHive|FreeHive AI Gateway]].

## Key Facts

| Property | Value |
|----------|-------|
| **Package** | `ai-wanderer` (`github.com/sshnaidm/ai-wanderer`) |
| **Version** | v0.2.0 |
| **Install method** | `pipx install ai-wanderer` (from GitHub) |
| **Command** | `ai-free-swap` |
| **API compatibility** | OpenAI + Anthropic |
| **Strategy** | Automatic provider fallback between free tiers |
| **Role** | Fallback router behind FreeHive (primary) |

## Architecture

```
AI Agent (OpenCode, Claude, etc.)
        │
        ▼
  FreeHive Gateway (:7200)        ← Primary
        │
        ▼
  ai-wanderer (ai-free-swap)      ← Fallback
        │
        ▼
  Free-tier AI Providers
  (OpenAI free, Gemini free,
   Claude free, etc.)
```

## Related

- [[concepts/FreeHive]] — Primary AI gateway on this system
- [[concepts/OpenCode]] — Agent configured to use FreeHive + ai-wanderer
- [[journal/2026-07-14-system-admin-tool-installs]] — Installation session
