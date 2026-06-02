#!/usr/bin/env bash
# Overnight parameter sweep (many profiles × rock + maniac).
#
# Env:
#   SWEEP_HANDS      — per profile per opponent (default 2500)
#   SWEEP_PROFILES   — named+grid | named | grid | default | p1,p2,...
#   SWEEP_SEED       — base seed (default YYYYMMDD UTC)
#   REPORT_DIR       — default reports/sweep
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
export REPORT_DIR="${REPORT_DIR:-reports/sweep}"

mkdir -p "$REPORT_DIR"
exec "$PYTHON" examples/run_train_sweep.py 2>&1 | tee -a "${REPORT_DIR}/run.log"
