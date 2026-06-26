---
title: K122 — Poker researcher track research plan
type: source
tags: [source, brief, poker, devfun, researcher-track, k122, hu]
keywords: [trueskill, hu-sandbox, jungleman, pfr-fix, starter-kit]
related:
  - sources/research-k122-poker-paper-landscape-2026-06-19.md
  - concepts/heads-up-arena-strategy.md
  - concepts/poker-axis-eval-literacy.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
maturity: validated
read_status: deep-read
created: 2026-06-19
updated: 2026-06-26
cross-wiki-source: "briefs/2026-06-19_k122-poker-researcher-track-research-plan.md"
---

## Relations

- @sources/research-k122-poker-paper-landscape-2026-06-19.md — 12-paper map (companion research doc)
- @concepts/heads-up-arena-strategy.md — HU strategy primer
- @sources/brief-k123-researcher-jun21-checklist-2026-06-20.md — Jun 21 β checklist

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K122 researcher track 6-lane research plan |
| **Date** | 2026-06-19 |
| **Lanes** | papers · GitHub · SDK · HU strategy · OSINT · wiki inventory |

## Narrative

### Executive summary

Researcher track = **HU sandbox** + **TrueSkill** + pure-code **`decide()`** (Level 3–4). Build on `devfun-org/poker-arena-starter-kit` + `uoftcprg/pokerkit`.

**Blocker (K118):** passive PFR (~2.2% vs VPIP ~11.5%) fatal for HU — fix shared preflop path before style emulation.

### Workstream highlights

| Window | Tasks |
|--------|-------|
| **W0 (pre β)** | Starter kit green; P0 PFR fix; HU `decide()` fork; 29+ HU regression spots |
| **W1 (Jun 21–25)** | BTN open 70–85%; BB defend wide; 3-bet 20–25%+; Jungleman default style rep |
| **W2 (ongoing)** | Paper deep-reads → wiki stubs; PokerSkill Phase-0; slumbot2019 freq compare |

### Architecture choice

Stay **pure-code heuristic** — not runtime LLM (L2) or trained CFR weights (L3) before public sandbox. Optimize **match W/L** for TrueSkill, not selfplay bb/100 alone.

## Dead Ends

- Porting Playground 6-max charts unchanged to HU
- Selfplay bb/100 as TrueSkill optimization target
