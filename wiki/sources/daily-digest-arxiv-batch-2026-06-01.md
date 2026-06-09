---
title: Daily digest arXiv batch — 2026-06-01 (4 papers)
type: source
tags: [source, arxiv, daily-digest, sports-betting, poker, prediction-markets]
keywords: [match-fixing, live-betting, pokerskill, stakebench, big-2, rl]
related:
  - meta/daily-research-digest-cadence.md
  - concepts/live-betting-match-integrity.md
  - concepts/pm-commitment-grounded-language.md
  - entities/tools/pokerskill.md
  - concepts/poker-strategy-overview.md
  - entities/bots/poker-bot-tooling.md
  - entities/platforms/polymarket.md
  - concepts/sports-betting-fundamentals.md
  - entities/games/poker.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - concepts/opponent-modeling-imperfect-info.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
maturity: validated
created: 2026-06-01
updated: 2026-06-09
---

## Relations

- @meta/daily-research-digest-cadence.md — federated digest provenance
- @concepts/opponent-modeling-imperfect-info.md — PokerSkill / sim research cross-ref
- @sweeps/2026-06-01-daily.md — morning sweep that fetched these PDFs

## Raw Concept

| Field | Value |
|-------|-------|
| **Origin** | `research to be indexed/` via `daily_research_digest_run.py` |
| **Retrieved** | 2026-06-01 |
| **Papers** | 4 (all NEW per preingest_check) |

| arXiv | Title | sha256 (prefix) |
|-------|-------|-----------------|
| 2605.30209 | Betting Against Integrity (match-fixing, live betting) | `a5ab76326c56…` |
| 2605.30094 | PokerSkill (LLM + rule skills, HUNL) | `954caa1b668c…` |
| 2605.26074 | StakeBench (PM/Manifold commitment NLP) | `19d5bdd83942…` |
| 2605.28863 | Self-play RL in Big 2 | `8030124f2c0f…` |

## Narrative

First **full ingest** from gambling-wiki daily digest. Four arXiv papers spanning **live-betting integrity**, **poker LLM agents**, **PM commitment benchmarks**, and **imperfect-info RL** (Big 2).

### Retail / wagering takeaways

1. **2605.30209** — Live betting ≈ half of European sports betting volume; fraud detection must use **stakes + odds**, not odds alone. Serie B proof-of-concept; ties to FLB literature and Sportradar UFDS. [CONFIRMED abstract]
2. **2605.30094** — **PokerSkill** (MIT-ish open repo): expert rule library + LLM = competitive HUNL vs GTOWizard **without CFR/solver**. Retail lesson: LLM “knows poker” but needs structured skill grounding — parallels bot **signal→action** design. [CONFIRMED]
3. **2605.26074** — **StakeBench**: Polymarket + Manifold comments linked to **verified positions**; sentiment benchmarks miss **revealed commitment**. Weak LLMs on action/odds tasks. [CONFIRMED]
4. **2605.28863** — Big 2 PPO > value methods under budget; **research lane only** for gambling-wiki (not live poker product). [CONFIRMED]

### Routing

- Match integrity → `@concepts/live-betting-match-integrity.md`
- StakeBench → `@concepts/pm-commitment-grounded-language.md`, `@entities/platforms/polymarket.md`
- PokerSkill → `@entities/tools/pokerskill.md`, `@concepts/poker-strategy-overview.md`
- Big 2 → note on `@entities/bots/poker-bot-tooling.md` only

### Not ingested from sweep news rows

Digest listed Kalshi/PM retail URLs (R1–R3), +EV articles (R4–R6), WC futures (R7–R9), DFS BBM (R10–R12) — ingested `@sources/daily-digest-news-r1-r12-2026-06-01.md`.

## Snippets

> "Including betting volumes can enhance model accuracy, as high liquidity can stabilise odds and conceal manipulation." [Source: arxiv-2605.30209, Winkelmann et al.]

> "PokerSkill reduces losses by 49–61% compared to default-prompt baselines and outperforming the strong bot Slumbot." [Source: arxiv-2605.30094, Li et al.]

> "Existing financial NLP benchmarks… measuring how language is perceived rather than what speakers have committed to in the market." [Source: arxiv-2605.26074, Pei et al.]

## Dead Ends

- **Big 2 RL** — academic sim; no retail sportsbook/PM edge path
- **PolyGnosis 2.0** (2605.25958) — ingested `@sources/polygnosis-2-polymarket-osint-2026-06-01.md`
