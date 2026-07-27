---
title: Grok
tags: [grok, xai, coding, cli]
type: concept
created: 2026-07-09
updated: 2026-07-24
lifecycle: verified
tier: supporting
source: project
---

# Grok

## Overview

Grok is xAI's AI coding assistant, available as a CLI tool. It provides code generation, explanation, and assistance through xAI's models.

## Version
v0.2.93

## Installation
```bash
curl -fsSL https://grok.x.ai/install | bash
```

## Location
- Binary: `~/.grok/bin/grok`
- Completions: `~/.grok/completions/bash/grok.bash`
- Config: `~/.grok/`

## Features
- **xAI Models**: Access to Grok's language models
- **Code Generation**: Write and explain code
- **Terminal Integration**: Bash completions included
- **Cross-Agent**: Can be used alongside other AI agents

## Usage

```bash
# Start interactive mode
grok

# Check version
grok --version

# One-shot prompt
grok -p "Explain quantum computing"
```

## Related
- [[AI Agents]] — Agent ecosystem overview
- [[OpenCode]] — OpenCode CLI agent
