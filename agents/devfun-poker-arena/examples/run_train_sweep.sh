#!/usr/bin/env bash
# Overnight parameter sweep (many profiles × rock + maniac).
#
# Env:
#   SWEEP_HANDS      — per profile per opponent (default 2500)
#   SWEEP_PROFILES   — named+grid | named | grid | default | p1,p2,...
#   SWEEP_SEED           — base seed (default YYYYMMDD UTC)
#   SWEEP_PLAYER_SIZES   — seat counts 2–6 (default 6 for S28 full tables)
#   SWEEP_PLAYER_WEIGHTS — optional 6:0.55,4:0.25,2:0.20 for mixed-size ranking
#   REPORT_DIR           — default reports/sweep
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PYTHON="${PYTHON:-./venv/bin/python}"
if [[ ! -x "$PYTHON" ]]; then
  PYTHON="uv run python"
fi

export SWEEP_HANDS="${SWEEP_HANDS:-2500}"
export SWEEP_PROFILES="${SWEEP_PROFILES:-named+grid}"
export SWEEP_SEED="${SWEEP_SEED:-$(date -u +%Y%m%d)}"
export SWEEP_PLAYER_SIZES="${SWEEP_PLAYER_SIZES:-6}"
export REPORT_DIR="${REPORT_DIR:-reports/sweep}"

mkdir -p "$REPORT_DIR"
exec "$PYTHON" examples/run_train_sweep.py 2>&1 | tee -a "${REPORT_DIR}/run.log"
