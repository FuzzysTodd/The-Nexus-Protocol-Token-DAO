from .state_inline import Delimiter as Delimiter, StateInline as StateInline

def tokenize(state: StateInline, silent: bool) -> bool:
    """Insert each marker as a separate text token, and add it to delimiter list"""
def postProcess(state: StateInline) -> None:
    """Walk through delimiter list and replace text tokens with tags."""
