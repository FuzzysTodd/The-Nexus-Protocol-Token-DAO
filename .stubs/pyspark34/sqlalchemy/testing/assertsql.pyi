from .. import event as event
from ..engine import url as url
from ..engine.default import DefaultDialect as DefaultDialect
from ..schema import BaseDDLElement as BaseDDLElement
from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

class AssertRule:
    is_consumed: bool
    errormessage: Incomplete
    consume_statement: bool
    def process_statement(self, execute_observed) -> None: ...
    def no_more_statements(self) -> None: ...

class SQLMatchRule(AssertRule): ...

class CursorSQL(SQLMatchRule):
    statement: Incomplete
    params: Incomplete
    consume_statement: Incomplete
    def __init__(self, statement, params: Incomplete | None = None, consume_statement: bool = True) -> None: ...
    errormessage: Incomplete
    is_consumed: bool
    def process_statement(self, execute_observed) -> None: ...

class CompiledSQL(SQLMatchRule):
    statement: Incomplete
    params: Incomplete
    dialect: Incomplete
    enable_returning: Incomplete
    def __init__(self, statement, params: Incomplete | None = None, dialect: str = 'default', enable_returning: bool = True) -> None: ...
    is_consumed: bool
    errormessage: Incomplete
    def process_statement(self, execute_observed) -> None: ...

class RegexSQL(CompiledSQL):
    regex: Incomplete
    orig_regex: Incomplete
    params: Incomplete
    dialect: Incomplete
    enable_returning: Incomplete
    def __init__(self, regex, params: Incomplete | None = None, dialect: str = 'default', enable_returning: bool = False) -> None: ...

class DialectSQL(CompiledSQL): ...

class CountStatements(AssertRule):
    count: Incomplete
    def __init__(self, count) -> None: ...
    def process_statement(self, execute_observed) -> None: ...
    def no_more_statements(self) -> None: ...

class AllOf(AssertRule):
    rules: Incomplete
    def __init__(self, *rules) -> None: ...
    is_consumed: bool
    errormessage: Incomplete
    def process_statement(self, execute_observed) -> None: ...

class EachOf(AssertRule):
    rules: Incomplete
    def __init__(self, *rules) -> None: ...
    is_consumed: bool
    consume_statement: bool
    errormessage: Incomplete
    def process_statement(self, execute_observed) -> None: ...
    def no_more_statements(self) -> None: ...

class Conditional(EachOf):
    def __init__(self, condition, rules, else_rules) -> None: ...

class Or(AllOf):
    is_consumed: bool
    errormessage: Incomplete
    def process_statement(self, execute_observed) -> None: ...

class SQLExecuteObserved:
    context: Incomplete
    clauseelement: Incomplete
    parameters: Incomplete
    statements: Incomplete
    def __init__(self, context, clauseelement, multiparams, params) -> None: ...

class SQLCursorExecuteObserved(NamedTuple('SQLCursorExecuteObserved', [('statement', Incomplete), ('parameters', Incomplete), ('context', Incomplete), ('executemany', Incomplete)])): ...

class SQLAsserter:
    accumulated: Incomplete
    def __init__(self) -> None: ...
    def assert_(self, *rules) -> None: ...

def assert_engine(engine) -> Generator[Incomplete, None, None]: ...
