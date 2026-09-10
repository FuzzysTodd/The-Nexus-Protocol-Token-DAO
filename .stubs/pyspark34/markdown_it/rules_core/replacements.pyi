import re
from ..token import Token as Token
from .state_core import StateCore as StateCore
from _typeshed import Incomplete

LOGGER: Incomplete
RARE_RE: Incomplete
SCOPED_ABBR_RE: Incomplete
PLUS_MINUS_RE: Incomplete
ELLIPSIS_RE: Incomplete
ELLIPSIS_QUESTION_EXCLAMATION_RE: Incomplete
QUESTION_EXCLAMATION_RE: Incomplete
COMMA_RE: Incomplete
EM_DASH_RE: Incomplete
EN_DASH_RE: Incomplete
EN_DASH_INDENT_RE: Incomplete
SCOPED_ABBR: Incomplete

def replaceFn(match: re.Match[str]) -> str: ...
def replace_scoped(inlineTokens: list[Token]) -> None: ...
def replace_rare(inlineTokens: list[Token]) -> None: ...
def replace(state: StateCore) -> None: ...
