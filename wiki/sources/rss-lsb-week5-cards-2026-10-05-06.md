---
title: "LSB cards — NHL under, MNF props, AFC North, MLB props, Super Bowl 61 (2026-10-05/06)"
type: source
tags: [source, rss, nhl, nfl, mlb, odds, k182]
keywords: [sharks-stars-under, bijan-robinson, devaughn-vele, afc-north-odds, super-bowl-61, dustin-may, ty-france]
related:
  - entities/sports/nhl-betting.md
  - entities/sports/nfl-betting.md
  - sources/rss-lsb-week4-game-cards-2026-10-02.md
  - sources/daily-digest-batch-k182-2026-10-07.md
maturity: draft
read_status: deep-read
created: 2026-10-07
updated: 2026-10-07
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/
phase_0_verdict: REFERENCE — cards across four sports; mechanisms only, no auto-enter
wire_status: policy_wired
---

## Relations

- @entities/sports/nhl-betting.md — the NHL card continues that vertical
- @entities/sports/nfl-betting.md — MNF props, AFC North futures, Super Bowl futures
- @sources/rss-lsb-week4-game-cards-2026-10-02.md — the prior week's cards from the same feed
- @sources/daily-digest-batch-k182-2026-10-07.md — K182 hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Feed** | Legal Sports Betting (`legal-sports-betting`) |
| **Published** | 2026-10-05 → 2026-10-06 |
| **Articles** | 5 |
| **URLs** | https://www.legalsportsbetting.com/news/best-bet-under-6-5-in-sharks-stars-on-monday-s-nhl-slate-10-05-2026/ · https://www.legalsportsbetting.com/news/best-odds-and-player-props-for-falcons-vs-saints-mnf-clash-10-05-2026/ · https://www.legalsportsbetting.com/news/browns-tied-for-first-yet-1500-in-afc-north-odds-10-05-2026/ · https://www.legalsportsbetting.com/news/best-brewers-vs-padres-props-dustin-may-ty-france-10-06-2026/ · https://www.legalsportsbetting.com/news/super-bowl-odds-movement-post-week-4-rams-reclaim-lead-10-06-2026/ |

**Location** (`cemini-egress-fi:/opt/cemini-bulk/research/gambling/`): the five archived `rss-legal-sports-betting-2026-10-0{5,6}-*.md` files.

## Narrative

### NHL — Sharks @ Stars: Under 6.5 (−117)

**Best bet: Under 6.5.** The total sits **0.2 above the 6.3 average** from games involving both teams last season.

| | Dallas | San Jose |
|---|--------|----------|
| Record | **0-2-0** (first time since 2019) | 2-0 (both OT wins, both home) |
| Avg goals in their games | 6.04 | 6.57 |
| Shots/game | **25.3** | **25.8** |

The league averages **6.15** goals this season, matching last year's 6.16. Both clubs sit among the **seven lowest-volume shooting teams** (league average 27.8 shots); projected combined shots are **~53.5**, 2.2 below the NHL's 55.7.

The signal: Dallas scored 273 goals last season on thin volume with a **league-best 13.2% shooting percentage** — regression-prone. This season Dallas has **one goal in two games on 55 shots (1.8%)**, and San Jose's nine goals came from **5.4 expected**, with a PDO around **104** — above the 102 unsustainable-luck threshold.

**Risks to the under:** Dallas' power play converted **28.6%** last season (2nd in the NHL) while San Jose's kill was **76.4%**; two Dallas PP goals carry most of the way to seven. Goalie **Yaroslav Askarov** was **18.9 goals worse than expected** over 47 games last season.

Futures: Stars ML −195 to −205 (needs a **66–67%** win rate, above the 63.4% home mark last season), Sharks +171 to +173.

> "We're not creating at a high level right now." — Glen Gulutzan, Stars coach

**Mechanism:** the under case rests on **shot volume plus shooting-percentage regression**, not on defense. Two teams in the bottom seven for shot generation cannot sustain a high total.

### NFL MNF — Falcons @ Saints: total and two props

Three plays, all at −115:

| Play | Case |
|------|------|
| **Over 47.5** (−115) | New Orleans is top-10 scoring (27/game); Atlanta scored **35** in Penix's season debut. Both have playmakers and unreliable defenses |
| **Bijan Robinson over 85.5 rush yds** (−115) | 83 in W1, 72 in W2, then **194 in W3** vs Green Bay once Penix started and Atlanta led. New Orleans is missing **three run defenders** — Anfernee Jennings (knee), Carl Granderson (ankle), Kaden Elliss (calf) — and ranked **27th** (128.7 rush yds/game) even before those injuries |
| **Devaughn Vele over 44.5 rec yds** (−115) | 172 yards on 15 catches through three games. Atlanta ranks **30th** in passing yards allowed (>260/game) and is missing A.J. Terrell. Vele cleared 44.5 in two of three |

