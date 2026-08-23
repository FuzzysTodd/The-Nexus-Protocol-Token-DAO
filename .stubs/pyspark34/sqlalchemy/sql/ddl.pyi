import typing
from . import roles as roles
from .. import exc as exc, util as util
from ..engine.base import Connection as Connection
from ..engine.interfaces import CacheStats as CacheStats, CompiledCacheType as CompiledCacheType, Dialect as Dialect, SchemaTranslateMapType as SchemaTranslateMapType
from ..util import topological as topological
from ..util.typing import Protocol as Protocol, Self as Self
from .base import Executable as Executable, SchemaVisitor as SchemaVisitor
from .compiler import Compiled as Compiled, DDLCompiler as DDLCompiler
from .elements import BindParameter as BindParameter, ClauseElement as ClauseElement
from .schema import Constraint as Constraint, ForeignKeyConstraint as ForeignKeyConstraint, SchemaItem as SchemaItem, Sequence as Sequence, Table as Table
from .selectable import TableClause as TableClause
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Callable, Iterable, List, Sequence as typing_Sequence, Tuple

class BaseDDLElement(ClauseElement):
    '''The root of DDL constructs, including those that are sub-elements
    within the "create table" and other processes.

    .. versionadded:: 2.0

    '''

class DDLIfCallable(Protocol):
    def __call__(self, ddl: BaseDDLElement, target: SchemaItem, bind: Connection | None, tables: List[Table] | None = None, state: Any | None = None, *, dialect: Dialect, compiler: DDLCompiler | None = ..., checkfirst: bool) -> bool: ...

class DDLIf(typing.NamedTuple):
    dialect: str | None
    callable_: DDLIfCallable | None
    state: Any | None

