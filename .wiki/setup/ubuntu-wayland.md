---
title: Ubuntu Wayland Setup
category: config
tags: [ubuntu, wayland, setup, gnome, configuration]
summary: Ubuntu GNOME Wayland configuration and troubleshooting
lifecycle: active
tier: 2
---

# Ubuntu Wayland Setup

## Overview
Configuration notes for Ubuntu running under GNOME Wayland.

## Key Considerations

### Clipboard Managers
Wayland restricts clipboard access compared to X11.
Use Wayland-compatible clipboard managers like CopyQ or GPaste.
See [[tools/clipboard-managers]] for a full comparison.

### Display Protocol
Check which display server is active:
```bash
echo $XDG_SESSION_TYPE
```

### Environment Variables
```bash
# Force Wayland for specific apps
GDK_BACKEND=wayland
QT_QPA_PLATFORM=wayland
```

## Related
- [[config/copyq/README|CopyQ Configuration]]
- [[config/ubuntu-wayland]]
