---
title: Poker strategy overview
type: concept
tags: [concept, poker, cash-game, tournament, gto, math]
keywords: [poker, texas-holdem, icm, position, pot-odds, tournament, rake, bots]
related:
  - concepts/bankroll-management.md
  - concepts/casino-game-house-edge.md
  - entities/games/poker.md
  - entities/platforms/pokerstars.md
  - sources/youtube-operator-batch-casino-2026-05-31.md
  - sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md
  - entities/tools/pokerskill.md
  - entities/bots/poker-bot-tooling.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - entities/tools/rlcard.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @entities/games/poker.md — game entity
- @entities/platforms/pokerstars.md — major online room
- @sources/youtube-operator-batch-casino-2026-05-31.md — operator YouTube poker cluster

## Raw Concept

Poker as **skill game** — cash vs MTT, bankroll, math-first decision making, study workflow.

## Narrative

### Cash vs tournament

| | Cash | MTT |
|---|------|-----|
| Stack depth | Fixed rebuy | Shrinking vs field |
| Edge expression | bb/100 | ROI % over large sample |
| Bankroll rule | 20–40 BI | **100+ BI** (200 cautious; ~300 hyper) [Source: yrGExOmDRLk] |
| Key extra skill | Table select | ICM |

### MTT zero → $10k grind (Raise Your Edge) [TENTATIVE]

Creator 10-step path for **online MTTs** [Source: @sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md]:

1. **Variance first** — short-run results ≠ skill; 100-buy-in floor before moving stakes
2. **Preflop literacy** — understand opens by position; don't memorize charts blindly
3. **Micro stakes** — play smallest available even with $500 roll; session review (Hand2Note optional)
4. **Value-first postflop** at low stakes — bet big with strong hands; avoid bluff wars vs stations
5. **ICM** — near money, chip EV is non-linear; study before moving up in buy-in
6. **Mindset** — tilt and "know vs do" gap; river curiosity calls flagged as **gambling behavior**

**Move-up rule:** never promote stake after **one big score** — require large-sample results.

### Core skills (operator batch)

1. **Math** — pot odds, equity, implied odds; "math every pro knows" [Source: QqXzTxxMzjU]
2. **Position** — "Position is to poker what location is to real estate" [Source: zH45e91Nk8E]
3. **Triple threat framework** — position + controlled aggression + fundamentals; win by **fewest mistakes** [Source: zH45e91Nk8E]
4. **Beginner foundations** — starting hand discipline, bet sizing basics [Source: Ix4QxqCtUCs]
5. **MTT survival** — preserve stack early, respect blind escalation [Source: k0tKWIrHpMk]

### Rake as "house edge"

Poker rooms take **rake** from pots — effective -EV drag. Table selection (soft games) and rakeback matter.

### Modern study stack

- Preflop charts → postflop solvers (Pio, GTO Wizard) [entity stubs on ingest]
- Hand review + leak tracking
- Live vs online tempo differences

### Not sports betting

Different variance profile and bankroll math — do not mix bankrolls without tracking (`@concepts/bankroll-management.md`).

## Snippets

> "Position is to poker what location is to real estate." [Source: zH45e91Nk8E via @sources/youtube-operator-batch-casino-2026-05-31.md]

> "ICM means that tournament chips are not worth real money in a linear way." [Source: yrGExOmDRLk via @sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md]

## Dead Ends

- **3+ hour tip compilations** (Galfond `GE8BGWjUDYs`) — link-only; defer deep extract
- **Online bot/collusion** (`CIYODgIqqhU`) — opponent integrity issue, not exploitable edge for retail
- **Casino bot podcasts** — awareness only; no +EV playbook
