---
title: PokerSkill (LLM + expert skill library)
type: entity
tags: [entity, tool, poker, llm, open-source, research]
keywords: [pokerskill, hunl, gto, llm-agent, github-lbn187]
related:
  - concepts/poker-strategy-overview.md
  - entities/bots/poker-bot-tooling.md
  - entities/games/poker.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-04.md
  - concepts/gambling-bot-architecture.md
  - entities/tools/rlcard.md
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - concepts/opponent-modeling-imperfect-info.md
maturity: draft
created: 2026-06-01
updated: 2026-06-04
---

## Relations

- @concepts/poker-strategy-overview.md — human GTO study vs LLM play
- @concepts/opponent-modeling-imperfect-info.md — skill-library vs consistent COM exploit lane
- @entities/bots/poker-bot-tooling.md — CFR/solver lane contrast

## Raw Concept

- **Repo**: https://github.com/lbn187/PokerSkill
- **Paper**: arxiv:2605.30094 (Li, Wang, Huang 2026)
- **Paradigm**: Training-free, solver-free HUNL via **deterministic context engine** + **layered expert skill library** + frontier LLM

## Narrative

### What it does

At each decision: engine labels board texture, hand class, action line, SPR, pressure → retrieves **~60 action-line scenarios**, 23 hand classes, 46 bet-size thresholds from human expert library → LLM picks among **bounded legal actions**.

### Benchmark (vs GTOWizard)

| Agent | mbb/hand vs GTO benchmark |
|-------|---------------------------|
| GPT-5.5 XHigh + PokerSkill | **−57 ± 21** |
| Claude Opus 4.6 + PokerSkill | −80 ± 29 |
| Default-prompt Opus 4.6 | −204 ± 44 |
| Slumbot (strong open bot) | worse than PokerSkill agents |

**49–61% loss reduction** vs default prompting; beats Slumbot without CFR training.

### Phase-0 verdict

| Check | Result |
|-------|--------|
| License | Verify on GitHub before prod use [NEEDS VERIFICATION 2026-06-01] |
| Retail online poker | **NO-GO** — ToS / bot detection; study tool only |
| Gambling-bot program | **REFERENCE** — skill-library + LLM grounding pattern for future **study assistants**, not account automation |

### Design lesson for wiki

**Decision-binding problem**: LLMs know concepts but fail to apply the right one per node — structured retrieval fixes binding. Analog for sportsbook bots: alert → **structured playbook** → LLM triage, not raw “place bet.”

### Related LLM poker training (SEPO) [TENTATIVE]

**SEPO** (arxiv:2605.30854) is an alternative paradigm: RL fine-tune with exploitability / collusion / externality penalties rather than skill-library retrieval. Benchmarks include **Kuhn Poker**; SFT warm-start alone worsens exploit resistance. Complements PokerSkill's training-free approach — see `@sources/daily-digest-arxiv-batch-2026-06-04.md`.

## Snippets

> "Rule-based skills alone do not constitute a strong strategy, and LLMs alone cannot play well, but their combination yields an agent that requires neither training nor solver access." [Source: arxiv-2605.30094 abstract]
