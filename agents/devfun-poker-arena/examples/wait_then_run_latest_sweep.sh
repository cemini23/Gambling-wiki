#!/usr/bin/env bash
# Wait until no training sweep is running, then start the latest primary pipeline.
# Primary OnSuccess= chains to mixed-size phase automatically.
set -euo pipefail

UNITS=(
  cemini-poker-train.service
  cemini-poker-train-mixed.service
)
POLL="${SWEEP_WAIT_POLL_SEC:-30}"

_sweep_running() {
  for u in "${UNITS[@]}"; do
    state="$(systemctl show "$u" -p ActiveState --value 2>/dev/null || echo inactive)"
    sub="$(systemctl show "$u" -p SubState --value 2>/dev/null || echo dead)"
    if [[ "$state" == "activating" || "$state" == "active" ]]; then
      return 0
    fi
    if [[ "$state" == "activating" && "$sub" == "start" ]]; then
      return 0
    fi
  done
  if pgrep -f 'run_train_sweep' >/dev/null 2>&1; then
    return 0
  fi
  return 1
}

echo "[latest-followup] waiting for training sweeps to finish (poll ${POLL}s)..."

while _sweep_running; do
  sleep "$POLL"
done

echo "[latest-followup] idle — starting cemini-poker-train.service (named+grid+seats → mixed)"
exec systemctl start --no-block cemini-poker-train.service
