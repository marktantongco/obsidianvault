---
title: GPaste Wayland dock and shortcuts
tags: [gpaste, gnome, wayland, clipboard]
summary: GPaste daemon cannot grab keys on Wayland without extension; use GNOME custom Super+Shift+V; Utility desktop for dock.
project: AI-Second-Brain
capture_source: grok-session
sources:
  - "AI-Second-Brain session (2026-07-09)"
base_confidence: 0.8
provenance:
  extracted: 0.5
  inferred: 0.5
lifecycle: draft
lifecycle_changed: 2026-07-09
created: 2026-07-09T10:00:20Z
---

# GPaste Wayland dock and shortcuts

## Finding
On GNOME Wayland, `GrabAccelerators` is denied for gpaste-daemon without a loaded Shell extension. Register **custom keybindings** to `/usr/bin/gpaste-client ui`.

## Dock
System desktop is under Settings + `edit-paste` action icon — dock may hide it. Override same id with `Categories=Utility` and app icon `org.gnome.GPaste`.

## CopyQ
Keep installed but `Hidden=true` / autostart disabled so only GPaste owns clipboard.

## Promote
→ [[skills/gpaste-gnome-wayland]]
