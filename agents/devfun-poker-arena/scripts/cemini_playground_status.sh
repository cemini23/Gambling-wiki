#!/usr/bin/env bash
# Playground S1 qualification snapshot — rank vs top-20 cutoff.
#
# Usage:
#   ./scripts/cemini_playground_status.sh
#   ./scripts/cemini_playground_status.sh --competition cmpy2qy65002ud9ej6b7jjq0l
#   CEMINI_AGENT_HANDLE=cemini_wiki_poker ./scripts/cemini_playground_status.sh
set -euo pipefail
cd "$(dirname "$0")/.."

COMP="${1:-${ARENA_LOBBY_COMPETITION_ID:-cmpy2qy65002ud9ej6b7jjq0l}}"
HANDLE="${CEMINI_AGENT_HANDLE:-cemini_wiki_poker}"
CUTOFF_RANK=20

if [[ "${1:-}" == "--competition" ]]; then
  COMP="${2:?competition id required}"
fi

uv run python - <<'PY' "$COMP" "$HANDLE" "$CUTOFF_RANK"
import json, os, sys
from pathlib import Path

comp, handle, cutoff_rank = sys.argv[1:4]
cutoff_rank = int(cutoff_rank)
root = Path.cwd()
examples = root / "examples"
sys.path.insert(0, str(examples))

from dotenv import load_dotenv
load_dotenv(root / ".env")

from arena_client import ArenaClient, ArenaError, CREDS_PATH, DEFAULT_BASE

def load_key() -> str | None:
    if os.environ.get("ARENA_API_KEY"):
        return os.environ["ARENA_API_KEY"]
    if CREDS_PATH.is_file():
        c = json.loads(CREDS_PATH.read_text())
        return c.get("apiKey")
    return None

key = load_key()
base = os.environ.get("ARENA_API_BASE", DEFAULT_BASE)
client = ArenaClient(base, api_key=key)

lb = client.get(f"/competition/leaderboard?competitionId={comp}&limit={cutoff_rank}&offset={cutoff_rank - 1}")
rows = lb.get("data") or []
cutoff = rows[0] if rows else None

me = None
if key:
    try:
        me = client.get("/agent/me")
    except ArenaError:
        me = None

# Find our handle on leaderboard (public — no auth needed)
ours = None
for offset in range(0, 300, 50):
    page = client.get(f"/competition/leaderboard?competitionId={comp}&limit=50&offset={offset}")
    for row in page.get("data") or []:
        ag = row.get("agent") or {}
        if ag.get("handle") == handle:
            ours = row
            break
    if ours:
        break

total = lb.get("total") if isinstance(lb, dict) else None
print("=" * 60)
print(f"  Playground qualification — {comp}")
print(f"  Field size (reported): {total}")
print(f"  Cutoff: top {cutoff_rank} advance to tournament knockout")
print("=" * 60)

if cutoff:
    ag = cutoff.get("agent") or {}
    print(f"  Rank #{cutoff['rank']} floor: {cutoff['totalScore']} chips  "
          f"({cutoff.get('graduateCount', 0)} hands, {cutoff.get('correctCount', 0)} won)  "
          f"— {ag.get('handle')}")
else:
    print("  (could not fetch rank-20 row)")

if ours:
    ag = ours.get("agent") or {}
    gap = (cutoff["totalScore"] - ours["totalScore"]) if cutoff else 0
    print(f"  OUR AGENT ({handle}):")
    print(f"    rank={ours['rank']}  chips={ours['totalScore']}  "
          f"hands={ours.get('graduateCount', 0)}  won={ours.get('correctCount', 0)}")
    if cutoff and ours["rank"] > cutoff_rank:
        print(f"    GAP to top-{cutoff_rank}: +{gap} chips needed")
    elif cutoff:
        print(f"    IN ZONE (top {cutoff_rank}) — keep playing, don't bust")
    if me and ag.get("id") and me.get("id") != ag.get("id"):
        print(f"    WARN: creds agent {me.get('id')} != leaderboard {ag.get('id')}")
else:
    print(f"  OUR AGENT ({handle}): not found on leaderboard (wrong handle or no hands)")

if me:
    for row in me.get("leaderboard") or []:
        if row.get("arenaId") == comp:
            print(f"  AUTH AGENT: {me.get('handle')} id={me.get('id')} "
                  f"rank={row.get('rank')} score={row.get('totalScore')}")
            break

print("=" * 60)
print("  Stages (dev.fun): Jun 3–7 + Jun 7–11 playground → top 20 each")
print("  Knockout tournament → top 25 advance (separate stage)")
print("=" * 60)
client.close()
PY
