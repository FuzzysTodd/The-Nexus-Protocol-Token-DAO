from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
MCP_ASSESSMENT_SUMMARY = (
    "Customized MCP/MPC assessment coverage now includes "
    "repository inventory, branch calculation, and DAO "
    "improvement priorities."
)


def test_chimera_dashboard_references_dashboard_script_and_sections():
    dashboard = (REPO_ROOT / "chimera.html").read_text()

    assert "Nexus Protocol Web3 Directory" in dashboard
    assert "Verified public web links" in dashboard
    assert "Customized MCP/MPC servers" in dashboard
    assert "Governance coverage" in dashboard
    assert "Nexus owner + authority map" in dashboard
    assert "@FuzzysTodd" in dashboard
    assert '<script src="./logical.js"></script>' in dashboard
    assert "./logical_demo.js" in dashboard


def test_dashboard_script_contains_verified_web_links_and_governance_targets():
    script = (REPO_ROOT / "logical.js").read_text()

    expected_links = [
        "https://nouns.wtf",
        "https://docs.aave.com/developers/",
        "https://governance.aave.com/",
        "https://chain.link/",
        "https://docs.chain.link/",
        "https://gmxio.gitbook.io/gmx/contracts",
        "./GOVERNANCE.md",
        "./nexus/repo_assessment.py",
        "./mcp/agents/mig-network-config.json",
        "./contracts/NexusGameTheoryToken.sol",
        "./Nouns-DAO/contracts/governance/NounsDAOLogicV3.sol",
        "./Nouns-DAO/contracts/test/NounsDAOLogicV3Harness.sol",
    ]

    for link in expected_links:
        assert link in script


def test_dashboard_script_is_static_only_and_wallet_demo_is_isolated():
    dashboard_script = (REPO_ROOT / "logical.js").read_text()
    demo_script = (REPO_ROOT / "logical_demo.js").read_text()

    assert "connectWallet" not in dashboard_script
    assert "ethers.providers.Web3Provider" not in dashboard_script
    assert "YOUR_PRIVATE_KEY" not in dashboard_script

    assert "connectWallet" in demo_script
    assert "voteOnProposal" in demo_script
    assert "server-side" in demo_script
    assert "YOUR_PRIVATE_KEY" not in demo_script


def test_ci_workflow_is_validation_only():
    workflow = (
        REPO_ROOT / ".github" / "workflows" / "main.yml"
    ).read_text()

    assert "contents: read" in workflow
    assert "Self-heal backoff" not in workflow
    assert "Create PR on success" not in workflow
    assert "git push" not in workflow
    assert 'pytest -q || echo "TESTS_FAILED" > .agent/status' not in workflow
