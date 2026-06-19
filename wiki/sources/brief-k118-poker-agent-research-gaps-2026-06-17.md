---
title: K118 — Poker agent research gaps and fix backlog
type: source
tags: [source, brief, poker, devfun, hl-loop, k118]
keywords: [k118, cemini_decide, PFR, AlphaExploitem, ToolPoker, arena-pokerkit]
related:
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/platforms/devfun-poker-arena.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - entities/bots/poker-bot-tooling.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k107-poker-open-spot-audit-2026-06-09.md
maturity: validated
read_status: deep-read
created: 2026-06-17
updated: 2026-06-19
cross-wiki-source: "briefs/2026-06-17_k118-gambling-poker-agent-research-gap-fixes.md"
---

## Relations

- @concepts/poker-hl-analyst-loop.md — HL loop; PFR gate gap documented here
- @entities/bots/cemini-devfun-poker-agent.md — public agent summary
- Private brief: `briefs/2026-06-17_k118-gambling-poker-agent-research-gap-fixes.md` (operator fix backlog)

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K118 poker agent research gap analysis |
| **Date** | 2026-06-17 |
| **Selfplay audit** | 400h seed 42 — VPIP 11.5%, PFR 2.2%, gap ~9pp |
| **Implementation** | `@osint-wiki/agents/devfun-poker-arena/` |

## Narrative

Cross-walk of **2025–2026 poker-agent literature** (AlphaExploitem, ToolPoker, RL-CFR, PokerSkill, arena-pokerkit-hands) against **cemini_decide** architecture. Primary gap: **passive PFR** (SB limp inflation, rock steal threshold 0.99, no PFR deploy gate). Secondary: thin session memory vs multi-hand exploit research; eval panel (DeepCFR) vs Playground opponent mismatch.

### P0 fixes (private repo)

1. Add PFR / VPIP−PFR gate to `cemini_selfplay_audit.py`
2. SB complete → fold for trash; lower rock `open_steal_equity`
3. Chart audit for CO/BTN opens mapped to check

Full table: see private K118 brief.

## Dead Ends

- **Runtime LLM decide()** — latency + ToolPoker knowing–doing gap at inference
- **Full COM / river CFR in prod** — Arena clock + complexity
- **Optimize for selfplay bb/100** — misaligned with Playground analyze leaks
