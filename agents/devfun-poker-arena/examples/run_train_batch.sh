#!/usr/bin/env bash
# Overnight batch: rock + maniac self-play with HUD (offline, no Arena API).
#
# Env:
#   TRAIN_HANDS   — hands per archetype (default 5000)
#   TRAIN_SEED     — RNG seed (default YYYYMMDD UTC)
#   REPORT_DIR     — output directory (default reports/train)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

HANDS="${TRAIN_HANDS:-5000}"
SEED="${TRAIN_SEED:-$(date -u +%Y%m%d)}"
REPORT_DIR="${REPORT_DIR:-reports/train}"
PYTHON="${PYTHON:-./venv/bin/python}"
if [[ ! -x "$PYTHON" ]]; then
  PYTHON="uv run python"
fi

mkdir -p "$REPORT_DIR"
STAMP="$(date -u +%Y-%m-%dT%H%M%SZ)"
LOG="$REPORT_DIR/${STAMP}.txt"
LATEST="$REPORT_DIR/latest.txt"

run_one() {
  local opp="$1"
  export TRAINING_OPPONENT_MODE="$opp"
  echo ""
  echo "========== $opp × $HANDS hands (seed=$SEED) =========="
  $PYTHON examples/selfplay.py \
    --agent examples/cemini_decide.py \
    --opponent "$opp" \
    --hands "$HANDS" \
    --training-hud \
    --seed "$SEED"
}

{
  echo "cemini train batch — $STAMP"
  echo "host: $(hostname)"
  echo "hands_per_archetype: $HANDS"
  echo "seed: $SEED"
  echo ""
  run_one rock
  run_one maniac
  echo ""
  echo "done $STAMP"
} 2>&1 | tee "$LOG"

cp -f "$LOG" "$LATEST"
echo "[train-batch] wrote $LOG"
