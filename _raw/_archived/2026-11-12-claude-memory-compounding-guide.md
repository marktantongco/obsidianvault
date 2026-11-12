---
title: "Giving Claude Code a Memory That Compounds Instead of Resets (source guide)"
category: reference
tags: [claude, obsidian, memory, karpathy, wiki, workflow]
summary: "Raw source guide for Karpathy-style compounding memory (raw/wiki/output, CLAUDE.md schema, index cache, ingest/ask/lint, manifest)."
lifecycle: draft
tier: core
source: conversation
confidence: 0.95
created: 2026-11-12
updated: 2026-11-12
processed: true
processed_at: 2026-11-12
---

# Giving Claude Code a Memory That Compounds Instead of Resets

---

## 0. The Problem (Why This Exists)

Claude Code has no memory between sessions. Every terminal window starts at zero.

- It re-reads your codebase, but not your *decisions* ("we tried Firebase, moved to Supabase, here's why").
- You re-explain the same project context every session — burning tokens on recap instead of work.
- Without a fixed source of truth, answers drift: one session says X, the next contradicts it.

CLAUDE.md alone doesn't fix this — it's a static instruction file, not a growing memory. You need a place for *accumulated* knowledge that Claude reads from and writes to, session after session.

This pattern is not new. Andrej Karpathy described it publicly in early 2026: use an LLM to maintain a plain-markdown personal wiki instead of building a RAG/vector-database pipeline. Source docs go in one folder; the model compiles them into a structured, cross-linked wiki; the wiki compounds in value every time you use it. This framework is that pattern, adapted into a concrete, reusable folder + file spec for Claude Code + Obsidian.

---

## 1. Setup (5 minutes)

1. Download Obsidian (free): https://obsidian.md
2. Create a vault — **one per domain**. Don't merge "client work" and "personal journal" into one vault; Claude's index gets noisy and you lose the ability to point Claude at just one context.
3. Open the vault folder in your terminal. This is where you'll run `claude`.

```bash
mkdir -p ~/vaults/work-brain && cd ~/vaults/work-brain
git init   # optional but recommended — free version history + backup
```

---

## 2. Folder Structure (The Three Layers)

```
work-brain/
├── CLAUDE.md              ← the schema (Claude reads this first, every session)
├── 00-INDEX.md            ← the cache (compact map of everything, read second)
├── raw/                   ← Layer 1: input, untouched, immutable
│   ├── inbox/             ← anything dropped in — transcripts, pasted notes, emails
│   └── _processed/        ← raw files Claude has already ingested (archived, not deleted)
├── wiki/                  ← Layer 2: Claude-maintained knowledge, the actual brain
│   ├── people/
│   ├── projects/
│   ├── decisions/
│   ├── concepts/
│   └── _moc/              ← Maps of Content — one index note per domain folder
├── output/                ← Layer 3: finished deliverables pulled FROM the wiki
└── .claude/
    ├── commands/          ← slash commands (below)
    └── manifest.json      ← change-tracking file (below)
```

**Rule that makes this work:** files in `raw/` are immutable once saved. You never edit them — they're your source of truth. Everything derived goes into `wiki/`. If wiki content turns out wrong, you don't edit the wiki page by hand — you drop a new raw note that corrects it, and let Claude reconcile. This keeps provenance intact: every claim in the wiki traces back to a raw source.

---

## 3. CLAUDE.md — The Schema

This is the single highest-leverage file in the system. Claude reads it at the start of every session — it's the onboarding doc for your AI's permanent memory.

```markdown
# work-brain — Wiki Protocol

You are the maintainer of this knowledge base. Two jobs:

## Job 1: Ingest
When asked to process `raw/inbox/`, for each unprocessed file:
1. Read the file. Identify its type: person, project, decision, concept, or meeting.
2. Search `wiki/` for an existing page with the same entity (check title + `aliases` in frontmatter).
3. If a match exists: append a new dated subsection to that page. Never overwrite existing content.
4. If no match exists: create a new page in the matching subfolder using the template below.
5. Add `[[wikilinks]]` to every other entity mentioned (person, project, concept). Create stub
   pages for entities that don't have one yet (title + `status: stub` frontmatter only).
6. Update the relevant `_moc/` (Map of Content) page: add a link to any new or updated page.
7. Move the raw file to `raw/_processed/` and add `processed: true` + today's date to its frontmatter.
8. Regenerate `00-INDEX.md` (see format below).

## Job 2: Answer
When asked a question:
1. Read `00-INDEX.md` first — never read the whole vault.
2. From the index, identify 2–5 candidate pages. Read only those.
3. If those pages link to others you need, follow the links — don't grep the whole vault.
4. Answer, and cite which wiki pages you drew from.

## Conventions
- Every wiki page has YAML frontmatter: `type`, `status`, `tags`, `created`, `updated`, `aliases`.
- Every page ends with a `## Notes` section listing dated entries — this is the append log.
- Never delete a wikilink because the target page doesn't exist yet — create a stub instead.
- Orphan pages (zero backlinks) are a defect. Flag them when you find one.
- Contradictions between a new raw note and an existing wiki page: don't silently overwrite.
  Add a `> [!contradiction]` callout noting both claims and their source dates.
```

---

## 4. Note Template (Wiki Layer)

Every page Claude creates in `wiki/` follows this shape — consistent frontmatter is what makes the index cheap to generate and cheap to read.

```markdown
---
type: project          # person | project | decision | concept | meeting
status: active         # active | stub | archived
tags: [client-work, ai-creative]
aliases: []
created: 2026-07-07
updated: 2026-07-07
---

# powerUP Brand Runtime

One-line summary Claude can put straight into an index without re-reading the page.

## Links
[[Mark Tantongco]] · [[React/Vite Stack]] · [[Vercel Deployment]]

