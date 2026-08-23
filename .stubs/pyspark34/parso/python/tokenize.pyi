from _typeshed import Incomplete
from parso.python.token import PythonTokenTypes as PythonTokenTypes
from parso.utils import PythonVersionInfo as PythonVersionInfo, parse_version_string as parse_version_string, split_lines as split_lines
from typing import Dict, Iterable, Iterator, List, NamedTuple, Pattern, Set, Tuple

MAX_UNICODE: str
STRING: Incomplete
NAME: Incomplete
NUMBER: Incomplete
OP: Incomplete
NEWLINE: Incomplete
INDENT: Incomplete
DEDENT: Incomplete
ENDMARKER: Incomplete
ERRORTOKEN: Incomplete
ERROR_DEDENT: Incomplete
FSTRING_START: Incomplete
FSTRING_STRING: Incomplete
FSTRING_END: Incomplete

class TokenCollection(NamedTuple):
    pseudo_token: Pattern
    single_quoted: Set[str]
    triple_quoted: Set[str]
    endpats: Dict[str, Pattern]
    whitespace: Pattern
    fstring_pattern_map: Dict[str, str]
    always_break_tokens: Tuple[str]

BOM_UTF8_STRING: Incomplete

def group(*choices, capture: bool = False, **kwargs): ...
def maybe(*choices): ...

unicode_character_name: str
fstring_string_single_line: Incomplete
fstring_string_multi_line: Incomplete
fstring_format_spec_single_line: Incomplete
fstring_format_spec_multi_line: Incomplete

class Token(NamedTuple):
    type: PythonTokenTypes
    string: str
    start_pos: Tuple[int, int]
    prefix: str
    @property
    def end_pos(self) -> Tuple[int, int]: ...

class PythonToken(Token): ...

class FStringNode:
    quote: Incomplete
    parentheses_count: int
    previous_lines: str
    last_string_start_pos: Incomplete
    format_spec_count: int
    def __init__(self, quote) -> None: ...
    def open_parentheses(self, character) -> None: ...
    def close_parentheses(self, character) -> None: ...
    def allow_multiline(self): ...
    def is_in_expr(self): ...
    def is_in_format_spec(self): ...

def tokenize(code: str, *, version_info: PythonVersionInfo, start_pos: Tuple[int, int] = (1, 0)) -> Iterator[PythonToken]:
    """Generate tokens from a the source code (string)."""
def tokenize_lines(lines: Iterable[str], *, version_info: PythonVersionInfo, indents: List[int] = None, start_pos: Tuple[int, int] = (1, 0), is_first_token: bool = True) -> Iterator[PythonToken]:
    """
    A heavily modified Python standard library tokenizer.

    Additionally to the default information, yields also the prefix of each
    token. This idea comes from lib2to3. The prefix contains all information
    that is irrelevant for the parser like newlines in parentheses or comments.
    """
