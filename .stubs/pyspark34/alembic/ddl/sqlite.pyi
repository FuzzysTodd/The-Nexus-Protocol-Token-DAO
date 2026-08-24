from .. import util as util
from ..operations.batch import BatchOperationsImpl as BatchOperationsImpl
from .base import RenameTable as RenameTable, alter_table as alter_table, format_table_name as format_table_name
from .impl import DefaultImpl as DefaultImpl
from sqlalchemy.engine.reflection import Inspector as Inspector
from sqlalchemy.sql.compiler import DDLCompiler as DDLCompiler
from sqlalchemy.sql.elements import Cast as Cast, ClauseElement as ClauseElement
from sqlalchemy.sql.schema import Column as Column, Constraint as Constraint, Table as Table
from sqlalchemy.sql.type_api import TypeEngine as TypeEngine
from typing import Any, Dict

class SQLiteImpl(DefaultImpl):
    __dialect__: str
    transactional_ddl: bool
    def requires_recreate_in_batch(self, batch_op: BatchOperationsImpl) -> bool:
        """Return True if the given :class:`.BatchOperationsImpl`
        would need the table to be recreated and copied in order to
        proceed.

        Normally, only returns True on SQLite when operations other
        than add_column are present.

        """
    def add_constraint(self, const: Constraint): ...
    def drop_constraint(self, const: Constraint): ...
    def compare_server_default(self, inspector_column: Column[Any], metadata_column: Column[Any], rendered_metadata_default: str | None, rendered_inspector_default: str | None) -> bool: ...
    def autogen_column_reflect(self, inspector: Inspector, table: Table, column_info: Dict[str, Any]) -> None: ...
    def render_ddl_sql_expr(self, expr: ClauseElement, is_server_default: bool = False, **kw) -> str: ...
    def cast_for_batch_migrate(self, existing: Column[Any], existing_transfer: Dict[str, TypeEngine | Cast], new_type: TypeEngine) -> None: ...
    def correct_for_autogen_constraints(self, conn_unique_constraints, conn_indexes, metadata_unique_constraints, metadata_indexes) -> None: ...

def visit_rename_table(element: RenameTable, compiler: DDLCompiler, **kw) -> str: ...
