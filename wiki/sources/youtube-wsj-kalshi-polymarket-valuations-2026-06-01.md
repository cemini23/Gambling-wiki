---
title: "WSJ — How Kalshi and Polymarket are worth billions without a gambling license (R3)"
type: source
tags: [source, youtube, wsj, kalshi, polymarket, regulation, retail]
keywords: [r3, event-contracts, cftc, dcm, state-gaming, sports-volume, insider-trading]
related:
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/prediction-markets-crossover.md
  - concepts/sharp-vs-soft-books.md
  - concepts/sportsbook-pm-line-divergence.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/daily-digest-news-r1-r12-2026-06-01.md — sweep row R3
- @entities/platforms/kalshi.md — CFTC DCM, sports dominance, state fights
- @entities/platforms/polymarket.md — offshore vs US CFTC platform, insider rules
- @concepts/prediction-markets-crossover.md — retail vs osint-wiki regulation depth
- @osint-wiki/sources/polygnosis-2-polymarket-osint-2026-06-01.md — unrelated product lane; same PM ecosystem

## Raw Concept

| Field | Value |
|-------|-------|
| **URL** | https://www.youtube.com/watch?v=S2g0TwfecJE |
| **Show** | WSJ *The Economics Of* |
| **Transcript** | YouTube auto-captions (en), retrieved 2026-06-01 via `yt-dlp` |
| **Archive** | `raw-sources/youtube-wsj-S2g0TwfecJE.en.vtt` (local) |
| **Confidence** | [TENTATIVE] on valuations and % stats — journalism, not primary filings |

## Narrative

### Valuations and product framing

WSJ opens with exotic PM markets (Hormuz, BTC tick, aliens) and cites **Kalshi >$20B** and **Polymarket ~$9B** valuations amid hype. Core mechanic explained for retail: **event contracts** pay **$1 / $0** on yes/no; price ∈ [0,1] ≈ implied probability.

### Regulatory split (US retail)

| Platform | WSJ framing |
|----------|-------------|
| **Kalshi** | **CFTC-regulated** US DCM; event contracts as **swaps** under CFTC (same agency as commodity futures) |
| **Polymarket** | Main platform **offshore** for broader contract set; **2026** rollout of **CFTC-compliant US** offering noted |

Legal risk: sports on PMs triggered **state vs federal** fight — **39 states + DC** legalized sports gambling; **31** with online post-**2018 Supreme Court** reversal of federal ban. **Nevada** key battleground on whether PMs need **state gambling licenses**. Research firm cited: **~69%** of Kalshi volume from **19 states** without legal online sports betting [TENTATIVE].

Congress: bipartisan bill (CA + UT senators) to **ban sports** on prediction markets; CFTC chair (Trump appointee) asserts **exclusive authority** over DCM derivatives — “see you in court.”

### Sports vs books (retail edge cases)

- Kalshi **sports >70%** of volume (WSJ).
- Pro bettor **Frank Santolo** (Las Vegas): moved volume from books to Kalshi for **higher limits** — books limit/sharp-ban; PMs want **volume + fees** per trade.
- Kalshi marketing: “**not the house**” — complicated by internal **Kalshi Trading LLC** market maker (liquidity / price setting).
- **Polymarket** positioning: **>90%** audience as “information market”; median trader loss **<$10** (company-reported, WSJ) [TENTATIVE].

### Compliance tail risks

- Insider trading: Kalshi monitoring; PM updated rules (stolen info, illegal tips, outcome influence). **SF soldier** ~$400k Maduro market cited.
- WSJ close: possible **pendulum** — more prosecutions, stricter allowed-event boundaries.

**Not betting advice** — jurisdiction and product access change quickly; verify before wagering.

## Snippets

> "Koshi is fully regulated in the US while Poly Market's main platform operates offshore so it can offer more types of contracts." [Source: YouTube auto-captions S2g0TwfecJE, 2026-06-01]

> "It has surged to over 70% of its trading volume [sports on Kalshi]." [Source: same]

> "Sports books are notorious for kicking out professional bettors who are too successful. Prediction markets don't do that." [Source: same — Santolo segment]

> "About 69% of Kshi's volume came from 19 states that have not legalized online sports betting." [Source: same — gambling research firm, May report, TENTATIVE]

> "If it acts like gambling, if it's talks like gambling, it is gambling, right?" [Source: same — state AG perspective]

## Dead Ends

- Video does not provide executable fee tables — pair with R1/R2 digest rows for fee math
- Duplicate caption lines in auto-transcript — cleaned for narrative, not legal evidence
