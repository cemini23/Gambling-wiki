---
title: NFL betting
type: entity
tags: [entity, sport, nfl, football, sports-betting]
keywords: [nfl, football, spreads, props, totals, key-numbers, clv, injury-report]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/best-ball-strategy.md
  - entities/tournaments/best-ball-mania-vii.md
  - concepts/dfs-strategy-overview.md
  - concepts/line-shopping-and-clv.md
  - concepts/sharp-vs-soft-books.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/bankroll-management.md
  - entities/sports/nba-betting.md
  - entities/sports/world-cup-2026-betting.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/platforms/hard-rock-bet.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md
  - sources/web-sportsbookreview-hard-rock-bet-2026-06-20.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/platforms/underdog-fantasy.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sweeps/2026-06-20-tier2-w8-nfl.md
maturity: validated
created: 2026-05-31
updated: 2026-06-20
---

## Relations

- @entities/platforms/hard-rock-bet.md — operator primary NFL book (W8)
- @concepts/line-shopping-and-clv.md — CLV workflow
- @concepts/best-ball-strategy.md — shared player research stack
- @concepts/dfs-strategy-overview.md — FanDuel/Underdog DFS overlap
- @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md — K124 process primer

## Raw Concept

NFL-specific betting and fantasy context — key numbers, season structure, market types, operator W8 workflow.

## Narrative

### W8 operator stack (2026 season)

| Lane | Platform | Wiki home |
|------|----------|-----------|
| Sportsbook + casino | Hard Rock Bet | @entities/platforms/hard-rock-bet.md |
| Daily fantasy GPP | FanDuel | @entities/platforms/fanduel.md |
| Best ball | Underdog BBM7 | @entities/tournaments/best-ball-mania-vii.md |

Same injury and game-environment research feeds all three; **betting** is vs the line, **DFS/best ball** vs the field.

### Key numbers (spread) [CONFIRMED]

3 and 7 dominate NFL margins (FG + TD). Order of frequency: **3 > 7 > 10 > 6 > 14**. Half-points around 3 and 7 are the highest-ROI shop targets; 1/4/5 are rare margins.

| Line move | EV note |
|-----------|---------|
| -3 → -2.5 (fav) | Often worth worse price |
| +3 → +3.5 (dog) | Often worth worse price |
| +6.5 → +7 | Valuable on dogs |

See @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md for situational angles (weather, rest, division, backup QB).

### Market menu

| Market | Notes | CLV tracking |
|--------|-------|--------------|
| Spread / ML / total | Highest liquidity | **Primary** — log open vs close |
| Player props | Higher hold (~30¢ vig on soft books) | Secondary; more FLB on longshots |
| SGP | Correlation priced — see @concepts/parlay-and-correlated-bets.md | Usually -EV unless correlated edge |
| Futures | Division, SB — capital locked months | Low frequency |
| Live | Fast moves on drives | Supplement pre-game; pre-set rules |

### Process (season-long) [CONFIRMED]

1. **Line shop** across Hard Rock + FanDuel + others for best number
2. **Flat 1–2% units** — @concepts/bankroll-management.md
3. **Track CLV** — positive close beat = edge signal stronger than W-L
4. **Avoid parlay-core strategy** — hold compounds per leg

### Season rhythm

| Phase | Betting notes |
|-------|---------------|
| **Jun–Aug** | BBM7 drafts; futures move on camp news |
| **Preseason** | Unreliable lines, low limits — mostly ignore for +EV |
| **Regular season** | Sun/Mon/Thu slates; injury report **Wed/Fri** moves |
| **Playoffs** | Tighter lines; public on favorites |

### Injury / news cadence

- **Wed** — initial practice report
- **Fri** — final injury designations (major line moves)
- **Inactive lists** — 90 min pre-kick (props, totals)

Cross-link DFS: same OUT tags move FanDuel ownership and Underdog ADP.

### Live betting hygiene

- Markets overreact to early TDs; slow starts can improve live unders
- Do not size live bets larger than pre-game unit — set rules before kickoff

### Open-source ML note

Gemini landscape cites NBA ML repos as analog class — **NFL models need separate validation**; see @sources/gemini-github-sports-betting-landscape-2026-05-30.md.

## Snippets

> "If you consistently beat [the closing line] … you are very likely betting with a real edge." [Source: @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md]

> "Hard Rock's quality of NFL odds – 20-cent vig on standard markets and 30-cent vig on secondary opportunities." [Source: @sources/web-sportsbookreview-hard-rock-bet-2026-06-20.md]
