---
title: "Profit–bias identity in sports betting (arXiv 2609.06739)"
type: source
tags: [source, arxiv, sports-betting, vig, k170]
keywords: [profit-bias, levitt, hold, shading, public-bias, simpsons-paradox, mlb]
related:
  - concepts/vig-and-hold.md
  - concepts/favorite-longshot-bias.md
  - concepts/sharp-vs-soft-books.md
  - concepts/line-shopping-and-clv.md
  - entities/sports/nfl-betting.md
  - sources/daily-digest-batch-k170-2026-09-11.md
  - sources/brief-k170-week1-papers-rss-2026-09-11.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-09-11-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-11
updated: 2026-09-11
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2609.06739-the-profit-bias-identity-in-sports-betting-bookm.pdf
phase_0_verdict: ADOPT 2026-09-11 — hold-first margin decomposition; policy wire vig/FLB
wire_status: policy_wired
---

## Relations

- @concepts/vig-and-hold.md — three-channel margin decomposition
- @concepts/favorite-longshot-bias.md — public leans favorites; shading test in MLB panel
- @concepts/sharp-vs-soft-books.md — adverse-selection vs public-bias framing
- @entities/sports/nfl-betting.md — do not assume Levitt shading on NFL without evidence
- @sources/daily-digest-batch-k170-2026-09-11.md — digest batch
- @sources/brief-k170-week1-papers-rss-2026-09-11.md — operator brief

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2609.06739](https://arxiv.org/abs/2609.06739) |
| **Author** | Jacek P. Dmochowski (CCNY) |
| **Type** | q-fin — sports betting market structure |
| **FOSS** | None |
| **Phase-0** | **ADOPT (pattern)** — profit–bias identity supersedes independence assumption in Levitt (2004) |
| **Wire** | `policy_wired` — vig-and-hold + favorite-longshot-bias bullets |

## Narrative

Levitt (2004) models book profit from two numbers — cover probability and handle share — assuming **independence** between bet share and outcome. Dmochowski derives a **profit–bias identity**: expected profit is affine and increasing in the expected share of handle on the **losing** side. Levitt's formula is the independence special case.

Book margin decomposes into **three channels**:

1. **Hold** (overround)
2. **Product of price shading × public lean**
3. **Covariance between bet share and outcome**

A lean is worthless without shading; shading is worthless without a lean. Under a public-belief model, the profit driver is the public's **Bayes error** — probability a representative bettor picks the losing side.

**MLB test (1,139 games):** apparent bet-share/outcome dependence is **Simpson's paradox** — present when games are pooled, absent when split by which side the book favored. Public leans toward favorites, but **no matching shading** detected; realized margin ≈ hold alone.

**NFL Week 1 posture:** keep hold-first edge-card math. Do not assume books shade NFL favorites the way Levitt-style models suggest without side-split tests.

### Lane fit

| Lane | Fit |
|------|-----|
| **Vig / FLB literacy** | **ADOPT** — policy wire on concept pages |
| **Hard Rock edge card** | **No math swap** — hold-first de-vig unchanged |
| **Prod bots / pm scp** | **NONE** |

## Snippets

> "Profit is affine and increasing in the expected share of handle on the losing side, with Levitt's expression as the special case of independence." [Source: arxiv:2609.06739 abstract]

> "The realized margin is indistinguishable from the hold" once games are separated by which side the book favored. [Source: arxiv:2609.06739 abstract — MLB panel]

## Dead Ends

- Applying Levitt shading narrative to NFL spreads without side-split covariance tests
- Treating pooled handle/outcome correlation as proof of exploitable public bias
