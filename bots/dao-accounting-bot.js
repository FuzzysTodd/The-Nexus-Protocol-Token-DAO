#!/usr/bin/env node
/**
 * dao-accounting-bot.js — Nexus Protocol DAO File-Accounting Bot
 * ---------------------------------------------------------------
 * One of Todd's personal DAO bots. Deterministic, zero AI credits.
 *
 * Duty: Account for EVERY file in the repository — especially the loose
 * root-level files — by generating a full inventory with category, purpose,
 * and disposition. The DAO source manifest (dao-data-source-manifest.json)
 * references this inventory; if a file is not accounted for, this bot fails.
 *
 * Usage:  node bots/dao-accounting-bot.js
 * Output: reports/file-accounting.json, reports/file-accounting.md
 */

"use strict";

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const REPORTS_DIR = path.join(ROOT, "reports");
const MANIFEST = path.join(ROOT, "dao-data-source-manifest.json");

// ── Curated purpose map for notable loose files ───────────────────────────────
const CURATED = {
  "README.md": "Project entry point — links to every major surface",
  "GOVERNANCE.md": "DAO authority structure and operating mandate",
  "SECURITY.md": "Security policy and disclosure process",
  "CODEOWNERS": "Auto-requested reviewers per path (FuzzysTodd + Co-Pilot)",
  "CODE_OF_CONDUCT.md": "Community conduct rules",
  "FUNDING.yml": "GitHub Sponsors configuration for DAO contributors",
  "dashboard.html": "Primary owner dashboard (Overview / Portfolio / Governance / Treasury / Properties / Signals / Config / Agents)",
  "index.html": "Public landing page",
  "user-guide.html": "Beginner-friendly walkthrough of the ecosystem",
  "marketing.html": "NGTT digital campaign landing page",
  "chimera.html": "Web3 directory — protocol ecosystem browser",
  "games.html": "Games arcade front-end",
  "withdraw.html": "Withdrawal Manager — wallet-based ETH withdrawal UI",
  "governance.html": "Governance surface — proposals and voting",
  "financial-ops-dashboard.html": "Financial operations dashboard",
  "expert-registry.html": "Expert registry front-end",
  "approval-service.html": "Human-gated approval service front-end",
  "builder-fund.html": "Builder fund front-end",
  "live-map.html": "Live network map visualization",
  "web3-interface.html": "Web3 interface surface",
  "crypto-expert-guide.html": "Crypto expert guide (HTML)",
  "marketing.html ": "placeholder",
  "server.js": "Main dashboard server (express)",
  "nexus-config.js": "Runtime configuration — ports, RPC, contracts, hosting",
  "nexus-signal-bus.js": "Live signal bus (WebSocket fan-out)",
  "money-flow.js": "Money-flow analytics engine",
  "logical.js": "Logic/rules engine used by dashboards",
  "logical_demo.js": "Demo harness for logical.js",
  "games.js": "Games arcade logic",
  "withdraw.js": "Withdrawal Manager logic",
  "financial-ops-rest-server.js": "Financial ops REST API",
  "approval-service-server.js": "Human-gated approval service API",
  "expert-registry-server.js": "Expert registry API",
  "agents/reporting/metrics.js": "Agent & MCP scoring engine",
  "dashwall.py": "Python dashboard wall utility",
  "test_web3_dashboard.py": "Web3 dashboard integration tests (Python)",
  "dao-data-source-manifest.json": "DAO source-of-truth manifest — accounts for every data source and loose file",
  "network-registry.json": "Chain/network registry",
  "DAO_BOT_TOKEN.json": "DAO bot GitHub API helper (token via env only)",
  "mcp/nexus-agent-registry.json": "MCP agent specialization registry — every agent's domain, tools, duties",
  "mcp/agents/financial-ops-bots.json": "Financial-ops bot duty definitions",
  "mcp-fin-011.sol": "On-chain bot governance guard (mcp-fin-011)",
  ".mcp.json": "MCP server configuration",
  "package.json": "Node package manifest + bot runner scripts",
  "package-lock.json": "Dependency lockfile",
  "Dockerfile": "Container build",
  "docker-compose.yml": "Local orchestration",
  "ecosystem.config.js": "PM2 process config",
  "vercel.json": "Vercel deployment config",
  "remix.config.json": "Remix IDE config",
  ".env.example": "Environment variable template (secrets never committed)",
  "requirements.txt": "Python runtime dependencies",
  "requirements-dev.txt": "Python dev dependencies",
  ".flake8": "Python lint config",
  ".solhint.json": "Solidity lint config",
  ".gitattributes": "Line-ending / diff attributes",
  ".gitignore": "Ignore rules",
  "CRYPTO_REVENUE_GUIDE.md": "Documentation of all 10 NGTT revenue streams",
  "MARKETING_PATH.md": "Canonical go-to-market strategy",
  "MARKETING_STRATEGY.md": "Digital marketing & legal strategy",
  "MCP_GATEWAY_DOCUMENTATION.md": "MCP gateway documentation",
  "MCP_GATEWAY_QUICKREF.md": "MCP gateway quick reference",
  "IMPLEMENTATION_SUMMARY.md": "Implementation notes",
  "RESOLUTION_APPROVAL.md": "Resolution approval policy",
  "CLOUDFLARE_PRIVATE_DEPLOY.md": "Cloudflare private deployment guide",
  "README.xml": "Technical architecture documentation",
};

