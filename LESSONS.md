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

**Before every deploy:** confirm `ARENA_API_BASE=https://arena.dev.fun/api/arena`, prod `.arena-credentials` matches claimed agent (`cmpy4lcyi001y11vnekn1zlo3`). Deploy **copies** local `.arena-credentials` to prod when agentIds match; skips only on mismatch (use `CEMINI_FORCE_CREDS=1` to override). Keep `.arena-credentials.b-beta` as archive only.

**Playground vs MON:** Playground join fails with **409** (chips), not **402** (MON). MON on official is for paid competitions + gas; chip stack is separate arena currency.

## L5 — Playground: multi-agent probe, late claim (2026-06-03)

**Lesson:** Competitors register **5–10 agents**, run them **unclaimed** while tuning strategy, then **claim X only on the best chip performer(s)** before prizes matter. We claimed **`cemini_wiki_poker` early** and locked one `decide()` line onto the public leaderboard — hard to pivot after bleed (#4 → ~#215).

**Next playground window (S1b Jun 7–11 or next season):**

1. **Register 5–10 handles** on **official** `arena.dev.fun` (unique names; save each `.arena-credentials.N` locally).
2. **Run in parallel** — local lobby loops or lightweight prod VMs; same HL loop, different strategy branches / param profiles.
3. **Do not claim** until ~50–100 hands per agent or clear rank separation (`cemini_playground_status.sh` per agent).
4. **Claim 1–2 winners** via `GET /auth/claim/status` → X verify; retire or ignore the rest.
5. **Prod deploy** only the claimed winner's creds; keep `ARENA_NO_AUTO_REGISTER=1` on prod to avoid accidental duplicates.

**Why it works:** Unclaimed agents still play and accumulate chips; claim is reversible visibility/prize gate, not strategy lock-in. Our mistake was one agent + early claim + prod credential coupling, not lack of bot quality alone.

## L6 — Playground hand-history scan (2026-06-03 evening)

**Source:** prod `arena_monitor.py analyze` — 100 recent hands, Playground S1 (`cmpy2qy65002ud9ej6b7jjq0l`). Rank **#230 @ 782 chips**; top-20 floor **~1975** (+1193 gap).

| Metric | Value |
|--------|-------|
| Win / loss / push | 10 / 66 / 24 (~10% win rate) |
| Net (sample) | **−3961 chips** |
| Worst seat | **SB −69/hand** (18 hands); then BTN −49, BB −35 |
| Worst-hand pattern | **15/15 at −100** — full buy-in bust lines, not small leaks |

**Leak clusters (priority order):**

1. **SB discipline** — 8 of 15 worst hands SB: `22`, `79`, `96`, `88`, `JJ` paired, `A8` on `J86`, `K6` TPTK. Still #1 seat leak after pre-patch deploy; need tighter SB complete/fold and small-pair OOP give-ups.
2. **Weak ace offsuit** — `A6` BB (999 board), `A7` CO (paired), `A8` SB, `A9` BTN preflop −100: calling/stealing too wide with dominated aces.
3. **Marginal pairs OOP** — `96` BB/ SB, `88` SB river: middle/bottom pair stacking off.
4. **BTN show-downs** — `QAh` on `55776`, `AT` on monotone flush board: overcalling IP vs aggression on paired/scary runouts.
5. **What works** — `TT` CO +396, `77` MP +284, `AK` BB +122: value with real pairs/premium; strategy isn't uniformly bad.

**Ops:** Stack **782 < 1000 buy-in** → intermittent `409 not enough chips`; one more −100 SB line may bench the agent until Jun 7–11. Re-analyze after **50 post-patch hands** before next code change.

**Next regression spots to add:** `A8o` SB TPTK weak kicker; `22`/`88` SB OOP; `A6o`–`A9o` postflop on paired boards.
