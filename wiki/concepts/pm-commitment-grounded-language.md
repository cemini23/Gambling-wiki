---
title: Prediction-market commitment-grounded language (StakeBench)
type: concept
tags: [concept, prediction-markets, polymarket, nlp, retail]
keywords: [stakebench, commitment, revealed-preference, polymarket, manifold]
related:
  - concepts/prediction-markets-crossover.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/pm-perspective-mismatch-trading.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @entities/platforms/polymarket.md — primary StakeBench corpus (514k comments)
- @concepts/pm-copy-trading-retail-risks.md — whale-copy vs reading **commitment**

## Raw Concept

**StakeBench** (Pei et al. 2026): benchmark linking PM/Manifold **comments** to **verified positions**, post-comment **actions**, and **odds trajectories** — supervision from revealed market behavior, not crowd sentiment labels.

## Narrative

### Problem for retail + research

Twitter/Reddit **sentiment** on PM markets often misreads posters who hold YES/NO stakes. StakeBench tests whether LLMs recover:

| Task | Question |
|------|----------|
| G1 | Does commenter hold a position? |
| G2 | Which side (YES/NO)? |
| G3 | Next action (flip/increase/decrease/hold)? |
| G4 | Collective odds direction vs stake-weighted baseline? |

### Key results [CONFIRMED abstract]

- **560,876** comments, **2,261** resolved markets (Polymarket + Manifold).
- G2 **Directed Accuracy** ~0.51–0.60 across 15 LLMs — partial side recovery.
- **10/15 models** collapse to 1–2 action labels on G3.
- **No model** consistently beats naive odds-direction baseline on G4.
- **Scale ≠ performance**; finance-tuned models do not dominate.

### Retail implications

1. **Do not trust text-only PM alpha** — position size and trade history matter more than bullish thread tone.
2. **Copy-trading risk** — speakers may advocate against their book for engagement; StakeBench formalizes “commitment vs perception.”
3. **Cross-venue** — Polymarket has stronger **monetary commitment** signal; Manifold denser position coverage — platform incentives shape tasks.

### Bot / OSINT routing

Dataset + eval code **CC-BY 4.0** — useful for **PM comment classifiers** on @osint-wiki; retail discipline stays here.

## Snippets

> "Supervision is derived from observable market behavior… replacing perception-based labels with observable commitment signals." [Source: arxiv-2605.26074]

> "Polymarket offers stronger monetary commitment signals, while Manifold provides broader position coverage." [Source: same]
