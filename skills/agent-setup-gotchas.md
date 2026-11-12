---
title: Agent Setup Gotchas
category: skills
tags: [setup, agents, troubleshooting, gotchas, python, obsidian, github]
relationships:
  - target: "[[concepts/AI Agents]]"
    type: related_to
  - target: "[[concepts/Obsidian Wiki]]"
    type: uses
  - target: "[[concepts/Hermes Agent]]"
    type: related_to
  - target: "[[concepts/OpenCode]]"
    type: related_to
  - target: "[[skills/multi-agent-vault-wiring]]"
    type: related_to
sources:
  - conversation:2026-07-09
  - _raw/_archived/2026-07-09-multi-agent-setup-gotchas.md
summary: The six failures that eat a multi-agent setup session — GitHub 429s on plugin assets, PEP 668, missing git-remote-https, half-installed Obsidian plugins, Hermes' Python pin, and OpenCode's strict config schema — each with the workaround that actually worked.
provenance: {extracted: 0.8, inferred: 0.2, ambiguous: 0.0}
base_confidence: 0.75
lifecycle: draft
lifecycle_changed: 2026-07-09
tier: supporting
created: 2026-07-09
updated: 2026-11-13
processed: true
processed_at: 2026-11-13
---

# Agent Setup Gotchas

Failures hit while standing up the multi-agent stack (`[[skills/multi-agent-vault-wiring]]`): every item below has a confirmed workaround, so check this page before debugging from scratch.

## 1. GitHub raw downloads get HTTP 429

- **Cause:** raw content is rate limited per IP; pulling several `main.js` plugin files back to back trips it.
- **Fix:** wait ~1 hour, install through Obsidian's Community Plugin browser, or space downloads 5–10 s apart; prefer release ZIP/tarball assets over per-file raw fetches.
- **Impact:** blocked automatic install of 5 of 6 Obsidian plugins.

## 2. `pip install` fails with "externally-managed-environment"

- **Cause:** PEP 668 — system Python refuses user installs that could break distro tooling.
- **Fix:** venv (`python3 -m venv`), or `pip install --break-system-packages <pkg>` as the quick path. `uv` is the faster isolated option.

## 3. `git clone` fails with "git: 'remote-https' is not a git command"

- **Cause:** `git-remote-https` missing from a minimal git install.
- **Fix:** fetch the tarball instead — `curl -fsSL https://github.com/<user>/<repo>/archive/refs/heads/main.tar.gz | tar xz` — or install the git http transport.

## 4. Obsidian plugins need *both* `manifest.json` and `main.js`

- **Cause:** plugins ship as release assets, not as files on the branch; a rate-limited download silently yields a plugin that never loads.
- **Fix:** GUI install via the Community Plugin browser, or release ZIP once the limit resets.

## 5. Hermes needs Python 3.11–3.13

- **Cause:** `pip install hermes-agent` pins `>=3.11,<3.14`; a 3.14 system Python fails.
- **Fix:** dedicated interpreter venv —
  ```bash
  cd ~/.hermes/hermes-agent
  python3.11 -m venv .venv && .venv/bin/pip install -e .
  ```
- See `[[concepts/Hermes Agent]]` for the orchestrator itself.

## 6. OpenCode rejects unknown config keys

- **Cause:** `Unrecognized key: permissions` — the schema is strict and validated at load.
- **Fix:** remove unsupported keys from the active config file. In OpenCode v2 the file is `~/.config/opencode/opencode.json`, not `~/opencode.json`; a project-level `.opencode/opencode.json` silently overrides it. See `[[concepts/OpenCode]]`.

## Recovery patterns

- **429 loop:** stop all attempts → wait an hour → switch to release assets → add delays → prefer the built-in browser.
- **Python too new:** check `Requires-Python` first, then choose `--break-system-packages` (throwaway) vs venv (anything with a daemon or systemd unit).

## Related

- [[skills/multi-agent-vault-wiring]] — wiring one vault into every CLI agent
- [[concepts/AI Agents]] · [[concepts/Obsidian Wiki]] · [[concepts/OpenCode]] · [[concepts/Hermes Agent]]

## Notes

- **2026-11-13** — Ingested from `_raw/_archived/2026-07-09-multi-agent-setup-gotchas.md`. Findings 1–5 still reproduce on this host; finding 6 is sharper in v2: strict schema *and* a project-level config file can override the global one without warning.
