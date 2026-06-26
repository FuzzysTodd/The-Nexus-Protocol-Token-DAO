from .. import util as util
from ..autogenerate import render as render
from ..autogenerate.api import AutogenContext as AutogenContext
from ..operations import ops as ops, schemaobj as schemaobj
from ..operations.base import BatchOperations as BatchOperations, Operations as Operations
from ..runtime.migration import MigrationContext as MigrationContext
from ..util import sqla_compat as sqla_compat
from .base import AlterColumn as AlterColumn, ColumnComment as ColumnComment, IdentityColumnDefault as IdentityColumnDefault, RenameTable as RenameTable, _ServerDefault, alter_column as alter_column, alter_table as alter_table, compiles as compiles, format_column_name as format_column_name, format_table_name as format_table_name, format_type as format_type
from .impl import DefaultImpl as DefaultImpl
from _typeshed import Incomplete
from sqlalchemy import Index as Index, UniqueConstraint as UniqueConstraint
from sqlalchemy.dialects.postgresql import ExcludeConstraint
from sqlalchemy.dialects.postgresql.array import ARRAY as ARRAY
from sqlalchemy.dialects.postgresql.base import PGDDLCompiler as PGDDLCompiler
from sqlalchemy.dialects.postgresql.hstore import HSTORE as HSTORE
from sqlalchemy.dialects.postgresql.json import JSON as JSON, JSONB as JSONB
from sqlalchemy.sql.elements import BinaryExpression as BinaryExpression, ClauseElement as ClauseElement, ColumnClause, quoted_name as quoted_name
from sqlalchemy.sql.schema import MetaData as MetaData, Table as Table
from sqlalchemy.sql.type_api import TypeEngine as TypeEngine
from typing import Any, Dict, Literal, Sequence, Tuple

log: Incomplete

class PostgresqlImpl(DefaultImpl):
    __dialect__: str
    transactional_ddl: bool
    type_synonyms: Incomplete
    identity_attrs_ignore: Incomplete
    def create_index(self, index: Index, **kw: Any) -> None: ...
    def prep_table_for_batch(self, batch_impl, table) -> None: ...
    def compare_server_default(self, inspector_column, metadata_column, rendered_metadata_default, rendered_inspector_default): ...
    def alter_column(self, table_name: str, column_name: str, nullable: bool | None = None, server_default: _ServerDefault | Literal[False] = False, name: str | None = None, type_: TypeEngine | None = None, schema: str | None = None, autoincrement: bool | None = None, existing_type: TypeEngine | None = None, existing_server_default: _ServerDefault | None = None, existing_nullable: bool | None = None, existing_autoincrement: bool | None = None, **kw: Any) -> None: ...
    def autogen_column_reflect(self, inspector, table, column_info) -> None: ...
    def correct_for_autogen_constraints(self, conn_unique_constraints, conn_indexes, metadata_unique_constraints, metadata_indexes) -> None: ...
    def create_index_sig(self, index: Index) -> Tuple[Any, ...]: ...
    def create_unique_constraint_sig(self, const: UniqueConstraint) -> Tuple[Any, ...]: ...
    def adjust_reflected_dialect_options(self, reflected_options: Dict[str, Any], kind: str) -> Dict[str, Any]: ...
    def render_type(self, type_: TypeEngine, autogen_context: AutogenContext) -> str | Literal[False]: ...

class PostgresqlColumnType(AlterColumn):
    type_: Incomplete
    using: Incomplete
    def __init__(self, name: str, column_name: str, type_: TypeEngine, **kw) -> None: ...

def visit_rename_table(element: RenameTable, compiler: PGDDLCompiler, **kw) -> str: ...
def visit_column_type(element: PostgresqlColumnType, compiler: PGDDLCompiler, **kw) -> str: ...
def visit_column_comment(element: ColumnComment, compiler: PGDDLCompiler, **kw) -> str: ...
def visit_identity_column(element: IdentityColumnDefault, compiler: PGDDLCompiler, **kw): ...

class CreateExcludeConstraintOp(ops.AddConstraintOp):
    """Represent a create exclude constraint operation."""
    constraint_type: str
    constraint_name: Incomplete
    table_name: Incomplete
    elements: Incomplete
    where: Incomplete
    schema: Incomplete
    kw: Incomplete
    def __init__(self, constraint_name: sqla_compat._ConstraintName, table_name: str | quoted_name, elements: Sequence[Tuple[str, str]] | Sequence[Tuple[ColumnClause[Any], str]], where: BinaryExpression | str | None = None, schema: str | None = None, _orig_constraint: ExcludeConstraint | None = None, **kw) -> None: ...
    @classmethod
    def from_constraint(cls, constraint: ExcludeConstraint) -> CreateExcludeConstraintOp: ...
    def to_constraint(self, migration_context: MigrationContext | None = None) -> ExcludeConstraint: ...
    @classmethod
    def create_exclude_constraint(cls, operations: Operations, constraint_name: str, table_name: str, *elements: Any, **kw: Any) -> Table | None:
        '''Issue an alter to create an EXCLUDE constraint using the
        current migration context.

        .. note::  This method is Postgresql specific, and additionally
           requires at least SQLAlchemy 1.0.

        e.g.::

            from alembic import op

            op.create_exclude_constraint(
                "user_excl",
                "user",
                ("period", "&&"),
                ("group", "="),
                where=("group != \'some group\'"),
            )

        Note that the expressions work the same way as that of
        the ``ExcludeConstraint`` object itself; if plain strings are
        passed, quoting rules must be applied manually.

        :param name: Name of the constraint.
        :param table_name: String name of the source table.
        :param elements: exclude conditions.
        :param where: SQL expression or SQL string with optional WHERE
         clause.
        :param deferrable: optional bool. If set, emit DEFERRABLE or
         NOT DEFERRABLE when issuing DDL for this constraint.
        :param initially: optional string. If set, emit INITIALLY <value>
         when issuing DDL for this constraint.
        :param schema: Optional schema name to operate within.

        '''
    @classmethod
    def batch_create_exclude_constraint(cls, operations: BatchOperations, constraint_name: str, *elements: Any, **kw: Any):
        '''Issue a "create exclude constraint" instruction using the
        current batch migration context.

        .. note::  This method is Postgresql specific, and additionally
           requires at least SQLAlchemy 1.0.

        .. seealso::

            :meth:`.Operations.create_exclude_constraint`

        '''
