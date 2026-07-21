---
title: free-claude-code
category: entities
tags:
  - tool
  - claude
  - codex
  - free-tier
  - uv
sources:
  - conversation:2026-07-14
  - journal/2026-07-14-system-admin-tool-installs
summary: >-
  Open-source CLI toolset installed via uv from
  github.com/Alishahryar1/free-claude-code. Provides 6 executables for
  Claude/Codex-style AI assistance via free-tier API routing. Includes
  fcc-claude, fcc-codex, fcc-init, fcc-pi, fcc-server, and free-claude-code.
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

# free-claude-code

## Overview

free-claude-code is an open-source CLI toolset that provides free-tier alternatives to Claude Code and OpenAI Codex. It routes requests through free API tiers and exposes multiple entry points for different use cases.

## Key Facts

| Property | Value |
|----------|-------|
| **Repository** | `github.com/Alishahryar1/free-claude-code` |
| **Install method** | `uv tool install git+https://github.com/Alishahryar1/free-claude-code.git` |
| **Status** | ✅ Installed |

### Executables

The package installs 6 CLI commands:

| Command | Purpose |
|---------|---------|
| `fcc-claude` | Claude-style free-tier assistant |
| `fcc-codex` | Codex-style free-tier code assistant |
| `fcc-init` | Initialize configuration |
| `fcc-pi` | Raspberry Pi-optimized variant |
| `fcc-server` | Server mode (HTTP endpoint) |
| `free-claude-code` | Primary entry point |

## Usage

```bash
# Check version
fcc-claude --version

# Start interactive mode
fcc-claude

# Run server mode
fcc-server
```

## Related

- [[concepts/FreeHive]] — Primary AI gateway (free-claude-code is an alternative approach)
- [[entities/ai-wanderer]] — Another free-tier proxy router
- [[concepts/Claude Code]] — The commercial tool this emulates
- [[concepts/OpenAI Codex]] — The commercial tool this emulates
- [[journal/2026-07-14-system-admin-tool-installs]] — Installation session
