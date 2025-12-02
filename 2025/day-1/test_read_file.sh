#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SCRIPT="$ROOT_DIR/2025/day-1/secret-entrance.py"
EXAMPLE="$ROOT_DIR/2025/day-1/example.txt"

if [[ ! -x "$SCRIPT" ]]; then
  echo "Note: $SCRIPT is not executable; trying with python3..."
  CMD=(python3 "$SCRIPT")
else
  CMD=("$SCRIPT")
fi

expected="3"
output="$(${CMD[@]} "$EXAMPLE")"

if [[ "$output" == "$expected" ]]; then
  echo "TEST OK"
  exit 0
else
  echo "TEST FAILED"
  echo "--- expected ---"
  printf '%s
' "$expected"
  echo "--- got ---"
  printf '%s
' "$output"
  exit 1
fi
