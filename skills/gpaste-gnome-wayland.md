---
title: GPaste on GNOME Wayland
category: skills
tags: [gpaste, gnome, wayland, clipboard, ubuntu]
sources:
  - conversation:2026-07-09
summary: Install and dock-pin GPaste on Ubuntu GNOME Wayland; custom Super+Shift+V; disable CopyQ.
provenance: {extracted: 0.8, inferred: 0.2, ambiguous: 0.0}
base_confidence: 0.7
lifecycle: draft
lifecycle_changed: 2026-07-09
tier: supporting
created: 2026-07-09T09:57:44Z
updated: 2026-07-09T10:44:46Z
relationships:
  - target: "[[entities/GPaste]]"
    type: implements
  - target: "[[entities/CopyQ]]"
    type: replaces
---

# GPaste on GNOME Wayland

## Install
```bash
sudo apt install gpaste-2 gnome-shell-extension-gpaste
systemctl --user enable --now org.gnome.GPaste.service
```

## Gotchas
- Daemon alone **cannot** grab accelerators on Wayland without Shell extension (`GrabAccelerators` AccessDenied).
- Use **GNOME custom shortcuts** → `/usr/bin/gpaste-client ui`.
- Settings-category desktop files hide poorly on Ubuntu Dock — override Categories to Utility + app icon.
- Enabling only GPaste in `enabled-extensions` **disables Ubuntu Dock** — always keep `ubuntu-dock@ubuntu.com`.

## Shortcuts (configured)
| Super+Shift+V | Open GPaste UI |
| Super+Shift+H | Preferences |

## Related
- [[entities/GPaste]] · [[entities/CopyQ]] · [[concepts/Development Workflow]]

## Session notes (promoted 2026-07-09)

# GPaste Wayland dock and shortcuts

## Finding
On GNOME Wayland, `GrabAccelerators` is denied for gpaste-daemon without a loaded Shell extension. Register **custom keybindings** to `/usr/bin/gpaste-client ui`.

## Dock
System desktop is under Settings + `edit-paste` action icon — dock may hide it. Override same id with `Categories=Utility` and app icon `org.gnome.GPaste`.

## CopyQ
Keep installed but `Hidden=true` / autostart disabled so only GPaste owns clipboard.

## Promote
→ [[skills/gpaste-gnome-wayland]]
