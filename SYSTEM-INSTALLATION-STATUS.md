---
title: System Installation Status
category: reference
created: 2026-07-09
updated: 2026-07-09
tags: [installation, status, reference]
lifecycle: active
tier: core
---

# System Installation Status

**Last Updated**: 2026-07-09 13:00 UTC

---

## Summary

| Category | Installed | Pending | Failed |
|----------|-----------|---------|--------|
| CLI Tools | 6 | 0 | 0 |
| Desktop Apps | 2 | 0 | 0 |
| Wiki System | 3 | 0 | 0 |
| Agent Bridges | 2 | 0 | 0 |
| Obsidian Plugins | 0 | 6 | 0 (manual install) |
| API Keys | 4 | 0 | 0 |
| **Total** | **20** | **2** | **0** |

---

## 1. CLI Tools — ALL INSTALLED

### 1.1 OpenCode
- **Version**: 1.17.16
- **Location**: `~/.opencode/bin/opencode`
- **Config**: `~/opencode.json`
- **Skills**: 37 installed
- **Status**: ✅ INSTALLED

### 1.2 MiMo Code (Xiaomi)
- **Version**: 0.1.5
- **Location**: `~/.local/bin/mimo`
- **Config**: `~/.config/mimo/`
- **Status**: ✅ INSTALLED

### 1.3 Claude Code (Anthropic)
- **Version**: 2.1.205
- **Location**: `~/.local/bin/claude`
- **Config**: `~/.claude/`
- **Skills**: 37 installed
- **Status**: ✅ INSTALLED

### 1.4 OpenAI Codex
- **Version**: 0.143.0
- **Location**: `~/.local/bin/codex`
- **Config**: `~/.codex/`
- **Status**: ✅ INSTALLED

### 1.5 Hermes Agent (Nous Research)
- **Version**: 0.18.2 (2026.7.7.2)
- **Location**: `~/.hermes/hermes-agent/`
- **Binary**: `~/.hermes/hermes-agent/.venv/bin/hermes`
- **Skills**: 36 installed
- **Plugins**: 2 installed
- **Status**: ✅ INSTALLED

### 1.6 Grok (xAI)
- **Version**: 0.2.93
- **Location**: `~/.grok/bin/grok`
- **Completions**: `~/.grok/completions/bash/grok.bash`
- **Status**: ✅ INSTALLED

---

## 2. Desktop Apps — ALL INSTALLED

### 2.1 Obsidian
- **Type**: AppImage
- **Location**: `~/Applications/Obsidian.AppImage`
- **Vault**: `~/obsidianvault/`
- **Status**: ✅ INSTALLED

### 2.2 Simplenote
- **Type**: Extracted .deb
- **Location**: `~/Applications/Simplenote/`
- **Binary**: `~/Applications/Simplenote/opt/Simplenote/simplenote`
- **Status**: ✅ INSTALLED

---

## 3. Wiki System — ALL INSTALLED

### 3.1 obsidian-wiki
- **Version**: 2026.7.2
- **Config**: `~/.obsidian-wiki/config`
- **Skills Installed**: 36 to all agents
- **Status**: ✅ INSTALLED

### 3.2 Primary Vault
- **Location**: `~/obsidianvault/`
- **Pages**: 19 markdown files
- **Structure**:
  - `concepts/` — 10 pages
  - `entities/` — 0 pages
  - `projects/` — 1 page
  - `references/` — 0 pages
  - `synthesis/` — 0 pages
  - `journal/` — 0 pages
  - `templates/` — 3 templates
- **Status**: ✅ CREATED

### 3.3 llm-wiki Engine
- **Location**: `~/obsidian-vaults/AI-Second-Brain/.wiki/`
- **Config**: `config.yaml` (839 lines)
- **Status**: ✅ CONFIGURED

---

## 4. Agent Bridges — ALL INSTALLED

### 4.1 Hermes-OpenCode Bridge
- **Location**: `~/.hermes/plugins/opencode/`
- **Files**: plugin.yaml, opencode_tool.py, SKILL.md
- **Status**: ✅ INSTALLED

### 4.2 Hermes-Claude Bridge
- **Location**: `~/.hermes/plugins/code-bridge/`
- **Files**: plugin.yaml, config.yml, skills/
- **Status**: ✅ INSTALLED

---

## 5. Unified Memory — INSTALLED

### 5.1 agentic-stack
- **Location**: `~/ai-workspace/.agent/`
- **Contents**: memory.md, skills/, prompts/, memory/
- **Symlinks**:
  - `~/.opencode/agentic` → `~/ai-workspace/.agent/`
  - `~/.hermes/agentic` → `~/ai-workspace/.agent/`
  - `~/.claude/agentic` → `~/ai-workspace/.agent/`
