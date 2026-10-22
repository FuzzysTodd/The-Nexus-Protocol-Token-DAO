#!/usr/bin/env node
/**
 * fleet-runner.js — Nexus DAO Agent Fleet Runner ($0 local runtime)
 * -------------------------------------------------------------------
 * Todd's personal fleet of bots/agents, operating without cloud cost:
 *   • No GitHub Actions charges (account billing lock) — runs locally instead
 *   • No model API calls — every tool below is deterministic code
 *
 * Scope (honest): this runs SEVEN maintenance/reporting commands. The 11 MCP
 * registry agents remain definitions (they execute only when wired to an
 * engine), and the 3 financial-ops bots stay human-gated — this runner does
 * NOT implement their full operational duties, only the reporting side.
 *
 * What each executed tool actually does (verified by inspection):
 *   • Node bots — read local files, run local git
 *   • finance_ops_report.py / asset_finder.py — pure local file scanning
 *   • repo_assessment.py — local file scan + local git
 *   • telemetry_monitor.py — local hardware query (nvidia-smi) + local
 *     network-interface listing. No external network requests.
 *
 * Execution order matters: generators run FIRST, the File-Accounting Bot runs
 * LAST (after outputs exist and are staged) so its inventory is never stale.
 *
 * Usage:  node bots/fleet-runner.js           (or:  npm run agents:run)
 * Output: reports/fleet-report.json, reports/fleet-manifest.json + tool reports
 */

"use strict";

const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const REPORTS_DIR = path.join(ROOT, "reports");

// Generated-output allowlist: everything the fleet writes, and everything
// the daily runner is allowed to stage and commit. Nothing else.
const OUTPUT_PATHSPECS = ["reports/", "ops/reports/"];

// ── Python interpreter detection (python3 / python / py -3) ───────────────────
function detectPython() {
  for (const cand of [["python3"], ["python"], ["py", "-3"]]) {
    try {
      const r = spawnSync(cand[0], [...cand.slice(1), "--version"], { encoding: "utf8", timeout: 10000 });
      if (r.status === 0) return cand;
    } catch { /* try next */ }
  }
  return null;
}
const PYTHON = detectPython();

// ── Deterministic writes ─────────────────────────────────────────────────────
// Strip volatile values (timestamps, durations) before comparing, so a run
// only rewrites a file when its MEANINGFUL content changed. Prevents commit
// churn from timestamps/execution durations.
function normalize(s) {
  return s
    .replace(/"generatedAt": "[^"]*"/g, '"generatedAt": "<ts>"')
    .replace(/"ts": "[^"]*"/g, '"ts": "<ts>"')
    .replace(/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})/g, "<iso-ts>")
    .replace(/"durationMs": \d+/g, '"durationMs": <n>');
}

function writeIfChanged(filePath, content) {
  let existing = null;
  try { existing = fs.readFileSync(filePath, "utf8"); } catch { /* absent */ }
  if (existing !== null && normalize(existing) === normalize(content)) return false;
  fs.writeFileSync(filePath, content);
  return true;
}

// ── Fleet definition ──────────────────────────────────────────────────────────
const FLEET = [
  // generators first (their outputs feed the accounting inventory)
  {
    id: "finance-ops-reporter",
    kind: "python",
    label: "Financial Ops Reporter (nexus/finance_ops_report.py)",
    cmd: () => [...PYTHON, "nexus/finance_ops_report.py"],
    note: "Writes ops/reports/financial-ops-report.{json,md} — the reporting side of the financial-ops bots. NOT their full operational duties.",
  },
  {
    id: "repo-assessor",
    kind: "python",
    label: "Repo Assessor (nexus/repo_assessment.py)",
    cmd: () => [...PYTHON, "nexus/repo_assessment.py", "--repo-root", ".", "--json"],
    captureTo: "reports/repo-assessment.json",
  },
  {
    id: "asset-finder",
    kind: "python",
    label: "Asset Finder (nexus/asset_finder.py)",
    cmd: () => [...PYTHON, "nexus/asset_finder.py", "--root", "."],
    captureTo: "reports/asset-finder.txt",
  },
  {
    id: "telemetry-monitor",
    kind: "python",
    label: "Telemetry Monitor (nexus.telemetry_monitor)",
    cmd: () => [...PYTHON, "-m", "nexus.telemetry_monitor", "--iterations", "1"],
    captureTo: "reports/telemetry-snapshot.json",
  },
  // internet intel — public APIs, no key, no model calls by default
  {
    id: "intel-bot",
    kind: "node",
    label: "Intel Bot (internet: public market + repo data)",
    cmd: () => ["node", "bots/intel-bot.js"],
    note: "Fetches public no-key APIs (Coinbase prices, GitHub repo stats). Optional thinking step only runs if NEXUS_MODEL_API_KEY is set — and that costs money per call.",
  },
  // maintenance bots — accounting LAST so it sees every generated output
  { id: "dao-health-bot", kind: "node", label: "Health Bot", cmd: () => ["node", "bots/health-bot.js"] },
  { id: "dao-registry-sync-bot", kind: "node", label: "Registry Sync Bot", cmd: () => ["node", "bots/registry-sync-bot.js"] },
  { id: "dao-accounting-bot", kind: "node", label: "File-Accounting Bot", cmd: () => ["node", "bots/dao-accounting-bot.js"] },
];

