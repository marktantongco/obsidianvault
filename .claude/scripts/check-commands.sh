#!/usr/bin/env bash
# Command-list check: are /ingest, /ask, /lint actually exposed to each agent client?
#
#   bash .claude/scripts/check-commands.sh          # from vault root
#   bash .claude/scripts/check-commands.sh --all    # list every command per client
#
# Claude Code  : discovers .claude/commands/<name>.md (no CLI listing surface -> parsed).
# OpenCode v2  : discovers .opencode/command*/<name>.md per project directory, but only when
#                the server is asked about THAT directory; a cold instance answers [].
#                Reuses the single canonical file: both clients read the same command names
#                from their own dir, so the bodies must stay in sync (see CLAUDE.md).
set -uo pipefail
VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WANT=(ingest ask lint)
ALL=0; [ "${1:-}" = "--all" ] && ALL=1

echo "vault: $VAULT"

# ---------- Claude Code ----------
echo
echo "Claude Code  (.claude/commands/)"
declare -A CC
for f in "$VAULT"/.claude/commands/*.md; do
  [ -e "$f" ] || continue
  n=$(basename "$f" .md)
  d=$(python3 - "$f" <<'PY'
import sys,re
t=open(sys.argv[1],encoding='utf-8').read()
m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
desc=''
if m:
    dm=re.search(r'^description:\s*(.+)$',m.group(1),re.M)
    if dm: desc=dm.group(1).strip().strip('"\'')
if not desc:
    for line in t.splitlines():
        if line.strip() and not line.startswith('---'): desc=line.strip()[:70]; break
print(desc)
PY
)
  CC["$n"]="$d"
  [ "$ALL" = 1 ] && printf '  %-16s %s\n' "/$n" "$d"
done
for n in "${WANT[@]}"; do
  if [ -n "${CC[$n]:-}" ]; then printf '  PASS /%s\n' "$n"; else printf '  FAIL /%s (no .claude/commands/%s.md)\n' "$n" "$n"; fi
done

# ---------- OpenCode ----------
echo
echo "OpenCode  (api GET /api/command, directory=$VAULT)"
LIST=""
for attempt in 1 2 3; do
  LIST=$(opencode api GET /api/command -H "x-opencode-directory: $VAULT" 2>/dev/null)
  [ -n "$LIST" ] && ! printf '%s' "$LIST" | grep -q '"data":\[\]' && break
  sleep 3   # cold instance answers with an empty list before config/dir load
done
if [ -z "$LIST" ]; then
  echo "  UNKNOWN (opencode server unreachable: opencode service status)"
  exit 1
fi
python3 - "$LIST" "$ALL" "${WANT[@]}" <<'PY'
import json,sys
raw=sys.argv[1]; show_all=sys.argv[2]=='1'; want=sys.argv[3:]
try:
    d=json.loads(raw)
except Exception:
    print('  UNKNOWN (non-JSON reply from server)'); sys.exit(1)
loc=d.get('location',{}).get('directory')
cmds={c['name']:c.get('description','') for c in d.get('data') or []}
print(f"  server resolved directory: {loc}  ({len(cmds)} commands)")
if show_all:
    for k in sorted(cmds): print(f"  {k:24} {cmds[k][:60]}")
for n in want:
    print(f"  {'PASS' if n in cmds else 'FAIL'} /{n}" + ('' if n in cmds else ' (not registered for this directory)'))
sys.exit(0 if all(n in cmds for n in want) else 1)
PY
