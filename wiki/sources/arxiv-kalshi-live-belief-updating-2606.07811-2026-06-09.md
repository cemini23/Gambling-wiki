---
title: Kalshi live belief updating — NBA event contracts (arXiv 2606.07811)
type: source
tags: [source, arxiv, kalshi, prediction-markets, nba, live-betting, market-efficiency]
keywords: [2606.07811, kalshi, nba, live-betting, underreaction, salience, liquidity, belief-updating]
related:
  - concepts/pm-live-belief-updating.md
  - concepts/prediction-markets-crossover.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/sports-betting-fundamentals.md
  - concepts/gambling-bot-architecture.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/sports/nba-betting.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-06-09-daily.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
maturity: validated
read_status: deep-read
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sweeps/2026-06-09-daily.md — overnight fetch provenance
- @concepts/pm-live-belief-updating.md — retail + bot synthesis page
- @entities/platforms/kalshi.md — platform entity
- @entities/sports/nba-betting.md — sport context (NBA Finals stress test window)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | When Do Markets Fully Process Public Information? Evidence from Real-Time Prediction Markets |
| **Authors** | Giovanni Angelini; Luca De Angelis (University of Bologna) |
| **arXiv** | [2606.07811](https://arxiv.org/abs/2606.07811) |
| **PDF** | `raw-sources/arxiv-2606.07811-when-do-markets-fully-process-public-information.pdf` |
| **sha256** | `4fc5367e0e2928c5…` |
| **Data** | 1-min Kalshi NBA game-contract midpoints merged with NBA play-by-play; 1,421 games / 1,438 game clusters; 362k+ contract-minutes live |
| **Read status** | deep-read — abstract, hypotheses, pre-game calibration, live directional + efficient updating, salience×liquidity, conclusions |

## Narrative

### Thesis

Kalshi NBA **game-winner** contracts are **informative and directionally responsive** to public play-by-play signals, but **do not update one-for-one** with an out-of-sample public-information win-probability benchmark. The **updating gap** predicts **5–15 minute midpoint drift** even net of future benchmark moves — yet **executable** buy-ask/sell-bid returns are **negative**, so the drift is largely absorbed by **spread + fees**.

**gambling-wiki owns:** retail interpretation (don't confuse direction with efficiency), live PM vs book timing, liquidity/salience heuristics for manual and bot design.

**@osint-wiki owns:** prod Kalshi bot execution, quote ingestion, TCA on live NBA lanes.

### Pre-game calibration [CONFIRMED — §4, Table 2, Figure 1]

| Horizon | Brier | Pattern |
|---------|-------|---------|
| 24h before tip | 0.204 | Informative; slope ≈ 0.98 vs realized |
| Close (last pre-play quote) | 0.199 | **+0.0046 Brier improvement** vs 24h (significant) |
| Pre-game revision | — | Coefficient **1.29** on revision → payout (10pp revision ≈ 13pp payout lift) |

Kalshi pre-game prices are a **meaningful prior**; live tests are updates from that prior, not from a blank slate.

### Directional live updating [CONFIRMED — §5, Tables 3–4]

Prices move **symmetrically** in the expected direction after signed public signals:

| Signal (favorable vs unfavorable) | Mean ∆mid (pp) |
|-----------------------------------|----------------|
| Net points, 1 min | ±2.8 |
| Made 3pt | ±3.7 / 3.8 |
| Lead change | ±4.5 |
| 10–0 run | ±2.8 |

Regression: **+1 net point in prior minute → +1.22pp** midpoint (with controls). Market **processes public information in real time** directionally.

### Efficient updating — the core finding [CONFIRMED — §5.1, Table 5]

Out-of-sample logit benchmark `q_it` (pre-game close + score margin, clock, period, recent scoring — **excludes contemporaneous Kalshi price**):

| Stat | Value |
|------|-------|
| Benchmark Brier | 0.164 (= live Kalshi; vs 0.211 pre-game close) |
| **β: ∆p on ∆q** | **0.638** (H₀: β=1 rejected, p<0.001) |
| Interpretation | **10pp benchmark move → ~6.4pp Kalshi move on impact** |

**Directional responsiveness ≠ efficient updating.**

### Gradual correction [CONFIRMED — Table 6, Figure 4]

Updating gap `Gap = ∆q − ∆p` predicts future drift; **net of future benchmark changes** at 5 min: **ρ ≈ 0.46** (10pp gap → ~4.6pp additional midpoint move). Persists 1–15 minutes. **Clutch states:** β falls to **~0.51** (Appendix C).

### Salience × liquidity [CONFIRMED — §6, Tables 7–8]

- **Salience** (3pt, lead change, runs): smaller underreaction gaps on average — visible events recognized faster.
- **Illiquidity** (wide spread, low volume/OI): **larger** underreaction on impact.
- **Interaction:** salient events in **thin markets** still underreact most; lead-change × illiquidity largest.
- Salience **does not** imply systematic overreaction in this data.

### Executable returns — no free lunch [CONFIRMED — Appendix B]

Midpoint drift survives volume/spread filters, but **buy-at-ask / sell-at-bid** style returns are **negative**. Predictable drift is **not** a retail arb after crossing the spread.

### Retail takeaways

1. **Kalshi live NBA mids track the game** — useful for situational reads, not stale.
2. **Mids lag full public-information move by ~36%** on 1-min horizons — expect **continued drift** after big runs, especially in **low-liquidity** games/periods.
3. **Do not treat PM mid as "fair" instantly** after salient events — wait for spread to tighten or size down.
4. **Cross-venue:** books may also lag, but this paper is **Kalshi-only**; don't assume identical β on DK/FD in-play.
5. **Bot design:** signal→order needs **liquidity gate** + **drift-aware exit**; naive "benchmark says +10pp, mid only +6pp, buy" loses to spread unless maker/limit logic.

### Routing

- Live PM efficiency → `@concepts/pm-live-belief-updating.md`
- Kalshi entity → `@entities/platforms/kalshi.md`
- NBA sport → `@entities/sports/nba-betting.md`
- Cross-venue divergence (pre-game / static) → `@concepts/sportsbook-pm-line-divergence.md`

## Snippets

> "A one-minute change in benchmark win probability is associated with only about a 0.64-for-one contemporaneous change in market prices." [Source: arxiv-2606.07811, Abstract]

> "Directional responsiveness is not the same as efficient updating." [Source: arxiv-2606.07811, §1]

> "Executable-style returns that buy at the ask and sell at the bid are negative, indicating that the predictable midpoint drift is largely absorbed by trading costs." [Source: arxiv-2606.07811, §5.1 / Appendix B]

> "Salience appears to improve recognition of public information, while liquidity determines whether that information is fully incorporated into prices." [Source: arxiv-2606.07811, §6]

## Dead Ends

- **Midpoint drift as retail edge** — spread/fees eat predictable correction; not a +EV manual system without maker infrastructure.
- **Direct transfer to Polymarket/crypto CLOB** — paper is regulated Kalshi NBA only; microstructure may differ.
- **Sportsbook in-play β=0.64 claim** — no book data in paper; cross-venue extrapolation is `[TENTATIVE]`.
