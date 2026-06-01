---
title: RLCard (datamllab) — poker RL environments
type: entity
tags: [entity, tool, poker, reinforcement-learning, research]
keywords: [rlcard, poker, rl, simulation, k92]
related:
  - concepts/poker-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - entities/bots/poker-bot-tooling.md
  - entities/bots/wagerbrain.md
  - entities/bots/README.md
maturity: validated
created: 2026-06-01
updated: 2026-06-01
laptop_install: VERIFIED 2026-06-01 — OSINT `.local/venv-gambling-research` (rlcard 1.2.0); run `gambling_research_venv.sh` in OSINT repo
---

## Relations

- @concepts/poker-strategy-overview.md — poker research lane
- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 Adopt (Cemini financial in eval; gambling = sim research)

## Raw Concept

- **Repo**: `github.com/datamllab/rlcard`
- **K92 tier**: Adopt (eval) — **gambling-wiki** owns poker **simulation** use; prod trading stack on @osint-wiki if ever needed

## Narrative

Open-source **card-game RL toolkit** (poker, blackjack, etc.) for research and bot prototyping — not a sportsbook/PM execution engine.

### Phase-0 audit (2026-06-01)

Clone: `/tmp/k92-phase0/rlcard`

| Check | Result |
|-------|--------|
| License | **MIT** |
| Maturity | 3481★ / 744 forks / 80 open issues |
| Activity | Last push **2024-06-26** (maintained, not daily) |
| Fit | Poker-bot **research** and policy eval — aligns with casino/poker dead-end vs sportsbook split |
| Cemini prod | **NO** default prod adopt — use for offline sim only unless explicit poker-bot workstream |

**Verdict: CONDITIONAL-GO** — laptop research installs OK; document env deps; no prod deploy without separate brief.

### Adoption status [ADOPTED 2026-06-01]

Isolated venv on OSINT laptop: `bash scripts/gambling_research_venv.sh` (from OSINT workspace). Activate: `.local/venv-gambling-research/bin/activate`. Poker-bot fleet specs reference this for offline policy eval only.

## Snippets

> K92 v7 Adopt — rlcard for RL card environments. [Source: @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
