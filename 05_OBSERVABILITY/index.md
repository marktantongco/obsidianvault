---
title: OBSERVABILITY — Logs, Metrics & Dashboards
bucket: OBSERVABILITY
path: 05_OBSERVABILITY/
purpose: System logs, metrics, dashboards
lifecycle: active
tier: core
---

# 05_OBSERVABILITY — System Logs, Metrics & Dashboards

This bucket holds system observability data — session logs, error records, system status, and operational metrics. It is one of the most valuable buckets for agents diagnosing system state.

## Current Content

This bucket is populated by files matching these classification keywords: `metric`, `log`, `monitor`, `alert`, `dashboard`.

### Session Logs (4 journal entries)
| Entry | Date | Content |
|-------|------|---------|
| [[journal/2026-07-09-multi-agent-wiki-compound]] | 2026-07-09 | Setup refresh, @ai ingest, multi-agent capture |
| [[journal/2026-07-13-second-brain-integration-session]] | 2026-07-13 | Full second brain integration across 7 agents |
| [[journal/2026-07-14-system-admin-tool-installs]] | 2026-07-14 | MCP cleanup, Docker disable, AI tool installs |
| [[journal/2026-07-21-freebuff-vault-enrichment-session]] | 2026-07-21 | Vault enrichment: concept pages, entity thickening |

### System Health Documentation
- [[SYSTEM-COMPLETE]] — Full system inventory: 20 items installed
- [[SYSTEM-INSTALLATION-STATUS]] — Detailed installation status per component
- [[ERROR-LOG]] — Active and resolved errors with patterns
- [[TROUBLESHOOTING]] — Comprehensive troubleshooting guide

### Monitoring References
- [[hot]] — Recent activity cache
- [[log]] — Query log

### Activity Tracking
- [[AGENTS.md]] — Vault conventions and session bootstrap protocol

## Related Buckets
- [[06_STATE/index|06_STATE]] — System configs and runtime state
- [[02_KNOWLEDGE/index|02_KNOWLEDGE]] — Concepts inferred from log analysis
