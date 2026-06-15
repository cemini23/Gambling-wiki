---
title: Polymarket-v1 database — research dataset (arXiv 2606.04217)
type: source
tags: [source, arxiv, polymarket, dataset, k100, microstructure]
keywords: [2606.04217, polymarket, database, vpin, flb, fee-reform]
related:
  - concepts/polymarket-v1-research-database.md
  - concepts/favorite-longshot-bias.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/prediction-markets-crossover.md
  - entities/platforms/polymarket.md
  - osint-wiki/sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md
  - osint-wiki/concepts/polymarket-microstructure-findings.md
maturity: validated
read_status: deep-read
created: 2026-06-05
updated: 2026-06-05
cross-wiki-measurement: "@osint-wiki/concepts/polymarket-microstructure-findings.md"
---

## Relations

- @concepts/polymarket-v1-research-database.md — retail access patterns + backtest boundary
- @entities/platforms/polymarket.md — fee reform timeline, platform entity
- @concepts/favorite-longshot-bias.md — Polymarket "FLB reversal" empirical panel
- @concepts/pm-copy-trading-retail-risks.md — inferred flow direction ≈ noise
- @osint-wiki/concepts/polymarket-microstructure-findings.md — TCA, on-chain pipeline (do not duplicate)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Polymarket-v1 Database |
| **Authors** | Boka Qin; Rui Yang (Time Seventeen) |
| **arXiv** | [2606.04217](https://arxiv.org/abs/2606.04217) |
| **Dataset** | [HuggingFace TimeSeventeen/Polymarket-v1](https://huggingface.co/datasets/TimeSeventeen/Polymarket-v1) |
| **PDF** | `raw-sources/arxiv-2606.04217-polymarket-v1-database.pdf` (cemini-librarian bulk retired 2026-06) |
| **Span** | 2022-11-21 → 2026-04-28 (CTF Exchange v1 lifecycle) |
| **Scale** | 1.20B trades · 1.30M markets · ~$61B nominal volume · ~$29B economic (de-relayer) |
| **Read status** | deep-read — abstract, institutional background, stylized facts, fee DiD, calibration benchmarks |

## Narrative

### Thesis (gambling-wiki slice)

First **full-lifecycle** public archive of Polymarket CTF Exchange v1 with **ground-truth aggressor direction** from on-chain settlement — not inferred from tick rule or bulk volume classifiers. Paper benchmarks microstructure tools and links trade-level quality to **forecast calibration** (Brier scores).

**gambling-wiki owns:** dataset access for retail backtests, FLB/calibration takeaways, 2026 fee-reform timeline, warnings on copy-trading flow heuristics.

**@osint-wiki owns:** on-chain OrderFilled pipeline, VPIN/OFI TCA, prod bot data paths.

### Dataset access (retail / research)

| Property | Detail |
|----------|--------|
| Source layer | Polygon CTF Exchange `OrderFilled` events only (no off-chain quote book) |
| Partitions | 42 monthly parquet files |
| Metadata join | 99.8% of trades matched to market/category labels |
| Direction | 100% ground-truth taker side (YES/NO normalized to event-probability axis) |
| Relayer filter | 53% of nominal trades excluded (platform-router artifacts) |
| v1 boundary | Ends 2026-04-28 — v2 migration is separate venue evolution |

Use for **offline** field studies (FLB by category, fee-impact panels, calibration). Live wagering still uses Gamma/CLOB APIs — dataset does not auto-update.

### Favorite-longshot reversal [CONFIRMED — Table 3, 238M+ resolved trades]

Polymarket shows the **opposite sign** of classic horse-racing FLB (Snowberg & Wolfers 2010):

| Price band | Mean return (payout − price) | Interpretation |
|------------|------------------------------|----------------|
| 0.00–0.30 | **Negative** (−0.0023 to −0.0005) | Longshots **overpriced** |
| 0.40–1.00 | **Positive** (+0.0015 to +0.0098) | Favorites **underpriced** |

Paper labels this **"favorite-longshot reversal"** — retail systematically overestimates tail outcomes. See `@concepts/favorite-longshot-bias.md`.

### Fee reform 2026 [CONFIRMED — Table 7, on-chain fee revenue panel]

Staggered category activation (DiD identification):

| Category | Activation |
|----------|------------|
| Crypto | 2026-01 |
| Sports (selected leagues) | 2026-02 |
| Politics, News, Entertainment, others | 2026-03 |

Fee revenue was **zero before Jan 2026** on v1 tape. Post-reform descriptive pattern: taker-fee tax associates with **noise-trader flight** (higher true VPIN among remaining flow), **wider Gibbs spreads**, and **lower wash-trading share** [TENTATIVE — DiD pre-trend caveats on VPIN/Amihud; wash share more defensible].

Aligns with SI.com retail fee summaries already on `@entities/platforms/polymarket.md` — this paper **confirms on-chain activation dates**.

### Category quality (Sports retail lens)

Standard Binary sub-sample (Table 4): **Sports** median Gibbs spread **0.016** vs **Crypto 0.007** — sports books are wider on this panel. Sports = 483k markets (largest category count). Esports/Tennis rank worst on spread heatmap (Figure 9).

### Copy-trading / flow-signal warning [CONFIRMED]

Tick rule and bulk volume classifiers achieve **49.83%** and **50.51%** aggregate accuracy vs ground truth — near coin-flip. Inferred VPIN/OFI diverge from true measures. **Retail products that infer buy/sell from public tape without on-chain join should not be treated as informed-flow signals.**

Participant concentration: top **1%** of makers = **84.1%** of maker volume; top **1%** of takers = **69.7%** of taker volume — whale-copy strategies chase a thin elite.

### Calibration selection effect [CONFIRMED]

- **True VPIN ↑ → Brier score ↑** (worse forecasts) — toxic flow degrades calibration
- **Gibbs spread ↑ → Brier score ↓** — high-spread niche markets attract informed specialists, not noise
- Classified (inferred) proxies **attenuate** both relationships — measurement error matters for any retail "market quality" heuristic

### Retail vs prod split

| Layer | Home |
|-------|------|
| HuggingFace download, FLB tables, fee timeline, copy-trade warnings | **gambling-wiki** |
| On-chain harvester, VPIN TCA, Cemini Layer-1 ingest | **@osint-wiki** |

## Snippets

> "Its defining feature is all ground-truth aggressor direction derived from the blockchain settlement layer."

> "The tick rule and bulk volume classification achieve near-random aggregate accuracy (49.83% and 50.51%)."

> "Low-probability tokens exhibit negative realized returns (systematic overpricing), while high-probability tokens exhibit positive returns (underpricing). This is the reverse of the classic longshot bias in betting markets."

> "Markets with higher toxic order flow (True VPIN) exhibit systematically higher forecasting errors (Brier scores). Counterintuitively, markets with wider spreads exhibit lower forecast errors."

> — [Source: arxiv-2606.04217-polymarket-v1-database.pdf, retrieved 2026-06-05]

## Dead Ends

- **Not** a live trading feed — frozen v1 tape; v2 architecture is post-sample
- **Not** a substitute for reading current Polymarket fee schedule UI — use platform docs for exact taker curves at your price point
- Full HF dataset mirror — laptop `raw-sources/` or HuggingFace only; cemini-librarian bulk retired 2026-06
- DiD t-statistics on some liquidity metrics likely under-clustered — treat magnitudes as directional, not precise causal calibration
