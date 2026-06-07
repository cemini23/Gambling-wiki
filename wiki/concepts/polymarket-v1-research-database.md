---
title: Polymarket-v1 research database
type: concept
tags: [concept, polymarket, data, k100, backtest]
keywords: [2606.04217, dataset, huggingface, flb, calibration]
related:
  - sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md
  - concepts/favorite-longshot-bias.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/prediction-markets-crossover.md
  - entities/platforms/polymarket.md
  - osint-wiki/sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md
  - osint-wiki/concepts/polymarket-microstructure-findings.md
maturity: validated
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- @sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md — K100 source page
- @entities/platforms/polymarket.md — live platform entity
- @osint-wiki/concepts/polymarket-microstructure-findings.md — measurement-layer synthesis

## Raw Concept

Public **1.2B-trade** archive of Polymarket CTF Exchange v1 (Nov 2022 – Apr 2026) with verified aggressor side — primary offline lab for PM retail research; live bots use Gamma/CLOB per OSINT boundary.

## Narrative

### When to use this vs live APIs

| Use case | Tool |
|----------|------|
| FLB / calibration panels across 1.3M markets | **Polymarket-v1 dataset** |
| Fee-reform before/after studies (Jan–Mar 2026) | **Polymarket-v1 dataset** |
| Category spread/liquidity baselines (Sports vs Crypto) | **Polymarket-v1 dataset** |
| Placing today's WC or politics bet | **Live Polymarket UI / API** |
| Bot execution, copy latency | **@osint-wiki** prod stack |

Download: [HuggingFace TimeSeventeen/Polymarket-v1](https://huggingface.co/datasets/TimeSeventeen/Polymarket-v1). Paper: `@sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md`.

### Key retail findings (distilled)

1. **Favorite-longshot reversal** — longshots overpriced, favorites underpriced on resolved v1 panel (opposite of classic racetrack FLB). Update sizing bias toward favorite-side value unless independent model says otherwise (`@concepts/favorite-longshot-bias.md`).

2. **Inferred flow is unreliable** — tick rule ≈ 50% accuracy. Copy-trading and "smart money flow" products built on public tape without on-chain join are structurally weak (`@concepts/pm-copy-trading-retail-risks.md`).

3. **Fee reform confirmed on-chain** — Crypto Jan 2026, Sports Feb 2026, other categories Mar 2026. Post-fee descriptive pattern: less wash volume, wider spreads, remaining flow more "toxic" (informed). Factor into effective hold math (`@concepts/prediction-markets-crossover.md`).

4. **Market quality ≠ easy money** — wider spreads correlate with **better** Brier scores (informed niche markets); high VPIN with **worse** calibration. Don't assume thin/wide markets are automatically -EV or +EV without category context.

5. **Concentration** — top 1% makers ≈ 84% volume. Retail is almost always the taker side of institutional liquidity.

### Boundary

- Dataset is **v1-only** and **frozen** — not a substitute for v2 venue rules or current fee UI.
- Microstructure TCA (VPIN, OFI, on-chain join code) lives on `@osint-wiki` — cross-link only.

## Snippets

> "A truth-aligned database is essential for reliable prediction market design and probability calibration." [Source: arxiv-2606.04217 abstract]
