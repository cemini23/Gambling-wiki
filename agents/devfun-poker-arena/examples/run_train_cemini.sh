#!/usr/bin/env bash
# Private local training — no Arena API, no public leaderboard.
#
# Usage:
#   ./examples/run_train_cemini.sh              # 500 HU hands vs rock + HUD
#   ./examples/run_train_cemini.sh maniac 1000  # vs maniac, 1000 hands
#   ./examples/run_train_cemini.sh rock 200 --seed 7
set -euo pipefail
cd "$(dirname "$0")/.."

OPP="${1:-rock}"
HANDS="${2:-500}"
shift 2 2>/dev/null || shift 1 2>/dev/null || true

export TRAINING_OPPONENT_MODE="$OPP"

echo "==> cemini private train: opponent=$OPP hands=$HANDS (offline, no network)"

exec uv run examples/selfplay.py \
  --agent examples/cemini_decide.py \
  --opponent "$OPP" \
  --hands "$HANDS" \
  --training-hud \
  "$@"
