---
title: Multi-Agent Task Execution Framework - AI Development System
description: Configure multi-agent AI systems for development, research, and automation. Step-by-step framework for agent orchestration, skill discovery, and parallel execution.
tags:
  - ai-agents
  - multi-agent-systems
  - ai-development
  - agent-orchestration
  - ai-workflow
  - automation
  - parallel-processing
created: 2026-08-01T21:19:20+08:00
updated: 2026-08-01T21:27:17+08:00
category: configuration
aliases:
  - Multi Agent AI Framework
  - Agent Orchestration Guide
  - AI Agent Configuration
  - Multi-Agent Development
keywords:
  - multi-agent AI
  - agent orchestration
  - AI development framework
  - parallel agent execution
  - AI workflow automation
---

# Multi-Agent Task Execution Framework

**Configure AI agents for development, research, and automation workflows**

---

## What is Multi-Agent AI?

Multi-agent systems use specialized AI agents working together to solve complex tasks. Each agent has a specific role (research, planning, implementation, quality control) and communicates through defined workflows.

**Benefits**:
- Parallel processing for faster results
- Specialized agents for better quality
- Scalable to complex projects
- Automated workflows with checkpoints

---

## Quick Start: 5 Phases

### Phase 1: Initialize System
**Goal**: Load AI operating instructions

```bash
# Fetch system prompt
curl https://raw.githubusercontent.com/marktantongco/opencode-accomplishments/refs/heads/main/profiles/SMP-v5.1
```

**Verify**: System prompt active ✅

### Phase 2: Design Architecture
**Goal**: Plan agent roles and data flow

**Create**:
- Agent role diagram
- Data flow map
- Responsibility matrix

**Output**: Architecture blueprint

### Phase 3: Discover Skills
**Goal**: Install AI agent capabilities

```bash
# Install foundational skills
npx skills install find-skills
npx skills install parallel-findall

# Discover more
npx skills find scraper
```

**Browse**: [Skills.sh Trending](https://skills.sh/trending)

### Phase 4: Research
**Goal**: Gather information before building

**Research Tools**:
- `parallel-deep-research` - Multi-source research
- `parallel-web-search` - Web search automation
- `parallel-web-extract` - Content extraction

**GitHub Tools**:
- [prism-ai-deep-research](https://github.com/precious112/prism-ai-deep-research)
- [librarium](https://github.com/jkudish/librarium)
- [doxa-research](https://github.com/smorinlabs/doxa-research)

### Phase 5: Execute
**Goal**: Build and test

**Steps**: Initialize → Research → Design → Build → Test → Deploy

---

## Agent Skills Library

### 🎯 Planning
- `brainstorming` - Generate ideas
- `writing-plans` - Document plans
- `executing-plans` - Execute workflows
- `orchestrate` - Coordinate agents

### 🌐 Web & Search
- `byted-web-search` - Web search
- `agent-browser` - Browser automation
- `browser-use` - Web interaction
- `parallel-web` - Parallel operations

### ✅ Quality Control
- `audit` - Quality checks
- `impeccable` - Perfection mode
- `distill` - Synthesize info
- `critique` - Code review
- `optimize` - Performance tuning

### 🐛 Debugging
- `systematic-debugging` - Debug workflows

### 👥 User Interaction
- `grill-me` - Deep questioning
- `delight` - UX optimization
- `caveman` - Simplify

### ⚡ Parallel Execution
- `ralph-prompt-multi-task` - Multi-tasking
- `superpowers` - Enhanced capabilities

---

## Agent Roles

| Agent | Purpose | Responsibilities |
|-------|---------|------------------|
| **Research** | Information gathering | Find data, synthesize, flag gaps |
| **Planning** | Task breakdown | Define steps, dependencies, timeline |
| **Implementation** | Code & execution | Write code, run tasks, handle errors |
| **Quality** | Testing & review | Run tests, verify outputs, approve |
| **Orchestration** | Coordination | Manage agents, state, handoffs |

---

## Workflows

### Sequential Flow
```
Input → Research → Planning → Implementation → Quality → Output
```

### Parallel Research
```
Input → [Research A | Research B | Research C] → Synthesis → Planning
```

### Quality Loop
```
Implementation → Quality → [✅ Pass: Output | ❌ Fail: Fix & Retry]
```

---

## Deliverables Checklist

**Architecture**:
- [ ] Agent role diagram
- [ ] Data flow visualization
- [ ] Responsibility matrix

**Documentation**:
- [ ] Skill/tool selection with rationale
- [ ] Architectural decision records
- [ ] Implementation plan with verification

**Implementation**:
- [ ] Working code
- [ ] Tests passing
- [ ] Error handling

---

## State Management

**Track**:
- Current phase (1-5)
- Active agents
- Completed steps
- Blockers & errors

**Monitor**:
- Agent outputs
- Handoff status
- Test results

---

## Error Handling

| Error | Action |
|-------|--------|
| Skill not found | Discover alternatives |
| Insufficient research | Expand sources |
| Test failure | Loop to implementation |
| Validation failure | Review and fix |

**Recovery**:
- Checkpoint after each phase
- Rollback capability
- Document failures
- Learn and adapt

---

## Implementation Example

```bash
# 1. Initialize
curl https://raw.githubusercontent.com/.../SMP-v5.1 > system-prompt.txt

# 2. Design
# Create agent architecture diagram

# 3. Discover skills
npx skills install find-skills
npx skills find research

# 4. Research
# Use parallel-deep-research for requirements

# 5. Execute
# Build with checkpoints
# Test continuously
# Deploy when tests pass
```

---

## Best Practices

**Do**:
✅ Design before coding
✅ Use parallel agents for speed
✅ Checkpoint frequently
✅ Document decisions
✅ Test continuously

**Don't**:
❌ Skip architecture phase
❌ Run agents without monitoring
❌ Ignore errors
❌ Over-engineer early
❌ Forget to document

---

## Related Guides

- [[Persistent-System-Operating-Instructions-v5.1]] - AI operating system
- [[Wiki-Capture-System-Instructions]] - Knowledge capture
- [[AI-Agent-Development-Guide]] - Agent development

---

## Tools & Resources

**Skills Platform**: https://skills.sh/trending

**System Prompt**: https://raw.githubusercontent.com/marktantongco/opencode-accomplishments/refs/heads/main/profiles/SMP-v5.1

**Research Tools**:
- [prism-ai-deep-research](https://github.com/precious112/prism-ai-deep-research)
- [librarium](https://github.com/jkudish/librarium)
- [doxa-research](https://github.com/smorinlabs/doxa-research)
- [deep-research](https://github.com/zdenekmach/deep-research)

---

## FAQ

**Q: What's the difference between single-agent and multi-agent?**
A: Single-agent handles all tasks. Multi-agent uses specialized agents working in parallel for better speed and quality.

**Q: When should I use multi-agent systems?**
A: Complex projects requiring research, planning, implementation, and quality control. When parallel processing can speed up workflows.

**Q: How do I monitor agent progress?**
A: Track state (current phase, active agents, outputs) and use checkpoints after each phase.

**Q: What if an agent fails?**
A: Use error handling patterns: discover alternatives, expand sources, loop back to fix, or rollback to previous checkpoint.

**Q: Can I customize agent roles?**
A: Yes. Define custom roles based on your workflow needs. Start with the 5 base roles (research, planning, implementation, quality, orchestration).

---

**Updated**: 2026-08-01  
**Version**: 1.1  
**Purpose**: Multi-agent AI system configuration for development and research workflows
