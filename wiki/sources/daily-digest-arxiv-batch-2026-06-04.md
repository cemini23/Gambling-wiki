---
title: Daily digest arXiv batch (2026-06-04 sweep)
type: source
tags: [source, arxiv, daily-digest, poker, marl, dead-end]
keywords: [2605.30854, 2605.17623, SEPO, Kuhn poker, exploitability, D-Wave, dead-end]
related:
  - meta/daily-research-digest-cadence.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - entities/bots/poker-bot-tooling.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/tools/pokerskill.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sweeps/2026-06-04-daily.md
maturity: validated
read_status: read
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @sweeps/2026-06-04-daily.md — nightly discovery (`daily_research_digest_run.py`)
- @sources/daily-digest-arxiv-batch-2026-06-02.md — prior digest batch (GIMARL, replicability PM)

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-06-04 |
| **Origin** | `research to be indexed/` via PM digest |
| **Papers** | 2 NEW |

| arXiv | Title | sha256 (prefix) | Verdict |
|-------|-------|-----------------|---------|
| 2605.30854 | Safe Equilibrium Policy Optimization for Strategic Agent Policies | 359d1eee143e9aa6 | **Ingest** — Kuhn poker + exploitability training |
| 2605.17623 | Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization | c42d63912bf869de | **Dead end** — quant portfolio, not wagering |

## Narrative

Fourth gambling-wiki digest fetch (2026-06-04 sweep). One paper is **research-lane poker/LLM strategy** (SEPO); one is **out of scope** (D-Wave portfolio audit — route quant finance to `@osint-wiki` if needed).

### 2605.30854 — Safe Equilibrium Policy Optimization (SEPO) [TENTATIVE — research]

**Arumugam, Manku, Dhanda (Amazon)** — RL training objective for **language-model game agents** that augments task payoff with penalties for **exploitability**, **collusion risk**, and **externality cost**:

$$J_{\text{SEPO}}(\pi) = u(\pi) - \lambda_e \cdot e(\pi) - \lambda_c \cdot c(\pi) - \lambda_x \cdot x(\pi)$$

| Takeaway | Gambling-wiki relevance |
|----------|-------------------------|
| Evaluated on IPD, auctions, negotiation, **Kuhn Poker** (6-hand, 3-card) | Direct imperfect-info poker benchmark for LLM agents |
| SEPO achieves **zero exploit-pool advantage** in Kuhn Poker (both Gemma 4 and Qwen 3.5-4B at best checkpoint) — converges toward Nash mixed strategy | Complements `@concepts/opponent-modeling-imperfect-info.md` exploit-resistance lane |
| SFT warm-start **degrades** exploit resistance; SEPO corrects it | Design note for `@entities/tools/pokerskill.md` / `@entities/bots/cemini-devfun-poker-agent.md` training stacks |
| **Per-rollout** exploit computation required — constant penalty cancels in GRPO advantage normalization (zero gradient) | Implementation pitfall for arena bot RL loops |
| Code + SFT datasets released | Research reference only — not prod dev.fun path |

**Action:** Research note on `@entities/bots/poker-bot-tooling.md`; cross-ref opponent modeling + PokerSkill. No prod bot changes.

### 2605.17623 — D-Wave hybrid portfolio optimization audit [DEAD END — wagering]

**Lozano (EGADE)** — operational decomposition audit of D-Wave LeapHybridCQM vs classical Gurobi on cardinality-constrained mean-variance-turnover portfolios.

| Takeaway | Gambling-wiki relevance |
|----------|-------------------------|
| QPU access ≈0.68% of hybrid wall-clock; wins are constraint-native classical pipelines | Quant finance / portfolio optimization |
| Out-of-sample Sharpe 1.94 (QPU-selected) vs 2.22 for 1/N baseline | No sports betting, poker, PM retail, or casino edge |
| JEL G11; C61; C63 — asset allocation literature | **Do not route** to betting strategy pages |

**Action:** Archive PDF; no new concept page. Cross-wiki only if operator wants `@osint-wiki` quant note.

## Snippets

> "SEPO achieves zero exploit-pool advantage in Kuhn Poker for both models, converging to the Nash mixed strategy against the adversaries in our pool." [Source: arxiv-2605.30854, abstract]

> "A constant exploit penalty cancels in SEPO's advantage normalization and produces zero gradient — a consequence of the standard constant control-variate property." [Source: arxiv-2605.30854, §3]

> "The practical implication is that reported D-Wave hybrid wins on this problem class are constraint-native classical pipelines, not quantum-sampling wins." [Source: arxiv-2605.17623, abstract]

## Dead Ends

- **2605.17623** — portfolio optimization benchmarking; not gambling, sports betting, or PM retail.
- **2605.30854** — no direct path to +EV sportsbook or live NLHE deployment; sim/research + Kuhn poker only.
