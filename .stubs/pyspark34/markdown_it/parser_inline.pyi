from . import rules_inline as rules_inline
from .ruler import Ruler as Ruler
from .rules_inline.state_inline import StateInline as StateInline
from .token import Token as Token
from .utils import EnvType as EnvType
from _typeshed import Incomplete
from markdown_it import MarkdownIt as MarkdownIt
from typing import Callable

RuleFuncInlineType = Callable[[StateInline, bool], bool]
RuleFuncInline2Type = Callable[[StateInline], None]

class ParserInline:
    ruler: Incomplete
    ruler2: Incomplete
    def __init__(self) -> None: ...
    def skipToken(self, state: StateInline) -> None:
        """Skip single token by running all rules in validation mode;
        returns `True` if any rule reported success
        """
    def tokenize(self, state: StateInline) -> None:
        """Generate tokens for input range."""
    def parse(self, src: str, md: MarkdownIt, env: EnvType, tokens: list[Token]) -> list[Token]:
        """Process input string and push inline tokens into `tokens`"""
