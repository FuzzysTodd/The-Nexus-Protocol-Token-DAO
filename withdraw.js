/**
 * Nexus Protocol – Contract Withdrawal Manager
 *
 * Manages a list of owned contracts (stored in localStorage) and lets the
 * owner withdraw ETH proceeds from each one through their transparent proxy
 * interface using MetaMask / ethers.js v5.
 */

// ---------------------------------------------------------------------------
// Transparent-proxy ABI (provided by owner – only exposes proxy-level pieces;
// implementation calls go through the proxy fallback via raw call-data).
// ---------------------------------------------------------------------------
const PROXY_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "_logic", "type": "address"},
            {"internalType": "address", "name": "admin_", "type": "address"},
            {"internalType": "bytes", "name": "_data", "type": "bytes"}
        ],
        "stateMutability": "payable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": false, "internalType": "address", "name": "previousAdmin", "type": "address"},
            {"indexed": false, "internalType": "address", "name": "newAdmin", "type": "address"}
        ],
        "name": "AdminChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": true, "internalType": "address", "name": "beacon", "type": "address"}
        ],
        "name": "BeaconUpgraded",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": true, "internalType": "address", "name": "implementation", "type": "address"}
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {"stateMutability": "payable", "type": "fallback"},
    {"stateMutability": "payable", "type": "receive"}
];

// ---------------------------------------------------------------------------
// Common implementation withdraw selectors that can be called through the
// proxy fallback.  The proxy delegates everything it receives to the
// implementation, so we just need to encode the right call-data.
// ---------------------------------------------------------------------------
const WITHDRAW_METHODS = {
    "withdraw()": "0x3ccfd60b",
    "withdrawAll()": "0x853828b6",
    "release(address)": "0x19165587",
    "withdrawEth()": "0x690d8320",
    "claimRewards()": "0x372500ab",
    "collectProceeds()": "0x55e9b9cc",
    "custom": "custom",
};

// ---------------------------------------------------------------------------
// Storage key
// ---------------------------------------------------------------------------
const STORAGE_KEY = "nexus_withdraw_contracts";
const IMPORT_STORAGE_KEY = "nexus_imported_wallet_data";
const DESTINATION_STORAGE_KEY = "nexus_settlement_destination";
const MAX_DISPLAYED_BALANCES = 25;
const MAX_DISPLAYED_COLLECTIBLES = 25;
const MAX_DISPLAYED_TRANSACTIONS = 25;

// ---------------------------------------------------------------------------
// App state
// ---------------------------------------------------------------------------
let provider = null;
let signer = null;
let signerAddress = null;

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function shortAddr(addr) {
    if (!addr || addr.length < 10) return addr;
    return addr.slice(0, 6) + "…" + addr.slice(-4);
}

function loadContracts() {
    try {
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    } catch (_) {
        return [];
    }
}

function saveContracts(list) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
}

function loadImportedData() {
    try {
        return JSON.parse(localStorage.getItem(IMPORT_STORAGE_KEY) || "null");
    } catch (_) {
        return null;
    }
}

function saveImportedData(payload) {
    localStorage.setItem(IMPORT_STORAGE_KEY, JSON.stringify(payload));
}

function clearImportedData() {
    localStorage.removeItem(IMPORT_STORAGE_KEY);
}

function loadSettlementDestination() {
    try {
        return localStorage.getItem(DESTINATION_STORAGE_KEY) || "";
    } catch (_) {
        return "";
    }
}

function saveSettlementDestination(address) {
    localStorage.setItem(DESTINATION_STORAGE_KEY, address);
}

function showStatus(msg, isError) {
    const el = document.getElementById("status-bar");
    if (!el) return;
    el.textContent = msg;
    el.className = "status-bar " + (isError ? "status-error" : "status-ok");
    el.style.display = "block";
    clearTimeout(el._timer);
    el._timer = setTimeout(() => { el.style.display = "none"; }, 6000);
}

function updateProgress(percent) {
    const progressFill = document.getElementById("progress-fill");
    if (progressFill) {
        progressFill.style.width = percent + "%";
        if (percent >= 100) {
            setTimeout(() => {
                progressFill.style.width = "0%";
            }, 1000);
        }
    }
}

function getMoneyFlowHelper(name) {
    if (
        typeof window !== "undefined" &&
        window.NexusMoneyFlow &&
        typeof window.NexusMoneyFlow[name] === "function"
    ) {
        return window.NexusMoneyFlow[name];
    }
    return null;
}

function formatUsd(value) {
    const formatter = getMoneyFlowHelper("formatUsd");
    if (formatter) {
        return formatter(value);
    }
    const amount = Number(value);
    if (!Number.isFinite(amount)) return "—";
    return `$${amount.toFixed(amount >= 1000 ? 0 : 2)}`;
}

