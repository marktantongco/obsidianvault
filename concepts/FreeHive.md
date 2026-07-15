---
title: >-
  FreeHive AI Gateway
category: concepts
tags:
  - ai
  - gateway
  - proxy
  - free-ai
sources:
  - "default project session (2026-07-14)"
created: 2026-07-14
updated: 2026-07-14
summary: >-
  FreeHive is a local AI gateway backend that routes requests to multiple AI providers (Claude, ChatGPT, Gemini, etc.) through OAuth-based authentication, running as a systemd user service on port 7200.
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.8
lifecycle: draft
lifecycle_changed: 2026-07-14
tier: supporting
---

# FreeHive AI Gateway

FreeHive is a local AI provider gateway that routes requests to multiple AI backends with automatic failover between providers.

## How It Works

FreeHive runs as a systemd user service and exposes an OpenAI-compatible API at `http://127.0.0.1:7200`. It acts as a middleware layer that:

1. Accepts requests in standard format (Anthropic Messages API or OpenAI Chat API)
2. Routes to the best available provider based on health checks
3. Cascades through provider strategies if one fails (direct_oauth → ...)
4. Returns responses in the expected format

## Auth Model

FreeHive authenticates via OAuth tokens from the AI providers themselves:

- **Claude**: needs `claude login` to produce a valid OAuth session — detected by FreeHive's `cli_introspection` module
- **ChatGPT CLI**: registered as `chatgpt_cli` provider
- Without auth, the backend returns 401/503

Health status is tracked per-provider with live probes.

## Provider Config

When used with OpenCode, two providers are configured:
- `freehive` — Anthropic-compatible endpoint (for Claude SDK clients)
- `freehive-oai` — OpenAI-compatible endpoint (for OpenAI SDK clients)

## Installation

Installed as a `.deb` package (v0.1.0) from GitHub releases. Managed as a systemd user service at `~/.config/systemd/user/freehive.service`.

## Related
- [[concepts/MCP Servers]]
- [[concepts/OpenCode]]
