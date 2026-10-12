---
title: "Daily digest batch K184 — Stake Brazil, Sharp W5 final, RotoBaller W6, MLB pennant (2026-10-12)"
type: source
tags: [source, batch, k184, industry, nfl, fantasy, mlb]
keywords: [stake-brazil, provisional-measure, sharp-football, waiver-wire, al-pennant, seminole-counts]
related:
  - sources/rss-sbc-brazil-stake-2026-10-09-12.md
  - sources/rss-sharp-football-week5-final-2026-10-09-11.md
  - sources/rss-rotoballer-week5-6-2026-10-11-12.md
  - sources/rss-lsb-mlb-al-pennant-2026-10-09.md
  - sources/rss-pm-legal-2026-10-07-09.md
  - sweeps/2026-10-12-daily.md
maturity: draft
read_status: deep-read
created: 2026-10-12
updated: 2026-10-12
phase_0_verdict: REFERENCE — 24 RSS; 1 cross-feed duplicate merged into K183
wire_status: policy_wired
---

## Batch summary

24 inbox files → **4 source pages + this hub**, plus an **enrichment of the K183 Seminole page**.

| # | Source | Phase-0 | Wire |
|---|--------|---------|------|
| 1–5 | SBC — Stake Brazil ×2, Betfred, Sky Bet, Flutter/Entain | OOD | wont_wire |
| 6–16 | Sharp Football W5 final — bets, injuries, leader odds, DFS | MIXED | policy_wired |
| 17–21 | RotoBaller — W5 starts/sits ×3, W6 waivers ×2 | REFERENCE | policy_wired |
| 22 | LSB MLB — AL pennant | OOD | wont_wire |
| 23 | LSB Seminole v DraftKings | **cross-feed duplicate** | merged into K183 |
| 24 | (counted above) | — | — |

## Recommended actions

1. **Stake's Brazil injunction lasted one day.** Judge di Salvo of the Federal Regional Court of the 3rd Region suspended it on 2026-10-09 because treating one operator differently from compliant rivals was unequal. **Justice Fux will not rule until after the runoff on 2026-10-25.**
2. **Flutter's leadership churn continues** — Dan Taylor took over as Group CEO on 2026-10-01, and Neil Banbury is the new Sky Betting & Gaming MD. Flutter's share price is **down over 63% year over year**.
3. **Sharp Football's free tier is confirmed again**: best bets, injuries, and leader odds are free; **DFS picks are paywalled**. Use the free ones.
4. **The rushing-leader volume rule is the keeper** — 15 of 15 weekly leaders from winning teams in 2025, and through four weeks **no back topped 100 yards on fewer than 17 carries**.
5. **The Stale-URL problem is now confirmed for Sharp Football** — see below.

## Process note — two ingest defects found

**1. Cross-feed story duplicates are invisible to preingest.** The LSB article on the Seminole lawsuit covers the same story as the LSR article already ingested in K183. preingest indexes **URLs and titles**, so a second feed reporting the same event matches neither. It reported NEW.

**Handled by merging:** the LSB version added the **five counts**, the **absent breach-of-claim**, the product launch dates, and the compact economics. That detail is now on `@sources/rss-pm-legal-2026-10-07-09.md` rather than in a second page.

**2. Sharp Football's RSS stubs carry URLs that 404.** All eleven stub URLs returned 404; the canonical paths differ in shape (`…/week-5-nfl-best-bets-against-the-spread-game-total-picks/` → `…/best-bets-picks-nfl-week-5-2026/`). Fetching required reconstructing the real URLs.

**Consequence:** the poller is storing a URL that cannot be fetched. Worth checking whether `rss_digest.py` normalises the link or takes a canonical hint.

## Notes

- **No briefs dispatched.** No incoming brief referenced a missing page.
- **Archive pending.**
