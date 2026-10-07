/**
 * Nexus Protocol — Unified Dashboard Server
 *
 * Serves all HTML dashboards as static files from the repo root
 * and exposes the approval-service REST API on /api/approval/*.
 *
 * Ports:
 *   PORT (default 3000) — main HTTP server (static + API)
 *
 * The withdraws API and signal bus each run as separate processes
 * via scripts/start-local.sh or scripts/start-remote.sh.
 */

"use strict";

const express = require("express");
const path    = require("path");
const fs      = require("fs");

const app  = express();
const PORT = Number(process.env.PORT || process.env.APPROVAL_SERVICE_PORT || 3000);
const ROOT = __dirname;

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// ── Approval-service state helpers ───────────────────────────────────────────
const STATE_FILE = path.join(ROOT, ".approval-service-state.json");

function readState() {
  try { return JSON.parse(fs.readFileSync(STATE_FILE, "utf8")); }
  catch (_) { return { serviceUrl: `http://localhost:${PORT}`, audit: [], lastTest: null, lastError: null }; }
}

function writeState(state) {
  fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2));
}

// ── Approval-service REST API ─────────────────────────────────────────────────
app.get("/api/approval/state", (_req, res) => res.json(readState()));

app.post("/api/approval/approve", (req, res) => {
  const state = readState();
  const entry = { action: "approve", ok: true, message: req.body.message || "Approved", timestamp: new Date().toISOString() };
  state.audit.push(entry);
  state.lastTest = entry;
  writeState(state);
  res.json({ ok: true, entry });
});

app.post("/api/approval/reject", (req, res) => {
  const state = readState();
  const entry = { action: "reject", ok: false, message: req.body.message || "Rejected", timestamp: new Date().toISOString() };
  state.audit.push(entry);
  state.lastError = entry;
  writeState(state);
  res.json({ ok: true, entry });
});

// ── Status / health ───────────────────────────────────────────────────────────
app.get("/api/status", (_req, res) => {
  res.json({
    ok:   true,
    env:  process.env.NEXUS_ENV || "local",
    ts:   new Date().toISOString(),
    port: PORT,
    dashboards: [
      "/dashboard.html",
      "/financial-ops-dashboard.html",
      "/approval-service.html",
      "/builder-fund.html",
      "/governance.html",
      "/withdraw.html",
      "/unstoppable-dashboard.html",
      "/web3-interface.html",
      "/expert-registry.html",
    ],
  });
});

// ── Serve all HTML dashboards as static files from repo root ─────────────────
// Explicit file list so we don't accidentally serve .env or secrets
const PUBLIC_HTML = [
  "index.html",
  "dashboard.html",
  "financial-ops-dashboard.html",
  "approval-service.html",
  "builder-fund.html",
  "governance.html",
  "withdraw.html",
  "unstoppable-dashboard.html",
  "web3-interface.html",
  "expert-registry.html",
  "chimera.html",
  "games.html",
  "marketing.html",
  "crypto-expert-guide.html",
  "user-guide.html",
  "live-map.html",
];

PUBLIC_HTML.forEach((file) => {
  const filePath = path.join(ROOT, file);
  if (fs.existsSync(filePath)) {
    app.get(`/${file}`, (_req, res) => res.sendFile(filePath));
  }
});

// ── Root → dashboard ─────────────────────────────────────────────────────────
app.get("/", (_req, res) => {
  const dashPath = path.join(ROOT, "dashboard.html");
  if (fs.existsSync(dashPath)) return res.sendFile(dashPath);
  res.json({ ok: true, message: "Nexus Protocol API is running", docs: "/api/status" });
});

// ── 404 fallback ──────────────────────────────────────────────────────────────
app.use((_req, res) => res.status(404).json({ error: "Not found" }));

// ── Start ─────────────────────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`[Nexus] Dashboard server running → http://localhost:${PORT}`);
  console.log(`[Nexus] Environment: ${process.env.NEXUS_ENV || "local"}`);
  console.log(`[Nexus] GET /api/status for endpoint list`);
});
