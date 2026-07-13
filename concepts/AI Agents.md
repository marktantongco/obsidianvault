---
tags: [ai, agents, orchestration]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: core
---

# AI Agents

## Overview
AI agents are autonomous systems that can perceive their environment, make decisions, and take actions to achieve specific goals.

## Key Components
- **LLM Backend**: The reasoning engine (Claude, GPT, Gemini, etc.)
- **Tools**: External capabilities (file access, shell, web search)
- **Memory**: Persistent state across sessions
- **Planning**: Task decomposition and execution strategy

## Agent Types in This Setup

### Primary Agents
| Agent | Version | Role | Location |
|-------|---------|------|----------|
| [[Hermes]] | v0.18.2 | Orchestrator | `~/.hermes/hermes-agent/` |
| [[OpenCode]] | v1.17.15 | Code Worker | `~/.opencode/bin/opencode` |
| [[Claude Code]] | v2.1.205 | Reviewer | `~/.local/bin/claude` |
| [[MiMo Code]] | v0.1.5 | Xiaomi Assistant | `~/.local/bin/mimo` |

### Secondary Agents
| Agent | Version | Role | Location |
|-------|---------|------|----------|
| [[OpenAI Codex]] | v0.143.0 | Code Generation | `~/.local/bin/codex` |
| [[Grok]] | v0.2.93 | xAI Assistant | `~/.grok/bin/grok` |

## Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    HERMES (The Brain)                       │
│  - Persistent memory & learning                            │
│  - High-level planning & orchestration                     │
│  - Delegates tasks to specialists                          │
└──────────────────┬──────────────────────────────────────────┘
                   │
    ┌──────────────┼──────────────────────────┐
    │              │                          │
    ▼              ▼                          ▼
┌─────────┐  ┌──────────┐           ┌─────────────────┐
│OpenCode │  │Claude Code│          │  Obsidian Vault  │
│(Worker) │  │ (Worker)  │          │  (Knowledge Base)│
└─────────┘  └──────────┘           └─────────────────┘
```

## Agent Bridges
- **Hermes-OpenCode**: `~/.hermes/plugins/opencode/`
- **Hermes-Claude**: `~/.hermes/plugins/code-bridge/`

## Unified Memory
- **agentic-stack**: `~/ai-workspace/.agent/`
- Symlinked to all agents

## Related
- [[Development Workflow]]
- [[MCP Servers]]
- [[Obsidian Wiki]]
