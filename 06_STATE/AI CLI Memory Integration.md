---
title: AI CLI Memory Integration
type: map
status: evergreen
created: 2026-11-07
tags:
  - map
  - memory
  - ai-cli
category: system
updated: 2026-11-10

---

# AI CLI Memory Integration

Map of how AI CLI tools (OpenCode, Claude Code, Hermes) share this vault as durable memory.

## Vault

- Path: `/home/x1/Projects`
- Registered in Obsidian (`~/.config/obsidian/obsidian.json`).

## Skills (shared via `~/.agents/skills`)

See [[06_STATE/configs/obsidian-mcp-wiring|Obsidian MCP Wiring]] for vault/MCP bridge details.

- `obsidian-markdown`, `obsidian-bases`, `obsidian-cli`, `json-canvas`, `defuddle`, `knap` (kepano/obsidian-skills)
- `obsidian-vault-curator` (hermes-obsidian-self-organizing-vault)
- Symlinked into `~/.claude/skills`, `~/.hermes/skills`, `~/.opencode/skills`.

## Proxy / MCP

- OWL reverse proxy (OpenAI-compatible): `http://127.0.0.1:8080/api/v1` (`owl-local` provider in OpenCode).
- Sidecar MCP (owl-egress): `/home/x1/.owl-agent-upstream/mcp.sh` (proxy_pick, proxy_stats, proxy_rotate, proxy_validate, memory_set/get/search, web_search).
- Registered in `~/.config/opencode/opencode.json` (`mcp.servers.owl-egress`) and `~/.agents/mcp.json`.

## Rules

- No secrets in notes.
- Use `[[wikilinks]]` for durable entities.
- Tags for workflow/status only.

## Skills pipeline (2026-11-07)

- Canonical root: `~/.agents/skills` (hub). `~/.config/opencode/skills` retired → symlink to hub. Backup: `~/.config/opencode/skills.bak-merged-20261107`.
- Merged 75 opencode-only skills into hub (union now 168; curated target 88 — overage pending review).
- R1 installed: `free-search-aggregator`, `freeUnlimited-websearch`, `you-web`, `yao-meta-skill` (global, 58 agents each).
- R2 promoted 10 conceptual skills: `ralph-prompt-multi-task`, `orchestrate`, `chain-of-thought`, `headroom`, `caveman`, `devils-advocate`, `codemap`, `parallel-agent-skills`, `agent-skills`, `impeccable` (+ `ralph-claude`, `ralph-zero`).
- yao-meta-skill: adopted (not built-in). parallel-findall: built-ins only.
- you-web MCP registered (keyless free profile) in `~/.agents/mcp.json` + `~/.config/opencode/opencode.json`.
- free-search-aggregator venv at `.agents/skills/free-search-aggregator/.venv` (bs4, PyYAML, requests); `fsearch.sh` patched to use venv python.
- freeUnlimited-websearch venv with `ddgs`; shebang patched.

## Platform integration (2026-11-09)

See also: [[references/ai-skills-consolidated-framework|Skills Hub / AI Skills Framework]], [[entities/Owl-Agent|OWL-AGENT Proxy Defense Stack]].

### MCP parity — 6 shared servers

`agentmemory` (http `127.0.0.1:8765/mcp`), `thinking`, `owl-egress` (`OWL_AGENT_HOME=~/.owl-agent-upstream`), `you-web`, `you-research`, `you-finance`.

| Host | Config | Live check |
|---|---|---|
| OpenCode | `~/.config/opencode/opencode.json` (7 local + `opencode_console`) | `opencode run` OK |
| Claude Code | `~/.claude.json` `mcpServers` (added 2026-11-09; was empty) | `claude mcp list` 6/6 Connected |
| Codex | `~/.codex/config.toml` + `plannotator-inbox` | `codex mcp list`, OAuth on you.com |
| Hermes | `~/.hermes/config.yaml` `mcp_servers` (7 incl. plannotator-inbox) | `hermes mcp list` all enabled |
| Pi | `~/.pi/agent/mcp.json` (keeps its stdio `agentmemory`) | `pi mcp list` 4 connected, 2 need sign-in |
| LM Studio | `~/.lmstudio/mcp.json` (native shape: `url`, no `type`) | loads at next app launch |

### Skills

- Canonical hub `~/.agents/skills` (98 entries) is the only source.
- `~/.claude/skills` = 67 symlinks into the hub (+12 Watchtower, +3 Omarchy) — no drift, no broken links.
- `~/.claude/skills/conceptual/` relocated to `~/repos/conceptual/` (869 nested `SKILL.md` removed from Claude's discovery path by design).
- Hermes: `skills.external_dirs: ['~/.agents/skills']` → 158 skills enabled (49 builtin / 109 local).
- 75 overage skills archived to `~/.agents/skills-archive/` (reversible).

### Health (2026-11-09)

- OWL ingress `:8080` → `200` via local Ollama fallback (`qwen2.5:7b`); upstream free tier is metered per egress block (429 `FreeUsageLimitError`).
- Command Code proxy `:55990` → `200`.
- Sidecar selftest OK; agentmemory `initialize` → `200`; owl-heartbeat 8 clean runs / 2h.
- Hermes router `:8766` fallback repaired (`:11434` → `:11435`, documented Ollama port move); Hermes `model.api_key` + default model corrected.

### Known gaps

- Claude Code: not logged in (`claude -p` → "Not logged in"); MCP + skills verified, model call unverified.
- Codex: no OpenAI/ChatGPT credentials (`401`); MCP + skills verified, model call unverified.
- Pi: `you-research` / `you-finance` need OAuth (`pi mcp login <name>`).
- Ollama is currently a user-level daemon, not the systemd service — `sudo systemctl start ollama` to restore.
- `codemap` CLI unbuilt (needs `go`, then `make` in `~/repos/conceptual/codemap`).
