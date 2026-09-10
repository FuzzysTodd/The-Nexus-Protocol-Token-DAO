from ..token import Token as Token
from .state_core import StateCore as StateCore

def text_join(state: StateCore) -> None:
    """Join raw text for escape sequences (`text_special`) tokens with the rest of the text"""
