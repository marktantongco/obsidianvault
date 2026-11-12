#!/usr/bin/env bash
# vault-lock — single-writer guard for the Obsidian vault.
#
# Why: several writers touch this vault (agent sessions, obsidian-git's auto-commit,
# the daily edge-sync Action). Content edits are the dangerous ones: two agents editing
# the same page race, and a later `git add -A` sweeps the other session's half-finished
# work into someone else's commit. This gives content writers one mutex with a TTL so a
# crashed session cannot wedge the vault.
#
# The lock lives in .git/ — it is per-clone, not per-remote, which is the honest scope:
# it coordinates writers on this machine, not the GitHub Action or the phone.
#
# Usage
#   vault-lock acquire [purpose]        # exit 0 acquired, 3 busy, 4 error
#   vault-lock release [--force]
#   vault-lock status [--json]
#   vault-lock touch                    # extend the TTL (long jobs)
#   vault-lock run <purpose> -- <cmd...>  # acquire, run, always release
#   vault-lock guard                    # session-start report (does not acquire)
#
# Env
#   VAULT_DIR        vault root (default: git toplevel of this script)
#   VAULT_WRITER_ID  identity for logs (agents should set e.g. opencode:ses_abc)
#   VAULT_LOCK_TTL   seconds before a lock is considered abandoned (default 1800)
#   VAULT_LOCK_WAIT  seconds to wait for a held lock before giving up (default 0)
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"   # follow the ~/.local/bin symlink
VAULT="${VAULT_DIR:-$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)}"
[ -n "$VAULT" ] || { echo "vault-lock: not inside a git repository (set VAULT_DIR)" >&2; exit 4; }
GITDIR="$(git -C "$VAULT" rev-parse --absolute-git-dir)"
LOCK="$GITDIR/vault-writer.lock"     # flock target, never parsed
STATE="$GITDIR/vault-writer.state"   # KEY=VALUE holder record
EVENTS="$GITDIR/vault-writer.log"    # append-only audit trail
TTL="${VAULT_LOCK_TTL:-1800}"
WAIT="${VAULT_LOCK_WAIT:-0}"
WRITER="${VAULT_WRITER_ID:-pid$PPID}"

now() { date +%s; }
clean() { printf '%s' "$1" | tr -d '\r\n\t' | cut -c1-60; }
event() { printf '%s %s %s\n' "$(date -Is)" "$WRITER" "$*" >> "$EVENTS"; }
get() { sed -n "s/^$1=//p" "$STATE" 2>/dev/null | head -1; }

# Discover whether a holder still owns the lock. TTL is authoritative: a writer that
# cannot call release (agent killed, window closed) must not block the vault forever.
holder() {
  [ -f "$STATE" ] || { echo "free"; return; }
  local w p a e pid rem
  w=$(get writer); p=$(get purpose); a=$(get acquired_at); e=$(get expires_at); pid=$(get pid)
  rem=$(( ${e:-0} - $(now) ))
  if [ "$rem" -le 0 ]; then
    echo "stale|$w|$p|$a|${pid:-?}|$rem"
  else
    echo "held|$w|$p|$a|${pid:-?}|$rem"
  fi
}

# Take the mutex, then decide under it. Two acquires cannot race past each other.
lock_fd() { exec 9>"$LOCK"; flock -w "$WAIT" 9; }

cmd_acquire() {
  local purpose; purpose=$(clean "${1:-work}")
  lock_fd || { echo "vault-lock: timed out after ${WAIT}s waiting for the mutex" >&2; exit 3; }
  local h; h=$(holder)
  if [ "${h%%|*}" = "held" ]; then
    local IFS='|'; read -r _ w p a pid rem <<< "$h"
    printf 'vault-lock: BUSY — %s holds it (%s, %ss left, pid %s)\n' "$w" "$p" "$rem" "$pid" >&2
    echo "vault-lock: retry later, or 'vault-lock status' / 'vault-lock run <purpose> -- <cmd>'" >&2
    exit 3
  fi
  if [ "${h%%|*}" = "stale" ]; then
    local IFS='|'; read -r _ w p a pid rem <<< "$h"
    event "STEAL stale holder=$w purpose=$p acquired=$a"
    echo "vault-lock: took over an abandoned lock from $w (expired $(( -rem ))s ago)" >&2
  fi
  {
    echo "writer=$WRITER"
    echo "purpose=$purpose"
    echo "acquired_at=$(now)"
    echo "expires_at=$(( $(now) + TTL ))"
    echo "pid=$PPID"
    echo "host=$(hostname)"
    echo "dir=$VAULT"
  } > "$STATE"
  event "ACQUIRE purpose=$purpose ttl=${TTL}s"
  echo "vault-lock: acquired by $WRITER ($purpose, ${TTL}s)"
  exit 0
}

