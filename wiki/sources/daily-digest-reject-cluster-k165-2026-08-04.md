---
title: Daily digest reject cluster K165 (2026-08-04)
type: source
tags: [source, arxiv, daily-digest, reject, k165]
keywords: [digest, reject, 2607.28779, bits-per-spike, neuroscience, kelly-metaphor]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-04-daily.md
  - sources/daily-digest-batch-k165-2026-08-04.md
  - sources/brief-k165-bits-per-spike-false-positive-shelf-2026-08-04.md
maturity: validated
read_status: skimmed
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- @sources/daily-digest-batch-k165-2026-08-04.md — sibling batch

## Raw Concept

| arXiv | Title | Verdict |
|-------|-------|---------|
| 2607.28779 | Bits per Spike as a Betting Game: An Interpretable Unit for Held-Out Log-Likelihood in Neural Data Analysis | **Reject** — neural spike-train stats / bits-per-spike |

**Archive:** PDF archived with batch to egress-fi.  
**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.28779-bits-per-spike-as-a-betting-game-an-interpretabl.pdf`

## Narrative

Williams (NYU / Flatiron) reinterprets **bits per spike** (held-out log-likelihood vs homogeneous Poisson) as a Kelly-style betting game against a baseline “market,” with Ville’s inequality giving anytime-valid significance via wealth process. Application domain: **mouse thalamic head-direction cells / GLMs** — computational neuroscience, not sports betting or bankroll sizing.

Digest false positive via `kelly-bankroll-arxiv` — query matched `Kelly` + `betting` without requiring odds/sports/wagering anchors.

## Dead Ends

- Bits-per-spike as DFS ownership or CLV unit
- Neural recording “time to significance” as sportsbook Kelly fraction
- Spike-train FOSS adopt for gambling bots
