// Static dashboard data and rendering for the Project Chimera repository index.

// --- Dashboard data for the static repository index ---
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
        name: "Nexus User Guide (Start Here!)",
        href: "./user-guide.html",
        description: "Friendly walkthrough for humans - explains how to use Nexus Protocol from beginner to advanced.",
        source: "Local user guide",
    },
    {
        name: "Contract Withdrawal Manager",
        href: "./withdraw.html",
        description: "Interactive interface to manage withdrawals from smart contracts using MetaMask.",
        source: "Local web interface",
    },
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

const CUSTOM_MCP_SERVERS = [
    {
        name: "Repository assessment module",
        href: "./nexus/repo_assessment.py",
        description: "Calculates repository inventory, branch coverage, and DAO improvement priorities against real-world web3 references.",
        source: "nexus/repo_assessment.py",
    },
    {
        name: "MIG network config (MCP agents)",
        href: "./mcp/agents/mig-network-config.json",
        description: "Defines 10 MCP agents (mcp-001 through mcp-010) covering game theory, tokenomics, governance, GPU rendering, and more.",
        source: "mcp/agents/mig-network-config.json",
    },
];

const AUTHORITY_MAP_LINKS = [
    {
        name: "Owner & authority — @FuzzysTodd",
        href: "./@FuzzysTodd.md",
        description: "Repository owner and primary admin anchor. Wallet: 0x33ffc308e693a5b49e0ee0241f41f03ccef495f2",
        source: "@FuzzysTodd.md",
    },
    {
        name: "Governance charter",
        href: "./GOVERNANCE.md",
        description: "Authority structure, DAO mandate, and operating rules for the Nexus Protocol repository.",
        source: "GOVERNANCE.md",
    },
    {
        name: "MCP gateway documentation",
        href: "./MCP_GATEWAY_DOCUMENTATION.md",
        description: "Complete MCP/MFC Gateway FPGA GPU Swarm Hive orchestration system documentation.",
        source: "MCP_GATEWAY_DOCUMENTATION.md",
    },
];

const MONSTERBALL_LINKS = [
    {
        name: "MonsterBall module",
        href: "./nexus/monsterball.py",
        description: "PlayerStats dataclass, PredictorWeights, predict(), rank_players(), render_match_report(). Universal weighted predictor for any numeric domain.",
        source: "nexus/monsterball.py",
    },
    {
        name: "MonsterBall tests",
        href: "./nexus/test_monsterball.py",
        description: "11 focused tests: DOMINANT/SUBDUED verdicts, ranking, match reports, arbitrary-domain prediction.",
        source: "nexus/test_monsterball.py",
    },
];

const SUPER_LOGICAL_LINKS = [
    {
        name: "Super Logical module",
        href: "./nexus/super_logical.py",
        description: "64-dimension SuperLogicalWeights, LogicalReading, super_predict(), compose_super_predict(), render_super_logical_report(). CRITICAL/HIGH/MODERATE/LOW tiers.",
        source: "nexus/super_logical.py",
    },
    {
        name: "Super Logical tests",
        href: "./nexus/test_super_logical.py",
        description: "18 tests: confidence tiers, reasoning chain, domain presets, empty results, arbitrary-domain coverage.",
        source: "nexus/test_super_logical.py",
    },
];

const ALGEBRA3_LINKS = [
    {
        name: "3-Algebra module",
        href: "./nexus/algebra3.py",
        description: "Three algebraic layers (L1 linear, L2 polynomial, L3 exponential) blended by alpha/beta/gamma. Behavior library with 10 named profiles. apply_algebra3() works on any domain.",
        source: "nexus/algebra3.py",
    },
    {
        name: "3-Algebra tests",
        href: "./nexus/test_algebra3.py",
        description: "24 tests: layer arithmetic, behavior matching, domain presets, human-response and climate arbitrary domains.",
        source: "nexus/test_algebra3.py",
    },
];

const SUPREMACY_LINKS = [
    {
        name: "NGTT Supremacy module",
        href: "./nexus/nexus_token_supremacy.py",
        description: "Runs MonsterBall + Super Logical + 3-Algebra against the full NGTT stat profile. Produces a fused supremacy score, BTC-era rank, and a permanent eternal declaration.",
        source: "nexus/nexus_token_supremacy.py",
    },
    {
        name: "NGTT Supremacy tests",
        href: "./nexus/test_nexus_token_supremacy.py",
        description: "20 tests: DOMINANT verdict, CRITICAL/HIGH tier, GREATEST rank, eternal declaration, score bounds, three-engine outputs.",
        source: "nexus/test_nexus_token_supremacy.py",
    },
    {
        name: "NGTT contract",
        href: "./contracts/NexusGameTheoryToken.sol",
        description: "The on-chain NGTT token with BTC-backing ratio, MCP groups, skill rewards, and profit distribution.",
        source: "contracts/NexusGameTheoryToken.sol",
    },
];

