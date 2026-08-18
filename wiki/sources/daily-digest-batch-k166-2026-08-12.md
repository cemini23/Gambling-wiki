---
title: Daily digest batch K166 (2026-08-12)
type: source
tags: [source, arxiv, daily-digest, k166, game-theory, fictitious-play]
keywords: [digest, 2608.09389, 2608.09256, ftrl, team-fp, dtoa]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-12-daily.md
  - sources/daily-digest-batch-k163-2026-07-29.md
  - sources/daily-digest-batch-k164-2026-07-30.md
  - sources/daily-digest-batch-k165-2026-08-04.md
  - sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
  - sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md
  - sources/brief-k166-regret-learning-games-shelf-2026-08-12.md
  - sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
  - sources/daily-digest-batch-k167-2026-08-18.md
maturity: validated
read_status: skimmed
created: 2026-08-12
updated: 2026-08-18
---

## Relations

- @sweeps/2026-08-12-daily.md — overnight fetch (2 PDFs)
- @sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md — REFERENCE FTRL/FP literacy shelf
- @sources/arxiv-2608.09256-distributed-team-orchestration-supervisor-2026-08-12.md — REFERENCE team-FP shelf + FOSS NO-GO
- @sources/brief-k166-regret-learning-games-shelf-2026-08-12.md — operator shelf brief
- @sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md — next FP shelf (K167 SFP-MFG)
- @sources/daily-digest-batch-k167-2026-08-18.md — next digest batch

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-08-12 |
| **Origin** | `research to be indexed/` — 2 PDFs |
| **Verdict** | **2 REFERENCE / 0 GO / 0 reject** (incl. FOSS NO-GO for 09256) |

| arXiv | Title | Phase-0 | Verdict |
|-------|-------|---------|---------|
| 2608.09389 | Regret, equilibrium, and learning in games: A guided tour (Mertikopoulos) | Survey/chapter; no FOSS | **REFERENCE** — FTRL/Hedge/FP literacy shelf |
| 2608.09256 | Distributed Team Orchestration via Supervisor Networks (DTOA / BR-DTOA) | Claimed code GitHub → 404; user 0 public repos | **REFERENCE** — team-FP/MAS shelf + **FOSS NO-GO** |

**Archive:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/` (2 PDFs; inbox cleared)

## Narrative

Two-REFERENCE batch under arxiv-only discovery (`poker-mafp-arxiv` cluster). 09389 is the primary paper — a canonical unified tour of FTRL / Hedge / EXP3 / FP with the Brown–Robinson theorem, a quantitative zero-sum ergodic Gap bound, and a folk theorem linking NE to attracting points of regularized learning. 09256 is a weak team-FP adjacency (supervisor-network distributed belief learning + Byzantine resilience) — shelf only, no steal. No FOSS for either; claimed 09256 repo verified HTTP 404. Poker-arena research brief only; no atto / GuruWatcher / CeminiDFS / TipDrop / prod scp; decide() untouched.
