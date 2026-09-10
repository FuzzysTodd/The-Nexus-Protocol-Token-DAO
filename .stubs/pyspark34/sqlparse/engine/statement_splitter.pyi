from _typeshed import Incomplete
from collections.abc import Generator
from sqlparse import sql as sql

class StatementSplitter:
    """Filter that split stream at individual statements"""
    def __init__(self) -> None: ...
    consume_ws: bool
    def process(self, stream) -> Generator[Incomplete, None, None]:
        """Process the stream"""
