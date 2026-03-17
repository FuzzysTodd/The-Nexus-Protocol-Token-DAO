from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent


def test_chimera_dashboard_references_dashboard_script_and_sections():
    dashboard = (REPO_ROOT / "chimera.html").read_text()

    assert "Nexus Protocol Web3 Directory" in dashboard
    assert "Verified public web links" in dashboard
    assert "Governance coverage" in dashboard
    assert "Nexus owner + authority map" in dashboard
    assert "@FuzzysTodd" in dashboard
    assert '<script src="./logical.js"></script>' in dashboard


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
        "./contracts/NexusGameTheoryToken.sol",
        "./Nouns-DAO/contracts/governance/NounsDAOLogicV3.sol",
        "./Nouns-DAO/contracts/test/NounsDAOLogicV3Harness.sol",
        "@FuzzysTodd",
        "Delegated AI + MPC creation scope",
        "Protected account + token controls",
        "existing 7-test suite",
    ]

    for link in expected_links:
        assert link in script
