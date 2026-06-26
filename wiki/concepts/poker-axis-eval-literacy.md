---
title: Poker axis eval literacy (Raeth M₁–M₉)
type: concept
tags: [concept, poker, devfun, researcher-track, eval, cross-wiki]
keywords: [multi-axis, cognitive profile, trajectory, bet-sizing, bluff-frequency, raeth]
related:
  - concepts/heads-up-arena-strategy.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/platforms/devfun-poker-arena.md
  - concepts/poker-hl-analyst-loop.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
maturity: draft
created: 2026-06-19
updated: 2026-06-26
---

## Relations

- @osint-wiki/concepts/poker-arena-multi-axis-cognitive-profile.md — **canonical** nine-axis table, M₁–M₉ definitions, trajectory export ritual
- @osint-wiki/concepts/devfun-researcher-track-readiness-2026-06.md — pre-submit gates (`axis_summary.json`)
- @concepts/heads-up-arena-strategy.md — HU strategy; axes are **submit hygiene**, not primary TrueSkill metric

## Raw Concept

Gambling-wiki **pointer stub** — dev.fun Researcher Round evaluates agents on *how* they play (multi-axis cognitive profile), not only win rate. Full rubric lives in OSINT wiki (Raeth arXiv 2606.13815).

## Narrative

Researcher sandbox ranking is **TrueSkill** (HU match outcomes) per K121 email. Separately, BenchFlow / Discord thesis expects **trajectory export** and multi-axis profiling — bet sizing vs GTO histograms (M₁), bluff frequency (M₂), opponent-read quality (M₃), positional VPIP gaps (M₉), etc.

**Operator rule:** Optimize for TrueSkill first; run axis summary gates before every submit so style-rep and research narrative do not fail on obvious holes (e.g. never bluffing, illegal sizing, flat VPIP across positions).

Do **not** duplicate the M₁–M₉ table here — read @osint-wiki/concepts/poker-arena-multi-axis-cognitive-profile.md.

## Snippets

> Trajectory + multi-axis score shapes next eval version — Discord Researcher Round welcome [Source: @osint-wiki/sources/devfun-researcher-track-discord-welcome-2026-06-18.md]

## Dead Ends

- Treating axis score as **primary** LB sort — email confirms **TrueSkill** for sandbox rank
- Duplicating full Raeth methodology in public wiki while competition live — keep prod thresholds in OSINT agent repo
