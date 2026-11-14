---
description: Trigger Obsidian Git autosave (commit-and-sync) and verify vault sync
---

# Obsidian Autosave

Force an immediate Obsidian Git autosave/sync for `/home/x1/Projects/obsidianvault` and report the result. Optional argument: `$ARGUMENTS` (used as the commit message when provided).

## 1. Ensure Obsidian + MCP are up

Run:

```bash
obsidian-mcp --doctor
```

If it reports `verdict: FAIL`, start Obsidian durably (transient user unit) and wait for the listener:

```bash
systemctl --user reset-failed obsidian.service 2>/dev/null || true
systemctl --user is-active obsidian.service >/dev/null 2>&1 || \
systemd-run --user --unit=obsidian --collect \
  --property=Environment=DISPLAY=:0 \
  --property=Environment=WAYLAND_DISPLAY=wayland-1 \
  --property=Environment=XDG_RUNTIME_DIR=/run/user/1000 \
  --property=Environment=DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
  /usr/bin/obsidian
```

Wait up to ~30 s for `https://127.0.0.1:27124` to accept connections, then re-run `obsidian-mcp --doctor`. If it still fails, stop and report — do not fall back to direct git writes.

Fallback launcher if `systemd-run` is unavailable:

```bash
nohup setsid obsidian >/tmp/obsidian-launch.log 2>&1 &
```

## 2. Capture before-state

```bash
git -C /home/x1/Projects/obsidianvault status -sb
git -C /home/x1/Projects/obsidianvault log --oneline -3
```

## 3. Trigger autosave (commit-and-sync)

Read the API key from `.obsidian/plugins/obsidian-local-rest-api/data.json` (never print it), then call the Obsidian Git plugin command:

```bash
APIKEY=$(python3 -c "import json;print(json.load(open('/home/x1/Projects/obsidianvault/.obsidian/plugins/obsidian-local-rest-api/data.json'))['apiKey'])")
curl -sk -X POST \
  -H "Authorization: Bearer $APIKEY" \
  "https://127.0.0.1:27124/commands/obsidian-git:push/"
```

`obsidian-git:push` = “Git: Commit-and-sync”. If a commit message was supplied via `$ARGUMENTS`, prefer `obsidian-git:commit-push-specified-message` (check its input schema via `GET https://127.0.0.1:27124/commands/` first).

If the push is rejected as non-fast-forward, run once and retry:

```bash
git -C /home/x1/Projects/obsidianvault pull --rebase -X theirs origin master
```

Never hand-edit `index.md`, `hot.md`, `log.md`, or `cache.json` — the edge-sync webhook regenerates them.

## 4. Verify

```bash
git -C /home/x1/Projects/obsidianvault status -sb
git -C /home/x1/Projects/obsidianvault log --oneline -3
git -C /home/x1/Projects/obsidianvault fetch origin
git -C /home/x1/Projects/obsidianvault rev-list --left-right --count origin/master...HEAD
```

Note: the GitHub webhook may add an `[edge-sync]` commit shortly after a successful push, so a brief “behind by one” can be normal.

## 5. Report

State whether a commit/push occurred, the resulting HEAD, and any remaining uncommitted files. If there was nothing to save, say so explicitly (no-op).

## Notes

- This uses the Obsidian Git plugin’s own routines (not raw `git commit`/`push`) so it stays consistent with the plugin’s `autoCommit`/`autoPush` settings and the `gh auth git-credential` helper.
- Plugin cadence in `.obsidian/plugins/obsidian-git/data.json`: `autoSaveInterval=5`, `autoPushInterval=10`; this command forces both immediately.
- Do not acquire the vault writer lock unless you are also editing pages; autosave only commits.
