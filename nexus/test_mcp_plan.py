"""Tests for MCP task plan generation."""

import json
import os
import subprocess
import tempfile
from pathlib import Path

from nexus.mcp_plan import (
    build_mcp_plan,
    collect_repository_branches,
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
    assert provenance["branches"]
    assert provenance["agents"][0]["id"] == "mcp-001"
    assert provenance["agents"][0]["role"] == "Game Theory Coordinator"
    assert ".gitignore" in provenance["files"]
    assert "chimera.html" in provenance["files"]
    assert "nexus/test_telemetry.py" in provenance["files"]


def test_collect_repository_files_only_returns_tracked_repo_files():
    fd, name = tempfile.mkstemp(
        dir=REPO_ROOT / "nexus",
        prefix="_tmp_untracked_mcp_plan_",
        suffix=".tmp",
        text=True,
    )
    untracked_path = Path(name)
    untracked_name = f"nexus/{untracked_path.name}"
    os.close(fd)
    untracked_path.write_text("temporary = True\n", encoding="utf-8")

    try:
        files = collect_repository_files(REPO_ROOT)
    finally:
        untracked_path.unlink(missing_ok=True)

    assert ".gitignore" in files
    assert "mcp/agents/mig-network-config.json" in files
    assert untracked_name not in files


def test_collect_repository_files_falls_back_to_filtered_filesystem_scan(
    tmp_path, monkeypatch
):
    (tmp_path / ".gitignore").write_text("node_modules/\n", encoding="utf-8")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "guide.md").write_text("# Guide\n", encoding="utf-8")
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config").write_text("[core]\n", encoding="utf-8")
    (tmp_path / "node_modules").mkdir()
    (tmp_path / "node_modules" / "pkg.js").write_text(
        "module.exports = {}\n", encoding="utf-8"
    )

    def raise_git_unavailable(*_args, **_kwargs):
        raise FileNotFoundError

    monkeypatch.setattr(subprocess, "run", raise_git_unavailable)

    files = collect_repository_files(tmp_path)

    assert ".gitignore" in files
    assert "docs/guide.md" in files
    assert ".git/config" not in files
    assert "node_modules/pkg.js" not in files


def test_collect_repository_branches_excludes_origin_head(monkeypatch):
    def fake_run(*_args, **_kwargs):
        class CompletedProcess:
            stdout = "\n".join(
                [
                    "main",
                    "feature/mcp",
                    "origin/main",
                    "origin/feature/mcp",
                    "origin/HEAD",
                ]
            )

        return CompletedProcess()

    monkeypatch.setattr(subprocess, "run", fake_run)

    branches = collect_repository_branches(REPO_ROOT)

    assert branches == [
        "feature/mcp",
        "main",
        "origin/feature/mcp",
        "origin/main",
    ]


def test_collect_repository_branches_returns_empty_list_when_git_fails(
    monkeypatch,
):
    def raise_git_failure(*_args, **_kwargs):
        raise subprocess.CalledProcessError(1, "git")

    monkeypatch.setattr(subprocess, "run", raise_git_failure)

    assert collect_repository_branches(REPO_ROOT) == []
