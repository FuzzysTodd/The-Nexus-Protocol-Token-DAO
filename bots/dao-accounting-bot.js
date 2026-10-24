#!/usr/bin/env node
/**
 * dao-accounting-bot.js — Nexus Protocol DAO File-Accounting Bot
 * ---------------------------------------------------------------
 * One of Todd's personal DAO bots. Deterministic, zero AI credits.
 *
 * Duty: Account for EVERY tracked file in the repository — the full tree,
 * not just the root — with a category, purpose, and disposition. Files that
 * don't match a known pattern are marked "review" (never silently "keep").
 * The DAO source manifest (dao-data-source-manifest.json) references this
 * inventory; if the manifest policy is violated, this bot fails.
 *
 * Usage:  node bots/dao-accounting-bot.js
 * Output: reports/file-accounting.json, reports/file-accounting.md
 */

"use strict";

// --check: read-only mode used by git hooks — run every check, write nothing
// (a pre-push generator cannot ship files with the push it is part of).
const CHECK_ONLY = process.argv.includes("--check");

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const REPORTS_DIR = path.join(ROOT, "reports");
const MANIFEST = path.join(ROOT, "dao-data-source-manifest.json");

// ── Curated purpose map for notable files ─────────────────────────────────────
const CURATED = {
  "README.md": "Project entry point — links to every major surface",
  "GOVERNANCE.md": "DAO authority structure and operating mandate",
  "SECURITY.md": "Security policy and disclosure process",
  "CODEOWNERS": "Auto-requested reviewers per path (FuzzysTodd + Co-Pilot)",
  "CODE_OF_CONDUCT.md": "Community conduct rules",
  "FUNDING.yml": "GitHub Sponsors configuration for DAO contributors",
  "dashboard.html": "Primary owner dashboard — Overview / Portfolio / Governance / Treasury / Properties / Signals / Config / Agents & Bots",
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
  "dashwall.py": "Python dashboard wall utility",
  "test_web3_dashboard.py": "Web3 dashboard integration tests (Python)",
  "dao-data-source-manifest.json": "DAO source-of-truth manifest — accounts for every data source and file",
  "network-registry.json": "Chain/network registry",
  "DAO_BOT_TOKEN.json": "DAO bot GitHub API helper (token via env only)",
  "mcp/nexus-agent-registry.json": "MCP agent specialization registry — every agent's domain, tools, duties",
  "mcp/agents/financial-ops-bots.json": "Financial-ops bot duty definitions",
  "mcp-fin-011.sol": "On-chain bot governance guard (mcp-fin-011)",
  "docs/governance-changelog-schema.json": "Governance changelog JSON schema",
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
  "LICENSE": "MIT license (Todd Stephens / FuzzysTodd)",
  "CRYPTO_REVENUE_GUIDE.md": "Documentation of all 10 NGTT revenue streams",
  "MARKETING_PATH.md": "Canonical go-to-market strategy",
  "MARKETING_STRATEGY.md": "Digital marketing & legal strategy",
  "MCP_GATEWAY_DOCUMENTATION.md": "MCP gateway documentation",
  "MCP_GATEWAY_QUICKREF.md": "MCP gateway quick reference",
  "IMPLEMENTATION_SUMMARY.md": "Implementation notes",
  "RESOLUTION_APPROVAL.md": "Resolution approval policy",
  "CLOUDFLARE_PRIVATE_DEPLOY.md": "Cloudflare private deployment guide",
  "README.xml": "Technical architecture documentation",
  "dap": "Example ethers.js integration code for Project Chimera contracts (frontend reference)",
  "githubprice.gh": "GitHub CLI snippet — quest-synthesis / price-lookup experiment (operator notes)",
  "Snippets_Importing_libraries.ipynb": "Reference notebook — library import snippets",
  "universal_quantum_law.ipynb": "Personal research notebook — universal quantum law exploration",
  ".devcontainer/post-create.sh": "Codespace post-create setup script",
  ".devcontainer/devcontainer.json": "Codespace container definition",
  "scripts/setup-identity.sh": "One-time git identity + frictionless pull/push setup",
  "scripts/install-hooks.sh": "Installs the DAO-bot git hooks (Actions-free automation)",
  "scripts/bots-daily.sh": "Daily DAO bot run without GitHub Actions (cron / manual)",
  "scripts/bots-daily.cmd": "Daily DAO bot run without GitHub Actions (Windows Task Scheduler)",
  "scripts/start-local.sh": "Local stack launcher",
  "bots/health-bot.js": "DAO Health Bot — deterministic repo health checks",
  "bots/dao-accounting-bot.js": "DAO File-Accounting Bot (this file)",
  "bots/registry-sync-bot.js": "DAO Registry Sync Bot — feeds dashboard agent data",
  "bots/fleet-runner.js": "Agent Fleet Runner — runs Todd's full bot/agent fleet locally at $0 (no Actions, no AI credits)",
  "reports/fleet-report.json": "Fleet run results (fleet-runner output)",
  "reports/fleet-manifest.json": "Fleet classification — what runs at $0 locally vs definition-only vs human-gated",
  "reports/repo-assessment.json": "Repo assessor output (read-only snapshot)",
  "reports/asset-finder.txt": "Token/contract asset inventory (asset-finder output)",
  "reports/telemetry-snapshot.json": "Telemetry snapshot (telemetry-monitor output)",
  "reports/telemetry-snapshot.txt": "Telemetry dashboard render (telemetry-monitor output, saved as text)",
  "reports/intel.json": "Internet intel — market prices + repo stats (intel-bot output)",
  "reports/file-accounting.json": "Machine-readable accounting inventory (this bot's output)",
  "reports/file-accounting.md": "Human-readable accounting report (this bot's output)",
  "reports/agents.json": "Dashboard agent/bot payload (registry-sync bot output)",
  "reports/health-report.json": "Health bot output",
};

