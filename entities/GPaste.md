---
title: GPaste
category: entities
tags:
  - tool
  - clipboard
  - gnome
  - wayland
sources:
  - conversation:2026-07-09
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - skills/gpaste-gnome-wayland
  - journal/2026-07-09-multi-agent-wiki-compound
summary: >-
  GNOME clipboard manager (gpaste-2) preferred over CopyQ on GNOME Wayland.
  Configured with Super+Shift+V custom shortcut. Requires gpaste-2 daemon,
  gnome-shell-extension-gpaste, and custom GNOME shortcut config.
provenance:
  extracted: 0.7
  inferred: 0.3
  ambiguous: 0.0
base_confidence: 0.7
lifecycle: draft
tier: supporting
created: 2026-07-09T09:57:44Z
updated: 2026-07-21T08:00:00Z
---

# GPaste

## Overview

GPaste is the active clipboard manager on this system, preferred over [[entities/CopyQ]] on GNOME Wayland. It provides native GNOME integration with clipboard history, search, and configurable shortcuts.

## Key Facts

- **Version**: gpaste-2 (GPaste 2.x series for GNOME)
- **Type**: GNOME clipboard manager (native GTK)
- **Status**: Active — replaced CopyQ
- **Components**:
  - `gpaste-2` — Core daemon and CLI tool
  - `gnome-shell-extension-gpaste` — GNOME Shell integration

## Configuration

### Installation
```bash
sudo apt install gpaste-2 gnome-shell-extension-gpaste
```

### Custom Shortcut (Super+Shift+V)
Per [[skills/gpaste-gnome-wayland|GPaste on GNOME Wayland]]:

1. GNOME Settings → Keyboard → View and Customize Shortcuts
2. Custom Shortcuts → Add
3. **Name**: GPaste History
4. **Command**: `gpaste-client history`
5. **Shortcut**: Super+Shift+V

### Dock Pin
- Search for "GPaste" in Activities
- Right-click the Utilities category launcher → Add to Favorites

### CLI Usage
```bash
# View clipboard history
gpaste-client history

# Search clipboard
gpaste-client search <query>

# Show current item
gpaste-client get-current

# Select specific item
gpaste-client select <index>
```

## Important: Extension Conflict

Per the [[journal/2026-07-09-multi-agent-wiki-compound|July 9 session]] and [[skills/gpaste-gnome-wayland]]:

- Setting `enabled-extensions` to **only** GPaste **disables Ubuntu Dock**
- Always keep `ubuntu-dock@ubuntu.com` in the enabled extensions list

## Related

- [[entities/CopyQ]] — Replaced clipboard manager (inactive)
- [[skills/gpaste-gnome-wayland]] — Full setup guide
- [[journal/2026-07-09-multi-agent-wiki-compound]] — Session documenting the switch
