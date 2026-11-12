#!/usr/bin/env bash
# Prints files in _raw/inbox (and legacy unprocessed files in _raw/) modified since last ingest.
# Run from the vault root: bash .claude/scripts/diff-inbox.sh

set -euo pipefail
MANIFEST=".claude/inbox-manifest.json"
[ -f "$MANIFEST" ] || echo '{}' > "$MANIFEST"

get_mtime() {
  stat -c %Y "$1" 2>/dev/null || stat -f %m "$1" 2>/dev/null || echo 0
}

is_newer() {
  local f="$1" mtime recorded
  mtime=$(get_mtime "$f")
  recorded=$(python3 - "$MANIFEST" "$f" <<'PY'
import json,sys
m=json.load(open(sys.argv[1]))
v=m.get(sys.argv[2],0)
try:
    print(int(float(v)))
except Exception:
    print(0)
PY
)
  [ "${mtime:-0}" -gt "${recorded:-0}" ]
}

shopt -s nullglob
for f in _raw/inbox/*.md _raw/inbox/*.txt; do
  [ -e "$f" ] || continue
  is_newer "$f" && echo "$f"
done
# Legacy: unprocessed captures directly in _raw/ (exclude index/archived)
for f in _raw/*.md _raw/*.txt; do
  [ -e "$f" ] || continue
  case "$(basename "$f")" in index.md|README.md) continue ;; esac
  grep -qE '^processed:\s*true' "$f" 2>/dev/null && continue
  is_newer "$f" && echo "$f"
done
