#!/usr/bin/env bash
# Archive local Claude Code sessions to a dedicated logs branch in git
set -euo pipefail

VAULT_DIR="$HOME/obsidianvault"
CLAUDE_SESSIONS_DIR="$HOME/.claude/sessions"
TEMP_DIR="/tmp/vault-logs-archive"

echo "=== Archiving local session logs to Git Branch ==="

if [ ! -d "$CLAUDE_SESSIONS_DIR" ] || [ -z "$(ls -A "$CLAUDE_SESSIONS_DIR" 2>/dev/null)" ]; then
  echo "No sessions found to archive. Local workspace is already clean."
  exit 0
fi

# Clone vault to temp directory
rm -rf "$TEMP_DIR"
git clone "$VAULT_DIR" "$TEMP_DIR"
cd "$TEMP_DIR"

# Checkout or create logs branch
if git show-ref --verify --quiet refs/remotes/origin/logs; then
  git checkout logs
  git pull origin logs
else
  git checkout --orphan logs
  git rm -rf .
fi

# Move files from local sessions to temp dir
mkdir -p sessions
cp -r "$CLAUDE_SESSIONS_DIR"/* sessions/

# Add, commit and push
git add sessions/
git commit -m "chore: archive session logs $(date +'%Y-%m-%d %H:%M')"
git push origin logs

# Clear local session logs to restore space
rm -rf "$CLAUDE_SESSIONS_DIR"/*
echo "Success! Session logs moved to remote 'logs' branch. Local sessions directory cleared."
