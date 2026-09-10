from .. import util as util
from ..autogenerate import compare as compare
from ..util import sqla_compat as sqla_compat
from .base import AlterColumn as AlterColumn, ColumnDefault as ColumnDefault, ColumnName as ColumnName, ColumnNullable as ColumnNullable, ColumnType as ColumnType, _ServerDefault, alter_table as alter_table, format_column_name as format_column_name, format_server_default as format_server_default
from .impl import DefaultImpl as DefaultImpl
from _typeshed import Incomplete
from sqlalchemy.dialects.mysql.base import MySQLDDLCompiler as MySQLDDLCompiler
from sqlalchemy.sql.ddl import DropConstraint as DropConstraint
from sqlalchemy.sql.schema import Constraint as Constraint
from sqlalchemy.sql.type_api import TypeEngine as TypeEngine
from typing import Any, Literal

class MySQLImpl(DefaultImpl):
    __dialect__: str
    transactional_ddl: bool
    type_synonyms: Incomplete
    type_arg_extract: Incomplete
    def alter_column(self, table_name: str, column_name: str, nullable: bool | None = None, server_default: _ServerDefault | Literal[False] = False, name: str | None = None, type_: TypeEngine | None = None, schema: str | None = None, existing_type: TypeEngine | None = None, existing_server_default: _ServerDefault | None = None, existing_nullable: bool | None = None, autoincrement: bool | None = None, existing_autoincrement: bool | None = None, comment: str | Literal[False] | None = False, existing_comment: str | None = None, **kw: Any) -> None: ...
    def drop_constraint(self, const: Constraint) -> None: ...
    def compare_server_default(self, inspector_column, metadata_column, rendered_metadata_default, rendered_inspector_default): ...
    def correct_for_autogen_constraints(self, conn_unique_constraints, conn_indexes, metadata_unique_constraints, metadata_indexes) -> None: ...
    def correct_for_autogen_foreignkeys(self, conn_fks, metadata_fks) -> None: ...

class MariaDBImpl(MySQLImpl):
    __dialect__: str

class MySQLAlterDefault(AlterColumn):
    column_name: Incomplete
    default: Incomplete
    def __init__(self, name: str, column_name: str, default: _ServerDefault, schema: str | None = None) -> None: ...

class MySQLChangeColumn(AlterColumn):
    column_name: Incomplete
    nullable: Incomplete
    newname: Incomplete
    default: Incomplete
    autoincrement: Incomplete
    comment: Incomplete
    type_: Incomplete
    def __init__(self, name: str, column_name: str, schema: str | None = None, newname: str | None = None, type_: TypeEngine | None = None, nullable: bool | None = None, default: _ServerDefault | Literal[False] | None = False, autoincrement: bool | None = None, comment: str | Literal[False] | None = False) -> None: ...

class MySQLModifyColumn(MySQLChangeColumn): ...
