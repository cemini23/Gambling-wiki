---
title: NHL betting
type: entity
tags: [entity, sport, nhl, hockey, sports-betting]
keywords: [nhl, hockey, puck-line, moneyline, totals, power-play, shots-on-goal, goaltending]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/vig-and-hold.md
  - concepts/line-shopping-and-clv.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/bankroll-management.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/platforms/hard-rock-bet.md
  - entities/platforms/draftkings.md
  - sources/rss-lsb-nhl-opening-night-props-2026-09-29.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- @concepts/sports-betting-fundamentals.md — ML, spread, totals mechanics
- @concepts/vig-and-hold.md — de-vig posted prices before comparing markets
- @concepts/line-shopping-and-clv.md — puck-line prices vary by board
- @concepts/parlay-and-correlated-bets.md — goal + Over is correlated
- @entities/sports/nfl-betting.md — sibling US major sport
- @entities/sports/nba-betting.md — sibling US major sport
- @sources/rss-lsb-nhl-opening-night-props-2026-09-29.md — 2026-27 opening-night seed batch

## Raw Concept

NHL-specific betting — puck lines, special teams, shot volume, and goaltending.

**Status:** new vertical as of 2026-09-30. No operator lane was open before this page. It is a **research entity only** — no auto-enter.

## Narrative

### Structural traits

- **Low-scoring, high-variance.** A 5.5 or 6.0 total leaves little cushion. Three-goal third periods are common.
- **Puck line replaces the spread.** The standard is -1.5 / +1.5. The favourite almost always lays the -1.5, so the price is a **win-margin** bet, not a win bet. Break-even on a plus-money puck line requires a high share of multi-goal wins.
- **Special teams are a first-class input.** Power-play percentage against penalty-kill percentage is a repeatable, published weekly number. It is the cleanest edge source in the sport.
- **Goaltending is a single point of failure.** Starter confirmations arrive late. A backup start rewrites every prop bar built on the starter.
- **Shot volume is more forecastable than finishing.** Shooting percentage is noisy; shot rates are stable. Prefer shot-volume props over goal props when the price is fair.

### Market notes

- **Puck-line pricing varies by board.** Always shop. A spread of +102 to +105 on the same line is routine.
- **Correlation.** A player goal and the game Over are positively correlated. Do not price them as independent legs in a parlay.
- **Futures.** Stanley Cup outrights are a separate board; they are not a substitute for game-level pricing.

### Worked mechanics (from the 2026-27 opening-night batch)

- **Break-even on a plus-money puck line.** At -256 on the moneyline, the favourite needs roughly **68%** of wins by two-plus goals for a **+105** puck line to break even.
- **Special-teams delta.** Power-play rate plus the opponent's penalty-kill shortfall gives an adjusted conversion rate. Multiply by power-play opportunities per game for an expected power-play-goal figure.

See @sources/rss-lsb-nhl-opening-night-props-2026-09-29.md for the full arithmetic.

### Data

No free data source is wired for this wiki yet. Candidate inputs: NHL public API (schedule, box score, shot events) and naturalstattrick-style rate exports. Both are unvetted for ToS. [NEEDS VERIFICATION 2026-09-30]

## Snippets

> "The case for the shot-volume markets is that they do not rely on finishing, while goal and point props inherit finishing risk." [Source: @sources/rss-lsb-nhl-opening-night-props-2026-09-29.md, paraphrasing LSB 2026-09-29]

## Dead Ends

- **Do not treat the opening-night cards as picks.** Single author, single outlet, affiliate disclosure. The mechanisms transfer; the selections do not.
- **No bankroll allocation without a CLV sample.** NHL has no closing-line history in this wiki yet.
- **Do not auto-enter.** See @concepts/gambling-wiki-scope.md and the responsible-gambling posture in `CLAUDE.md`.
