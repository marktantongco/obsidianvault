---
title: Daily Note
date: <% tp.date.now("YYYY-MM-DD") %>
type: daily
tags: [daily, proxy-check]
lifecycle: active
tier: core
---

# <% tp.date.now("dddd, MMMM D, YYYY") %>

## 🖥️ Proxy Status Check

> Run this in your terminal to check all proxy services:
> ```bash
> ./freebuff.sh status && ./freebuff.sh smoke
> ```

| Service | Port | Expected | Check |
|---------|------|----------|-------|
| jcode-daemon | `:1456` | ✅ Running | `curl -sf http://127.0.0.1:1456/health` |
| jcode-proxy | `:8088` | ✅ Running | `curl -sf http://127.0.0.1:8088/health` |
| mimo-unified | `:8877` | ✅ Running | `curl -sf http://127.0.0.1:8877/v1/models` |

📊 Full dashboard: [[dashboards/proxy-dashboard|Proxy Dashboard]]

---

## 📋 Tasks

- [ ] 

## 📝 Notes


## 💡 Learnings


## 🔗 Related

- [[hot|Recent Activity]]
- [[dashboards/proxy-dashboard|Proxy Dashboard]]
- [[<% tp.date.now("YYYY-MM-DD", -1) %>|Yesterday]]
