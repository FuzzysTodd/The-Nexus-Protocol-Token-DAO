import json
from pathlib import Path
from failsafe import failsafe_active

REGISTRY_PATH = Path("mcp/nexus-agent-registry.json")

def load_registry():
    """Load the MCP agent registry JSON."""
    with REGISTRY_PATH.open() as f:
        return json.load(f)

def resolve_martial_law(registry: dict) -> bool:
    """
    Determine if martial law is active.
    - Primary source: failsafe/state.json (via failsafe_active())
    - Secondary source: registry.failsafe.martial_law
    """
    ml_failsafe = failsafe_active()
    ml_registry = registry.get("failsafe", {}).get("martial_law", False)
    return ml_failsafe or ml_registry

def load_active_agents():
    """Return only agents allowed under current failsafe conditions."""
    registry = load_registry()
    martial_law = resolve_martial_law(registry)

    active_agents = []
    for agent in registry.get("agents", []):
        # Skip AI/automation agents during martial law
        if martial_law and agent.get("disabled_when_martial_law", False):
            print(f"[MARTIAL LAW] Skipping agent: {agent['id']}")
            continue

        # Manual-only mode enforcement
        if martial_law and agent.get("mode") == "manual-only":
            print(f"[MARTIAL LAW] Loading manual-only agent: {agent['id']}")
            active_agents.append(agent)
            continue

        # Normal mode
        active_agents.append(agent)

    return active_agents

def init_agents():
    """Initialize all active agents."""
    agents = load_active_agents()
    for agent in agents:
        print(f"Initializing agent: {agent['id']} (mode={agent.get('mode')})")
        # TODO: Insert your actual MCP agent initialization logic here
        # Example:
        # agent_init(agent["endpoint"], agent["role"])

if __name__ == "__main__":
    init_agents()
