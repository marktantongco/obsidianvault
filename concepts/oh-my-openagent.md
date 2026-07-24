---
title: oh-my-openagent
category: concepts
tags:
  - mcp
  - plugins
  - agents
  - injection
  - configuration
created: 2026-07-21
updated: 2026-07-21
summary: >-
  MCP injection plugin that programmatically loads MCP server definitions into
  AI agents. Supports disabled_mcps feature to disable memory-heavy MCPs
  (tokensave ~549MB, codegraph ~228MB) without breaking plugin upgrades.
lifecycle: draft
tier: supporting
source: opencode
confidence: 0.8
---

# oh-my-openagent

## Overview

**oh-my-openagent** is a plugin system that programmatically injects MCP (Model Context Protocol) server definitions into AI agents. Rather than each agent manually listing MCP servers in its config file, the plugin reads a centralized `.mcp.json` and injects them at load time. This means MCPs are added or removed in one place and propagate to all agents automatically.

Installed as part of the [[projects/AI-Second-Brain|AI Second Brain]] setup, it sits between the agent config layer and the MCP runtime.

---

## Architecture

```
oh-my-openagent.json (plugin config)
        │
        ▼
   Plugin Loader
        │
        ├── Reads .mcp.json (MCP definitions)
        ├── Applies disabled_mcps filter
        └── Injects filtered MCPs into agent runtime
```

| Layer | File | Purpose |
|-------|------|---------|
| **Plugin config** | `oh-my-openagent.json` | User settings — declared triggers, disabled MCPs |
| **MCP definitions** | `.mcp.json` | All available MCP server definitions (installed by setup) |
| **Agent runtime** | Agent-specific config | Injected MCPs are available as tools |

---

## MCP Memory Management

The primary operational concern with oh-my-openagent is memory. Two MCPs in particular are memory-intensive and were disabled on this system (per the [[journal/2026-07-14-system-admin-tool-installs|July 14 session]]):

| MCP | Memory | Contents |
|-----|--------|----------|
| **tokensave** | ~549MB | Binary at `~/.local/bin/tokensave` (153MB) + data dir `~/.tokensave/` (~150MB) + DB + index |
| **codegraph** | ~228MB | Data dir at `~/.codegraph/` |

Combined they consumed **~777MB** on a system with only 7.1GB RAM (Ubuntu 26.04, Intel i5-6200U).

### disabled_mcps Mechanism

Instead of removing MCP entries from `.mcp.json` (which would break on plugin upgrades), oh-my-openagent supports a `disabled_mcps` array in its config:

```json
{
  "disabled_mcps": ["codegraph", "tokensave"]
}
```

**This is the recommended approach** because:

- The MCP entries remain in the plugin's `.mcp.json` — upgrades restore them
- The plugin config (`oh-my-openagent.json`) is separate from plugin code — survives upgrades
- Entries are filtered at load time, never loaded into agent memory
- To re-enable, simply remove the name from the array

---

## Related

- [[concepts/MCP Servers]] — The Model Context Protocol standard
- [[journal/2026-07-14-system-admin-tool-installs]] — Session documenting MCP cleanup
- [[concepts/AI Agents]] — Agents that receive injected MCPs
- [[projects/AI-Second-Brain]] — Project context
