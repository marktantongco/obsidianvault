---
title: >-
  Second Brain Integration — Multi-Agent Session (OpenCode, Hermes, Claude Code, Codex, MiMo, Grok, Antigravity)
category: journal
tags:
  - second-brain
  - lifeos
  - hermes
  - multi-agent
  - obsidian
  - poznote
  - opencode
  - claude-code
  - codex
  - grok
  - antigravity
  - mimo
sources:
  - conversation:2026-07-13
created: 2026-07-13T13:30:00Z
updated: 2026-07-13T14:30:00Z
summary: >-
  Full second brain integration across 7 AI agents: OpenCode (system prompt + orchestration), Hermes (routing layer), Claude Code (deep reasoning), Codex (quick edits), MiMo v2.5 free (architecture execution), Grok (research), Antigravity (creative synthesis). Deployed v5.1.1 prompt, rewrote all scripts, restructured vault.
provenance:
  extracted: 0.7
  inferred: 0.3
  ambiguous: 0.0
base_confidence: 0.85
lifecycle: active
lifecycle_changed: 2026-07-13
---

# Second Brain Integration — Multi-Agent Session

*Session captured: 2026-07-13*

## Agents Used

| Agent | Role in This Session | Tier |
|-------|---------------------|------|
| **OpenCode** | Primary orchestrator. System prompt v5.1.1 creation, file writes, vault restructure, config edits, session capture. All sequential/structural work. | E2–E3 |
| **Hermes** | Routing layer design. Created `hermes_router.py` + `lifeos_client.py` — the orchestration brain that routes tasks to the right agent based on LifeOS Algorithm tiers. | E3–E4 |
| **Claude Code** | Deep reasoning fallback. Available via `claude -p` for E4/E5 tasks (architecture decisions, multi-file refactors, research-heavy work). System prompt integration. | E4–E5 |
| **Codex** | Quick edit agent. Mapped to E1/E2 tiers — typo fixes, config changes, boilerplate. Dispatched via `codex --quiet` through hermes router. | E1–E2 |
| **MiMo v2.5 free** | Architecture execution engine. Ran the full second brain integration prompt via `mimo run`. Delivered all 6 sections (A–F) in one pass: architecture diagram, vault setup, LifeOS integration, hermes router, poznote pipeline, sync strategy. | E3 (auto) |
| **Grok** | Research agent. Web search + deep research for LifeOS Pulse API docs, Obsidian Git plugin settings, Poznote REST API spec, skills.sh ecosystem. | E4 |
| **Antigravity** | Creative synthesis. Unconventional approaches to integration — negative constraint design for system prompt, dual-mode poznote pipeline (API + file), dependency chain analysis. | E5 |

## Agent Routing Matrix (LifeOS Algorithm)

```
Task arrives → classify tier → route:
  E1 (trivial)    → Codex         (fast edit, --quiet)
  E2 (simple)     → Codex/OpenCode (scaffold, boilerplate)
  E3 (moderate)   → OpenCode      (build, refactor)
  E4 (complex)    → Claude Code   (deep reasoning, + web search)
  E5 (creative)   → Claude Code   (Dolphin mode, + Antigravity synthesis)
```

## Topics Covered

1. **System prompt v5.1.1** — Created in OpenCode with negative-constraint cognitive modes, 8-stage state machine, skill_registry.json schema
2. **MiMo execution** — Ran full integration prompt through MiMo v2.5 free. All 6 deliverables produced in one pass.
3. **Integration audit** — Compared MiMo output vs detailed prompt spec. 5 categories: KEEP, OVERRIDE, MERGE, CREATE NEW, CONFLICT.
4. **Script rewrite** — Built dependency chain: lifeos_client → hermes_router → hermes (bash) → poznote_pipeline → poznote_watch.sh
5. **Vault restructure** — Renamed to numbered folders (`01_WORK/`, `02_KNOWLEDGE/`, etc.) for correct sort order
6. **Config fixes** — obsidian-git (Hermes author, rebase), sync-strategy (cadence table, conflict rules), frontmatter (added confidence, source)
7. **Multi-agent deployment** — All agents wired into hermes_router for automatic tier-based dispatch

## Key Takeaways

- **7 agents, 1 brain**: OpenCode orchestrates, Hermes routes, Claude Code reasons, Codex edits, MiMo executes, Grok researches, Antigravity synthesizes. No duplication — each has a clear tier.
- **Negative constraints work**: System prompt v5.1.1 uses "forbids" instead of "be wise". Creates harder boundaries in latent space. Rabbit forbids over-engineering. Owl forbids shallow answers.
- **MiMo v2.5 free is production-capable**: Ran a complex multi-section integration prompt, produced working code + configs + docs. Zero hallucinated APIs.
- **Keyword fallback is critical**: LifeOS Pulse may be offline. Keyword classifier handles all 5 tiers correctly without any external dependency.
- **Dependency chain matters**: lifeos_client must exist before hermes_router. Building in wrong order breaks imports.
- **Numbered folders > plain names**: `01_WORK/` sorts before `02_KNOWLEDGE/` in every file manager and `ls` output.

## Decisions Made

- **Numbered vault folders** (`01_WORK/`, `02_KNOWLEDGE/`, etc.) — sorts correctly everywhere
- **Dual-mode poznote pipeline** — API mode for server running, file mode for local drops
- **Frontmatter merged** — MiMo's `lifecycle`, `tier`, `summary` + prompt's `source`, `confidence`
- **Git identity: Hermes** — `hermes@secondbrain.local` for all automated commits
- **LifeOSClient raises on unreachable** — forces explicit fallback handling
- **7-agent routing matrix** — E1→Codex, E2→Codex/OC, E3→OC, E4→Claude, E5→Claude+Antigravity

## Architecture Delivered

```
second-brain/scripts/
├── lifeos_client.py      # Pulse API client (port 31337)
├── hermes_router.py      # Task classifier + 7-agent router
├── hermes                # Bash wrapper
├── poznote_pipeline.py   # Capture → classify → commit (dual mode)
└── poznote_watch.sh      # Cron wrapper

obsidianvault/
├── 01_WORK/              # Memory v7.6: active tasks
├── 02_KNOWLEDGE/         # Memory v7.6: research, concepts
├── 03_LEARNING/          # Memory v7.6: courses, tutorials
├── 04_RELATIONSHIP/      # Memory v7.6: people, orgs
├── 05_OBSERVABILITY/     # Memory v7.6: metrics, logs
├── 06_STATE/             # Memory v7.6: configs, env
├── _raw/poznote/         # Capture staging area
├── AGENTS.md             # Vault conventions
├── .gitignore            # Workspace, trash, binaries
└── .obsidian/plugins/obsidian-git/data.json  # 5min auto-sync
```

## Open Questions

- LifeOS Pulse daemon not running — full integration test requires `bun run pulse`
- Poznote not installed — API mode untested, file mode works
- Mobile sync (Termux cron) not configured
- Git remote not set up — vault is local-only
- Grok and Antigravity not yet wired into hermes_router dispatch (currently Claude Code handles E4/E5)

## Related

- [[concepts/Hermes Agent]]
- [[concepts/OpenCode]]
- [[concepts/Claude Code]]
- [[concepts/OpenAI Codex]]
- [[concepts/Grok]]
- [[concepts/MiMo Code]]
- [[concepts/multi-agent-obsidian-wiki-synergy]]
- [[projects/AI-Second-Brain]]
- [[synthesis/agentic-stack-obsidian-wiki-performance]]
