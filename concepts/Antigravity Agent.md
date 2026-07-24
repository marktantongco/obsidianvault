---
title: Antigravity Agent
category: concepts
tags:
  - antigravity
  - agents
  - creative
  - synthesis
  - e5
created: 2026-07-21
updated: 2026-07-21
summary: >-
  E5 creative synthesis agent. Contributed negative constraint design for
  system prompt v5.1.1, dual-mode poznote pipeline, and dependency chain
  analysis. Used for unconventional approaches and novel solutions.
lifecycle: draft
tier: core
source: opencode
confidence: 0.7
---

# Antigravity Agent

## Overview

Antigravity is the **E5 creative synthesis agent** in the [[concepts/LifeOS Algorithm|LifeOS multi-agent routing matrix]]. It handles the most complex and open-ended tasks — those requiring unconventional thinking, novel approaches, and synthesis across disparate domains.

Unlike the other agents which are installed CLI tools (OpenCode, Hermes, Claude Code, etc.), Antigravity is not a standalone binary. It is a **designation for the creative execution mode** within Claude Code (Dolphin cognitive mode from the [[concepts/system-prompt-v5-1-1|System Prompt v5.1.1]]), used when a problem demands non-obvious solutions.

---

## Role in the Agent Matrix

```
E5 (creative) → Claude Code (Dolphin mode) + Antigravity synthesis
```

| Property | Value |
|----------|-------|
| **Tier** | E5 (highest complexity) |
| **Execution** | Via Claude Code with Dolphin cognitive mode |
| **Constraint** | Forbids conventional/obvious solutions |
| **Trigger** | Problems requiring creative synthesis, novel architecture, or unconventional approaches |

### What Antigravity Does That Other Agents Don't

- Applies **negative constraints** instead of positive guidance (showed that "forbids" creates harder boundaries in latent space than "be wise")
- Designs **dual-mode** systems that work in both online and offline configurations
- Maps **dependency chains** across the entire system before building anything
- Prefers **unconventional decompositions** over standard architectural patterns

---

## Key Contributions

### 1. Negative Constraint Design (System Prompt v5.1.1)

Antigravity contributed the core insight that switched v5.1 from positive guidance to negative constraints:

> **Before (v5.1):** "Be thorough. Be wise. Ship fast."
> **After (v5.1.1):** "Forbids over-engineering. Forbids shallow answers. Forbids conventional solutions."

This shift creates harder boundaries in LLM latent space by explicitly forbidding undesired behaviors rather than vaguely encouraging desired ones. Every cognitive mode was redefined as a negative constraint:

| Mode | v5.1 (Positive) | v5.1.1 (Negative) |
|------|-----------------|-------------------|
| Rabbit | "Ship fast" | "Forbids over-engineering" |
| Owl | "Be thorough" | "Forbids shallow answers" |
| Dolphin | "Be creative" | "Forbids conventional solutions" |

### 2. Dual-Mode Poznote Pipeline

Designed the [[concepts/poznote-pipeline|Poznote Capture Pipeline]] to work in two modes simultaneously:

- **File mode** — Watches local inbox directory; works offline, no dependencies
- **API mode** — Serves HTTP endpoint for remote/mobile capture; requires daemon

This ensures the pipeline works regardless of network state — captures never block on external services.

### 3. Dependency Chain Analysis

Mapped the strict build order for the `second-brain/scripts/` project, preventing import errors:

```
lifeos_client.py → hermes_router.py → hermes (bash) → poznote_pipeline.py → poznote_watch.sh
```

This analysis prevented the common mistake of building scripts in source-alphabetical order, which would break all imports.

---

## Activation

Antigravity is invoked when a task reaches the E5 tier in the LifeOS routing matrix. The dispatch path is:

```
Task → hermes_router.py → classify as E5 → route to Claude Code with Dolphin mode → apply Antigravity synthesis
```

Currently, Grok and Antigravity are not yet wired as separate dispatch targets in `hermes_router.py` — Claude Code handles both E4 and E5 tasks. Full Antigravity dispatch is pending router updates.

## Related

- [[concepts/system-prompt-v5-1-1]] — Negative constraint design contributed by Antigravity
- [[concepts/LifeOS Algorithm]] — E5 routing tier
- [[concepts/poznote-pipeline]] — Dual-mode architecture contributed by Antigravity
- [[concepts/Claude Code]] — Execution host for Antigravity synthesis
- [[concepts/AI Agents]] — The agent catalog
- [[journal/2026-07-13-second-brain-integration-session]] — Original design session
