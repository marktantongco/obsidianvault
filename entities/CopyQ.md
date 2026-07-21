---
title: CopyQ
category: entities
tags:
  - tool
  - clipboard
  - qt
  - wayland
sources:
  - conversation:2026-07-09
  - /home/x1/Downloads/@ai/free-china-proxy-research.md
  - journal/2026-07-09-multi-agent-wiki-compound
summary: >-
  Qt-based clipboard manager with advanced features (tabs, search, scripting).
  Installed on the system but autostart disabled in favor of GPaste on Wayland.
  Fallback clipboard manager when not using GNOME/Wayland.
provenance:
  extracted: 0.6
  inferred: 0.4
  ambiguous: 0.0
base_confidence: 0.55
lifecycle: draft
tier: peripheral
created: 2026-07-09T09:57:44Z
updated: 2026-07-21T08:00:00Z
---

# CopyQ

## Overview

CopyQ is an advanced Qt-based clipboard manager with tabbed clipboard history, search, scripting support, and custom commands. It was the primary clipboard manager on this system until the switch to [[entities/GPaste]].

## Key Facts

- **Type**: Qt clipboard manager
- **Install method**: Likely via apt (`apt install copyq`)
- **Autostart**: **Disabled** — removed in favor of GPaste on GNOME Wayland
- **Status**: Installed but inactive
- **Replacement**: [[entities/GPaste]] (gpaste-2) preferred on Wayland

## Why Replaced

Per the [[journal/2026-07-09-multi-agent-wiki-compound|July 9 session]]:

- CopyQ is a Qt application, which can have integration issues on GNOME Wayland
- [[entities/GPaste]] is natively GNOME/GTK, providing tighter shell integration
- The GNOME Wayland environment benefits from gpaste's native clipboard handling

## Potential Use Cases

- Fallback when not using GNOME (e.g., X11, other desktop environments)
- If GPaste has issues, CopyQ can be re-enabled by re-adding its autostart entry

## Related

- [[entities/GPaste]] — Replacement clipboard manager (active)
- [[skills/gpaste-gnome-wayland]] — GPaste setup guide
- [[journal/2026-07-09-multi-agent-wiki-compound]] — Session documenting the switch
