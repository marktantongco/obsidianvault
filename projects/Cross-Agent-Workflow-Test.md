---
title: Cross-Agent Workflow Test
type: project
created: 2026-07-09
updated: 2026-07-09
status: testing
tags: [test, workflow, agents]
---

# Cross-Agent Workflow Test

## Goal
Test the complete multi-agent workflow from research to implementation.

## Test Plan

### Test 1: Wiki Query (Knowledge Retrieval)
**Command**: `wiki-query @personal What is the current state of my AI setup?`
**Expected**: Returns compiled knowledge from wiki pages
**Status**: ✅ PASSED (tested 2026-07-09)

### Test 2: Wiki Capture (Save Finding)
**Command**: `wiki-capture --quick "Test finding from workflow"`
**Expected**: Saves to `_raw/` staging area
**Status**: ⏳ PENDING

### Test 3: OpenCode Execution
**Command**: `opencode -p "Write a Python hello world script"`
**Expected**: Generates and explains code
**Status**: ⏳ PENDING

### Test 4: Claude Code Review
**Command**: `claude "Review this code for best practices"`
**Expected**: Provides code review feedback
**Status**: ⏳ PENDING

### Test 5: Hermes Orchestration
**Command**: `hermes "Plan a simple web scraper project"`
**Expected**: Creates task breakdown
**Status**: ⏳ PENDING

### Test 6: Cross-Agent Handoff
**Flow**: Hermes → OpenCode → Claude → Wiki
**Expected**: Task flows through agents, results saved to wiki
**Status**: ⏳ PENDING

---

## Test Script

```bash
# Test 1: Wiki Query
wiki-query @personal What agents are installed?

# Test 2: Wiki Capture
wiki-capture --quick "Workflow test completed successfully"

# Test 3: OpenCode
opencode -p "Create a simple REST API endpoint in Python"

# Test 4: Claude Code
claude "Review the code at ~/ai-workspace/test_api.py"

# Test 5: Hermes
hermes "Break down the task: Build a todo app with React"

# Test 6: Full Workflow
# Step 1: Hermes plans
hermes "Plan: Create a Python script that fetches weather data"

# Step 2: OpenCode implements
opencode -p "Implement the weather script planned by Hermes"

# Step 3: Claude reviews
claude "Review ~/ai-workspace/weather.py for security issues"

# Step 4: Wiki documents
wiki-capture --quick "Weather script created and reviewed"
```

---

## Expected Results

### After Test 1
- Wiki returns compiled knowledge
- Pages cited: [[AI Agents]], [[OpenCode]], etc.

### After Test 2
- Finding saved to `_raw/`
- Available for future queries

### After Test 3
- Code generated at `~/ai-workspace/test_api.py`
- Explanation provided

### After Test 4
- Code review feedback
- Security recommendations

### After Test 5
- Task breakdown with subtasks
- Estimated time/complexity

### After Test 6
- Complete workflow documented
- All artifacts saved to wiki

---

## Success Criteria

- [ ] All 6 tests pass
- [ ] Wiki captures all findings
- [ ] Code is generated and reviewed
- [ ] Workflow is documented
- [ ] No errors in logs

---

## Notes

- Tests run sequentially for verification
- Each test builds on previous
- Results logged to `log.md`
- Findings captured to wiki
