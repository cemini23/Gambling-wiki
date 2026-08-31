---
title: Odds conversion under EMH — OO-EPC and FL-GLM (arXiv 2604.17194)
type: source
tags: [source, arxiv, sports-betting, vig, flb, k168]
keywords: [oo-epc, fl-glm, multiplicative-de-vig, shin, power-conversion, booksum]
related:
  - concepts/vig-and-hold.md
  - concepts/favorite-longshot-bias.md
  - concepts/line-shopping-and-clv.md
  - concepts/daily-edge-card.md
  - entities/sports/nfl-betting.md
  - sources/daily-digest-batch-k168-2026-08-31.md
  - sources/brief-k168-nfl-season-paper-rss-2026-08-31.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-31-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2604.17194.pdf
phase_0_verdict: REFERENCE 2026-08-31 — soccer 1X2 de-vig methods; do not swap edge-card multiplicative until NFL 2-way check
wire_status: wont_wire
---

## Relations

- @concepts/vig-and-hold.md — multiplicative de-vig is the common method this paper critiques
- @concepts/line-shopping-and-clv.md — conversion method is independent of which book you shop
- @concepts/favorite-longshot-bias.md — FL-GLM fits one FLB parameter
- @concepts/daily-edge-card.md — card still uses multiplicative `fair_p`; OO-EPC is a candidate, not a swap
- @entities/sports/nfl-betting.md — W8 process literacy, not a soccer tip sheet
- @sources/brief-k168-nfl-season-paper-rss-2026-08-31.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2604.17194](https://arxiv.org/abs/2604.17194) |
| **Title** | Forecast Sports Outcomes under Efficient Market Hypothesis: Theoretical and Experimental Analysis of Odds-Only and Generalised Linear Models |
| **Authors** | Goto, Takeishi, Yairi (University of Tokyo) |
| **Data** | 90,014 association-football matches, five books, 2012–2024 |
| **FOSS** | Kaggle notebook cited in paper; GitHub search 2026-08-31 returned **0** SPDX repos |
| **Verdict** | **REFERENCE** — de-vig literacy. Soccer 1X2 ≠ NFL spread. |

## Narrative

Converting posted odds into probabilities is the step the daily edge card already does (multiplicative de-vig). This paper shows that common odds-only converters rest on assumptions the data reject:

| Method | Assumption this paper flags |
|--------|-----------------------------|
| **Multiplicative** | Equal expected loss on every outcome — contradicts FLB |
| **Shin (numerical / analytical)** | Fewer insiders → worse odds; booksum vs accuracy correlation **not** found |
| **Power** | Power-law with **no intercept**; intercept is significant in their panel |

**OO-EPC** (odds-only, no history): reduce inverse odds by a shared z-score so the bookmaker has equal profitability-confidence on each outcome. Beats other odds-only methods on **most** of five books (log-loss); Bet365 / William Hill sometimes prefer Shin or Power. Falls back to multiplicative when booksum is too tight (rare: >99.9% of their sample satisfies the constraint).

**FL-GLM** (needs history): one fitted power parameter for FLB plus an adaptive intercept so probabilities sum. More accurate and more interpretable than multinomial / ordered logit converters on this panel.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **W8 Hard Rock card** | **MEDIUM** — method class matches `daily_edge_card.py`; do **not** replace multiplicative until a two-way NFL/NBA check |
| **CLV / de-vig** | **HIGH** — literacy: `fair_p` is converter-dependent |
| **CeminiDFS / FanDuel GPP** | **LOW** — 1X2 soccer, not fantasy projections |
| **Prod wagering bots** | NO-GO |

## Snippets

> "The most common approach is the multiplicative conversion… This method assumes that bettors have the same expected loss on all outcomes. This assumption contradicts the favourite-longshot bias." [Source: arxiv:2604.17194 §2]

> "Our proposed OO-EPC method had a significantly superior log-loss than all other odds-only methods for the majority of the five bookmakers." [Source: arxiv:2604.17194 §5.1]

## Dead Ends

- Treating soccer 1X2 log-loss ranks as NFL spread proof
- Swapping the edge-card converter without a paired NFL two-way holdout
- Claiming OO-EPC GitHub (no SPDX clone found 2026-08-31)
