---
title: Git Sync & Conflict Strategy
category: skills
tags:
  - git
  - sync
  - obsidian
  - mobile
  - conflict
  - backup
created: 2026-07-21
updated: 2026-07-21
summary: >-
  Step-by-step guide for setting up and managing git sync across desktop and
  mobile for the Obsidian vault. Covers initial config, per-device cadence,
  conflict resolution, and disaster recovery.
lifecycle: draft
tier: supporting
source: opencode
confidence: 0.85
---

# Git Sync & Conflict Strategy

## Overview

This skill covers git-based sync for the Obsidian vault across multiple devices. The vault uses [[concepts/Obsidian Wiki|Obsidian Git plugin]] for automated sync on desktop and either the plugin or Termux cron on mobile.

The canonical sync rules are defined in `06_STATE/configs/sync-strategy.md`. This skill provides step-by-step setup and operational commands.

---

## Initial Setup

### 1. Configure Git Identity

The vault uses a shared identity for automated commits:

```bash
git config user.name "Hermes"
git config user.email "hermes@secondbrain.local"
```

### 2. Set Remote Origin

```bash
git remote add origin https://github.com/marktantongco/obsidianvault.git
```

### 3. Initial Push

```bash
git add -A
git commit -m "[setup] Initial vault push"
git push -u origin main
```

---

## Per-Device Sync Cadence

### Desktop (Primary) — Obsidian Git Plugin

Configure in `.obsidian/plugins/obsidian-git/data.json`:

```json
{
  "autoCommitInterval": 10,
  "autoPushInterval": 30,
  "autoPullInterval": 5,
  "mergeStrategy": "standard"
}
```

| Operation | Frequency | Command |
|-----------|-----------|---------|
| Auto commit | Every 10 min | Plugin handles |
| Auto push | Every 30 min | Plugin handles |
| Auto pull | Every 5 min | Plugin handles |
| Manual sync | As needed | `Ctrl+Shift+G` → Commit/Push |

### Mobile (Plugin) — Obsidian Git on Android

```json
{
  "autoCommitInterval": 10,
  "autoPushInterval": 30,
  "autoPullOnStartup": true,
  "mergeStrategy": "theirs"
}
```

| Operation | Frequency | Command |
|-----------|-----------|---------|
| Auto commit | Every 10 min | Plugin handles |
| Auto push | Every 30 min | Plugin handles |
| Auto pull | On startup | Plugin handles |

### Mobile (Termux) — CLI Cron

```bash
# Install termux-services
pkg install termux-services

# Create sync script at ~/bin/vault-sync.sh
cat > ~/bin/vault-sync.sh << 'SCRIPT'
#!/data/data/com.termux/files/usr/bin/bash
cd /data/data/com.termux/files/home/storage/shared/obsidianvault
git pull --rebase --strategy-option=theirs
git add -A
git commit -m "[mobile] $(date '+%Y-%m-%d %H:%M') auto-sync"
git push
SCRIPT

chmod +x ~/bin/vault-sync.sh

# Add cron job (runs every 10 minutes)
crontab -e
# Add: */10 * * * * ~/bin/vault-sync.sh
```

---

## Conflict Resolution

### Types of Conflicts

| Type | How It Happens | Resolution |
|------|---------------|------------|
| **Frontmatter** | Both devices edit metadata | Auto-merge: union of keys. `created` keeps earliest. `updated` keeps latest. |
| **Body** | Both devices edit markdown body | Insert conflict markers `<<<<<<< HEAD`. Do NOT auto-resolve. Flag for manual review. |
| **File rename** | File renamed on both sides | Prefer newer timestamp. Git tracks renames. |
| **Binary** | Attachment >1MB | Never commit. Use `.gitignore` + external storage (NAS, S3-compatible). |

### Automated Frontmatter Merge

When frontmatter conflicts, merge rules are:

```python
# Pseudocode for the merge logic
merged_frontmatter = {}
for key in union(ours.keys(), theirs.keys()):
    if key == "created":
        merged_frontmatter[key] = min(ours[key], theirs[key])  # earliest
    elif key == "updated":
        merged_frontmatter[key] = max(ours[key], theirs[key])  # latest
    else:
        merged_frontmatter[key] = ours[key]  # ours wins for all other keys
```

### Manual Body Conflict Resolution

1. Open the conflicted file
2. Locate conflict markers: `<<<<<<< HEAD`, `=======`, `>>>>>>>`
3. Review both versions
4. Keep one, merge both, or rewrite
5. Remove conflict markers
6. Save and stage:

```bash
git add conflicted-file.md
git commit -m "[hermes] Resolved merge conflict in conflicted-file.md"
```

### Simultaneous Edit Handling

Mobile captures are quick notes (Poznote-style). Desktop edits are deep work.

- **Rule**: Mobile pushes first → desktop pulls → gets merge conflict
- **Resolution**: Desktop user reviews conflict markers, keeps both versions if unsure
- **Prevention**: Mobile uses `_raw/poznote/` for captures (append-only, rarely conflicts). Desktop organizes into final buckets.
- **Worst case**: Hermes routes to E2 (Codex) for resolution suggestion via LifeOS Algorithm

---

## Disaster Recovery

| Scenario | Recovery Commands |
|----------|-------------------|
| **Vault corruption** | `git reflog` → find last good commit → `git reset --hard <hash>` |
| **Remote repo compromised** | Local clone is backup. Re-init remote, force push from known-good local. |
| **Mobile edit lost** | Check `git stash list`. Poznote retains original until pipeline processes. |
| **Simultaneous edit conflict** | Frontmatter auto-merged. Body gets conflict markers. |

### Full Recovery Walkthrough

#### Revert to Last Good Commit

```bash
# Find the last commit before corruption
git reflog

# Hard reset to known good state
git reset --hard <commit-hash>

# Force push to remote (if needed)
git push --force-with-lease origin main
```

#### Restore Locally-Only Changes

```bash
# Find stashed changes
git stash list

# Apply a specific stash
git stash apply stash@{0}

# Or pop (apply + drop)
git stash pop stash@{0}
```

---

## Related

- [[06_STATE/configs/sync-strategy]] — Canonical config with cadence table and conflict rules
- [[concepts/Obsidian Wiki]] — The vault being synced
- [[concepts/poznote-pipeline]] — Capture pipeline that feeds into git sync
- [[concepts/LifeOS Algorithm]] — Routes conflict resolution tasks to appropriate agent tier
