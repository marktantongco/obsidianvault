---
title: Quick Start Guide
---

# Quick Start Guide

## Essential Hotkeys

| Action | Hotkey |
|--------|--------|
| Quick Switcher | Ctrl+O |
| Command Palette | Ctrl+Shift+P |
| Daily Note | Ctrl+D |
| Insert Template | Ctrl+Shift+T |
| Graph View | Ctrl+Shift+G |
| Search | Ctrl+F |
| Toggle Checkbox | Ctrl+Enter |

## Navigation

- **File Explorer**: Left sidebar
- **Backlinks**: Right sidebar
- **Graph View**: Ctrl+Shift+G
- **Tag Pane**: Right sidebar

## Creating Notes

1. **New Note**: Ctrl+N
2. **From Template**: Ctrl+Shift+T → Select template
3. **Daily Note**: Ctrl+D

## Wiki Skills

From any project directory, use these commands:

```bash
# Query the wiki
wiki-query @personal What do I know about X?

# Capture a finding
wiki-capture --quick "Important discovery"

# Update wiki
wiki-update
```

## Agent Integration

All agents are linked to the wiki:

- **OpenCode**: `~/.opencode/skills/`
- **Hermes**: `~/.hermes/skills/`
- **Claude**: `~/.claude/skills/`

## Vault Structure

```
~/obsidianvault/
├── concepts/          # Core concepts
├── entities/          # People, organizations
├── projects/          # Active projects
├── references/        # External references
├── synthesis/         # Cross-cutting analysis
├── journal/           # Daily notes
├── templates/         # Note templates
├── index.md           # Wiki index
├── hot.md             # Recent activity
└── log.md             # Query log
```

## Next Steps

1. Install community plugins (see PLUGIN-SETUP.md)
2. Configure plugin settings
3. Start creating notes
4. Test wiki-query skill
5. Build your first project
