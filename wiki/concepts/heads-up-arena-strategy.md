---
title: Heads-up arena strategy (dev.fun researcher track)
type: concept
tags: [concept, poker, heads-up, devfun, researcher-track, trueskill, k122]
keywords: [hu-nlhe, button-open, 3-bet-frequency, blind-defense, trueskill, jungleman, sandbox]
related:
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-strategy-overview.md
  - entities/people/daniel-cates-jungleman.md
  - entities/people/tom-dwan.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - concepts/poker-axis-eval-literacy.md
  - sources/research-k122-poker-paper-landscape-2026-06-19.md
  - sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md
  - sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md
  - sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
  - sources/brief-k122-poker-researcher-track-plan-2026-06-19.md
maturity: draft
created: 2026-06-19
updated: 2026-06-26
---

## Relations

- @entities/platforms/devfun-poker-arena.md — researcher track HU sandbox (K121)
- @sources/devfun-poker-researcher-track-email-2026-06-19.md — TrueSkill + style rep mechanic
- @entities/people/daniel-cates-jungleman.md — default HU aggression target for TrueSkill
- @concepts/poker-strategy-overview.md — ring-game doctrine; **not portable** to HU without rewrite
- @osint-wiki/concepts/devfun-researcher-track-readiness-2026-06.md — ops hub + HU gates (cross-wiki)

## Raw Concept

Strategy primer for **heads-up NLHE** on dev.fun **researcher track** — distinct from 6-max Playground/Tournament logic.

## Narrative

### Why HU is a fork, not a tweak

Researcher sandbox is **BTN (SB) vs BB** only [CONFIRMED K121]. Playground is **6-max** with season bankroll. Preflop ranges, 3-bet frequencies, and opponent modeling assumptions **do not transfer**.

| Dimension | 6-max Playground | HU researcher |
|-----------|------------------|---------------|
| Hero positions | UTG…BTN + blinds | **In position (button)** vs BB every other hand |
| Typical open | Position-dependent tight opens | **Wide button opens** (often 70%+ at 100bb) |
| 3-bet culture | ~6–10% population | **20–25%+** at elite HU (Jungleman era) [TENTATIVE] |
| Opponents | Multiway pots | **One villain** — HUD stats dominate |
| Win metric | Chips / survival | **TrueSkill** from match outcomes |
| Style goal | Qualify top 20 | **Beat field + emulate Jungleman/Dwan** for rep pick |

### Preflop HU principles [TENTATIVE — training material synthesis]

**Button (in position):**

- Open wide at 100bb — steal blinds + build pots with initiative
- Mix raises and limps only if skillFile/rubric rewards it; default **raise-first**
- 3-bet with suited connectors (56s) and polarized value — Jungleman quote [Source: Paul Phua interview]

**Big blind (out of position):**

- Defend wide vs small opens — folding too much bleeds TrueSkill
- 3-bet/4-bet back with polarized range + suited wheel hands
- Avoid fit-or-fold patterns Jungleman probes

**Stack depth:** Under ~30bb, shift toward shove/fold preflop — different chart set than 100bb Playground survival.

### Postflop HU principles

- **Single villain** → continuation bet frequently on favorable boards; check-raise draws (stop-and-go)
- **Thin value** more correct HU than full ring
- **Pot control less valuable** — HU pots are zero-sum; passivity loses TrueSkill vs aggressive pool

### TrueSkill vs chip EV

TrueSkill ranks **pairwise match wins**. Optimize local selfplay for **match W/L**, not bb/100 vs tight heuristics. High variance early — plan sustained volume.

**Dual objective tension:** TrueSkill max may conflict with **style rep** (Dwan merge vs Jungleman probe frequency). Default **Jungleman-shaped** aggression for sandbox; keep Dwan overlay for rep lane tests [Source: @osint-wiki/concepts/devfun-researcher-pro-style-targets-2026-06.md].

### K118 blocker (shared preflop path)

Passive **PFR 2.2%** vs VPIP 11.5% is **anti-HU** and **anti-Jungleman** — fix P0 open/3-bet path before researcher submit (`@sources/brief-k118-poker-agent-research-gaps-2026-06-17.md`).

### Unique every-hand states (bot architecture)

Each hand is a new imperfect-information state. Policy stack:

1. **Spot classifier** — HU preflop open / vs 3-bet / postflop branch
2. **Preflop chart** — `_HU_OPEN_CHART` (not 6-max UTG)
3. **Postflop equity** — pokerkit / treys Monte Carlo vs pot odds
4. **Single-villain HUD** — session VPIP/PFR/3-bet with decay
5. **Optional style overlay** — `jungleman` or `durrrr` priors for rep lane
6. **Offline HL loop** — patch thresholds from analyze reports; **zero runtime LLM**

Full research plan: @sources/brief-k122-poker-researcher-track-plan-2026-06-19.md (operator copy in `briefs/`).

### SDK local iteration

Use **`devfun-org/poker-arena-starter-kit`**: `./pokerkit test`, `./pokerkit selfplay --hands 200`, `./pokerkit analyze`. HU-specific selfplay opponents TBD when researcher SDK ships [NEEDS VERIFICATION 2026-06-21].

## Snippets

> "In heads-up it’s rare to have [a very strong hand]" — context for wide aggression [Source: Paul Phua / Jungleman HU interview]

> "I just try to win all the pots that I possibly can." [Source: @sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md]

## Dead Ends

- **6-max Playground charts in HU sandbox** — wrong geometry
- **Selfplay bb/100 as training target** — misaligns with TrueSkill and Playground analyze
- **Runtime LLM decide()** — starter kit L2; K118 dead-end for prod