### NFL futures — AFC North

Cleveland is **3-1** and tied with Baltimore atop the division, yet sits at **+1500** — the same price as the **2-2** Steelers.

| Team | Record | Price | Move |
|------|--------|-------|------|
| Ravens | 3-1 | **−145** (59.18%) | from −135 |
| Bengals | 2-2 | +180 (35.71%) | unchanged |
| **Browns** | 3-1 | **+1500** (6.25%) | **from +2500** |
| **Steelers** | 2-2 | **+1500** (6.25%) | **from +900** — the board's biggest drop, 3.8 points |

Cleveland leads on division record (1-0 vs Baltimore's 0-0). At +1500 a Browns bet breaks even only if they win the division **once in 16 tries**. Baltimore has all **six** division games left, two against Cleveland; Cleveland has five.

The board orders by **net EPA per play**: Baltimore 9th (+0.06), Cincinnati 12th (+0.04), Pittsburgh 20th and Cleveland 21st (both −0.04) — per nflverse through four games, with the article's own caveat that four games is the low end of the 4–6 needed for EPA to settle, and that the figures are **not opponent-adjusted**.

The telling line: the board rates **Cincinnati's +12 point differential and 12th-ranked net EPA above the head-to-head result** — Pittsburgh beat Cincinnati 30-27 in Week 3, yet the price gap is 29.5 points.

### MLB — Brewers @ Padres Game 3 (NLDS)

| Play | Price | Case |
|------|-------|------|
| **Dustin May under 8.5 pitching outs** | **+115** | May exceeded 8.5 outs in only **one** of his last three regular-season starts (and that was exactly nine). Manager Pat Murphy pulled Logan Henderson after five innings in Game 2 despite one earned run and only 72 pitches — below Henderson's average. With a clinch chance and a rest day, Murphy may lean on the bullpen |
| **Ty France over 1.5 hits+runs+RBI** | −110 | 2nd half (63 games): **.321 / 10 HR / 39 RBI / 35 R** — 2.37 combined per game. Postseason: **.467**. vs May (13 PA): 4 hits, 1 HR. vs Milwaukee (19 PA): 7 hits, 1 HR |
| **France "laser" HR, 105+ MPH exit velo** | **+1700** | A longshot. In Game 1 a 105.3 mph, 49-degree ball hit the roof and was ruled out. **>62%** of his home runs this season were 105+ mph, so +1700 is roughly **double his +750** to homer at all |

### NFL futures — Super Bowl 61 after Week 4

**Top of the board:** **Rams +650** reclaimed sole favouritism over **Bills +700**; then 49ers +800, Ravens +850, Chiefs and Seahawks both +900.

| | Team | Move | Driver |
|---|------|------|--------|
| **Riser** | Jaguars | **+2200 → +1400** | Beat Cincinnati to reach 3-1; allowed 53 points (2nd-best), scored 104 (12th). Division has two 0-4 teams (Texans +4500, Titans +100000) |
| **Riser** | Falcons | **+12000 → +8500** | Beat New Orleans 45-24. With Penix at QB they average **40 points/game**, versus **8** with Cooper Rush |
| **Faller** | Chargers | **+10000 → +12500** | Fell to 0-4; next five are Denver, KC, the Rams, Houston, Baltimore |
| **Faller** | Jets | **+20000 → +50000** | Lost 12-23 to Chicago with **157 total yards and seven first downs**, dropping to 1-3 |

The Rams moved up on "a Rams win in Puka Nacua's return paired with Buffalo's home loss to the New England Patriots." Only the 49ers, Chiefs, and Vikings remained undefeated.

## Snippets

> "The board rating Cincinnati's plus-12 point differential and 12th-ranked net EPA above the head-to-head result." [Source: LSB AFC North, 2026-10-05]

> "We're not creating at a high level right now." — Glen Gulutzan [Source: LSB NHL, 2026-10-05]

## Dead Ends

- **Five articles, one feed, affiliate disclosure.** Use the mechanisms — shot-volume plus shooting-percentage regression, injury-driven run-defense collapse, EPA-vs-record divergence — not the selections.
- **MLB is out of the operator's lanes.** The Brewers-Padres card is recorded for the prop-shaped thinking (a manager-tendency read on pitching outs, an exit-velocity split), not as a lane.
- **No CLV sample in any of these.** Nothing here is a closing-line record.
- **Do not auto-enter.** A human types the ticket.
