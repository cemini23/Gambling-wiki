---
title: Poker bot tooling (rlcard, poker_ai, pokerstove cluster)
type: entity
tags: [entity, bot, poker, research, steal-from, k92]
keywords: [rlcard, poker_ai, pokerstove, dickreuter-poker, pypokerengine, k92]
related:
  - concepts/poker-strategy-overview.md
  - entities/games/poker.md
  - entities/bots/README.md
  - concepts/gambling-bot-architecture.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - entities/tools/pokerskill.md
  - entities/tools/rlcard.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - osint-wiki/entities/tools/poker-query-language.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-02.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/daily-digest-arxiv-batch-2026-06-04.md
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sources/brief-k107-poker-open-spot-audit-2026-06-09.md
  - sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md
maturity: draft
created: 2026-06-01
updated: 2026-06-19
---

## Relations

- @concepts/poker-strategy-overview.md — human strategy context
- @concepts/opponent-modeling-imperfect-info.md — rlcard / sim lane for COM research
- @concepts/poker-hl-analyst-loop.md — arena regression + HL tooling
- @entities/games/poker.md — game entity
- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 eval cluster
- @sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md — K103 poker/casino reject strip
- @entities/tools/devfun-poker-arena-starter-kit.md — K102 Arena entry (MIT arena-pokerkit)

## Raw Concept

K92 eval **poker engine / RL** cluster — **research and evaluation** lane for future poker bots, not live online poker botting (collusion/ToS dead end on real-money sites). K103 adds a **reject cluster** for immature/no-license poker playgrounds — document only, no adoption.

## Narrative

### Repos (K92 tiers)

| Repo | Tier | Notes |
|------|------|-------|
| datamllab/rlcard | **Adopt** (research) | RL environments for poker variants |
| dickreuter/Poker | Steal-from | Bot framework |
| andrewprock/pokerstove | Steal-from | Equity calculator |
| fedden/poker_ai | Steal-from | Deep CFR / research |
| ishikota/PyPokerEngine | Defer | Engine |

### K103 reject cluster (2026-06-07) [CONFIRMED — Phase-0]

| Repo | Eval tier | K103 verdict | Notes |
|------|-----------|--------------|-------|
| solve-poker/Poker-Query-Language | Steal-from | **NO-GO** | ~4★ WIP; immature query language — stub only `@osint-wiki/entities/tools/poker-query-language.md` |
| ToNiePiter/casinogame | Reject | **Reject** | No license |
| alfredzimmer/poker-equity-playground | Reject | **Reject** | Playground only; no license |

**Action:** wiki reference / cross-wiki stub only. No laptop venv install, no prod gambling bot brief, no WC bot adoption from this cluster. Arena path remains `@entities/tools/devfun-poker-arena-starter-kit.md` (K102 MIT).

### Daily digest note (2026-06-01)

**Big 2** self-play RL (arxiv:2605.28863): PPO beats value methods in 4-player imperfect-info card game — **research sim only**, not online poker. Complements **rlcard** (poker variants) and **PokerSkill** (LLM + skills, `@entities/tools/pokerskill.md`).

**GIMARL** (arxiv:2605.31318, 2026-06-02 digest): **Generalized Intention Modeling** — mixture of task-specific opponent intent embeddings; one head maximizes MI with ego **returns**. [TENTATIVE] Useful design pattern for **sim bots** and Arena-style opponent modeling; benchmarks are general MARL, not NLHE. See `@sources/daily-digest-arxiv-batch-2026-06-02.md`.

**SEPO** (arxiv:2605.30854, 2026-06-04 digest): **Safe Equilibrium Policy Optimization** — GRPO reward = payoff minus exploitability / collusion / externality penalties. Achieves **zero exploit-pool advantage** on **Kuhn Poker** (Gemma 4, Qwen 3.5-4B); SFT alone worsens exploit resistance. Critical implementation detail: exploit penalty must be computed **per rollout** (constant penalty cancels in advantage normalization → zero gradient). [TENTATIVE] Research lane for LLM poker agents; complements PokerSkill (skills + LLM) and Ganzfried opponent modeling. See `@sources/daily-digest-arxiv-batch-2026-06-04.md`.

### Gambling-bot program fit

- **Study / sim bots** — equity, ICM drills, bot-vs-bot sim
- **Not** for deploying against real-money online poker (`@sources/youtube-operator-batch-casino-2026-05-31.md` collusion awareness)

### Verdict

**REFERENCE / RESEARCH** — strip-mine math; **NO-GO** for live account automation without explicit operator scope + legal review.

## Snippets

> K92: rlcard Adopt for poker RL environments; poker_ai / pokerstove Steal-from. [Source: @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
