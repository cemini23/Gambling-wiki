---
title: WNBA betting
type: entity
tags: [entity, sport, wnba, basketball, sports-betting, live-betting]
keywords: [wnba, women basketball, unders, quarter totals, last two minutes, cold streak, kalshi]
related:
  - entities/sports/nba-betting.md
  - entities/platforms/kalshi.md
  - concepts/gambling-bot-architecture.md
  - concepts/pm-live-belief-updating.md
  - concepts/favorite-longshot-bias.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/sports-betting-fundamentals.md
  - sources/research-wnba-cold-streak-live-unders-2026-08-13.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @entities/sports/nba-betting.md — sibling basketball sport; Kalshi live underreaction research is NBA-primary
- @entities/platforms/kalshi.md — WNBA series inventory (game/total/spread/quarter/team totals); no last-2:00 contract
- @concepts/gambling-bot-architecture.md — alert-only default; no sportsbook auto-wager
- @concepts/pm-live-belief-updating.md — live mid drift ≠ +EV after bid–ask (NBA evidence; WNBA thinner)
- @concepts/parlay-and-correlated-bets.md — both-teams-under-5 is a correlated 2-leg
- @sources/research-wnba-cold-streak-live-unders-2026-08-13.md — 189-game ESPN PBP + Kalshi + OpenCLI social pass

## Raw Concept

WNBA-specific sports betting — pace/scoring level vs NBA, retail “blind under” folklore, live quarter/game totals, and whether cold-shooting or last-two-minute props have measurable edge. Prompted by operator research on (1) five consecutive missed FGs → remaining-quarter under and (2) last 2:00 of Q4, each team under 5.

## Narrative

### Structural traits

- **Lower scoring / longer empty stretches than NBA** — retail forums treat this as a free under; books already price lower PPG. 2026 sample combined quarter means were roughly flat (~44.5 / 42.9 / 44.3 / 44.1) — Q4 is not a free under window [CONFIRMED for 2026-06-01…08-12 sample].
- **Thinner live books** — wider spreads and earlier market locks than NBA; r/sportsbook reports live spreads often suspend near the final ~2:00 of quarters.
- **Player-prop spam on X** — public WNBA betting discourse is mostly tout SGPs, not systematic live-total scanners.

### Idea 1 — five consecutive team FG misses → remaining quarter under [CONFIRMED no edge]

ESPN play-by-play, **189 completed 2026 games** (1 Jun–12 Aug), 26,150 FG attempts (sample FG% **45.8%**):

| After k consecutive **team** FG misses | Next FG% | n |
|---|---|---|
| 3 | 47.3% | 1,853 |
| 4 | 46.1% | 960 |
| 5 | **46.6%** | 511 |
| All FG (sample) | 45.8% | 26,150 |

After a 5-miss trigger, remaining team points in that quarter averaged **10.75** vs **10.55** clock-only expected (~**51.9%** under expected). Combined remaining **21.41** vs **21.09**. Trigger is common (~2.8/game; median clock left ~4:42). **Do not build a live bot on this signal** — the drought is already in the score/clock; next-shot rate does not collapse.

### Idea 2 — last 2:00 of Q4, each team under 5 [CONFIRMED game-state, not cold hand]

Same 189-game sample. Margin measured **at the 2:00 mark of Q4**:

| State at 2:00 | n | Mean pts/team | Both under 5 | Fair American (both) | One-team under 5 fair |
|---|---|---|---|---|---|
| All games | 189 | 5.16 | **23.8%** | **+320** | +135 |
| Close (margin ≤5) | 74 | 5.93 | **12.2%** | **+720** | +222 |
| Mid | 68 | 4.83 | **29.4%** | **+240** | — |
| Blowout (margin ≥15) | 47 | 4.41 | **34.0%** | **+194** | −114 |

