---
title: lifeos-cli
category: entities
tags:
  - tool
  - lifeos
  - cli
  - memory
  - pulse
sources:
  - conversation:2026-07-14
  - journal/2026-07-14-system-admin-tool-installs
  - 06_STATE/configs/second-brain-skill
summary: >-
  LifeOS CLI tool (v0.21.1) installed via uv. Manages LifeOS memory database
  (SQLite, 632KB) at ~/.local/share/lifeos/lifeos.db. CLI interface to the
  LifeOS Pulse daemon and Memory v7.6 buckets. Complementary to the LifeOS AI
  harness skill at ~/.claude/skills/LifeOS/.
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.85
lifecycle: draft
tier: supporting
created: 2026-07-14
updated: 2026-07-21
---

# lifeos-cli

## Overview

The LifeOS CLI (`lifeos-cli`) is the terminal interface to the [[concepts/LifeOS Algorithm|LifeOS system]]. It manages the LifeOS memory database, provides access to Memory v7.6 buckets, and connects to the LifeOS Pulse daemon at `localhost:31337`.

## Key Facts

| Property | Value |
|----------|-------|
| **Version** | v0.21.1 |
| **Install method** | `uv tool install --upgrade lifeos-cli` |
| **Database** | `~/.local/share/lifeos/lifeos.db` (SQLite, 632KB) |
| **Timezone** | Asia/Manila |
| **Complementary** | LifeOS AI harness skill at `~/.claude/skills/LifeOS/` (v7.1.1) |
| **Status** | ✅ Installed |

## Relationship to LifeOS Pulse

The CLI and the Pulse daemon serve different but complementary roles:

| Interface | Purpose | Status |
|-----------|---------|--------|
| **lifeos-cli** | Terminal commands for memory management | ✅ Installed |
| **LifeOS Pulse** | Daemon at `localhost:31337` with REST API | ⏳ Not running (`bun run pulse` needed) |
| **LifeOS AI skill** | AI harness integration at `~/.claude/skills/LifeOS/` | ✅ Installed, needs `/lifeos-setup` |

Per the [[06_STATE/configs/second-brain-skill|SecondBrain skill config]], the LifeOS system provides these API endpoints:

```text
GET  /api/memory/{bucket}      — list vault entries in bucket
POST /api/memory/{bucket}      — create entry (writes to vault + Memory)
GET  /api/memory/search?q=     — full-text search across buckets
POST /api/algorithm/step       — trigger OBSERVE→THINK→PLAN cycle
GET  /api/pulse/status         — daemon health check
```

## Related

- [[concepts/LifeOS Algorithm]] — The task routing algorithm driven by LifeOS
- [[concepts/agentic-stack]] — Separate session memory layer (agentic-stack is distinct from LifeOS memory)
- [[concepts/Hermes Agent]] — Runs hermes_router.py which integrates with LifeOS
- [[journal/2026-07-14-system-admin-tool-installs]] — Installation session
- [[06_STATE/configs/second-brain-skill]] — Skill config with vault↔memory mapping
