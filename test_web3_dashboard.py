from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent


def test_chimera_dashboard_references_dashboard_script_and_sections():
    dashboard = (REPO_ROOT / "chimera.html").read_text()

    assert "Nexus DAO Command Center" in dashboard
    assert "MetaMask control center" in dashboard
    assert "data-preferred-wallet-address" in dashboard
    assert "data-open-wallet" in dashboard
    assert 'href="#"' in dashboard
    assert "DAO feature map" in dashboard
    assert "How the DAO operates" in dashboard
    assert "Verified public web links" in dashboard
    assert "Governance coverage" in dashboard
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
        "https://etherscan.io/address/",
        "0xeCE999c86452c573Adfdd7F0C9226e673477973a",
    ]

    for link in expected_links:
        assert link in script

    expected_wallet_hooks = [
        "eth_requestAccounts",
        "eth_accounts",
        "eth_chainId",
        "accountsChanged",
        "chainChanged",
        "PREFERRED_WALLET_ADDRESS",
    ]

    for wallet_hook in expected_wallet_hooks:
        assert wallet_hook in script
