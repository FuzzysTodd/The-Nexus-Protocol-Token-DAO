from .ruler import Ruler as Ruler
from .rules_core import block as block, inline as inline, linkify as linkify, normalize as normalize, replace as replace, smartquotes as smartquotes, text_join as text_join
from .rules_core.state_core import StateCore as StateCore
from _typeshed import Incomplete
from typing import Callable

RuleFuncCoreType = Callable[[StateCore], None]

class ParserCore:
    ruler: Incomplete
    def __init__(self) -> None: ...
    def process(self, state: StateCore) -> None:
        """Executes core chain rules."""