Combined last-2:00 mean **10.31**. Close games score **more** late (fouling/FTs). Blowouts score less but both-under-5 is **not a lock** (34%) — garbage-time runs are real. A “high odds” (+400–600) both-under ticket is only plausibly +EV in a **decided** game; in a one-possession game even plus-money can be −EV vs true ~12%.

**Product shape if any:** Discord/SMS **alert + log** when Q4 hits 2:00, margin ≥12–15, and offered odds beat fair (~longer than +240 on both-under, or better than −114 on single-team under 5). Paper a month before staking. **No sportsbook auto-submit** (`@concepts/gambling-bot-architecture.md`).

### Kalshi WNBA inventory (public API, 2026-08-13) [CONFIRMED]

Public `api.elections.kalshi.com/trade-api/v2` — **no auth required** for series/events/markets. **88** WNBA / Women’s Pro Basketball series. Sports-wide search for last-2 / final-2 / 2-minute wording: **0** series.

| Series (examples) | Contract | Maps to ideas? |
|---|---|---|
| `KXWNBAGAME` / `TOTAL` / `SPREAD` | Game winner / total / spread | Liquid game total; not last 2:00 |
| `KXWNBA1–4QTOTAL` | Combined quarter points | Idea 1 only (buy No on a strike) — thin/wide live |
| `KXWNBA1HTOTAL` / `2HTOTAL` | Half totals | Not last 2:00 |
| `KXWNBATEAMTOTAL` | Full-game team total | Not last-2:00 team under 5 |
| `KXWNBANEXTTEAM` | Caitlin Clark next team | Name collision — not next-to-score |
| Last 2:00 each-team-under-5 | **Does not exist** | Friend’s ticket is sportsbook-only |

Live illustration (ATL @ CONN blowout, 13 Aug ~21:00 ET): ATL ~99¢ to win; 4Q over **41.5** yes **21–58¢** (last 48¢) — buying under costs ~79¢ into a ~37¢ spread. Game totals on the same event have far more OI than 4Q.

### Retail / social discourse (OpenCLI Reddit + X, 2026-08-13)

- **“WNBA unders are a life hack”** (r/sportsbetting) — live under after Q1/mid-Q2 look; domination → under folklore. **Not** a 5-miss rule.
- **“WNBA Warning”** — closest cousin: live under with “minutes left”; commenter hit then lost 0.5 on a late 3 after the line had already dropped.
- **2026 “just bet the under”** threads get sharp pushback that lines are already adjusted.
- **r/sportsbook “Betting in the final minute”** — live markets often lock ~final 2:00.
- **X** — tout player props; no indexed system matching either exact idea. Garbage-time spike anecdotes exist (e.g. large trailing-team runs late in Q4).

Documented **live-under** pattern elsewhere (hot quarter → fade inflated live total) is **mean reversion of the line**, opposite of miss-continuation — see `@concepts/sports-betting-fundamentals.md` hygiene + Tech Insider NFL notes.

## Snippets

> After five team FG misses, next FG% 46.6% (n=511) vs sample 45.8%; remaining Q scoring ≈ clock baseline (~52% under expected).
> [Source: @sources/research-wnba-cold-streak-live-unders-2026-08-13.md]

> Both teams under 5 in last 2:00 of Q4: 23.8% all / 12.2% close / 34.0% blowout (margin at 2:00). Fair both-under ≈ +320 / +720 / +194.
> [Source: @sources/research-wnba-cold-streak-live-unders-2026-08-13.md]

> Kalshi: 88 WNBA series; zero last-2-minute contracts; closest live objects are `KXWNBAnQTOTAL` and game totals.
> [Source: Kalshi public trade-api/v2, 2026-08-13]

## Dead Ends

- **Five-miss → quarter-under bot** — no edge vs time-adjusted remaining total; trigger fires almost every game.
- **Trade friend’s ticket on Kalshi** — contract does not exist; do not invent a proxy without fillable 4Q/game-total liquidity.
- **Blind “always under WNBA”** — retail meme contradicted by flat 2026 quarter scoring and adjusted lines.
