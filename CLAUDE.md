# Claude Memory Protocol → see AGENTS.md

This file used to hold a second, Parallel Compounding Memory protocol. It now delegates to the single canonical protocol in `AGENTS.md` ("## Claude Memory Protocol (Compounding, coexists with v7.6)") to avoid split-brain instructions.

Read `AGENTS.md`. That section defines ingest / ask / lint, layer mapping, canonical-folder precedence, and the command surface (`/ingest`, `/ask`, `/lint` for both Claude Code `.claude/commands/` and OpenCode `.opencode/command/`).

Additions specific to this file's former standalone role:
- `00-INDEX.md` is the curator's compact retrieval cache; `index.md` remains the curated map. Regenerate the Wiki section from `wiki/` frontmatter only.
- Raw originals in `_raw/` are immutable. A wrong claim is corrected by a new raw note, never by editing history.
- Vault MCP (`vault_read`/`vault_write`/`vault_append`/`vault_patch`/`search_simple`) is the preferred way to read and write vault pages.
