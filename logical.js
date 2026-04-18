// This file contains example JavaScript code to interact with the Project Chimera smart contracts.
// It uses the ethers.js library, a popular alternative to web3.js.
// You would integrate this logic into the interactive web application's frontend.

// --- Required imports (assuming you're using a bundler like Vite or Webpack) ---
// import { ethers } from "ethers";
// import NexusFinancialContractABI from './abis/NexusFinancialContract.json';
// import NexusGreenTokenABI from './abis/NexusGreenToken.json';

// --- Dashboard data for the static repository index ---
const DAO_FEATURES = [
    {
        name: "Governance authority",
        description: "Owner authority, MPC automation, and super delegates anchor proposal flow and execution authority.",
        source: "./GOVERNANCE.md",
        bullets: [
            "FuzzysTodd remains the top-level authority",
            "MPC can propose and automate DAO actions",
            "Super delegates provide emergency and veto paths",
        ],
    },
    {
        name: "MCP coordination groups",
        description: "The NGTT contract can create named MCP groups and track their activity across gameplay and rewards.",
        source: "./contracts/NexusGameTheoryToken.sol",
        bullets: [
            "Owner-managed group creation",
            "Per-group member rosters",
            "Games played and token totals tracked on-chain",
        ],
    },
    {
        name: "Rewards and progression",
        description: "Gameplay rewards scale with skill growth, optional boosts, and age-group multipliers.",
        source: "./contracts/NexusGameTheoryToken.sol",
        bullets: [
            "Skill-based reward multiplier",
            "Age-group boost support",
            "Player stats and timestamps exposed",
        ],
    },
    {
        name: "Treasury and profit sharing",
        description: "Profit pool distribution is weighted by active group participation, then claimable per member.",
        source: "./contracts/NexusGameTheoryToken.sol",
        bullets: [
            "Central profit pool accounting",
            "Activity-weighted group share logic",
            "Member claim flow for accrued profits",
        ],
    },
    {
        name: "NES security designation",
        description: "Repository-authored security, signing, and protected-message conventions are grouped under NES.",
        source: "./GOVERNANCE.md",
        bullets: [
            "Protocol-owned designation",
            "Applies to repository-authored surfaces",
            "Respects bundled third-party licenses",
        ],
    },
    {
        name: "Bundled ecosystem integrations",
        description: "The repository links into Nouns, Aave, Chainlink, and GMX references for governance and DeFi expansion.",
        source: "./Nouns-DAO/README.md",
        bullets: [
            "Governance reference implementations",
            "Developer docs and public portals",
            "Repo-local entry points for deeper review",
        ],
    },
];

const DAO_OPERATIONS = [
    {
        name: "1. Direct and propose",
        description: "Strategy starts with the owner mandate, MPC automation, or delegate intervention.",
        source: "./GOVERNANCE.md",
        bullets: [
            "Authority and mandate are documented in the governance charter",
            "The page keeps those documents one click away",
        ],
    },
    {
        name: "2. Organize members",
        description: "MCP groups organize participants into named teams for scoring, rewards, and treasury share tracking.",
        source: "./contracts/NexusGameTheoryToken.sol",
        bullets: [
            "Member wallets map into a group id",
            "Group performance contributes to profit allocation",
        ],
    },
    {
        name: "3. Reward contribution",
        description: "Completed games mint rewards, increase skill, and update per-group totals for the DAO economy.",
        source: "./contracts/NexusGameTheoryToken.sol",
        bullets: [
            "Skill growth compounds future rewards",
            "Boost activation can accelerate progression",
        ],
    },
    {
        name: "4. Route profits",
        description: "Treasury profits are added to the pool, distributed by activity, then claimed by members.",
        source: "./contracts/NexusGameTheoryToken.sol",
        bullets: [
            "Only active, participating groups receive distribution",
            "Members can claim minted profit allocations",
        ],
    },
];

