#!/usr/bin/env bash
# One-shot: wait for primary sweep, then start mixed-size sweep.
# Used when primary was started before OnSuccess chaining was installed.
set -euo pipefail

PRIMARY="${PRIMARY_SWEEP_UNIT:-cemini-poker-train.service}"
MIXED="${MIXED_SWEEP_UNIT:-cemini-poker-train-mixed.service}"
POLL="${SWEEP_WAIT_POLL_SEC:-30}"

echo "[followup] waiting for ${PRIMARY} to finish (poll ${POLL}s)..."

while true; do
  state="$(systemctl show "$PRIMARY" -p ActiveState --value 2>/dev/null || echo inactive)"
  sub="$(systemctl show "$PRIMARY" -p SubState --value 2>/dev/null || echo dead)"
  if [[ "$state" != "activating" && "$state" != "active" ]]; then
    break
  fi
  if [[ "$state" == "activating" && "$sub" == "dead" ]]; then
    break
  fi
  sleep "$POLL"
done

if systemctl is-active --quiet "$MIXED" 2>/dev/null; then
  echo "[followup] ${MIXED} already running — skip"
  exit 0
fi

echo "[followup] primary done (${state}/${sub}); starting ${MIXED}"
exec systemctl start --no-block "$MIXED"
