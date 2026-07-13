#!/usr/bin/env bash
# Mobile sync setup for Obsidian vault via Termux
# Prerequisites: Termux + Termux:API + Termux:Widget (optional)
set -euo pipefail

echo "=== Obsidian Mobile Sync Setup ==="

# 1. Install dependencies
pkg update -y
pkg install -y git openssh termux-services

# 2. Configure SSH for Git
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Generate key if not present
if [ ! -f ~/.ssh/id_ed25519 ]; then
  ssh-keygen -t ed25519 -C "termux@mobile" -f ~/.ssh/id_ed25519 -N ""
  echo ""
  echo "=== ADD THIS PUBLIC KEY TO YOUR GIT HOST ==="
  cat ~/.ssh/id_ed25519.pub
  echo ""
  echo "Press Enter after adding the key..."
  read -r
fi

# 3. Clone vault
VAULT_DIR="$HOME/obsidianvault"
REMOTE_URL="git@github.com:YOUR_USER/obsidianvault.git"  # EDIT THIS

if [ ! -d "$VAULT_DIR/.git" ]; then
  git clone "$REMOTE_URL" "$VAULT_DIR"
fi

# 4. Configure git
cd "$VAULT_DIR"
git config user.name "Termux"
git config user.email "termux@mobile.local"

# 5. Set up auto-sync via cron (every 10 minutes)
CRON_CMD="*/10 * * * * cd $VAULT_DIR && git pull --rebase && git add -A && git diff --cached --quiet || git commit -m '[mobile] auto-sync' && git push"
(crontab -l 2>/dev/null | grep -v "obsidianvault"; echo "$CRON_CMD") | crontab -

# 6. Create sync widget (if Termux:Widget installed)
WIDGET_DIR="$HOME/.shortcuts"
mkdir -p "$WIDGET_DIR"
cat > "$WIDGET_DIR/vault-sync.sh" << 'WIDGET'
#!/usr/bin/env bash
cd ~/obsidianvault
git pull --rebase
git add -A
git diff --cached --quiet || git commit -m "[mobile] manual sync"
git push
echo "Sync complete" | xargs -I{} termux-notification --title "Vault Sync" --content "{}"
WIDGET
chmod +x "$WIDGET_DIR/vault-sync.sh"

echo "=== Setup complete ==="
echo "Vault: $VAULT_DIR"
echo "Cron: every 10 minutes auto-sync"
echo "Widget: tap vault-sync for manual sync"