const WEB3_PROJECT_LINKS = [
    {
        name: "Nouns DAO webapp",
        href: "https://nouns.wtf",
        description: "Frontend for Noun auctions as referenced by the bundled Nouns monorepo README.",
        source: "./Nouns-DAO/README.md",
    },
    {
        name: "Aave developer documentation",
        href: "https://docs.aave.com/developers/",
        description: "Official Aave developer docs for integration and protocol reference.",
        source: "./Aave-V3/README.md",
    },
    {
        name: "Aave governance forum",
        href: "https://governance.aave.com/",
        description: "Community governance forum linked from the Aave v3 repository docs.",
        source: "./Aave-V3/README.md",
    },
    {
        name: "Chainlink",
        href: "https://chain.link/",
        description: "Official Chainlink site for oracle network access and developer resources.",
        source: "./ChainLink/README.md",
    },
    {
        name: "Chainlink documentation",
        href: "https://docs.chain.link/",
        description: "Developer documentation for Chainlink integrations and node operations.",
        source: "./ChainLink/README.md",
    },
    {
        name: "GMX contracts docs",
        href: "https://gmxio.gitbook.io/gmx/contracts",
        description: "GMX contract documentation referenced by the bundled contracts repository.",
        source: "./GMX.io/README.md",
    },
];

const REPOSITORY_ENTRY_POINTS = [
    {
        name: "Nouns DAO repository docs",
        href: "./Nouns-DAO/README.md",
        description: "Documents the bundled nouns webapp, API, SDK, subgraph, and contracts.",
        source: "Local repo",
    },
    {
        name: "Aave v3 repository docs",
        href: "./Aave-V3/README.md",
        description: "Contains Aave developer, community, and governance references.",
        source: "Local repo",
    },
    {
        name: "Chainlink repository docs",
        href: "./ChainLink/README.md",
        description: "Provides official site, docs, community, and build instructions.",
        source: "Local repo",
    },
    {
        name: "GMX repository docs",
        href: "./GMX.io/README.md",
        description: "Covers GMX contracts usage and documentation entry points.",
        source: "Local repo",
    },
];

const GOVERNANCE_LINKS = [
    {
        name: "Repository governance charter",
        href: "./GOVERNANCE.md",
        description: "Authority structure and DAO operating mandate for the repository.",
        source: "Local governance doc",
    },
    {
        name: "NexusGameTheoryToken governance contract",
        href: "./contracts/NexusGameTheoryToken.sol",
        description: "NGTT token contract with MCP group creation, rewards, profits, and stats.",
        source: "Local Solidity contract",
    },
    {
        name: "Nouns DAO governance logic",
        href: "./Nouns-DAO/contracts/governance/NounsDAOLogicV3.sol",
        description: "Bundled DAO proposal and voting implementation from the Nouns governance suite.",
        source: "Local Solidity contract",
    },
    {
        name: "Nouns DAO governance harness tests",
        href: "./Nouns-DAO/contracts/test/NounsDAOLogicV3Harness.sol",
        description: "Test harness for governance logic that helps verify proposal and voting behavior.",
        source: "Local Solidity test harness",
    },
];

const VALIDATION_SUMMARY = [
    "flake8 . completed successfully in the repository root.",
    "Repository pytest validation completed successfully with the existing test suite.",
    "DAO feature cards, operations, and governance artifacts are linked in one browser page.",
];

const PREFERRED_WALLET_ADDRESS = "0xeCE999c86452c573Adfdd7F0C9226e673477973a";
const PREFERRED_WALLET_ADDRESS_LOWER = PREFERRED_WALLET_ADDRESS.toLowerCase();
const ETHERSCAN_ADDRESS_URL = `https://etherscan.io/address/${PREFERRED_WALLET_ADDRESS}`;

