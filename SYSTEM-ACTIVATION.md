---
title: System Activation Guide
type: reference
created: 2026-07-21
updated: 2026-07-21
tags: [activation, setup, configuration, getting-started]
---

# System Activation Guide

## Overview

The vault documents a sophisticated multi-agent AI development environment, but several components need activation before the system is fully operational. This guide walks through each step in dependency order.

---

## Prerequisites

- Physical or SSH access to the Ubuntu 26.04 machine
- Terminal with `sudo` access
- API keys: OpenAI ✅, Anthropic ⏳, Gemini ⏳, MiMo ⏳
- ~10 minutes for full activation

---

## Step 1: Configure API Keys

**Why**: Most agents and services need API keys to function.

```bash
# 1. Get your API key from https://console.anthropic.com/
# 2. Add to Claude Code
echo "ANTHROPIC_API_KEY=sk-ant-..." >> ~/.claude/.env

# 3. Add to OpenCode (optional)
echo "ANTHROPIC_API_KEY=sk-ant-..." >> ~/.opencode/.env

# 4. Get Gemini API key from https://aistudio.google.com/apikey
echo "GEMINI_API_KEY=..." >> ~/.opencode/.env
echo "GEMINI_API_KEY=..." >> ~/.hermes/hermes-agent/.env

# 5. Set secure permissions
chmod 600 ~/.opencode/.env ~/.claude/.env ~/.hermes/hermes-agent/.env ~/.codex/.env

# 6. Verify
export ANTHROPIC_API_KEY=$(grep ANTHROPIC_API_KEY ~/.claude/.env | cut -d= -f2)
curl -s https://api.anthropic.com/v1/models \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" | head -5
```

**Verify**: `claude -p "Hello, world"` returns a response.

---

## Step 2: Authenticate FreeHive Gateway

**Why**: FreeHive routes requests to Claude and ChatGPT via OAuth, bypassing direct API keys.

```bash
# 1. Authenticate Claude CLI (generates OAuth tokens FreeHive uses)
claude login
# Follow browser prompt to authenticate with your Anthropic account

# 2. Verify FreeHive can see the auth
systemctl --user status freehive.service
# Look for: "Provider cli_introspection: authenticated"

# 3. Test through FreeHive
curl -s http://127.0.0.1:7200/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer freehive" \
  -d '{"model":"claude-sonnet-4-20250514","messages":[{"role":"user","content":"Hello"}]}' | head -5
```

**Verify**: HTTP 200 with a response body (not 401/503).

---

## Step 3: Start LifeOS Pulse Daemon

**Why**: The LifeOS Algorithm's `hermes_router.py` uses Pulse for context-aware task classification. Without it, the keyword fallback works but is less accurate.

```bash
# 1. Navigate to the LifeOS project directory
cd ~/ai-workspace/lifeos  # or wherever LifeOS is installed

# 2. Start the Pulse daemon
bun run pulse &
# OR if systemd service exists:
systemctl --user start lifeos-pulse.service

# 3. Verify it's running
curl -s http://localhost:31337/api/pulse/status
# Expected: {"status":"ok","version":"..."}

# 4. Enable on boot
systemctl --user enable lifeos-pulse.service
```

**Verify**: `curl http://localhost:31337/api/pulse/status` returns 200 OK.

---

## Step 4: Run Cross-Agent Workflow Tests

**Why**: Validates that all 7 agents and the LifeOS routing work end-to-end.

```bash
# Navigate to the second-brain scripts
cd ~/ai-workspace/second-brain/scripts/

# Ensure dependency chain is built correctly (order matters!)
# 1. lifeos_client.py must exist before hermes_router.py
# 2. hermes_router.py must exist before hermes (bash wrapper)
ls -la lifeos_client.py hermes_router.py hermes poznote_pipeline.py poznote_watch.sh
```

Run the test sequence:

```bash
# Test 1: Wiki Query (Knowledge Retrieval)
wiki-query @personal What agents are installed?
# Expected: Returns compiled knowledge from vault pages
# Pages: [[concepts/AI Agents]], [[concepts/OpenCode]], [[concepts/Hermes Agent]]

# Test 2: Wiki Capture (Save Finding)
wiki-capture --quick "Workflow test completed successfully"
# Expected: Saves to _raw/poznote/ staging area
# Verify: ls ~/obsidianvault/_raw/poznote/

# Test 3: OpenCode Execution
opencode -p "Write a Python hello world script"
# Expected: Generates and explains code

# Test 4: Claude Code Review
claude "Review this code for best practices"
# Expected: Provides code review feedback with security recommendations

# Test 5: Hermes Orchestration
hermes "Break down the task: Build a todo app with React"
# Expected: Creates task breakdown with subtasks

# Test 6: Full Workflow (Cross-Agent Handoff)
hermes "Plan: Create a Python script that fetches weather data"           # Hermes plans
opencode -p "Implement the weather script planned by Hermes"              # OpenCode implements
claude "Review ~/ai-workspace/weather.py for security issues"             # Claude reviews
wiki-capture --quick "Weather script created and reviewed"                # Wiki documents
```

**Expected outcome**: All 6 tests pass. Results are logged to `log.md` and captured to wiki.

---

## Step 5: Configure Mobile Sync

**Why**: Enables capture from phone/tablet during the day.

```bash
# On Android with Termux:
pkg install git termux-services
termux-setup-storage

# Clone vault
cd ~/storage/shared
git clone https://github.com/marktantongco/obsidianvault.git
cd obsidianvault
git config user.name "Hermes"
git config user.email "hermes@secondbrain.local"

# Create sync script
mkdir -p ~/bin
cp ~/ai-workspace/second-brain/scripts/poznote_watch.sh ~/bin/vault-sync.sh
chmod +x ~/bin/vault-sync.sh

# Set up cron (runs every 10 minutes)
sv-enable crond
crontab -e
# Add: */10 * * * * ~/bin/vault-sync.sh
```

---

## Post-Activation Checklist

- [ ] **Anthropic API key** configured (`~/.claude/.env`)
- [ ] **Gemini API key** configured (`~/.opencode/.env`)
- [ ] **FreeHive** authenticated (`claude login`)
- [ ] **LifeOS Pulse** running (`http://localhost:31337`)
- [ ] **Test 1** Wiki Query — PASSED
- [ ] **Test 2** Wiki Capture — PASSED
- [ ] **Test 3** OpenCode Execution — PASSED
- [ ] **Test 4** Claude Code Review — PASSED
- [ ] **Test 5** Hermes Orchestration — PASSED
- [ ] **Test 6** Cross-Agent Handoff — PASSED
- [ ] **Mobile sync** configured (Termux cron)

---

## Troubleshooting

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| FreeHive returns 401 | No OAuth token | Run `claude login` |
| FreeHive returns 503 | Provider not reachable | Check network, try direct API call |
| Pulse daemon won't start | Port 31337 in use | `lsof -i :31337` → kill process |
| `hermes_router.py` import error | Build order wrong | `lifeos_client.py` must exist first |
| `opencode -p` hangs | No model configured | Check FreeHive provider in `opencode.json` |
| `wiki-query` returns nothing | Vault not compiled | Run `obsidian-wiki setup --vault ~/obsidianvault` |

## Related

- [[API-KEY-GUIDE]] — Detailed API key setup
- [[projects/Cross-Agent-Workflow-Test]] — Test plan with expected results
- [[concepts/FreeHive]] — AI gateway configuration
- [[concepts/LifeOS Algorithm]] — Task routing system
- [[skills/mobile-sync-termux]] — Mobile sync setup
