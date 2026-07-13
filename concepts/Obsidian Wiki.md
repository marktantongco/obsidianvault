---
tags: [obsidian, wiki, knowledge-base]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: core
---

# Obsidian Wiki

## Overview
Obsidian is a powerful knowledge base that works on local Markdown files. Combined with obsidian-wiki and llm-wiki, it becomes an AI-powered knowledge management system.

## Components

### 1. Obsidian Desktop App
- **Location**: `~/Applications/Obsidian.AppImage`
- **Type**: AppImage (portable)

### 2. obsidian-wiki
- **Version**: v2026.7.2
- **Skills**: 36 skills installed to all agents
- **Config**: `~/.obsidian-wiki/config`

### 3. llm-wiki Engine
- **Location**: `~/obsidianvault/ (compiled pages) + framework repo`
- **Type**: Karpathy-pattern personal knowledge base

## Vault Locations

### Primary Vault
- **Path**: `~/obsidianvault/`
- **Items**: 13+ pages
- **Structure**:
  - `concepts/` — Core concepts
  - `entities/` — People, organizations
  - `projects/` — Active projects
  - `references/` — External references
  - `synthesis/` — Cross-cutting analysis
  - `journal/` — Daily notes

### Secondary Vault
- **Path**: `~/obsidian-vaults/AI-Second-Brain/`
- **Engine**: llm-wiki

## Skills Installed
All agents have access to 36+ wiki skills:
- `wiki-query` — Search and retrieve knowledge
- `wiki-capture` — Save findings to wiki
- `wiki-ingest` — Add sources to wiki
- `wiki-lint` — Check wiki health
- `wiki-update` — Sync knowledge
- And 31 more...

## Usage
```bash
# Open Obsidian
~/Applications/Obsidian.AppImage

# Query wiki
wiki-query @personal What do I know about X?

# Capture finding
wiki-capture --quick "Important discovery"
```

## Related
- [[AI Agents]]
- [[Development Workflow]]
- [[MCP Servers]]

## Related
- [[multi-agent-obsidian-wiki-synergy]] · [[skills/multi-agent-vault-wiring]] · [[references/obsidian-claude-memory-framework]]
