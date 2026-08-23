import re
from .specifiers import Specifier as Specifier
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Iterator, NoReturn, Tuple

@dataclass
class Token:
    name: str
    text: str
    position: int
    def __init__(self, name, text, position) -> None: ...

class ParserSyntaxError(Exception):
    """The provided source text could not be parsed correctly."""
    span: Incomplete
    message: Incomplete
    source: Incomplete
    def __init__(self, message: str, *, source: str, span: Tuple[int, int]) -> None: ...

DEFAULT_RULES: Dict[str, str | re.Pattern[str]]

class Tokenizer:
    """Context-sensitive token parsing.

    Provides methods to examine the input stream to check whether the next token
    matches.
    """
    source: Incomplete
    rules: Incomplete
    next_token: Incomplete
    position: int
    def __init__(self, source: str, *, rules: Dict[str, str | re.Pattern[str]]) -> None: ...
    def consume(self, name: str) -> None:
        """Move beyond provided token name, if at current position."""
    def check(self, name: str, *, peek: bool = False) -> bool:
        """Check whether the next token has the provided name.

        By default, if the check succeeds, the token *must* be read before
        another check. If `peek` is set to `True`, the token is not loaded and
        would need to be checked again.
        """
    def expect(self, name: str, *, expected: str) -> Token:
        """Expect a certain token name next, failing with a syntax error otherwise.

        The token is *not* read.
        """
    def read(self) -> Token:
        """Consume the next token and return it."""
    def raise_syntax_error(self, message: str, *, span_start: int | None = None, span_end: int | None = None) -> NoReturn:
        """Raise ParserSyntaxError at the given position."""
    def enclosing_tokens(self, open_token: str, close_token: str, *, around: str) -> Iterator[None]: ...
