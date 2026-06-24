---
title: IRumAI — reinforcement learning for Indian Rummy (arXiv 2606.21975)
type: source
tags: [source, arxiv, casino, rummy, reinforcement-learning, k127]
keywords: [irumai, indian rummy, ppo, meld-validity, deadwood, card-game-ai, cog-2026]
related:
  - entities/games/indian-rummy.md
  - entities/bots/poker-bot-tooling.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/gambling-bot-architecture.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
  - sources/daily-digest-reject-cluster-k127-2026-06-24.md
  - sweeps/2026-06-24-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-24
updated: 2026-06-24
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.21975-pdf-reinforcement-learning-for-indian-rummy-irum.pdf
phase_0_verdict: REFERENCE 2026-06-24 — no public repo; research-only until IEEE CoG release
---

## Relations

- @entities/games/indian-rummy.md — game entity (meld-validity card game)
- @sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md — operator steal summary (K127)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.21975](https://arxiv.org/abs/2606.21975) |
| **Title** | IRumAI: Reinforcement Learning for Indian Rummy |
| **Venue** | IEEE Conference on Games (CoG) 2026 (to appear) |
| **Phase-0** | No public GitHub at ingest; `gh api` search empty |
| **Verdict** | **REFERENCE** — casino card-game RL benchmark; not live botting |

## Narrative

Indian Rummy has hundreds of millions of players but **no prior RL agents** in literature. IRumAI is the first: PPO with meld-aware observation encoding, deadwood-driven reward shaping, and a dual-branch convolutional architecture. Training uses behaviour-cloning warm-start on stronger demos, then RL **only against weak heuristics** — yet generalizes to **53.9% win rate** vs the strongest search-based baseline unseen in RL training.

### Why this differs from poker (NLHE)

| Dimension | Indian Rummy | Texas Hold'em |
|-----------|--------------|---------------|
| Hand value | **Binary meld validity** — worthless until 13 cards partition into sequences/sets | Continuous strength spectrum on any 2-hole + board |
| State space | Wildcard rewrites values each deal; deal space > 7×10²² | Smaller per-street branching with fixed ranks |
| Inference | **0.33 ms/action** (no explicit search) | CFR / search hybrids dominate research baselines |
| Opponent read | Discard-pile blocking + meld inference | Betting + board texture |

Linear probing shows the network **implicitly models opponent hidden cards** from public interactions — parallel to HUD + line-based range reads in poker.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Casino card-game bot research** | REFERENCE — meld-constraint games as imperfect-info benchmark |
| **Poker arena (dev.fun)** | Analog only — fast policy inference without search; opponent-hand probing |
| **Live online rummy botting** | **NO-GO** — real-money ToS / collusion dead end (same as poker-bot-tooling posture) |

## Snippets

> "IRumAI requires just 0.33 ms per action, which is over 7,000× faster than the state-of-the-art heuristic." [Source: arxiv:2606.21975 abstract]

> "Linear probing reveals that the network implicitly models the opponent's hidden hand from public interactions." [Source: arxiv:2606.21975 abstract]

## Dead Ends

- **Port IRumAI architecture to NLHE `decide()`** — different action space and payoff structure
- **Deploy on real-money Indian Rummy sites** — ToS / regulatory dead end
- **Adopt without code release** — paper-only at Phase-0
