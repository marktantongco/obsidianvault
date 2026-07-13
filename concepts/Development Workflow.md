---
tags: [workflow, development, process]
type: concept
created: 2026-07-09
updated: 2026-07-09
lifecycle: verified
tier: core
---

# Development Workflow

## Multi-Agent Pipeline
```
Research → Plan → Implement → Review → Verify
   ↓         ↓         ↓          ↓         ↓
 Hermes   Hermes   OpenCode   Claude    Both
```

## Workflow Steps

### 1. Research
- Use Hermes to gather context
- Query Obsidian wiki for existing knowledge
- Check agentic-stack memory

### 2. Plan
- Hermes breaks down tasks
- Identify which agents handle what
- Create task list

### 3. Implement
- OpenCode executes code changes
- MiMo Code assists with Xiaomi-specific tasks
- Codex generates code snippets

### 4. Review
- Claude Code audits the implementation
- Checks for security issues
- Validates against best practices

### 5. Verify
- Run tests
- Check documentation
- Update wiki with findings

## Tools
- [[OpenCode]] for code execution
- [[Claude Code]] for review
- [[Hermes Agent]] for orchestration
- [[Obsidian Wiki]] for knowledge persistence

## Best Practices
1. Start with research and planning
2. Implement in small increments
3. Review before merging
4. Document decisions in the wiki
5. Use wiki-capture to save findings

## Related
- [[AI Agents]]
- [[MCP Servers]]
- [[Obsidian Wiki]]
