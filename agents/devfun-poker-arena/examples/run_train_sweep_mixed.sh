#!/usr/bin/env bash
# Phase 2: mixed table sizes (6/4/2-max) after primary 6-max sweep.
#
# Defaults tuned for ~2–3h on egress after the full 6-max grid.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export SWEEP_PLAYER_SIZES="${SWEEP_PLAYER_SIZES:-6,4,2}"
export SWEEP_HANDS="${SWEEP_HANDS:-1500}"
export SWEEP_PROFILES="${SWEEP_PROFILES:-named+grid}"
export SWEEP_PLAYER_WEIGHTS="${SWEEP_PLAYER_WEIGHTS:-6:0.55,4:0.25,2:0.20}"
export REPORT_DIR="${REPORT_DIR:-reports/sweep-mixed}"
export SWEEP_SEED="${SWEEP_SEED:-$(date -u +%Y%m%d)}"

mkdir -p "$REPORT_DIR"
LOCK="${REPORT_DIR}/.sweep.lock"
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "[mixed-sweep] already running (lock ${LOCK}) — skip duplicate start"
  exit 0
fi

exec "$ROOT/examples/run_train_sweep.sh"
