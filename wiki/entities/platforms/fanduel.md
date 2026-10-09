---
title: FanDuel
type: entity
tags: [entity, platform, sportsbook, dfs, us-legal, nfl]
keywords: [fanduel, fd, sportsbook, dfs, nfl-gpp, half-ppr, showdown]
related:
  - entities/platforms/draftkings.md
  - entities/platforms/hard-rock-bet.md
  - concepts/sports-betting-fundamentals.md
  - concepts/dfs-strategy-overview.md
  - concepts/sharp-vs-soft-books.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - entities/people/rufus-peabody.md
  - sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md
  - sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md
  - sweeps/2026-06-20-tier2-w8-nfl.md
  - sources/brief-k222-k231-pm-retail-awareness-2026-08.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
  - sources/brief-k169-nfl-week1-ready-2026-08-31.md
  - sources/rss-lsr-nfl-app-downloads-pm-share-2026-09-24.md
  - sources/rss-lsr-pm-industry-2026-09-29-30.md
  - sources/daily-digest-batch-k180-2026-10-02.md
  - sources/rss-operator-scrutiny-2026-10-07-08.md
  - sources/daily-digest-batch-k183-2026-10-09.md
maturity: validated
created: 2026-05-31
updated: 2026-10-09
---

## Relations

- @entities/platforms/draftkings.md — primary US competitor (DFS + book)
- @entities/platforms/hard-rock-bet.md — cross-shop sportsbook peer (W8)
- @concepts/dfs-strategy-overview.md — NFL GPP framework
- @sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md — K124 FanDuel-relevant GPP playbook
- @sources/brief-k222-k231-pm-retail-awareness-2026-08.md — Predicts sports → Crypto.com (Q2 2026)
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — NFL official betting partner (with DK / Fanatics)
- @sources/brief-k169-nfl-week1-ready-2026-08-31.md — Week-1 DFS: Jacobs / Charbonnet / Tyson out; Nacua Q

## Raw Concept

Major US legal operator (Flutter-owned). **W8 lanes:** NFL DFS GPP/tournaments + soft-book line shop vs Hard Rock handle.

## Narrative

### Sportsbook (CLV cross-shop)

Same **soft book** retail profile as DraftKings. Industry reviews often rank FanDuel among **sharper spread prices** on NFL — use for line shopping even when primary handle is Hard Rock.

### FanDuel Predicts (PM, Aug 2026) [CONFIRMED via EH]

Q2: sports/novelties on **Predicts** move to **Crypto.com**; CME retained for financials. Flutter flagged **~$50M** market-making revenue for 2026 ($6M in Q2). Predicts is **not** the FanDuel sportsbook line — shop it as a third venue (book vs Kalshi vs Predicts/Crypto.com). Hub: `@sources/brief-k222-k231-pm-retail-awareness-2026-08.md`.

### VIP video letter from Congress (K183, 2026-10-08) [CONFIRMED]

**Sen. Richard Blumenthal** (CT), **Rep. Paul Tonko** (NY), and **Rep. Valerie Foushee** (NC) wrote to FanDuel President **Christian Genetski**, replying to FanDuel's own 2026-09-24 letter — which said the company sent VIP bettors **"approximately 30 such videos of athletes and entertainers over the last two years"** as loyalty rewards.

The lawmakers argue that **contradicts** FanDuel's position that it does not encourage continued gambling.

**The named case:** **Terry Thompson** allegedly lost **$1.5M** and received a personalized **Bryce Harper** video. Harper said he "did not know what the purpose of the video he created was." Thompson is suing FanDuel and DraftKings, claiming they "preyed on him despite a clear gambling addiction."

**Demanded by 2026-10-20:** every personalized VIP video; per-video bet amounts, problem-gambling resource requests, recipient-selection rationale, and VIP-host steps to avoid problem gambling; athlete/entertainer awareness; and FanDuel's problem-gambling screening tools.

**Why it matters:** the request is for the **decision records** behind each video, not the marketing. Hub: `@sources/rss-operator-scrutiny-2026-10-07-08.md`.

**Analyst note (same batch):** Macquarie's Chad Beynon trimmed the **Flutter target to $128** (from $150) alongside six other gaming names, citing lower sports betting hold and **higher predictions investment** — the books spending to compete with the markets they want regulated.