// Top-level directories with known purpose
const DIR_PURPOSE = {
  ".github": "GitHub workflows, issue templates, and repo automation",
  "contracts": "Solidity smart contracts (NGTT token, governance, treasury)",
  "governance": "Governance artifacts and changelogs",
  "docs": "Project documentation",
  "mcp": "MCP agent registry, gateway configs, and game-theory data",
  "agents": "Agent reporting and metrics engines",
  "agent": "Agent tools (Dune analytics)",
  "bots": "Personal DAO bots — deterministic, zero AI credits",
  "scripts": "Operational and deployment scripts",
  "reports": "Bot-generated reports (accounting, health, agents)",
  "githooks": "Git hooks (pre-commit / pre-push) that run the DAO bots locally — Actions-free mode",
  "skills": "Skill definitions library",
  "src": "Application source",
  "web": "Web assets",
  "data": "Data files",
  "ops": "Operations runbooks",
  "ops/reports": "Generated operational reports (financial-ops)",
  "nexus": "Nexus core modules",
  "basic-dao": "Reference DAO implementation",
  "sourcify-verified": "Verified contract sources",
  "playwright-tool": "Browser automation tooling",
  "subscriptions": "Subscription modules",
  "vercel": "Vercel deployment config",
  "package": "(removed typo dir — archived)",
  "archive": "Preserved files from the 2026 revamp (see archive/2026-revamp/README.md)",
};

// Reference protocol directories (imported third-party contract sources)
const REFERENCE_DIRS = new Set([
  "0x", "0xSplits", "1Inch-V2", "Aave-V3", "AntiBot-ERC20", "ApeCoin",
  "Azuki-ERC721A-ERC721A", "Azuki-ERC721A-ERC721ABurnable", "Azuki-ERC721A-ERC721ABurnableMock",
  "Azuki-ERC721A-NFT-Sale", "Azuki-ERC721A-NFT-Sale-basic", "Buyback-Token-with-Fees",
  "ChainLink", "Circle-USDC-FiatTokenV2", "Compound", "Delegate", "Eigenlayer",
  "Ethereum-Name-Service", "ERC20-NFT-Sale-with-Distributed-Royalties", "FlashloanAttacker",
  "GMX.io", "Gnosis-Safe", "Lens-Protocol", "Lyra-Finance", "Manifold.xyz",
  "Moonbirds-Core", "NGTT", "Nouns-DAO", "Olympus-DAO", "OpenSea-Seaport", "POAP",
  "PancakeSwap-V3", "STFIL", "SuperFluid", "SushiSwap-V3", "Synthetix", "Ubeswap",
  "Umbra-Cash", "Uniswap-V2", "Uniswap-V3", "Uniswap-V4", "WorldCoin-Core",
  "burnable-token", "dividend-paying-token-with-buy-sell-fee",
  "erc20-token-with-automatic-vesting", "flagship-cookbook-nft",
  "mintable-token", "multi-collection-nft-with-burnable-nfts-and-pausable-transfers",
  "nft-staking-with-infinite-rewards", "on-chain-income-splitter-and-distributor",
  "reflection-token-supporting-3-wallets", "royalty-splitter", "simple-nft-sale",
  "soulbound-nft", "tether-usdt", "voting-token",
]);

