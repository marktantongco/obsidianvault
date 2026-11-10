---
title: Obsidian MCP Wiring
category: system
tags: [obsidian, mcp, memory, integration]
summary: How the Obsidian vault is exposed to every AI client on this machine as one MCP server, and why a stdio bridge sits in front of it.
lifecycle: verified
tier: core
source: agent-session
confidence: high
---

# Obsidian MCP Wiring

One server, five clients, one secret location.

## Shape

```
opencode / claude / codex / lmstudio / hermes
                 |
                 v  stdio (JSON-RPC)
        ~/.local/bin/obsidian-mcp        <- reads the key, speaks HTTP
                 |
                 v  https://127.0.0.1:27124/mcp
   obsidian-local-rest-api 5.0.2 (inside the Obsidian app)
                 |
                 v
   /home/x1/Projects/obsidianvault   <- 16 MCP tools over the vault
```

## Why a bridge instead of direct HTTP

- The plugin's TLS listener uses a **self-signed certificate**; Node/Rust/Python
  MCP clients reject it by default. The bridge disables verification for the
  loopback call only, never globally.
- The API key lives in the plugin's own `data.json`. Inlining it into five
  client configs would mean five copies to rot when the plugin rotates it. The
  bridge re-reads the key on every launch, so rotation costs nothing.

## Client registration

| Client | Where | Transport |
|--------|-------|-----------|
| OpenCode | `~/.config/opencode/opencode.json` → `mcp.servers.obsidian` | local stdio |
| Claude Code | `~/.claude.json` → `mcpServers.obsidian` (user scope) | stdio |
| Codex | `~/.codex/config.toml` → `[mcp_servers.obsidian]` | stdio |
| LM Studio | `~/.lmstudio/mcp.json` → `mcpServers.obsidian` | stdio |
| Hermes | `~/.hermes/config.yaml` → `mcp_servers.obsidian` | stdio |

## Checks

- `obsidian-mcp --doctor` — vault path, key, handshake, live `vault_list`.
- `obsidian-mcp --selftest` — prints the 16 tool names.
- `claude mcp list` — shows `obsidian ✔ Connected`.
- `hermes mcp list` — shows `obsidian ✓ enabled`.
- `ss -ltnp | grep 27124` — the plugin listener.

## Failure modes seen

- Obsidian closed → nothing on `:27124`; bridge returns a JSON-RPC error rather
  than hanging.
- Vault not registered / in Restricted Mode → plugins never load, so no
  listener. Fixed by registering the vault and trusting the author.
- Hermes ignored *every* setting because `config.yaml` had duplicate `provider`
  and `base_url` keys in `model:`; the whole file failed to parse. Removing the
  shadowed duplicates fixed parsing with no behavior change.

## Related

- [[AI CLI Memory Integration]]
- [[AGENTS]]

## Verified

- Vault written through MCP (`vault_write`) and read back with frontmatter parsed.
