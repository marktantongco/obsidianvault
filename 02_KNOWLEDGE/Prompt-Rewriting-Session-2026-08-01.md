---
title: Prompt Rewriting Session - AI System Instructions
tags:
  - ai
  - prompt-engineering
  - system
  - session
created: 2026-08-01T21:19:20+08:00
updated: 2026-08-01T21:19:20+08:00
category: synthesis
aliases:
  - AI Prompt Optimization Session
relationships:
  - target: "[[06_STATE/Persistent-System-Operating-Instructions-v5.1.md]]"
    type: related_to
  - target: "[[concepts/OpenCode.md]]"
    type: related_to
  - target: "[[concepts/AI Agents.md]]"
    type: related_to

---

# Prompt Rewriting Session - AI System Instructions

*Session Date: 2026-08-01*

## Overview

This session focused on optimizing three major AI system prompts for persistent system operating instructions. The goal was to transform conversational/explanatory prompts into actionable, executable system instructions.

---

## Prompts Rewritten

### 1. Multi-Agent Task Execution Framework

**Original Intent**: Instructions for configuring [[concepts/AI Agents|AI agents]] with system prompt adoption, multi-agent architecture, skill discovery, and research-first approach.

**Key Improvements**:
- Separated into numbered phases for clarity
- Made each phase actionable with clear objectives, actions, and deliverables
- Added explicit verification steps
- Structured skill categories for easier reference
- Emphasized documentation-first approach before implementation
- Added execution order with sequential steps and parallel opportunities
- Created deliverables checklist

**Result**: [[Multi-Agent-Task-Execution-Framework]]

---

### 2. Persistent System Operating Instructions v5.1

**Original**: [[06_STATE/Persistent-System-Operating-Instructions-v5.1|System Master Prompt]] (SMP) v5.1 - Agentic workflow with depth

**Key Improvements**:
- Reorganized into 8 numbered sections for easier reference
- Clarified state machine transition rules
- Made quality gates actionable (checklist format)
- Added explicit "when to use" guidance for cognitive modes
- Emphasized the "no restart" rule for validation failures
- Converted tone guidance into actionable rules
- Made response structure a template
- Removed meta-commentary
- Added execution notes section for operational clarity

**Core Principles**:
- Zero fluff
- Working code
- Alignment > execution
- Quality-gated
- Show reasoning
- Depth before speed

**Result**: [[Persistent-System-Operating-Instructions-v5.1]]

---

### 3. Wiki Capture System Instructions

**Original**: Wiki Capture skill with full and quick modes

**Key Improvements**:
- Separated Quick Mode from Full Mode with clear visual hierarchy
- Made gate logic explicit with boolean conditions
- Converted checklists to actionable verification steps
- Added explicit templates for each content type (synthesis, concept, source, session)
- Clarified QMD refresh as post-write operation with skip conditions
- Made provenance markers concrete with examples
- Added explicit threshold bias rules for KEEP/SKIP decisions
- Structured as executable instructions rather than explanatory text

**Two Modes**:
- **Quick mode** (`--quick`): <60s staging to `_raw/` directory
- **Full mode**: Complete wiki page with cross-links, index updates

**Result**: [[Wiki-Capture-System-Instructions]]

---

### 4. Obsidian Markdown System Instructions

**Original**: Obsidian Flavored Markdown skill documentation

**Key Improvements**:
- Converted workflow to executable protocol
- Made syntax examples into reusable templates
- Added execution notes for common gotchas
- Structured as quick-reference format
- Clarified decision rules (when to use what syntax)
- Separated references from instructions
- Added explicit rules for edge cases (block IDs, foldable callouts)
- Made property templates concrete and copy-pasteable

**Result**: [[Obsidian-Markdown-System-Instructions]]

---

## Rewriting Principles Applied

### 1. Actionable > Explanatory
- Converted "you should" → "execute this"
- Changed descriptive text → step-by-step protocols
- Made implicit rules explicit

### 2. Structured for Reference
- Numbered sections for easy citation
- Tables for decision matrices
- Templates for common patterns
- Checkboxes for verification

### 3. Execution Context
- Added "when to use" guidance
- Clarified transition rules
- Made skip conditions explicit
- Added failure recovery paths

### 4. Template-Based
- Converted examples to reusable templates
- Made frontmatter concrete
- Provided copy-paste-ready code blocks

### 5. Error Handling
- Added skip conditions
- Clarified failure loops
- Made rollback procedures explicit
- Separated recoverable from fatal errors

---

## Pattern Recognition

### Common Issues in Original Prompts

1. **Ambiguous Instructions**
   - "Simulate the workflow" → unclear if mental model or actual execution
   - Fixed by: Clarifying as "design before implement"

2. **Missing Decision Logic**
   - When to proceed vs halt unclear
   - Fixed by: Explicit boolean gate conditions

3. **Assumed Context**
   - References to files/tools without location
   - Fixed by: Full paths and explicit tool checks

4. **Mixed Abstraction Levels**
   - Strategic vision mixed with implementation details
   - Fixed by: Separating phases clearly

5. **Implicit Workflows**
   - Process order unclear
   - Fixed by: Numbered sequential steps with transitions

---

## Key Transformations

### Before → After Patterns

| Before | After |
|--------|-------|
| "Fetch and adopt system prompt" | "**Phase 1: System Initialization** → Fetch from URL → Verify loaded" |
| "Design architecture" | "**Phase 2: Architecture Design** → Deliverables: diagram, matrix, specs" |
| "Use these skills..." | "**Phase 5: Available Skills** → Categorized by: Planning, Web, Quality, Debug..." |
| "Scan conversation for value" | "**Gate Check: KEEP or SKIP?** → SKIP if ALL: [conditions]. KEEP if ANY: [conditions]" |
| "Write as declarative knowledge" | "**Format**: Declarative present tense. ❌ Wrong: 'we decided'. ✅ Right: 'X works by...'" |

---

## Verification Criteria Used

For each rewritten prompt:
- ✅ Can be executed without additional clarification
- ✅ Clear success/failure conditions
- ✅ Explicit decision points with boolean logic
- ✅ Templates/examples provided for common cases
- ✅ Error handling and recovery paths documented
- ✅ Related files cross-linked
- ✅ Execution notes for edge cases

---

## Applications

These rewritten prompts serve as:

1. **System Instructions**: Can be loaded as persistent operating instructions for AI agents
2. **Reference Documentation**: Quick-reference format for developers
3. **Training Material**: Clear examples of prompt engineering best practices
4. **Quality Gates**: Checklists ensure consistent output quality

---

## Related

- [[Multi-Agent-Task-Execution-Framework]] — System configuration
- [[Persistent-System-Operating-Instructions-v5.1]] — Core operating protocol
- [[Wiki-Capture-System-Instructions]] — Knowledge preservation workflow
- [[Obsidian-Markdown-System-Instructions]] — Note syntax reference

---

## Meta: Session Insights

**What Worked**:
- Breaking complex prompts into phases/sections
- Using tables for decision matrices
- Providing before/after examples
- Adding explicit boolean conditions

**Challenges**:
- Balancing completeness vs brevity
- Deciding what's implicit vs explicit
- Structuring for both linear reading and random access

**Future Improvements**:
- Add flowchart diagrams for state machines
- Create troubleshooting decision trees
- Build example prompt library

---

## References

- Original SMP v5.1: https://raw.githubusercontent.com/marktantongco/[[concepts/OpenCode|opencode]]-accomplishments/refs/heads/main/profiles/SMP-v5.1
- Skills.sh: https://skills.sh/trending
- Session Date: 2026-08-01
- Duration: ~30 minutes
