from _typeshed import Incomplete
from sqlalchemy import Index as Index, Table as Table, __version__, create_mock_engine as create_mock_engine, sql
from sqlalchemy.engine import Connection as Connection, Dialect as Dialect, Transaction as Transaction
from sqlalchemy.engine.reflection import Inspector as Inspector
from sqlalchemy.sql.base import ColumnCollection as ColumnCollection
from sqlalchemy.sql.compiler import SQLCompiler as SQLCompiler
from sqlalchemy.sql.dml import Insert as Insert
from sqlalchemy.sql.elements import BindParameter, ColumnElement as ColumnElement, TextClause
from sqlalchemy.sql.schema import Constraint as Constraint, SchemaItem as SchemaItem
from sqlalchemy.sql.selectable import Select as Select, TableClause as TableClause
from typing_extensions import TypeGuard

sqla_13: Incomplete
sqla_14: Incomplete
sqla_14_18: Incomplete
sqla_14_26: Incomplete
sqla_2: Incomplete
sqlalchemy_version = __version__

class _Unsupported:
    """Placeholder for unsupported SQLAlchemy classes"""
class Computed(_Unsupported): ...

has_computed: bool
has_computed_reflection: bool

class Identity(_Unsupported): ...

has_identity: bool

def constraint_name_defined(name: _ConstraintName) -> TypeGuard[_ConstraintNameDefined]: ...
def constraint_name_string(name: _ConstraintName) -> TypeGuard[str]: ...
def constraint_name_or_none(name: _ConstraintName) -> str | None: ...

AUTOINCREMENT_DEFAULT: str

def url_render_as_string(url, hide_password: bool = True): ...

class _textual_index_element(sql.ColumnElement):
    """Wrap around a sqlalchemy text() construct in such a way that
    we appear like a column-oriented SQL expression to an Index
    construct.

    The issue here is that currently the Postgresql dialect, the biggest
    recipient of functional indexes, keys all the index expressions to
    the corresponding column expressions when rendering CREATE INDEX,
    so the Index we create here needs to have a .columns collection that
    is the same length as the .expressions collection.  Ultimately
    SQLAlchemy should support text() expressions in indexes.

    See SQLAlchemy issue 3174.

    """
    __visit_name__: str
    table: Incomplete
    text: Incomplete
    key: Incomplete
    fake_column: Incomplete
    def __init__(self, table: Table, text: TextClause) -> None: ...
    def get_children(self): ...

class _literal_bindparam(BindParameter): ...

def is_expression_index(index: Index) -> bool: ...
