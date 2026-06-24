---
title: Equilibrium with internal transfers — SETE and M-SETE (arXiv 2606.20960)
type: source
tags: [source, arxiv, game-theory, poker, equilibrium, k127, farina]
keywords: [sete, m-sete, internal-transfers, nash, polymatrix, social-welfare, farina, mediated-equilibrium]
related:
  - sources/arxiv-2606.16139-team-zero-sum-games-complexity-2026-06-20.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - concepts/opponent-modeling-imperfect-info.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
  - sources/daily-digest-reject-cluster-k127-2026-06-24.md
  - sweeps/2026-06-24-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-24
updated: 2026-06-24
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.20960-2606-20960v1-equilibrium-with-internal-transfers.pdf
phase_0_verdict: REFERENCE 2026-06-24 — theoretical; EC 2026; no wagering implementation
---

## Relations

- @sources/arxiv-2606.16139-team-zero-sum-games-complexity-2026-06-20.md — team / multi-agent equilibrium complexity
- @sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md — game-theory steal note (K127)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.20960](https://arxiv.org/abs/2606.20960) |
| **Title** | Equilibrium with Internal Transfers |
| **Authors** | Liu, **Farina**, Ozdaglar (MIT LIDS) |
| **Venue** | ACM EC 2026 (accepted) |
| **Verdict** | **REFERENCE** — transfer-augmented equilibrium concepts |

## Narrative

Nash equilibrium can have arbitrarily poor social welfare and is hard to compute. This paper studies **budget-balanced internal transfers** among players before play to improve incentives.

### Solution concepts

| Concept | Mechanism | Property |
|---------|-----------|----------|
| **SETE** (Self-Enforcing Transfer Equilibrium) | Peer-to-peer transfers paid only if recipient does not deviate | Polymatrix: any socially optimal profile sustainable; poly-time algorithm + decentralized learning |
| **M-SETE** (Mediated SETE) | Mediator makes payment schedule + strategies **binding** | True NE of augmented game; any finite game can support socially optimal M-SETE |

Unlike correlated equilibrium (requires mediator sampling + trust), SETE preserves **independent play on the equilibrium path** while improving welfare.

### Gambling-wiki hook

| Application | Fit |
|-------------|-----|
| **Multi-way poker soft-play / chip-dumping** | Conceptual — side payments before hands mirror transfer-augmented games (enforcement differs) |
| **Arena bot design** | Low — no NLHE eval; Farina poker literature cross-ref only |
| **PM / sportsbook** | Out of scope |

Farina co-authorship places this in the same research orbit as poker equilibrium computation (Libratus / CFR line) — useful vocabulary for **collusion detection** and welfare analysis, not a deployable bot technique.

## Snippets

> "Internal transfers improve welfare and computation while preserving independent play on the equilibrium path." [Source: arxiv:2606.20960 abstract]

> "For polymatrix games, every stationary point of the social welfare function can be sustained as a SETE." [Source: arxiv:2606.20960 abstract]

## Dead Ends

- **Implement SETE in `cemini_decide()`** — cooperative transfer design, not NLHE action selection
- **Use M-SETE as dev.fun arena strategy** — requires binding mediator; not venue mechanic
