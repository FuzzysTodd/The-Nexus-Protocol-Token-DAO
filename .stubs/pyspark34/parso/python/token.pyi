from _typeshed import Incomplete
from enum import Enum

class TokenType:
    name: str
    contains_syntax: bool
    def __init__(self, name: str, contains_syntax: bool = False) -> None: ...

class PythonTokenTypes(Enum):
    STRING: Incomplete
    NUMBER: Incomplete
    NAME: Incomplete
    ERRORTOKEN: Incomplete
    NEWLINE: Incomplete
    INDENT: Incomplete
    DEDENT: Incomplete
    ERROR_DEDENT: Incomplete
    FSTRING_STRING: Incomplete
    FSTRING_START: Incomplete
    FSTRING_END: Incomplete
    OP: Incomplete
    ENDMARKER: Incomplete
