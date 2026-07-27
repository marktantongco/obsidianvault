---
title: "Tool Guide — All Installed Tools & Services"
created: 2026-07-27
tags:
  - reference
  - guide
  - tools
  - infrastructure
aliases:
  - Tool Guide
  - Installed Tools
  - Services Overview
cssclasses:
  - wide-page
---

# 🛠️ Tool Guide — All Installed Tools & Services

A comprehensive reference for every tool, service, and agent installed and configured on this system, with paths, purposes, ports, and quick commands.

---

## 1. 🦉 OWL-AGENT v4.2

Self-optimising proxy HTTP client with intelligent proxy pool, quality scoring, adaptive rate limiting, circuit breakers, and Chrome fingerprinting.

| Property | Value |
|----------|-------|
| **Path** | `~/.owl-agent/` |
| **Venue** | `~/.owl-agent/venv` |
| **Purpose** | Intelligent web scraping through rotating proxies |
| **Status** | ✅ Installed & running |

### Services

| Service | Port | Status | Type |
|---------|------|--------|------|
| API Server | `:60000` | 🔵 systemd | `owl-agent.service` |
| Metrics | `:9091` | 🔵 Prometheus | via API server |

### Key Files

| File | Purpose |
|------|---------|
| `proxy_defense.py` | Core engine — proxy pool, quality scoring, rate limiting, circuit breaker |
| `owl_server.py` | HTTP API server with `/fetch`, `/health`, `/stats`, `/metrics` |
| `run.sh` | Unified CLI runner |
| `Containerfile` | Podman-native container image |
| `podman-compose.yml` | Multi-service deployment with Redis |
| `owl-agent.skill.json` | OpenCode skill definition |
| `obsidian-skill.js` | Obsidian scraper skill |
| `warp-agent.yaml` | Warp terminal agent config |
| `owl-agent.service` | Systemd unit file |
| `install_owl_agent.sh` | All-in-one installer |

### Quick Commands

```bash
~/.owl-agent/run.sh health                           # Health check
~/.owl-agent/run.sh fetch https://example.com         # Fetch a URL
curl -s :60000/health | python3 -m json.tool          # API health
curl -s :9091/metrics | grep owl_                     # Prometheus metrics

# Fetch via API
curl -X POST :60000/fetch -H 'Content-Type: application/json' \
  -d '{"url":"https://api.github.com/users/octocat"}'
```

> [!tip] Podman Deploy
> ```bash
> cd ~/.owl-agent && podman build -t owl-agent:4.2 -f Containerfile .
> podman-compose -f podman-compose.yml up -d
> ```

---

## 2. 🔗 free-buff-lol Proxy

Lightweight proxy relay running on port 1455.

| Property | Value |
|----------|-------|
| **Path** | `~/ai-workspace/free-buff-lol/` |
| **Port** | `:1455` |
| **Purpose** | Proxy relay with 10 models, 1 valid token, country=PH |
| **Status** | ✅ Running (PID 11762, Node.js) |
| **Source** | `github.com/notBlubbll/free-buff-lol.git` |

### Quick Commands

```bash
# Check if running
lsof -i :1455

# Restart
cd ~/ai-workspace/free-buff-lol && node proxy.js
```

---

## 3. 🧠 Hermes Agent v0.19.0

Self-improving AI agent from Nous Research — creates skills from experience and runs anywhere.

| Property | Value |
|----------|-------|
| **Path** | `~/.hermes/hermes-agent/` |
| **Venue** | `~/.hermes/hermes-agent/venv` |
| **Python** | 3.11.15 |
| **Purpose** | Autonomous AI agent with tool-calling, skill creation, memory |
| **Status** | ✅ Installed (editable `-e .[acp]`) |
| **Source** | Nous Research (cloned to `~/.hermes/hermes-agent`) |

### CLI Entry Points

| Command | Module | Purpose |
|---------|--------|---------|
| `hermes` | `hermes_cli.main:main` | Interactive chat agent |
| `hermes-agent` | `run_agent:main` | Direct agent runner |
| `hermes-acp` | `acp_adapter.entry:main` | ACP adapter |

### Quick Commands

```bash
~/.hermes/hermes-agent/venv/bin/hermes --help
~/.hermes/hermes-agent/venv/bin/hermes chat
```

---

## 4. 🎵 Mistral Vibe v2.22.0

Minimal CLI coding agent by Mistral AI.

| Property | Value |
|----------|-------|
| **Path** | `/tmp/mistral-vibe/` |
| **Venue** | `/tmp/mistral-vibe/.venv` |
| **Python** | 3.12.13 (isolated) |
| **Purpose** | CLI coding assistant with tool-calling |
| **Status** | ✅ Installed |
| **Source** | `github.com/mistralai/mistral-vibe` |
| **Stars** | 4,700+ |

