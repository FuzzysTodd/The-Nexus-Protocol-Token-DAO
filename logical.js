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


    },

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

\

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
    populateContainer("[data-governance-links]", GOVERNANCE_LINKS);

    populateValidationSummary();
}

if (typeof window !== "undefined") {
    window.NexusDashboard = {
        WEB3_PROJECT_LINKS,
        REPOSITORY_ENTRY_POINTS,
        GOVERNANCE_LINKS,

    };

    if (typeof document !== "undefined") {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", hydrateChimeraDashboard);
        } else {
            hydrateChimeraDashboard();
        }
    }
}
