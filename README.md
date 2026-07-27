# 🧠 Second Brain — Obsidian Wiki Vault

[![GitHub Pages](https://img.shields.io/github/deployments/marktantongco/obsidianvault/github-pages?label=GitHub%20Pages&logo=github&style=flat-square)](https://marktantongco.github.io/obsidianvault/)
[![License](https://img.shields.io/github/license/marktantongco/obsidianvault?style=flat-square)](LICENSE)
[![Last Updated](https://img.shields.io/github/last-commit/marktantongco/obsidianvault/master?label=Last%20Updated&style=flat-square)](https://github.com/marktantongco/obsidianvault/commits/master)
[![Pages](https://img.shields.io/badge/Pages-122+-blue?style=flat-square)](#-vault-structure)
[![Skills](https://img.shields.io/badge/Skills-55+-purple?style=flat-square)](#-skills-inventory)
[![AI Agents](https://img.shields.io/badge/AI%20Agents-9-orange?style=flat-square)](#-agent-ecosystem)
[![Structure](https://img.shields.io/badge/Architecture-6%20Buckets-success?style=flat-square)](#-the-second-brain-architecture)

> An AI-compiled Obsidian knowledge ecosystem — 122+ wiki pages, 55+ reusable agent skills, 9 AI agents, 6-bucket Memory v7.6 architecture. Built by [OpenCode](https://github.com/marktantongco/opencode), fed by Claude, Codex, Hermes, Grok, and more.

---

## 📋 Overview

This vault is a **Karpathy-style LLM Wiki** — a "Second Brain" compiled by multiple AI coding agents working in concert. Every page, link, and tag is the product of human-AI collaboration: raw knowledge captured from sessions, distilled into interconnected wiki pages, and surfaced through a structured schema.

### Three-Layer Architecture

| Layer | Location | Purpose |
|-------|----------|---------|
| **Raw** | `_raw/` | Immutable source captures — session logs, exports, downloads |
| **Wiki** | All `.md` pages | Distilled, interconnected knowledge with frontmatter & wikilinks |
| **Schema** | `AGENTS.md`, frontmatter, tag taxonomy | Conventions, constraints, and structure rules |

### Memory v7.6 Bucket Architecture

| Bucket | Path | Purpose |
|--------|------|---------|
| WORK | `01_WORK/` | Active tasks, project notes, sprints |
| KNOWLEDGE | `02_KNOWLEDGE/` | Distilled research, concepts, references |
| LEARNING | `03_LEARNING/` | Courses, tutorials, takeaways |
| RELATIONSHIP | `04_RELATIONSHIP/` | People, orgs, meeting notes |
| OBSERVABILITY | `05_OBSERVABILITY/` | System logs, metrics, dashboards |
| STATE | `06_STATE/` | Configs, env files, runtime state |

---

## 🚀 Quick Start

```bash
# Clone the vault
git clone https://github.com/marktantongco/obsidianvault.git

# Open in Obsidian
obsidian obsidianvault/

# Or serve the SPA reader directly
python3 -m http.server 8080
# → http://localhost:8080/index.html
```

### Essential Hotkeys

| Action | Hotkey |
|--------|--------|
| Quick Switcher | `Ctrl+O` |
| Command Palette | `Ctrl+Shift+P` |
| Daily Note | `Ctrl+D` |
| Graph View | `Ctrl+Shift+G` |
| Search | `Ctrl+F` |

---

## 📁 Vault Structure

```
obsidianvault/
├── 01_WORK/              # Active tasks, project notes
├── 02_KNOWLEDGE/          # Distilled research, concepts
├── 03_LEARNING/           # Courses, tutorials
├── 04_RELATIONSHIP/       # People, orgs, contacts
├── 05_OBSERVABILITY/      # Logs, metrics, dashboards
├── 06_STATE/              # Configs, env files
├── concepts/              # 22 AI/agent concept pages
├── entities/              # 11 tool & service references
├── skills/                # 7 agent skill documents
├── projects/              # 4 active project pages
├── journal/               # 7 session logs
├── references/            # 4 external source research
├── synthesis/             # 3 cross-cutting analyses
├── tags/                  # Tag index pages
├── dashboards/            # Live status dashboards
├── _raw/                  # Raw captures (staging area)
├── _skills/               # 5 installed skill definitions
├── templates/             # Note templates
├── .github/               # GitHub Actions + scripts
├── .obsidian/             # Obsidian config + 9 plugins
│
├── index.html             # Interactive landing page (SPA)
├── reader.html            # Full wiki reader app
├── index.md               # Wiki index (auto-generated)
├── hot.md                 # Recent activity cache
├── log.md                 # Query log
├── sitemap.xml            # SEO sitemap
├── AGENTS.md              # Vault agent conventions
│
├── install-plugins.sh     # Plugin installation script
├── attio.js               # Analytics integration
├── cache.json             # Source cache manifest
└── changelog.json         # Change tracking
```

---

## 🏛️ The Second Brain Architecture

### Layer 1 — Raw Sources (`_raw/`)

Immutable captures from AI coding sessions, web research, and document uploads. Nothing is edited in place — raw sources are preserved as a verifiable audit trail.

### Layer 2 — Wiki (All `.md` pages)

Every page is distilled knowledge with:
- **Frontmatter**: `title`, `category`, `tags`, `summary`, `lifecycle`, `tier`, `source`, `confidence`
- **Wikilinks**: `[[cross-references]]` between related concepts
- **Lifecycle states**: `seedling` → `growing` → `evergreen` → `verified`
- **Tier system**: `core` (foundational), `supporting` (contextual), `peripheral` (transient)

### Layer 3 — Schema (`AGENTS.md`)

Machine-readable conventions that every agent follows:
- **Memory v7.6 Bucket Mapping** — structured directory routing
- **System Master Prompt v5.1** — cognitive modes & workflow state machine
- **Tag Taxonomy** — controlled vocabulary for consistent tagging
- **Sync Rules** — commit format, merge strategy, frequency

### Sync Strategy

| Mechanism | Frequency | Scope |
|-----------|-----------|-------|
| Obsidian Git Plugin | Every 5 min | Desktop auto commit-and-sync |
| Termux Cron | Every 10 min | Mobile vault sync |
| GitHub Actions | Daily at 1 AM UTC | Index regeneration, hot.md rebuild |

---

## 🤖 Agent Ecosystem

Nine AI agents interact with this vault, contributing knowledge through their unique roles:

| Agent | Source | Role | Skills |
|-------|--------|------|--------|
| **OpenCode** | [marktantongco/opencode](https://github.com/marktantongco/opencode) | Terminal AI TUI agent | 37 |
| **Claude Code** | Anthropic | Coding + review agent | 37 |
| **OpenAI Codex** | OpenAI | Lightweight coding agent | — |
| **Grok** | xAI | AI coding assistant | — |
| **MiMo Code** | Xiaomi | Mobile coding assistant | — |
| **Hermes Agent** | Nous Research | Self-improving orchestrator | 36 |
| **JCode** | jcode.io | Daemon + proxy + web | — |
| **Freebuff** | — | Unified proxy manager | — |
| **Owl-Agent** | — | HTTP scraping engine v4.2 | — |

All agents share a unified knowledge pool through the vault — what one learns, all can reference.

---

## 🛠️ Skills Inventory

### Wiki & Obsidian (26)

| Skill | Category | Purpose |
|-------|----------|---------|
| `llm-wiki` | Foundation | Karpathy-style LLM wiki pattern |
| `wiki-setup` | Foundation | Initialize a new vault |
| `wiki-switch` | Foundation | Switch between vault profiles |
| `wiki-ingest` | Ingest | Ingest documents, URLs, text |
| `wiki-capture` | Ingest | Capture current conversation as note |
| `wiki-update` | Ingest | Sync project knowledge into wiki |
| `wiki-history-ingest` | Ingest | Bulk ingest agent history |
| `wiki-agent` | Ingest | Targeted topic search across agent history |
| `wiki-stage-commit` | Ingest | Review & promote staged pages |
| `wiki-query` | Query | Answer questions from wiki knowledge |
| `wiki-context-pack` | Query | Produce token-bounded context slices |
| `wiki-narrate` | Query | Generate briefings & lectures |
| `wiki-research` | Query | Autonomous multi-round web research |
| `wiki-lint` | Maintenance | Audit wiki health & fix issues |
| `wiki-dedup` | Maintenance | Merge duplicate pages |
| `wiki-synthesize` | Maintenance | Discover cross-cutting connections |
| `cross-linker` | Maintenance | Auto-add missing wikilinks |
| `tag-taxonomy` | Maintenance | Enforce controlled vocabulary |
| `graph-colorize` | Maintenance | Color-code Obsidian graph view |
| `wiki-status` | Reporting | Show wiki state & source delta |
| `wiki-digest` | Reporting | Periodic knowledge digest |
| `wiki-export` | Reporting | Export to JSON / GraphML / Neo4j |
| `wiki-import` | Reporting | Import from exported bundles |
| `wiki-dashboard` | Ops | Dynamic vault dashboards |
| `wiki-rebuild` | Ops | Archive & rebuild from scratch |
| `daily-update` | Ops | Daily maintenance cycle |

### History Ingestion (6)

| Skill | Source Agent |
|-------|-------------|
| `claude-history-ingest` | Claude Code |
| `codex-history-ingest` | OpenAI Codex |
| `copilot-history-ingest` | GitHub Copilot |
| `hermes-history-ingest` | Hermes Agent |
| `openclaw-history-ingest` | OpenClaw |
| `pi-history-ingest` | Pi Agent |

### Animation & Motion (12)

| Skill | Purpose |
|-------|---------|
| `ui-ux-pro-max` | 84 styles, 192 palettes, 74 font pairings |
| `framer-motion-animator` | Micro-interactions, gestures |
| `gsap-core` | Core GSAP animations |
| `gsap-timeline` | Timeline sequencing |
| `gsap-scrolltrigger` | Scroll-driven animations |
| `gsap-plugins` | GSAP utility plugins |
| `gsap-react` | React + GSAP integration |
| `gsap-frameworks` | Framework-specific patterns |
| `gsap-performance` | GSAP optimization |
| `gsap-utils` | GSAP utility helpers |
| `threejs-animation` | 3D scenes, GLTF |
| `remotion-best-practices` | Programmatic video |

### Obsidian Sub-Skills (5)

| Skill | Purpose |
|-------|---------|
| `obsidian-bases` | Create database-like .base files |
| `obsidian-cli` | Vault operations from CLI |
| `obsidian-markdown` | Obsidian-flavored markdown |
| `json-canvas` | Canvas files with nodes & edges |
| `defuddle` | Extract clean markdown from web pages |

### Utility (7)

| Skill | Purpose |
|-------|---------|
| `skill-creator` | Create & optimize agent skills |
| `impl-validator` | Validate implementations |
| `memory-bridge` | Cross-tool knowledge comparison |
| `vault-skill-factory` | Package wiki pages as portable skills |
| `apify-ultimate-scraper` | Web scraping |
| `obsidian-layout-adjustment` | CSS snippet workflow |
| `customize-opencode` | Configure opencode itself |

---

## 📜 Agent Conventions

All agents follow the rules defined in [`AGENTS.md`](AGENTS.md):

### Memory v7.6 Bucket Mapping

Each bucket maps to a numbered directory. Agent output is routed to the correct bucket based on content type.

### Frontmatter Requirements

Every page must include:
- `title`, `category`, `tags`, `summary`
- `lifecycle` (seedling / growing / evergreen / verified)
- `tier` (core / supporting / peripheral)
- `source` (which agent or process created it)
- `confidence` (how reliable the information is)

### Writing Conventions

- `[[Wikilinks]]` for all cross-references
- `^[inferred]` for speculative content
- Project-specific knowledge → `01_WORK/projects/<name>/`
- General knowledge → appropriate bucket root

### Sync Rules

```text
Commit format: [source] YYYY-MM-DD HH:mm description
Merge strategy: rebase
Desktop sync: Obsidian Git (5 min interval)
Mobile sync: Termux cron (10 min interval)
```

---

## 🧠 System Prompt v5.1 — Cognitive Modes

The vault runs on a unified system prompt that defines how agents think and work:

### Cognitive Modes

| Mode | Constraint |
|------|-----------|
| 🐇 **Rabbit (Speed)** | Forbids over-engineering. Ship fast. |
| 🐜 **Ant (Systematic)** | Forbids skipping steps. Break into smallest units. |
| 🦫 **Beaver (Builder)** | Forbids theoretical fluff. Make it real. |
| 🦉 **Owl (Depth)** | Forbids shallow answers. Examine hidden factors. |
| 🦅 **Eagle (Strategy)** | Forbids getting lost in weeds. Long-term vision. |
| 🐬 **Dolphin (Creative)** | Forbids conventional solutions. Unconventional approaches. |
| 🐘 **Elephant (Memory)** | Forbids amnesic design. Connect to history. |

### 8-Stage Orchestrated Workflow

```
Discovery → Brainstorming → Research → Planning →
Execution → Validation → Review → Completion
```

Each stage has strict transition rules. Validation failures loop back to Execution (not Discovery), ensuring rapid iteration without wasted context.

---

## 🧩 21st.dev Component

A PinList component is published on [21st.dev](https://21st.dev):

```bash
# Via @marktantongco
npx @21st-dev/registry add @marktantongco/pinlist

# Via @imarkytanky
npx @21st-dev/registry add @imarkytanky/pinlist
```

[View on 21st.dev](https://21st.dev/@marktantongco/components/pinlist)

---

## 🌐 Deployment

### GitHub Pages

Auto-deployed via GitHub Actions every daily update at **1:00 AM UTC**. The SPA reader app at `index.html` is served directly.

### Vercel

Deployed at [obsidianvault-ochre.vercel.app](https://obsidianvault-ochre.vercel.app/). The static site is fully self-contained — no build step required.

### Cloudflare

Edge caching configured via `_headers`:

```
/*.md           → Cache-Control: public, max-age=600
/index.html     → Cache-Control: public, max-age=300
```

---

## ⚙️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Knowledge Base** | [Obsidian](https://obsidian.md/) with 9 community plugins |
| **Plugins** | Git, Dataview, Templater, Kanban, Tasks, Calendar, Excalidraw, Local REST API |
| **Automation** | Python (daily update scripts), Bash (install/maintenance) |
| **SPA Reader** | Vanilla JS, [Marked.js](https://marked.js.org/), [D3.js](https://d3js.org/), [Fuse.js](https://fusejs.io/) |
| **Animation** | GSAP (8 sub-skills), Framer Motion, Three.js, Remotion |
| **CI/CD** | GitHub Actions (daily sync + deploy) |
| **Edge** | Cloudflare (static caching via `_headers`) |
| **Styling** | [Pico CSS](https://picocss.com/), [Highlight.js](https://highlightjs.org/) |
| **Analytics** | Attio (via `attio.js`) |

---

## 🤝 Contributing

This vault is primarily a personal knowledge ecosystem, but you are welcome to:

- **Fork it** and adapt the structure for your own Second Brain
- **Use the skills** — all 26 wiki skills are available as reusable agent instructions
- **Open a PR** for improvements to the vault structure, documentation, or automation

### Wiki Skills (Run from Any Project)

```bash
# Query the wiki
wiki-query @personal What do I know about X?

# Capture a finding
wiki-capture --quick "Important discovery"

# Update wiki from current project
wiki-update

# Research a topic
wiki-research "Topic"
```

---

## 📄 License

[MIT](LICENSE) © 2026 [Mark Tan Tongco](https://github.com/marktantongco)

---

<p align="center">
  <sub>Built with ❤️ by OpenCode • Fed by 9 AI Agents • Distilled into Knowledge</sub>
</p>
