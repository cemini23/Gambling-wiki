---
title: "Kelly (1956) — A New Interpretation of Information Rate"
type: source
tags: [source, paper, kelly-criterion, position-sizing]
keywords: [kelly-1956, information-rate, optimal-betting, fractional-kelly]
related:
  - concepts/kelly-criterion-betting.md
  - concepts/bankroll-management.md
  - concepts/vig-and-hold.md
  - concepts/sports-betting-fundamentals.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
read_status: deep-read
---

## Relations

- @concepts/kelly-criterion-betting.md — retail formulas derived here
- @osint-wiki/sources/kelly-1956-information-rate.md — canonical deep-read + PM bot linkage

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A New Interpretation of Information Rate |
| Author | J. L. Kelly, Jr. (Bell Telephone Laboratories) |
| Journal | Bell System Technical Journal, Vol. 35, pp. 917–926, July 1956 |
| Location | `raw-sources/A New Interpretation of Information Rate.pdf` (cemini-librarian bulk retired 2026-06) |
| Retrieved | 2026-05-31 (cross-wiki from @osint-wiki) |
| Read status | deep-read |

## Narrative

Foundational paper linking Shannon information rate to **optimal bet sizing**. For retail bettors: Kelly gives the growth-maximizing fraction when you have an edge; fractional Kelly (½, ¼) is standard because `p` is never known exactly.

### Results that matter for wagering

1. **Fair odds:** bet proportional to your estimated win probability `q(s|r)` — posted odds cancel when fair.
2. **Unfair odds (no take):** any positive edge increases growth rate; still bet `q(s|r)` ignoring posted prices in the fair-odds limit.
3. **Track take:** constrained optimization — cannot cancel bets; water-filling threshold for which outcomes to play.

### Retail application

Use Kelly as **upper bound**, then apply bankroll caps (`@concepts/bankroll-management.md`). Never full-Kelly on correlated same-slate bets without portfolio adjustment.

## Snippets

> "If the input symbols to a communication channel represent the outcomes of a chance event on which bets are available at odds consistent with their probabilities (i.e., 'fair' odds), a gambler can use the knowledge given him by the received symbols to cause his money to grow exponentially." [Source: Kelly 1956 p.917]

> "the gambler ignores the posted odds in placing his bets!" [Source: Kelly 1956 p.922]
