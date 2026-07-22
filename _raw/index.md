---
title: _raw — Staging & Raw Captures
category: raw
tags: [staging, raw-captures, index]
purpose: "Inbox-style directory for raw note captures before they're processed into permanent vault pages"
summary: "Staging directory with 2 active raw captures and 5 archived notes. Raw captures are unprocessed inbound notes; archived notes have been superseded by permanent vault pages."
lifecycle: active
tier: peripheral
---

# _raw — Staging & Raw Captures

This directory serves as the vault's **inbox** — raw captures and unprocessed notes that haven't been distilled into permanent concept, entity, or skill pages.

## Active Raw Captures

| Note | Date | Status |
|------|------|--------|
| [[_raw/2026-07-09-multi-agent-setup-gotchas\|Multi-Agent Setup Gotchas]] | 2026-07-09 | 📥 Unprocessed |
| [[_raw/2026-07-13-opencode-free-model-config\|OpenCode Free Model Config]] | 2026-07-13 | 📥 Unprocessed |

## Archived Notes

These notes have been superseded by permanent vault pages:

| Archived Note | Superseded By |
|---------------|---------------|
| [[_raw/_archived/2026-07-09-free-china-proxy-direct-first\|Free China Proxy Direct-First]] | [[skills/free-china-proxy-ops]] |
| [[_raw/_archived/2026-07-09-gpaste-wayland-dock\|GPaste Wayland Dock]] | [[skills/gpaste-gnome-wayland]] |
| [[_raw/_archived/2026-07-09-multi-agent-vault-wiring\|Multi-Agent Vault Wiring]] | [[skills/multi-agent-vault-wiring]] |
| [[_raw/_archived/2026-07-09-wiki-compound-habit\|Wiki Compound Habit]] | [[skills/wiki-compound-loop]] |
| [[_raw/_archived/2026-07-14-session-state-tool-installs\|Session State Tool Installs]] | [[journal/2026-07-14-system-admin-tool-installs]] |

## Workflow

1. **Capture** → Place raw notes in `_raw/`
2. **Process** → Distill into a proper page (concept, entity, skill, etc.)
3. **Archive** → Move processed notes to `_raw/_archived/`
4. **Link** → Add a cross-reference from the archived note to its superseding page

## Related
- [[02_KNOWLEDGE/index|02_KNOWLEDGE]] — Distilled knowledge from processed captures
- [[concepts/poznote-pipeline]] — Capture pipeline automation