class ExecutableDDLElement(roles.DDLRole, Executable, BaseDDLElement):
    """Base class for standalone executable DDL expression constructs.

    This class is the base for the general purpose :class:`.DDL` class,
    as well as the various create/drop clause constructs such as
    :class:`.CreateTable`, :class:`.DropTable`, :class:`.AddConstraint`,
    etc.

    .. versionchanged:: 2.0  :class:`.ExecutableDDLElement` is renamed from
       :class:`.DDLElement`, which still exists for backwards compatibility.

    :class:`.ExecutableDDLElement` integrates closely with SQLAlchemy events,
    introduced in :ref:`event_toplevel`.  An instance of one is
    itself an event receiving callable::

        event.listen(
            users,
            'after_create',
            AddConstraint(constraint).execute_if(dialect='postgresql')
        )

    .. seealso::

        :class:`.DDL`

        :class:`.DDLEvents`

        :ref:`event_toplevel`

        :ref:`schema_ddl_sequences`

    """
    target: SchemaItem | None
    def against(self, target: SchemaItem) -> Self:
        '''Return a copy of this :class:`_schema.ExecutableDDLElement` which
        will include the given target.

        This essentially applies the given item to the ``.target`` attribute of
        the returned :class:`_schema.ExecutableDDLElement` object. This target
        is then usable by event handlers and compilation routines in order to
        provide services such as tokenization of a DDL string in terms of a
        particular :class:`_schema.Table`.

        When a :class:`_schema.ExecutableDDLElement` object is established as
        an event handler for the :meth:`_events.DDLEvents.before_create` or
        :meth:`_events.DDLEvents.after_create` events, and the event then
        occurs for a given target such as a :class:`_schema.Constraint` or
        :class:`_schema.Table`, that target is established with a copy of the
        :class:`_schema.ExecutableDDLElement` object using this method, which
        then proceeds to the :meth:`_schema.ExecutableDDLElement.execute`
        method in order to invoke the actual DDL instruction.

        :param target: a :class:`_schema.SchemaItem` that will be the subject
         of a DDL operation.

        :return: a copy of this :class:`_schema.ExecutableDDLElement` with the
         ``.target`` attribute assigned to the given
         :class:`_schema.SchemaItem`.

        .. seealso::

            :class:`_schema.DDL` - uses tokenization against the "target" when
            processing the DDL string.

        '''
    def execute_if(self, dialect: str | None = None, callable_: DDLIfCallable | None = None, state: Any | None = None) -> Self:
        '''Return a callable that will execute this
        :class:`_ddl.ExecutableDDLElement` conditionally within an event
        handler.

        Used to provide a wrapper for event listening::

            event.listen(
                        metadata,
                        \'before_create\',
                        DDL("my_ddl").execute_if(dialect=\'postgresql\')
                    )

        :param dialect: May be a string or tuple of strings.
          If a string, it will be compared to the name of the
          executing database dialect::

            DDL(\'something\').execute_if(dialect=\'postgresql\')

          If a tuple, specifies multiple dialect names::

            DDL(\'something\').execute_if(dialect=(\'postgresql\', \'mysql\'))

        :param callable\\_: A callable, which will be invoked with
          three positional arguments as well as optional keyword
          arguments:

            :ddl:
              This DDL element.

            :target:
              The :class:`_schema.Table` or :class:`_schema.MetaData`
              object which is the
              target of this event. May be None if the DDL is executed
              explicitly.

            :bind:
              The :class:`_engine.Connection` being used for DDL execution.
              May be None if this construct is being created inline within
              a table, in which case ``compiler`` will be present.

            :tables:
              Optional keyword argument - a list of Table objects which are to
              be created/ dropped within a MetaData.create_all() or drop_all()
              method call.

            :dialect: keyword argument, but always present - the
              :class:`.Dialect` involved in the operation.

            :compiler: keyword argument.  Will be ``None`` for an engine
              level DDL invocation, but will refer to a :class:`.DDLCompiler`
              if this DDL element is being created inline within a table.

            :state:
              Optional keyword argument - will be the ``state`` argument
              passed to this function.

            :checkfirst:
             Keyword argument, will be True if the \'checkfirst\' flag was
             set during the call to ``create()``, ``create_all()``,
             ``drop()``, ``drop_all()``.

          If the callable returns a True value, the DDL statement will be
          executed.

        :param state: any value which will be passed to the callable\\_
          as the ``state`` keyword argument.

        .. seealso::

            :meth:`.SchemaItem.ddl_if`

            :class:`.DDLEvents`

            :ref:`event_toplevel`

        '''
    def __call__(self, target, bind, **kw) -> None:
        """Execute the DDL as a ddl_listener."""
DDLElement = ExecutableDDLElement

class DDL(ExecutableDDLElement):
    '''A literal DDL statement.

    Specifies literal SQL DDL to be executed by the database.  DDL objects
    function as DDL event listeners, and can be subscribed to those events
    listed in :class:`.DDLEvents`, using either :class:`_schema.Table` or
    :class:`_schema.MetaData` objects as targets.
    Basic templating support allows
    a single DDL instance to handle repetitive tasks for multiple tables.

    Examples::

      from sqlalchemy import event, DDL

      tbl = Table(\'users\', metadata, Column(\'uid\', Integer))
      event.listen(tbl, \'before_create\', DDL(\'DROP TRIGGER users_trigger\'))

      spow = DDL(\'ALTER TABLE %(table)s SET secretpowers TRUE\')
      event.listen(tbl, \'after_create\', spow.execute_if(dialect=\'somedb\'))

      drop_spow = DDL(\'ALTER TABLE users SET secretpowers FALSE\')
      connection.execute(drop_spow)

    When operating on Table events, the following ``statement``
    string substitutions are available::

      %(table)s  - the Table name, with any required quoting applied
      %(schema)s - the schema name, with any required quoting applied
      %(fullname)s - the Table name including schema, quoted if needed

    The DDL\'s "context", if any, will be combined with the standard
    substitutions noted above.  Keys present in the context will override
    the standard substitutions.

    '''
    __visit_name__: str
    statement: Incomplete
    context: Incomplete
    def __init__(self, statement, context: Incomplete | None = None) -> None:
        """Create a DDL statement.

        :param statement:
          A string or unicode string to be executed.  Statements will be
          processed with Python's string formatting operator using
          a fixed set of string substitutions, as well as additional
          substitutions provided by the optional :paramref:`.DDL.context`
          parameter.

          A literal '%' in a statement must be escaped as '%%'.

          SQL bind parameters are not available in DDL statements.

        :param context:
          Optional dictionary, defaults to None.  These values will be
          available for use in string substitutions on the DDL statement.

        .. seealso::

            :class:`.DDLEvents`

            :ref:`event_toplevel`

        """

