---
title: Mobile Vault Sync via Termux
category: skills
tags:
  - mobile
  - termux
  - sync
  - git
  - android
  - cron
created: 2026-07-21
updated: 2026-07-21
summary: >-
  Set up vault git sync on Android using Termux. Covers Termux installation,
  storage permissions, git setup, cron job configuration, and troubleshooting
  for spotty mobile connectivity.
lifecycle: draft
tier: supporting
source: opencode
confidence: 0.7
---

# Mobile Vault Sync via Termux

## Overview

This skill covers syncing the Obsidian vault on Android devices using Termux. It's designed for mobile capture sessions (quick notes via Poznote-style `_raw/` drops) where the vault needs to push to and pull from the remote git repository.

The canonical sync cadence and conflict strategies are defined in [[skills/git-sync-strategy]]. This skill focuses specifically on the Termux/Android setup.

---

## Prerequisites

- Android device with Termux installed
- Termux:API add-on (for storage access)
- Obsidian vault cloned to the device
- Termux cron (termux-services) for automation

---

## Step-by-Step Setup

### 1. Install Termux & Dependencies

```bash
# Update packages
pkg update && pkg upgrade

# Install git
pkg install git

# Install termux-services for cron
pkg install termux-services

# Add storage access
termux-setup-storage
# → Grant storage permission when prompted
```

### 2. Clone the Vault

```bash
# Navigate to shared storage
cd ~/storage/shared

# Clone the vault
git clone https://github.com/marktantongco/obsidianvault.git

# Configure git identity
cd obsidianvault
git config user.name "Hermes"
git config user.email "hermes@secondbrain.local"
```

### 3. Verify Access

```bash
# Check remote URL
git remote -v
# → origin  https://github.com/marktantongco/obsidianvault.git

# Pull latest
git pull --rebase --strategy-option=theirs
```

### 4. Create Sync Script

```bash
mkdir -p ~/bin

cat > ~/bin/vault-sync.sh << 'SCRIPT'
#!/data/data/com.termux/files/usr/bin/bash
#
# Vault sync script for Termux
# Handles: pull → add → commit → push
# Uses theirs strategy for mobile (local captures win on conflict)

VAULT_PATH="/data/data/com.termux/files/home/storage/shared/obsidianvault"
LOG_FILE="/data/data/com.termux/files/home/vault-sync.log"

cd "$VAULT_PATH" || {
  echo "[$(date '+%Y-%m-%d %H:%M')] ERROR: vault path not found" >> "$LOG_FILE"
  exit 1
}

# Pull latest with theirs strategy
git pull --rebase --strategy-option=theirs >> "$LOG_FILE" 2>&1 || {
  echo "[$(date '+%Y-%m-%d %H:%M')] WARN: pull failed, continuing" >> "$LOG_FILE"
}

# Stage all changes (captures, new notes)
git add -A >> "$LOG_FILE" 2>&1

# Commit if there are changes
if ! git diff --cached --quiet; then
  git commit -m "[mobile] $(date '+%Y-%m-%d %H:%M') auto-sync" >> "$LOG_FILE" 2>&1

  # Push (handle transient network failures)
  git push >> "$LOG_FILE" 2>&1 || {
    echo "[$(date '+%Y-%m-%d %H:%M')] WARN: push failed, will retry next cycle" >> "$LOG_FILE"
  }
fi

echo "[$(date '+%Y-%m-%d %H:%M')] Sync complete" >> "$LOG_FILE"
SCRIPT

chmod +x ~/bin/vault-sync.sh
```

### 5. Set Up Cron Job

```bash
# Start cron daemon
sv-enable crond

# Edit crontab
crontab -e
```

Add the following line to run every 10 minutes:

```cron
*/10 * * * * ~/bin/vault-sync.sh
```

### 6. Test the Setup

```bash
# Run the sync script manually
~/bin/vault-sync.sh

# Check the log
cat ~/vault-sync.log
```

---

## Sync Strategy

Mobile uses the `theirs` merge strategy:

- **Local captures (additions)**: Keep — these are new notes dropped in `_raw/poznote/`
- **Remote changes (edits)**: Accept — these are desktop deep work sessions
- **Conflicts**: Accept remote version on body conflicts; frontmatter is auto-merged

This is safe because:
- Mobile captures go to `_raw/poznote/` (append-only, rarely conflicts)
- Desktop edits go to numbered buckets (never written by mobile)
- The staging area is a one-way inbox, not an editing workspace

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `Permission denied` | Storage not granted | Run `termux-setup-storage` again |
| `git: remote-https not found` | git not fully installed | `pkg install git` |
| `Could not resolve host` | No network | Wait for connectivity, cron retries |
| `Merge conflict` | Both devices edited same file | Check `_raw/poznote/` for duplicates, remove one |
| Cron not running | termux-services not started | `sv-enable crond` then reboot Termux |

### Check Sync Log

```bash
tail -20 ~/vault-sync.log
```

### Force Sync

```bash
cd ~/storage/shared/obsidianvault
git pull --rebase --strategy-option=theirs
git add -A
git commit -m "[mobile] $(date '+%Y-%m-%d %H:%M') manual sync"
git push
```

---

## Security Notes

- The vault git remote uses HTTPS — credentials are managed by the device's credential helper
- If using a PAT or deploy token, store it in `~/.git-credentials`:

```bash
git config --global credential.helper store
# First push will prompt for credentials, then cache them
```

> ⚠️ **Important**: Per the vault's sync rules, never commit binaries >1MB to git. Ensure `.gitignore` covers workspace files, trash, and large attachments.

## Related

- [[skills/git-sync-strategy]] — Full git sync strategy with desktop, mobile plugin, and conflict rules
- [[concepts/poznote-pipeline]] — Capture pipeline that mobile feeds into
- [[06_STATE/configs/sync-strategy]] — Canonical sync config
- [[concepts/Obsidian Wiki]] — The vault being synced
