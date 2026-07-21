---
title: >-
  MCP Cleanup, Docker Disable, and AI Tool Installations
category: journal
tags:
  - sysadmin
  - tools
  - mcp
  - free-ai
  - docker
  - gdm
sources:
  - "default project session (2026-07-14)"
created: 2026-07-14
updated: 2026-07-14
summary: >-
  Cleaned up memory-heavy MCPs (tokensave/codegraph, 777MB freed), disabled Docker, fixed apt 403 mirror error, disabled GDM Wayland on Intel HD 520, and installed FreeHive, lifeos-cli, p2d-duck, ai-wanderer, free-claude-code, and LifeOS skill.
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.85
lifecycle: active
lifecycle_changed: 2026-07-14
tier: core
---

# MCP Cleanup, Docker Disable, and AI Tool Installations

*Session captured: 2026-07-14*

## System: Ubuntu 26.04 (resolute)
- Intel HD 520 (Skylake), i5-6200U, 7.1GB RAM
- Bun 1.3.14, Node v22.14.0

## MCP Memory Cleanup

### tokensave — Removed
- Ran `tokensave uninstall`, removed binary (`~/.local/bin/tokensave`, 153MB) + data dir (`~/.tokensave/`, ~150MB). Total ~549MB including DB and index.
- MCP entry removed from Claude Code and Codex configs.

### codegraph — Removed
- Removed `~/.codegraph/` data dir (~228MB).
- Entry removed from oh-my-openagent plugin's `.mcp.json`.
- Both disabled via `"disabled_mcps": ["codegraph", "tokensave"]` in `oh-my-openagent.json` — survives plugin upgrades.

## Docker — Disabled
- `sudo systemctl stop docker && systemctl disable docker`
- Now inactive. Docker daemon no longer starts on boot.

## apt Mirror Fix
- Default `ph.archive.ubuntu.com` (Philippine mirror) returned 403 on `linux-firmware-amd-misc`
- Fixed by switching to `archive.ubuntu.com` in `/etc/apt/sources.list.d/ubuntu.sources`
- 41 packages remain upgradable (not yet run after fix)

## GDM Wayland Fix
- Intel HD 520 (Skylake) has broken Wayland support on Ubuntu 26.04
- Added `WaylandEnable=false` under `[daemon]` in `/etc/gdm3/custom.conf`
- **Requires reboot** to take effect

## Tools Installed

### FreeHive AI Gateway
- v0.1.0 from GitHub releases (`.deb`), systemd user service on `:7200`
- Routes to Claude/ChatGPT/Gemini via OAuth
- **Needs `claude login`** — auth not yet configured
- Two providers added to opencode.json: `freehive` (Anthropic) + `freehive-oai` (OpenAI)

### lifeos-cli
- v0.21.1 via `uv tool install --upgrade lifeos-cli`
- SQLite DB at `~/.local/share/lifeos/lifeos.db` (632KB)
- Timezone Asia/Manila

### p2d-duck
- v1.3.1 via pipx — commands: `duck-ai`, `p2d-duck`

### ai-wanderer (ai-free-swap)
- v0.2.0 via pipx from `github.com/sshnaidm/ai-wanderer`
- OpenAI/Anthropic-compatible free-tier proxy router with automatic provider fallback
- Command: `ai-free-swap`

### free-claude-code
- Via `uv tool install git+https://github.com/Alishahryar1/free-claude-code.git`
- 6 executables: `fcc-claude`, `fcc-codex`, `fcc-init`, `fcc-pi`, `fcc-server`, `free-claude-code`

### danielmiessler/LifeOS Skill
- v7.1.1 skill placed at `~/.claude/skills/LifeOS/`
- Needs AI harness `/lifeos-setup` command for onboarding conversation

## Topics Covered
1. MCP memory management (tokensave/codegraph removal via `disabled_mcps`)
2. Docker disable — systemd control
3. apt mirror 403 fix — ubuntu.sources edit
4. GDM Wayland disable — custom.conf edit for Intel Skylake
5. FreeHive setup — local AI provider gateway
6. AI tool installs (p2d-duck, ai-wanderer, free-claude-code)
7. LifeOS skill installation

## Key Takeaways
- **disabled_mcps in oh-my-openagent.json** is the cleanest way to disable MCPs without breaking plugin upgrades
- **FreeHive** needs `claude login` before it works — OAuth token required
- **lifeos-cli** and **LifeOS skill** are complementary: CLI for terminal, skill for AI harness integration
- **apt 403 on ph.archive.ubuntu.com** is a known mirror issue — switching to archive.ubuntu.com resolves it
- **Wayland on Intel HD 520** is broken in Ubuntu 26.04 — force Xorg in GDM config

## Decisions Made
- Use `disabled_mcps` for MCP management vs removing plugin entries — survives upgrades
- pipx for Python tools, uv for Python/Rust tools, Bun for JS/TS tools
- FreeHive as primary AI gateway; ai-wanderer as fallback for free-tier routing

## Open Questions
- FreeHive still needs `claude login` — no auth configured yet
- Reboot pending for GDM Wayland fix + zswap activation
- apt upgrade skipped — 41 packages still upgradable
- LifeOS needs AI harness `/lifeos-setup` to complete onboarding

## Related
- [[concepts/MCP Servers]]
- [[concepts/FreeHive]]
- [[concepts/OpenCode]]
- [[skills/gpaste-gnome-wayland]]
