#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip

if [ -f requirements-dev.txt ]; then
  pip install -r requirements-dev.txt
fi

if [ -f playwright-tool/package.json ]; then
  (
    cd playwright-tool
    npm install
  )
fi
