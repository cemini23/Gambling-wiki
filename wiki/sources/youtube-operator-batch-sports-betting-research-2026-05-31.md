---
title: "YouTube — operator sports betting research batch (13 videos, May 2026)"
type: source
tags: [source, youtube, sports-betting, research, clv, kelly, sharp, tools]
keywords: [unabated, odds-jam, pickfinder, rufus-peabody, linemaker, ev, devig, pinnacle, novig]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - concepts/sharp-vs-soft-books.md
  - concepts/kelly-criterion-betting.md
  - concepts/vig-and-hold.md
  - concepts/bankroll-management.md
  - concepts/prediction-markets-crossover.md
  - entities/tools/unabated.md
  - entities/tools/odds-jam.md
  - entities/tools/pickfinder.md
  - entities/people/rufus-peabody.md
  - entities/platforms/pinnacle.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
maturity: validated
read_status: deep-read
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @sources/youtube-operator-batch-wc-bbm-2026-05-31.md — prior operator batch (WC + BBM7)
- @entities/tools/unabated.md — Unabated cluster (2 videos)
- @entities/tools/odds-jam.md — model-building tutorial
- @entities/people/rufus-peabody.md — Wharton PM interview

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Operator YouTube drop — sports betting research, EV, and tools |
| **Author** | Operator paste (13 URLs) |
| **Type** | Auto-caption transcript synthesis via `yt-dlp` |
| **Videos** | 13 |
| **Retrieved** | 2026-05-31 |
| **Read status** | deep-read |

**Credibility:** Mix of sharp-education (Unabated, Wharton) and promo/tool tutorials (PickFinder, LINEMAKER AI). Treat P&L claims and product edge stats as `[TENTATIVE]`.

## Narrative

### Batch themes

1. **Process over picks** — +EV is finding mispriced lines, not predicting winners (Unabated, Extranet Shaquille).
2. **Sharp line as benchmark** — Pinnacle/Circa for CLV and model devig (OddsJam tutorial, Unabated, DubClub).
3. **Kelly + bankroll** — edge ÷ odds; fractional Kelly for variance (Unabated, OddsJam).
4. **Research workflows** — line-movement filters (LINEMAKER), game-film watching (youngkardi), stat stacks (Calling Our Shot, Goon).
5. **Prediction markets crossover** — Rufus Peabody on Novig vs books, limits, fees (Wharton) — no Kalshi/Polymarket in this batch.

---

### Video catalog

