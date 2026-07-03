from _typeshed import Incomplete
from sqlparse import sql as sql

class RightMarginFilter:
    keep_together: Incomplete
    width: Incomplete
    line: str
    def __init__(self, width: int = 79) -> None: ...
    def process(self, group) -> None: ...
