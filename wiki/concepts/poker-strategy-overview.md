---
title: Poker strategy overview
type: concept
tags: [concept, poker, cash-game, tournament, gto]
keywords: [poker, texas-holdem, icm, gto, solver, bankroll]
related:
  - concepts/bankroll-management.md
  - concepts/casino-game-house-edge.md
  - entities/games/poker.md
  - entities/platforms/pokerstars.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @entities/games/poker.md — game entity
- @entities/platforms/pokerstars.md — major online room
- @concepts/casino-game-house-edge.md — contrast: poker is player-vs-player with rake

## Raw Concept

Poker as skill game — cash vs MTT, bankroll, study workflow (solvers, ranges).

## Narrative

### Cash vs tournament

| | Cash | MTT |
|---|------|-----|
| Stack depth | Fixed rebuy | Shrinking vs field |
| Edge expression | bb/100 | ROI % over large sample |
| Bankroll rule | 20–40 BI | 100+ BI [TENTATIVE] |
| Key extra skill | Table select | ICM |

### Rake as "house edge"

Poker rooms take **rake** from pots — effective -EV drag. Table selection (soft games) and rakeback matter.

### Modern study stack

- Preflop charts → postflop solvers (Pio, GTO Wizard) [entity stubs on ingest]
- Hand review + leak tracking
- Live vs online tempo differences

### Not sports betting

Different variance profile and bankroll math — do not mix bankrolls without tracking (`@concepts/bankroll-management.md`).

## Snippets

*(populate from ingested poker sources)*
