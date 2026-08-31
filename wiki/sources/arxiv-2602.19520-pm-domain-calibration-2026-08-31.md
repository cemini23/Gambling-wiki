---
title: Domain-specific PM calibration — Kalshi/Polymarket sports vs politics (arXiv 2602.19520)
type: source
tags: [source, arxiv, prediction-markets, kalshi, nfl, calibration, k168]
keywords: [crowd-wisdom, logistic-recalibration, sports-calibration, favorite-longshot, namanhzz]
related:
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/sports/nfl-betting.md
  - concepts/prediction-markets-crossover.md
  - concepts/favorite-longshot-bias.md
  - concepts/pm-whale-conviction-bias-2026-07.md
  - sources/daily-digest-batch-k168-2026-08-31.md
  - sources/brief-k168-nfl-season-paper-rss-2026-08-31.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-31-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2602.19520.pdf
phase_0_verdict: REFERENCE 2026-08-31 — MIT replication repo; sports prices near-calibrated short-horizon; no retail auto-recalibrate
wire_status: wont_wire
---

## Relations

- @entities/platforms/kalshi.md — sports is ~67% of Kalshi trades in this panel; short-horizon NFL prices are the trustworthy slice
- @entities/platforms/polymarket.md — sports slope ~1.06 on comparable bins
- @entities/sports/nfl-betting.md — game contracts vs season-long futures
- @concepts/favorite-longshot-bias.md — sports FLB is a **long-horizon** effect here (slope 1.74 beyond 1 month)
- @concepts/pm-whale-conviction-bias-2026-07.md — large Kalshi **political** trades compress; sports size gap is null
- @sources/brief-k168-nfl-season-paper-rss-2026-08-31.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2602.19520](https://arxiv.org/html/2602.19520) |
| **Title** | Decomposing Crowd Wisdom: Domain-Specific Calibration Dynamics in Prediction Markets |
| **Author** | Nam Anh Le |
| **Data** | 353M trades / 429k binaries; Kalshi primary; Polymarket compare; cutoff **2025-12-31** |
| **FOSS** | [namanhzz/prediction-market-calibration](https://github.com/namanhzz/prediction-market-calibration) **MIT** |
| **Verdict** | **REFERENCE** — read sports slopes; do not clone as a trading bot |

## Narrative

A 70¢ contract is not always a 70% probability. Logistic recalibration slope `b`: `b>1` = prices compressed toward 50% (underconfidence / FLB-like); `b<1` = prices too extreme.

**Sports (Kalshi, Table 4 horizons):** slopes **0.90–1.10** from 0–48h, then **1.24** at 1 week–1 month, **1.74** beyond one month. Sports ECE **0.008** (Politics **0.117**). Trade-size gap in sports is **null** (`Δ +0.07`); Politics large vs single is `+0.53`.

**Operator read for NFL 2026:**

| Horizon | Trust the posted PM price? |
|---------|----------------------------|
| Kickoff-week / in-game / next-few-days | **Yes, as a probability** (near-calibrated) |
| Season win totals / awards / month-plus futures | **No** — compress toward 50%; favorites underpriced, longshots overpriced |
| Whale size on sports | No extra compression (unlike politics) |

Sports dominates Kalshi **trade count** (43.2M / 66.7%) with 55,637 markets. Do not mix political calibration into NFL game contracts.

Replication is MIT. **Do not** wire as a live recalibrator or clone into CeminiSuite. Extract the domain×horizon table only.

## Snippets

> "Sports markets are close to calibrated at short-to-medium horizons (slopes 0.90–1.10 from 0 to 48 hours) but become underconfident at long horizons, reaching 1.74 beyond one month." [Source: arxiv:2602.19520 Stylized Fact 2]

> "For sports markets. At horizons under one week, sports market prices are reasonably trustworthy (slopes 0.90–1.10). Beyond one month, the favorite–longshot bias appears strongly (slope 1.74)." [Source: arxiv:2602.19520 §9]

## Dead Ends

- Recalibrating every Kalshi NFL ticket with the politics slope
- Treating MIT replication as a prod PM bot
- Reading "sports well calibrated" as +EV vs Hard Rock — calibration ≠ vig-beating edge
