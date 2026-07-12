---
title: Policy improvement with style-specific demonstrations — MPPO (arXiv 2506.16995)
type: source
tags: [source, arxiv, poker, blackjack, rl, opponent-modeling, k153, mppo]
keywords: [mppo, style-preserving, learning-from-demonstration, blackjack, mahjong, d-policy]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/games/blackjack.md
  - entities/tools/mppo.md
  - sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md
  - sources/brief-k153-mppo-style-pm-evidence-steals-2026-07-12.md
  - sources/daily-digest-batch-k153-2026-07-12.md
  - sweeps/2026-07-12-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-12
updated: 2026-07-12
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2506.16995-policy-improvement-with-style-specific-demonstra.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-12 — github.com/AMysteriousBeing/MPPO (1★, no LICENSE); style-preserving LfD reference
---

## Relations

- @entities/tools/mppo.md — Phase-0 entity
- @sources/brief-k153-mppo-style-pm-evidence-steals-2026-07-12.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2506.16995](https://arxiv.org/abs/2506.16995) |
| **Repo** | [github.com/AMysteriousBeing/MPPO](https://github.com/AMysteriousBeing/MPPO) |
| **Phase-0** | **No LICENSE** (gh api 2026-07-12); 1★ |
| **Verdict** | **CONDITIONAL-GO** — **Mixed PPO (MPPO)** improves suboptimal stylized agents without erasing style |

## Narrative

**MPPO** mixes online self-play samples with offline **style-specific demonstrations** (β≈0.05) in unified PPO objective — implicit behavior-cloning constraint via sample distribution.

| Env | Gambling-wiki fit |
|-----|-------------------|
| **Blackjack** | **HIGH** — casino game baseline |
| **Mahjong** | LOW — tile game benchmark |
| **Maze** | N/A |

Introduces **D_policy** (total-variation style distance). Stylized suboptimal demonstrators → MPPO agents match/beat pure PPO proficiency while preserving lower D_policy.

| Lane | Fit |
|------|-----|
| **Arena opponent league** | **HIGH** — upgrade stylized pool bots without homogenizing to Nash-ish self-play |
| **NLHE prod** | Research only — pairs K152 yardstick eval |
| **Blackjack bot** | Methods reference only |

**Adoption for David:** when strengthening MAFP/league opponents from stylized archetypes, use **demonstration-mixed RL** to avoid style collapse; track **D_policy** or equivalent when promoting league members.

## Snippets

> "MPPO achieves proficiency levels comparable to, or even superior to, pure online algorithms while preserving demonstrators' play styles." [Source: arxiv:2506.16995 Abstract]

## Dead Ends

- Mahjong Botzone Elo as NLHE sandbox proof
- MPPO repo fork without LICENSE
