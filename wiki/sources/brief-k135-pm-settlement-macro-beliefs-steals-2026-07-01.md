---
title: K135 — PM settlement manipulation + Kalshi macro belief steals
type: source
tags: [source, brief, prediction-markets, kalshi, polymarket, k135]
keywords: [settlement-manipulation, five-minute-btc, cpi-threshold, tail-risk, retail-hygiene]
related:
  - sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md
  - sources/arxiv-2606.30040-kalshi-macro-belief-distributions-2026-07-01.md
  - sources/daily-digest-batch-k135-2026-07-01.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/prediction-markets-crossover.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
maturity: validated
read_status: deep-read
created: 2026-07-01
updated: 2026-07-01
cross-wiki-source: "briefs/2026-07-01_k135-pm-settlement-macro-beliefs-steals.md"
---

## Relations

- @sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md — settlement manipulation evidence
- @sources/arxiv-2606.30040-kalshi-macro-belief-distributions-2026-07-01.md — CPI distribution methodology
- Private brief: `briefs/2026-07-01_k135-pm-settlement-macro-beliefs-steals.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K135 PM settlement + macro belief steals |
| **Date** | 2026-07-01 |
| **Batch** | K135 daily digest (2 PDFs) |

## Narrative

### Settlement manipulation steal (2606.31675)

| Idea | Retail action |
|------|---------------|
| **5-min BTC** Polymarket | **NO-GO or minimal size** — settlement-time spot pushes, post-close reversals |
| **15-min+** horizon | Manipulation signature attenuated — prefer longer oracle windows |
| **Near-even closes** | Highest manipulation risk (~3.9× flow spike) |
| **Retail loss share** | ~93% of non-MM losses in pushed cycles — liquidity-taker tax |
| **Underlying harm** | Degrades spot price discovery despite higher liquidity |

### Kalshi macro beliefs steal (2606.30040)

| Idea | Retail action |
|------|---------------|
| **Threshold ladder** | Convert adjacent CPI binaries → full implied distribution |
| **Tail vs mean** | Size tail trades separately; mean may track Reuters consensus |
| **Surprise memory** | Lagged CPI surprises raise upper-tail probabilities (~4.7pp per 0.1pp surprise) |

### Operator checklist addendum

- [ ] Add **contract horizon** + **cash-settlement-on-spot** flags to PM retail checklist
- [ ] Kalshi macro: read stacked thresholds, not single headline binary
- [ ] Cross-link @osint-wiki PM bots for settlement-window guards — no prod config in public wiki

## Dead Ends

- Election-market "manipulation improves accuracy" applied to 5-min crypto
- CPI tail sizing without fee + spread model
- Auto-scp brief to cemini-prod
