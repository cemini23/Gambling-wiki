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

| Check | Beta | Official (prod) |
|-------|------|-----------------|
| API base | `https://b-arena.dev.fun/api/arena` | `https://arena.dev.fun/api/arena` |

**Outbound transfers:** `POST /agent/wallet/transfer/native` only accepts **dev.fun protocol addresses** (402 entry-fee `paymentRequirements.to`). Sending to another agent wallet returns **403**. You cannot "move" beta MON to official via the API.

**Fund official:** MoonPay or send MON to the **official** agent wallet address from an external wallet. Wallet/agent IDs live in **private** creds only — not in this repo.

**Before every deploy:** confirm `ARENA_API_BASE=https://arena.dev.fun/api/arena` and prod `.arena-credentials` matches the intended claimed agent. Deploy copies local creds to prod when agentIds match; skips on mismatch.

**Playground vs MON:** Playground join fails with **409** (chips), not **402** (MON). MON on official is for paid competitions + gas; chip stack is separate arena currency.

## L5 — Playground: credential coupling + claim timing (2026-06-03)

**Lesson (ops only — no strategy detail in public docs):** Arena competitors often run **multiple agents** before claiming. Coupling **one** public handle to **one** prod deploy path early makes iteration expensive — rank visibility ≠ strategy lock-in, but ops friction is real.

**Operator checklist (private runbooks hold specifics):**

1. Separate beta vs official creds; never fund the wrong wallet.
2. Defer X claim until you are ready to commit to a public leaderboard identity.
3. Keep strategy patches, analyze output, and regression spots **out of git** during active competition windows.

**Do not publish:** multi-agent probe playbooks, rank/chip targets, or opponent-specific tuning — see competitive-secrecy note in `ROADMAP.md` W6.

## L6 — Playground analyze cadence (2026-06-03)

**Lesson:** After each deploy, pull a fresh Arena analyze sample and patch **one** leak at a time. Wait for ~50 post-patch hands before the next code change. Full bust patterns (−100 lines) usually mean preflop/OOP discipline, not small postflop leaks — but **specific hand classes, seats, and regression spots stay in private briefs**, not here.
