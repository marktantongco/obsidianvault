---
title: Troubleshooting Guide
category: reference
created: 2026-07-09
updated: 2026-07-09
tags: [troubleshooting, debugging, reference]
lifecycle: active
tier: supporting
---

# Troubleshooting Guide

**Last Updated**: 2026-07-09

---

## Quick Diagnostics

Run these commands to check system status:

```bash
# Check all installations
echo "=== Installation Check ==="
which opencode && echo "✓ OpenCode" || echo "✗ OpenCode"
which mimo && echo "✓ MiMo" || echo "✗ MiMo"
which claude && echo "✓ Claude" || echo "✗ Claude"
which codex && echo "✓ Codex" || echo "✗ Codex"
which hermes && echo "✓ Hermes" || echo "✗ Hermes"
which grok && echo "✓ Grok" || echo "✗ Grok"

# Check versions
echo "=== Version Check ==="
opencode --version 2>&1 | head -1
mimo --version 2>&1
claude --version 2>&1
codex --version 2>&1
hermes --version 2>&1 | head -1
grok --version 2>&1

# Check skills
echo "=== Skills Check ==="
ls ~/.opencode/skills/ | wc -l
ls ~/.hermes/skills/ | wc -l
ls ~/.claude/skills/ | wc -l

# Check vault
echo "=== Vault Check ==="
ls ~/obsidianvault/ | wc -l
ls ~/obsidianvault/.obsidian/plugins/ | wc -l
```

---

## Common Issues

### Issue 1: Command Not Found

**Symptoms**:
- `command not found: opencode`
- `command not found: hermes`
- `command not found: claude`

**Causes**:
- Binary not in PATH
- PATH not sourced
- Installation incomplete

**Solutions**:
```bash
# Source bashrc
source ~/.bashrc

# Check if binary exists
ls -la ~/.opencode/bin/opencode
ls -la ~/.hermes/hermes-agent/.venv/bin/hermes
ls -la ~/.local/bin/claude

# Add to PATH manually
export PATH="$HOME/.opencode/bin:$PATH"
export PATH="$HOME/.hermes/hermes-agent/.venv/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# Make permanent
echo 'export PATH="$HOME/.opencode/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/.hermes/hermes-agent/.venv/bin:$PATH"' >> ~/.bashrc
```

---

### Issue 2: Permission Denied

**Symptoms**:
- `Permission denied: ...`
- `Operation not permitted`

**Causes**:
- File not executable
- Wrong ownership
- Restricted directory

**Solutions**:
```bash
# Make executable
chmod +x ~/.opencode/bin/opencode
chmod +x ~/.local/bin/claude
chmod +x ~/Applications/Obsidian.AppImage

# Fix ownership
chown -R $USER ~/.opencode
chown -R $USER ~/.hermes
chown -R $USER ~/.claude
```

---

### Issue 3: API Key Errors

**Symptoms**:
- `Invalid API key`
- `Authentication failed`
- `401 Unauthorized`

**Causes**:
- Key not configured
- Wrong key format
- Key revoked/expired

**Solutions**:
```bash
# Check if key exists
cat ~/.opencode/.env | grep API_KEY

# Verify key format
# OpenAI: sk-proj-...
# Anthropic: sk-ant-...
# Gemini: AIza...

# Reconfigure key
echo "OPENAI_API_KEY=sk-proj-..." > ~/.opencode/.env
chmod 600 ~/.opencode/.env
```

---

### Issue 4: GitHub Rate Limiting (HTTP 429)

**Symptoms**:
- `curl: (22) The requested URL returned error: 429`
- Downloads fail repeatedly

**Causes**:
- Too many API requests
- IP blocked temporarily

**Solutions**:
```bash
# Wait 1 hour
sleep 3600

# Use alternative download method
# Instead of raw GitHub, use release assets

# Install via Obsidian Community Plugin browser
# Settings → Community Plugins → Browse
```

---

### Issue 5: Git HTTPS Not Working

**Symptoms**:
- `git: 'remote-https' is not a git command`
- Cannot clone repos

**Causes**:
- git-remote-https missing
- Git installation incomplete

