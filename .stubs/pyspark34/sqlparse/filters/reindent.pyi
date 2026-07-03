from _typeshed import Incomplete
from sqlparse import sql as sql
from sqlparse.utils import indent as indent, offset as offset

class ReindentFilter:
    n: Incomplete
    width: Incomplete
    char: Incomplete
    indent: Incomplete
    offset: int
    wrap_after: Incomplete
    comma_first: Incomplete
    indent_columns: Incomplete
    def __init__(self, width: int = 2, char: str = ' ', wrap_after: int = 0, n: str = '\n', comma_first: bool = False, indent_after_first: bool = False, indent_columns: bool = False) -> None: ...
    @property
    def leading_ws(self): ...
    def nl(self, offset: int = 0): ...
    def process(self, stmt): ...
