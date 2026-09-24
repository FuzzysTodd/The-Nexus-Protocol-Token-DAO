#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# Nexus Protocol — Local Stack Launcher
#
# Starts all three Node.js services on localhost at zero external cost.
# All services read nexus-config.js with NEXUS_ENV=local.
#
# Services started:
#   PID file   Port   Service
#   .pid/8787  8787   Approval Service   (approval-service-server.js)
#   .pid/8788  8788   Financial Ops REST (financial-ops-rest-server.js)
#   .pid/8790  8790   Nexus Signal Bus   (nexus-signal-bus.js)
#
# Usage:
#   bash scripts/start-local.sh          # start all
#   bash scripts/start-local.sh stop     # stop all
#   bash scripts/start-local.sh status   # show running PIDs
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_DIR="$ROOT/.pids"
LOG_DIR="$ROOT/.logs"
NEXUS_ENV=local

mkdir -p "$PID_DIR" "$LOG_DIR"

# ── Load .env if present ──────────────────────────────────────────────────────
if [ -f "$ROOT/.env" ]; then
  set -a
  # shellcheck disable=SC1090
  source "$ROOT/.env"
  set +a
fi

export NEXUS_ENV=local
export APPROVAL_SERVICE_PORT="${APPROVAL_SERVICE_PORT:-8787}"
export FINANCIAL_OPS_REST_PORT="${FINANCIAL_OPS_REST_PORT:-8788}"
export NEXUS_SIGNAL_BUS_PORT="${NEXUS_SIGNAL_BUS_PORT:-8790}"

# ── Helper: start one background process ─────────────────────────────────────
start_service () {
  local name="$1"
  local script="$2"
  local logfile="$LOG_DIR/${name}.log"
  local pidfile="$PID_DIR/${name}.pid"

  if [ -f "$pidfile" ] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
    echo "  ▸ $name already running (PID $(cat "$pidfile"))"
    return
  fi

  node "$ROOT/$script" >> "$logfile" 2>&1 &
  echo $! > "$pidfile"
  echo "  ✓ $name started  (PID $!)  → $logfile"
}

stop_service () {
  local name="$1"
  local pidfile="$PID_DIR/${name}.pid"
  if [ -f "$pidfile" ]; then
    local pid
    pid=$(cat "$pidfile")
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid" && echo "  ✓ $name stopped (PID $pid)"
    else
      echo "  ▸ $name not running"
    fi
    rm -f "$pidfile"
  else
    echo "  ▸ $name not running (no PID file)"
  fi
}

status_service () {
  local name="$1"
  local pidfile="$PID_DIR/${name}.pid"
  if [ -f "$pidfile" ] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
    echo "  ✓ $name  running  (PID $(cat "$pidfile"))"
  else
    echo "  ✗ $name  stopped"
  fi
}

CMD="${1:-start}"

case "$CMD" in
  start)
    echo "🚀 Starting Nexus Protocol local stack (NEXUS_ENV=local)…"
    start_service "approval-service"   "approval-service-server.js"
    start_service "financial-ops"      "financial-ops-rest-server.js"
    start_service "signal-bus"         "nexus-signal-bus.js"
    echo ""
    echo "Local endpoints:"
    echo "  Approval Service  → http://localhost:${APPROVAL_SERVICE_PORT}"
    echo "  Financial Ops     → http://localhost:${FINANCIAL_OPS_REST_PORT}"
    echo "  Signal Bus (WS)   → ws://localhost:${NEXUS_SIGNAL_BUS_PORT}"
    echo ""
    echo "Logs: $LOG_DIR/"
    echo "Stop: bash scripts/start-local.sh stop"
    ;;
  stop)
    echo "🛑 Stopping Nexus Protocol local stack…"
    stop_service "approval-service"
    stop_service "financial-ops"
    stop_service "signal-bus"
    ;;
  status)
    echo "📋 Nexus Protocol local stack status:"
    status_service "approval-service"
    status_service "financial-ops"
    status_service "signal-bus"
    ;;
  *)
    echo "Usage: $0 [start|stop|status]"
    exit 1
    ;;
esac
