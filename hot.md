---
title: Hot Cache
updated: 2026-07-24T20:55:00.000Z

---

# Hot Cache

## Recent Activity
* [[journal/2026-07-25-mimo-proxy-uninstall|MiMo Proxy Troubleshooting & Cleanup Session]] — risk control bypass, SOCKS5, uninstall
* Fixed MiMo "risk control" HTTP 400/441 errors with intercept proxy (IP rotation + fingerprint rotation + exponential backoff)
* Resolved 8 upstream API IPs for rotation: `8.222.147.102`, `47.84.2.69`, `47.84.235.191`, `47.236.158.11`, `47.236.158.71`, `47.237.8.234`, `47.245.105.117`, `8.222.143.90`
* Added SOCKS5 proxy support to `mimo-intercept-proxy.py` (PySocks) and `mimo-unified-proxy.py` (httpx native)
* Added **SOCKS5 auto-discovery** — when all proxies fail, fetches from SpeedX/ShiftyTR/proxyscrape, tests 200 candidates against Xiaomi bootstrap with 30 workers, returns up to 3 working proxies
* Created cleanup script `cleanup-mimo-opencode.sh` — removes mimocode, opencode, jcode completely
* Created `uninstall-mimo-proxy.sh` for MiMo-only cleanup
* Setup trusted SSL certificate via local CA
* Documented architecture: `mimo CLI → iptables → intercept proxy (:8443) → unified proxy (:8877) → SOCKS5 → Xiaomi API`
* Crated [[concepts/MiMo Proxy Fix|MiMo Proxy Fix]] concept page

## Key Takeaways
- Xiaomi risk control is IP+ASN based — rotating between 8 Alibaba Cloud IPs alone is NOT enough
- SOCKS5 proxy from different ASN is required to fully bypass blocks
- Combined strategy: SOCKS5 egress + IP rotation + fingerprint rotation + exponential backoff
- Auto-discovery fetches fresh SOCKS5 proxies from 3 public lists on attempt 3/5

## Active Integrations
| Tool | Status |
|------|--------|
| [[concepts/Freebuff\|Freebuff]] | ✅ Configured (4 proxies) |
| [[concepts/JCode\|JCode]] | ✅ Running (:1456 + :8088) |
| [[concepts/OpenCode\|OpenCode]] | ✅ Installed (37 skills) |
| [[concepts/MiMo Code\|MiMoCode]] | ✅ Installed |
| [[concepts/Claude Code\|Claude Code]] | ✅ Installed (37 skills) |
| [[concepts/Hermes Agent\|Hermes Agent]] | ✅ Installed (36 skills, 2 plugins) |
| [[concepts/OpenAI Codex\|OpenAI Codex]] | ✅ Installed |
| [[concepts/Grok\|Grok]] | ✅ Installed |
| [[entities/Owl-Agent\|Owl-Agent]] | ✅ Active |

