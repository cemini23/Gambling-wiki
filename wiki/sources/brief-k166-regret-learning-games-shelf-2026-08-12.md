---
title: Brief K166 — regret / learning-in-games shelf
type: source
tags: [brief, k166, game-theory, regret, ftrl, fictitious-play]
keywords: [k166, 2608.09389, 2608.09256, ftrl, hedge, team-fp, dtoa, shelf]
related:
  - meta/daily-research-digest-cadence.md
  - sources/daily-digest-batch-k166-2026-08-12.md
  - sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
  - sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/brief-k163-swap-regret-attention-shelf-2026-07-29.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sweeps/2026-08-12-daily.md
maturity: validated
read_status: deep-read
created: 2026-08-12
updated: 2026-08-12
wire_status: wont_wire
cross-wiki-source: "briefs/2026-08-12_k166-regret-learning-games-shelf.md"
---

## Relations

- Wiki: `briefs/2026-08-12_k166-regret-learning-games-shelf.md`
- OSINT arena: `agents/devfun-poker-arena/briefs/2026-08-12_k166-regret-learning-games-shelf.md`
- Phase-1: `wont_wire` — both papers REFERENCE-only; no ADOPT-GO runtime

## Raw Concept

K166 shelf — FTRL / Hedge / FP literacy (09389) + team-FP supervisor adjacency (09256). **Do not** import either into decide()/HL. Phase-0 REFERENCE for both; FOSS NO-GO for 09256 (claimed repo HTTP 404).

## Narrative

1. 09389 Mertikopoulos guided tour: unified regularized learning (Hedge/EXP3/Tsallis-INF/FTRL), Brown–Robinson FP (Thm 1), zero-sum ergodic Gap bound (Thm 4), folk theorem NE ↔ attracting points (Thm 5). Theory shelf next to K163/K157/K152.
2. 09256 DTOA/BR-DTOA: team-FP over supervisor-network beliefs; Byzantine misreporting + identification. Shelf-only adjacency to MAFP; not an HU-poker solver.
3. No FOSS (09256 repo 404 verified); no atto / GuruWatcher / CeminiDFS / TipDrop / prod scp.

## Sources

- @sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
- @sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md
