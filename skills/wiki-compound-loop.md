---
title: Wiki Knowledge Compounding Loop
category: skills
tags:
  - wiki
  - capture
  - ingest
  - query
  - workflow
  - compound
created: 2026-07-21
updated: 2026-07-21
summary: >-
  The compounding knowledge workflow: capture findings during work, ingest and
  promote to compiled knowledge, then query in the next session. This is the
  core loop that converts ephemeral session notes into durable vault knowledge.
lifecycle: draft
tier: core
source: opencode
confidence: 0.9
---

# Wiki Knowledge Compounding Loop

## Overview

This skill defines the **knowledge compounding loop** — the core workflow that converts ephemeral session output into durable, queryable vault knowledge. Without this loop, the vault stays thin. With it, each session builds on the last.

First identified in [[synthesis/agentic-stack-obsidian-wiki-performance]]: *"vault stayed thin until: `obsidian-wiki setup` → status → `@ai` text ingest → session capture."*

The loop is tightly integrated with [[concepts/poznote-pipeline|the Poznote capture pipeline]] and the [[concepts/LifeOS Algorithm|LifeOS Algorithm]] routing system.

---

## The Loop

```mermaid
graph LR
    Work --> Capture
    Capture --> Ingest
    Ingest --> Promote
    Promote --> Query
    Query --> Work
    
    style Work fill:#3B82F6,color:#fff
    style Capture fill:#22C55E,color:#fff
    style Ingest fill:#F59E0B,color:#fff
    style Promote fill:#8B5CF6,color:#fff
    style Query fill:#EC4899,color:#fff
```

### Stage 1: Work (`work`)
Do the actual work — code, research, writing, configuration. Every work session produces artifacts (code outputs, research notes, decisions, errors).

**Pro tip**: Keep a scratch note open during work. Jot down findings, decisions, and dead ends as they happen.

### Stage 2: Capture (`wiki-capture`)
Capture findings to the vault. Two modes:

**Quick capture** (during or immediately after work):
```bash
wiki-capture --quick "Key finding or decision from session"
```
This drops a timestamped note into `_raw/poznote/` for later processing by the [[concepts/poznote-pipeline]].

**Full capture** (at session end):
```bash
wiki-capture --full
```
This runs the full Poznote pipeline: classify → frontmatter → route to bucket → git commit.

### Stage 3: Ingest & Promote (`wiki-ingest promote`)
Promote raw captures to compiled vault knowledge:
```bash
wiki-ingest promote
```

The promotion process:
1. Reads raw captures from `_raw/poznote/`
2. Classifies into the correct Memory v7.6 bucket
3. Injects proper frontmatter (title, tags, summary, lifecycle, tier)
4. Routes to the correct directory (`01_WORK/`–`06_STATE/`)
5. Git commits with format: `[source] YYYY-MM-DD HH:mm description`

### Stage 4: Query (`wiki-query`)
Before starting the next session, query the vault for relevant context:
```bash
wiki-query @personal What do I know about <topic>?

# Or with specific bucket scope
wiki-query @personal --bucket WORK What's in progress?
```

The query returns compiled knowledge from across all buckets — concepts, findings, decisions, and previous session takeaways.

---

## When to Run Each Stage

| Stage | Frequency | Duration | Best Practice |
|-------|-----------|----------|---------------|
| **Work** | Continuous | Variable | Keep a scratch note open |
| **Quick capture** | Every 15–30 min | 10 seconds | `wiki-capture --quick "..."` |
| **Full capture** | End of session | 2 minutes | Before closing terminal |
| **Ingest & promote** | Daily | 5 minutes | End of day routine |
| **Query** | Start of session | 1 minute | First command of the day |

---

## Automation

The loop can be partially automated:

### Automatic (via Poznote pipeline + cron)
- **Inbox watch**: Files dropped in `_raw/poznote/` are processed by `poznote_watch.sh` (cron-based)
- **Git sync**: Obsidian Git plugin auto-commits every 10 minutes, pushes every 30

### Manual (recommended for quality)
- **Promotion**: Review raw captures before promoting — check classification accuracy and frontmatter quality
- **Synthesis**: Manually create synthesis pages when new cross-cutting patterns emerge

---

## Integration with Other Systems

| System | Role in the Loop |
|--------|------------------|
| [[concepts/poznote-pipeline]] | The engine: capture → classify → route → commit |
| [[concepts/agentic-stack]] | Session memory layer — feeds into quick captures |
| [[concepts/LifeOS Algorithm]] | Routes capture classification tasks to appropriate agent tier |
| [[concepts/Obsidian Wiki]] | The vault — destination for promoted knowledge |
| [[skills/git-sync-strategy]] | Syncs captured knowledge across devices |
| [[06_STATE/configs/poznote-capture-schema]] | Defines the capture frontmatter schema |

## Trap to Avoid

> *"Claude/Codex jsonl history may be empty; capture conversation knowledge instead."*

Don't rely on agent internal history files (JSONL logs) for knowledge persistence. They are transient and agent-specific. Instead:
1. **Quick-capture** actionable findings during the session
2. **Full-capture** the session summary at session end
3. **Promote** daily for durable knowledge

## Related

- [[concepts/poznote-pipeline]] — The capture pipeline that powers this loop
- [[synthesis/agentic-stack-obsidian-wiki-performance]] — Original identification of the loop
- [[concepts/agentic-stack]] — Session memory that feeds captures
- [[concepts/system-prompt-v5-1-1]] — Master prompt for quality capture discipline
- [[06_STATE/configs/poznote-capture-schema]] — Frontmatter schema for captures
