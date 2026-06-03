# LESSONS — Gambling Wiki

Meta-lessons about **how we work** (not what we learned about betting). Operational log lives in `wiki/log.md`.

## L1 — Scope split from osint-wiki (2026-05-31)

**Lesson:** Prediction markets appear in both wikis. **Gambling-wiki** owns retail product knowledge (fees, rules, behavioral edges, sportsbook-style strategy). **Osint-wiki** owns automation (bots, LP, CeminiSuite, regulatory/compliance for trading stack). When ingesting, ask: *"Would a human bettor care, or an engineer deploying code?"* — route accordingly.

## L2 — Don't duplicate Kelly/FLB — cross-link (2026-05-31)

Kelly criterion and favorite-longshot bias have **general theory** (here) and **Polymarket-specific implementations** (osint-wiki). Write the general page here; link to `@osint-wiki/concepts/kelly-sizing-quarter.md` for quarter-Kelly bot defaults. Update both sides when maturity promotes.

## L3 — Phase-0 paid tools before recommending (2026-05-31)

Odds services, copy-trading alerts, and "AI pick" products often market inflated ROI. Entity pages get GO/CONDITIONAL-GO/NO-GO after TOS + sample-track review — same discipline as osint tool evals, different failure mode (account limits, stale lines, -EV churn).

## L4 — dev.fun beta vs official = separate wallets (2026-06-03)

**Lesson:** `b-arena.dev.fun` (beta) and `arena.dev.fun` (official) are **not** the same environment. Registering the same handle twice creates **two agent IDs** and **two custodial Monad wallets**. MON sent to the beta wallet does **not** appear on the official wallet.

| Check | Beta (wrong for Playground S1 leaderboard) | Official (prod) |
|-------|--------------------------------------------|-----------------|
| API base | `https://b-arena.dev.fun/api/arena` | `https://arena.dev.fun/api/arena` |
| Cemini agent ID | `cmpvvczea0iyndve98srkcwwq` (retired) | `cmpy4lcyi001y11vnekn1zlo3` |
| Wallet (Jun 3) | `0x3fB1…c40D` — **~648 MON stranded** | `0x7d2a…0bEF` — **0 MON** |

**Outbound transfers:** `POST /agent/wallet/transfer/native` only accepts **dev.fun protocol addresses** (402 entry-fee `paymentRequirements.to`). Sending to another agent wallet returns **403**. You cannot "move" beta MON to official via the API.

**Fund official:** MoonPay or send MON to the **official** agent wallet address from an external wallet. Script: `agents/devfun-poker-arena/scripts/cemini_wallet_check.sh`.

**Before every deploy:** confirm `ARENA_API_BASE=https://arena.dev.fun/api/arena`, prod `.arena-credentials` matches claimed agent, and **never** `CEMINI_FORCE_CREDS=1` unless intentional. Keep `.arena-credentials.b-beta` only as archive — do not point prod lobby at beta.

**Playground vs MON:** Playground join fails with **409** (chips), not **402** (MON). MON on official is for paid competitions + gas; chip stack is separate arena currency.
