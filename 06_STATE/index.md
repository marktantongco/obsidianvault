---
title: STATE — Configs, Env & Runtime State
bucket: STATE
path: 06_STATE/
purpose: Configs, env files, runtime state
tags: [bucket, state, configs]
lifecycle: active
tier: core
---

# 06_STATE — Configs, Env & Runtime State

This bucket holds configuration files, environment definitions, and runtime state for the multi-agent system. It is the most populated bucket directory with config-driven content.

## Configuration Files

### Poznote Capture Schema
[[06_STATE/configs/poznote-capture-schema]] — Defines the frontmatter schema, field definitions, and classification rules used by the Poznote pipeline to auto-classify captures into memory buckets.

### SecondBrain Skill Config
[[06_STATE/configs/second-brain-skill]] — LifeOS skill configuration bridging Obsidian vault paths to Memory v7.6 categories. Declares triggers (`new_file_in_raw`, `file_written_to_vault`), tools (`vault_read`, `vault_write`, `memory_sync`), and Pulse API endpoints.

### Sync Strategy
[[06_STATE/configs/sync-strategy]] — Git sync cadence table (desktop 10min commit / 30min push / 5min pull), conflict resolution rules (frontmatter merge, body markers), and disaster recovery procedures.

## Skills Referencing Configs
- [[skills/git-sync-strategy]] — Step-by-step sync setup promoted from config
- [[skills/mobile-sync-termux]] — Mobile sync setup using Termux

## API Key Configuration
- [[API-KEY-GUIDE]] — Guide for obtaining and configuring API keys (OpenAI ✅, Anthropic ⏳, Gemini ⏳, MiMo ⏳)
- Key files (on local machine): `~/.opencode/.env`, `~/.claude/.env`, `~/.hermes/hermes-agent/.env`, `~/.codex/.env`

## Quick-Start & Setup
- [[QUICK-START]] — Essential hotkeys, navigation, vault structure, wiki skills
- [[MANUAL-PLUGIN-INSTALL]] — Obsidian community plugin installation guide
- [[PLUGIN-SETUP]] — Plugin configuration after installation
- [[SYSTEM-COMPLETE]] — Full system inventory
- [[SYSTEM-INSTALLATION-STATUS]] — Per-component installation status

## Related Buckets
- [[05_OBSERVABILITY/index|05_OBSERVABILITY]] — Logs and metrics tracking config changes
- [[02_KNOWLEDGE/index|02_KNOWLEDGE]] — Concepts implemented by these configs
- [[01_WORK/index|01_WORK]] — Projects that modify these configs
