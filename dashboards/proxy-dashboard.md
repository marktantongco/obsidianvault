---
title: Proxy Dashboard
tags: [dashboard, proxy, monitoring, status]
relationships:
  - target: "[[concepts/Freebuff.md]]"
    type: related_to
  - target: "[[concepts/JCode.md]]"
    type: related_to
  - target: "[[concepts/MiMo Code.md]]"
    type: related_to
type: dashboard
created: 2026-07-24
updated: 2026-07-24
lifecycle: active
tier: core
---

# 🖥️ Proxy Dashboard

*Last refreshed: 2026-07-24*

## 📊 Quick Status

Run in your terminal for live status:
```bash
./[[concepts/Freebuff|freebuff]].sh status     # Shows all 6 services
./freebuff.sh smoke      # Tests all endpoints
```

## 📋 Services Overview

| # | Service | Port | Type | Framework | Management |
|---|---------|------|------|-----------|------------|
| 1 | **codebuff-proxy** | `:3211` | AI Proxy | Bun + Convex | `./freebuff.sh start codebuff-proxy` |
| 2 | **Freebuff2API** | `:8080` | API Gateway | Go | `./freebuff.sh start freebuff2api` |
| 3 | **freebuff-proxy** | `:1455` | AI Proxy | Go | `./freebuff.sh start freebuff-proxy-ff` |
| 4 | **[[concepts/JCode|jcode]]-daemon** | `:1456` | AI Agent | Go (jcode) | `./freebuff.sh start jcode-daemon` |
| 5 | **jcode-proxy** | `:8088` | API Bridge | Go | `./freebuff.sh start jcode-proxy` |
| 6 | **mimo-unified** | `:8877` | AI Proxy | Python | `./freebuff.sh start mimo-unified` |

## 🔗 Proxy Chain Architecture

```
┌────────────┐    ┌──────────────┐    ┌────────────┐    ┌─────────────┐
│  Clients   │───▶│ jcode-proxy  │───▶│jcode-daemon│───▶│ AI Providers│
│ (curl/CLI) │    │   :8088      │    │   :1456     │    │ OpenAI/etc  │
└────────────┘    └──────────────┘    └────────────┘    └─────────────┘

┌────────────┐    ┌──────────────┐    ┌────────────┐
│  Clients   │───▶│codebuff-proxy│───▶│  AI APIs   │
│ (Bun apps) │    │   :3211      │    │            │
└────────────┘    └──────────────┘    └────────────┘

┌────────────┐    ┌──────────────┐    ┌────────────┐
│  Clients   │───▶│ Freebuff2API │───▶│  AI APIs   │
│            │    │   :8080      │    │            │
└────────────┘    └──────────────┘    └────────────┘

┌────────────┐    ┌────────────────┐   ┌────────────┐
│  Clients   │───▶│ freebuff-proxy │───▶│  AI APIs   │
│            │    │   :1455        │   │            │
└────────────┘    └────────────────┘   └────────────┘

┌────────────┐    ┌────────────────┐   ┌────────────┐
│  Clients   │───▶│ mimo-unified   │───▶│  MiMo API  │
│            │    │   :8877        │   │ (Xiaomi)   │
└────────────┘    └────────────────┘   └────────────┘
```

## 🚀 Quick Management

### Start Everything
```bash
# All freebuff proxies
./freebuff.sh start all

# Or individually:
./freebuff.sh start jcode-daemon
./freebuff.sh start jcode-proxy
./freebuff.sh start mimo-unified
```

### Check Status
```bash
./freebuff.sh status
./freebuff.sh smoke
```

### Stop Everything
```bash
./freebuff.sh stop all
```

## 🌐 Environment Variables

Set these to route tools through the jcode proxy chain:

```bash
# In ~/.bashrc:
export OPENAI_BASE_URL="http://localhost:8088"
export OPENAI_API_KEY="jcode-proxy"
```

## 📈 Health Checks

### jcode-daemon
```bash
curl http://127.0.0.1:1456/health
# → {"status":"ok","version":"v0.55.0"}
```

### jcode-proxy
```bash
curl http://127.0.0.1:8088/health
# → {"status":"healthy","upstream":"http://127.0.0.1:1456"}

curl http://127.0.0.1:8088/v1/models
# → Lists available models
```

## 🔧 Aliases

### jcode aliases (from `~/.jcode_aliases`)
```bash
jc:start-daemon   jc:stop-daemon   jc:status
jc:start-proxy    jc:stop-proxy    jc:smoke
```

### jc wrapper (from `~/.local/bin/jc`)
```bash
jc daemon start   jc proxy start   jc status   jc ps
```

### freebuff aliases (from `~/.freebuff_aliases`)
```bash
fb:start-jcode-daemon   fb:start-jcode-proxy
fb:stop-jcode-daemon    fb:stop-jcode-proxy
```

## 📚 Related Pages

- [[concepts/Freebuff]] — Freebuff proxy manager
- [[concepts/JCode]] — jcode ecosystem (daemon, proxy, web)
- [[concepts/[[concepts/MiMo Code|MiMo Code]]]] — MiMo CLI tool
- [[concepts/OpenCode]] — OpenCode CLI agent
- [[concepts/Hermes Agent]] — Hermes orchestrator
- [[hot]] — Recent activity log

---

*Dashboard auto-refreshes on vault open. Run `Dataview: Refresh` (Ctrl+Shift+R) to update.*
