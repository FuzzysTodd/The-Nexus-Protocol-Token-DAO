from _typeshed import Incomplete
from collections.abc import Generator
from sqlparse import lexer as lexer
from sqlparse.engine import grouping as grouping
from sqlparse.engine.statement_splitter import StatementSplitter as StatementSplitter

class FilterStack:
    preprocess: Incomplete
    stmtprocess: Incomplete
    postprocess: Incomplete
    def __init__(self) -> None: ...
    def enable_grouping(self) -> None: ...
    def run(self, sql, encoding: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