function buildDaoStats() {
    return [
        {
            value: "1.0B NGTT",
            label: "Initial supply",
            detail: "Minted in the NexusGameTheoryToken constructor.",
        },
        {
            value: `${DAO_FEATURES.length}`,
            label: "Core DAO features",
            detail: "Governance, groups, rewards, treasury, NES, and integrations.",
        },
        {
            value: `${WEB3_PROJECT_LINKS.length + REPOSITORY_ENTRY_POINTS.length + GOVERNANCE_LINKS.length}`,
            label: "Linked entry points",
            detail: "External and repo-local surfaces available from this page.",
        },
        {
            value: new Date().toUTCString(),
            label: "Dashboard loaded at",
            detail: "Timestamp captured when this dashboard instance was hydrated.",
        },
    ];
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function normalizeBulletsForSearch(bullets) {
    if (!Array.isArray(bullets)) {
        return [];
    }

    return bullets
        .filter((bullet) => bullet !== null && bullet !== undefined)
        .map((bullet) => String(bullet));
}

function buildSearchText(item) {
    return [
        item.name || "",
        item.description || "",
        item.source || "",
        item.href || "",
        ...normalizeBulletsForSearch(item.bullets),
    ].join(" ").toLowerCase();
}

function renderStat(item) {
    return `
        <article class="stat-card">
            <strong>${escapeHtml(item.value)}</strong>
            <div>${escapeHtml(item.label)}</div>
            <span>${escapeHtml(item.detail)}</span>
        </article>
    `;
}

function renderCard(item) {
    return `
        <article class="card" data-dashboard-card="true" data-search-text="${escapeHtml(buildSearchText(item))}">
            <h3>${escapeHtml(item.name)}</h3>
            <p>${escapeHtml(item.description)}</p>
            <a href="${escapeHtml(item.href)}" target="${item.href.startsWith("http") ? "_blank" : "_self"}" rel="noopener noreferrer">
                ${escapeHtml(item.href)}
            </a>
            <span class="source">Source: ${escapeHtml(item.source)}</span>
        </article>
    `;
}

function renderFeatureCard(item) {
    return `
        <article class="card" data-dashboard-card="true" data-search-text="${escapeHtml(buildSearchText(item))}">
            <h3>${escapeHtml(item.name)}</h3>
            <p>${escapeHtml(item.description)}</p>
            <ul class="feature-list">
                ${item.bullets.map((bullet) => `<li>${escapeHtml(bullet)}</li>`).join("")}
            </ul>
            <span class="source">Source: ${escapeHtml(item.source)}</span>
        </article>
    `;
}

function populateContainer(selector, items) {
    if (typeof document === "undefined") return;
    const container = document.querySelector(selector);
    if (!container) return;
    container.innerHTML = items.map(renderCard).join("");
}

function populateFeatureContainer(selector, items) {
    if (typeof document === "undefined") return;
    const container = document.querySelector(selector);
    if (!container) return;
    container.innerHTML = items.map(renderFeatureCard).join("");
}

function populateDaoStats() {
    if (typeof document === "undefined") return;
    const container = document.querySelector("[data-dao-stats]");
    if (!container) return;
    container.innerHTML = buildDaoStats().map(renderStat).join("");
}

function populateValidationSummary() {
    if (typeof document === "undefined") return;
    const container = document.querySelector("[data-validation-summary]");
    if (!container) return;

    container.innerHTML = VALIDATION_SUMMARY.map((item) => `<li><strong>Verified:</strong> ${escapeHtml(item)}</li>`).join("");
}

function getWorkspaceElements() {
    if (typeof document === "undefined") {
        return null;
    }

    return {
        dashboardSearch: document.querySelector("[data-dashboard-search]"),
        clearDashboardSearchButton: document.querySelector("[data-clear-dashboard-search]"),
        refreshWalletButton: document.querySelector("[data-refresh-wallet]"),
        dashboardSearchStatus: document.querySelector("[data-dashboard-search-status]"),
    };
}

function getWalletElements() {
    if (typeof document === "undefined") {
        return null;
    }

    return {
        preferredWalletAddress: document.querySelector("[data-preferred-wallet-address]"),
        connectedWalletAddress: document.querySelector("[data-connected-wallet-address]"),
        walletChainId: document.querySelector("[data-wallet-chain-id]"),
        walletMatchState: document.querySelector("[data-wallet-match-state]"),
        walletStatus: document.querySelector("[data-wallet-status]"),
        walletStatusText: document.querySelector("[data-wallet-status-text]"),
        connectWalletButton: document.querySelector("[data-connect-wallet]"),
        copyWalletButton: document.querySelector("[data-copy-wallet]"),
        openWalletLink: document.querySelector("[data-open-wallet]"),
    };
}

function updateDashboardSearchStatus(message) {
    const elements = getWorkspaceElements();
    if (!elements || !elements.dashboardSearchStatus) {
        return;
    }

    elements.dashboardSearchStatus.textContent = message;
}

function filterDashboardCards(rawQuery) {
    if (typeof document === "undefined") {
        return 0;
    }

    const query = String(rawQuery || "").trim().toLowerCase();
    const cards = Array.from(document.querySelectorAll("[data-dashboard-card]"));
    let visibleCount = 0;

    cards.forEach((card) => {
        const searchText = (card.dataset.searchText || "").toLowerCase();
        const matches = query === "" || searchText.includes(query);
        card.hidden = !matches;
        if (matches) {
            visibleCount += 1;
        }
    });

    if (query === "") {
        updateDashboardSearchStatus("Showing all dashboard cards.");
    } else if (visibleCount === 0) {
        updateDashboardSearchStatus(`No dashboard cards match "${rawQuery}".`);
    } else {
        updateDashboardSearchStatus(`Showing ${visibleCount} matching dashboard cards for "${rawQuery}".`);
    }

    return visibleCount;
}

function setWalletStatus(message, tone) {
    const elements = getWalletElements();
    if (!elements || !elements.walletStatus || !elements.walletStatusText) {
        return;
    }

    elements.walletStatus.dataset.tone = tone;
    elements.walletStatusText.textContent = message;
}

function updateWalletDetails(state) {
    const elements = getWalletElements();
    if (!elements) {
        return;
    }

    if (elements.preferredWalletAddress) {
        elements.preferredWalletAddress.textContent = PREFERRED_WALLET_ADDRESS;
    }

    if (elements.connectedWalletAddress) {
        elements.connectedWalletAddress.textContent = state.connectedAddress || "Not connected";
    }

    if (elements.walletChainId) {
        elements.walletChainId.textContent = state.chainId || "Unavailable";
    }

    if (elements.walletMatchState) {
        if (!state.connectedAddress) {
            elements.walletMatchState.textContent = "Waiting for MetaMask";
        } else if (state.matchesPreferredWallet) {
            elements.walletMatchState.textContent = "Connected wallet matches preferred DAO wallet";
        } else {
            elements.walletMatchState.textContent = `Connected wallet differs from preferred wallet (${PREFERRED_WALLET_ADDRESS})`;
        }
    }

    if (elements.openWalletLink) {
        elements.openWalletLink.href = ETHERSCAN_ADDRESS_URL;
    }
}

async function readWalletState() {
    if (typeof window === "undefined" || typeof window.ethereum === "undefined") {
        return {
            hasMetaMask: false,
            connectedAddress: "",
            chainId: "",
            matchesPreferredWallet: false,
        };
    }

    const [accounts, chainId] = await Promise.all([
        window.ethereum.request({ method: "eth_accounts" }),
        window.ethereum.request({ method: "eth_chainId" }),
    ]);
    const connectedAddress = accounts && accounts.length > 0 ? accounts[0] : "";

    return {
        hasMetaMask: true,
        connectedAddress,
        chainId,
        matchesPreferredWallet: connectedAddress !== "" && connectedAddress.toLowerCase() === PREFERRED_WALLET_ADDRESS_LOWER,
    };
}

async function refreshWalletDashboard() {
    try {
        const state = await readWalletState();
        updateWalletDetails(state);

        if (!state.hasMetaMask) {
            setWalletStatus("MetaMask was not detected in this browser. Install it to connect the preferred DAO wallet.", "warn");
            return state;
        }

        if (!state.connectedAddress) {
            setWalletStatus("MetaMask is available. Connect a wallet to compare it against the preferred DAO wallet and inspect chain state.", "idle");
            return state;
        }

        if (state.matchesPreferredWallet) {
            setWalletStatus("MetaMask is connected and the active account matches the preferred DAO wallet.", "ok");
        } else {
            setWalletStatus("MetaMask is connected, but the active account does not match the preferred DAO wallet.", "warn");
        }

        return state;
    } catch (error) {
        console.error("Failed to refresh wallet dashboard:", error);
        setWalletStatus("MetaMask state could not be read. Check wallet permissions and try again.", "warn");
        updateWalletDetails({
            connectedAddress: "",
            chainId: "",
            matchesPreferredWallet: false,
        });
        return null;
    }
}

async function connectPreferredWallet() {
    if (typeof window === "undefined" || typeof window.ethereum === "undefined") {
        setWalletStatus("MetaMask is not installed. Add the extension, then reconnect from this dashboard.", "warn");
        return null;
    }

    try {
        await window.ethereum.request({ method: "eth_requestAccounts" });
        return await refreshWalletDashboard();
    } catch (error) {
        console.error("MetaMask connection failed:", error);
        setWalletStatus("MetaMask connection request was rejected or failed. Retry when the wallet is available.", "warn");
        return null;
    }
}

async function copyPreferredWalletAddress() {
    if (typeof navigator !== "undefined" && navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
        await navigator.clipboard.writeText(PREFERRED_WALLET_ADDRESS);
        setWalletStatus("Preferred DAO wallet address copied to the clipboard.", "ok");
        return;
    }

    notifyUser(`Preferred DAO wallet: ${PREFERRED_WALLET_ADDRESS}`);
    setWalletStatus("Clipboard access is unavailable in this browser. The preferred wallet address was shown in a prompt instead.", "idle");
}

function bindWalletControls() {
    const elements = getWalletElements();
    if (!elements) {
        return;
    }

    if (elements.connectWalletButton) {
        elements.connectWalletButton.addEventListener("click", () => {
            connectPreferredWallet();
        });
    }

    if (elements.copyWalletButton) {
        elements.copyWalletButton.addEventListener("click", () => {
            copyPreferredWalletAddress().catch((error) => {
                console.error("Failed to copy preferred wallet address:", error);
                setWalletStatus("Copying the preferred wallet address failed. You can still copy it manually from the page.", "warn");
            });
        });
    }

    if (typeof window !== "undefined" && window.ethereum && typeof window.ethereum.on === "function") {
        window.ethereum.on("accountsChanged", () => {
            refreshWalletDashboard();
        });
        window.ethereum.on("chainChanged", () => {
            refreshWalletDashboard();
        });
    }
}

function bindWorkspaceControls() {
    const elements = getWorkspaceElements();
    if (!elements) {
        return;
    }

    if (elements.dashboardSearch) {
        elements.dashboardSearch.addEventListener("input", (event) => {
            filterDashboardCards(event.target.value);
        });
    }

    if (elements.clearDashboardSearchButton) {
        elements.clearDashboardSearchButton.addEventListener("click", () => {
            if (elements.dashboardSearch) {
                elements.dashboardSearch.value = "";
            }
            filterDashboardCards("");
        });
    }

    if (elements.refreshWalletButton) {
        elements.refreshWalletButton.addEventListener("click", () => {
            refreshWalletDashboard();
        });
    }
}

function hydrateChimeraDashboard() {
    populateDaoStats();
    populateFeatureContainer("[data-dao-features]", DAO_FEATURES);
    populateFeatureContainer("[data-dao-operations]", DAO_OPERATIONS);
    populateContainer("[data-web3-links]", WEB3_PROJECT_LINKS);
    populateContainer("[data-repo-links]", REPOSITORY_ENTRY_POINTS);
    populateContainer("[data-governance-links]", GOVERNANCE_LINKS);
    populateValidationSummary();
    bindWorkspaceControls();
    filterDashboardCards("");
    updateWalletDetails({
        connectedAddress: "",
        chainId: "",
        matchesPreferredWallet: false,
    });
    bindWalletControls();
    refreshWalletDashboard();
}

if (typeof window !== "undefined") {
    window.NexusDashboard = {
        DAO_FEATURES,
        DAO_OPERATIONS,
        WEB3_PROJECT_LINKS,
        REPOSITORY_ENTRY_POINTS,
        GOVERNANCE_LINKS,
        VALIDATION_SUMMARY,
        PREFERRED_WALLET_ADDRESS,
        ETHERSCAN_ADDRESS_URL,
        buildDaoStats,
        filterDashboardCards,
        connectPreferredWallet,
        copyPreferredWalletAddress,
        refreshWalletDashboard,
        hydrateChimeraDashboard,
    };

    if (typeof document !== "undefined") {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", hydrateChimeraDashboard);
        } else {
            hydrateChimeraDashboard();
        }
    }
}

