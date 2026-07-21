---
title: "Session State - MCP Cleanup and AI Tool Installations"
tags: [sysadmin, tools, environment-setup]
summary: "Removed tokensave/codegraph MCPs (777MB freed), installed FreeHive, lifeos-cli, p2d-duck, ai-wanderer, free-claude-code, and LifeOS skill. Fixed apt mirror. GDM Wayland fix in progress."
base_confidence: 0.9
lifecycle_changed: 2026-07-14
sources:
  - "default project session (2026-07-14)"
lifecycle: archived
tier: peripheral
---

## Finding: tokensave and codegraph MCP Removal

Removed both memory-heavy MCP servers from the system. **tokensave** (~549MB) uninstalled via its own `tokensave uninstall` command + binary/data dir removal. **codegraph** MCP (~228MB) data dir removed and plugin entry disabled.

**Control mechanism**: Both are disabled via `"disabled_mcps": ["codegraph", "tokensave"]` in `oh-my-openagent.json` (line ~268) rather than removing from the plugin entirely. This survives plugin upgrades.

## Finding: FreeHive AI Gateway

Installed v0.1.0 from GitHub releases (deb). Runs as a systemd user service on `http://127.0.0.1:7200`. Acts as an AI provider gateway with backend routing to Claude, ChatGPT, Gemini etc.

**Auth requirement**: Needs `claude login` to authenticate Claude Code OAuth before it can serve requests. Without it, the backend returns 401/503.

**Provider config**: Added `freehive` (Anthropic) and `freehive-oai` (OpenAI-compatible) providers to `opencode.json`.

## Finding: lifeos-cli Installed

v0.21.1 installed via `uv tool install --upgrade lifeos-cli`. SQLite DB initialized at `~/.local/share/lifeos/lifeos.db` (632KB). Timezone set to Asia/Manila. This replaces the LifeOS Pulse service for the LifeOS ecosystem.

## Finding: apt Mirror 403 and Fix

Ubuntu 26.04 (resolute) defaults to `ph.archive.ubuntu.com` (Philippine mirror) in `/etc/apt/sources.list.d/ubuntu.sources`. This mirror returned 403 Forbidden for `linux-firmware-amd-misc` package. Fix: `sudo sed -i 's|ph.archive.ubuntu.com|archive.ubuntu.com|g' /etc/apt/sources.list.d/ubuntu.sources` to switch to the main archive mirror.

## Finding: GDM Wayland Disabled on Intel HD 520

Intel HD 520 (Skylake) has broken Wayland support. Added `WaylandEnable=false` under `[daemon]` in `/etc/gdm3/custom.conf`. Takes effect after reboot - until then GDM may still default to Wayland.

## Finding: Tools Installed via pipx/uv

Four additional tools installed in this session:
- **p2d-duck** v1.3.1 via pipx — commands: `duck-ai`, `p2d-duck`
- **ai-wanderer (ai-free-swap)** v0.2.0 via pipx from source (`github.com/sshnaidm/ai-wanderer`) — command: `ai-free-swap`, an OpenAI/Anthropic-compatible free-tier proxy router
- **free-claude-code** via `uv tool install` — 6 executables: `fcc-claude`, `fcc-codex`, `fcc-init`, `fcc-pi`, `fcc-server`, `free-claude-code`
- **danielmiessler/LifeOS** skill placed at `~/.claude/skills/LifeOS/` — AI-native Life Operating System skill. Needs AI harness `/lifeos-setup` for onboarding.

## Finding: Docker Disabled

Docker was stopped and disabled via `sudo systemctl disable docker`. Now inactive.

## Related

- [[opencode-mcp-management]]
- [[ubuntu-sources-mirror]]
- [[gdm-wayland-intel-skylake]]
