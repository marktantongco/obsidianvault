---
title: Cross-Agent Workflow Test
type: project
created: 2026-07-09
updated: 2026-07-21
status: testing
tags: [test, workflow, agents]
---

# Cross-Agent Workflow Test

## Goal
Test the complete multi-agent workflow from research to implementation.

## System State (2026-07-21)

The vault now has comprehensive documentation of all 7 agents and their routing through the LifeOS Algorithm. This test plan validates that the actual CLI tools work as documented.

**Current environment**: Freebuff Cloud workspace — does not have local CLI agents installed (OpenCode, Claude, Hermes, etc.).
**Test results below reflect**: The last known state from the local machine (Ubuntu 26.04, Intel HD 520, i5-6200U).

---

## Test Results

### Test 1: Wiki Query (Knowledge Retrieval)

| Field | Detail |
|-------|--------|
| **Command** | `wiki-query @personal What is the current state of my AI setup?` |
| **Expected** | Returns compiled knowledge from wiki pages |
| **Status** | ✅ **PASSED** (tested 2026-07-09) |
| **Evidence** | The `obsidian-wiki doctor` command confirmed 12 agents provisioned and doctor pass. Wiki-query returned compiled knowledge from the vault pages. |
| **Pages cited** | [[concepts/AI Agents]], [[concepts/OpenCode]], [[concepts/Hermes Agent]], etc. |

### Test 2: Wiki Capture (Save Finding)

| Field | Detail |
|-------|--------|
| **Command** | `wiki-capture --quick "Test finding from workflow"` |
| **Expected** | Saves to `_raw/` staging area |
| **Status** | ⏳ **NOT RUN** |
| **Context** | Requires `wiki-capture` skill to be available on the local machine. The capture pipeline is fully documented at [[concepts/poznote-pipeline]]. |
| **Blockers** | This test was deferred during the initial setup session. The pipeline script (`poznote_pipeline.py`) exists at `second-brain/scripts/` but the Poznote tool itself was not installed on the machine. File mode (dropping `.md` files in `_raw/poznote/`) is the available fallback. |

### Test 3: OpenCode Execution

| Field | Detail |
|-------|--------|
| **Command** | `opencode -p "Write a Python hello world script"` |
| **Expected** | Generates and explains code |
| **Status** | ⏳ **NOT RUN** |
| **Context** | OpenCode v1.17.16 is installed at `~/.opencode/bin/opencode` with 37 skills. Configured with FreeHive provider for model access. |
| **Blockers** | Requires local CLI access to the machine. OpenCode initial TUI setup may be needed after FreeHive provider config. |

### Test 4: Claude Code Review

| Field | Detail |
|-------|--------|
| **Command** | `claude "Review this code for best practices"` |
| **Expected** | Provides code review feedback |
| **Status** | ⏳ **NOT RUN** |
| **Context** | Claude Code v2.1.205 is installed at `~/.local/bin/claude` with 37 skills. Only OpenAI API key configured — Anthropic API key still pending (see [[API-KEY-GUIDE]]). |
| **Blockers** | No Anthropic API key configured. Claude Code uses OpenAI API as fallback, but Anthropic models are preferred for code review. FreeHive gateway could also serve Claude models if `claude login` is run. |

### Test 5: Hermes Orchestration

| Field | Detail |
|-------|--------|
| **Command** | `hermes "Plan a simple web scraper project"` |
| **Expected** | Creates task breakdown |
| **Status** | ⏳ **NOT RUN** |
| **Context** | Hermes v0.18.2 is installed at `~/.hermes/hermes-agent/.venv/bin/hermes` with 36 skills and 2 plugins (Hermes-OpenCode, Hermes-Claude bridges). |
| **Blockers** | The hermes_router.py dispatch integration was built during the July 13 session but the LifeOS Pulse daemon (`bun run pulse`) has not been started. Hermes CLI works independently but full LifeOS Algorithm dispatch hasn't been validated end-to-end. |

### Test 6: Cross-Agent Handoff

| Field | Detail |
|-------|--------|
| **Flow** | Hermes → OpenCode → Claude → Wiki |
| **Expected** | Task flows through agents, results saved to wiki |
| **Status** | ⏳ **NOT RUN** |
| **Context** | The full handoff pipeline is architected in `hermes_router.py` with the LifeOS Algorithm E1→E5 routing matrix. |
| **Blockers** | Requires Tests 3–5 to complete first. Additionally, Grok and Antigravity are not yet wired into hermes_router dispatch (Claude Code currently handles both E4 and E5 tiers). |

---

## Prerequisites for Full Run

These dependencies must be satisfied before Tests 2–6 can execute:

| Prerequisite | Blocks | Status |
|-------------|--------|--------|
| Local CLI access to Ubuntu 26.04 machine | Tests 2–6 | ⚠️ Remote — Freebuff workspace doesn't have local agents |
| Anthropic API key | Test 4 (Claude) | ⏳ Pending (see [[API-KEY-GUIDE]]) |
| LifeOS Pulse daemon running (`bun run pulse`) | Test 5 (Hermes routing) | ⏳ Pending — daemon not started |
| Poznote tool installed | Test 2 | ⏳ Pending |
| Grok + Antigravity wired into hermes_router | Test 6 (full handoff) | ⏳ Pending — currently Claude handles E4 and E5 |

## Test Script

The following script is ready to run on the local machine once prerequisites are met:

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

## Success Criteria Progress

- [x] Test 1: Wiki Query — PASSED (2026-07-09)
- [ ] Test 2: Wiki Capture — Blocked (Poznote not installed)
- [ ] Test 3: OpenCode Execution — Blocked (requires local CLI)
- [ ] Test 4: Claude Code Review — Blocked (no Anthropic API key)
- [ ] Test 5: Hermes Orchestration — Blocked (Pulse daemon not running)
- [ ] Test 6: Cross-Agent Handoff — Blocked (depends on 3–5)
- [ ] Wiki captures all findings
- [ ] Code is generated and reviewed
- [ ] Workflow is documented
- [ ] No errors in logs

---

## Notes

- Tests run sequentially — each builds on the previous
- Results should be logged to `log.md`
- Findings should be captured to wiki via `wiki-capture`
- The vault documentation now covers all agents, routing, and pipelines — test execution is the remaining gap

## Related

- [[concepts/AI Agents]] — Agent catalog
- [[concepts/LifeOS Algorithm]] — E1→E5 routing matrix
- [[concepts/system-prompt-v5-1-1]] — Master prompt governing all agents
- [[concepts/poznote-pipeline]] — Capture pipeline
- [[API-KEY-GUIDE]] — Required API keys
- [[concepts/FreeHive]] — AI gateway for model access
