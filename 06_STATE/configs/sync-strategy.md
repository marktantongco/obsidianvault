---
title: Sync & Conflict Strategy
tags: [sync, git, conflict, strategy]
lifecycle: active
tier: supporting
---

# Sync & Conflict Strategy

## Git Sync Cadence

| Device | Auto Commit | Auto Push | Auto Pull | Merge Strategy |
|--------|-------------|-----------|-----------|----------------|
| Desktop (primary) | Every 10 min | Every 30 min | Every 5 min | Standard merge |
| Mobile (plugin) | Every 10 min | Every 30 min | On startup | `theirs` (local wins) |
| Mobile (Termux) | Manual / cron | Manual / cron | Before commit | `theirs` |

## Conflict Resolution Rules

1. **Frontmatter preservation**: If frontmatter conflicts, merge keys (union of both sides). `created` keeps earliest. `updated` keeps latest.
2. **Body conflicts**: Insert conflict markers `<<<<<<< HEAD` etc. Do NOT auto-resolve. Agent flags for manual review.
3. **File renames**: Git tracks renames. If conflict, prefer newer timestamp.
4. **Binary attachments**: Never commit binaries >1MB to git. Use `.gitignore` + external storage (NAS, S3-compatible).

## Backup / Rollback

| Scenario | Recovery |
|----------|----------|
| Vault corruption | `git reflog` → find last good commit → `git reset --hard <hash>` |
| Remote repo compromised | Local clone is backup. Re-init remote, force push from known-good local. |
| Mobile edit lost | Check `git stash list`. Poznote retains original until pipeline processes. |
| Simultaneous edit conflict | Frontmatter auto-merged. Body gets conflict markers. Hermes routes to E2 (Codex) for resolution suggestion. |

## Simultaneous Edit Handling

Mobile captures are quick notes (Poznote-style). Desktop edits are deep work.
- If mobile pushes before desktop pulls: desktop gets merge conflict on next pull.
- Resolution: desktop user reviews conflict markers, keeps both versions if unsure.
- Prevention: mobile uses `_raw/poznote/` for captures, desktop organizes into final buckets. Inbox is append-only, rarely conflicts.

## Related

- [[skills/mobile-sync-termux|Mobile Sync Termux]] — Termux-based sync setup
- [[06_STATE/configs/poznote-capture-schema|Poznote Capture Schema]] — Inbox capture workflow
- [[skills/git-sync-strategy|Git Sync Strategy]] — Commit and push rules
