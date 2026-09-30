---
title: Unabated
type: entity
tags: [entity, tool, sports-betting, education, +ev, sharp]
keywords: [unabated, ev, kelly, sharp-line, originators, education]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/kelly-criterion-betting.md
  - concepts/line-shopping-and-clv.md
  - concepts/sharp-vs-soft-books.md
  - concepts/bankroll-management.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - entities/tools/pickfinder.md
maturity: draft
created: 2026-05-31
updated: 2026-09-30
---

## Relations

- @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md — EQt2sq0_s64, KpNwHBJikoM

## Raw Concept

**Unabated** — sports betting education and tooling brand emphasizing **+EV process** (edge, Kelly, sharp-line comparison) over pick selling.

## Narrative

### What they teach (from operator YouTube batch)

1. **Process over picks** — profit from small, repeatable edges, not lottery long shots
2. **Expected value (EV)** — compare offered price to true probability; coin-flip pricing demo (+110 vs fair)
3. **Sharp line benchmark** — e.g. total 51½ at soft book vs 52½ sharp reference = potential edge
4. **Kelly Criterion** — stake ≈ edge ÷ odds; warns on **full Kelly** variance → use fractional Kelly
5. **Information hierarchy** — **originators** vs **downstream** bettors; syndicate/bankroll paths [Source: KpNwHBJikoM]

### Background cited

Presenter Jack: ex-**blackjack** card counter → sports bettor [Source: EQt2sq0_s64] — aligns with `@concepts/casino-game-house-edge.md` crossover discipline.

### Phase-0 checklist — closed 2026-09-30

| Check | Result |
|-------|--------|
| **Free tier** | **None.** Paid only. A 5-day trial runs **$15** (reported free with a promo code) [TENTATIVE] |
| **Props+ / Essentials** | **$99/mo** or **$83/mo** billed annually [TENTATIVE — one source quotes $67/$49] |
| **Premium** | **$199/mo** or **$132–$167/mo** billed annually. Adds the Unabated Line (vig-free fair odds), live bets, futures simulators [TENTATIVE] |
| **Add-ons** | NBA $199/mo · Edge Rusher **$250/week** · WNBA $199/mo · College Football $149/mo · CFL $99/mo · Tennisform $55/mo · Concierge $799/mo (requires Premium) |
| **API / enterprise** | **$3,000/mo** — WebSocket, sales call required, no free tier |
| **Refund** | Trial-gated; no published money-back guarantee found [NEEDS VERIFICATION 2026-09-30] |
| **Jurisdiction** | US sharp-bettor market. **No prediction-market coverage** — sportsbook fair-odds only |
| **CLV track record** | The "**Unabated Line**" is a vig-free consensus built from books that reach the closing line fastest. It is a fair-odds benchmark, **not** a published bet-by-bet CLV ledger [TENTATIVE] |
| **Overlap vs OddsJam** | Same price band (~$199/mo premium) but a different philosophy: Unabated does **fair-odds modelling**, OddsJam does **+EV/promo alerts**. Neither scans prediction markets |

### Verdict

**REFERENCE / CONDITIONAL-GO** — sharp betting literacy and a de-vig benchmark, at a real price. Fits `@concepts/sports-betting-fundamentals.md`, `@concepts/vig-and-hold.md`, and `@concepts/kelly-criterion-betting.md`. **Not a sportsbook and not a PM scanner.**

Phase-0 closed 2026-09-30. Buy decision belongs to the operator: $83–$199/mo is significant, and the program already has free de-vig tooling in `@scripts/daily_edge_card.py` + `@concepts/daily-edge-card.md`. Do not subscribe without a CLV-ledger plan to measure whether it pays for itself.

**Marketing caution:** the vendor claim that "96% of members become winning bettors" is unverifiable. Ignore it.

## Snippets

> "This full Kelly Criterion is very risky … bet a fraction of Kelly such as a quarter Kelly." [Source: EQt2sq0_s64 via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]

> "Beating sportsbooks … it's not about picks." [Source: KpNwHBJikoM via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]
