---
title: Error Log
category: reference
created: 2026-07-09
updated: 2026-07-09
tags: [errors, debugging, reference]
lifecycle: active
tier: supporting
---

# Error Log

**Last Updated**: 2026-07-09 13:00 UTC

---

## Active Errors

### E001: GitHub Rate Limiting (HTTP 429)
- **Date**: 2026-07-09
- **Component**: Obsidian Plugin Installation
- **Error**: `curl: (22) The requested URL returned error: 429`
- **Cause**: Too many GitHub API requests in short time
- **Impact**: 5 of 6 Obsidian plugins not fully installed (only manifest.json)
- **Workaround**: Install via Obsidian Community Plugin browser
- **Resolution**: Wait 1 hour, then install manually through Obsidian UI
- **Status**: ⚠️ OPEN

### E002: Git HTTPS Not Working
- **Date**: 2026-07-09
- **Component**: Git
- **Error**: `git: 'remote-https' is not a git command`
- **Cause**: git-remote-https binary missing or not in PATH
- **Impact**: Cannot clone repos via HTTPS, must use curl+tarball
- **Workaround**: Download tarballs manually
- **Resolution**: `sudo apt install git` (requires sudo)
- **Status**: ⚠️ OPEN

### E003: Python PEP 668 Restriction
- **Date**: 2026-07-09
- **Component**: pip
- **Error**: `error: externally-managed-environment`
- **Cause**: System Python 3.14 protected by PEP 668
- **Impact**: Cannot install packages globally with pip
- **Workaround**: Use `--break-system-packages` flag
- **Resolution**: Use venv or pipx
- **Status**: ✅ WORKAROUND IN PLACE

---

## Resolved Errors

### E004: OpenCode Invalid Configuration
- **Date**: 2026-07-09
- **Component**: OpenCode
- **Error**: `Configuration is invalid at /home/x1/opencode.json - Unrecognized key: permissions`
- **Cause**: Invalid `permissions` key in opencode.json
- **Impact**: OpenCode would not start
- **Resolution**: Removed `permissions` key from config
- **Status**: ✅ RESOLVED

### E005: Hermes Agent Git Clone Failed
- **Date**: 2026-07-09
- **Component**: Hermes Agent
- **Error**: `fatal: remote helper 'https' aborted session`
- **Cause**: Git HTTPS not working (E002)
- **Impact**: Could not clone hermes-agent repo
- **Resolution**: Downloaded tarball manually, installed via pip in venv
- **Status**: ✅ RESOLVED

### E006: MiMo Code Download Timeout
- **Date**: 2026-07-09
- **Component**: MiMo Code
- **Error**: `bash tool terminated command after exceeding timeout`
- **Cause**: Large download file, slow connection
- **Impact**: Official installer timed out
- **Resolution**: Used npm install instead (`npm install -g @mimo-ai/cli`)
- **Status**: ✅ RESOLVED

### E007: Hermes Python Version Incompatible
- **Date**: 2026-07-09
- **Component**: Hermes Agent
- **Error**: `Package 'hermes-agent' requires a different Python: 3.14.4 not in '<3.14,>=3.11'`
- **Cause**: System Python 3.14, Hermes requires Python <3.14
- **Impact**: Cannot install Hermes with system Python
- **Resolution**: Created venv with Python 3.11
- **Status**: ✅ RESOLVED

---

## Error Patterns

### Pattern 1: Rate Limiting
- **Symptoms**: HTTP 429 errors
- **Common Causes**: Too many API requests, GitHub raw content
- **Solution**: Add delays between requests, use alternative sources

### Pattern 2: Missing Binaries
- **Symptoms**: `command not found`, `not a git command`
- **Common Causes**: Incomplete installation, PATH issues
- **Solution**: Reinstall, update PATH

### Pattern 3: Version Incompatibility
- **Symptoms**: `requires different Python`, `not supported`
- **Common Causes**: System version too new/old
- **Solution**: Use venv with compatible version

---

## Debugging Commands

```bash
# Check if binary exists
which <command>

# Check version
<command> --version

# Check PATH
echo $PATH | tr ':' '\n' | grep <pattern>

# Check file permissions
ls -la <file>

# Check Python version
python3 --version
python3.11 --version

# Check pip packages
pip list | grep <package>

# Check npm packages
npm list -g | grep <package>
```

---

## Prevention Tips

1. **Always check prerequisites** before installation
2. **Use venvs** for Python projects
3. **Add delays** between API calls
4. **Backup configs** before modifying
5. **Test installations** immediately after
6. **Document errors** as they occur
7. **Use workarounds** when blocked