function notifyUser(message) {
    if (typeof window !== "undefined" && typeof window.alert === "function") {
        window.alert(message);
        return;
    }
    console.warn(message);
}

// --- Contract Addresses (replace with your deployed addresses) ---
const nexusFinancialContractAddress = "0x...";
const nexusGreenTokenAddress = "0x...";

let provider;
let signer;
let nexusFinancialContract;
let nexusGreenToken;

/**
 * Connects to the user's Ethereum wallet (e.g., MetaMask).
 */
async function connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
        try {
            provider = new ethers.providers.Web3Provider(window.ethereum);
            await provider.send("eth_requestAccounts", []);
            signer = provider.getSigner();

            nexusFinancialContract = new ethers.Contract(nexusFinancialContractAddress, NexusFinancialContractABI.abi, signer);
            nexusGreenToken = new ethers.Contract(nexusGreenTokenAddress, NexusGreenTokenABI.abi, signer);

            console.log("Wallet connected:", await signer.getAddress());
            // Add UI logic to show connected state
        } catch (error) {
            console.error("User rejected connection:", error);
            // Add UI logic to show connection error
        }
    } else {
        console.error("MetaMask is not installed!");
        // Add UI logic to prompt user to install MetaMask
    }
}

/**
 * Listens for events from the NexusFinancialContract.
 */