### CLI

```bash
vibe --help                           # Full help
vibe "explain this codebase"          # Interactive prompt
vibe --setup                          # Initial configuration
vibe -p "list all files" --output text  # Programmatic mode
```

---

## 5. 🆓 glm-free-claude-code

Use the free GLM 5.2 API with Claude Code — three small, dependency-free tools.

| Property | Value |
|----------|-------|
| **Path** | `/tmp/glm-free-claude-code/` |
| **Purpose** | Free GLM 5.2 API for offloading cheap work from paid Claude sessions |
| **Status** | ✅ Installed (needs ZenMux API key) |
| **Source** | `github.com/Matswm86/glm-free-claude-code` |

### Tools

| Tool | Path | Purpose |
|------|------|---------|
| `glm` | `~/.local/bin/glm` | One-shot free GLM 5.2 query |
| `glm-agent` | `~/.local/bin/glm-agent` | Headless GLM Claude Code agent |
| `cc-glm` | Shell function in `~/.bashrc` | Full GLM 5.2 Claude Code session |

### Setup (requires free key)

```bash
# 1. Go to https://zenmux.ai → Models → GLM 5.2 Free → Create API Key
# 2. Store the key:
mkdir -p ~/.config/zenmux && umask 177 && printf '%s' 'YOUR_KEY_HERE' > ~/.config/zenmux/key

# 3. Test:
glm "Hello, what model are you?"
```

### Usage

```bash
glm "write a pytest for this function"           # Prompt as arg
cat big.log | glm "summarise the errors"          # Pipe stdin
glm -s "code only, no prose" "debounce in TS"     # System prompt
glm -m 8000 "long refactor plan"                  # Bigger budget

# Full GLM 5.2 session (after `source ~/.bashrc`):
cc-glm
```

---

## 6. 👾 Peri AI Agent v2.8.6

AI agent from the Peri project.

| Property | Value |
|----------|-------|
| **Path** | `~/.peri/agent-v2.8.6/peri` |
| **Symlink** | `~/.local/bin/peri` |
| **Purpose** | AI agent with ACP mode, plugins, web PTY terminal |
| **Status** | ✅ Installed |
| **Source** | `github.com/konghayao/peri` |

### CLI

```bash
peri --help
peri "your instruction here"
```

---

## 7. 📦 Package Managers & Runtimes

| Tool | Path/Version | Purpose |
|------|-------------|---------|
| **Python** | `/usr/bin/python3` (3.14.4) | System Python |
| **uv** | `~/.local/bin/uv` | Fast Python package manager |
| **Node.js** | system | JavaScript runtime |
| **npm** | system | Node package manager |
| **Podman** | system | Container runtime (Docker alternative) |
| **systemd** | system | Service manager |

---

## 8. 🔌 Port Map

| Port | Service | Purpose |
|------|---------|---------|
| `:60000` | OWL-AGENT API | HTTP API for proxy-backed fetching |
| `:9090` | Prometheus | System Prometheus instance |
| `:9091` | OWL-AGENT Metrics | OWL-AGENT Prometheus metrics |
| `:1455` | free-buff-lol | Proxy relay (Node.js) |
| `:8081` | freebuff-gateway | Gateway (currently broken upstream) |

---

## 9. 🗺️ Directory Map

```
~/
├── .owl-agent/           # OWL-AGENT v4.2 — proxy engine, server, deploy configs
├── .hermes/hermes-agent/ # Hermes Agent v0.19.0
├── .peri/                # Peri AI Agent v2.8.6
├── .local/bin/           # User binaries (peri, glm, glm-agent, vibe)
├── ai-workspace/
│   └── free-buff-lol/    # Proxy relay on :1455
├── obsidianvault/        # This Obsidian vault
├── .opencode/skills/     # OpenCode skills
└── /tmp/
    ├── mistral-vibe/     # Mistral Vibe v2.22.0
    └── glm-free-claude-code/  # GLM 5.2 free tools
```

---

## 10. 🔧 Quick Troubleshooting

```bash
# Check what's running on a port
lsof -i :PORT

# Restart OWL-AGENT service
sudo systemctl restart owl-agent

# View OWL-AGENT logs
sudo journalctl -u owl-agent -n 50 --no-pager

# Verify PATH includes user binaries
echo $PATH | tr ':' '\n' | grep ".local/bin"

# Source new shell functions
source ~/.bashrc
```

---

> [!info] Created: 2026-07-27 | Last updated: 2026-07-27
> See also: [[index]], [[hot]], [[AGENTS]]
