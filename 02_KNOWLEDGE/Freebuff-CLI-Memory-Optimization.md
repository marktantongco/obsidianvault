---
title: Freebuff CLI — Memory Optimization & Resource Limits
tags:
  - freebuff
  - memory
  - performance
  - cli
  - research
created: 2026-08-03T12:00:00+08:00
updated: 2026-08-03T12:00:00+08:00
category: skill
aliases:
  - freebuff memory
  - freebuff cli rss
---

# Freebuff CLI — Memory Optimization & Resource Limits

Research into the freebuff CLI (the CodebuffAI agent at
`~/.config/manicode/freebuff`, version `0.0.13`) after it was observed using
**~1.99 GB RSS (26.6% of system memory)**.

## Root cause

A single **241 MB `chat-messages.json`** file that expands **5–10×** when
parsed into in-memory JS objects. The conversation history is the dominant
memory consumer, not the agent runtime itself.

## Techniques / tweaks

- **Trim conversation history** — bound or periodically compact
  `chat-messages.json`; the file's in-memory expansion is the multiplier.
- **Configure resource limits** (systemd `MemoryMax` / `MemoryHigh`, or the
  CLI's own config if exposed) to cap RSS rather than letting it grow to
  GB-scale.
- **Watch the file size trend** — if `chat-messages.json` grows without
  bound across long sessions, add compaction/archival so a single session
  can't balloon memory.

## Takeaways

- For a coding agent, history persistence (JSONL/JSON on disk) is usually
  small; the **parse-time expansion** is the real cost — estimate memory as
  file-size × expansion factor, not file-size.
- Investigate the CLI's config surface (`~/.config/manicode/freebuff`) for
  history/context caps before reaching for OS-level limits.

## Sources

- `opencode://ses_0416912ceffesYZnRBez48O90t` (Research freebuff CLI for
  memory optimization)
