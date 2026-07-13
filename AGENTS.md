# Vault Agent Conventions

**Canonical vault path:** `/home/x1/obsidianvault`
**Git remote:** SSH, auto commit-and-sync via Obsidian Git plugin

## Every new session

1. Read this file.
2. Skim `hot.md` for recent activity.
3. Use `[[wikilinks]]`, frontmatter with `title`, `category`, `tags`, `summary`, `lifecycle`, `tier`.

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
