import abc
from _typeshed import Incomplete
from pypika.terms import Field as Field, Function as Function, Term as Term
from pypika.utils import format_alias_sql as format_alias_sql

class Array(Term):
    def __init__(self, values: list, converter_cls: Incomplete | None = None, converter_options: dict = None, alias: str = None) -> None: ...
    def get_sql(self): ...

class HasAny(Function):
    alias: Incomplete
    schema: Incomplete
    args: Incomplete
    name: str
    def __init__(self, left_array: None, right_array: None, alias: str = None, schema: str = None) -> None: ...
    def get_sql(self, with_alias: bool = False, with_namespace: bool = False, quote_char: Incomplete | None = None, dialect: Incomplete | None = None, **kwargs): ...

class _AbstractArrayFunction(Function, metaclass=abc.ABCMeta):
    schema: Incomplete
    alias: Incomplete
    name: Incomplete
    def __init__(self, array: None, alias: str = None, schema: str = None) -> None: ...
    def get_sql(self, with_namespace: bool = False, quote_char: Incomplete | None = None, dialect: Incomplete | None = None, **kwargs): ...
    @classmethod
    @abc.abstractmethod
    def clickhouse_function(cls) -> str: ...

class NotEmpty(_AbstractArrayFunction):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class Empty(_AbstractArrayFunction):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class Length(_AbstractArrayFunction):
    @classmethod
    def clickhouse_function(cls) -> str: ...
