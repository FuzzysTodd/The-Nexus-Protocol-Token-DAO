from ..common.utils import charCodeAt as charCodeAt, isMdAsciiPunct as isMdAsciiPunct, isPunctChar as isPunctChar, isWhiteSpace as isWhiteSpace
from ..token import Token as Token
from .state_core import StateCore as StateCore
from _typeshed import Incomplete

QUOTE_TEST_RE: Incomplete
QUOTE_RE: Incomplete
APOSTROPHE: str

def replaceAt(string: str, index: int, ch: str) -> str: ...
def process_inlines(tokens: list[Token], state: StateCore) -> None: ...
def smartquotes(state: StateCore) -> None: ...
