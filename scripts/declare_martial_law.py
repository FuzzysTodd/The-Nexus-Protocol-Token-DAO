import json, datetime

with open("failsafe/state.json") as f:
    state = json.load(f)

state["martial_law"] = True
state["activated_by"] = "todd"
state["activated_at"] = datetime.datetime.utcnow().isoformat()
state["reason"] = "AI/automation outage"

with open("failsafe/state.json", "w") as f:
    json.dump(state, f, indent=4)

print("Martial law declared.")