class _CreateDropBase(ExecutableDDLElement):
    """Base class for DDL constructs that represent CREATE and DROP or
    equivalents.

    The common theme of _CreateDropBase is a single
    ``element`` attribute which refers to the element
    to be created or dropped.

    """
    element: Incomplete
    def __init__(self, element) -> None: ...
    @property
    def stringify_dialect(self): ...

class _CreateBase(_CreateDropBase):
    if_not_exists: Incomplete
    def __init__(self, element, if_not_exists: bool = False) -> None: ...

class _DropBase(_CreateDropBase):
    if_exists: Incomplete
    def __init__(self, element, if_exists: bool = False) -> None: ...

class CreateSchema(_CreateBase):
    """Represent a CREATE SCHEMA statement.

    The argument here is the string name of the schema.

    """
    __visit_name__: str
    stringify_dialect: str
    def __init__(self, name, if_not_exists: bool = False) -> None:
        """Create a new :class:`.CreateSchema` construct."""

class DropSchema(_DropBase):
    """Represent a DROP SCHEMA statement.

    The argument here is the string name of the schema.

    """
    __visit_name__: str
    stringify_dialect: str
    cascade: Incomplete
    def __init__(self, name, cascade: bool = False, if_exists: bool = False) -> None:
        """Create a new :class:`.DropSchema` construct."""

class CreateTable(_CreateBase):
    """Represent a CREATE TABLE statement."""
    __visit_name__: str
    columns: Incomplete
    include_foreign_key_constraints: Incomplete
    def __init__(self, element: Table, include_foreign_key_constraints: typing_Sequence[ForeignKeyConstraint] | None = None, if_not_exists: bool = False) -> None:
        """Create a :class:`.CreateTable` construct.

        :param element: a :class:`_schema.Table` that's the subject
         of the CREATE
        :param on: See the description for 'on' in :class:`.DDL`.
        :param include_foreign_key_constraints: optional sequence of
         :class:`_schema.ForeignKeyConstraint` objects that will be included
         inline within the CREATE construct; if omitted, all foreign key
         constraints that do not specify use_alter=True are included.

        :param if_not_exists: if True, an IF NOT EXISTS operator will be
         applied to the construct.

         .. versionadded:: 1.4.0b2

        """

class _DropView(_DropBase):
    '''Semi-public \'DROP VIEW\' construct.

    Used by the test suite for dialect-agnostic drops of views.
    This object will eventually be part of a public "view" API.

    '''
    __visit_name__: str

class CreateConstraint(BaseDDLElement):
    element: Incomplete
    def __init__(self, element: Constraint) -> None: ...

