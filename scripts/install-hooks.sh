#!/usr/bin/env bash
# install-hooks.sh — Wire the DAO bots into git hooks (no GitHub Actions needed)
#
# While the GitHub account has a billing lock, Actions can't run. This points
# the repo's git hooks at the tracked githooks/ directory, so the bots run
# automatically on YOUR machine:
#   • pre-commit  → health + accounting bots
#   • pre-push    → all three bots, reports refreshed before they hit the remote
#
# Bots are deterministic and quiet on success — zero friction, zero credits.
# In a hurry, bypass once with --no-verify.
#
# Usage:  bash scripts/install-hooks.sh     (or:  npm run hooks:install)
# Safe to re-run — idempotent.

set -euo pipefail

cd "$(dirname "$0")/.."

echo "▸ Pointing git hooks at the tracked githooks/ directory"
git config core.hooksPath githooks

# Ensure hook scripts are executable (repo-local chmod)
chmod +x githooks/pre-commit githooks/pre-push 2>/dev/null || true

echo ""
echo "✅ DAO bot hooks installed:"
echo "    pre-commit  → health + file-accounting bots"
echo "    pre-push    → all three bots (health, accounting, registry-sync)"
echo ""
echo "Bots run automatically from now on. Bypass once with --no-verify."
echo "Remove anytime with:  git config --unset core.hooksPath"
