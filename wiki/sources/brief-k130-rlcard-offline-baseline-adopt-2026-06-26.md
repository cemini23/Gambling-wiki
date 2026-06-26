---
title: K130 — RLCard offline baseline Adopt
type: source
tags: [source, brief, poker, rl, rlcard, k130, phase-0]
keywords: [rlcard, leduc, limit-hu, offline-baseline, mit, adopt]
related:
  - entities/tools/rlcard.md
  - entities/bots/poker-bot-tooling.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
maturity: validated
read_status: deep-read
created: 2026-06-26
updated: 2026-06-26
cross-wiki-source: "briefs/2026-06-26_k130-rlcard-offline-baseline-adopt.md"
---

## Relations

- @entities/tools/rlcard.md — primary entity (K92 + K130 refresh)
- @entities/bots/poker-bot-tooling.md — poker RL baseline cluster
- @osint-wiki/sources/eval-poker-github-repos-2026-06-26.md — OSINT eval lane [NEEDS VERIFICATION 2026-06-26]

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K130 RLCard offline baseline Adopt |
| **Date** | 2026-06-26 |
| **Phase-0** | MIT · 3508★ · last push 2024-06-26 · `gh api` 2026-06-26 |
| **Verdict** | **ADOPT** — offline card-game RL baselines only |

## Narrative

K130 OSINT ingest reaffirms **RLCard** (`datamllab/rlcard`) as the gambling-wiki **Adopt** lane for offline poker/card-game RL baselines — not live botting.

### Operator actions

| Action | Detail |
|--------|--------|
| **Venv** | OSINT `.local/venv-gambling-research` via `scripts/gambling_research_venv.sh` |
| **Use cases** | Leduc / limit-HU policy baselines; opponent-modeling sims |
| **Boundary** | Offline research only — no prod `decide()` or real-money sites |
| **Cross-wiki** | OSINT `@entities/tools/rlcard.md` stub links here as domain owner |

### vs dev.fun arena

RLCard baselines complement but do **not replace** arena-pokerkit regression gates (K102/K118). Use for Leduc/limit-HU sanity checks before NLHE HU fork work.

## Dead Ends

- RLCard policy as Playground lobby bot
- Live online poker automation via RLCard env wrappers