function parseDecimalAmount(amount, decimals) {
    const parser = getMoneyFlowHelper("parseDecimalAmount");
    if (parser) {
        return parser(amount, decimals);
    }
    const numeric = Number(amount);
    if (!Number.isFinite(numeric)) return Number.NaN;
    const precision = Number.isFinite(Number(decimals)) ? Number(decimals) : 0;
    return numeric / (10 ** precision);
}

function classifySettlementRail(entry) {
    const classifier = getMoneyFlowHelper("classifySettlementRail");
    if (classifier) {
        return classifier(entry);
    }
    const chain = String(entry.chain || "unknown").toLowerCase();
    const chainLabel = chain === "base"
        ? "Base"
        : (chain === "ethereum" ? "Ethereum" : (chain.charAt(0).toUpperCase() + chain.slice(1)));
    const collectible = String(entry.asset_type || "").toLowerCase() === "collectible" || entry.token_standard;

    if (collectible) {
        return {
            network: chainLabel,
            destination: chain === "base" ? "Base wallet review" : "Manual NFT review",
            supportsDirectTransfer: false,
            reason: chain === "base"
                ? "Collectibles on Base require manual Coinbase or wallet support checks before transfer."
                : `Collectibles on ${chainLabel} require manual destination review before transfer.`
        };
    }

    if (chain === "base") {
        return {
            network: "Base",
            destination: "Coinbase Base deposit",
            supportsDirectTransfer: true,
            reason: "Use a Base-compatible Coinbase deposit address for direct routing."
        };
    }

    if (chain === "ethereum") {
        return {
            network: "Ethereum",
            destination: "Coinbase Ethereum deposit",
            supportsDirectTransfer: true,
            reason: "Use an Ethereum-compatible Coinbase deposit address for direct routing."
        };
    }

    return {
        network: chainLabel,
        destination: "Manual bridge review",
        supportsDirectTransfer: false,
        reason: `Verify bridge and destination support before sending funds from ${chainLabel}.`
    };
}

function classifyOffRamp(balance) {
    const classifier = getMoneyFlowHelper("classifyOffRamp");
    if (classifier) {
        return classifier(balance);
    }
    const settlement = classifySettlementRail(balance);
    if (String(balance.asset_type || "").toLowerCase() === "collectible" || balance.token_standard) {
        return {
            status: balance.is_spam ? "blocked" : "review",
            label: balance.is_spam ? "Spam / ignore" : "Collectible review",
            reason: balance.is_spam
                ? "Spam collectibles should be ignored and never routed."
                : "Collectibles are excluded from fiat routing and need manual Coinbase/Base transfer review.",
            settlement
        };
    }
    if (balance.low_liquidity) {
        return { status: "review", label: "Low liquidity", reason: "Review route before cash-out.", settlement };
    }
    return { status: "swap", label: "Swap first", reason: "Swap into a supported asset first.", settlement };
}

function summarizeImportedBalances(balances) {
    const summarizer = getMoneyFlowHelper("summarizeImportedBalances");
    if (summarizer) {
        return summarizer(balances);
    }
    return {
        totalValueUsd: (balances || []).reduce((sum, balance) => sum + (Number(balance.value_usd) || 0), 0),
        readyValueUsd: 0,
        swapValueUsd: 0,
        reviewValueUsd: 0,
        blockedValueUsd: 0,
        lowLiquidityCount: (balances || []).filter(balance => balance.low_liquidity).length,
        lowLiquidityValueUsd: 0,
        unpricedAssetCount: (balances || []).filter(balance => !Number.isFinite(Number(balance.value_usd))).length,
        nativeAssetCount: (balances || []).filter(balance => String(balance.address).toLowerCase() === "native").length,
        chains: {}
    };
}

function formatTokenAmount(amount, decimals) {
    const normalized = parseDecimalAmount(amount, decimals);
    if (!Number.isFinite(normalized)) return "—";
    if (normalized >= 1000000) return normalized.toLocaleString(undefined, { maximumFractionDigits: 2 });
    if (normalized >= 1) return normalized.toLocaleString(undefined, { maximumFractionDigits: 6 });
    return normalized.toLocaleString(undefined, { maximumSignificantDigits: 6 });
}

function getSettlementDestination() {
    const input = typeof document !== "undefined"
        ? document.getElementById("settlement-destination")
        : null;
    const value = input ? input.value.trim() : loadSettlementDestination();
    if (typeof ethers !== "undefined" && ethers.utils.isAddress(value)) {
        return value;
    }
    return null;
}

function getSettlementDestinationLabel() {
    return getSettlementDestination() || "No destination configured";
}

