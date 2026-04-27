# Nexus Builder Fund — Developer Micropayment Protocol

## What it is

The **NexusBuilderFund** is a data-driven, on-chain developer compensation pool.
It answers the question:

> *"Can we sparsely embed a payment API in the code so that every time someone
> uses the protocol, a tiny satoshi/wei fee flows automatically to the builders
> who wrote it?"*

**Yes — and this is exactly how it works.**

---

## How the payment flows

```
User / API caller
    │
    │  pays feePerCall (USD-cent denominated, auto-converted via
    │  Chainlink ETH/USD feed to exact wei)
    ▼
financial-ops-rest-server.js
    │  builderFundUsage.record(endpoint)  — in-process counter
    │
    ▼
GET /api/v1/builder-fund/stats   ← read-only snapshot for dashboards / upkeeps
    │
    │  Chainlink Automation upkeep (or trusted ORACLE_ROLE wallet)
    │  reads the stats endpoint and calls:
    │
    ▼
NexusBuilderFund.recordUsage(endpoint_hash, callCount)  ← on-chain
    │
    │  ETH fees accumulate in the contract from:
    │    • depositFees()  (API gateways, bridges, GitHub Sponsors)
    │    • receive()      (plain ETH transfers)
    │
    ▼
Builder calls claimReward()
    └──► proportional ETH transferred to builder's wallet
```

---

## Fee denomination

| Denomination | Helper | Example (fee = $0.01) |
|---|---|---|
| ETH (wei) | `getFeeWei()` | ≈ 3 333 wei at ETH = $3 000 |
| Bitcoin (satoshi) | `getFeeSatoshis()` | ≈ 1 666 sat at BTC = $60 000 |

Both use Chainlink AggregatorV3 feeds, with a 1-hour staleness guard.
Price denomination is USD-cents — `feePerCallUsdCents = 1` means **$0.01 per call**.

Setting `feePerCallUsdCents = 0` disables per-call enforcement;
fees are deposited externally (Lightning bridge, GitHub Sponsors, etc.).

---

## Data-driven oracle settlement

The REST server tracks usage **in-process** (zero on-chain gas per call).
A **Chainlink Automation** upkeep (or cron job) polls `/api/v1/builder-fund/stats`,
checks if the accumulated delta is worth a gas fee to record, then submits:

```solidity
builderFund.recordUsage(
    keccak256("/api/v1/member"),
    uint256(deltaCallCount)
);
```

This is the "data-driven" pattern: off-chain event → on-chain settlement,
exactly like Chainlink Keepers / The Graph indexer rewards.

---

## Builder registry

Builders are registered by the DAO admin:

```solidity
// Register FuzzysTodd with 100 shares
builderFund.registerBuilder(
    0x33ffc308e693a5b49e0ee0241f41f03ccef495f2,
    100,
    "FuzzysTodd"
);

// Register a contributor with 50 shares
builderFund.registerBuilder(
    0xContributorWallet,
    50,
    "contributor-github-handle"
);
```

Shares are relative weights. With 100 + 50 = 150 total shares:
- FuzzysTodd receives 100/150 = **66.7%** of all deposited fees.
- Contributor receives 50/150 = **33.3%**.

Shares are updatable by the admin at any time.

---

## REST API

| Method | Path | Auth | Description |
|---|---|---|---|
| `GET` | `/api/v1/builder-fund/stats` | Public | Read-only usage snapshot |
| `POST` | `/api/v1/builder-fund/usage` | `Bearer NEXUS_ORACLE_SECRET` | Oracle records a batch of calls |

### Example: read stats

```bash
curl http://localhost:8788/api/v1/builder-fund/stats
```

```json
{
  "service": "nexus-builder-fund-usage",
  "startedAt": "2026-04-27T19:00:00.000Z",
  "snapshotAt": "2026-04-27T20:00:00.000Z",
  "totalCalls": 1842,
  "byEndpoint": {
    "/api/v1/member": 1204,
    "/api/signals":   412,
    "/api/summary":   226
  },
  "builderFundContract": "0x...",
  "oracleNote": "Submit stats.byEndpoint to NexusBuilderFund.recordUsage() via ORACLE_ROLE."
}
```

### Example: oracle records usage

```bash
curl -X POST http://localhost:8788/api/v1/builder-fund/usage \
  -H "Authorization: Bearer $NEXUS_ORACLE_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"endpoint": "/api/v1/member", "callCount": 1204}'
```

---

## Smart contract

**`contracts/NexusBuilderFund.sol`** — key functions:

| Function | Who calls it | Description |
|---|---|---|
| `registerBuilder(wallet, shares, handle)` | Admin | Add a developer to the fund |
| `updateBuilder(id, shares, active)` | Admin | Change shares or deactivate |
| `depositFees(note)` | Anyone (payable) | Deposit ETH into the pool |
| `recordUsage(endpoint, count)` | ORACLE_ROLE | Record off-chain API calls |
| `claimReward()` | Registered builder | Pull proportional ETH share |
| `getFeeWei()` | View | Current per-call fee in wei (Chainlink) |
| `getFeeSatoshis()` | View | Current per-call fee in satoshis (Chainlink) |
| `pendingReward(builderId)` | View | Claimable ETH for a builder |
| `builderCount()` | View | Total registered builders |

---

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `NEXUS_ORACLE_SECRET` | *(empty = no auth)* | Bearer token for POST `/api/v1/builder-fund/usage` |
| `NEXUS_BUILDER_FUND_ADDRESS` | *(empty)* | Deployed contract address (shown in stats) |

---

## Chainlink Automation upkeep script (example)

```javascript
// upkeep.js — run as a Chainlink Automation compatible job
// or as a simple cron: node upkeep.js
const { ethers } = require("ethers");

const STATS_URL   = process.env.STATS_URL || "http://localhost:8788/api/v1/builder-fund/stats";
const CONTRACT    = process.env.NEXUS_BUILDER_FUND_ADDRESS;
const ORACLE_KEY  = process.env.ORACLE_PRIVATE_KEY;
const RPC_URL     = process.env.RPC_URL;

const ABI = [
    "function recordUsage(bytes32 endpoint, uint256 callCount) external",
];

async function run() {
    const stats = await fetch(STATS_URL).then(r => r.json());
    const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
    const signer   = new ethers.Wallet(ORACLE_KEY, provider);
    const fund     = new ethers.Contract(CONTRACT, ABI, signer);

    for (const [endpoint, count] of Object.entries(stats.byEndpoint)) {
        if (count < 10) continue; // Only worth a tx above 10 calls
        const hash = ethers.utils.keccak256(ethers.utils.toUtf8Bytes(endpoint));
        const tx = await fund.recordUsage(hash, count);
        await tx.wait();
        console.log(`Recorded ${count} calls for ${endpoint}: ${tx.hash}`);
    }
}

run().catch(console.error);
```

---

## Academic alignment

- **Protocol Guild** (Ethereum core dev funding) — exact same share-weight pool pattern
- **MIT 15.S12 (Blockchain & Money)** — data-driven settlement without intermediaries
- **Wharton** — proportional revenue share as an incentive alignment mechanism
- **Chainlink Functions / Automation** — the "data-driven" oracle bridge between off-chain usage and on-chain payment

---

*Part of the Nexus Protocol DAO strategic plan — Phase 2 signal bus / builder compensation.*
*Owner: @FuzzysTodd — governed by GOVERNANCE.md.*
