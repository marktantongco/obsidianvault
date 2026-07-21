---
title: agentic-stack
category: concepts
tags:
  - agentic-stack
  - memory
  - unified
  - agents
  - session
created: 2026-07-21
updated: 2026-07-21
summary: >-
  Unified memory layer at ~/ai-workspace/.agent/ shared across all agents via
  symlinks. Stores session memory, lessons learned, permissions, and prompts.
  Complements the Obsidian vault (durable knowledge) with session-level memory.
lifecycle: draft
tier: core
source: opencode
confidence: 0.85
---

# agentic-stack

## Overview

The **agentic-stack** is the shared session memory layer for the multi-agent system. Located at `~/ai-workspace/.agent/`, it stores ephemeral state that lives between sessions but is more volatile than the [[concepts/Obsidian Wiki|Obsidian vault]] — lessons learned, permissions granted, session transcripts, and runtime prompts.

Every agent in the system symlinks to this directory, ensuring that what one agent learns is immediately visible to all others. The vault holds **durable, compiled knowledge** (concepts, skills, references); agentic-stack holds **session-level context** (what happened in the last conversation, what permissions were granted, what lessons were extracted).

---

## Location & Symlinks

| Agent | Symlink Path | Target |
|-------|-------------|--------|
| OpenCode | `~/.opencode/agentic` | `~/ai-workspace/.agent/` |
| Hermes | `~/.hermes/agentic` | `~/ai-workspace/.agent/` |
| Claude Code | `~/.claude/agentic` | `~/ai-workspace/.agent/` |

### Anatomy

```
~/ai-workspace/.agent/
├── AGENTS.md          # Master instructions (requires vault read every session)
├── memory.md          # Running session memory
├── skills/            # Shared skill definitions
├── prompts/           # Reusable prompt templates
├── memory/            # Per-session memory snapshots
└── lessons/           # Extracted lessons (promoted to vault on capture)
```

| Directory | Purpose | Volatility |
|-----------|---------|------------|
| `memory.md` | Active session state, current context | High — overwritten each session |
| `memory/` | Archived session snapshots | Medium — retained for reference |
| `lessons/` | Extracted takeaways from sessions | Medium — promoted to vault as concepts |
| `skills/` | Shared skill definitions used across agents | Low — change only on upgrade |
| `prompts/` | Prompt templates for common operations | Low — change only on refinement |
| `AGENTS.md` | Bootstrap instructions (require vault read) | Very low — system-level |

---

## Role in the System

The agentic-stack is one of three layers in the knowledge architecture:

```
┌─────────────────────────────────────────────────────┐
│  agentic-stack (~/.agent/)                          │
│  Session memory, lessons, permissions, prompts      │
│  Volatile — cleared/rebuilt per session             │
├─────────────────────────────────────────────────────┤
│  Obsidian Vault (~/obsidianvault/)                  │
│  Durable knowledge, concepts, skills, references    │
│  Persistent — survives sessions                     │
├─────────────────────────────────────────────────────┤
│  Agent Skills (per-agent skills/ directories)       │
│  Operational harness, tool definitions              │
│  Stable — changes only via obsidian-wiki setup      │
└─────────────────────────────────────────────────────┘
```

### What Goes Where

| Content | Destination | Why |
|---------|-------------|-----|
| New concept or skill | Vault `concepts/` or `skills/` | Durable, cross-session knowledge |
| Session timeline | Vault `journal/` | Permanent record |
| Current task state | `memory.md` | Active context, lost on session end |
| "I learned X" | `lessons/` → vault on `wiki-capture` | Temporary until promoted |
| Agent permissions | `.agent/` | Agent-specific, not vault knowledge |
| System prompt | `AGENTS.md` (vault root) | Shared across agents |

---

## Session Bootstrap

Every agent follows this sequence at session start (defined in `AGENTS.md`):

```
1. Read host AGENTS.md / CLAUDE.md
2. Resolve OBSIDIAN_VAULT_PATH from ~/.obsidian-wiki/config
3. Read $VAULT/AGENTS.md
4. Skim hot.md for recent activity
5. Read agentic-stack memory.md for session context
6. Use wiki-* skills as needed
```

The agentic-stack's `memory.md` is read after the vault's `AGENTS.md` and `hot.md`, giving the agent both durable knowledge and recent session context.

---

## Compose Rules

Per [[skills/multi-agent-vault-wiring]] and the [[journal/2026-07-13-second-brain-integration-session|July 13 session]]:

- `.agent/` = session memory, lessons, permissions
- Vault = durable distilled knowledge
- Do **not** fork a second vault per agent — single vault for all CLIs prevents knowledge silos
- Two skill systems exist: harness ops (`skills/` directories) vs wiki knowledge (vault `skills/`) — use the right set for the task

---

## Integration with LifeOS

The agentic-stack is distinct from the [[concepts/LifeOS Algorithm|LifeOS system]]:

| System | Role | Location |
|--------|------|----------|
| **agentic-stack** | Session memory, lessons, permissions | `~/ai-workspace/.agent/` |
| **LifeOS Pulse** | Algorithm daemon, memory API | `localhost:31337` |
| **LifeOS memory** | SQLite database for LifeOS | `~/.local/share/lifeos/lifeos.db` |

The agentic-stack is not aware of LifeOS Pulse — they are complementary: agentic-stack holds agent session state, LifeOS holds the algorithm loop and memory graph.

---

## Health Assessment

Per [[synthesis/agentic-stack-obsidian-wiki-performance|system performance assessment]] (2026-07-09):

- **Status**: Healthy
- **Performance scales** with capture/ingest habit, not install alone
- **Single vault** for all CLIs prevents knowledge silos
- **Session memory** is the weakest link — it's overwritten each session unless explicitly captured to vault

## Related

- [[concepts/Obsidian Wiki]] — The durable knowledge counterpart
- [[concepts/LifeOS Algorithm]] — Task routing system (separate but complementary)
- [[skills/multi-agent-vault-wiring]] — How agents connect to the vault
- [[synthesis/agentic-stack-obsidian-wiki-performance]] — System performance assessment
- [[concepts/AI Agents]] — All agents that symlink to agentic-stack
- [[projects/AI-Second-Brain]] — Project context