class CreateColumn(BaseDDLElement):
    '''Represent a :class:`_schema.Column`
    as rendered in a CREATE TABLE statement,
    via the :class:`.CreateTable` construct.

    This is provided to support custom column DDL within the generation
    of CREATE TABLE statements, by using the
    compiler extension documented in :ref:`sqlalchemy.ext.compiler_toplevel`
    to extend :class:`.CreateColumn`.

    Typical integration is to examine the incoming :class:`_schema.Column`
    object, and to redirect compilation if a particular flag or condition
    is found::

        from sqlalchemy import schema
        from sqlalchemy.ext.compiler import compiles

        @compiles(schema.CreateColumn)
        def compile(element, compiler, **kw):
            column = element.element

            if "special" not in column.info:
                return compiler.visit_create_column(element, **kw)

            text = "%s SPECIAL DIRECTIVE %s" % (
                    column.name,
                    compiler.type_compiler.process(column.type)
                )
            default = compiler.get_column_default_string(column)
            if default is not None:
                text += " DEFAULT " + default

            if not column.nullable:
                text += " NOT NULL"

            if column.constraints:
                text += " ".join(
                            compiler.process(const)
                            for const in column.constraints)
            return text

    The above construct can be applied to a :class:`_schema.Table`
    as follows::

        from sqlalchemy import Table, Metadata, Column, Integer, String
        from sqlalchemy import schema

        metadata = MetaData()

        table = Table(\'mytable\', MetaData(),
                Column(\'x\', Integer, info={"special":True}, primary_key=True),
                Column(\'y\', String(50)),
                Column(\'z\', String(20), info={"special":True})
            )

        metadata.create_all(conn)

    Above, the directives we\'ve added to the :attr:`_schema.Column.info`
    collection
    will be detected by our custom compilation scheme::

        CREATE TABLE mytable (
                x SPECIAL DIRECTIVE INTEGER NOT NULL,
                y VARCHAR(50),
                z SPECIAL DIRECTIVE VARCHAR(20),
            PRIMARY KEY (x)
        )

    The :class:`.CreateColumn` construct can also be used to skip certain
    columns when producing a ``CREATE TABLE``.  This is accomplished by
    creating a compilation rule that conditionally returns ``None``.
    This is essentially how to produce the same effect as using the
    ``system=True`` argument on :class:`_schema.Column`, which marks a column
    as an implicitly-present "system" column.

    For example, suppose we wish to produce a :class:`_schema.Table`
    which skips
    rendering of the PostgreSQL ``xmin`` column against the PostgreSQL
    backend, but on other backends does render it, in anticipation of a
    triggered rule.  A conditional compilation rule could skip this name only
    on PostgreSQL::

        from sqlalchemy.schema import CreateColumn

        @compiles(CreateColumn, "postgresql")
        def skip_xmin(element, compiler, **kw):
            if element.element.name == \'xmin\':
                return None
            else:
                return compiler.visit_create_column(element, **kw)


        my_table = Table(\'mytable\', metadata,
                    Column(\'id\', Integer, primary_key=True),
                    Column(\'xmin\', Integer)
                )

    Above, a :class:`.CreateTable` construct will generate a ``CREATE TABLE``
    which only includes the ``id`` column in the string; the ``xmin`` column
    will be omitted, but only against the PostgreSQL backend.

    '''
    __visit_name__: str
    element: Incomplete
    def __init__(self, element) -> None: ...

class DropTable(_DropBase):
    """Represent a DROP TABLE statement."""
    __visit_name__: str
    def __init__(self, element: Table, if_exists: bool = False) -> None:
        """Create a :class:`.DropTable` construct.

        :param element: a :class:`_schema.Table` that's the subject
         of the DROP.
        :param on: See the description for 'on' in :class:`.DDL`.
        :param if_exists: if True, an IF EXISTS operator will be applied to the
         construct.

         .. versionadded:: 1.4.0b2

        """

class CreateSequence(_CreateBase):
    """Represent a CREATE SEQUENCE statement."""
    __visit_name__: str
    def __init__(self, element: Sequence, if_not_exists: bool = False) -> None: ...

class DropSequence(_DropBase):
    """Represent a DROP SEQUENCE statement."""
    __visit_name__: str
    def __init__(self, element: Sequence, if_exists: bool = False) -> None: ...

class CreateIndex(_CreateBase):
    """Represent a CREATE INDEX statement."""
    __visit_name__: str
    def __init__(self, element, if_not_exists: bool = False) -> None:
        """Create a :class:`.Createindex` construct.

        :param element: a :class:`_schema.Index` that's the subject
         of the CREATE.
        :param if_not_exists: if True, an IF NOT EXISTS operator will be
         applied to the construct.

         .. versionadded:: 1.4.0b2

        """

