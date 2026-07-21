---
title: >-
  OpenCode FreeHive Integration
category: synthesis
tags:
  - opencode
  - freehive
  - configuration
  - systemd
sources:
  - conversation:2026-07-14
created: 2026-07-14T04:06:00Z
updated: 2026-07-14T04:06:00Z
summary: >-
  FreeHive configured as an AI provider in OpenCode with 10 GPT/Gemini models;
  Puter MCP removed; systemd restart loop resolved.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.9
lifecycle: draft
lifecycle_changed: 2026-07-14
tier: supporting
---

# OpenCode FreeHive Integration

## Context

[[concepts/FreeHive]] (Nazzero/FreeHive local AI gateway) was installed and running on port 7200, but OpenCode had no configured provider for it. The OpenCode config also contained an unused [[concepts/MCP Servers|Puter MCP]] entry that needed removal.

## Changes Made

### 1. Removed Puter MCP from OpenCode

The `puter` MCP server entry was removed from `/home/x1/.config/opencode/opencode.json`. Puter.js is a cloud-based service (User-Pays model, 500+ models) unrelated to FreeHive and was not being used.

### 2. Added FreeHive AI Provider

A new `freehive` provider was added using `@ai-sdk/openai-compatible`:

```
endpoint: http://127.0.0.1:7200/v1
apiKey: "freehive"
```

Ten models defined with per-model context/output limits and zero-cost (local):

| Model | Context | Output | Notes |
|---|---|---|---|
| gpt-5.6-terra | 1,050,000 | 128,000 | Most capable |
| gpt-5.6-luna | 1,050,000 | 128,000 | Most capable |
| gpt-5.5 | 128,000 | 32,768 | |
| gpt-5.4-mini | 128,000 | 32,768 | Fast |
| gemini-3.1-pro-preview | 1,000,000 | 65,536 | |
| gemini-3-pro-preview | 1,000,000 | 65,536 | |
| gemini-3.1-flash-lite-preview | 1,000,000 | 65,536 | Fast |
| gemini-2.5-pro | 1,000,000 | 65,536 | Balanced |
| gemini-2.5-flash | 1,000,000 | 65,536 | Balanced |
| gemini-2.5-flash-lite | 1,000,000 | 65,536 | Most quota |

No Claude models are available via FreeHive without authenticating Anthropic OAuth (`claude login`).

### 3. Fixed FreeHive systemd Restart Loop

The `freehive.service` (user systemd unit) was stuck in auto-restart (543 restarts) because a rogue `freehive-backend` process (PID 11964) held port 7200 before systemd could bind it. Killing the rogue process let systemd restart cleanly.

```
kill 11964  # then systemctl --user restart freehive.service
```

## Reasoning

- `@ai-sdk/openai-compatible` was used instead of `@ai-sdk/anthropic` because FreeHive exposes an OpenAI-compatible API even for non-OpenAI models.
- The `apiKey` is set to `"freehive"` — FreeHive accepts any non-empty key at the API level.
- Model limits were set conservatively to match FreeHive's backend model capacity rather than upstream API limits.

## Implications

- OpenCode can now switch to any FreeHive-hosted model via its model picker.
- The service restart loop fix is permanent as long as no other process binds port 7200.
- Anthropic Claude models will remain unavailable through FreeHive until `claude login` is run to set up OAuth tokens.
- Other agents (Claude Code, Codex, etc.) can also use FreeHive at `http://127.0.0.1:7200/v1`.

## Related

- [[concepts/FreeHive]] — Local AI provider gateway
- [[concepts/OpenCode]] — Terminal-based AI coding agent
- [[concepts/MCP Servers]] — Model Context Protocol
