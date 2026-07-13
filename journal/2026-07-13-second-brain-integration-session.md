---
title: >-
  Second Brain Integration — System Prompt v5.1.1, MiMo Execution, Full Stack Merge
category: journal
tags:
  - second-brain
  - lifeos
  - hermes
  - multi-agent
  - obsidian
  - poznote
sources:
  - conversation:2026-07-13
created: 2026-07-13T13:30:00Z
updated: 2026-07-13T14:00:00Z
summary: >-
  Complete second brain integration session: deployed system prompt v5.1.1, ran MiMo v2.5 free for architecture delivery, audited MiMo output vs detailed spec, rewrote all scripts with LifeOS Pulse API integration, restructured vault with numbered Memory v7.6 buckets.
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.85
lifecycle: active
lifecycle_changed: 2026-07-13
---

# Second Brain Integration — Full Stack Session

*Session captured: 2026-07-13*

## Topics Covered

1. System prompt v5.1.1 creation (cognitive modes, state machine, skill registry)
2. MiMo v2.5 free execution of the second brain integration prompt
3. Integration audit: MiMo output vs detailed prompt spec
4. Script rewrite: lifeos_client, hermes_router, poznote_pipeline
5. Vault restructuring: numbered Memory v7.6 folders
6. Config fixes: obsidian-git, sync-strategy, frontmatter schema

## Key Takeaways

- **System Prompt v5.1.1**: Negative constraints ("forbids") create harder boundaries than positive personas. 8-stage state machine with explicit IF/THEN transitions prevents infinite loops.
- **MiMo v2.5 free**: Ran the full second brain integration prompt via `mimo run`. Delivered all 6 sections (A–F) in one pass. Produced working hermes_router.py, poznote_pipeline.py, vault structure, and configs.
- **Integration audit revealed 5 categories**: KEEP (MiMo's vault_write, keyword classifier, file watcher), OVERRIDE (hermes_router needs LifeOSClient, poznote needs API client), MERGE (frontmatter schema, classification), CREATE NEW (lifeos_client, hermes bash wrapper, poznote_watch.sh), CONFLICT (folder naming → numbered wins).
- **Dependency chain**: lifeos_client.py → hermes_router.py → hermes (bash) → poznote_pipeline.py → poznote_watch.sh. Build order matters.
- **Keyword fallback works**: When Pulse is unreachable, classifier falls back to keyword matching. All 5 tiers (E1–E5) classify correctly without LifeOS running.

## Decisions Made

- **Numbered vault folders** (`01_WORK/`, `02_KNOWLEDGE/`, etc.) over plain names — sorts correctly in file managers and terminal `ls`.
- **Poznote dual mode**: API mode (REST v1) for when Poznote server is running, file mode for local `.md` drops. Both feed into the same classification + git commit pipeline.
- **Frontmatter schema merged**: Kept MiMo's `lifecycle`, `tier`, `summary` + added prompt's `source`, `confidence`. All fields useful.
- **Git init with Hermes identity**: `hermes@secondbrain.local` — consistent author across all automated commits.
- **LifeOSClient.classify_task() raises on unreachable**: Forces caller to handle fallback explicitly rather than silently defaulting to E3.

## Architecture Delivered

```
second-brain/scripts/
├── lifeos_client.py      # Pulse API client (port 31337)
├── hermes_router.py      # Task classifier + agent router
├── hermes                # Bash wrapper
├── poznote_pipeline.py   # Capture → classify → commit
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

- LifeOS Pulse daemon not running on this system — full integration test requires `bun run pulse` or systemd service
- Poznote not installed yet — API mode untested, file mode works
- Mobile sync (Termux cron) not configured — needs `poznote_watch.sh` deployed to phone
- Git remote not set up — vault is local-only until SSH remote added

## Related

- [[concepts/Hermes Agent]]
- [[concepts/multi-agent-obsidian-wiki-synergy]]
- [[projects/AI-Second-Brain]]
- [[synthesis/agentic-stack-obsidian-wiki-performance]]
