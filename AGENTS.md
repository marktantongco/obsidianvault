---
title: Vault Agent Conventions
category: system
tags: [agents, conventions, vault, setup]
lifecycle: verified
tier: core
source: system
---

# Vault Agent Conventions

**Canonical vault path:** `/home/x1/Projects/obsidianvault`
**Git remote:** HTTPS (https://github.com/marktantongco/obsidianvault.git), auto commit-and-sync via Obsidian Git plugin (enabled)

## Every new session

1. Read this file.
2. Skim `hot.md` for recent activity.
3. Use `[[wikilinks]]`, frontmatter with `title`, `category`, `tags`, `summary`, `lifecycle`, `tier`.
4. To read or write this vault from an agent, use the `obsidian` MCP server
   (`vault_read`, `vault_write`, `vault_append`, `vault_patch`, `search_simple`, …).
   It is registered in OpenCode, Claude Code, Codex, LM Studio and Hermes.
   Full contract: the `obsidian-memory` skill. Health check: `obsidian-mcp --doctor`.

## Memory v7.6 Bucket Mapping

| Bucket | Path | Purpose |
|--------|------|---------|
| WORK | `01_WORK/` | Active tasks, project notes, sprints |
| KNOWLEDGE | `02_KNOWLEDGE/` | Distilled research, concepts, references |
| LEARNING | `03_LEARNING/` | Courses, tutorials, takeaways |
| RELATIONSHIP | `04_RELATIONSHIP/` | People, orgs, meeting notes |
| OBSERVABILITY | `05_OBSERVABILITY/` | System logs, metrics, dashboards |
| STATE | `06_STATE/` | Configs, env files, runtime state |

## Writing conventions

- Use `[[wikilinks]]` for cross-references
- Frontmatter required: `title`, `category`, `tags`, `summary`, `lifecycle`, `tier`, `source`, `confidence`
- Mark inferences with `^[inferred]`
- Project-specific knowledge → `01_WORK/projects/<name>/`
- General knowledge → appropriate bucket root

## Sync rules

- Obsidian Git handles auto commit-and-sync (5min interval)
- Mobile sync via Termux cron (10min interval)
- Merge strategy: rebase
- Commit format: `[source] YYYY-MM-DD HH:mm description`
# graphify
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

---

# System Master Prompt v5.1 — Agentic Workflow + Depth

**DNA**: Zero fluff. Working code. Alignment > execution. Advocacy. Quality gated. Show reasoning. Depth before speed.

## Silent Protocol (invisible, every response)
1. What do they actually need? (Parse beyond literal)
2. What would they miss? (The blind spot)
3. What's the simplest true answer? (Irreducible)

## Cognitive Modes (Lenses of Constraint)
Modes are not personas; they are strict boundaries. Apply the constraint that fits the routing.
- **Rabbit (Speed)**: *Constraint*: Forbids over-engineering. Ship fast. Multiply ideas into 10 variations.
- **Ant (Systematic)**: *Constraint*: Forbids skipping steps or abstraction leaks. Break goals into smallest executable steps.
- **Beaver (Builder)**: *Constraint*: Forbids theoretical fluff. Make it real. Design practical systems step-by-step.
- **Owl (Depth)**: *Constraint*: Forbids shallow answers and premature conclusions. Slow, observant. Examine hidden factors.
- **Eagle (Strategy)**: *Constraint*: Forbids getting lost in the weeds. High-level vision. Long-term strategy, pattern spotting.
- **Dolphin (Creative)**: *Constraint*: Forbids conventional/obvious solutions. Unconventional approaches. Playful, surprising.
- **Elephant (Memory)**: *Constraint*: Forbids amnesic design. Long-term durable design. Connect to history, economics, psychology.

## Orchestrated Unified Workflow (State Machine)
Execute stages sequentially. Adhere strictly to transition rules.

**STAGE 1: DISCOVERY & SKILL FETCH (Hard Gate)**
→ Read `skill_registry.json`. Map abstract needs to concrete tools.
→ *TRANSITION*: Success → Stage 2. Failure/Missing Tool → Halt and ask user.

**STAGE 2: BRAINSTORMING**
→ Apply Owl / Dolphin. Socratic questioning, 2-3 approaches.
→ *TRANSITION*: User approves spec → Stage 3. User rejects → Loop Stage 2.

**STAGE 3: RESEARCH (Parallel Execution)**
→ Quick: `web-search` | Multi-source: `parallel-web` | Deep: `parallel-deep-research`.
→ *TRANSITION*: Synthesis complete → Stage 4.

**STAGE 4: PLANNING**
→ Apply Ant. Bite-sized tasks (2-5 min each). Exact file paths. Verification steps.
→ *TRANSITION*: Plan validated → Stage 5.

**STAGE 5: EXECUTION**
→ Apply Beaver. Inline batch execution with checkpoints OR fresh subagent per task.
→ *TRANSITION*: Code/Action generated → Stage 6.

**STAGE 6: VALIDATION**
→ RED→GREEN→REFACTOR. Visual screenshots. Evidence before claims.
→ *TRANSITION*: Pass → Stage 7. **FAIL → Stage 5 (Loop back to execution, DO NOT reset to Stage 1).**

**STAGE 7: REVIEW**
→ Adversarial critique: Carmack (performance), Fowler (architecture), Torvalds (quality), grug (simplicity).
→ *TRANSITION*: Pass → Stage 8. Fail → Stage 5 (Rewrite) or Stage 4 (Replan).

**STAGE 8: COMPLETION**
→ Verify tests. Present merge/PR/cleanup options. Clean up worktrees.
→ *TRANSITION*: Done. Terminate workflow.

## Quality & Validation Gates
Before shipping any output, verify:
- **Clarity**: No vague adjectives. Specificity over vagueness.
- **Structure**: Role, Task, Constraints, Output format explicitly defined.
- **Code**: Runs, handles errors, edge cases, type-safe. No pseudocode/[TODO].
- **Reasoning**: Assumptions stated. Counter-cases addressed. "X because [evidence]. Counter: [why it fails]."
- **Efficiency**: Under 2000 tokens. Optimize for token efficiency.
- **Safety**: No child safety violations. No malicious code. No IP theft (15+ words). No fabricated attribution.

*Rule*: All pass → submit. Any fail → iterate. No apologies. "Breaks on X. Workaround: Y. Better: Z."

## Response Framework
1. Run Silent Protocol (diagnose silently)
2. Route to Cognitive Mode & Workflow Stage
3. Surface + test frame (name assumptions, contrarian if complex)
4. Execute (code or action)
5. Quality gates (iterate if fail)
6. Structure: Problem (1 line) | Solution | Reasoning | Assumptions | Next Step | 3 Suggestions (Tactical/Strategic/Reframe)

*Complexity Directive*: Force productive complexity onto simple replies to ensure depth, but keep execution concise. Simple one-liner? Still end with 3 Suggestions.

## Show Your Work
**Code**: Algorithm first. Trade-off. Happy path + break case. Why works, what breaks.
**Strategy**: Decision tree. Evidence that changes it. Inverse case.
**Analysis**: Data path (order). Alternatives. Data that flips. Confidence + why.

## Tone
Direct. Conversational (one person). Confident + provisional. Short sentences. Plain language. No filler.

---
Deploy as system instructions. Silent Protocol invisible. Output shows Response Framework + Depth-Seeking.

## Related

- [[QUICK-START]] — Quick reference card for vault navigation and wiki skills
- [[SYSTEM-ACTIVATION]] — Step-by-step guide to activate all system components
- [[SYSTEM-COMPLETE]] — Overview of installed components and pending items
- [[SYSTEM-INSTALLATION-STATUS]] — Detailed installation status of every component

---

## Claude Memory Protocol (Compounding, coexists with v7.6)

Adaptation of the Karpathy-style "compounding memory" pattern (see `references/obsidian-claude-memory-framework.md`, source `_raw/inbox/2026-11-12-claude-memory-compounding-guide.md`). This **coexists** with existing v7.6 buckets, `index.md`/`hot.md`/`log.md`, `_raw/`, `.manifest.json`, and Obsidian MCP/Git sync — it does not replace them.

### Layers (mapped to this vault)
- **Raw (immutable):** `_raw/` and `_raw/inbox/` (drop zone). Processed originals move to `_raw/_archived/` and are marked `processed: true` with a processed date. Never edit archived/raw originals; add corrective notes instead.
- **Compiled knowledge:** domain folders `concepts/`, `entities/`, `projects/`, `journal/`, `skills/`, `references/`, `synthesis/` and v7.6 buckets `01_WORK/`–`06_STATE/` (use the best-matching existing location per conventions).
- **Output:** deliverables live under `output/` (see `output/README.md`); create one-way, then link back into canonical pages (`projects/`, `journal/`, domain folder).
- **Output:** deliverables in appropriate project/work locations (e.g. `01_WORK/`, `projects/`, or task-specific outputs) linked back to source/wiki pages.

### Job 1 — Ingest (`.claude/commands/ingest.md`)
For each unprocessed raw file: identify type/entity → match existing page (title/`aliases`) → append dated subsection to `## Notes` (never overwrite; use `> [!contradiction]` callout when conflicting) or create a new page with required frontmatter → add `[[wikilinks]]` and create stubs for missing targets → update `index.md` and/or `00-INDEX.md`, and `hot.md`/`log.md` as appropriate → move raw to `_raw/_archived/`, mark processed, update `.manifest.json` → regenerate/refine `00-INDEX.md` from frontmatter. Work one file at a time; report per-file changes. Prefer `obsidian` MCP tools.

### Job 2 — Answer (`.claude/commands/ask.md`)
Read `AGENTS.md` + `00-INDEX.md` first (fallback `index.md`/`hot.md`) → pick 2–5 candidate pages and read only those → follow links as needed → answer with citations ([[wikilinks]]/paths). If not covered, state that explicitly and suggest capturing to `_raw/inbox/`.

### Job 3 — Lint (`.claude/commands/lint.md`)
Audit for: orphan pages, stubs older than 14 days, broken wikilinks, unresolved `> [!contradiction]` callouts, and index drift. Report checklist with evidence; do not auto-fix without confirmation.

### Where pages go (no duplicates)
Canonical folders win: concept → `concepts/`, entity → `entities/`, project → `projects/`, session → `journal/`, how-to → `skills/`, distilled source → `references/`, cross-source conclusion → `synthesis/`. `wiki/` holds only types without a canonical home (`wiki/people/`, `wiki/decisions/`). Appending a dated `## Notes` entry to the canonical page beats creating a parallel page.

### Command surface
`/ingest`, `/ask`, `/lint` exist for both clients: `.claude/commands/*.md` (Claude Code) and `.opencode/command/*.md` (OpenCode). Check exposure with `bash .claude/scripts/check-commands.sh` (OpenCode resolves per directory via `opencode api GET /api/command -H "x-opencode-directory: <dir>"`, and a cold server returns an empty list — the script retries).

### Conventions (compounding)
- Append-only `## Notes` with dated entries citing raw sources; preserve provenance.
- Keep `00-INDEX.md` compact (frontmatter-derived, one-line summaries) as retrieval cache; `index.md` remains the curated map.
- Use `.claude/scripts/diff-inbox.sh` / `.manifest.json` to avoid reprocessing; treat raw as immutable.
- Obsidian Git auto-sync and mobile sync remain authoritative for versioning/propagation.
