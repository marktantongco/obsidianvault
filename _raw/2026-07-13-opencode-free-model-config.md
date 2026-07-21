---
title: >-
  OpenCode Free Model Configuration for Agents
category: synthesis
tags: [opencode, ai-agents, configuration, free-models, cost-optimization]
sources:
  - conversation:2026-07-13
created: 2026-07-13T12:00:00+08:00
updated: 2026-07-13T12:00:00+08:00
summary: >-
  Configured OpenCode agents and categories to use free-tier models from opencode zen instead of paid models. User prefers only "opencode zen" free models, not nvidia or google models.
provenance:
  extracted: 0.7
  inferred: 0.3
  ambiguous: 0.0
base_confidence: 0.7
lifecycle: draft
lifecycle_changed: 2026-07-13
tier: supporting
---

# OpenCode Free Model Configuration

## Context
OpenCode agents were configured to use expensive paid models by default. User wanted to optimize costs by using free-tier models available on the opencode platform.

## Configuration Files Modified

### oh-my-openagent.json
Located at `/home/x1/.config/opencode/oh-my-openagent.json`

**Agents section** — 11 agents configured:
- sisyphus, build, oracle, explore, momus, sisyphus-junior → primary: `nvidia/nemotron-nano-9b-v2:free`
- librarian, plan, metis, multimodal-looker, atlas → primary: `google/gemma-4-31b-it:free`
- deep, artistry, writing → primary: `google/gemma-4-31b-it:free`

**Categories section** — 8 categories configured:
- quick, ultrabrain, deep, unspecified-low → primary: `nvidia/nemotron-nano-9b-v2:free`
- visual-engineering, artistry, unspecified-high, writing → primary: `google/gemma-4-31b-it:free`

### opencode.jsonc
Located at `/home/x1/.config/opencode/opencode.jsonc`

**Agent section** — 11 agents with fallback chains:
- All agents now use free models as primary
- Paid models (xiaomi/mimo-v2-pro, deepseek/deepseek-r1) only as last-resort fallbacks

## Free Models Available

| Model | Provider | Context | Max Output |
|-------|----------|---------|------------|
| nvidia/nemotron-nano-9b-v2:free | n9router | 200K | 65K |
| google/gemma-4-31b-it:free | n9router | 131K | 32K |
| google/gemma-4-27b-it:free | n9router | 131K | 32K |
| liquid/lfm-2.5-1.2b-instruct:free | n9router | 32K | 32K |

## User Preference
User explicitly requested: **"do not use models from nvidia or google only free models from 'opencode zen' free"**

This indicates preference for models that are:
1. Free tier (no cost)
2. From the opencode platform specifically (not third-party providers)

## Open Questions
- Which specific models qualify as "opencode zen" free models?
- Are `nvidia/nemotron-nano-9b-v2:free` and `google/gemma-4-31b-it:free` considered "opencode zen" models or third-party?
- What other free models are available on opencode zen?

## Implications
- Current configuration may need revision based on user's clarification of "opencode zen" free models
- Cost optimization achieved by removing paid model defaults
- Fallback chains still include paid models as last resort

## Related
- OpenCode Configuration
- AI Agent System
- Cost Optimization Strategies