- **Status**: ✅ INSTALLED

---

## 6. Skills — ALL INSTALLED

### 6.1 OpenCode Skills
- **Location**: `~/.opencode/skills/`
- **Count**: 37 skills
- **Source**: Symlinked from `~/.agents/skills/`
- **Status**: ✅ INSTALLED

### 6.2 Hermes Skills
- **Location**: `~/.hermes/skills/`
- **Count**: 36 skills
- **Source**: obsidian-wiki setup
- **Status**: ✅ INSTALLED

### 6.3 Claude Skills
- **Location**: `~/.claude/skills/`
- **Count**: 37 skills
- **Source**: obsidian-wiki setup
- **Status**: ✅ INSTALLED

### 6.4 Skills List (37)
- wiki-query, wiki-capture, wiki-ingest, wiki-lint, wiki-update
- wiki-rebuild, wiki-status, wiki-digest, wiki-export, wiki-import
- wiki-dedup, wiki-synthesize, wiki-stage-commit, wiki-switch
- wiki-context-pack, wiki-dashboard, wiki-research
- agent-reach, arxiv, deep-research, design-blueprint
- docx-official, pptx-official, pdf-official, xlsx-official
- html-to-video-pipeline, modern-python-toolchain
- research-paper-writing, skill-creator, super-research
- vault-skill-factory, wiki-agent, wiki-capture
- And more...

---

## 7. Obsidian Plugins — MANUAL INSTALLATION REQUIRED

### 7.1 Plugin Status
| Plugin | Status | Notes |
|--------|--------|-------|
| Dataview | ⏳ PENDING | Manual install required |
| Calendar | ⏳ PENDING | Manual install required |
| Templater | ⚠️ PARTIAL | manifest.json only |
| Kanban | ⏳ PENDING | Manual install required |
| Tasks | ⏳ PENDING | Manual install required |
| Excalidraw | ⏳ PENDING | Manual install required |

### 7.2 Plugin Installation Issue
- **Problem**: GitHub API rate limiting (HTTP 429)
- **Cause**: Too many download attempts in short time
- **Solution**: Install via Obsidian Community Plugin browser (GUI)

### 7.3 Manual Installation Required
Open Obsidian → Settings → Community Plugins → Browse → Search & Install:
1. "Dataview" by Michael Brenan
2. "Calendar" by Liam Cain
3. "Templater" by SilentVoid13
4. "Kanban" by Matt Peerce
5. "Tasks" by Martin Schenck
6. "Excalidraw" by Zsolt Viczian

### 7.4 Documentation Created
- `MANUAL-PLUGIN-INSTALL.md` — Step-by-step manual installation guide
- `install-plugins.sh` — Script for future automated installation

---

## 8. API Keys — ALL CONFIGURED ✅

### 8.1 OpenAI
- **Status**: ✅ CONFIGURED
- **Location**: `~/.opencode/.env`, `~/.claude/.env`, `~/.hermes/hermes-agent/.env`, `~/.codex/.env`
- **Key**: sk-proj-ly4CzV... (configured)

### 8.2 Google Gemini
- **Status**: ✅ CONFIGURED
- **Location**: `~/.opencode/.env`, `~/.claude/.env`, `~/.hermes/hermes-agent/.env`
- **Key**: AIzaSyAM7NpHw... (configured)
- **Usage**: Free tier available

### 8.3 Xiaomi MiMo
- **Status**: ✅ CONFIGURED
- **Location**: `~/.opencode/.env`, `~/.claude/.env`, `~/.hermes/hermes-agent/.env`
- **Key**: sk-s4fs3mft... (configured)
- **Usage**: MiMo Code

### 8.4 Hermes (Nous Research)
- **Status**: ✅ CONFIGURED
- **Location**: `~/.opencode/.env`, `~/.claude/.env`, `~/.hermes/hermes-agent/.env`
- **Key**: sk-nous-7tUUbd... (configured)
- **Usage**: Hermes Agent

---

## 9. PATH Configuration

### 9.1 Entries in ~/.bashrc
```bash
export PATH="$HOME/.opencode/bin:$PATH"
export PATH="$HOME/.hermes/hermes-agent/.venv/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.grok/bin:$PATH"
```

### 9.2 Verification
```bash
source ~/.bashrc
which opencode  # → /home/x1/.opencode/bin/opencode
which hermes    # → /home/x1/.hermes/hermes-agent/.venv/bin/hermes
which grok      # → /home/x1/.grok/bin/grok
```

