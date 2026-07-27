---
title: Wikilinks — Cross-Reference Convention
category: concepts
tags: [concepts, conventions, linking]
summary: Obsidian wikilink syntax for cross-referencing pages in the vault.
lifecycle: active
tier: peripheral
created: 2026-07-23T00:00:00Z
updated: 2026-07-23T00:00:00Z
---

# Wikilinks — Cross-Reference Convention

Wikilinks (`[[wikilinks]]`) are the standard cross-reference mechanism in this vault. Every content page should use them to connect related knowledge.

## Syntax

- **Basic link:** `[[page name]]`
- **With display text:** `[[page name|Display Text]]`
- **With path:** `[[category/page-name]]`
- **With path and display:** `[[category/page-name|Display Text]]`

## Rules

- Always prefer wikilinks over bare URLs or plain-text mentions of other vault pages
- Use display text when the link target name is not readable as-is (e.g., `[[entities/DeepSeek|DeepSeek]]`)
- Frontmatter `tags:` serve a different purpose — they're for classification, not navigation

## Related

- [[concepts/Obsidian Wiki|Obsidian Wiki]] — The vault's wiki knowledge management system
