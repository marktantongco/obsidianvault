---
title: Kiro CLI Pool-Proxy — Architecture & 403 Debug
tags:
  - kiro
  - proxy
  - auth
  - debugging
  - session
created: 2026-08-03T12:00:00+08:00
updated: 2026-08-03T13:00:00+08:00
category: skill
aliases:
  - kiro-pool-proxy
  - kiro-cli-pool-proxy 403
---

# Kiro CLI Pool-Proxy — Architecture & 403 Debug

Findings from reverse-engineering the `kiro-cli-pool-proxy` Go project at
`/home/ubuntu/kiro-cli-pool-proxy/` (running on `127.0.0.1:5000`), driven by
`kiro-cli chat` failing with **403 AccessDenied from AWS** after MCP servers
load.

## Architecture

- **Plain HTTP reverse-proxy for Kiro CLI** — the CLI is pointed at the proxy
  via its built-in endpoint settings (`http://127.0.0.1:5000` for
  `api.krs`, `api.cps`, `api.codewhisperer`). No MITM, no cert, no CLI fork.
- **Account pool** (`pool/pool.go`): round-robin account selection with
  per-account cooldown + rotation (`strategy: "smart"`).
- **Auth module** (`auth/`): multiple import/refresh flows — social (Kiro
  desktop), AWS Builder ID device-code, IAM SSO, Microsoft SSO, and raw SSO
  token import.
- **Request path** (`proxy/server.go`): validates the pool API key
  (`kpp-...`), swaps the `Authorization` header to the pool account's
  `accessToken`, rewrites `profileArn` in the body, and forwards to
  `runtime.us-east-1.kiro.dev` (social) with `tokentype: EXTERNAL_IDP`.
- **Refresh** (`auth/refresh.go`): social refresh via
  `prod.us-east-1.auth.desktop.kiro.dev/refreshToken` with a
  Kiro-desktop User-Agent.
- **Probe** (`proxy/probe.go`): dedicated admin "test model" client, separate
  from the hot path so probes never contend with chat.

## Diagnosis journey (what was ruled out)

1. **Wrong authMethod**: account stored `authMethod: "social"` but login was
   Builder ID (OIDC). The social refresh endpoint rejects non-social tokens →
   403. Fix: set `authMethod` to empty (falls through to OIDC refresh).
2. **poolKey check**: `X-Pool-Key` mismatch returns plain-text
   `forbidden\n`. Client must present the pool key / seeded API key.
3. **Token scopes**: Builder-ID tokens carry only data-plane scopes
   (`codewhisperer:completions/analysis/conversations`) — no
   `ListAvailableProfiles`, so control-plane profile discovery returns
   AccessDenied.
4. **Initial hypothesis (WRONG)**: "add `profileArn` to the account entry in
   `data/config.json`". The imported account did lack `profileArn`, but that
   was not the real blocker.

## Real root cause

- The kiro binary's `GenerateAssistantResponse` (data-plane chat) request body
  **does not include `profileArn` at all** — the proxy must inject it.
- The pool-proxy's `RewriteProfileArn(body, account.ProfileArn)` is a **no-op
  when `account.ProfileArn` is empty** (returns body unchanged), and the
  account had no profileArn.
- Result: AWS receives the chat request with **no profileArn** → rejects with
  `ValidationException: profileArn is required for this request`.

## The fix (verified working)

Inject the ARN that is **hardcoded in the kiro binary** itself
(`crates/fig_api_client/src/profile_resolver.rs:70` — the fallback used when
profile discovery fails):

- `fallbackProfileArn(region)` →
  `arn:aws:codewhisperer:{region}:638616132270:profile/AAAACCCCXXXX`
- `InjectProfileArn(body, arn)` → inserts `"profileArn":"..."` into the JSON
  body when the request is chat-shaped and the account has no profileArn.

Applied in three files: `proxy/rewrite.go` (new helpers), `proxy/server.go`
and `proxy/anthropic.go` (call sites).

**Verification:** `echo "2+2" | kiro-cli chat` → `"2 + 2 = 4"` with credits
shown. Chat works end-to-end through the pool-proxy. The same fix was ported
to **Cybx-GateawayQue** (which has the identical profileArn bug) as
[PR #7](https://github.com/cybha22/Cybx-GateawayQue/pull/7).

## Operational notes

- The systemd unit `kiro-pool-proxy.service` auto-restarts the proxy — manual
  `kill`/restarts get overridden; edit config + `systemctl restart` instead.
- The auth token is stored in SQLite (`auth_kv`); `setup-client.sh` seeds a
  **fake token** (the pool API key) so the pool-proxy can swap in real account
  tokens — do not confuse the two.
- A `200` upstream response can still carry an error embedded in the **SSE
  stream** (not an HTTP error) — check the streamed body, not just status.

## Sources

- `opencode://ses_03c73d3c3ffelzHaSEov3k2G1K` (Reverse engineer pool-proxy)
- `opencode://ses_03c75d623ffewZf22YfpXIFnRE` (Reverse engineer kiro proxy)
- `opencode://ses_04130bd30ffer8ksOS4f1Cl33E` (OpenCode debug config — fix &
  verification)
