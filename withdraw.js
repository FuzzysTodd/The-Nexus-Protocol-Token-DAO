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

function showStatus(msg, isError) {
    const el = document.getElementById("status-bar");
    if (!el) return;
    el.textContent = msg;
    el.className = "status-bar " + (isError ? "status-error" : "status-ok");
    el.style.display = "block";
    clearTimeout(el._timer);
    el._timer = setTimeout(() => { el.style.display = "none"; }, 6000);
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
        provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        signer = provider.getSigner();
        signerAddress = await signer.getAddress();
        document.getElementById("wallet-address").textContent = signerAddress;
        document.getElementById("wallet-section").classList.add("connected");
        document.getElementById("connect-btn").textContent = "✔ Connected";
        document.getElementById("connect-btn").disabled = true;
        document.getElementById("add-contract-form").style.display = "block";
        showStatus("Wallet connected: " + signerAddress);
        await refreshAll();
    } catch (err) {
        showStatus("Wallet connection failed: " + err.message, true);
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
        showStatus("Invalid Ethereum address.", true);
        return;
    }

    const list = loadContracts();
    if (list.find(c => c.address.toLowerCase() === addr.toLowerCase())) {
        showStatus("Contract already in the list.", true);
        return;
    }

    list.push({ address: addr, label, customAbi, method, customSelector });
    saveContracts(list);
    document.getElementById("input-address").value = "";
    document.getElementById("input-label").value = "";
    document.getElementById("input-custom-abi").value = "";
    document.getElementById("input-custom-selector").value = "";
    renderContracts();
    showStatus("Contract added: " + label);
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
            // release(address) needs a payee argument – use the connected wallet
            const iface = new ethers.utils.Interface([
                "function release(address payee)"
            ]);
            callData = iface.encodeFunctionData("release", [signerAddress]);
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
        container.innerHTML = '<p class="empty-state">No contracts added yet.</p>';
        return;
    }

    // Render placeholders first for speed
    container.innerHTML = list.map(c => `
        <article class="card contract-card" data-address="${escapeHtml(c.address)}">
            <div class="card-header">
                <div>
                    <h3 title="${escapeHtml(c.address)}">${escapeHtml(c.label)}</h3>
                    <code class="addr">${escapeHtml(c.address)}</code>
                </div>
                <button class="btn btn-danger btn-sm" data-action="remove">✕ Remove</button>
            </div>
            <div class="card-body">
                <div class="balance-row">
                    <span class="muted">Balance:</span>
                    <span class="balance" id="bal-${escapeHtml(c.address)}">loading…</span>
                </div>
                <div class="method-row">
                    <span class="pill">${escapeHtml(c.method === "custom" ? (c.customSelector || "custom") : c.method)}</span>
                </div>
                <button class="btn btn-accent" data-action="withdraw">
                    ⬇ Withdraw
                </button>
            </div>
        </article>
    `).join("");

    // Attach event listeners via delegation (avoids inline JS injection risk)
    // Note: the listener is attached once in initWithdrawDashboard; do not
    // re-attach here to avoid duplicate handlers.

    // Async balance updates
    for (const c of list) {
        const el = document.getElementById("bal-" + escapeHtml(c.address));
        if (el) {
            fetchBalance(c.address).then(bal => { el.textContent = bal; });
        }
    }
}

async function refreshAll() {
    await renderContracts();
}

// ---------------------------------------------------------------------------
// Toggle custom selector input visibility
// ---------------------------------------------------------------------------
function onMethodChange() {
    const sel = document.getElementById("input-method").value;
    const customRow = document.getElementById("custom-selector-row");
    if (customRow) customRow.style.display = (sel === "custom") ? "block" : "none";
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

    // Single delegation listener for all contract card buttons
    const contractList = document.getElementById("contract-list");
    if (contractList) contractList.addEventListener("click", _handleContainerClick);

    renderContracts();
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
    };

    if (typeof document !== "undefined") {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", initWithdrawDashboard);
        } else {
            initWithdrawDashboard();
        }
    }
}