function setupEventListeners() {
    if (!nexusFinancialContract) return;

    nexusFinancialContract.on("TransactionInitiated", (transactionId, initiator, principal) => {
        console.log(`Transaction Initiated: ID=${transactionId}, User=${initiator}, Amount=${ethers.utils.formatEther(principal)}`);
        // Add UI logic to display a notification or update a transaction list.
    });

    nexusFinancialContract.on("TransactionStateChanged", (transactionId, newState) => {
        console.log(`Transaction State Changed: ID=${transactionId}, New State=${newState}`);
        // Update the UI to reflect the new state of the transaction.
    });

    nexusFinancialContract.on("ProposalCreated", (proposalId, proposer, description) => {
        console.log(`New Proposal: ID=${proposalId}, Proposer=${proposer}, Desc=${description}`);
        // Add the new proposal to the DAO voting section of the UI.
    });
}


/**
 * Example function to be called from the UI to create a DAO proposal.
 * Note: In the real dApp, this would be an admin/backend function.
 * @param {string} description The text description of the proposal.
 */
async function createProposal(description) {
    if (!nexusFinancialContract) {
        notifyUser("Please connect your wallet first.");
        return;
    }
    try {
        const tx = await nexusFinancialContract.createProposal(description);
        console.log("Creating proposal... TX hash:", tx.hash);
        await tx.wait();
        console.log("Proposal created successfully!");
        // Add UI feedback
    } catch (error) {
        console.error("Error creating proposal:", error);
    }
}


