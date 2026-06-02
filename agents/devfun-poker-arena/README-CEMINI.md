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

## Live play

**Registered:** handle `cemini_wiki_poker`, agent ID on wiki bot page. Credentials in `.arena-credentials` (gitignored).

```bash
# Playground / Tournament lobby (active on b-arena now)
uv run examples/run_cemini_lobby.py --skip-join

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
uv run examples/arena_monitor.py analyze --match cmpr1uomm2is6x69xx4nyqz9r
uv run examples/arena_monitor.py poll-eval
uv run examples/arena_monitor.py watch --interval 1800

# Prod
ssh cemini-prod systemctl start cemini-devfun-poker-monitor.service
ssh cemini-prod tail -3 /opt/devfun-poker-arena/reports/analyze/history.jsonl
ssh cemini-prod cat /opt/devfun-poker-arena/reports/alerts.txt
```

When Poker Eval goes live, monitor logs `POKER EVAL LIVE` with the `run_cemini.py` command. Optional auto-start: `--auto-benchmark` (off by default).

Swap `ARENA_LOBBY_COMPETITION_ID` in remote `.env` when June 3 main season ID drops, then redeploy.

## June 3 main event

Watch [dev.fun](https://dev.fun/) + Discord for the Monad-sponsored competition ID. Swap `ARENA_LOBBY_COMPETITION_ID` / `ARENA_COMPETITION_ID` when live.