function parseHexAmount(value) {
    if (!value) return 0;
    try {
        if (typeof ethers !== "undefined") {
            return Number(ethers.utils.formatEther(value));
        }
    } catch (_) {
        return 0;
    }
    return 0;
}

// ---------------------------------------------------------------------------
// Wallet connection
// ---------------------------------------------------------------------------
async function connectWallet() {
    if (typeof window.ethereum === "undefined") {
        showStatus("MetaMask (or compatible wallet) is not installed.", true);
        return;
    }
    try {
        // Update progress bar
        updateProgress(33);
        
        provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        signer = provider.getSigner();
        signerAddress = await signer.getAddress();
        
        // Update UI elements
        const walletAddressEl = document.getElementById("wallet-address");
        walletAddressEl.textContent = signerAddress;
        walletAddressEl.style.display = "block";
        
        const connectionStatus = document.getElementById("connection-status");
        connectionStatus.className = "connection-status connected";
        connectionStatus.innerHTML = "<span>Connected</span>";
        
        document.getElementById("wallet-section").classList.add("connected");
        document.getElementById("connect-btn").innerHTML = '<span>✓</span><span>Connected</span>';
        document.getElementById("connect-btn").disabled = true;
        document.getElementById("add-contract-form").classList.add("visible");
        document.getElementById("add-contract-form").style.display = "block";
        
        updateProgress(66);
        showStatus("✓ Wallet connected: " + shortAddr(signerAddress));
        await refreshAll();
        updateProgress(100);
    } catch (err) {
        updateProgress(0);
        showStatus("✗ Wallet connection failed: " + err.message, true);
    }
}

// ---------------------------------------------------------------------------
// Add a contract to the list
// ---------------------------------------------------------------------------
function addContract(event) {
    event.preventDefault();
    const addr = document.getElementById("input-address").value.trim();
    const label = document.getElementById("input-label").value.trim() || shortAddr(addr);
    const customAbi = document.getElementById("input-custom-abi").value.trim();
    const method = document.getElementById("input-method").value;
    const customSelector = document.getElementById("input-custom-selector").value.trim();

    if (!ethers.utils.isAddress(addr)) {
        showStatus("✗ Invalid Ethereum address.", true);
        return;
    }

    const list = loadContracts();
    if (list.find(c => c.address.toLowerCase() === addr.toLowerCase())) {
        showStatus("✗ Contract already in the list.", true);
        return;
    }

    list.push({ address: addr, label, customAbi, method, customSelector });
    saveContracts(list);
    document.getElementById("input-address").value = "";
    document.getElementById("input-label").value = "";
    document.getElementById("input-custom-abi").value = "";
    document.getElementById("input-custom-selector").value = "";
    updateProgress(50);
    renderContracts();
    updateProgress(100);
    showStatus("✓ Contract added: " + label);
}

// ---------------------------------------------------------------------------
// Remove a contract from the list
// ---------------------------------------------------------------------------
function removeContract(address) {
    const list = loadContracts().filter(c => c.address.toLowerCase() !== address.toLowerCase());
    saveContracts(list);
    renderContracts();
}

// ---------------------------------------------------------------------------
// Fetch ETH balance for a contract
// ---------------------------------------------------------------------------
async function fetchBalance(address) {
    if (!provider) return "—";
    try {
        const bal = await provider.getBalance(address);
        return ethers.utils.formatEther(bal) + " ETH";
    } catch (_) {
        return "error";
    }
}

// ---------------------------------------------------------------------------
// Execute a withdrawal through the proxy (fallback delegation)
// ---------------------------------------------------------------------------
async function withdrawFromContract(address, method, customSelector, customAbi) {
    if (!signer) {
        showStatus("Connect your wallet first.", true);
        return;
    }

    let callData;
    try {
        if (method === "release(address)") {
            // release(address) needs a payee argument – use the configured destination
            const settlementDestination = getSettlementDestination();
            if (!settlementDestination) {
                showStatus("Configure and verify a destination address before using release(address).", true);
                return;
            }
            const iface = new ethers.utils.Interface([
                "function release(address payee)"
            ]);
            callData = iface.encodeFunctionData("release", [settlementDestination]);
        } else if (method === "custom" && customSelector) {
            // User-supplied hex selector / call-data
            callData = customSelector.startsWith("0x") ? customSelector : "0x" + customSelector;
        } else if (method in WITHDRAW_METHODS) {
            callData = WITHDRAW_METHODS[method];
        } else {
            // If user provided a full implementation ABI, use the first no-arg
            // function whose name contains "withdraw", "release", "claim", or
            // "collect".  Requiring an explicit name avoids accidentally calling
            // an unrelated function.
            if (customAbi) {
                let parsed;
                try {
                    parsed = JSON.parse(customAbi);
                } catch (_) {
                    showStatus("Invalid ABI JSON format – check your input.", true);
                    return;
                }
                const iface = new ethers.utils.Interface(parsed);
                const WITHDRAW_NAMES = /withdraw|release|claim|collect/i;
                const fn = Object.values(iface.functions).find(
                    f => WITHDRAW_NAMES.test(f.name) && f.inputs.length === 0
                );
                if (!fn) {
                    showStatus(
                        "No zero-argument withdraw/release/claim function found in ABI.",
                        true
                    );
                    return;
                }
                callData = iface.encodeFunctionData(fn.name, []);
            } else {
                showStatus("No valid withdraw method selected.", true);
                return;
            }
        }

        showStatus("Sending withdrawal transaction…");
        const tx = await signer.sendTransaction({ to: address, data: callData });
        showStatus("Transaction sent – hash: " + tx.hash);
        await tx.wait();
        showStatus("✅ Withdrawal confirmed: " + tx.hash);
        await refreshAll();
    } catch (err) {
        showStatus("Withdrawal failed: " + (err.reason || err.message), true);
    }
}

