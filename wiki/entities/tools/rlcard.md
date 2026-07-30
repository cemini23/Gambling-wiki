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
  - entities/tools/pokerskill.md
  - entities/bots/wagerbrain.md
  - entities/bots/README.md
  - concepts/opponent-modeling-imperfect-info.md
  - sources/brief-k130-rlcard-offline-baseline-adopt-2026-06-26.md
  - entities/tools/adversarial-coevolution.md
  - sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md
  - sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md
  - entities/tools/code-world-models.md
  - sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md
  - sources/brief-k164-ccs-mccfr-chance-sampling-steals-2026-07-30.md
maturity: validated
created: 2026-06-01
updated: 2026-07-30
laptop_install: VERIFIED 2026-06-01 — OSINT `.local/venv-gambling-research` (rlcard 1.2.0); run `gambling_research_venv.sh` in OSINT repo
phase_0_verdict: ADOPT 2026-06-26 — K130 refresh; MIT; offline Leduc/limit-HU baselines only
---

## Relations

- @concepts/poker-strategy-overview.md — poker research lane
- @concepts/opponent-modeling-imperfect-info.md — sim research for opponent modeling
- @sources/brief-k130-rlcard-offline-baseline-adopt-2026-06-26.md — K130 Adopt reaffirmation
- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 Adopt (Cemini financial in eval; gambling = sim research)
- @entities/tools/code-world-models.md — K158 play-adequacy CWM (Kuhn/Leduc inference sibling)
- @sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md — verified-vs-correct gap on imperfect-info CWMs
- @sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md — CCS-MCCFR Kuhn/Leduc exploitability cuts (K164)
- @sources/brief-k164-ccs-mccfr-chance-sampling-steals-2026-07-30.md — K164 steals

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
| Maturity | 3508★ / 749 forks / 80 open issues (K130 refresh 2026-06-26) |
| Activity | Last push **2024-06-26** (maintained, not daily) |
| Fit | Poker-bot **research** and policy eval — aligns with casino/poker dead-end vs sportsbook split |
| Cemini prod | **NO** default prod adopt — use for offline sim only unless explicit poker-bot workstream |

**Verdict: ADOPT** (K130 2026-06-26) — laptop research installs OK; Leduc/limit-HU offline baselines; no prod deploy without separate brief.

### Adoption status [ADOPTED 2026-06-01]

Isolated venv on OSINT laptop: `bash scripts/gambling_research_venv.sh` (from OSINT workspace). Activate: `.local/venv-gambling-research/bin/activate`. Poker-bot fleet specs reference this for offline policy eval only.

## Snippets

> K92 v7 Adopt — rlcard for RL card environments. [Source: @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