class DropIndex(_DropBase):
    """Represent a DROP INDEX statement."""
    __visit_name__: str
    def __init__(self, element, if_exists: bool = False) -> None:
        """Create a :class:`.DropIndex` construct.

        :param element: a :class:`_schema.Index` that's the subject
         of the DROP.
        :param if_exists: if True, an IF EXISTS operator will be applied to the
         construct.

         .. versionadded:: 1.4.0b2

        """

class AddConstraint(_CreateBase):
    """Represent an ALTER TABLE ADD CONSTRAINT statement."""
    __visit_name__: str
    def __init__(self, element) -> None: ...

class DropConstraint(_DropBase):
    """Represent an ALTER TABLE DROP CONSTRAINT statement."""
    __visit_name__: str
    cascade: Incomplete
    def __init__(self, element, cascade: bool = False, if_exists: bool = False, **kw) -> None: ...

class SetTableComment(_CreateDropBase):
    """Represent a COMMENT ON TABLE IS statement."""
    __visit_name__: str

class DropTableComment(_CreateDropBase):
    """Represent a COMMENT ON TABLE '' statement.

    Note this varies a lot across database backends.

    """
    __visit_name__: str

class SetColumnComment(_CreateDropBase):
    """Represent a COMMENT ON COLUMN IS statement."""
    __visit_name__: str

class DropColumnComment(_CreateDropBase):
    """Represent a COMMENT ON COLUMN IS NULL statement."""
    __visit_name__: str

class SetConstraintComment(_CreateDropBase):
    """Represent a COMMENT ON CONSTRAINT IS statement."""
    __visit_name__: str

class DropConstraintComment(_CreateDropBase):
    """Represent a COMMENT ON CONSTRAINT IS NULL statement."""
    __visit_name__: str

class InvokeDDLBase(SchemaVisitor):
    connection: Incomplete
    def __init__(self, connection) -> None: ...
    def with_ddl_events(self, target, **kw) -> None:
        """helper context manager that will apply appropriate DDL events
        to a CREATE or DROP operation."""

class InvokeCreateDDLBase(InvokeDDLBase):
    def with_ddl_events(self, target, **kw) -> Generator[None, None, None]:
        """helper context manager that will apply appropriate DDL events
        to a CREATE or DROP operation."""

class InvokeDropDDLBase(InvokeDDLBase):
    def with_ddl_events(self, target, **kw) -> Generator[None, None, None]:
        """helper context manager that will apply appropriate DDL events
        to a CREATE or DROP operation."""

class SchemaGenerator(InvokeCreateDDLBase):
    checkfirst: Incomplete
    tables: Incomplete
    preparer: Incomplete
    dialect: Incomplete
    memo: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = False, tables: Incomplete | None = None, **kwargs) -> None: ...
    def visit_metadata(self, metadata) -> None: ...
    def visit_table(self, table, create_ok: bool = False, include_foreign_key_constraints: Incomplete | None = None, _is_metadata_operation: bool = False) -> None: ...
    def visit_foreign_key_constraint(self, constraint) -> None: ...
    def visit_sequence(self, sequence, create_ok: bool = False) -> None: ...
    def visit_index(self, index, create_ok: bool = False) -> None: ...

class SchemaDropper(InvokeDropDDLBase):
    checkfirst: Incomplete
    tables: Incomplete
    preparer: Incomplete
    dialect: Incomplete
    memo: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = False, tables: Incomplete | None = None, **kwargs) -> None: ...
    def visit_metadata(self, metadata): ...
    def visit_index(self, index, drop_ok: bool = False) -> None: ...
    def visit_table(self, table, drop_ok: bool = False, _is_metadata_operation: bool = False, _ignore_sequences=()) -> None: ...
    def visit_foreign_key_constraint(self, constraint) -> None: ...
    def visit_sequence(self, sequence, drop_ok: bool = False) -> None: ...

