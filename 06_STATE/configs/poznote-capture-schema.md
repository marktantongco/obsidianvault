---
title: Poznote Capture Schema
category: state
tags:
  - poznote
  - schema
  - capture
  - pipeline
summary: "Frontmatter schema and field definitions for the Poznote capture pipeline. Defines required/optional fields, classification rules, and file naming conventions."
lifecycle: active
tier: core
created: 2026-07-09
---

# Poznote Capture Format

## Markdown Frontmatter Schema

Every capture must include this frontmatter. Missing fields get defaults applied by the pipeline.

```yaml
---
title: "Descriptive title (required, used as filename)"
category: "WORK|KNOWLEDGE|LEARNING|RELATIONSHIP|OBSERVABILITY|STATE"
tags:
  - tag1
  - tag2
summary: "One-line summary (populated by classifier if blank)"
lifecycle: "active|archived|draft"
tier: "1|2|3|4|5"
source: "poznote|claude|codex|opencode|hermes|manual"
created: "2025-01-15T10:30:00"
related: []
---

# Body content here

Use [[wikilinks]] for cross-references.
```

## Field Definitions

| Field | Required | Values | Default |
|-------|----------|--------|---------|
| title | Yes | Free text | Filename stem |
| category | No | Memory v7.6 bucket | Auto-classified |
| tags | No | List of strings | Empty |
| summary | No | One sentence | Auto-generated |
| lifecycle | No | active, archived, draft | active |
| tier | No | 1 (core) to 5 (peripheral) | 2 |
| source | No | Tool name | poznote |
| created | No | ISO 8601 timestamp | Now |
| related | No | List of wikilinks | Empty |

## Classification Rules

The pipeline auto-classifies based on content keywords:

- **WORK**: task, project, sprint, todo, deadline, milestone
- **KNOWLEDGE**: concept, theory, research, reference, paper, article
- **LEARNING**: course, tutorial, lesson, learned, takeaway
- **RELATIONSHIP**: person, contact, meeting, org, team
- **OBSERVABILITY**: metric, log, monitor, alert, dashboard
- **STATE**: config, env, setup, install, version

If no keywords match, defaults to KNOWLEDGE.

## File Naming

- Title becomes filename: `My Great Idea.md`
- Special characters replaced: `<>:"/\|?*` → `-`
- Spaces preserved
- Case preserved

## Batch Processing

Files dropped in `~/poznote-inbox/` are processed by the pipeline:
1. Classify into bucket
2. Add/update frontmatter
3. Move to correct bucket directory
4. Git commit + push (batched, one commit per run)

## Related

- [[06_STATE/configs/second-brain-skill|Second Brain Skill]] — Companion AI skill configuration
- [[06_STATE/configs/sync-strategy|Sync Strategy]] — Mobile-desktop sync pipeline
- [[skills/wiki-compound-loop|Wiki Compound Loop]] — Capture pipeline automation
