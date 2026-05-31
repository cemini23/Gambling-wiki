# LESSONS — Gambling Wiki

Meta-lessons about **how we work** (not what we learned about betting). Operational log lives in `wiki/log.md`.

## L1 — Scope split from osint-wiki (2026-05-31)

**Lesson:** Prediction markets appear in both wikis. **Gambling-wiki** owns retail product knowledge (fees, rules, behavioral edges, sportsbook-style strategy). **Osint-wiki** owns automation (bots, LP, CeminiSuite, regulatory/compliance for trading stack). When ingesting, ask: *"Would a human bettor care, or an engineer deploying code?"* — route accordingly.

## L2 — Don't duplicate Kelly/FLB — cross-link (2026-05-31)

Kelly criterion and favorite-longshot bias have **general theory** (here) and **Polymarket-specific implementations** (osint-wiki). Write the general page here; link to `@osint-wiki/concepts/kelly-sizing-quarter.md` for quarter-Kelly bot defaults. Update both sides when maturity promotes.

## L3 — Phase-0 paid tools before recommending (2026-05-31)

Odds services, copy-trading alerts, and "AI pick" products often market inflated ROI. Entity pages get GO/CONDITIONAL-GO/NO-GO after TOS + sample-track review — same discipline as osint tool evals, different failure mode (account limits, stale lines, -EV churn).
