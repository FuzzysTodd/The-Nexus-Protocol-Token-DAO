import abc
from _typeshed import Incomplete
from pypika.terms import Function as Function
from pypika.utils import format_alias_sql as format_alias_sql

class _AbstractSearchString(Function, metaclass=abc.ABCMeta):
    def __init__(self, name, pattern: str, alias: str = None) -> None: ...
    @classmethod
    @abc.abstractmethod
    def clickhouse_function(cls) -> str: ...
    def get_sql(self, with_alias: bool = False, with_namespace: bool = False, quote_char: Incomplete | None = None, dialect: Incomplete | None = None, **kwargs): ...

class Match(_AbstractSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class Like(_AbstractSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class NotLike(_AbstractSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class _AbstractMultiSearchString(Function, metaclass=abc.ABCMeta):
    def __init__(self, name, patterns: list, alias: str = None) -> None: ...
    @classmethod
    @abc.abstractmethod
    def clickhouse_function(cls) -> str: ...
    def get_sql(self, with_alias: bool = False, with_namespace: bool = False, quote_char: Incomplete | None = None, dialect: Incomplete | None = None, **kwargs): ...

class MultiSearchAny(_AbstractMultiSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class MultiMatchAny(_AbstractMultiSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...
