---
title: CopyQ Configuration
category: config
tags: [copyq, clipboard, wayland, gnome, ubuntu]
summary: Optimized CopyQ setup for Ubuntu GNOME Wayland
lifecycle: active
tier: 1
---

# CopyQ Configuration

## Overview
Optimized CopyQ clipboard manager setup for Ubuntu GNOME Wayland.

## Installation
```bash
sudo apt install -y copyq
```

## Enable GNOME Extension
```bash
gnome-extensions enable copyq@hluk.github.com
```

## Configuration Files

### Main Config
Location: `~/.config/copyq/copyq.conf`

```ini
[General]
autostart=true
clipboard_monitor=true
item_limit=10000
ignore_passwords=true

[Clipboard]
check_selection=false
disable=false
ignore_empty=false
ignore_images=false
max_age=0

[Shortcuts]
ctrl+shift+v=menu
ctrl+shift+c=toggle
ctrl+v=paste
return=paste
```

### Autostart
Location: `~/.config/autostart/copyq.desktop`

```ini
[Desktop Entry]
Type=Application
Name=CopyQ
Exec=/home/x1/.local/bin/start-copyq.sh
X-GNOME-Autostart-enabled=true
```

## Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+V` | Toggle clipboard menu |
| `Ctrl+Shift+C` | Toggle CopyQ |
| `Ctrl+V` | Paste selected item |
| `Return` | Paste selected item |
| `Alt+Return` | Paste with newline |
| `Ctrl+Alt+X` | Clear clipboard |

## Commands
```bash
copyq show              # Show main window
copyq hide              # Hide main window
copyq menu              # Show clipboard menu
copyq toggle            # Toggle main window
copyq clear             # Clear clipboard
copyq clipboard         # Print clipboard content
copyq copy "text"       # Copy text to clipboard
copyq tab "Tab Name"    # Create/switch to tab
```

## Troubleshooting

### Clipboard monitoring not working
```bash
gnome-extensions list | grep copyq
gnome-extensions enable copyq@hluk.github.com
```

### Restart CopyQ
```bash
copyq --quit
copyq &
```

### Check logs
```bash
copyq log
```

## Related
- [[config/ubuntu-wayland]]
- [[tools/clipboard-managers]]
