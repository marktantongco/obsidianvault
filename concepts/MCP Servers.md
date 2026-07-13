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

## Usage
MCP tools are automatically available to agents when configured. They follow the same permission model as built-in tools.

## Related
- [[AI Agents]]
- [[Development Workflow]]
