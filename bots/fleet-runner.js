#!/usr/bin/env node
/**
 * fleet-runner.js — Nexus DAO Agent Fleet Runner ($0 local runtime)
 * -------------------------------------------------------------------
 * Todd's personal fleet of bots/agents, operating WITHOUT cloud cost:
 *   • No GitHub Actions (account billing lock) — runs locally instead
 *   • No AI credits — every tool below is deterministic code, no model calls
 *
 * Fleet executed by this runner (all verified runnable, all $0):
 *   1. dao-health-bot            (Node)   repo health checks
 *   2. dao-accounting-bot         (Node)   full-tree file accounting
 *   3. dao-registry-sync-bot      (Node)   dashboard agent data
 *   4. finance-ops-reporter      (Python) financial ops report → ops/reports/
 *   5. repo-assessor             (Python) read-only repo assessment → reports/
 *   6. asset-finder              (Python) token/contract inventory → reports/
 *   7. telemetry-monitor         (Python) read-only telemetry snapshot → reports/
 *
 * Fleet defined but NOT run here (needs wiring or human gating — see
 * reports/fleet-manifest.json for the full classification):
 *   • 11 MCP registry agents     — definitions; execute only when wired to an engine
 *   • 3 financial-ops bots        — human-gated by design; reporting side runs above
 *   • 87 skills                  — reference library for agents; no runtime cost
 *
 * Usage:  node bots/fleet-runner.js           (or:  npm run agents:run)
 * Output: reports/fleet-report.json + the tools' own reports
 */

"use strict";

const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const REPORTS_DIR = path.join(ROOT, "reports");

// ── Fleet definition ──────────────────────────────────────────────────────────
const FLEET = [
  {
    id: "dao-health-bot",
    kind: "node",
    label: "Health Bot",
    cmd: ["node", "bots/health-bot.js"],
  },
  {
    id: "dao-accounting-bot",
    kind: "node",
    label: "File-Accounting Bot",
    cmd: ["node", "bots/dao-accounting-bot.js"],
  },
  {
    id: "dao-registry-sync-bot",
    kind: "node",
    label: "Registry Sync Bot",
    cmd: ["node", "bots/registry-sync-bot.js"],
  },
  {
    id: "finance-ops-reporter",
    kind: "python",
    label: "Financial Ops Reporter (nexus/finance_ops_report.py)",
    cmd: ["python3", "nexus/finance_ops_report.py"],
    note: "Writes ops/reports/financial-ops-report.{json,md} — the reporting side of the financial-ops bots, at $0.",
  },
  {
    id: "repo-assessor",
    kind: "python",
    label: "Repo Assessor (nexus/repo_assessment.py)",
    cmd: ["python3", "nexus/repo_assessment.py", "--repo-root", ".", "--json"],
    captureTo: "reports/repo-assessment.json",
  },
  {
    id: "asset-finder",
    kind: "python",
    label: "Asset Finder (nexus/asset_finder.py)",
    cmd: ["python3", "nexus/asset_finder.py", "--root", "."],
    captureTo: "reports/asset-finder.txt",
  },
  {
    id: "telemetry-monitor",
    kind: "python",
    label: "Telemetry Monitor (nexus.telemetry_monitor)",
    cmd: ["python3", "-m", "nexus.telemetry_monitor", "--iterations", "1"],
    captureTo: "reports/telemetry-snapshot.json",
  },
];

// ── Fleet manifest: the full classification of Todd's agent fleet ─────────────
function buildManifest() {
  const manifest = {
    generatedBy: "fleet-runner",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    policy: "Everything that runs locally is deterministic code — zero AI credits, zero cloud cost. Agents needing an execution engine or human gating are classified as such and are never run automatically.",
    runByFleetRunner: FLEET.map((f) => f.id),
    notRun: [],
  };

  // MCP registry agents — definitions
  try {
    const reg = JSON.parse(fs.readFileSync(path.join(ROOT, "mcp/nexus-agent-registry.json"), "utf8"));
    manifest.notRun.push({
      group: "MCP registry agents",
      count: (reg.agents || []).length,
      runtime: "definition-only",
      cost: "$0 unless wired to a paid model — these are registry entries describing duties, tools, and authority; they execute only when an engine invokes them.",
      source: "mcp/nexus-agent-registry.json",
    });
  } catch { /* registry unreadable — health bot reports it */ }

  // Financial-ops bots — human-gated
  try {
    const botsDef = JSON.parse(fs.readFileSync(path.join(ROOT, "mcp/agents/financial-ops-bots.json"), "utf8"));
    manifest.notRun.push({
      group: "Financial-ops bots",
      count: (botsDef.financialOpsBots && botsDef.financialOpsBots.bots || []).length,
      runtime: "human-gated definitions",
      cost: "$0 — by design they never execute autonomously; their reporting side runs via finance-ops-reporter above.",
      source: "mcp/agents/financial-ops-bots.json",
    });
  } catch { /* same */ }

  // Skills library
  let skills = [];
  try { skills = fs.readdirSync(path.join(ROOT, "skills")).filter((d) => !d.startsWith(".")); } catch { /* none */ }
  manifest.notRun.push({
    group: "Skills library",
    count: skills.length,
    runtime: "reference definitions",
    cost: "$0 — a library of skill definitions agents can consult; no runtime cost until used.",
    source: "skills/",
  });

  return manifest;
}

// ── Run ───────────────────────────────────────────────────────────────────────
function main() {
  fs.mkdirSync(REPORTS_DIR, { recursive: true });

  const results = [];
  for (const bot of FLEET) {
    const started = Date.now();
    const run = spawnSync(bot.cmd[0], bot.cmd.slice(1), {
      cwd: ROOT,
      encoding: "utf8",
      timeout: 120000,
    });
    const ok = run.status === 0;
    const durationMs = Date.now() - started;

    if (ok && bot.captureTo) {
      fs.writeFileSync(path.join(ROOT, bot.captureTo), run.stdout || "");
    }
    results.push({
      id: bot.id,
      label: bot.label,
      ok,
      exitCode: run.status,
      durationMs,
      creditsUsed: 0,
      note: bot.note || "",
    });
    console.log(`  ${ok ? "✓" : "✗"} ${bot.label} (${durationMs}ms)`);
    if (!ok && run.stderr) {
      console.error(run.stderr.split("\n").slice(-3).join("\n"));
    }
  }

  const report = {
    generatedBy: "fleet-runner",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    mode: "local $0 runtime — no GitHub Actions, no AI credits",
    summary: {
      total: results.length,
      passed: results.filter((r) => r.ok).length,
      failed: results.filter((r) => !r.ok).length,
    },
    results,
    manifest: buildManifest(),
  };

  fs.writeFileSync(path.join(REPORTS_DIR, "fleet-report.json"),
    JSON.stringify(report, null, 2) + "\n");
  fs.writeFileSync(path.join(REPORTS_DIR, "fleet-manifest.json"),
    JSON.stringify(report.manifest, null, 2) + "\n");

  console.log(`\n✓ Fleet run complete: ${report.summary.passed}/${report.summary.total} tools OK — 0 AI credits, 0 cloud cost`);
  if (report.summary.failed > 0) process.exit(1);
}

main();
