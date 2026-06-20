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
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k107-poker-open-spot-audit-2026-06-09.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
  - entities/people/daniel-cates-jungleman.md
  - concepts/heads-up-arena-strategy.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
  - concepts/poker-axis-eval-literacy.md
maturity: draft
created: 2026-06-01
updated: 2026-06-19
phase_0_verdict: CONDITIONAL-GO 2026-06-01 — sanctioned bot arena (not live poker room); enter via arena API; prize claim needs X verify + external payout wallet
adoption_status: PHASE-0-COMPLETE
---

## Relations

- @entities/bots/cemini-devfun-poker-agent.md — Cemini custom `decide()` entry
- @concepts/poker-hl-analyst-loop.md — analyze → patch → deploy loop for Playground leaks
- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — K95 opponent modeling anchor
- @entities/tools/pokerskill.md — skill-library binding pattern for LLM/heuristic agents
- @entities/people/tom-dwan.md — Pro Table Finale + researcher rep selection
- @entities/people/daniel-cates-jungleman.md — researcher rep selection (Jungleman)
- @sources/devfun-poker-researcher-track-email-2026-06-19.md — researcher track invite (K121)
- @sources/devfun-poker-arena-phase0-2026-06-01.md — Phase-0 audit source

## Raw Concept

- **Product**: [dev.fun × Monad Poker Arena](https://dev.fun/)
- **Docs**: [docs.dev.fun](https://docs.dev.fun/) · skill index [arena.dev.fun/skills/arena.md](https://arena.dev.fun/skills/arena.md)
- **Starter kit**: [chenziz/arena-pokerkit](https://github.com/chenziz/arena-pokerkit) — see `@entities/tools/devfun-poker-arena-starter-kit.md` (K102)
- **Official API**: `https://arena.dev.fun/api/arena` — **use for Playground S1 / public leaderboard**
- **Beta API**: `https://b-arena.dev.fun/api/arena` — separate agents, wallets, leaderboards (legacy prep)

### Beta vs official wallets [CONFIRMED 2026-06-03]

Same handle on beta and official = **two agent IDs**, **two custodial Monad wallets**. MON deposited on beta does **not** sync to official. Outbound `POST /agent/wallet/transfer/native` only accepts dev.fun **protocol addresses** (402 entry fees); agent-to-agent transfer returns **403**. Fund official via MoonPay or external send. Wallet/agent IDs: private creds only. See repo `LESSONS.md` L4.
- **Main event opens**: **2026-06-03** (landing page); prize pool **$50K** + Tom Dwan pro-table seat (marketing)

### Event ladder — three public tracks + finale [CONFIRMED researcher detail 2026-06-19]

| Stage | Format | Advance / outcome |
|-------|--------|-------------------|
| **Playground S*N*** | 6-max bot qualifier, season bankroll | Top **20** → free **Tournament S*N*** entry |
| **Tournament S*N*** | Knockout bracket (paired season) | Top **25** in bracket |
| **Researcher track** | **Heads-up** sandbox; **TrueSkill** ranking | Top agent = **field benchmark**; Dwan + Jungleman pick **style-matched** bots to represent them |
| **Pro Table Finale** | Human vs AI showcase | Top agents vs pros (Dwan + Jungleman per PR) |

Playground S1 qualification does **not** carry to Tournament S2 — re-qualify each playground season. [TENTATIVE — Discord 2026-06-08 for Playground/Tournament pairing]

**Researcher track timeline** [CONFIRMED — @sources/devfun-poker-researcher-track-email-2026-06-19.md]:

| Date | Milestone |
|------|-----------|
| **2026-06-21** | Closed beta (researchers) |
| **2026-06-25** | Public sandbox opens |

**Researcher submission types:** Python bot, fine-tuned model, raw weights, or LLM agent with operator API key. **Tooling:** self-play SDK, Kaggle competition page, sponsored sandbox credits.

**Not the same lane as Playground** — HU vs 6-max; TrueSkill vs chip leaderboard; separate SDK/API surface until docs confirm parity with `arena-pokerkit`.

Tom Dwan and Jungleman are **pro anchors** for finale marketing and researcher **style rep selection**, not players in bot Playground brackets. See @entities/people/tom-dwan.md, @entities/people/daniel-cates-jungleman.md.

## Narrative

### What it is

**Bot-vs-bot NL Texas Hold’em** on a hosted arena API. Humans register agents; agents poll **pending actions** and submit fold/check/call/bet/raise with a short chat “read.” **Not** PokerStars automation — different legal/ToS lane from `@entities/platforms/pokerstars.md`.

### Game modes (platform)

| Mode | Shape |
|------|--------|
| **Texas Hold’em lobby** | Continuous 6-max tables, season bankroll |
| **Researcher sandbox** | **Heads-up** bot-vs-bot; **TrueSkill**; self-play SDK + Kaggle |
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

Selfplay audit (`cemini_selfplay_audit.py`, 400 hands, seed 42): **VPIP 11.5% / PFR 2.2%** (2026-06-17) — passive gap persists; SB VPIP 13.4%. See `@sources/brief-k118-poker-agent-research-gaps-2026-06-17.md` and `@concepts/poker-hl-analyst-loop.md`.

## Snippets

> "$50K. best bots climb the leaderboard, and earn a seat against Tom Dwan." [Source: https://dev.fun/ (retrieved 2026-06-01)]

> "we run it heads-up in a sandbox, ranked by TrueSkill" [Source: @sources/devfun-poker-researcher-track-email-2026-06-19.md]

> "If it acts like gambling…" — **not applicable here**; platform is explicit agent arena, not state-licensed sportsbook/room product.

## Dead Ends

- Treating arena win-rate as proof of +EV on DraftKings/Kalshi sports
- Port Playground 6-max charts to **researcher HU sandbox** without HU-specific regression — format mismatch
