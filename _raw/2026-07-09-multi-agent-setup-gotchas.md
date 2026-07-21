---
title: "Multi-Agent AI Setup: Gotchas and Workarounds"
type: raw
tags: [setup, agents, troubleshooting, gotchas]
project: ai-second-brain
created: 2026-07-09
summary: "Key issues encountered during multi-agent AI setup: GitHub rate limiting, Python PEP 668, git-remote-https missing, and plugin installation failures."
provenance:
  extracted: 0.8
  inferred: 0.2
base_confidence: 0.75
lifecycle: draft
tier: supporting
---

# Multi-Agent AI Setup: Gotchas and Workarounds

## Finding 1: GitHub API Rate Limiting (HTTP 429)

**Problem**: Bulk downloading Obsidian plugin files from GitHub raw content triggers rate limiting (HTTP 429).

**Root Cause**: GitHub limits raw content requests per IP. Downloading multiple plugin main.js files in quick succession hits the limit.

**Workaround**: 
- Wait 1 hour before retrying
- Use Obsidian's Community Plugin browser for installation
- Create a script with delays between downloads
- Alternative: Download release ZIP files instead of individual files

**Impact**: Prevented automatic installation of 5 of 6 Obsidian plugins.

---

## Finding 2: Python PEP 668 Restriction

**Problem**: `pip install` fails with "externally-managed-environment" error on Python 3.14+.

**Root Cause**: PEP 668 protects system Python from user-installed packages breaking system tools.

**Workaround**:
```bash
pip install --break-system-packages <package>
```
Or use venv:
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install <package>
```

**Impact**: Required `--break-system-packages` flag for pip installs.

---

## Finding 3: git-remote-https Missing

**Problem**: `git clone` fails with "git: 'remote-https' is not a git command".

**Root Cause**: git-remote-https binary missing or not in PATH. Common on minimal Git installations.

**Workaround**:
- Download tarballs via curl instead of git clone
```bash
curl -fsSL "https://github.com/user/repo/archive/refs/heads/main.tar.gz" -o repo.tar.gz
tar xzf repo.tar.gz
```

**Impact**: All git clones had to use tarball workaround.

---

## Finding 4: Obsidian Plugin Installation Failure

**Problem**: Plugins need both manifest.json AND main.js to function. GitHub rate limiting prevented downloading main.js files.

**Root Cause**: Plugins are distributed as release assets, not individual files on main branch.

**Workaround**:
- Install via Obsidian Community Plugin browser (GUI)
- Wait for rate limit to reset
- Use release ZIP downloads when available

**Impact**: Manual installation through Obsidian GUI required.

---

## Finding 5: Hermes Agent Python Version Incompatibility

**Problem**: `pip install hermes-agent` fails with "requires Python <3.14,>=3.11".

**Root Cause**: System Python is 3.14, but Hermes requires Python 3.11-3.13.

**Workaround**:
```bash
cd ~/.hermes/hermes-agent
python3.11 -m venv .venv
.venv/bin/pip install -e .
```

**Impact**: Must use Python 3.11 venv for Hermes.

---

## Finding 6: OpenCode Configuration Validation

**Problem**: OpenCode fails with "Unrecognized key: permissions".

**Root Cause**: Config file contains unsupported keys.

**Workaround**: Remove invalid keys from `~/opencode.json`.

**Impact**: Configuration must match OpenCode's expected schema.

---

## Pattern: Rate Limiting Recovery

When hitting HTTP 429 from GitHub:
1. Stop all download attempts
2. Wait minimum 1 hour
3. Use alternative download methods (release assets vs raw files)
4. Add delays (5-10 seconds) between requests
5. Consider using Obsidian's built-in plugin browser

---

## Pattern: Python Environment Isolation

When system Python is too new for a package:
1. Check package requirements: `pip show <package> | grep Requires-Python`
2. Use `--break-system-packages` for quick fix
3. Use venv for proper isolation
4. Consider using uv for faster, isolated installs