// ── Fleet manifest: the full classification of Todd's agent fleet ─────────────
function buildManifest() {
  const manifest = {
    generatedBy: "fleet-runner",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    scope: "Classification of the agent/bot fleet. This runner executes only the maintenance/reporting commands; the rest are definitions that cost nothing until wired to an engine.",
    runByFleetRunner: FLEET.map((f) => f.id),
    notRun: [],
  };

  try {
    const reg = JSON.parse(fs.readFileSync(path.join(ROOT, "mcp/nexus-agent-registry.json"), "utf8"));
    manifest.notRun.push({
      group: "MCP registry agents",
      count: (reg.agents || []).length,
      runtime: "definition-only",
      cost: "No charges unless wired to a paid model — these are registry entries describing duties, tools, and authority; they execute only when an engine invokes them. This runner does not implement them.",
      source: "mcp/nexus-agent-registry.json",
    });
  } catch { /* health bot reports registry problems */ }

  try {
    const botsDef = JSON.parse(fs.readFileSync(path.join(ROOT, "mcp/agents/financial-ops-bots.json"), "utf8"));
    manifest.notRun.push({
      group: "Financial-ops bots",
      count: (botsDef.financialOpsBots && botsDef.financialOpsBots.bots || []).length,
      runtime: "human-gated definitions",
      cost: "By design they never execute autonomously. finance-ops-reporter above covers only their REPORTING side; their operational duties (approvals, fund movement) remain human-gated.",
      source: "mcp/agents/financial-ops-bots.json",
    });
  } catch { /* same */ }

  let skills = [];
  try { skills = fs.readdirSync(path.join(ROOT, "skills")).filter((d) => !d.startsWith(".")); } catch { /* none */ }
  manifest.notRun.push({
    group: "Skills library",
    count: skills.length,
    runtime: "reference definitions",
    cost: "A library of skill definitions agents can consult; no charges until used.",
    source: "skills/",
  });

  return manifest;
}

// ── Run ───────────────────────────────────────────────────────────────────────
function main() {
  if (!PYTHON) {
    console.error("✗ No Python interpreter found (tried python3, python, py -3).");
    console.error("  The 4 nexus/ reporting tools need Python; the Node bots still work via npm run bots:all.");
    process.exit(1);
  }

  fs.mkdirSync(REPORTS_DIR, { recursive: true });

  const results = [];
  for (const bot of FLEET) {
    const started = Date.now();
    const argv = bot.cmd();
    const run = spawnSync(argv[0], argv.slice(1), {
      cwd: ROOT,
      encoding: "utf8",
      timeout: 120000,
    });
    const ok = run.status === 0;
    const durationMs = Date.now() - started;

    if (ok && bot.captureTo) {
      let out = run.stdout || "";
      let target = bot.captureTo;
      // Validate captured JSON — never save unparseable output as .json
      if (target.endsWith(".json")) {
        try {
          JSON.parse(out);
        } catch {
          console.error(`  ⚠ ${bot.id}: stdout is not valid JSON — saving as .txt instead`);
          target = target.replace(/\.json$/, ".txt");
          out = "NOTE: captured stdout failed JSON validation on " + new Date().toISOString() + "\n\n" + out;
        }
      }
      writeIfChanged(path.join(ROOT, target), out);
    }
    results.push({
      id: bot.id,
      label: bot.label,
      ok,
      exitCode: run.status,
      durationMs,
      note: bot.note || "",
    });
    console.log(`  ${ok ? "✓" : "✗"} ${bot.label} (${durationMs}ms)`);
    if (!ok && run.stderr) {
      console.error(run.stderr.split("\n").slice(-3).join("\n"));
    }
  }

  // Stage the fleet's own outputs so the accounting inventory (run last)
  // sees them, and so the daily runner commits exactly this allowlist.
  try {
    spawnSync("git", ["add", ...OUTPUT_PATHSPECS], { cwd: ROOT, encoding: "utf8" });
  } catch { /* not a git checkout — outputs still written */ }

  const report = {
    generatedBy: "fleet-runner",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    mode: "local runtime — no GitHub Actions charges, no model API calls for these commands",
    summary: {
      total: results.length,
      passed: results.filter((r) => r.ok).length,
      failed: results.filter((r) => !r.ok).length,
    },
    results,
    manifest: buildManifest(),
  };

  writeIfChanged(path.join(REPORTS_DIR, "fleet-report.json"), JSON.stringify(report, null, 2) + "\n");
  writeIfChanged(path.join(REPORTS_DIR, "fleet-manifest.json"), JSON.stringify(report.manifest, null, 2) + "\n");
  // the two files above are fleet outputs too — stage them
  try {
    spawnSync("git", ["add", ...OUTPUT_PATHSPECS], { cwd: ROOT, encoding: "utf8" });
  } catch { /* ignore */ }

  console.log(`\n✓ Fleet run complete: ${report.summary.passed}/${report.summary.total} tools OK`);
  console.log("  Charges for these local commands: $0 (no model APIs, no Actions).");
  if (report.summary.failed > 0) process.exit(1);
}

main();
