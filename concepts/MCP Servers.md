---
tags: [mcp, protocol, tools]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: supporting
---

# MCP Servers

## Overview
Model Context Protocol (MCP) provides a standardized way for AI agents to interact with external tools and services.

## Available MCP Tools
- File system access
- Web search and fetching
- Code execution
- Database queries
- Browser automation

## Configuration
MCP servers are configured in agent config files:
- `~/.opencode/config.json`
- `~/.hermes/config.yaml`
- `~/.claude/settings.json`

### Memory Management via `oh-my-openagent`

When using the oh-my-openagent plugin, MCP servers are injected programmatically. Memory-heavy MCPs (e.g., tokensave at ~549MB, codegraph at ~228MB) can be disabled without removing them from the plugin by setting `disabled_mcps` in `oh-my-openagent.json`:

```json
"disabled_mcps": ["codegraph", "tokensave"]
```

This approach survives plugin upgrades since the plugin config is separate from the plugin code. The entries remain in the plugin's `.mcp.json` but are filtered out at load time.

## Usage
MCP tools are automatically available to agents when configured. They follow the same permission model as built-in tools.

## Related
- [[AI Agents]]
- [[Development Workflow]]