### Flutter parent — record low (K180, 2026-09-29) [TENTATIVE]

Flutter Entertainment, FanDuel's parent, hit an **all-time low** after **Brazil banned online betting** — days before CEO Peter Jackson departed. Shares fell **more than 7%** from Friday's close into Monday's open, and Flutter has lost roughly **three-quarters of its value** since peaking above **$313 in August 2025**.

| Driver | Impact |
|--------|--------|
| **Brazil ban** | Betting + iCasino suspended ahead of an **Oct. 6** deadline; ~**$70M** revenue and ~**$20M** adj. EBITDA lost if the shutdown runs through 2026. Paid ~**$350M** for a **56%** NSX stake in 2025 |
| **India ban** | ~**$250M** revenue lost in 2026 and **$310M** in 2027; Junglee paid operations shut in August after a **$237M** investment |
| **US performance** | FanDuel held a leading **39%** of U.S. sportsbook GGR in Q2, but sportsbook revenue fell **15% YoY** and U.S. adj. EBITDA dropped **70%** to **$119M** |
| **Promo rebuild** | Flutter under-reinvested 2025 NFL winnings into promotions; ~**$270M** committed to rebuilding momentum, +**$40M** in higher state taxes |

**Operator relevance:** FanDuel is the operator's **primary DFS lane**. A parent under margin pressure can cut promotions or tighten DFS overlays. Watch promo generosity through the season rather than assuming the prior baseline. Hub: `@sources/rss-lsr-pm-industry-2026-09-29-30.md`.

### NFL DFS (operator primary DFS lane)

| Setting | FanDuel NFL |
|---------|-------------|
| Scoring | **Half-PPR** |
| Team stack cap | **4** players from one team (vs DK 5) |
| Main slates | Sun/Mon/Thu + alt slates |
| Showdown | Single-game; high correlation |

### GPP strategy summary [CONFIRMED — @sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md]

**Goal:** top-1% finish, not min-cash.

1. **Game stacks** — default 3×1 (QB + 2 pass-catchers + opp WR); 3×2 in smaller fields; 4×1 on short slates
2. **Game selection** — high Vegas totals, low QB pressure rate, rising totals through week
3. **RB workload** — secure-touch backs for floor; chalk RB ownership acceptable
4. **WR/TE leverage** — lower-owned pass-catchers (UPWR thesis: targets + air yards)
5. **Flex** — RB often best on half-PPR; **avoid TE in flex** for GPP ceiling
6. **Salary** — leave ≤ $500 on table
7. **MME (150 max)** — 3 game environments × both QBs; 5–10 RBs; 15–30 WRs; 4–6 TEs; 4–8 DST; max 2 off-stack players per team

### Week 1 2026 DFS notes (K169)

Do not treat **Jacobs**, **Charbonnet**, or **Tyson** as starters. Price **Lloyd / Brooks / Kaleb Johnson** (GB), **Jadarian Price** + Holani (SEA vs NE Wed 9/9), and **Olave** as NO WR1. **Nacua** is Questionable for Melbourne TNF 9/10 — wait T-90. Stokastic = member CSV only; do not scrape Sims HTML. Hub: `@sources/brief-k169-nfl-week1-ready-2026-08-31.md`.

### Sunday Million min-cash (operator app, 2026-09-30)

| Week | Min-cash | Note |
|------|----------|------|
| 1 | not in the app | Do not invent it |
| 2 | 113.78 | A 120 would have cashed |
| 3 | 130.3 | Best lineup was 126.26, short by 4.04 |

Do not store 130.3 as a projection weight. The line moved 16.5 points in one week.

### Bankroll

GPP = high variance — size entries per @concepts/bankroll-management.md; separate from Hard Rock sportsbook roll and Underdog BBM7 draft budget.

### Tools

- `@entities/tools/pydfs-lineup-optimizer.md` — FOSS lineup gen (MIT; see `scripts/fanduel_slate_optimize.py`)
- `@entities/tools/stokastic-dfs.md` — recommended paid projections/sims (W8)
- `@entities/tools/fantasylabs-dfs.md` — alternate paid + CSV export (ETR bundle)

## Snippets

> "On half-point PPR sites like FanDuel … consider using a running back in your flex spot for stability." [Source: @sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md]

> "When entering high-stakes or large-field GPP contests, the goal is to secure a top finish, not just to cash." [Source: same]
