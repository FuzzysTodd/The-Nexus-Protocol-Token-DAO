import json
from pathlib import Path
from failsafe import failsafe_active

REGISTRY_PATH = Path("mcp/nexus-agent-registry.json")

def load_registry():
    with REGISTRY_PATH.open() as f:
        return json.load(f)

def resolve_martial_law(registry: dict) -> bool:
    # Global flag from failsafe/state.json
    ml_failsafe = failsafe_active()

    # Optional override from registry itself
    ml_registry = registry.get("failsafe", {}).get("martial_law", False)

    return ml_failsafe or ml_registry

def load_active_agents():
    registry = load_registry()
    martial_law = resolve_martial_law(registry)

    active_agents = []
    for agent in registry.get("agents", []):
        if martial_law and agent.get("disabled_when_martial_law", False):
            # Skip AI/automation agents in emergency mode
            continue
        active_agents.append(agent)

    return active_agents

def init_agents():
    agents = load_active_agents()
    for agent in agents:
        # TODO: your actual MCP agent init logic here
        print(f"Initializing agent: {agent['id']} (mode={agent.get('mode')})")

if __name__ == "__main__":
    init_agents()
