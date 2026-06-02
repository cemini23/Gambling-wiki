---
title: Daily digest arXiv batch (2026-06-02 sweep)
type: source
tags: [source, arxiv, daily-digest, prediction-markets, marl]
keywords: [2605.27394, 2605.31318, hybrid-forecasting, opponent-modeling, dead-end]
related:
  - meta/daily-research-digest-cadence.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - concepts/pm-commitment-grounded-language.md
  - entities/bots/poker-bot-tooling.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
maturity: validated
read_status: read
created: 2026-06-02
updated: 2026-06-02
---

## Relations

- @sweeps/2026-06-02-daily.md — morning discovery (`daily_research_digest_run.py`)
- @sources/daily-digest-arxiv-batch-2026-06-01.md — prior digest batch (match-fixing, PokerSkill, Big 2, StakeBench)

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-06-02 |
| **Origin** | `research to be indexed/` via AM digest |
| **Papers** | 2 NEW (4 prior batch papers deduped by fetcher) |

## Narrative

Second gambling-wiki digest fetch. One paper is **out of scope** (scientific replicability markets); one is **research-lane MARL** (opponent intention modeling) with weak but useful tie to poker-bot study stack.

### 2605.27394 — Human-AI hybrid markets for scientific replicability [DEAD END — wagering]

**Chakra Vorti et al.** — hybrid **prediction markets** where algorithmic agents trade alongside humans to forecast whether published findings replicate.

| Takeaway | Gambling-wiki relevance |
|----------|-------------------------|
| Hybrid human+AI markets beat human-only or AI-only baselines on replication forecasts | Illustrates PM **mechanism design**, not sports/PM retail edge |
| Supervision from **observable market behavior** vs sentiment | Conceptual cousin to StakeBench “commitment vs perception” — different domain |
| No sports, event contracts, or consumer wagering | **Do not route** to betting strategy pages |

**Action:** Archive PDF; no new concept page. Cross-ref only: `@concepts/pm-commitment-grounded-language.md` (commitment-grounded supervision theme).

### 2605.31318 — Generalized Intention Modeling in MARL [TENTATIVE — research]

**Odrowaz-Sypniewski et al. (Cambridge)** — task-adaptive mixture of opponent **intent representations**; new embedding maximizes mutual information with ego-agent **future returns**.

| Takeaway | Gambling-wiki relevance |
|----------|-------------------------|
| Intent embeddings are **task-dependent**; single fixed opponent features fail | Informs **poker bot sim** design (theory-of-mind / opponent modeling) |
| Beats SOTA on diverse competitive MARL benchmarks | **Not** Texas hold'em product path — chess/prey-predator style tasks in paper |
| No online poker deployment or ToS discussion | Research lane only → `@entities/bots/poker-bot-tooling.md` |

**Action:** Short research note on poker-bot-tooling; no prod bot changes.

## Snippets

> "We introduce a hybrid prediction market in which algorithmic agents trade alongside human participants to jointly estimate the likelihood that a published scientific finding will be corroborated." [Source: arxiv-2605.27394, abstract]

> "Intentions are often task- and environment-dependent… we learn a performance-driven mixture of multiple intent representations." [Source: arxiv-2605.31318, abstract]

## Dead Ends

- **2605.27394** — academic replication forecasting; not Kalshi/Polymarket retail, not sports betting.
- **31318** — no direct path to +EV sportsbook or PM wagering; sim/research only.
