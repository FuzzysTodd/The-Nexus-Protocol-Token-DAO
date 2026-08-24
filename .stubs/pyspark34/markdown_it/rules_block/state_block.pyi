from ..common.utils import isStrSpace as isStrSpace
from ..ruler import StateBase as StateBase
from ..token import Token as Token
from ..utils import EnvType as EnvType
from _typeshed import Incomplete
from markdown_it.main import MarkdownIt as MarkdownIt
from typing import Literal

class StateBlock(StateBase):
    src: Incomplete
    md: Incomplete
    env: Incomplete
    tokens: Incomplete
    bMarks: Incomplete
    eMarks: Incomplete
    tShift: Incomplete
    sCount: Incomplete
    bsCount: Incomplete
    blkIndent: int
    line: int
    lineMax: int
    tight: bool
    ddIndent: int
    listIndent: int
    parentType: str
    level: int
    result: str
    def __init__(self, src: str, md: MarkdownIt, env: EnvType, tokens: list[Token]) -> None: ...
    def push(self, ttype: str, tag: str, nesting: Literal[-1, 0, 1]) -> Token:
        '''Push new token to "stream".'''
    def isEmpty(self, line: int) -> bool:
        """."""
    def skipEmptyLines(self, from_pos: int) -> int:
        """."""
    def skipSpaces(self, pos: int) -> int:
        """Skip spaces from given position."""
    def skipSpacesBack(self, pos: int, minimum: int) -> int:
        """Skip spaces from given position in reverse."""
    def skipChars(self, pos: int, code: int) -> int:
        """Skip character code from given position."""
    def skipCharsStr(self, pos: int, ch: str) -> int:
        """Skip character string from given position."""
    def skipCharsBack(self, pos: int, code: int, minimum: int) -> int:
        """Skip character code reverse from given position - 1."""
    def skipCharsStrBack(self, pos: int, ch: str, minimum: int) -> int:
        """Skip character string reverse from given position - 1."""
    def getLines(self, begin: int, end: int, indent: int, keepLastLF: bool) -> str:
        """Cut lines range from source."""
    def is_code_block(self, line: int) -> bool:
        """Check if line is a code block,
        i.e. the code block rule is enabled and text is indented by more than 3 spaces.
        """
