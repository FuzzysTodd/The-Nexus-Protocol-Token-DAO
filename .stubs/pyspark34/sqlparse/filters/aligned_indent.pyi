from _typeshed import Incomplete
from sqlparse import sql as sql
from sqlparse.utils import indent as indent, offset as offset

class AlignedIndentFilter:
    join_words: str
    by_words: str
    split_words: Incomplete
    n: Incomplete
    offset: int
    indent: int
    char: Incomplete
    def __init__(self, char: str = ' ', n: str = '\n') -> None: ...
    def nl(self, offset: int = 1): ...
    def process(self, stmt): ...