cmd_release() {
  local force=0; [ "${1:-}" = "--force" ] && force=1
  lock_fd || exit 4
  [ -f "$STATE" ] || { echo "vault-lock: nothing held"; exit 0; }
  local w; w=$(get writer)
  if [ "$w" != "$WRITER" ] && [ "$force" != 1 ]; then
    echo "vault-lock: held by $w, not $WRITER — refusing (use --force)" >&2
    exit 3
  fi
  rm -f "$STATE"
  event "RELEASE"$([ "$force" = 1 ] && echo " forced holder=$w")
  echo "vault-lock: released"
  exit 0
}

cmd_touch() {
  lock_fd || exit 4
  [ -f "$STATE" ] || { echo "vault-lock: nothing held" >&2; exit 1; }
  local w; w=$(get writer)
  [ "$w" = "$WRITER" ] || { echo "vault-lock: held by $w, not $WRITER — cannot extend" >&2; exit 3; }
  sed -i "s/^expires_at=.*/expires_at=$(( $(now) + TTL ))/" "$STATE"
  event "TOUCH ttl=${TTL}s"
  echo "vault-lock: extended by ${TTL}s"
}

cmd_status() {
  local json=0; [ "${1:-}" = "--json" ] && json=1
  local h; h=$(holder)
  local IFS='|'; read -r kind w p a pid rem <<< "$h"
  if [ "$json" = 1 ]; then
    if [ "$kind" = "free" ]; then
      printf '{"state":"free","vault":"%s"}\n' "$VAULT"
    else
      printf '{"state":"%s","writer":"%s","purpose":"%s","acquired_at":%s,"pid":"%s","remaining_s":%s,"vault":"%s"}\n' \
        "$kind" "$w" "$p" "${a:-0}" "$pid" "$rem" "$VAULT"
    fi
    return 0
  fi
  printf 'vault: %s\n' "$VAULT"
  case "$kind" in
    free) echo "lock:   FREE" ;;
    held) printf 'lock:   HELD by %s (%s), %ss left, pid %s\n' "$w" "$p" "$rem" "$pid" ;;
    stale) printf 'lock:   STALE (abandoned by %s, %s), safe to steal\n' "$w" "$p" ;;
  esac
  echo "events: $EVENTS"
}

cmd_run() {
  local purpose="work"
  [ $# -gt 0 ] && [ "$1" != "--" ] && { purpose=$(clean "$1"); shift; }
  [ "${1:-}" = "--" ] && shift
  [ $# -gt 0 ] || { echo "usage: vault-lock run <purpose> -- <cmd...>" >&2; exit 4; }
  VAULT_LOCK_TTL="$TTL" VAULT_WRITER_ID="$WRITER" "$0" acquire "$purpose" || exit $?
  trap 'VAULT_WRITER_ID="$WRITER" "$0" release >/dev/null 2>&1 || true' EXIT INT TERM
  "$@"
  local rc=$?
  VAULT_WRITER_ID="$WRITER" "$0" release >/dev/null 2>&1 || true
  trap - EXIT INT TERM
  return $rc
}

# Session-start report. Does not acquire — it tells an agent what it is walking into,
# which is the moment the collision actually happens.
cmd_guard() {
  cmd_status
  local dirty gen ahead behind
  dirty=$(git -C "$VAULT" status --porcelain | wc -l)
  gen=$(git -C "$VAULT" status --porcelain -- index.md hot.md log.md 00-INDEX.md | wc -l)
  ahead=$(git -C "$VAULT" rev-list --count 'origin/master..HEAD' 2>/dev/null || echo '?')
  behind=$(git -C "$VAULT" rev-list --count 'HEAD..origin/master' 2>/dev/null || echo '?')
  printf 'dirty:  %s file(s)\n' "$dirty"
  [ "$gen" -gt 0 ] && printf 'warn:   %s generated/derived file(s) modified — index.md/hot.md/log.md are owned by the daily Action, 00-INDEX.md by the index pass\n' "$gen"
  printf 'remote: %s ahead, %s behind origin/master\n' "$ahead" "$behind"
  if [ "$dirty" -gt 0 ]; then
    echo "note:   uncommitted work is not yours unless you made it — never 'git add -A'"
    git -C "$VAULT" status --porcelain | head -5 | sed 's/^/        /'
  fi
  echo "next:   vault-lock run <purpose> -- <cmd>   (or acquire / release around edits)"
}

case "${1:-}" in
  acquire) shift; cmd_acquire "$@" ;;
  release) shift; cmd_release "$@" ;;
  status)  shift; cmd_status "$@" ;;
  touch)   shift; cmd_touch ;;
  run)     shift; cmd_run "$@" ;;
  guard)   shift; cmd_guard ;;
  *) sed -n '2,30p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 64 ;;
esac