// ── Helpers ───────────────────────────────────────────────────────────────────

function categoryFor(relPath) {
  const name = path.basename(relPath);
  const ext = path.extname(name).toLowerCase();
  const topDir = relPath.includes("/") ? relPath.split("/")[0] : null;
  if (isReferenceDir(topDir)) return "reference-source";
  if (CURATED[relPath]) {
    if (relPath.endsWith(".md") || relPath === "README.xml") return "docs";
    if (relPath.endsWith(".html")) return "dashboard-surface";
    if (relPath.endsWith(".sol")) return "contracts";
    if (ext === ".js" || ext === ".ts") return "app-code";
    if (ext === ".json") return "config-data";
  }
  if (name.endsWith(".md") || name === "README.xml") return "docs";
  if (name.endsWith(".html")) return "dashboard-surface";
  if (name.endsWith(".sol")) return "contracts";
  if (ext === ".js" || ext === ".ts") return "app-code";
  if (ext === ".py") return "python-tools";
  if (ext === ".json") return "config-data";
  if (ext === ".yaml" || ext === ".yml" || ext === ".sh") return "automation";
  if (ext === ".dll" || ext === ".exe") return "binary-junk";
  if (topDir && DIR_PURPOSE[topDir]) return "known-directory";
  if (!topDir) return "loose-root-file";
  return "unclassified";
}

function isReferenceDir(dir) {
  return dir !== null && REFERENCE_DIRS.has(dir);
}

function purposeFor(relPath) {
  if (CURATED[relPath]) return CURATED[relPath];
  const parts = relPath.split("/");
  const topDir = parts.length > 1 ? parts[0] : null;
  if (topDir && REFERENCE_DIRS.has(topDir)) {
    return `Reference source imported for study — ${topDir}`;
  }
  if (topDir && DIR_PURPOSE[topDir]) return DIR_PURPOSE[topDir];
  const cat = categoryFor(relPath);
  switch (cat) {
    case "docs": return "Documentation";
    case "dashboard-surface": return "Static dashboard surface";
    case "app-code": return "Application logic";
    case "contracts": return "Smart contract source";
    case "config-data": return "Configuration or data file";
    case "automation": return "Workflow / automation definition";
    case "python-tools": return "Python utility or notebook";
    case "loose-root-file": return "Loose root file — purpose not yet documented";
    case "unclassified": return "Unclassified — needs review";
    default: return "See category";
  }
}

// Deterministic write: only replace the file if content (ignoring the
// generatedAt timestamp) actually changed — avoids commit churn in CI.
function writeIfChanged(filePath, content, stripPattern) {
  let existing = null;
  try { existing = fs.readFileSync(filePath, "utf8"); } catch { /* absent */ }
  const norm = (s) => (stripPattern ? s.replace(stripPattern, "generatedAt: <ts>") : s);
  if (existing !== null && norm(existing) === norm(content)) {
    return false;
  }
  fs.writeFileSync(filePath, content);
  return true;
}

