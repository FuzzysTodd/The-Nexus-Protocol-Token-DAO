from . import base as base
from .. import util as util
from ..autogenerate.api import AutogenContext as AutogenContext
from ..operations.batch import ApplyBatchImpl as ApplyBatchImpl, BatchOperationsImpl as BatchOperationsImpl
from ..util import sqla_compat as sqla_compat
from .base import _ServerDefault
from _typeshed import Incomplete
from sqlalchemy.engine import Connection as Connection, Dialect as Dialect
from sqlalchemy.engine.cursor import CursorResult as CursorResult
from sqlalchemy.engine.reflection import Inspector as Inspector
from sqlalchemy.sql.elements import ClauseElement as ClauseElement, ColumnElement as ColumnElement, quoted_name as quoted_name
from sqlalchemy.sql.schema import Column as Column, Constraint as Constraint, ForeignKeyConstraint as ForeignKeyConstraint, Index as Index, Table as Table, UniqueConstraint as UniqueConstraint
from sqlalchemy.sql.selectable import TableClause as TableClause
from sqlalchemy.sql.type_api import TypeEngine as TypeEngine
from typing import Any, Dict, List, Literal, NamedTuple, Sequence, Set, TextIO, Tuple, Type

class ImplMeta(type):
    def __init__(cls, classname: str, bases: Tuple[Type[DefaultImpl]], dict_: Dict[str, Any]) -> None: ...

class Params(NamedTuple):
    token0: Incomplete
    tokens: Incomplete
    args: Incomplete
    kwargs: Incomplete

class DefaultImpl(metaclass=ImplMeta):
    """Provide the entrypoint for major migration operations,
    including database-specific behavioral variances.

    While individual SQL/DDL constructs already provide
    for database-specific implementations, variances here
    allow for entirely different sequences of operations
    to take place for a particular migration, such as
    SQL Server's special 'IDENTITY INSERT' step for
    bulk inserts.

    """
    __dialect__: str
    transactional_ddl: bool
    command_terminator: str
    type_synonyms: Tuple[Set[str], ...]
    type_arg_extract: Sequence[str]
    identity_attrs_ignore: Tuple[str, ...]
    dialect: Incomplete
    connection: Incomplete
    as_sql: Incomplete
    literal_binds: Incomplete
    output_buffer: Incomplete
    memo: Incomplete
    context_opts: Incomplete
    def __init__(self, dialect: Dialect, connection: Connection | None, as_sql: bool, transactional_ddl: bool | None, output_buffer: TextIO | None, context_opts: Dict[str, Any]) -> None: ...
    @classmethod
    def get_by_dialect(cls, dialect: Dialect) -> Type[DefaultImpl]: ...
    def static_output(self, text: str) -> None: ...
    def requires_recreate_in_batch(self, batch_op: BatchOperationsImpl) -> bool:
        """Return True if the given :class:`.BatchOperationsImpl`
        would need the table to be recreated and copied in order to
        proceed.

        Normally, only returns True on SQLite when operations other
        than add_column are present.

        """
    def prep_table_for_batch(self, batch_impl: ApplyBatchImpl, table: Table) -> None:
        """perform any operations needed on a table before a new
        one is created to replace it in batch mode.

        the PG dialect uses this to drop constraints on the table
        before the new one uses those same names.

        """
    @property
    def bind(self) -> Connection | None: ...
    def execute(self, sql: ClauseElement | str, execution_options: dict[str, Any] | None = None) -> None: ...
    def alter_column(self, table_name: str, column_name: str, nullable: bool | None = None, server_default: _ServerDefault | Literal[False] = False, name: str | None = None, type_: TypeEngine | None = None, schema: str | None = None, autoincrement: bool | None = None, comment: str | Literal[False] | None = False, existing_comment: str | None = None, existing_type: TypeEngine | None = None, existing_server_default: _ServerDefault | None = None, existing_nullable: bool | None = None, existing_autoincrement: bool | None = None, **kw: Any) -> None: ...
    def add_column(self, table_name: str, column: Column[Any], schema: str | quoted_name | None = None) -> None: ...
    def drop_column(self, table_name: str, column: Column[Any], schema: str | None = None, **kw) -> None: ...
    def add_constraint(self, const: Any) -> None: ...
    def drop_constraint(self, const: Constraint) -> None: ...
    def rename_table(self, old_table_name: str, new_table_name: str | quoted_name, schema: str | quoted_name | None = None) -> None: ...
    def create_table(self, table: Table) -> None: ...
    def drop_table(self, table: Table) -> None: ...
    def create_index(self, index: Index, **kw: Any) -> None: ...
    def create_table_comment(self, table: Table) -> None: ...
    def drop_table_comment(self, table: Table) -> None: ...
    def create_column_comment(self, column: ColumnElement[Any]) -> None: ...
    def drop_index(self, index: Index, **kw: Any) -> None: ...
    def bulk_insert(self, table: TableClause | Table, rows: List[dict], multiinsert: bool = True) -> None: ...
    def compare_type(self, inspector_column: Column[Any], metadata_column: Column) -> bool:
        """Returns True if there ARE differences between the types of the two
        columns. Takes impl.type_synonyms into account between retrospected
        and metadata types
        """
    def compare_server_default(self, inspector_column, metadata_column, rendered_metadata_default, rendered_inspector_default): ...
    def correct_for_autogen_constraints(self, conn_uniques: Set[UniqueConstraint], conn_indexes: Set[Index], metadata_unique_constraints: Set[UniqueConstraint], metadata_indexes: Set[Index]) -> None: ...
    def cast_for_batch_migrate(self, existing, existing_transfer, new_type) -> None: ...
    def render_ddl_sql_expr(self, expr: ClauseElement, is_server_default: bool = False, **kw: Any) -> str:
        """Render a SQL expression that is typically a server default,
        index expression, etc.

        """
    def correct_for_autogen_foreignkeys(self, conn_fks: Set[ForeignKeyConstraint], metadata_fks: Set[ForeignKeyConstraint]) -> None: ...
    def autogen_column_reflect(self, inspector, table, column_info) -> None:
        """A hook that is attached to the 'column_reflect' event for when
        a Table is reflected from the database during the autogenerate
        process.

        Dialects can elect to modify the information gathered here.

        """
    def start_migrations(self) -> None:
        """A hook called when :meth:`.EnvironmentContext.run_migrations`
        is called.

        Implementations can set up per-migration-run state here.

        """
    def emit_begin(self) -> None:
        """Emit the string ``BEGIN``, or the backend-specific
        equivalent, on the current connection context.

        This is used in offline mode and typically
        via :meth:`.EnvironmentContext.begin_transaction`.

        """
    def emit_commit(self) -> None:
        """Emit the string ``COMMIT``, or the backend-specific
        equivalent, on the current connection context.

        This is used in offline mode and typically
        via :meth:`.EnvironmentContext.begin_transaction`.

        """
    def render_type(self, type_obj: TypeEngine, autogen_context: AutogenContext) -> str | Literal[False]: ...
    def create_index_sig(self, index: Index) -> Tuple[Any, ...]: ...
    def create_unique_constraint_sig(self, const: UniqueConstraint) -> Tuple[Any, ...]: ...
    def adjust_reflected_dialect_options(self, reflected_object: Dict[str, Any], kind: str) -> Dict[str, Any]: ...
