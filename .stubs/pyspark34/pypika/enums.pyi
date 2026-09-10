from _typeshed import Incomplete
from enum import Enum
from typing import Any

class Arithmetic(Enum):
    add: str
    sub: str
    mul: str
    div: str
    lshift: str
    rshift: str

class Comparator(Enum): ...

class Equality(Comparator):
    eq: str
    ne: str
    gt: str
    gte: str
    lt: str
    lte: str

class Matching(Comparator):
    not_like: str
    like: str
    not_ilike: str
    ilike: str
    rlike: str
    regex: str
    regexp: str
    bin_regex: str
    as_of: str
    glob: str

class Boolean(Comparator):
    and_: str
    or_: str
    xor_: str
    true: str
    false: str

class Order(Enum):
    asc: str
    desc: str

class JoinType(Enum):
    inner: str
    left: str
    right: str
    outer: str
    left_outer: str
    right_outer: str
    full_outer: str
    cross: str
    hash: str

class ReferenceOption(Enum):
    cascade: str
    no_action: str
    restrict: str
    set_null: str
    set_default: str

class SetOperation(Enum):
    union: str
    union_all: str
    intersect: str
    except_of: str
    minus: str

class DatePart(Enum):
    year: str
    quarter: str
    month: str
    week: str
    day: str
    hour: str
    minute: str
    second: str
    microsecond: str

class SqlType:
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def __call__(self, length: int) -> SqlTypeLength: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class SqlTypeLength:
    name: Incomplete
    length: Incomplete
    def __init__(self, name: str, length: int) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class SqlTypes:
    BOOLEAN: str
    INTEGER: str
    FLOAT: str
    NUMERIC: str
    SIGNED: str
    UNSIGNED: str
    DATE: str
    TIME: str
    TIMESTAMP: str
    CHAR: Incomplete
    VARCHAR: Incomplete
    LONG_VARCHAR: Incomplete
    BINARY: Incomplete
    VARBINARY: Incomplete
    LONG_VARBINARY: Incomplete

class Dialects(Enum):
    VERTICA: str
    CLICKHOUSE: str
    ORACLE: str
    MSSQL: str
    MYSQL: str
    POSTGRESQL: str
    REDSHIFT: str
    SQLLITE: str
    SNOWFLAKE: str

class JSONOperators(Enum):
    HAS_KEY: str
    CONTAINS: str
    CONTAINED_BY: str
    HAS_KEYS: str
    HAS_ANY_KEYS: str
    GET_JSON_VALUE: str
    GET_TEXT_VALUE: str
    GET_PATH_JSON_VALUE: str
    GET_PATH_TEXT_VALUE: str