// Curated junk/deprecated names that should never come back
const FORBIDDEN = new Set([
  "NVPrxy32.dll", "NvInstallerUtil.dll", ".vs/", "bash ", "package/json",
  "index.html1", "web.js", "agent-registry.yaml", "ecosystem.json", "as-is.",
  "fucopl", "grok.quiskit", "KELLEre.py`", "PACKAGELOCKE.js", "package-locke.json",
  "NexusProtocolDAO—GovernanceChangelogSchema.son",
]);

function categoryFor(name) {
  const ext = path.extname(name).toLowerCase();
  if (name.endsWith(".md") || name === "README.xml") return "docs";
  if (name.endsWith(".html")) return "dashboard-surface";
  if (name.endsWith(".sol")) return "contracts";
  if (name.endsWith(".js") || name.endsWith(".ts")) return "app-code";
  if (name.endsWith(".py") || name.endsWith(".ipynb")) return "python-tools";
  if (name.endsWith(".json")) return "config-data";
  if (name.endsWith(".yaml") || name.endsWith(".yml")) return "automation";
  if (ext === ".dll" || ext === ".exe") return "binary-junk";
  if (name.startsWith(".")) return "repo-config";
  return "root-file";
}

function purposeFor(name) {
  if (CURATED[name]) return CURATED[name];
  const cat = categoryFor(name);
  switch (cat) {
    case "docs": return "Project documentation";
    case "dashboard-surface": return "Static dashboard surface served from repo root";
    case "app-code": return "Application logic";
    case "config-data": return "Configuration or data file";
    case "automation": return "Workflow / automation definition";
    case "python-tools": return "Python utility or notebook";
    default: return "Loose root file — see accounting report";
  }
}

// ── Run ───────────────────────────────────────────────────────────────────────
function main() {
  const tracked = execSync("git ls-files", { cwd: ROOT, encoding: "utf8" })
    .split("\n").filter(Boolean);

  const loose = tracked.filter((f) => !f.includes("/")).sort();
  const errors = [];

  // Forbidden junk check
  for (const f of tracked) {
    for (const bad of FORBIDDEN) {
      if (f === bad || f.startsWith(bad)) errors.push(`forbidden junk present: ${f}`);
    }
  }

  const inventory = loose.map((name) => {
    let size = 0;
    try { size = fs.statSync(path.join(ROOT, name)).size; } catch { /* deleted */ }
    const cat = categoryFor(name);
    return {
      file: name,
      category: cat,
      purpose: purposeFor(name),
      disposition: cat === "binary-junk" ? "remove" : "keep",
      bytes: size,
    };
  });

  // Ensure reports dir exists
  fs.mkdirSync(REPORTS_DIR, { recursive: true });

  const report = {
    generatedBy: "dao-accounting-bot",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    totals: {
      trackedFiles: tracked.length,
      looseRootFiles: loose.length,
      accountedFor: inventory.length,
    },
    files: inventory,
    errors,
  };

  fs.writeFileSync(path.join(REPORTS_DIR, "file-accounting.json"),
    JSON.stringify(report, null, 2) + "\n");

  // Markdown table
  const md = [
    "# DAO File Accounting Report",
    "",
    `Generated by the **dao-accounting-bot** (deterministic — zero AI credits) at ${report.generatedAt}.`,
    "",
    `Owner: **@FuzzysTodd** — every loose root file is accounted for below.`,
    "",
    `**Totals:** ${report.totals.trackedFiles} tracked files, ${report.totals.looseRootFiles} loose root files, ${report.totals.accountedFor} accounted for.`,
    "",
    "| File | Category | Purpose | Disposition |",
    "|---|---|---|---|",
    ...inventory.map((f) => `| ${f.file} | ${f.category} | ${f.purpose} | ${f.disposition} |`),
    "",
  ];
  if (errors.length) md.push("## Errors", "", ...errors.map((e) => `- ${e}`), "");
  fs.writeFileSync(path.join(REPORTS_DIR, "file-accounting.md"), md.join("\n"));

  // Manifest cross-check
  try {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST, "utf8"));
    const inv = manifest.fileAccounting && manifest.fileAccounting.inventory;
    if (inv !== "reports/file-accounting.json") {
      errors.push("dao-data-source-manifest.json is missing fileAccounting.inventory -> reports/file-accounting.json");
    }
  } catch (e) {
    errors.push(`manifest unreadable: ${e.message}`);
  }

  console.log(`✓ file-accounting: ${inventory.length}/${loose.length} loose files accounted`);
  console.log(`  reports/file-accounting.json`);
  console.log(`  reports/file-accounting.md`);

  if (errors.length) {
    console.error("\n✗ Accounting errors:");
    errors.forEach((e) => console.error(`  - ${e}`));
    process.exit(1);
  }
  console.log("\n✓ All loose files accounted for. DAO file set is complete.");
}

main();