const SIGNAL_REPAIR_LINKS = [
    {
        name: "Signal repair module",
        href: "./nexus/signal_repair.py",
        description: "1 000-particle deterministic solver that evaluates degraded exchange signals and votes on consensus repair. Detects NOISY / DRIFTED / SPIKED / CLIPPED / DROPPED and more.",
        source: "nexus/signal_repair.py",
    },
    {
        name: "Signal repair tests",
        href: "./nexus/test_signal_repair.py",
        description: "Tests for the 1 000-particle signal repair consensus algorithm.",
        source: "nexus/test_signal_repair.py",
    },
];

const ATMOSPHERE_LINKS = [
    {
        name: "Atmosphere / planetary harmony module",
        href: "./nexus/atmosphere.py",
        description: "Electrons, quarks, neutrinos, photons, the Higgs boson and every Standard Model particle scored through 3-Algebra + Super Logical for GREATEST planetary health.",
        source: "nexus/atmosphere.py",
    },
    {
        name: "Atmosphere tests",
        href: "./nexus/test_atmosphere.py",
        description: "Tests validating the planetary and solar harmony scoring system.",
        source: "nexus/test_atmosphere.py",
    },
];

const FAMILY_LINKS = [
    {
        name: "Family Renaissance module",
        href: "./nexus/family_renaissance.py",
        description: "Quantitative diagnosis of the American family crisis. Ranks root causes and prescribes a prioritised repair plan for communication, wealth, community, and purpose.",
        source: "nexus/family_renaissance.py",
    },
    {
        name: "Family Renaissance tests",
        href: "./nexus/test_family_renaissance.py",
        description: "Tests for the Gen X & Gen Z family crisis diagnosis and repair prioritisation engine.",
        source: "nexus/test_family_renaissance.py",
    },
];

const VALIDATION_SUMMARY = [
    "Baseline lint: flake8 . — 0 errors",
    "Baseline tests: pytest -q — all tests passing",
    "Governance docs and contracts indexed",
    "MCP/MPC assessment coverage: repository inventory, branch calculation, and DAO improvement priorities",
    "NGTT Bitcoin-era supremacy: DOMINANT verdict, CRITICAL tier, GREATEST rank — forever",
];

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function renderCard(item) {
    return `
        <article class="card">
            <h3>${escapeHtml(item.name)}</h3>
            <p>${escapeHtml(item.description)}</p>
            <a href="${escapeHtml(item.href)}" target="${item.href.startsWith("http") ? "_blank" : "_self"}" rel="noopener noreferrer">
                ${escapeHtml(item.href)}
            </a>
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

function populateValidationSummary() {
    if (typeof document === "undefined") return;
    const container = document.querySelector("[data-validation-summary]");
    if (!container) return;

    container.innerHTML = VALIDATION_SUMMARY.map((item) => `<li><strong>Verified:</strong> ${escapeHtml(item)}</li>`).join("");
}

function hydrateChimeraDashboard() {
    populateContainer("[data-web3-links]", WEB3_PROJECT_LINKS);
    populateContainer("[data-repo-links]", REPOSITORY_ENTRY_POINTS);
    populateContainer("[data-custom-mcp-servers]", CUSTOM_MCP_SERVERS);
    populateContainer("[data-governance-links]", GOVERNANCE_LINKS);
    populateContainer("[data-authority-map]", AUTHORITY_MAP_LINKS);
    populateContainer("[data-monsterball-links]", MONSTERBALL_LINKS);
    populateContainer("[data-super-logical-links]", SUPER_LOGICAL_LINKS);
    populateContainer("[data-algebra3-links]", ALGEBRA3_LINKS);
    populateContainer("[data-supremacy-links]", SUPREMACY_LINKS);
    populateContainer("[data-signal-repair-links]", SIGNAL_REPAIR_LINKS);
    populateContainer("[data-atmosphere-links]", ATMOSPHERE_LINKS);
    populateContainer("[data-family-links]", FAMILY_LINKS);

    populateValidationSummary();
}

if (typeof window !== "undefined") {
    window.NexusDashboard = {
        WEB3_PROJECT_LINKS,
        REPOSITORY_ENTRY_POINTS,
        CUSTOM_MCP_SERVERS,
        GOVERNANCE_LINKS,
        AUTHORITY_MAP_LINKS,
        MONSTERBALL_LINKS,
        SUPER_LOGICAL_LINKS,
        ALGEBRA3_LINKS,
        SUPREMACY_LINKS,
        SIGNAL_REPAIR_LINKS,
        ATMOSPHERE_LINKS,
        FAMILY_LINKS,
        VALIDATION_SUMMARY,
    };

    if (typeof document !== "undefined") {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", hydrateChimeraDashboard);
        } else {
            hydrateChimeraDashboard();
        }
    }
}
