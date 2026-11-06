@echo off
REM bots-daily.cmd — Daily agent-fleet run WITHOUT GitHub Actions (Windows)
REM
REM GitHub Actions is blocked while the account has a billing lock. This does
REM what the 'DAO Bots' workflow did, from your PC — and pushes, because git
REM push is NOT affected by the billing lock.
REM
REM Fleet outputs (the ONLY paths this script commits): reports\ and ops\reports
REM
REM Schedule it ONCE (daily 6:00 AM) — from an ELEVATED command prompt inside
REM the repo folder (the path is picked up from the current directory):
REM
REM   schtasks /Create /TN "Nexus DAO Agents" /TR "%CD%\scripts\bots-daily.cmd" /SC DAILY /ST 06:00
REM
REM Or run manually:  scripts\bots-daily.cmd
REM
REM Guards: refuses to run when you have staged changes OUTSIDE the fleet
REM outputs (protects your WIP) or UNSTAGED edits INSIDE them (protects your
REM report edits). Retries any locally-committed-but-unpushed reports.
REM Exit codes: 0 = clean run, 1 = failure.

setlocal
cd /d "%~dp0.."

echo --- %DATE% %TIME% DAO agent fleet (Actions-free mode) ---

REM Preflight 1: staged changes outside the outputs → refuse
git diff --cached --name-only | findstr /V /B "reports/ ops/reports/" > "%TEMP%\staged-outside.txt"
for %%A in ("%TEMP%\staged-outside.txt") do if %%~zA GTR 0 (
  echo REFUSING TO RUN: staged changes OUTSIDE the fleet outputs:
  type "%TEMP%\staged-outside.txt"
  echo Commit or stash them first - this guard prevents committing your WIP.
  exit /b 1
)

REM Preflight 2: unstaged edits inside the outputs → refuse (protect them)
git diff --name-only -- reports/ ops/reports/ > "%TEMP%\unstaged-inside.txt"
for %%A in ("%TEMP%\unstaged-inside.txt") do if %%~zA GTR 0 (
  echo REFUSING TO RUN: fleet output paths have UNSTAGED edits:
  type "%TEMP%\unstaged-inside.txt"
  echo Commit or stash them first - this guard prevents overwriting your edits.
  exit /b 1
)

git config user.name  "Todd Stephens"
git config user.email "157565446+FuzzysTodd@users.noreply.github.com"

REM Run the full fleet (7 tools — no Actions charges, no model API calls)
node bots\fleet-runner.js
if errorlevel 1 goto :fail

REM Commit ONLY the fleet outputs, then push
git add reports ops\reports
git diff --cached --quiet -- reports/ "ops/reports/"
if not errorlevel 1 goto :sync
git commit -m "DAO agent fleet (Actions-free): zero-cost upkeep reports" -- reports/ "ops/reports/"
if errorlevel 1 goto :fail

:sync
REM Push anything locally-committed-but-unpushed (retries stranded pushes)
git rev-list --count origin/MASTER..HEAD > "%TEMP%\unpushed.txt" 2>nul
set /p UNPUSHED=<"%TEMP%\unpushed.txt"
if "%UNPUSHED%"=="" set UNPUSHED=0
if %UNPUSHED% GTR 0 (
  echo Pushing %UNPUSHED% locally-committed commit^(s^)...
  git push
  if errorlevel 1 (
    echo PUSH FAILED - reports stay committed locally; will retry next run.
    exit /b 1
  )
  echo Reports committed and pushed.
  exit /b 0
)
echo Everything is in sync with the remote.
exit /b 0

:fail
echo DAO agent fleet found problems - see output above.
exit /b 1