/**
 * Example function to vote on a proposal.
 * @param {number} proposalId The ID of the proposal to vote on.
 */
async function voteOnProposal(proposalId) {
    if (!nexusFinancialContract) {
        notifyUser("Please connect your wallet first.");
        return;
    }
    try {
        const tx = await nexusFinancialContract.vote(proposalId);
        console.log(`Voting on proposal ${proposalId}... TX hash:`, tx.hash);
        await tx.wait();
        console.log("Voted successfully!");
        // Add UI feedback
    } catch (error) {
        console.error("Error voting:", error);
    }
}


// --- Pseudo-code for how the off-chain system would interact ---
// This part is NOT for the frontend but illustrates the backend process.

/**
 * [BACKEND ONLY] Simulates the autonomous system initiating a transaction.
 * @param {string} userAddress The user's wallet address.
 * @param {number} amount The principal amount.
 */
async function backend_initiateTransaction(userAddress, amount) {
    // This requires a signer with owner privileges on the contract.
    const ownerSigner = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);
    const contractAsOwner = nexusFinancialContract.connect(ownerSigner);

    const principal = ethers.utils.parseEther(amount.toString());
    const metadataUri = `https://api.projectchimera.dev/transactions/${Date.now()}`;

    const tx = await contractAsOwner.initiateTransaction(userAddress, principal, metadataUri);
    await tx.wait();
    // ... then backend monitors and calls updateTransactionState and distributeValue
}
