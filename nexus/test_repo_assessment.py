"""Focused tests for repository and branch assessment helpers."""

import json

from nexus.repo_assessment import (
    collect_repo_assessment,
    render_repo_assessment,
)


def test_collect_repo_assessment_reports_repo_branch_and_mcp_inventory(
    tmp_path,
):
    (tmp_path / "Aave-V3").mkdir()
    (tmp_path / "Nouns-DAO").mkdir()
    (tmp_path / "Uniswap-V3").mkdir()
    (tmp_path / "contracts").mkdir()
    (tmp_path / "mcp" / "agents").mkdir(parents=True)
    (tmp_path / "docs").mkdir()
    (tmp_path / "contracts" / "NexusGameTheoryToken.sol").write_text(
        "pragma solidity ^0.8.0;"
    )
    (tmp_path / "GOVERNANCE.md").write_text("# Governance")
    (tmp_path / "chimera.html").write_text("<html></html>")
    (tmp_path / "docs" / "guide.md").write_text("# Guide")
    (tmp_path / "mcp" / "agents" / "mig-network-config.json").write_text(
        json.dumps(
            {
                "migNetwork": {
                    "mcpAgents": [{"id": "mcp-001"}, {"id": "mcp-011"}],
                    "mpcServers": [{"id": "mpc-server-001"}],
                }
            }
        )
    )

    def stub_runner(_command):
        return "* main\n  feature/dao\n  remotes/origin/main"

    summary = collect_repo_assessment(
        repo_root=tmp_path, command_runner=stub_runner
    )

    assert summary.current_branch == "main"
    assert [branch.name for branch in summary.branches] == [
        "main",
        "feature/dao",
        "remotes/origin/main",
    ]
    assert summary.web3_protocol_count == 3
    assert summary.custom_mcp_agent_count == 2
    assert summary.custom_mpc_server_count == 1
    assert summary.governance_asset_count == 4
    assert summary.dao_improvement_priorities


def test_render_repo_assessment_mentions_branch_protocols_and_improvements(
    tmp_path,
):
    (tmp_path / "basic-dao").mkdir()
    (tmp_path / "mcp" / "agents").mkdir(parents=True)
    (tmp_path / "mcp" / "agents" / "mig-network-config.json").write_text(
        json.dumps({"migNetwork": {"mcpAgents": [], "mpcServers": []}})
    )

    summary = collect_repo_assessment(
        repo_root=tmp_path,
        command_runner=lambda _command: "* main",
    )

    output = render_repo_assessment(summary)

    assert "REPOSITORY ASSESSMENT" in output
    assert "Current: main" in output
    assert "basic-dao" in output
    assert "[IMPROVE]" in output