// ---------------------------------------------------------------------------
// Event delegation handler for contract card buttons
// ---------------------------------------------------------------------------
function _handleContainerClick(event) {
    const btn = event.target.closest("[data-action]");
    if (!btn) return;
    const card = btn.closest("[data-address]");
    if (!card) return;
    const address = card.dataset.address;
    const action = btn.dataset.action;

    if (action === "remove") {
        removeContract(address);
    } else if (action === "withdraw") {
        const list = loadContracts();
        const entry = list.find(c => c.address.toLowerCase() === address.toLowerCase());
        if (entry) {
            withdrawFromContract(
                entry.address,
                entry.method,
                entry.customSelector || "",
                entry.customAbi || ""
            );
        }
    }
}

// ---------------------------------------------------------------------------
// Render the contract cards
// ---------------------------------------------------------------------------
async function renderContracts() {
    const list = loadContracts();
    const container = document.getElementById("contract-list");
    if (!container) return;

    if (list.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📋</div>
                <div class="empty-state-text">No contracts added yet</div>
                <div class="empty-state-hint">Connect your wallet and add a contract above to get started</div>
            </div>
        `;
        return;
    }

    // Render placeholders first for speed
    container.innerHTML = list.map(c => `
        <article class="contract-card" data-address="${escapeHtml(c.address)}">
            <div class="card-header">
                <div style="flex: 1;">
                    <h3 title="${escapeHtml(c.address)}">${escapeHtml(c.label)}</h3>
                    <code class="addr">${escapeHtml(c.address)}</code>
                </div>
            </div>
            <div class="card-body">
                <div class="balance-row">
                    <span class="label">Balance</span>
                    <span class="balance" id="bal-${escapeHtml(c.address)}">⏳ loading…</span>
                </div>
                <div class="method-row">
                    <span class="muted" style="font-size: 0.8rem; text-transform: uppercase; font-weight: 600;">Method:</span>
                    <span class="pill">${escapeHtml(c.method === "custom" ? (c.customSelector || "custom") : c.method)}</span>
                </div>
                <div class="card-actions">
                    <button class="btn btn-success" data-action="withdraw" title="Withdraw funds">
                        <span>💰</span>
                        <span>Withdraw</span>
                    </button>
                    <button class="btn btn-danger btn-sm" data-action="remove" title="Remove contract">
                        <span>🗑</span>
                    </button>
                </div>
            </div>
        </article>
    `).join("");

    // Fetch balances in parallel
    const balancePromises = list.map(async c => {
        const bal = await fetchBalance(c.address);
        const el = document.getElementById("bal-" + escapeHtml(c.address));
        if (el) el.textContent = bal;
    });
    await Promise.all(balancePromises);
}

async function refreshAll() {
    await renderContracts();
    renderImportedData();
}

// ---------------------------------------------------------------------------
// Toggle custom selector input visibility
// ---------------------------------------------------------------------------
function onMethodChange() {
    const sel = document.getElementById("input-method").value;
    const customRow = document.getElementById("custom-selector-row");
    if (customRow) {
        if (sel === "custom") {
            customRow.style.display = "flex";
            customRow.classList.add("visible");
        } else {
            customRow.style.display = "none";
            customRow.classList.remove("visible");
        }
    }
}

function normalizeImportedBalance(entry) {
    const symbol = entry.symbol || (String(entry.address || "").toLowerCase() === "native" ? "NATIVE" : "TOKEN");
    const valueUsd = Number(entry.value_usd);
    const priceUsd = Number(entry.price_usd);
    const offRamp = classifyOffRamp(entry);

    return {
        chain: entry.chain || "unknown",
        chainId: entry.chain_id || null,
        address: entry.address || "",
        symbol,
        name: entry.name || symbol,
        decimals: Number.isFinite(Number(entry.decimals)) ? Number(entry.decimals) : 18,
        rawAmount: String(entry.amount || "0"),
        displayAmount: formatTokenAmount(entry.amount || "0", entry.decimals),
        priceUsd: Number.isFinite(priceUsd) ? priceUsd : null,
        valueUsd: Number.isFinite(valueUsd) ? valueUsd : null,
        poolSize: Number.isFinite(Number(entry.pool_size)) ? Number(entry.pool_size) : null,
        lowLiquidity: Boolean(entry.low_liquidity),
        offRamp
    };
}

function normalizeImportedTransaction(entry) {
    const time = entry.block_time || entry.timestamp || "";
    const amount = entry.value ? parseHexAmount(entry.value) : parseDecimalAmount(entry.amount || "0", entry.decimals || 18);
    const nativeTransfer = isNativeTransfer(entry);

    return {
        chain: entry.chain || "unknown",
        chainId: entry.chain_id || null,
        hash: entry.hash || "",
        timestamp: time,
        transactionType: entry.transaction_type || "Unknown",
        from: entry.from || "",
        to: entry.to || "",
        amount,
        amountLabel: amount ? `${amount.toLocaleString(undefined, { maximumFractionDigits: 6 })} ${nativeTransfer ? "ETH" : (entry.symbol || "units")}` : "—",
        assetLabel: entry.symbol || (nativeTransfer ? "Native" : "Token"),
        success: entry.success !== false
    };
}

function normalizeImportedCollectible(entry) {
    const balance = Number(entry.balance);
    const offRamp = classifyOffRamp({
        chain: entry.chain,
        chain_id: entry.chain_id,
        symbol: entry.symbol,
        asset_type: "collectible",
        token_standard: entry.token_standard,
        is_spam: entry.is_spam
    });

    return {
        chain: entry.chain || "unknown",
        chainId: entry.chain_id || null,
        contractAddress: entry.contract_address || "",
        tokenId: String(entry.token_id || ""),
        tokenStandard: entry.token_standard || "Collectible",
        name: entry.name || entry.symbol || "Collectible",
        symbol: entry.symbol || "NFT",
        balance: Number.isFinite(balance) ? balance : 0,
        imageUrl: entry.image_url || "",
        description: entry.description || "",
        isSpam: Boolean(entry.is_spam),
        lastAcquired: entry.last_acquired || "",
        offRamp
    };
}

function isNativeTransfer(entry) {
    return Boolean(
        entry &&
        entry.value &&
        entry.data === "0x" &&
        Array.isArray(entry.logs) &&
        entry.logs.length === 0
    );
}

function isDuneCollectiblesPayload(payload) {
    return Boolean(
        payload &&
        typeof payload === "object" &&
        Array.isArray(payload.entries) &&
        !Array.isArray(payload.balances) &&
        !Array.isArray(payload.transactions)
    );
}

function parseImportedPayload(rawText) {
    let payload;
    try {
        payload = JSON.parse(rawText);
    } catch (_) {
        throw new Error("Invalid JSON format.");
    }
    if (!payload || typeof payload !== "object") {
        throw new Error("JSON import must contain an object.");
    }

    const balances = Array.isArray(payload.balances)
        ? payload.balances.map(normalizeImportedBalance)
        : [];
    const transactions = Array.isArray(payload.transactions)
        ? payload.transactions.map(normalizeImportedTransaction)
        : [];
    const collectibles = isDuneCollectiblesPayload(payload)
        ? payload.entries.map(normalizeImportedCollectible)
        : (Array.isArray(payload.collectibles) ? payload.collectibles.map(normalizeImportedCollectible) : []);

    if (balances.length === 0 && transactions.length === 0 && collectibles.length === 0) {
        throw new Error("JSON must include a balances array, a transactions array, or a collectibles entries array.");
    }

    return {
        walletAddress: payload.wallet_address || payload.address || "",
        requestTime: payload.request_time || "",
        responseTime: payload.response_time || "",
        nextOffset: payload.next_offset || "",
        source: isDuneCollectiblesPayload(payload) ? "dune-collectibles" : "wallet-json",
        balances,
        collectibles,
        transactions,
        importedAt: new Date().toISOString()
    };
}

function summarizeImportedCollectibles(collectibles) {
    return (collectibles || []).reduce((summary, collectible) => {
        const chain = String(collectible.chain || "unknown").toLowerCase();
        summary.totalCount += 1;
        if (!summary.chains[chain]) {
            summary.chains[chain] = 0;
        }
        summary.chains[chain] += 1;
        if (chain === "base") {
            summary.baseCount += 1;
        }
        if (collectible.isSpam) {
            summary.spamCount += 1;
        }
        return summary;
    }, {
        totalCount: 0,
        baseCount: 0,
        spamCount: 0,
        chains: {}
    });
}

function buildSummaryCards(summary, imported, collectibleSummary) {
    const cards = [
        {
            label: "Priced portfolio",
            value: formatUsd(summary.totalValueUsd),
            note: `${imported.balances.length} assets across ${Object.keys(summary.chains).length} chains`
        },
        {
            label: "Ready to off-ramp",
            value: formatUsd(summary.readyValueUsd),
            note: "Native assets and common cash-out pairs"
        },
        {
            label: "Swap before fiat",
            value: formatUsd(summary.swapValueUsd),
            note: "Likely route through ETH, USDC, or another liquid pair"
        },
        {
            label: "Manual review / blocked",
            value: formatUsd(summary.reviewValueUsd + summary.blockedValueUsd),
            note: `${summary.lowLiquidityCount} low-liquidity assets, ${summary.unpricedAssetCount} unpriced`
        }
    ];

    if (collectibleSummary.totalCount > 0) {
        cards.push({
            label: "Collectibles / NFTs",
            value: collectibleSummary.totalCount.toLocaleString(),
            note: `${collectibleSummary.baseCount} on Base, ${collectibleSummary.spamCount} flagged as spam`
        });
    }

    return cards;
}

function renderImportedBalances(imported) {
    const container = document.getElementById("import-balance-table");
    const empty = document.getElementById("import-balance-empty");
    const count = document.getElementById("import-balance-count");
    if (!container || !empty || !count) return;

    if (!imported || imported.balances.length === 0) {
        container.innerHTML = "";
        empty.style.display = "block";
        count.textContent = "0 assets";
        return;
    }

    const topBalances = [...imported.balances]
        .sort((left, right) => (right.valueUsd || 0) - (left.valueUsd || 0))
        .slice(0, MAX_DISPLAYED_BALANCES);

    count.textContent = `${imported.balances.length} assets`;
    empty.style.display = "none";
    container.innerHTML = topBalances.map(balance => `
        <tr>
            <td>${escapeHtml(balance.chain)}</td>
            <td>
                <div><strong>${escapeHtml(balance.symbol)}</strong></div>
                <div class="table-subtext">${escapeHtml(balance.name)}</div>
            </td>
            <td>${escapeHtml(balance.displayAmount)}</td>
            <td>${escapeHtml(formatUsd(balance.valueUsd))}</td>
            <td>${escapeHtml(balance.lowLiquidity ? "Low liquidity" : (balance.poolSize ? `Pool ${formatUsd(balance.poolSize)}` : "No pool data"))}</td>
            <td><span class="status-chip status-${escapeHtml(balance.offRamp.status)}">${escapeHtml(balance.offRamp.label)}</span></td>
        </tr>
    `).join("");
}

function renderImportedCollectibles(imported) {
    const container = document.getElementById("import-collectible-table");
    const empty = document.getElementById("import-collectible-empty");
    const count = document.getElementById("import-collectible-count");
    const importedCollectibles = Array.isArray(imported && imported.collectibles) ? imported.collectibles : [];
    if (!container || !empty || !count) return;

    if (!imported || importedCollectibles.length === 0) {
        container.innerHTML = "";
        empty.style.display = "block";
        count.textContent = "0 collectibles";
        return;
    }

    const collectibles = [...importedCollectibles]
        .sort((left, right) => String(right.lastAcquired).localeCompare(String(left.lastAcquired)))
        .slice(0, MAX_DISPLAYED_COLLECTIBLES);

    count.textContent = `${importedCollectibles.length} collectibles`;
    empty.style.display = "none";
    container.innerHTML = collectibles.map(collectible => `
        <tr>
            <td>${escapeHtml(collectible.chain)}</td>
            <td>
                <div><strong>${escapeHtml(collectible.name)}</strong></div>
                <div class="table-subtext">${escapeHtml(`${collectible.tokenStandard} #${collectible.tokenId || "—"}`)}</div>
            </td>
            <td>${escapeHtml(collectible.balance ? String(collectible.balance) : "1")}</td>
            <td>${escapeHtml(collectible.offRamp.settlement.network)}</td>
            <td>${escapeHtml(collectible.offRamp.settlement.destination)}</td>
            <td><span class="status-chip status-${escapeHtml(collectible.offRamp.status)}">${escapeHtml(collectible.offRamp.label)}</span></td>
        </tr>
    `).join("");
}

function renderImportedTransactions(imported) {
    const container = document.getElementById("import-transaction-table");
    const empty = document.getElementById("import-transaction-empty");
    const count = document.getElementById("import-transaction-count");
    if (!container || !empty || !count) return;

    if (!imported || imported.transactions.length === 0) {
        container.innerHTML = "";
        empty.style.display = "block";
        count.textContent = "0 transactions";
        return;
    }

    const recentTransactions = [...imported.transactions]
        .sort((left, right) => String(right.timestamp).localeCompare(String(left.timestamp)))
        .slice(0, MAX_DISPLAYED_TRANSACTIONS);

    count.textContent = `${imported.transactions.length} transactions`;
    empty.style.display = "none";
    container.innerHTML = recentTransactions.map(tx => `
        <tr>
            <td>${escapeHtml(tx.chain)}</td>
            <td>${escapeHtml(tx.assetLabel)}</td>
            <td>${escapeHtml(tx.amountLabel)}</td>
            <td>${escapeHtml(tx.transactionType)}</td>
            <td class="table-subtext">${escapeHtml(tx.timestamp || "—")}</td>
            <td class="table-subtext">${escapeHtml(shortAddr(tx.from || "—"))} → ${escapeHtml(shortAddr(tx.to || "—"))}</td>
            <td>
                <span class="status-chip status-${tx.success ? "ready" : "blocked"}">
                    ${tx.success ? "Confirmed" : "Failed"}
                </span>
            </td>
        </tr>
    `).join("");
}

function renderImportedData() {
    const imported = loadImportedData();
    const summaryEl = document.getElementById("import-summary");
    const alertEl = document.getElementById("import-alerts");
    const metaEl = document.getElementById("import-meta");
    const walletEl = document.getElementById("import-wallet-address");
    const destinationEl = document.getElementById("settlement-destination-display");

    if (!summaryEl || !alertEl || !metaEl || !walletEl || !destinationEl) return;

    destinationEl.textContent = getSettlementDestinationLabel();

    if (!imported) {
        summaryEl.innerHTML = `
            <div class="empty-state compact">
                <div class="empty-state-text">No wallet JSON imported yet</div>
                <div class="empty-state-hint">Paste or upload a balances, transactions, or collectibles payload to build a local settlement view.</div>
            </div>
        `;
        alertEl.innerHTML = "";
        metaEl.textContent = "Local-only import storage is empty.";
        walletEl.textContent = "No wallet loaded";
        renderImportedBalances({ balances: [], collectibles: [], transactions: [] });
        renderImportedCollectibles({ balances: [], collectibles: [], transactions: [] });
        renderImportedTransactions({ balances: [], collectibles: [], transactions: [] });
        return;
    }

    const summary = summarizeImportedBalances(imported.balances);
    const collectibleSummary = summarizeImportedCollectibles(imported.collectibles);
    const cards = buildSummaryCards(summary, imported, collectibleSummary);
    const alerts = [];

    if (summary.blockedValueUsd > 0) {
        alerts.push("Testnet balances are blocked from fiat redemption and must stay off-ramp excluded.");
    }
    if (summary.lowLiquidityCount > 0) {
        alerts.push(`${summary.lowLiquidityCount} assets are flagged as low liquidity and should be reviewed before any swap.`);
    }
    if (summary.unpricedAssetCount > 0) {
        alerts.push(`${summary.unpricedAssetCount} assets have no USD price and cannot be included in a fiat estimate.`);
    }
    if (summary.baseReadyCount > 0) {
        alerts.push(`${summary.baseReadyCount} fungible assets are already on Base and can use a Base-compatible Coinbase deposit route after verification.`);
    }
    if (collectibleSummary.totalCount > 0) {
        alerts.push(`${collectibleSummary.totalCount} collectibles were imported. NFTs are excluded from fiat estimates and require manual Coinbase/Base destination review.`);
    }
    if (collectibleSummary.baseCount > 0) {
        alerts.push(`${collectibleSummary.baseCount} collectibles are on Base. Verify Base wallet and NFT deposit support before sending any collection item.`);
    }
    if (collectibleSummary.spamCount > 0) {
        alerts.push(`${collectibleSummary.spamCount} collectibles are flagged as spam and should be ignored for settlement planning.`);
    }
    if (imported.transactions.length > 0) {
        alerts.push("Transaction history is informational only; settlement and fiat routing remain off-chain.");
    }
    alerts.push(`Configured settlement destination: ${getSettlementDestinationLabel()}`);

    walletEl.textContent = imported.walletAddress || "Wallet address unavailable";
    metaEl.textContent = [
        imported.source === "dune-collectibles" ? "Source Dune SIM collectibles" : "",
        imported.requestTime ? `Requested ${imported.requestTime}` : "",
        imported.responseTime ? `Responded ${imported.responseTime}` : "",
        imported.nextOffset ? `Next offset ${imported.nextOffset}` : ""
    ].filter(Boolean).join(" • ") || "Imported locally";

    summaryEl.innerHTML = cards.map(card => `
        <article class="summary-card">
            <div class="summary-label">${escapeHtml(card.label)}</div>
            <div class="summary-value">${escapeHtml(card.value)}</div>
            <div class="summary-note">${escapeHtml(card.note)}</div>
        </article>
    `).join("");

    alertEl.innerHTML = alerts.map(alert => `
        <div class="import-alert">${escapeHtml(alert)}</div>
    `).join("");

    renderImportedBalances(imported);
    renderImportedCollectibles(imported);
    renderImportedTransactions(imported);
}

function importJsonFromText(rawText) {
    const parsed = parseImportedPayload(rawText);
    saveImportedData(parsed);
    renderImportedData();
    showStatus("✓ Wallet JSON imported locally.");
}

function handleJsonImport(event) {
    event.preventDefault();
    const input = document.getElementById("json-import-input");
    if (!input || !input.value.trim()) {
        showStatus("Paste a balances or transactions JSON payload first.", true);
        return;
    }

    try {
        importJsonFromText(input.value.trim());
    } catch (err) {
        showStatus(err instanceof SyntaxError ? "JSON import failed: Invalid JSON format." : `JSON import failed: ${err.message}`, true);
    }
}

async function handleJsonFileImport(event) {
    const [file] = Array.from(event.target.files || []);
    if (!file) return;
    try {
        importJsonFromText(await file.text());
        const input = document.getElementById("json-import-input");
        if (input) input.value = "";
    } catch (err) {
        showStatus(err instanceof SyntaxError ? "JSON file import failed: Invalid JSON format." : `JSON file import failed: ${err.message}`, true);
    } finally {
        event.target.value = "";
    }
}

function clearJsonImportView() {
    clearImportedData();
    const input = document.getElementById("json-import-input");
    if (input) input.value = "";
    renderImportedData();
    showStatus("Imported wallet JSON cleared.");
}

function saveSettlementDestinationFromInput() {
    const input = document.getElementById("settlement-destination");
    if (!input) return;
    const address = input.value.trim();
    if (typeof ethers === "undefined" || !ethers.utils.isAddress(address)) {
        showStatus("Settlement destination must be a valid EVM address.", true);
        return;
    }
    saveSettlementDestination(address);
    renderImportedData();
    showStatus(`✓ Settlement destination saved: ${shortAddr(address)}`);
}

// ---------------------------------------------------------------------------
// Boot
// ---------------------------------------------------------------------------
function initWithdrawDashboard() {
    const form = document.getElementById("add-contract-form");
    if (form) form.addEventListener("submit", addContract);

    const methodSel = document.getElementById("input-method");
    if (methodSel) methodSel.addEventListener("change", onMethodChange);

    const connectBtn = document.getElementById("connect-btn");
    if (connectBtn) connectBtn.addEventListener("click", connectWallet);

    const importBtn = document.getElementById("import-json-btn");
    if (importBtn) importBtn.addEventListener("click", handleJsonImport);

    const clearImportBtn = document.getElementById("clear-json-btn");
    if (clearImportBtn) clearImportBtn.addEventListener("click", clearJsonImportView);

    const importFile = document.getElementById("json-import-file");
    if (importFile) importFile.addEventListener("change", handleJsonFileImport);

    const destinationInput = document.getElementById("settlement-destination");
    if (destinationInput) {
        destinationInput.value = loadSettlementDestination();
    }

    const destinationBtn = document.getElementById("save-settlement-destination");
    if (destinationBtn) destinationBtn.addEventListener("click", saveSettlementDestinationFromInput);

    // Single delegation listener for all contract card buttons
    const contractList = document.getElementById("contract-list");
    if (contractList) contractList.addEventListener("click", _handleContainerClick);

    refreshAll();
}

if (typeof window !== "undefined") {
    window.NexusWithdraw = {
        PROXY_ABI,
        WITHDRAW_METHODS,
        connectWallet,
        addContract,
        removeContract,
        withdrawFromContract,
        refreshAll,
        parseImportedPayload,
        renderImportedData,
        clearJsonImportView,
        normalizeImportedCollectible,
    };

    if (typeof document !== "undefined") {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", initWithdrawDashboard);
        } else {
            initWithdrawDashboard();
        }
    }
}

if (typeof module !== "undefined" && module.exports) {
    module.exports = {
        formatTokenAmount,
        getSettlementDestination,
        getSettlementDestinationLabel,
        parseImportedPayload,
        isNativeTransfer,
        normalizeImportedBalance,
        normalizeImportedCollectible,
        normalizeImportedTransaction,
    };
}