// ── Run ───────────────────────────────────────────────────────────────────────
function main() {
  // NUL-delimited so unusual filenames survive without git quoting
  const raw = execSync("git ls-files -z", { cwd: ROOT, encoding: "buffer" });
  const tracked = raw.toString("utf8").split("\0").filter(Boolean);

  const errors = [];

  // Forbidden junk check
  const junkRes = [/[.]dll$/i, /[.]exe$/i, /^\.vs\//, /^index\.html1$/, /^as-is\.$/];
  for (const f of tracked) {
    if (junkRes.some((re) => re.test(f))) errors.push(`forbidden junk present: ${f}`);
  }

  // Full-tree inventory
  const inventory = tracked.map((relPath) => {
    let size = 0;
    try { size = fs.statSync(path.join(ROOT, relPath)).size; } catch { /* deleted */ }
    const cat = categoryFor(relPath);
    const purpose = purposeFor(relPath);
    const disposition =
      cat === "binary-junk" ? "remove"
      : cat === "unclassified" ? "review"
      : cat === "loose-root-file" && !CURATED[relPath] ? "review"
      : "keep";
    return { file: relPath, category: cat, purpose, disposition, bytes: size };
  });

  const loose = inventory.filter((f) => !f.file.includes("/"));
  const unaccounted = inventory.filter((f) => f.disposition === "review");

  // ── Inventory-drift check: saved report must cover the same file set ───────
  // Compares the SAVED inventory (reports/file-accounting.json) against the
  // current tracked set — catches stale inventories loudly instead of
  // silently. Error in write mode; warning in --check mode (hooks) so adding
  // files doesn't block commits until the next fleet run refreshes it.
  const currentSet = new Set(tracked);
  let savedFiles = [];
  try {
    const saved = JSON.parse(fs.readFileSync(path.join(REPORTS_DIR, "file-accounting.json"), "utf8"));
    savedFiles = (saved.files || []).map((f) => f.file);
  } catch { /* no saved report yet — first run */ }
  const savedSet = new Set(savedFiles);
  const missingFromSaved = tracked.filter((f) => !savedSet.has(f));
  const extraInSaved = savedFiles.filter((f) => !currentSet.has(f));
  if (missingFromSaved.length || extraInSaved.length) {
    const msg = `inventory drift: ${missingFromSaved.length} tracked file(s) missing from saved inventory` +
      `${extraInSaved.length ? `, ${extraInSaved.length} stale entr(ies)` : ""}`;
    if (CHECK_ONLY) {
      console.log(`  ⚠ ${msg} — refresh with: npm run agents:run (warning, non-blocking in check mode)`);
    } else {
      // write mode: the fresh inventory written below heals the drift itself
      console.log(`  ⚠ ${msg} — self-healed by this run's fresh inventory`);
    }
  }

  // Manifest cross-check
  let manifestOk = false;
  try {
    const manifest = JSON.parse(fs.readFileSync(MANIFEST, "utf8"));
    const inv = manifest.fileAccounting && manifest.fileAccounting.inventory;
    if (inv !== "reports/file-accounting.json") {
      errors.push("dao-data-source-manifest.json is missing fileAccounting.inventory -> reports/file-accounting.json");
    } else {
      manifestOk = true;
    }
  } catch (e) {
    errors.push(`manifest unreadable: ${e.message}`);
  }

  // ── Write reports (errors included) — skipped in --check mode ─────────────
  fs.mkdirSync(REPORTS_DIR, { recursive: true });

  const report = {
    generatedBy: "dao-accounting-bot",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    totals: {
      trackedFiles: tracked.length,
      looseRootFiles: loose.length,
      accounted: inventory.filter((f) => f.disposition === "keep").length,
      needsReview: unaccounted.length,
    },
    policy: "Every tracked file appears below with category, purpose, and disposition. 'review' items need a documented purpose before they can be marked 'keep'.",
    files: inventory,
    needsReview: unaccounted.map((f) => f.file),
    errors,
  };

  const changedJson = CHECK_ONLY ? false : writeIfChanged(
    path.join(REPORTS_DIR, "file-accounting.json"),
    JSON.stringify(report, null, 2) + "\n",
    /"generatedAt": "[^"]+"/
  );

  const md = [
    "# DAO File Accounting Report",
    "",
    `Generated by the **dao-accounting-bot** (deterministic — zero AI credits).`,
    "",
    `Owner: **@FuzzysTodd** — every tracked file is accounted for below.`,
    "",
    `**Totals:** ${report.totals.trackedFiles} tracked files (${report.totals.looseRootFiles} loose root files) — ${report.totals.accounted} accounted, ${report.totals.needsReview} flagged for review.`,
    "",
    "| File | Category | Purpose | Disposition |",
    "|---|---|---|---|",
    ...inventory.map((f) => `| ${f.file} | ${f.category} | ${f.purpose} | ${f.disposition} |`),
    "",
  ];
  if (unaccounted.length) {
    md.push("## Needs Review", "",
      ...unaccounted.map((f) => `- ${f.file} — ${f.purpose}`), "");
  }
  if (errors.length) md.push("## Errors", "", ...errors.map((e) => `- ${e}`), "");
  if (!CHECK_ONLY) fs.writeFileSync(path.join(REPORTS_DIR, "file-accounting.md"), md.join("\n"));

  console.log(`✓ file-accounting: ${inventory.length} tracked files inventoried`);
  console.log(`  loose root: ${loose.length} — needs review: ${unaccounted.length}`);
  if (!CHECK_ONLY) console.log(`  reports/file-accounting.json ${changedJson ? "(updated)" : "(unchanged)"}`);
  if (!CHECK_ONLY) console.log(`  reports/file-accounting.md`);

  const hardFail = errors.length > 0 || !manifestOk;
  if (hardFail) {
    console.error("\n✗ Accounting errors:");
    errors.forEach((e) => console.error(`  - ${e}`));
    process.exit(1);
  }
  console.log("\n✓ Manifest policy satisfied. DAO file set is complete.");
}

main();
