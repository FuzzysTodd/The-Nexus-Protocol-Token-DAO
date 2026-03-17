"""Tests for MCP task plan generation."""

import json
from pathlib import Path

from nexus.mcp_plan import (
    build_mcp_plan,
    collect_repository_files,
    load_mcp_agents,
    write_mcp_plan_and_provenance,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "mcp" / "agents" / "mig-network-config.json"


def test_build_mcp_plan_maps_agents_to_their_tasks():
    agents = load_mcp_agents(CONFIG_PATH)

    plan = build_mcp_plan(agents)

    assert plan.startswith("# Plan")
    assert "- [ ] mcp-001: Game Theory Coordinator" in plan
    assert "  - coordinate game sessions" in plan
    assert "- [ ] mcp-010: Financial Analytics Agent" in plan
    assert "  - Bitcoin integration monitoring" in plan


def test_write_mcp_plan_and_provenance_records_agent_metadata(tmp_path):
    plan_path, provenance_path = write_mcp_plan_and_provenance(
        config_path=CONFIG_PATH,
        plan_dir=tmp_path / "plans",
        provenance_dir=tmp_path / "provenance",
        root=REPO_ROOT,
        timestamp=1234567890,
    )

    assert plan_path.name == "plan-1234567890.md"
    assert provenance_path.name == "1234567890.json"
    assert "- [ ] mcp-005: GPU Rendering Engine" in plan_path.read_text(
        encoding="utf-8"
    )

    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    assert provenance["ts"] == 1234567890
    assert provenance["agents"][0]["id"] == "mcp-001"
    assert provenance["agents"][0]["role"] == "Game Theory Coordinator"
    assert ".gitignore" in provenance["files"]
    assert "chimera.html" in provenance["files"]
    assert "nexus/test_telemetry.py" in provenance["files"]


def test_collect_repository_files_only_returns_tracked_repo_files():
    untracked_path = REPO_ROOT / "nexus" / "_tmp_untracked_mcp_plan_test.py"
    untracked_path.write_text("temporary = True\n", encoding="utf-8")

    try:
        files = collect_repository_files(REPO_ROOT)
    finally:
        untracked_path.unlink()

    assert ".gitignore" in files
    assert "mcp/agents/mig-network-config.json" in files
    assert "nexus/_tmp_untracked_mcp_plan_test.py" not in files
