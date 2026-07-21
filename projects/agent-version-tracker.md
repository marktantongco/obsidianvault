---
title: Agent Version Tracker
type: reference
created: 2026-07-21
updated: 2026-07-21
tags:
  - agents
  - versions
  - tracking
  - changelog
---

# Agent Version Tracker

## Overview

Single-page reference for all agent and tool versions in the multi-agent AI development environment. Update this page whenever an agent is upgraded or a new version is installed.

---

## Installed Agents & Tools

### Core CLI Agents

| Agent | Version | Installed | Install Method | Binary Location | Skills |
|-------|---------|-----------|----------------|-----------------|--------|
| [[concepts/OpenCode\|OpenCode]] | v1.17.15¹ | 2026-07-09 | `curl -fsSL https://opencode.ai/install \| bash` | `~/.opencode/bin/opencode` | 37 |
| [[concepts/Hermes Agent\|Hermes Agent]] | v0.18.2 (2026.7.7.2) | 2026-07-09 | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` | `~/.hermes/hermes-agent/.venv/bin/hermes` | 36 |
| [[concepts/Claude Code\|Claude Code]] | v2.1.205 | 2026-07-09 | `npm install -g @anthropic-ai/claude-code` | `~/.local/bin/claude` | 37 |
| [[concepts/OpenAI Codex\|OpenAI Codex]] | v0.143.0 | 2026-07-09 | `npm install -g @openai/codex` | `~/.local/bin/codex` | — |
| [[concepts/MiMo Code\|MiMo Code]] | v0.1.5 | 2026-07-09 | `npm install -g @mimo-ai/cli` | `~/.local/bin/mimo` | — |
| [[concepts/Grok\|Grok]] | v0.2.93 | 2026-07-09 | `curl -fsSL https://grok.com/install \| bash` | `~/.grok/bin/grok` | — |

¹ OpenCode: concept page says v1.17.15, SYSTEM-COMPLETE says v1.17.16. Needs verification.

### Infrastructure & Knowledge System

| Component | Version | Installed | Details |
|-----------|---------|-----------|---------|
| [[concepts/system-prompt-v5-1-1\|System Prompt]] | v5.1.1 | 2026-07-13 | Negative-constraint cognitive modes |
| [[concepts/Obsidian Wiki\|obsidian-wiki]] | v2026.7.2 | 2026-07-09 | Skill framework + compile pattern |
| [[concepts/FreeHive\|FreeHive AI Gateway]] | v0.1.0 | 2026-07-14 | `.deb` from GitHub, systemd user service on `:7200` |

### Secondary CLI Tools

| Tool | Version | Installed | Install Method | Command(s) |
|------|---------|-----------|----------------|------------|
| [[entities/lifeos-cli\|lifeos-cli]] | v0.21.1 | 2026-07-14 | `uv tool install --upgrade lifeos-cli` | `lifeos` |
| [[entities/ai-wanderer\|ai-wanderer]] | v0.2.0 | 2026-07-14 | `pipx install` from `github.com/sshnaidm/ai-wanderer` | `ai-free-swap` |
| [[entities/p2d-duck\|p2d-duck]] | v1.3.1 | 2026-07-14 | `pipx install p2d-duck` | `duck-ai`, `p2d-duck` |
| [[entities/free-claude-code\|free-claude-code]] | — | 2026-07-14 | `uv tool install git+...` | `fcc-claude`, `fcc-codex`, `fcc-init`, `fcc-pi`, `fcc-server` |

### AI Harness Skills

| Skill | Version | Installed | Location |
|-------|---------|-----------|----------|
| LifeOS AI harness skill | v7.1.1 | 2026-07-14 | `~/.claude/skills/LifeOS/` |
| graphify | — | — | `~/.claude/skills/graphify/SKILL.md` |

### Desktop Apps

| App | Version | Installed | Location |
|-----|---------|-----------|----------|
| Obsidian | AppImage | 2026-07-09 | `~/Applications/Obsidian.AppImage` |
| Simplenote | .deb | 2026-07-09 | `~/Applications/Simplenote/` |

---

## Agent Bridge Versions

| Bridge | Location | Status |
|--------|----------|--------|
| Hermes-OpenCode | `~/.hermes/plugins/opencode/` | ✅ Installed |
| Hermes-Claude | `~/.hermes/plugins/code-bridge/` | ✅ Installed |

---

## Version Change Log

| Date | Component | Old Version | New Version | Notes |
|------|-----------|-------------|-------------|-------|
| 2026-07-13 | System Prompt | v5.1 | **v5.1.1** | Negative constraints introduced |
| 2026-07-14 | FreeHive | — | **v0.1.0** | Fresh install |
| 2026-07-14 | lifeos-cli | — | **v0.21.1** | Fresh install |
| 2026-07-14 | ai-wanderer | — | **v0.2.0** | Fresh install |
| 2026-07-14 | p2d-duck | — | **v1.3.1** | Fresh install |
| 2026-07-14 | free-claude-code | — | — | Fresh install |
| 2026-07-14 | LifeOS skill | — | **v7.1.1** | Fresh install |

---

## System Runtime

| Component | Version |
|-----------|---------|
| OS | Ubuntu 26.04 (resolute) |
| CPU | Intel i5-6200U (Skylake) |
| GPU | Intel HD 520 |
| RAM | 7.1 GB |
| Bun | 1.3.14 |
| Node.js | v22.14.0 |
| Python | 3.10.12 (system), 3.11 (hermes venv) |

---

## Related

- [[concepts/AI Agents]] — Agent descriptions
- [[concepts/system-prompt-v5-1-1]] — Master prompt governing all agents
- [[projects/AI-Second-Brain]] — Project context
- [[SYSTEM-COMPLETE]] — Full system inventory
- [[SYSTEM-INSTALLATION-STATUS]] — Installation status per component
