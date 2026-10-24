#!/usr/bin/env bash
# bots-daily.sh — Daily agent-fleet run WITHOUT GitHub Actions
#
# GitHub Actions is blocked while the account has a billing lock. This script
# does what the 'DAO Bots' workflow did, from any machine with this repo:
#   1. Preflight guards:
#      • refuses to run if you have staged changes OUTSIDE the fleet's output
#        paths (never commits your work-in-progress),
#      • refuses to run if the fleet's output paths have UNSTAGED edits
#        (never overwrites your manual report edits).
#   2. Runs the full agent fleet (bots/fleet-runner.js — 7 tools, $0).
#   3. Commits ONLY the fleet's outputs (reports/ + ops/reports/) via explicit
#      pathspec, under your pre-configured identity, then pushes.
#   4. Even when there is nothing new to commit, pushes any locally committed
#      but unpushed reports (a failed push earlier is retried, not stranded).
#
# Schedule it (choose one):
#   Linux/macOS cron:      crontab -e
#     0 6 * * *  cd /path/to/repo && bash scripts/bots-daily.sh >> .bots-daily.log 2>&1
#   Or run manually:       bash scripts/bots-daily.sh
#
# Exit codes: 0 = clean run (nothing to do, or committed+pushed), 1 = failure.

set -euo pipefail
cd "$(dirname "$0")/.."

# Fleet output allowlist — the ONLY paths this script stages/commits/pushes
OUTPUTS=(reports/ ops/reports/)

echo "── $(date -u +%Y-%m-%dT%H:%MZ) DAO agent fleet (Actions-free mode) ──"

# ── Preflight 1: staged work outside the outputs → refuse ────────────────────
STAGED_OUTSIDE=$(git diff --cached --name-only | grep -v -E '^(reports/|ops/reports/)' || true)
if [ -n "$STAGED_OUTSIDE" ]; then
  echo "✗ Refusing to run: staged changes OUTSIDE the fleet outputs:"
  echo "$STAGED_OUTSIDE" | sed 's/^/    /'
  echo "  Commit or stash them first — this guard prevents committing your WIP."
  exit 1
fi

# ── Preflight 2: unstaged edits inside the outputs → refuse (protect them) ──
UNSTAGED_INSIDE=$(git diff --name-only -- "${OUTPUTS[@]}" || true)
if [ -n "$UNSTAGED_INSIDE" ]; then
  echo "✗ Refusing to run: the fleet's output paths have UNSTAGED edits:"
  echo "$UNSTAGED_INSIDE" | sed 's/^/    /'
  echo "  Commit or stash them first — this guard prevents overwriting your edits."
  exit 1
fi

# ── Identity (pre-configured by scripts/setup-identity.sh; idempotent) ────────
git config user.name  "Todd Stephens"
git config user.email "157565446+FuzzysTodd@users.noreply.github.com"

# ── Run the full fleet (7 tools — no Actions charges, no model API calls) ────
node bots/fleet-runner.js

# ── Commit ONLY the fleet outputs, then push ──────────────────────────────────
if git diff --quiet -- "${OUTPUTS[@]}" && git diff --cached --quiet -- "${OUTPUTS[@]}"; then
  echo "✓ No report changes — nothing to commit."
else
  git add "${OUTPUTS[@]}"
  git commit -m 'DAO agent fleet (Actions-free): zero-cost upkeep reports' -- "${OUTPUTS[@]}"
fi

# ── Sync: push anything locally committed but unpushed (retry stranded pushes) ─
UNPUSHED=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo 0)
if [ "$UNPUSHED" -gt 0 ]; then
  echo "▸ Pushing $UNPUSHED locally-committed commit(s)…"
  if git push; then
    echo "✓ Reports committed and pushed."
  else
    echo "✗ Push failed — reports are committed locally; will retry next run."
    exit 1
  fi
else
  echo "✓ Everything is in sync with the remote."
fi
