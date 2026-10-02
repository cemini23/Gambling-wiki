---
title: College football betting
type: entity
tags: [entity, sport, cfb, college-football, sports-betting]
keywords: [college-football, cfb, spreads, totals, heisman, player-props, ats, cfp]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/vig-and-hold.md
  - concepts/line-shopping-and-clv.md
  - concepts/parlay-and-correlated-bets.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/platforms/hard-rock-bet.md
  - entities/platforms/draftkings.md
  - sources/rss-lsb-cfb-week6-cards-2026-10-01.md
  - sources/daily-digest-batch-k180-2026-10-02.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
---

## Relations

- @concepts/sports-betting-fundamentals.md — spread, total, ML mechanics
- @concepts/vig-and-hold.md — de-vig posted prices before comparing
- @concepts/line-shopping-and-clv.md — CFB lines move faster and wider than NFL
- @entities/sports/nfl-betting.md — sibling US football vertical
- @sources/rss-lsb-cfb-week6-cards-2026-10-01.md — 2026-10-01 seed batch

## Raw Concept

College football betting — spreads, totals, player props, and Heisman futures.

**Status:** new vertical as of 2026-10-02. **Research entity only — no bankroll lane, no auto-enter.**

## Narrative

### Structural traits

- **Large, uneven market.** 130+ FBS teams at very different information quality. Soft numbers persist longer than in the NFL.
- **Wide spreads are common.** Double-digit and multi-touchdown lines are routine, which makes **buying the hook** a live decision. A half-point matters more here than in a typical NFL game.
- **Blowout risk is the core hazard.** Backdoor covers and garbage-time scoring swing totals and spreads. Game script is less stable than in the NFL.
- **Sample sizes are short and opponent quality varies wildly.** Early-season defensive numbers are inflated by FCS and Group-of-5 opponents. Always check the schedule behind the rating.
- **Availability reports are late.** The Big Ten, for example, publishes its final report **two hours before kickoff**. Injury-driven line movement can arrive very late.

### Market notes

- **Check the number, not just the side.** A spread listed at both 16.5 and 17 changes whether a 17-point win covers.
- **Prop pricing can outrun usage.** In the 2026-10-01 seed batch, a mobile quarterback's anytime-TD price implied **53.9%** while he had scored in **one of four** games. Run the implied-vs-realised check before taking a rushing-TD prop.
- **Heisman futures** reprice fast after a single big game; they are one-player, high-variance, and correlated with team performance.
- **Totals** carry the scoring-midpoint check: compare the midpoint of both teams' scoring averages against the posted number to see which way the cushion sits.

### Data

No free data source is wired for this wiki yet. Candidate inputs: CFBD (CollegeFootballData) API and public play-by-play feeds. Both are unvetted for ToS. [NEEDS VERIFICATION 2026-10-02]

## Snippets

> "It's the first time Clemson is a double-digit home underdog in Dabo Swinney's 245 games." [Source: @sources/rss-lsb-cfb-week6-cards-2026-10-01.md, quoting LSB]

## Dead Ends

- **No closing-line history.** This wiki has no CFB CLV sample. Do not allocate bankroll until one exists.
- **Do not treat the seed cards as picks.** Single outlet, affiliate disclosure. The mechanisms transfer; the selections do not.
- **Do not auto-enter.** See @concepts/gambling-wiki-scope.md and the responsible-gambling posture in `CLAUDE.md`.
