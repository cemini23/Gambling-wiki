---
title: dev.fun Poker Arena (Monad)
type: entity
tags: [entity, platform, prediction-markets-adjacent, poker, agent-arena, phase-0]
keywords: [devfun, poker-arena, monad, texas-holdem, agent-competition, tom-dwan]
related:
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/tools/pokerskill.md
  - entities/bots/poker-bot-tooling.md
  - concepts/poker-strategy-overview.md
  - entities/games/poker.md
  - concepts/gambling-bot-architecture.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - entities/games/poker.md
maturity: draft
created: 2026-06-01
updated: 2026-06-02
phase_0_verdict: CONDITIONAL-GO 2026-06-01 — sanctioned bot arena (not live poker room); enter via arena API; prize claim needs X verify + external payout wallet
adoption_status: PHASE-0-COMPLETE
---

## Relations

- @entities/bots/cemini-devfun-poker-agent.md — Cemini custom `decide()` entry
- @entities/tools/pokerskill.md — skill-library binding pattern for LLM/heuristic agents
- @sources/devfun-poker-arena-phase0-2026-06-01.md — Phase-0 audit source

## Raw Concept

- **Product**: [dev.fun × Monad Poker Arena](https://dev.fun/)
- **Docs**: [docs.dev.fun](https://docs.dev.fun/) · skill index [arena.dev.fun/skills/arena.md](https://arena.dev.fun/skills/arena.md)
- **Starter kit**: [chenziz/arena-pokerkit](https://github.com/chenziz/arena-pokerkit)
- **Beta API**: `https://b-arena.dev.fun/api/arena`
- **Main event opens**: **2026-06-03** (landing page); prize pool **$50K** + Tom Dwan pro-table seat (marketing)

## Narrative

### What it is

**Bot-vs-bot NL Texas Hold’em** on a hosted arena API. Humans register agents; agents poll **pending actions** and submit fold/check/call/bet/raise with a short chat “read.” **Not** PokerStars automation — different legal/ToS lane from `@entities/platforms/pokerstars.md`.

### Game modes (platform)

| Mode | Shape |
|------|--------|
| **Texas Hold’em lobby** | Continuous 6-max tables, season bankroll |
| **Poker Eval benchmark** | PVE vs reference panel; `POST /texas/benchmark/start` |
| **Pump prediction** | Separate dev.fun skill family (out of scope) |

### Phase-0 audit (2026-06-01)

| Check | Result |
|-------|--------|
| **License (starter kit)** | **MIT** — arena-pokerkit |
| **Entry fee** | **Competition-specific** — API returns **402** with MON/chain amount when required; main Poker Arena fee **TBD**; invite/partner paths documented |
| **Prize eligibility** | **X claim** + external payout wallet (agent wallet custodial / closed-loop) |
| **Retail online poker** | **NO-GO** for unsanctioned room bots — **GO** for this arena only |
| **Wiki overlap** | `@entities/tools/pokerskill.md`, `@entities/bots/poker-bot-tooling.md`, `@concepts/poker-strategy-overview.md` |
| **Ops** | Continuous play → cron/heartbeat (~4–6h); action clock → deadline fallbacks mandatory |

**Verdict: CONDITIONAL-GO** — participate in **dev.fun arena only**; do not reuse stack against consumer poker sites.

### Active beta competitions (2026-06-02) [CONFIRMED]

| ID | Name | Notes |
|----|------|-------|
| `cmpr1vesh2it1x69xmtpiaecp` | [Poker] Tournament S28 | **Prod lobby** — entry fee **0.01 MON** on Monad [CONFIRMED 2026-06-02] |
| `cmpr1uomm2is6x69xx4nyqz9r` | [Poker] Playground S1 | Dev / casual |
| `cmpdk0pt00eawvcaf1es8plw2` | Poker Eval 500-hand | Inactive until next eval window |

Re-check `GET /competition/list-active` before each run.

## Snippets

> "$50K. best bots climb the leaderboard, and earn a seat against Tom Dwan." [Source: https://dev.fun/ (retrieved 2026-06-01)]

> "If it acts like gambling…" — **not applicable here**; platform is explicit agent arena, not state-licensed sportsbook/room product.

## Dead Ends

- Treating arena win-rate as proof of +EV on DraftKings/Kalshi sports
- Expecting full June 3 rules before registration — use Playground / Poker Eval for prep
