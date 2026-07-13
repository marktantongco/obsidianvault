---
title: Agentic-Stack + Obsidian-Wiki System Performance
category: synthesis
tags: [architecture, multi-agent, wiki, assessment]
sources:
  - conversation:2026-07-09
summary: Plumbing is A− (shared vault, 12 agents, 36 skills); knowledge fill was early until this compound pass.
provenance: {extracted: 0.5, inferred: 0.5, ambiguous: 0.0}
base_confidence: 0.6
lifecycle: draft
lifecycle_changed: 2026-07-09
tier: core
created: 2026-07-09T09:58:13Z
updated: 2026-07-09T10:44:47Z
relationships:
  - target: "[[concepts/multi-agent-obsidian-wiki-synergy]]"
    type: extends
  - target: "[[skills/multi-agent-vault-wiring]]"
    type: uses
---

# Agentic-Stack + Obsidian-Wiki System Performance

## Context
Assessment of how `~/.agent` (agentic-stack), Ar9av `obsidian-wiki`, and `/home/x1/obsidianvault` work together after multi-agent wiring.

## Finding
| Layer | Role | Status |
|-------|------|--------|
| agentic-stack | Session memory, lessons, permissions | Healthy |
| obsidian-wiki | Skill framework + compile pattern | 12 agents provisioned, doctor pass |
| obsidianvault | Durable knowledge | Structure OK; compounds after ingest/capture |

## Implications
- Performance scales with capture/ingest habit, not install alone.
- Two skill systems: harness ops vs wiki knowledge — use the right set.
- Single vault for all CLIs prevents knowledge silos.

## Related
- [[concepts/multi-agent-obsidian-wiki-synergy]] · [[skills/multi-agent-vault-wiring]] · [[concepts/Obsidian Wiki]] · [[projects/AI-Second-Brain]]

## Session notes (promoted 2026-07-09)

# Wiki compound habit after install

## Finding
After multi-agent wiring, vault stayed thin until: `obsidian-wiki setup` → status → `@ai` text ingest → session capture. Claude/Codex jsonl history may be empty; capture conversation knowledge instead.

## Loop
```
work → wiki-capture --quick (or full) → wiki-ingest promote → wiki-query next session
```

## Promote
→ [[synthesis/agentic-stack-obsidian-wiki-performance]]