## Notes
### 2026-07-07 — source: raw/inbox/2026-07-07-standup.md
What happened, decided, or learned. Short. Dated. Append-only.
```

---

## 5. The Index — `00-INDEX.md` (This Is the Efficiency Layer)

This file is what makes the whole system cheap. Claude reads this instead of the full vault — one file, maybe 800–1500 tokens, instead of scanning every page.

```markdown
# Index — last regenerated 2026-07-07

## Projects
- [[powerUP Brand Runtime]] — active — React/Vite, pending deploy
- [[InsuranceHUB]] — active — Pacific Cross cinematic brutalist app

## People
- [[Mark Tantongco]] — founder, powerUP

## Decisions
- [[2026-06 Firebase to Supabase]] — active — reason: real-time sync cost

## Concepts
- [[Grace-First Reckoning]] — active — 5-beat content framework

## Orphans (needs linking)
- none currently
```

Claude regenerates this by walking frontmatter across `wiki/`, not by re-reading full page bodies — that's the trick that keeps regeneration cheap even as the vault grows.

---

## 6. Slash Commands (`.claude/commands/`)

Claude Code loads any `.md` file in `.claude/commands/` as a `/command`. Three cover the full lifecycle:

**`.claude/commands/ingest.md`**
```markdown
Process every file in raw/inbox/ per the Ingest job in CLAUDE.md.
Work one file at a time. After each file, state: file processed, pages created,
pages updated, links added. Do not summarize the whole batch until finished.
```

**`.claude/commands/ask.md`**
```markdown
Answer this question using only 00-INDEX.md and the wiki pages it points to.
Question: $ARGUMENTS
Cite the wiki pages you used. If the index doesn't cover it, say so — don't guess.
```

**`.claude/commands/lint.md`**
```markdown
Audit wiki/ for: orphan pages (zero backlinks), stub pages older than 14 days,
broken wikilinks (link target has no file), and any [!contradiction] callouts
still unresolved. Report as a checklist. Don't fix anything automatically —
list the issues and wait for confirmation.
```

Usage: `claude` → `/ingest`, `/ask what stack are we using for powerUP`, `/lint`.

---

## 7. Change Detection (`.claude/manifest.json`) — Avoid Re-Scanning Everything

Without this, Claude re-reads `raw/inbox/` in full every time you say "process my notes" — wasteful once the folder has history. A manifest tracks what's already been seen.

```bash
#!/usr/bin/env bash
# .claude/scripts/diff-inbox.sh
# Prints only files modified since the last recorded ingest. Run before /ingest.

MANIFEST=".claude/manifest.json"
[ -f "$MANIFEST" ] || echo '{}' > "$MANIFEST"

for f in raw/inbox/*.md; do
  [ -e "$f" ] || continue
  mtime=$(stat -f %m "$f" 2>/dev/null || stat -c %Y "$f")
  recorded=$(python3 -c "import json,sys; d=json.load(open('$MANIFEST')); print(d.get('$f',0))")
  if [ "$mtime" -gt "$recorded" ]; then
    echo "$f"
  fi
done
```

After a successful `/ingest`, have Claude update the manifest for each file it processed:
```bash
python3 -c "
import json, os, time
m = json.load(open('.claude/manifest.json'))
m['raw/inbox/2026-07-07-standup.md'] = time.time()
json.dump(m, open('.claude/manifest.json', 'w'), indent=2)
"
```

⚠️ Breaks if: you edit an already-processed raw file after the fact (raw is meant to be immutable — don't do this; drop a correcting note instead).

---

## 8. Why the Token Savings Are Real

The reported cost drop (users report cuts up to ~90%) doesn't come from magic — it comes from **retrieval instead of context-dumping**:

| Without this system | With this system |
|---|---|
| Paste/re-explain project context every session | Claude reads `CLAUDE.md` (schema) + `00-INDEX.md` (map) — a few hundred to ~1.5k tokens |
| Claude re-derives past decisions from scratch | Claude reads only the 2–5 wiki pages the index points to |
| Full vault scanned per question as it grows | Vault size stops mattering — index stays flat, only relevant pages load |

This holds up to roughly 100–150 wiki pages with plain markdown + keyword search. Past that, the index itself gets expensive to hold in full (every filename costs tokens) — at that scale, pair this with a vector store as a cold-archive layer and keep Obsidian for active working knowledge only.

---

## 9. Weekly Maintenance (Non-Negotiable)

Run `/lint` every 1–2 weeks. Systems like this die from silent drift, not from a single big failure:

- Orphan pages (no backlinks) — half-integrated knowledge, worse than not having it
- Stale stubs — created as a link target, never filled in
- Unresolved contradictions — flagged but never reconciled
- Broken wikilinks — typo'd or the target got renamed

---

## 10. Credit

This raw → wiki → CLAUDE.md pattern — plain markdown over vector databases, LLM as wiki maintainer rather than just a query interface — traces to Andrej Karpathy, who described using an LLM to auto-maintain a personal markdown knowledge base rather than reaching for a full RAG pipeline. Everything above is one concrete implementation of that idea, adapted for Claude Code + Obsidian with an added `output/` layer for finished deliverables.

---

## Quick-Start Checklist

- [ ] Install Obsidian, create one vault per domain
- [ ] Create `raw/inbox/`, `raw/_processed/`, `wiki/`, `output/`, `.claude/commands/`
- [ ] Write `CLAUDE.md` using the schema above (spend real time here — vague schema = vague wiki)
- [ ] Create empty `00-INDEX.md`
- [ ] Add `/ingest`, `/ask`, `/lint` commands
- [ ] Drop your first 3–5 notes into `raw/inbox/`, run `/ingest`
- [ ] Run `/lint` after two weeks, every two weeks after that
