from ..common.utils import arrayReplaceAt as arrayReplaceAt, isLinkClose as isLinkClose, isLinkOpen as isLinkOpen
from ..token import Token as Token
from .state_core import StateCore as StateCore
from _typeshed import Incomplete
from typing import Protocol

HTTP_RE: Incomplete
MAILTO_RE: Incomplete
TEST_MAILTO_RE: Incomplete

def linkify(state: StateCore) -> None:
    """Rule for identifying plain-text links."""

class _LinkType(Protocol):
    url: str
    text: str
    index: int
    last_index: int
    schema: str | None
