---
title: Policy representation SSL in two-player zero-sum imperfect-info games (arXiv 2607.01498)
type: source
tags: [source, arxiv, poker, opponent-modeling, game-theory, k149, ssl]
keywords: [policy-embedding, kuhn-poker, leduc-poker, self-supervised, depth-limited-search]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/tools/rlcard.md
  - sources/brief-k130-rlcard-offline-baseline-adopt-2026-06-26.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - sources/brief-k149-policy-ssl-advent-poker-steals-2026-07-07.md
  - sources/daily-digest-batch-k149-2026-07-07.md
  - sweeps/2026-07-07-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-07
updated: 2026-07-07
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.01498-towards-learning-representations-of-policies-in.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-07 — github.com/VitamintK/ssl-project (0★, no LICENSE file); Kuhn/Leduc research reference only
---

## Relations

- @entities/tools/rlcard.md — Leduc/Kuhn baseline env (K130)
- @sources/brief-k149-policy-ssl-advent-poker-steals-2026-07-07.md — K149 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.01498](https://arxiv.org/abs/2607.01498) |
| **Venue** | NExT-Game @ ICML 2026 workshop |
| **Repo** | [github.com/VitamintK/ssl-project](https://github.com/VitamintK/ssl-project) |
| **Phase-0** | **No SPDX license** on repo (gh api 2026-07-07); 0★ |
| **Verdict** | **CONDITIONAL-GO** — systematic policy-embedding benchmark on Kuhn/Leduc |

## Narrative

First systematic comparison of **self-supervised policy representations** in **2p zero-sum imperfect-information** games. Three parts: (1) policy dataset construction methods, (2) embedding learners, (3) downstream tasks (decode-to-policy, payoff prediction).

Evaluated on **Kuhn** and **Leduc** poker — shows basic SSL captures useful behavioral structure despite simple methods.

| Lane | Fit |
|------|-----|
| **Opponent modeling research** | **HIGH** — compact policy embeddings for depth-limited search / clustering opponent types |
| **Arena HU sandbox** | **MEDIUM** — toy-game methodology before NLHE; pairs RLCard Leduc baselines |
| **Prod `decide()`** | NO-GO — workshop research; no license |

**Adoption for David:** use as **methodology reference** when building opponent-policy feature sets on Leduc regression — verify repo license before any code fork.

## Snippets

> "In games with larger public belief states, such a policy becomes intractable to enumerate. Thus … an agent will need to reason with compact representations of policies." [Source: arxiv:2607.01498 §1]

## Dead Ends

- Kuhn embedding cosine similarity as Playground TrueSkill proxy
- ssl-project install without LICENSE audit
