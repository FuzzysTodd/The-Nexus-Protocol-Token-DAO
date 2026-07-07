import json

def failsafe_active():
    with open("failsafe/state.json") as f:
        state = json.load(f)
    return state.get("martial_law", False)
