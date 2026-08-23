from . import rules_block as rules_block
from .ruler import Ruler as Ruler
from .rules_block.state_block import StateBlock as StateBlock
from .token import Token as Token
from .utils import EnvType as EnvType
from _typeshed import Incomplete
from markdown_it import MarkdownIt as MarkdownIt
from typing import Callable

LOGGER: Incomplete
RuleFuncBlockType = Callable[[StateBlock, int, int, bool], bool]

class ParserBlock:
    """
    ParserBlock#ruler -> Ruler

    [[Ruler]] instance. Keep configuration of block rules.
    """
    ruler: Incomplete
    def __init__(self) -> None: ...
    def tokenize(self, state: StateBlock, startLine: int, endLine: int) -> None:
        """Generate tokens for input range."""
    def parse(self, src: str, md: MarkdownIt, env: EnvType, outTokens: list[Token]) -> list[Token] | None:
        """Process input string and push block tokens into `outTokens`."""
