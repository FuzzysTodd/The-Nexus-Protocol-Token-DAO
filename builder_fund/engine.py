import json
from pathlib import Path
from failsafe import failsafe_active

REGISTRY_PATH = Path("mcp/nexus-agent-registry.json")

def load_registry():
    """Load the MCP agent registry JSON."""
    with REGISTRY_PATH.open() as f:
        return json.load(f)

def resolve_martial_law():
    """Determine if martial law is active."""
    registry = load_registry()
    ml_failsafe = failsafe_active()
    ml_registry = registry.get("failsafe", {}).get("martial_law", False)
    return ml_failsafe or ml_registry

def run_ai_builder_fund_cycle():
    print("[BUILDER FUND] Running AI/automation builder fund cycle...")
    # TODO: your existing automated builder fund logic:
    # - automated micropayments to contributors
    # - automated scoring of contributions
    # - automated stream adjustments
    # - automated grant disbursements

def run_manual_builder_fund_cycle():
    print("[BUILDER FUND] Running MANUAL builder fund cycle...")
    # TODO: deterministic manual builder fund logic:
    # - human review of contributions
    # - manual approval of payouts
    # - manual grant decisions
    # - manual stream adjustments

def run_builder_fund_engine():
    martial_law = resolve_martial_law()

    if martial_law:
        print("[MARTIAL LAW] Builder fund engine in manual-only mode.")
        run_manual_builder_fund_cycle()
    else:
        print("[NORMAL] Builder fund engine in AI/automation mode.")
        run_ai_builder_fund_cycle()

if __name__ == "__main__":
    run_builder_fund_engine()