def sort_tables(tables: Iterable[TableClause], skip_fn: Callable[[ForeignKeyConstraint], bool] | None = None, extra_dependencies: typing_Sequence[Tuple[TableClause, TableClause]] | None = None) -> List[Table]:
    """Sort a collection of :class:`_schema.Table` objects based on
    dependency.

    This is a dependency-ordered sort which will emit :class:`_schema.Table`
    objects such that they will follow their dependent :class:`_schema.Table`
    objects.
    Tables are dependent on another based on the presence of
    :class:`_schema.ForeignKeyConstraint`
    objects as well as explicit dependencies
    added by :meth:`_schema.Table.add_is_dependent_on`.

    .. warning::

        The :func:`._schema.sort_tables` function cannot by itself
        accommodate automatic resolution of dependency cycles between
        tables, which are usually caused by mutually dependent foreign key
        constraints. When these cycles are detected, the foreign keys
        of these tables are omitted from consideration in the sort.
        A warning is emitted when this condition occurs, which will be an
        exception raise in a future release.   Tables which are not part
        of the cycle will still be returned in dependency order.

        To resolve these cycles, the
        :paramref:`_schema.ForeignKeyConstraint.use_alter` parameter may be
        applied to those constraints which create a cycle.  Alternatively,
        the :func:`_schema.sort_tables_and_constraints` function will
        automatically return foreign key constraints in a separate
        collection when cycles are detected so that they may be applied
        to a schema separately.

        .. versionchanged:: 1.3.17 - a warning is emitted when
           :func:`_schema.sort_tables` cannot perform a proper sort due to
           cyclical dependencies.  This will be an exception in a future
           release.  Additionally, the sort will continue to return
           other tables not involved in the cycle in dependency order
           which was not the case previously.

    :param tables: a sequence of :class:`_schema.Table` objects.

    :param skip_fn: optional callable which will be passed a
     :class:`_schema.ForeignKeyConstraint` object; if it returns True, this
     constraint will not be considered as a dependency.  Note this is
     **different** from the same parameter in
     :func:`.sort_tables_and_constraints`, which is
     instead passed the owning :class:`_schema.ForeignKeyConstraint` object.

    :param extra_dependencies: a sequence of 2-tuples of tables which will
     also be considered as dependent on each other.

    .. seealso::

        :func:`.sort_tables_and_constraints`

        :attr:`_schema.MetaData.sorted_tables` - uses this function to sort


    """
def sort_tables_and_constraints(tables, filter_fn: Incomplete | None = None, extra_dependencies: Incomplete | None = None, _warn_for_cycles: bool = False):
    """Sort a collection of :class:`_schema.Table`  /
    :class:`_schema.ForeignKeyConstraint`
    objects.

    This is a dependency-ordered sort which will emit tuples of
    ``(Table, [ForeignKeyConstraint, ...])`` such that each
    :class:`_schema.Table` follows its dependent :class:`_schema.Table`
    objects.
    Remaining :class:`_schema.ForeignKeyConstraint`
    objects that are separate due to
    dependency rules not satisfied by the sort are emitted afterwards
    as ``(None, [ForeignKeyConstraint ...])``.

    Tables are dependent on another based on the presence of
    :class:`_schema.ForeignKeyConstraint` objects, explicit dependencies
    added by :meth:`_schema.Table.add_is_dependent_on`,
    as well as dependencies
    stated here using the :paramref:`~.sort_tables_and_constraints.skip_fn`
    and/or :paramref:`~.sort_tables_and_constraints.extra_dependencies`
    parameters.

    :param tables: a sequence of :class:`_schema.Table` objects.

    :param filter_fn: optional callable which will be passed a
     :class:`_schema.ForeignKeyConstraint` object,
     and returns a value based on
     whether this constraint should definitely be included or excluded as
     an inline constraint, or neither.   If it returns False, the constraint
     will definitely be included as a dependency that cannot be subject
     to ALTER; if True, it will **only** be included as an ALTER result at
     the end.   Returning None means the constraint is included in the
     table-based result unless it is detected as part of a dependency cycle.

    :param extra_dependencies: a sequence of 2-tuples of tables which will
     also be considered as dependent on each other.

    .. seealso::

        :func:`.sort_tables`


    """
