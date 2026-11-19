# Technical Architecture Specification: The Nexus Protocol Token DAO

**Canonical Authority:** `@FuzzysTodd` (`tenkrypt.cb.id`)  
**Specification Version:** NES v1.0  
**Compliance Standards:** ISO 9001:2015 Clause 8 • IEEE 1012-2016 • ISO 27001 Annex A.12  

---

## 1. System Topology Overview

The Nexus Protocol architecture is organized into four distinct operational tiers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TIER 3: PRESENTATION & INTERFACE                      │
│   • React 18 + Vite Web Application                                         │
│   • Tailwind CSS + Lucide Icons + Recharts Analytics Engine                │
│   • Corrective Action Compliance Command Center                             │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│                  TIER 2: ORCHESTRATION & TELEMETRY BUS                      │
│   • WebSocket Signal Bus (:8790) ws://nexus-event-bus.cb.id:8790           │
│   • Circle Mint & Programmable Wallets Relayer (CCTP)                       │
│   • 6-Agent Autonomous MCP Fleet (Auditor, ML, Particle, Satoshi, Dex, FX) │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│                    TIER 1: CONSENSUS & PURE MATHEMATICS                     │
│   • Pure Logic Engine (src/dao/logic.ts)                                    │
│   • 1,000-Particle Median Consensus Solver                                  │
│   • 7-Vector Boundary Proof Fuzzing Engine                                  │
│   • Basis Point Split Residue Allocator                                     │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│                  TIER 0: ON-CHAIN SMART CONTRACTS (EVM)                     │
│   • NexusGameTheoryToken (NGTT.sol) — 1B Supply, 4% Quorum                  │
│   • NexusDAOTreasury.sol — 48h Timelock, 2-of-2 Guardian Multisig Gate     │
│   • NES v1.0 Payable Smart Contract Factory & Splitter Pools                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. On-Chain Contracts & Interfaces

### `NexusGameTheoryToken.sol`
- **Total Supply:** 1,000,000,000 `NGTT` (18 decimals).
- **Consensus Quorum:** 40,000,000 `NGTT` (4% threshold).
- **Demographic Split:** 7 age categories with progressive game theory weights.

### `NexusDAOTreasury.sol`
- **Withdrawal Tiers:**
  - `Tier 1 (< $25k)`: Single signature, immediate execution.
  - `Tier 2 ($25k - $100k)`: 24-hour timelock delay, 1 guardian co-signature.
  - `Tier 3 (> $100k)`: 48-hour timelock delay, dual 2-of-2 guardian co-signatures.
- **Circuit Breakers:** Anomaly detection threshold trigger halts outgoing withdrawals if gas > 80 Gwei or temperature > 82°C.

---

## 3. Financial Signals Bus (:8790)

The signal bus coordinates real-time oracle data and cross-venue arbitrage telemetry:
- **Port:** `8790`
- **Protocol:** WebSocket with framing format:
  ```json
  {
    "nonce": "0x10002A",
    "channel": "oracle.price.eth_usd",
    "value": 3150.25,
    "unit": "USD",
    "proofHash": "0x370a91ad8205aec26668f391c2cf3bd65162335e40cad5def5c55fbee46db93e",
    "signature": "NES-v1.0-ECDSA:0x...",
    "timestamp": 1730811600000
  }
  ```
- **1,000-Particle Solver:** Dampens deviations using median consensus:
  $$\hat{x} = (1 - \alpha) x_{\text{raw}} + \alpha x_{\text{expected}} \quad (\alpha = 0.85)$$

---

## 4. MCP Agent Fleet Specifications

| Agent ID | Codename | Primary Responsibility | Health Monitoring Interval |
|---|---|---|---|
| `mcp-fin-011` | Sentinel | Contract Bytecode & Chunk Auditor | 15s |
| `mcp-fin-012` | Prophet | ML Predictive Load & Anomaly Detector | 5s |
| `mcp-fin-013` | Particle | 1,000-Particle Median Consensus Solver | 1s |
| `mcp-fin-014` | Sweeper | Micro-Payment & Satoshi Accumulator | 30s |
| `mcp-fin-015` | Arbitrage | Base/Mainnet Triangular DEX Scanner | 2s |
| `dao-accounting-bot.js`| Ledger | Multi-Rail Reserve Reconciliation | 60s |