**Solutions**:
```bash
# Check git installation
git --version
which git

# Reinstall git (requires sudo)
sudo apt install git

# Alternative: use tarballs
curl -fsSL "https://github.com/user/repo/archive/refs/heads/main.tar.gz" -o repo.tar.gz
tar xzf repo.tar.gz
```

---

### Issue 6: Python PEP 668 Error

**Symptoms**:
- `error: externally-managed-environment`
- Cannot install packages with pip

**Causes**:
- System Python protected by PEP 668
- Python 3.11+ on Ubuntu/Debian

**Solutions**:
```bash
# Use --break-system-packages flag
pip install --break-system-packages <package>

# Or use venv
python3 -m venv myenv
source myenv/bin/activate
pip install <package>

# Or use pipx
pipx install <package>
```

---

### Issue 7: Obsidian Plugins Not Working

**Symptoms**:
- Plugins not loading
- Missing main.js errors
- Plugin commands not appearing

**Causes**:
- Incomplete installation
- Missing main.js file
- Plugin not enabled

**Solutions**:
```bash
# Check plugin directory
ls ~/obsidianvault/.obsidian/plugins/

# Verify main.js exists
ls ~/obsidianvault/.obsidian/plugins/dataview/main.js

# Reinstall via Obsidian
# Settings → Community Plugins → Browse → Search → Install

# Enable plugin
# Settings → Community Plugins → Toggle switch
```

---

### Issue 8: Hermes Agent Errors

**Symptoms**:
- `hermes: command not found`
- `No module named 'hermes'`
- Python version errors

**Causes**:
- Virtual environment not activated
- Wrong Python version
- Incomplete installation

**Solutions**:
```bash
# Check venv exists
ls ~/.hermes/hermes-agent/.venv/

# Activate venv
source ~/.hermes/hermes-agent/.venv/bin/activate

# Check Python version
python --version
# Should be 3.11.x

# Reinstall if needed
cd ~/.hermes/hermes-agent
python3.11 -m venv .venv
.venv/bin/pip install -e .
```

---

### Issue 9: Wiki Query Not Working

**Symptoms**:
- `wiki-query: command not found`
- No results returned
- Skill not found

**Causes**:
- Skill not installed
- Vault path not configured
- obsidian-wiki not installed

**Solutions**:
```bash
# Check skill exists
ls ~/.hermes/skills/wiki-query/

# Check vault config
cat ~/.obsidian-wiki/config

# Reinstall obsidian-wiki
pip install --break-system-packages obsidian-wiki
obsidian-wiki setup
```

---

### Issue 10: OpenCode Configuration Error

**Symptoms**:
- `Configuration is invalid`
- `Unrecognized key: ...`

**Causes**:
- Invalid JSON syntax
- Unsupported config keys
- Corrupted config file

**Solutions**:
```bash
# Check config
cat ~/opencode.json

# Fix JSON syntax
python3 -m json.tool ~/opencode.json

# Remove invalid keys
# Edit file and remove unsupported keys

# Reset config
rm ~/opencode.json
opencode init
```

---

## Debugging Commands

### System Info
```bash
# OS info
uname -a
lsb_release -a

# Python info
python3 --version
pip --version

# Node info
node --version
npm --version

# Disk space
df -h
```

### Network Debug
```bash
# Test connectivity
ping -c 3 google.com

# Test GitHub
curl -I https://github.com

# Test API endpoints
curl -I https://api.openai.com
curl -I https://api.anthropic.com
```

### Process Debug
```bash
# Check running processes
ps aux | grep opencode
ps aux | grep hermes
ps aux | grep claude

# Kill stuck processes
killall opencode
killall hermes
```

---

## Getting Help

### Check Logs
```bash
# OpenCode logs
ls ~/.opencode/log/

# Hermes logs
ls ~/.hermes/hermes-agent/logs/

# Obsidian logs
ls ~/obsidianvault/.obsidian/workspace.json
```

### Report Issues
1. Collect error message
2. Run diagnostic commands
3. Check [[ERROR-LOG]] for known issues
4. Search documentation
5. Ask for help with full context

---

## Prevention

1. **Always backup configs** before modifying
2. **Test installations** immediately after
3. **Document errors** as they occur
4. **Keep logs** for debugging
5. **Update regularly** to get fixes