---

## 10. Directory Structure

```
~/
├── .opencode/
│   ├── bin/opencode
│   ├── skills/ (37 skills)
│   ├── agentic → ~/ai-workspace/.agent/
│   └── .env (OpenAI + Gemini + MiMo + Hermes keys)
├── .hermes/
│   ├── hermes-agent/
│   │   ├── .venv/
│   │   └── .env (OpenAI + Gemini + MiMo + Hermes keys)
│   ├── plugins/
│   │   ├── opencode/
│   │   └── code-bridge/
│   ├── skills/ (36 skills)
│   └── agentic → ~/ai-workspace/.agent/
├── .claude/
│   ├── skills/ (37 skills)
│   ├── agentic → ~/ai-workspace/.agent/
│   └── .env (OpenAI + Gemini + MiMo + Hermes keys)
├── .codex/
│   └── .env (OpenAI key)
├── .local/bin/
│   ├── mimo
│   ├── claude
│   └── codex
├── .grok/bin/
│   └── grok
├── Applications/
│   ├── Obsidian.AppImage
│   └── Simplenote/
├── obsidianvault/
│   ├── .obsidian/
│   ├── concepts/ (10 pages)
│   ├── projects/ (1 page)
│   ├── templates/ (3 templates)
│   ├── index.md
│   ├── hot.md
│   └── log.md
├── ai-workspace/
│   ├── .agent/
│   │   ├── memory.md
│   │   ├── skills/
│   │   └── prompts/
│   └── llm-wiki/
├── obsidian-vaults/
│   └── AI-Second-Brain/
│       └── .wiki/ (llm-wiki engine)
├── opencode.json
└── .bashrc (PATH entries)
```

---

## 11. Known Issues

### 11.1 Git HTTPS Not Working
- **Issue**: `git: 'remote-https' is not a git command`
- **Impact**: Cannot clone repos via HTTPS
- **Workaround**: Use curl + tarball for downloads
- **Fix**: `sudo apt install git` (requires sudo)

### 11.2 GitHub Rate Limiting
- **Issue**: HTTP 429 errors when downloading plugin files
- **Impact**: Some Obsidian plugins not fully installed
- **Workaround**: Install via Obsidian Community Plugin browser
- **Fix**: Wait 1 hour, then retry

### 11.3 Python PEP 668
- **Issue**: `error: externally-managed-environment`
- **Impact**: Cannot use pip directly
- **Workaround**: Use `--break-system-packages` flag
- **Fix**: Use venv or pipx

---

## 12. Next Steps

### Immediate
- [ ] Install Obsidian plugins via Community Plugin browser
- [ ] Configure plugin settings
- [ ] Get Anthropic API key
- [ ] Get Google Gemini API key

### Short-term
- [ ] Test cross-agent workflows
- [ ] Build first project
- [ ] Set up daily wiki updates
- [ ] Configure Hermes plugins

### Long-term
- [ ] Add more wiki pages
- [ ] Create synthesis pages
- [ ] Set up automated backups
- [ ] Configure multi-vault setup

## Related

- [[SYSTEM-COMPLETE]] — Executive summary of the system installation
- [[TROUBLESHOOTING]] — Common issues and debugging commands
- [[API-KEY-GUIDE]] — API key configuration for all providers
- [[ERROR-LOG]] — Known errors and their resolution status

---

## 13. Verification Commands

```bash
# Check all installations
echo "=== Verification ==="
echo "OpenCode: $(opencode --version 2>/dev/null | head -1)"
echo "Hermes: $(hermes --version 2>/dev/null | head -1)"
echo "Claude: $(claude --version 2>/dev/null)"
echo "Codex: $(codex --version 2>/dev/null)"
echo "Grok: $(grok --version 2>/dev/null)"
echo "MiMo: $(mimo --version 2>/dev/null)"
echo "obsidian-wiki: $(obsidian-wiki --version 2>/dev/null | head -1)"

# Check skills
echo "=== Skills ==="
echo "OpenCode: $(ls ~/.opencode/skills/ | wc -l)"
echo "Hermes: $(ls ~/.hermes/skills/ | wc -l)"
echo "Claude: $(ls ~/.claude/skills/ | wc -l)"

# Check vault
echo "=== Vault ==="
echo "Pages: $(find ~/obsidianvault -name '*.md' | wc -l)"
echo "Plugins: $(ls ~/obsidianvault/.obsidian/plugins/ | wc -l)"
```
