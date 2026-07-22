---
title: Multi-agent vault wiring gotchas
tags: [obsidian, agents, symlink, configuration]
summary: Single vault for all CLIs via ~/.obsidian-wiki/config + skill/vault symlinks; do not empty enabled-extensions.
project: AI-Second-Brain
capture_source: grok-session
sources:
  - "AI-Second-Brain session (2026-07-09)"
base_confidence: 0.75
provenance:
  extracted: 0.4
  inferred: 0.6
lifecycle: draft
lifecycle_changed: 2026-07-09
created: 2026-07-09T10:00:20Z
tier: peripheral
---

# Multi-agent vault wiring gotchas

## Finding
Point every CLI at **one** vault (`/home/x1/obsidianvault`) via `~/.obsidian-wiki/config`, skill symlinks into package/repo `.skills/`, and `~/.<agent>/obsidian-vault` symlinks. Host + vault `AGENTS.md` must require vault load every session.

## Gotchas
- `obsidian-wiki setup` can thin global config — re-add `OBSIDIAN_WIKI_REPO` / `OBSIDIAN_SOURCES_DIR` after setup.
- Setting `enabled-extensions` to only GPaste **disables Ubuntu Dock** — always keep `ubuntu-dock@ubuntu.com`.
- Prefer symlink skills over copies so upgrades propagate.

## Promote
Run wiki-ingest to merge into [[skills/multi-agent-vault-wiring]].
