# Cemini dev.fun Poker Arena agent

Custom `decide()` for [dev.fun Poker Arena](https://dev.fun/) built on [arena-pokerkit](https://github.com/chenziz/arena-pokerkit).

## Setup

```bash
cd agents/devfun-poker-arena
uv sync
cp .env.example .env
```

## Local smoke test (no network)

```bash
uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 20
```

## Private training (starter kit — recommended before tournament)

Train on the **arena-pokerkit** local loop. Zero network, nothing on the public leaderboard, full HUD exploit path via `private/opponent_hud_exploit.py`.

| Mode | Command | Public? |
|------|---------|---------|
| **Unit scenarios** | `uv run python -m pytest tests/ -q` | No |
| **Self-play vs rock/maniac** | `./examples/run_train_cemini.sh rock 500` | No |
| **Self-play + HUD branch** | same script (`--training-hud` built in) | No |
| **Dry-run mock API** | `uv run examples/run_cemini.py --dry-run --max-hands 20` | No |
| **Poker Eval benchmark** | `uv run examples/run_cemini.py --max-hands 50` | Yes (Eval leaderboard) |
| **Playground lobby** | `run_cemini_lobby.py` + official Playground S1 | Yes (casual) |
| **Tournament S28** | swap `ARENA_LOBBY_COMPETITION_ID` | Yes (competition) |

**Recommended loop:** train locally until self-play bb/100 is stable vs `rock` and `maniac`, then deploy to prod for live Playground / tournament seasons.

```bash
# 6-max (default) — matches S28 full tables
./examples/run_train_cemini.sh rock 500

# maniac (CallMeMummy shape)
./examples/run_train_cemini.sh maniac 500

# HU or mixed sizes
TRAIN_PLAYERS=2 ./examples/run_train_cemini.sh rock 500
uv run examples/selfplay.py --agent examples/cemini_decide.py --players 4 --opponent rock --hands 500 --training-hud
```

**Grid seat layouts** (`uniform`, `one_maniac_mp`, `btn_maniac`): mixed layouts run **once** per profile (per-seat bots + HUD); `uniform` still runs rock + maniac homogeneous tables.

Use `SWEEP_PROFILES=named+grid` for the smaller grid without seat layouts (~48 profiles).

Opponent bots: `rock`, `maniac`, `tight`, `loose`, `random`, `call`, `mixed` via `pokerkit selfplay` / `selfplay.py`.

### Overnight parameter sweep on cemini-egress-fi

Idle egress runs a **two-phase nightly pipeline** at **03:00 UTC**:

1. **Primary** — full profile grid @ **6-max** (`reports/sweep/`)
2. **Mixed** — same grid @ **6/4/2-max**, 1500 hands/combo, tournament-weighted ranking (`reports/sweep-mixed/`)

Phase 2 starts automatically when phase 1 exits successfully (`OnSuccess=` in systemd).

```bash
# Deploy + enable nightly timer (requires private/opponent_hud_exploit.py locally)
./deploy/deploy_train_to_egress.sh

# Leaderboards
ssh cemini-egress-fi cat /opt/devfun-poker-arena-train/reports/sweep/latest/leaderboard.txt
ssh cemini-egress-fi cat /opt/devfun-poker-arena-train/reports/sweep-mixed/latest/leaderboard.txt

# Manual: mixed only (e.g. after primary already finished)
ssh cemini-egress-fi systemctl start --no-block cemini-poker-train-mixed.service

# Manual: wait for in-flight primary then mixed
ssh cemini-egress-fi systemctl start --no-block cemini-poker-train-followup.service
```

| Env (systemd / shell) | Default | Meaning |
|-----------------------|---------|---------|
| `SWEEP_HANDS` | 2500 | Hands per profile per opponent **per table size** |
| `SWEEP_PROFILES` | `named+grid+seats` | ~16 named + 108 grid (params × seat layout) |
| `SWEEP_PLAYER_SIZES` | `6` | Comma list: `6`, or `6,4,2` for mixed-size |
| `SWEEP_PLAYER_WEIGHTS` | (auto) | Ranking weights, e.g. `6:0.55,4:0.25,2:0.20` |
| `SWEEP_SEED` | UTC date | Reproducible base seed |

Local quick sweep:

```bash
SWEEP_PROFILES=named SWEEP_HANDS=1000 ./examples/run_train_sweep.sh
```

Single-profile batch (old behavior): `./examples/run_train_batch.sh` with `TRAIN_HANDS=5000`.

Tunable knobs live in `examples/train_profiles.py` (named presets) and env overrides read by `cemini_decide.py` + `private/opponent_hud_exploit.py`.

### Multi-way opponent targeting (4-max / 6-max)

HUD no longer uses one table-wide villain for every decision:

| Spot | Target | Margins |
|------|--------|---------|
| **Facing bet/raise** | **Last aggressor** on this street (actionHistory → max `currentBetChips`) | That villain's archetype (rock/maniac/…) |
| **Unopened pot** (steal / open) | Softest remaining villain (rock in blinds) | Rock steal exploits |
| **Fallback** | Table aggregate (maniac > rock > first) | Same as before |

**Multi-way adjustment:** with 2+ active villains, call/fold margins tighten and bluff bars drop; unopened steals need slightly stronger equity.

Training tags each bot seat via `TRAINING_SEAT_ARCHETYPES` (comma list, 6 seats):

```bash
# 6-max: 4 rocks + 1 maniac + 1 tight — tests aggressor-specific exploits
TRAIN_PLAYERS=6 TRAINING_SEAT_ARCHETYPES=rock,rock,maniac,tight,rock,rock \
  ./examples/run_train_cemini.sh rock 300
```

Live Arena: all seated `agentId`s are fetched; targeting uses the bettor's stats when you're facing action.

## Live play

**Registered:** handle `cemini_wiki_poker`, agent ID on wiki bot page. Credentials in `.arena-credentials` (gitignored).

```bash
# Official Playground S1 (prod lobby)
uv run examples/run_cemini_lobby.py --competition-id cmpy2qy65002ud9ej6b7jjq0l

# Poker Eval benchmark (when cmpdk… competition is active)
uv run examples/run_cemini.py --max-hands 50
```

**Prize eligibility:** claim X at URL from `GET /auth/claim/status` (see wiki bot page).

## Architecture

| Layer | File |
|-------|------|
| Lobby loop | `examples/run_cemini_lobby.py` |
| Eval benchmark | `examples/run_cemini.py` |
| Custom logic | `examples/cemini_decide.py` |
| Preflop research | `examples/research_static_chart.py` |
| PokerSkill stub | `examples/pokerskill_adapter.py` + `deploy/install_pokerskill_prod.sh` |
| Wiki Phase-0 | `@wiki/entities/bots/cemini-devfun-poker-agent.md` |

## Production (cemini-prod)

Always-on lobby loop via systemd — laptop can stay off.

```bash
./agents/devfun-poker-arena/deploy/deploy_to_cemini_prod.sh
```

Remote path: `/opt/devfun-poker-arena` · unit: `cemini-devfun-poker-lobby.service`

**Prod-only HUD exploits** live in `private/opponent_hud_exploit.py` (gitignored). Public `examples/opponent_hud.py` is a neutral facade. Deploy rsyncs `private/` when present locally.

```bash
ssh cemini-prod journalctl -u cemini-devfun-poker-lobby -f
ssh cemini-prod systemctl restart cemini-devfun-poker-lobby
```

### Monitor (analyze + Eval poll)

Systemd timer on prod runs every **30 min**:
- Playground failure analyze → `/opt/devfun-poker-arena/reports/analyze/`
- Position metrics history → `reports/analyze/history.jsonl`
- Poker Eval / Tournament availability → `reports/eval_poll.jsonl`, `reports/alerts.txt`

```bash
# Local one-shot (same as prod timer)
uv run examples/arena_monitor.py once

# Analyze only / poll only / loop
uv run examples/arena_monitor.py analyze --match cmpy2qy65002ud9ej6b7jjq0l
uv run examples/arena_monitor.py poll-eval
uv run examples/arena_monitor.py watch --interval 1800

# Prod
ssh cemini-prod systemctl start cemini-devfun-poker-monitor.service
ssh cemini-prod tail -3 /opt/devfun-poker-arena/reports/analyze/history.jsonl
ssh cemini-prod cat /opt/devfun-poker-arena/reports/alerts.txt
```

When Poker Eval goes live, monitor logs `POKER EVAL LIVE` with the `run_cemini.py` command. Optional auto-start: `--auto-benchmark` (off by default).

Swap `ARENA_LOBBY_COMPETITION_ID` in remote `.env` when a new Playground or tournament season opens, then `systemctl restart cemini-devfun-poker-lobby`.

## Active seasons

**Use official arena only:** `https://arena.dev.fun/api/arena` — **not** `b-arena.dev.fun` (beta; separate agents/leaderboards).

| Competition | ID | Environment | Notes |
|-------------|-----|-------------|-------|
| **Playground S1** | `cmpy2qy65002ud9ej6b7jjq0l` | **Official** (prod) | Featured on [arena.dev.fun](https://arena.dev.fun/) |
| Playground S2 | `cmpy1onq3088b8beendm27r1h` | Beta only | Old prod target — do not use for public leaderboard |
| Playground S1 (legacy) | `cmpr1uomm2is6x69xx4nyqz9r` | Beta only | |
| Tournament S28 | `cmpr1vesh2it1x69xmtpiaecp` | Beta only | 0.01 MON entry on beta |

After switching to official, re-claim X at `/auth/claim/status` → `claimUrl` (new token per environment).

Watch [arena.dev.fun](https://arena.dev.fun/) + Discord for new season IDs.
