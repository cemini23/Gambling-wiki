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
  - concepts/opponent-modeling-imperfect-info.md
  - entities/games/poker.md
  - concepts/gambling-bot-architecture.md
  - entities/people/tom-dwan.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - sources/youtube-pokergo-dwan-hsp-mega-compilation-2026-06-03.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
maturity: draft
created: 2026-06-01
updated: 2026-06-09
phase_0_verdict: CONDITIONAL-GO 2026-06-01 — sanctioned bot arena (not live poker room); enter via arena API; prize claim needs X verify + external payout wallet
adoption_status: PHASE-0-COMPLETE
---

## Relations

- @entities/bots/cemini-devfun-poker-agent.md — Cemini custom `decide()` entry
- @concepts/poker-hl-analyst-loop.md — analyze → patch → deploy loop for Playground leaks
- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — K95 opponent modeling anchor
- @entities/tools/pokerskill.md — skill-library binding pattern for LLM/heuristic agents
- @entities/people/tom-dwan.md — Pro Table Finale human pro (style + bot counter-strategy)
- @sources/devfun-poker-arena-phase0-2026-06-01.md — Phase-0 audit source

## Raw Concept

- **Product**: [dev.fun × Monad Poker Arena](https://dev.fun/)
- **Docs**: [docs.dev.fun](https://docs.dev.fun/) · skill index [arena.dev.fun/skills/arena.md](https://arena.dev.fun/skills/arena.md)
- **Starter kit**: [chenziz/arena-pokerkit](https://github.com/chenziz/arena-pokerkit)
- **Official API**: `https://arena.dev.fun/api/arena` — **use for Playground S1 / public leaderboard**
- **Beta API**: `https://b-arena.dev.fun/api/arena` — separate agents, wallets, leaderboards (legacy prep)

### Beta vs official wallets [CONFIRMED 2026-06-03]

Same handle on beta and official = **two agent IDs**, **two custodial Monad wallets**. MON deposited on beta does **not** sync to official. Outbound `POST /agent/wallet/transfer/native` only accepts dev.fun **protocol addresses** (402 entry fees); agent-to-agent transfer returns **403**. Fund official via MoonPay or external send. Wallet/agent IDs: private creds only. See repo `LESSONS.md` L4.
- **Main event opens**: **2026-06-03** (landing page); prize pool **$50K** + Tom Dwan pro-table seat (marketing)

### Event ladder — paired seasons [TENTATIVE 2026-06-08 Discord]

| Stage | Format | Advance |
|-------|--------|---------|
| **Playground S*N*** | Bot qualifier per season (fresh bankroll) | Top **20** → **free entry Tournament S*N*** |
| **Tournament S*N*** | Knockout bracket (paired to same season number) | Top **25** within that bracket |
| **Researcher track** | Invite-only sandbox benchmark | Top **3** paid |
| **Pro Table Finale** | **Human vs AI** — format **TBD** | Top agents earn seat vs pro |

Playground S1 qualification does **not** carry to Tournament S2 — re-qualify on each new playground season. [TENTATIVE — Discord team 2026-06-08; verify on docs when updated]

Tom Dwan is the **marketing anchor** for the finale, **not** a player in bot brackets. See @entities/people/tom-dwan.md.

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

### Season jackpots (`GET /texas/jackpots`) [CONFIRMED 2026-06-08]

| Type | Trigger (API introspection) | S2 pool (example) |
|------|---------------------------|-------------------|
| **Royal flush** | Showdown, hand unfolded | 5× 13,600 MON slots |
| **7-2 offsuit bluff** | Uncontested pot — all fold vs 72o | 10× 4,500 MON slots |

S1 royal slot **Claimed**. S2 runs **both** jackpots. Optional hunt on qual bot when flagged — not a substitute for top-20 pairing above.

### Active official competitions (2026-06-08) [CONFIRMED]

| ID | Name | Notes |
|----|------|-------|
| `cmq57o53r0bhw18g23qkydb08` | [Poker] Playground S2 | **Prod qual target** → Tournament S2 |
| `cmpy2qy65002ud9ej6b7jjq0l` | [Poker] Playground S1 | Closed — chip #1, Tournament S1 ticket |
| `seed_poker_eval_s1` | [Poker] Eval S1 | Benchmark panel |

Tournament S1/S2 IDs not in `list-active` yet — watch Discord + arena UI. Beta IDs (`b-arena`) are a separate environment.

Re-check `GET /competition/list-active` before each run.

### Preflop selfplay gate (K107 audit, 2026-06-09) [CONFIRMED]

Open-spot detection uses `is_preflop_open_spot()` in private `opponent_target.py` (handles Arena `callChips=BB` for UTG first-in). **Not** the raw `call_chips==0` anti-pattern from K107.

Selfplay audit (`cemini_selfplay_audit.py`, 400 hands): **VPIP 12.1% / PFR 2.1%** — passive gap persists; investigate `_preflop_open` raise rate vs live Arena analyze, not open-spot boolean alone. See `@concepts/poker-hl-analyst-loop.md`.

## Snippets

> "$50K. best bots climb the leaderboard, and earn a seat against Tom Dwan." [Source: https://dev.fun/ (retrieved 2026-06-01)]

> "If it acts like gambling…" — **not applicable here**; platform is explicit agent arena, not state-licensed sportsbook/room product.

## Dead Ends

- Treating arena win-rate as proof of +EV on DraftKings/Kalshi sports
- Expecting full June 3 rules before registration — use Playground / Poker Eval for prep
