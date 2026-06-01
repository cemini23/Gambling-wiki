---
title: PM perspective mismatch (Polymarket vs global media)
type: concept
tags: [concept, prediction-markets, polymarket, osint, retail]
keywords: [perspective-mismatch, polygnosis, gdelt, narrative-divergence, alpha-signal]
related:
  - concepts/pm-commitment-grounded-language.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - concepts/prediction-markets-crossover.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/pm-copy-trading-retail-risks.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/polygnosis-2-polymarket-osint-2026-06-01.md — PolyGnosis 2.0 formalizes the signal
- @concepts/pm-commitment-grounded-language.md — StakeBench: commitment in comments vs sentiment

## Raw Concept

**Perspective mismatch** — Polymarket-implied narrative diverges from **GDELT / global media** flow — proposed as a tradable diagnostic in PolyGnosis 2.0.

## Narrative

### Definition

| Signal | Meaning |
|--------|---------|
| PM trajectory | What priced-in traders + whales imply after anomaly |
| Media trajectory | GDELT sentiment / article volume direction |
| **Mismatch** | Actionable divergence between the two |

PM pool is **endogenous** (localized biases, crypto-native flow). Media is **exogenous** proxy for “rest of world” information.

### Retail discipline

1. **Not copy-trade thread tone** — mismatch research says text and price can disagree with global news.
2. **Cross-check WC/macro/sports** — before sizing PM positions, compare book lines (`@concepts/sportsbook-pm-line-divergence.md`).
3. **Latency** — media/GDELT slower than PM; not HFT-safe.

### vs StakeBench

| Lens | StakeBench | PolyGnosis |
|------|------------|------------|
| Unit | Comment + verified position | Anomaly alert + GDELT cluster |
| Question | What did speaker commit? | Does PM narrative match media? |

Complementary — both argue **perception-only NLP fails** on PM.

### Bot routing

Harness implementation → **@osint-wiki**. Requirements and failure modes documented here.

## Snippets

> "Relying solely on endogenous data lacks the external context necessary to evaluate the true validity of market sentiment." [Source: @sources/polygnosis-2-polymarket-osint-2026-06-01.md]
