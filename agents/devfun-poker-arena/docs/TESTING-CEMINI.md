# Cemini test strategy — why Playground bled chips & how to prevent it

## What went wrong (honest postmortem)

| Gap | What happened | Why tests didn't catch it |
|-----|---------------|---------------------------|
| **Wrong agent under test** | `tests/test_user_decide_example.py` exercises **`examples/agent.py`** (starter skeleton), not `cemini_decide.py` | Copy-paste template never swapped to our bot |
| **HU-only scenarios** | 20 fixtures in `examples/testing.py` are mostly **heads-up**, seat 1 = hero, no button rotation | 74o **MP** and UTG chart paths never executed |
| **No HUD / cold-start path** | Private `opponent_hud_exploit.py` only loads on prod rsync | Local pytest used neutral HUD (`open_steal_equity=0.99`) — steals always blocked locally, wide in prod |
| **No regression corpus** | Worst hands from `arena_monitor.py analyze` weren't frozen as tests | Each fix was reactive after chip loss |
| **Self-play not gated** | Egress sweeps rank **parameters**, not Playground opponent mix; no VPIP ceiling | Passing pytest ≠ passing vs Arena fish/maniac table |
| **Env mismatch** | Beta vs official arena split leaderboards | Operational, not unit-testable |

**Bottom line:** we had *API smoke tests* and *skeleton scenario tests*, not a *cemini Playground simulation harness*.

## Test layers (use all before deploy)

```
┌─────────────────────────────────────────────────────────────┐
│ 4. Live smoke (optional) — pokerkit run --max-hands 20      │
├─────────────────────────────────────────────────────────────┤
│ 3. Preflight gate — ./scripts/cemini_preflight.sh           │
│    pytest + self-play KPI audit (--gate) + dry-run          │
├─────────────────────────────────────────────────────────────┤
│ 2. Regression spots — tests/test_cemini_regression.py       │
│    6-max, prod leak hands (74o MP, J2o CO, overcommit…)     │
├─────────────────────────────────────────────────────────────┤
│ 1. Unit guards — preflop guards, cold-start HUD, helpers    │
└─────────────────────────────────────────────────────────────┘
```

### Layer 1 — Unit guards (fast, ~1s)

```bash
uv run python -m pytest tests/test_cemini_preflop_guards.py tests/test_cold_start_hud.py tests/test_session_memory.py tests/test_devfun_scan_behaviors.py -q
```

**dev.fun scan behaviors** (`tests/test_devfun_scan_behaviors.py`) — offline locks for personality/memory-inspired patches: candor fold chat, survival stack, composure deadline, session memory abstention. Baseline fixture: `tests/fixtures/devfun_scan_baselines.json`.

### Layer 2 — Regression spots (~1s)

Prod-shaped **6-max** tables via `tests/helpers/cemini_tables.py`.

```bash
uv run python -m pytest tests/test_cemini_regression.py tests/test_cemini_scenarios.py -q
```

**After each analyze cycle:** add a spot to `tests/fixtures/regression_spots.py` (or run `examples/export_regression_spots.py` for stubs).

### Layer 3 — Self-play KPI audit (~30–90s)

Tracks **VPIP, PFR, EP trash opens, bb/100** vs rock + maniac with `--training-hud`:

```bash
uv run python examples/cemini_selfplay_audit.py --hands 400 --seed 42 --gate
```

Default gates (tune in script):

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| **EP VPIP** (UTG+MP) | ≤ 22% | Playground leak was 74o MP, KTs UTG — not global VPIP |
| EP trash opens | 0 | 74o MP type leaks |
| bb/100 vs rock | ≥ −25 | Loose but not catastrophic offline |
| bb/100 vs maniac | ≥ −40 | Maniac tables are volatile |

Global VPIP is printed for info but **not gated** — SB completes and self-play position labels inflate it vs Arena HUD stats.

### Layer 4 — Pre-deploy (one command)

```bash
chmod +x scripts/cemini_preflight.sh   # once
./scripts/cemini_preflight.sh          # quick (~45s)
./scripts/cemini_preflight.sh --full   # 600 hands/ profile (~2 min)
```

## End-of-session workflow (next Playground round)

**Preferred:** HL analyst loop (one command to start):

```bash
./examples/cemini_hl_loop.sh --from-prod
# → patch cemini_decide.py from reports/hl-loop/latest_brief.md
./examples/cemini_hl_loop.sh --preflight-only
./examples/cemini_hl_loop.sh --deploy
```

Manual steps (same pipeline):

1. **Analyze** — `arena_monitor.py analyze --match <new-id> --top 15`
2. **Freeze leaks** — add regression spots for top 3–5 worst hands
3. **Fix decide / chart / HUD**
4. **Preflight** — `./scripts/cemini_preflight.sh --full`
5. **Deploy** — rsync + `systemctl restart`
6. **Monitor** — 30 min timer; re-analyze after ~50 hands

## What still won't be caught locally

- **DeepCFR** reference panel (use `pokerkit run --max-hands 50` on Eval when live)
- **Exact Playground opponent mix** (fish + maniac + lag unknowns)
- **Cloudflare 502** — covered by `test_smoke.py` lobby mocks, not decide logic
- **Chip bankroll / rebuy** — monitor `409 not enough chips` in journal

Treat local tests as **necessary, not sufficient**. Eval benchmark is the confirmation layer.

## Files added for this harness

| File | Role |
|------|------|
| `tests/helpers/cemini_tables.py` | 6-max Arena table builders |
| `tests/fixtures/regression_spots.py` | Named leak spots |
| `tests/test_cemini_regression.py` | Assert forbidden actions |
| `tests/test_cemini_scenarios.py` | cemini × 20 starter scenarios |
| `examples/cemini_selfplay_audit.py` | VPIP / bb100 gate |
| `scripts/cemini_preflight.sh` | One-shot pre-deploy |
| `scripts/cemini_wallet_check.sh` | Beta vs official MON balances (ops) |
| `tests/test_devfun_scan_behaviors.py` | Scan-inspired decide() behavior locks |
| `tests/fixtures/devfun_scan_baselines.json` | Frozen scan baseline metadata |
| `examples/cemini_hl_loop.sh` | HL analyst loop (analyze → brief → preflight → deploy) |
| `examples/cemini_hl_brief.py` | Build OSINT-shaped brief from analyze report |
| `prompts/cemini_hl_analyst_prompt.md` | Cursor patch prompt (cemini_decide only) |
| `examples/export_regression_spots.py` | Analyze → spot stubs |
