---
title: "Research — WNBA cold-streak / last-2-min live unders (2026-08-13)"
type: source
tags: [source, research, wnba, live-betting, kalshi, play-by-play]
keywords: [wnba, espn pbp, five misses, last two minutes, kalshi, opencli]
related:
  - entities/sports/wnba-betting.md
  - entities/sports/nba-betting.md
  - entities/platforms/kalshi.md
  - concepts/gambling-bot-architecture.md
  - concepts/pm-live-belief-updating.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/favorite-longshot-bias.md
read_status: deep-read
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @entities/sports/wnba-betting.md — synthesis hub
- @entities/platforms/kalshi.md — public series inventory used in this pass
- @concepts/gambling-bot-architecture.md — alert-only product constraint
- @concepts/pm-live-belief-updating.md — NBA live mid underreaction context

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | WNBA cold-streak props + last-2:00 each-team-under-5 research |
| **Type** | Original operator research (ESPN PBP + Kalshi public API + OpenCLI Reddit/X) |
| **Author** | Cemini / OSINT session 2026-08-13 |
| **Location** | Results: `/tmp/wnba_prop_research.json` (session); canvas: `~/.cursor/projects/.../canvases/wnba-cold-streak-props.canvas.tsx`; OpenCLI dumps: `/tmp/wnba-opencli/` |
| **Retrieved** | 2026-08-13 |
| **Read-status** | deep-read |

Prompt: friend hit a last-2-min each-team-under-5 ticket; ask whether a bot that watches five consecutive misses then bets the quarter under is +EV; check Kalshi (no sportsbook login); verify Reddit/X with OpenCLI.

## Narrative

### Methods

1. **ESPN WNBA PBP** via `site.web.api.espn.com` (browser UA) — 189 completed games, 2026-06-01…2026-08-12. Script `/tmp/wnba_prop_research.py`.
2. **Kalshi public trade-api/v2** — series/events/markets listing; no prod credentials used.
3. **agent-reach OpenCLI** — `opencli reddit search/read`, `opencli twitter search` (browser login).
4. Prior Flash Reddit pass was access-blocked; OpenCLI superseded it.

### Core results

- **5-miss → remaining Q under:** no edge vs clock baseline; next FG% slightly **higher** after droughts.
- **Last 2:00 both under 5:** 23.8% overall; 12.2% close; 34.0% blowout at 2:00 margin ≥15. Fair odds documented on `@entities/sports/wnba-betting.md`.
- **Kalshi:** 88 WNBA series; **0** last-2-min contracts; usable objects are game/quarter/half/team totals with thin live 4Q books.
- **Social:** retail “always under” + live-under-with-minutes-left anecdotes; no public 5-miss system; live markets lock ~2:00.

### Bot posture

Alert-only paper scanner for blowout last-2:00 unders **if** a sportsbook lists the prop and odds beat fair. Do not auto-wager. Do not pretend Kalshi proxies the friend’s ticket.

## Snippets

See tables on `@entities/sports/wnba-betting.md` (FG% after miss streaks; last-2:00 hit rates; Kalshi series map).