| ID | Channel | Title | Dur | Lane |
|----|---------|-------|-----|------|
| [EQt2sq0_s64](https://www.youtube.com/watch?v=EQt2sq0_s64) | Unabated | Winning Sports Betting Explained — Step-by-Step | 8m | EV, Kelly, sharp line |
| [KpNwHBJikoM](https://www.youtube.com/watch?v=KpNwHBJikoM) | Unabated | Beating Sportsbooks: It's Not About Picks | 7m | Originators vs downstream |
| [M1T0OlG3XEU](https://www.youtube.com/watch?v=M1T0OlG3XEU) | Knowledge at Wharton | Rufus Peabody: PM and Future of Analytics | 57m | Novig, props, sharp limits |
| [3FpV-iOXvQo](https://www.youtube.com/watch?v=3FpV-iOXvQo) | DubClub | From Data Scientist to Pro Sports Bettor | 86m | Capper ops, Pinnacle access |
| [XZvXWVztJoY](https://www.youtube.com/watch?v=XZvXWVztJoY) | Extranet Shaquille | What Everyone Gets Wrong About Gambling on Sports | 14m | EV, vig, CLV, arbs |
| [6HN-d9mC0DI](https://www.youtube.com/watch?v=6HN-d9mC0DI) | OddsJam | Building Your Own Betting Model | 50m | Devig, Pinnacle benchmark, Kelly |
| [tRZzx1Alw5A](https://www.youtube.com/watch?v=tRZzx1Alw5A) | PickFinder | PickFinder Tutorial | 9m | Research tool walkthrough |
| [7G2TtK80Hf4](https://www.youtube.com/watch?v=7G2TtK80Hf4) | Calling Our Shot | Sports Betting 101 Ep 3 — Research | 13m | Props, DFS DvP, totals |
| [jo-f7HwTBZE](https://www.youtube.com/watch?v=jo-f7HwTBZE) | Goon | Best Research Apps 2026 | 5m | Action, StatMuse list |
| [wtE5aXrUHzQ](https://www.youtube.com/watch?v=wtE5aXrUHzQ) | LINEMAKER SPORTS | Research Best Game Start-to-Finish | 14m | Whiteboard checklist, key numbers |
| [nimjqe3P5lA](https://www.youtube.com/watch?v=nimjqe3P5lA) | LINEMAKER SPORTS | Secret to Finding Best Games | 9m | Line-movement circle method |
| [njTt4UX_IxM](https://www.youtube.com/watch?v=njTt4UX_IxM) | LINEMAKER SPORTS | Find Winning Bets in 60 Seconds | 10m | AI promo — `[TENTATIVE]` edge claims |
| [u3VEGPWwKHc](https://www.youtube.com/watch?v=u3VEGPWwKHc) | youngkardi | How to Research Your Bets | 14m | Watch games, opening vs current line |

---

### Cluster summaries

**Unabated (EQt2sq0_s64, KpNwHBJikoM)** — Core retail education: small edges compounded; coin-flip EV demo; compare to sharp total; Kelly Criterion with **fractional Kelly** warning; sharps don't "pick more winners" — they bet price. Jack's background: blackjack card counting → sports.

**Wharton / Peabody (M1T0OlG3XEU)** — Career arc (props, Super Bowl week); **Novig** and sports **prediction markets** vs traditional books; **Pinnacle** as line reference; DK/FD **limit sharp winners**; bid-ask and fee drag on PM contracts; broker/middleman execution for size. Primary home for PM crossover detail: `@entities/people/rufus-peabody.md`.

**OddsJam model tutorial (6HN-d9mC0DI)** — Build models on **market prices**, not naive "last 5 games" stats; benchmark vs **Pinnacle/Circa**; **devig** juice from sharp lines; Kelly for bankroll; crossed-market **arb** example. Extends `@entities/tools/odds-jam.md` sportsbook lane.

**Extranet Shaquille (XZvXWVztJoY)** — Winning = **pricing knowledge**; vig on 50/50 markets; **CLV** example (promo line vs close); **arbitrage** intro; contrasts +EV poker/counters vs -EV casino.

**Research workflow cluster (LINEMAKER ×3, youngkardi, Calling Our Shot, Goon)** — Manual frameworks: line-movement filters, key spread numbers, offense/defense checklist, watch live games, Action/StatMuse/Odds Shark tool lists. Not quant — **hypothesis generation** before line shopping.

**PickFinder (tRZzx1Alw5A)** — SaaS research UI; Phase-0 before subscribe.

**DubClub (3FpV-iOXvQo)** — Capper business model: distribution + line timing, not beating Pinnacle's model; **Pinnacle/Bookmaker** as hard-to-ban sharp venues; bankroll/units for audience.

## Snippets

> "Sports betting isn't about picking winners … finding the small edges … grinding out a profit over time." [Source: EQt2sq0_s64]

> "Most sharp sports bettors don't work that way [pick winners]." [Source: KpNwHBJikoM]

> "Good sports betting is pricing knowledge." [Source: XZvXWVztJoY]

> "Closing line value or CLV … good deal at plus 150 and the CLV was minus 300." [Source: XZvXWVztJoY]

> "You can devig the market … remove the juice from Pinnacle." [Source: 6HN-d9mC0DI]

> "Kelly criterion is the best way to manage your bankroll." [Source: 6HN-d9mC0DI]

> "Books you can bet at and never get banned … Pinnacle … Bookmaker." [Source: 3FpV-iOXvQo]

> "Try to bet using logic over odds. Do not bet with your heart." [Source: 7r_r2VpPO30 — prior batch; same theme echoed in youngkardi/u3VEGPWwKHc on specialization]

## Dead Ends

- **LINEMAKER AI 60-second promo** (`njTt4UX_IxM`) — unverified edge percentages; marketing not validated
- **Goon app list** (`jo-f7HwTBZE`) — affiliate-style roundup; Phase-0 each tool individually
- **PickFinder / LINEMAKER** — product tutorials without independent CLV track record
