---
title: Manual Plugin Installation
category: reference
created: 2026-07-09
updated: 2026-07-09
tags: [plugins, installation, manual]
lifecycle: active
tier: supporting
---

# Manual Plugin Installation

**Status**: GitHub API rate limited - manual installation required

---

## Quick Install Steps

### Step 1: Open Obsidian Settings
- Press `Ctrl+,` or click Settings gear icon

### Step 2: Enable Community Plugins
- Go to **Community Plugins** in left sidebar
- Click **Turn on community plugins** if not already enabled

### Step 3: Browse Plugins
- Click **Browse** button
- Search for each plugin name below

### Step 4: Install & Enable
- Click **Install** on each plugin
- Click **Enable** after installation

---

## Plugins to Install

### 1. Dataview
- **Search**: "Dataview"
- **Author**: Michael Brenan
- **Purpose**: Query and display data from your vault
- **After Install**: Settings → Dataview → Enable JavaScript Queries

### 2. Calendar
- **Search**: "Calendar"
- **Author**: Liam Cain
- **Purpose**: Calendar view for daily notes
- **After Install**: Settings → Calendar → Configure display options

### 3. Templater
- **Search**: "Templater"
- **Author**: SilentVoid13
- **Purpose**: Advanced template system
- **After Install**: Settings → Templater → Set Template Folder: `templates`

### 4. Kanban
- **Search**: "Kanban"
- **Author**: Matt Peerce
- **Purpose**: Kanban boards for task management
- **After Install**: Create new Kanban board via Command Palette

### 5. Tasks
- **Search**: "Tasks"
- **Author**: Martin Schenck
- **Purpose**: Task tracking across vault
- **After Install**: Settings → Tasks → Configure default priority

### 6. Excalidraw
- **Search**: "Excalidraw"
- **Author**: Zsolt Viczian
- **Purpose**: Drawing and diagramming
- **After Install**: Create new Excalidraw drawing via Command Palette

---

## Plugin Configuration

### After Installing All Plugins

#### Dataview Settings
1. Settings → Dataview
2. Enable: **Enable JavaScript Queries**
3. Enable: **Enable Inline Queries**
4. Enable: **Enable Inline Queries in Code Blocks**

#### Calendar Settings
1. Settings → Calendar
2. Enable: **Show week number**
3. Set: **Start week on** (Monday recommended)

#### Templater Settings
1. Settings → Templater
2. Set: **Template folder location** = `templates`
3. Enable: **Trigger Templater on new file creation**

#### Tasks Settings
1. Settings → Tasks
2. Set: **Default priority** = Normal
3. Enable: **Auto-suggest in edit mode**

---

## Hotkeys to Configure

After installing, set these hotkeys in Settings → Hotkeys:

| Action | Hotkey |
|--------|--------|
| Dataview: Refresh | Ctrl+Shift+R |
| Calendar: Open | Ctrl+Shift+C |
| Templater: Insert Template | Ctrl+Shift+T |
| Kanban: Create new board | Ctrl+Shift+K |
| Tasks: Create new task | Ctrl+Shift+Alt+T |
| Excalidraw: Create new | Ctrl+Shift+E |

---

## Verification

After installing all plugins, verify they work:

1. Open Command Palette (`Ctrl+Shift+P`)
2. Type "Dataview" — should show Dataview commands
3. Type "Calendar" — should show Calendar commands
4. Type "Templater" — should show Templater commands
5. Type "Kanban" — should show Kanban commands
6. Type "Tasks" — should show Tasks commands
7. Type "Excalidraw" — should show Excalidraw commands

If all commands appear, plugins are installed correctly.

---

## Troubleshooting

### Plugin Not Appearing
1. Check if Community Plugins is enabled
2. Restart Obsidian
3. Check plugin folder: `~/obsidianvault/.obsidian/plugins/`

### Plugin Not Working
1. Check plugin is enabled in Settings
2. Check plugin version is compatible
3. Check for conflicts with other plugins

### Reinstall Plugin
1. Settings → Community Plugins
2. Find plugin in installed list
3. Click Uninstall
4. Reinstall via Browse

---

## Alternative: Install via Script

If GitHub API becomes available again:

```bash
# Run the installer script
cd ~/obsidianvault
bash install-plugins.sh
```

---

## Notes

- GitHub API rate limiting prevented automatic installation
- Manual installation through Obsidian GUI is reliable
- All plugins are free and open source
- Plugins update automatically through Obsidian

## Related

- [[PLUGIN-SETUP]] — Plugin configuration guide with hotkeys and settings
- [[SYSTEM-ACTIVATION]] — Full system activation guide
- [[TROUBLESHOOTING]] — Common issues and debugging
- [[SYSTEM-INSTALLATION-STATUS]] — Installation status overview
