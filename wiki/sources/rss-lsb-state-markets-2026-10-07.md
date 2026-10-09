---
title: "LSB state markets — Kentucky growth, Delaware parlay cards (2026-10-07)"
type: source
tags: [source, rss, us-sports-betting, state-revenue, parlay, k183]
keywords: [kentucky-handle, betmgm-growth, fanatics-growth, delaware-parlay-cards, hold-rate, hold-disparity]
related:
  - entities/sports/nfl-betting.md
  - concepts/vig-and-hold.md
  - concepts/parlay-and-correlated-bets.md
  - sources/daily-digest-batch-k183-2026-10-09.md
maturity: draft
read_status: deep-read
created: 2026-10-09
updated: 2026-10-09
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/
phase_0_verdict: REFERENCE — state revenue reports; hold disparity is the transferable finding
wire_status: policy_wired
---

## Relations

- @concepts/vig-and-hold.md — the Delaware hold disparity is a live example of hold by product
- @concepts/parlay-and-correlated-bets.md — parlay cards are the high-hold product here
- @sources/daily-digest-batch-k183-2026-10-09.md — K183 hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Feed** | Legal Sports Betting (`legal-sports-betting`) |
| **Author** | Michael Molter |
| **Published** | 2026-10-07 |
| **Articles** | 2 |
| **URLs** | https://www.legalsportsbetting.com/news/betmgm-fanatics-drive-kentucky-sports-betting-growth-10-07-2026/ · https://www.legalsportsbetting.com/news/parlay-cards-power-delaware-sports-betting-in-september-10-07-2026/ |

**Location:** the two archived `rss-legal-sports-betting-2026-10-07-{betmgm-fanatics-drive-kentucky…,parlay-cards-power-delaware…}.md` files.

## Narrative

### Kentucky — the incumbents stalled, two challengers grew

August 2026: **$206.3M** in bets, **+6.8%** year over year. Online was **$203M — 98.4%** of all action.

**The revenue story is hold, not handle.** Sportsbooks held **8.4%** versus **11.4%** a year earlier, so revenue **fell 20% to $17.1M** and the state collected **$2.47M**.

| Operator | Handle | Share move |
|----------|--------|-----------|
| DraftKings | $72.1M | — |
| FanDuel | $59.5M | revenue **−33%** to $5.5M; hold slid **13.7% → 9.3%** |
| **BetMGM** | **$17.3M** (**+79%** from $9.7M) | revenue **more than doubled** ($740k → $1.66M) |
| **Fanatics** | **$15.5M** (**+74%** from $8.9M) | revenue **−27%** on a 5.9% hold |
| bet365 | $21.2M (+3.5%) | — |
| Caesars | $9.3M (−3.6%) | — |

**The headline:** DraftKings and FanDuel combined for **$131.6M** — **64.8%** of the market, down from **70.2%** — but handled **essentially the same dollars** as last August (a difference **under $17,000**). Their duopoly share fell **5.4 points**.

**All the growth came from two challengers:** BetMGM and Fanatics added **$14.2M** in handle year over year — **"92% of Kentucky's online growth"** — taking **16.1%** of online handle, up from **9.9%**.

Since the September 2023 launch: **$8.4B** bet, **$907.4M** revenue, **$128.3M** in state tax. The 2026 monthly average is **$245M**, with **$10B** expected within months.

### Delaware — parlay cards carry the state

September: total handle **$25.1M**, down **9.1%** YoY, with tickets down **20.4%**.

**The concentration finding.** Lottery retailers took **$3.5M** of the $25.1M handle — **14%** — but contributed **$777,101** of the state's **$1.68M** share: **46.2%**.

| Venue type | Cents kept per dollar bet |
|-----------|--------------------------|
| **Retail parlay cards** | **24.7¢** |
| The three casino sportsbooks | **8.4¢** |

Per-dollar losses at the books: **Delaware Park 8.9¢ · Harrington 8.3¢ · Bally's Dover 6.4¢**. Retail parlay players lost **between 2.8× and 3.9× more per dollar** than sportsbook bettors.

**Overall:** hold rose **11.8% → 17.3%**; net proceeds **+30.2%** to $2.67M; state share **+22.3%** to $1.68M — its best month since December 2025. Average ticket **+14.3%** ($19.16 → $21.90) on 294,484 fewer tickets.

The article's own caveat on the handle dip: the window ran **Aug. 31–Sept. 27**, capturing **three** NFL Sundays versus **four** in 2025. Per NFL Sunday, handle was about **$8.4M** versus **$6.9M** — so the decline is a calendar artifact.

**Operators:** Delaware Park $13.6M (−11.8%), net +56.9%. Harrington $4.9M (−13.5%), net +133.2%. **Bally's Dover $3.1M (+21.7%)** — the only book to grow handle and the only one to earn less (−17.2%).

## Snippets

> "92% of Kentucky's online growth." [Source: LSB, on BetMGM + Fanatics]

> Retail parlay players lost "between 2.8 and 3.9 times more per dollar" than sportsbook bettors. [Source: LSB, Delaware]

## Dead Ends

- **State revenue reports are not actionable data.** They are published weeks late and describe handle already settled.
- **The Delaware 24.7¢ figure is a product fact, not an edge.** It is the house's hold on parlay cards — a reason to avoid them, not to play them. Compare `@concepts/vig-and-hold.md`.
- **Kentucky's hold drop is the item to watch.** An 11.4% → 8.4% slide on flat handle is what a competitive market looks like on the books' side.
