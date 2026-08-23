from .._compat import DATACLASS_KWARGS as DATACLASS_KWARGS
from ..common.utils import isMdAsciiPunct as isMdAsciiPunct, isPunctChar as isPunctChar, isWhiteSpace as isWhiteSpace
from ..ruler import StateBase as StateBase
from ..token import Token as Token
from ..utils import EnvType as EnvType
from _typeshed import Incomplete
from dataclasses import dataclass
from markdown_it import MarkdownIt as MarkdownIt
from typing import Literal, NamedTuple

@dataclass(**DATACLASS_KWARGS)
class Delimiter:
    marker: int
    length: int
    token: int
    end: int
    open: bool
    close: bool
    level: bool | None = ...
    def __init__(self, marker, length, token, end, open, close, level) -> None: ...

class Scanned(NamedTuple):
    can_open: Incomplete
    can_close: Incomplete
    length: Incomplete

class StateInline(StateBase):
    src: Incomplete
    env: Incomplete
    md: Incomplete
    tokens: Incomplete
    tokens_meta: Incomplete
    pos: int
    posMax: Incomplete
    level: int
    pending: str
    pendingLevel: int
    cache: Incomplete
    delimiters: Incomplete
    backticks: Incomplete
    backticksScanned: bool
    linkLevel: int
    def __init__(self, src: str, md: MarkdownIt, env: EnvType, outTokens: list[Token]) -> None: ...
    def pushPending(self) -> Token: ...
    def push(self, ttype: str, tag: str, nesting: Literal[-1, 0, 1]) -> Token:
        '''Push new token to "stream".
        If pending text exists - flush it as text token
        '''
    def scanDelims(self, start: int, canSplitWord: bool) -> Scanned:
        """
        Scan a sequence of emphasis-like markers, and determine whether
        it can start an emphasis sequence or end an emphasis sequence.

         - start - position to scan from (it should point at a valid marker);
         - canSplitWord - determine if these markers can be found inside a word

        """
