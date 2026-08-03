---
title: >-
  Kiro CLI MCP Fetch Repair, Agentic Firewall, and Claude Code Bedrock Setup
category: synthesis
tags: [mcp, kiro-cli, aws-bedrock, claude-code, agentic-firewall]
relationships:
  - target: "[[concepts/Claude Code.md]]"
    type: related_to
  - target: "[[concepts/MCP Servers.md]]"
    type: related_to
  - target: "[[concepts/agentic-stack.md]]"
    type: related_to
sources:
  - conversation:2026-07-30
created: 2026-07-30T07:05:00.000Z
updated: 2026-07-30T07:05:00.000Z
summary: >-
  Technical findings and fixes for kiro-cli MCP fetch tool crash, agentic-firewall installation, and Claude Code AWS Bedrock bearer token and region configuration.
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.9
lifecycle: verified
lifecycle_changed: 2026-07-30
---

# Kiro CLI MCP Fetch Repair, Agentic Firewall, and [[concepts/Claude Code|Claude Code]] Bedrock Setup

## Context
During CLI system operations, three distinct toolchain integration tasks were requested and completed:
1. Debugging `kiro-cli` MCP server connection failures for the `fetch` tool.
2. Installing and configuring `@shinertx/agentic-firewall` (`vibe-billing`).
3. Configuring and auditing Claude Code AWS Bedrock third-party credentials and region settings for `@imarkytanky`.

---

## 1. Kiro CLI MCP "Fetch" Tool Connection Repair

### Root Cause
When `kiro-cli` launches the `fetch` MCP server via stdio transport using `/home/ubuntu/.local/bin/uvx mcp-server-fetch`, `uvx` dynamically resolves the latest PyPI release of the `mcp` SDK (`v2.0.0`).
In `mcp 2.0.0`, the exception class in `mcp.shared.exceptions` was renamed from `McpError` to `MCPError`.
As a result, `mcp-server-fetch/server.py` crashes on startup:
```text
ImportError: cannot import name 'McpError' from 'mcp.shared.exceptions'. Did you mean: 'MCPError'?
```
The immediate process exit prevents `kiro-cli` from establishing stdio JSON-RPC transport.

### Fix
Updated `~/.kiro/settings/mcp.json` to pass `--with "mcp<2"` to `uvx`:
```json
"fetch": {
  "command": "/home/ubuntu/.local/bin/uvx",
  "args": ["--with", "mcp<2", "mcp-server-fetch"],
  "disabled": false,
  "autoApprove": ["fetch"]
}
```
*Verification*: Sending a JSON-RPC `initialize` request returned a valid 2.0 response from `mcp-fetch` server version `1.29.0`.

---

## 2. Agentic Firewall Installation (`@shinertx/vibebilling`)

### Installation & Build
- **Global Package**: Installed `@shinertx/vibebilling` globally via npm (`vibe-billing`).
- **Repository Setup**: Cloned `https://github.com/shinertx/agentic-firewall` to `/home/ubuntu/agentic-firewall`.
- **Monorepo Build**: Installed dependencies for all sub-packages (`agent-proxy`, `agent-dashboard`, `agent-mcp`).
- **CLI Commands Verified**: `vibe-billing doctor` and `vibe-billing scan` execute correctly.

---

## 3. Claude Code AWS Bedrock Configuration & Audit

### Credentials & Payload Analysis
- **Key Name**: `BedrockAPIKey-1q24-at-748178823323`
- **AWS Account ID**: `748178823323` (decoded from `ABSK` token payload).
- **Bearer Token**: `AWS_BEARER_TOKEN_BEDROCK="<REDACTED-rotate-key>"`

### Region Correction
- **Original Region Passed**: `imarkytanky` (user handle).
- **Correction**: Updated `AWS_REGION` and `AWS_DEFAULT_REGION` to **`us-east-1`** (standard AWS Bedrock primary region for Anthropic Claude models).

### Environment Persistence
Persisted in `~/.env`, `~/.bashrc`, and `~/.claude/settings.json`:
```bash
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION="us-east-1"
export AWS_DEFAULT_REGION="us-east-1"
export AWS_BEDROCK_KEY_NAME="BedrockAPIKey-1q24-at-748178823323"
export AWS_BEARER_TOKEN_BEDROCK="<REDACTED-rotate-key>"
export AWS_BEDROCK_API_KEY="<REDACTED-rotate-key>"
export BEDROCK_API_KEY="<REDACTED-rotate-key>"
```

---

## Related
- [[concepts/[[concepts/MCP Servers|MCP Servers]]|MCP Servers]]
- [[concepts/Claude Code|Claude Code]]
- [[concepts/[[concepts/agentic-stack|agentic-stack]]|agentic-stack]]
