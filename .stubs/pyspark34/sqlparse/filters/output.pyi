from _typeshed import Incomplete
from sqlparse import sql as sql

class OutputFilter:
    varname_prefix: str
    varname: Incomplete
    count: int
    def __init__(self, varname: str = 'sql') -> None: ...
    def process(self, stmt): ...

class OutputPythonFilter(OutputFilter): ...

class OutputPHPFilter(OutputFilter):
    varname_prefix: str
