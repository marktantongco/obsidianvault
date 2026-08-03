---
title: OWL-AGENT and Obsidian Skills Integration
category: infrastructure
tags: [owl-agent, obsidian-skills, integration, worktree, wiki, setup]
relationships:
  - target: "[[entities/Owl-Agent.md]]"
    type: related_to
  - target: "[[concepts/OpenCode.md]]"
    type: related_to
summary: Full session log — OWL-AGENT v4.2 deployment, obsidian-skills install, worktree + wiki alignment
lifecycle: evergreen
tier: 1
---

# [[entities/Owl-Agent|OWL-AGENT]] & Obsidian Skills Integration – Session Log

## Status: Complete

All major deliverables for this session are done and verified.

### What was built

| Component | Status | Location |
|-----------|--------|----------|
| OWL-AGENT v4.2 core | ✅ | `~/.owl-agent/proxy_defense.py` |
| Prometheus metrics | ✅ | `http://localhost:8000/metrics` |
| CLI (fetch / stats / bench) | ✅ | `~/.owl-agent/run.sh` |
| Podman deployment | ✅ | `~/.owl-agent/podman-compose.yml` |
| kiro-cli agent `owl-scraper` | ✅ | `~/.kiro/agents/owl-scraper.json` |
| Obsidian skills (5) | ✅ | `~/.[[concepts/OpenCode|opencode]]/skills/obsidian-skills/` |
| Vault wiki + worktree | ✅ | `~/obsidianvault/` + `~/obsidianvault-worktree/` |

---

## 1. OWL-AGENT v4.2

Self-optimising proxy HTTP client with:
- curl_cffi Chrome TLS fingerprinting
- Adaptive per-domain rate limiting (429 → slow, 200 → speed up)
- QualityScorer with exponential decay
- Circuit breaker per domain
- LRU cache + request deduplication
- Prometheus /metrics at port 8000

### Quick commands

```bash
# Fetch a URL through the proxy pool
~/.owl-agent/run.sh fetch https://example.com

# Show pool statistics
~/.owl-agent/run.sh stats

# Benchmark (10 concurrent, 100 requests)
~/.owl-agent/run.sh bench --url https://example.com --requests 100
```

---

## 2. obsidian-skills (OpenCode)

Installed 5 Agent Skills from `kepano/obsidian-skills`:

| Skill | Intent |
|-------|--------|
| `obsidian-markdown` | Create/edit Obsidian Flavoured Markdown |
| `obsidian-cli` | Interact with running Obsidian via CLI |
| `obsidian-bases` | Create `.base` database views |
| `json-canvas` | Create `.canvas` visual canvases |
| `defuddle` | Extract clean markdown from web pages |

Path: `~/.opencode/skills/obsidian-skills/`

OpenCode auto-discovers all `SKILL.md` files under that tree — no config file changes needed.

---

## 3. Obsidian Vault wiki

The vault lives at `~/obsidianvault/` and is pushed to:

```
origin  https://github.com/marktantongco/obsidianvault.git (fetch/push)
```

The `.wiki/` directory inside the vault holds:
- `config/` – machine/DE configuration notes
- `setup/` – environment setup guides
- `tools/` – tool comparisons and usage

### Vault structure

```
~/obsidianvault/
├── 01_WORK/
├── 02_KNOWLEDGE/
│   └── OWL-AGENT-v4.2.md
├── 03_LEARNING/
├── 04_RELATIONSHIP/
├── 05_OBSERVABILITY/
├── 06_STATE/
├── _raw/
├── _skills/
├── .wiki/
│   ├── config/
│   ├── setup/
│   └── tools/
└── ...
```

---

## 4. Git worktree setup

A separate worktree `~/obsidianvault-worktree/` was created so the vault can be opened
in isolation (e.g. by a different tool or an additional Obsidian window)
without interfering with the main working copy.

```bash
# Current worktrees
git -C ~/obsidianvault worktree list
```

---

## 5. Memory diagnostics

| Resource | Value |
|----------|-------|
| Total RAM | 7.1 GiB |
| Used | 5.2 GiB (73 %) |
| Swap used | 2.3 GiB / 4 GiB |
| Top consumer | opencode (823 MiB) |

### Running services

- kiro-gateway, kirolink, fluent-bit, gost
- grafana-server, loki, prometheus, warp-plus

OWL-AGENT itself consumes very little when idle; the proxy pool is loaded lazily.

---

## Files created / modified

| File | Action |
|------|--------|
| `proxy_defense.py` | Prometheus metrics + CLI subcommands |
| `run.sh` | Already existed, now points to latest `proxy_defense.py` |
| `Dockerfile` / `podman-compose.yml` | Podman-first deployment |
| `observe-skill.js` | Obsidian scraping skill |
| `~/.kiro/agents/owq-scraper.json` | kiro-cli agent config |
| `~/.kiro/skills/owq-scraper/` | kiro-cli skill + installer |
| `OWL-AGENT-v4.2.md` (in vault) | Long-form knowledge page |
| `obsidianvault-worktree/` | Isolated git worktree |

---

## Next possible steps

1. **Enable Redis** – install redis-server and set `OWL_USE_REDIS=true` for persistent state
2. **Stop unused services** – `grafana-server`, `loki`, `fluent-bit` consume ~330 MiB combined
3. **Power down Vivaldi tabs** – 16 renderer processes consume ~2 GiB
4. **Prometheus alert rules** – add alerts for proxy pool depletion
5. **Push vault** – `git -C ~/obsidianvault push` to back up to GitHub
