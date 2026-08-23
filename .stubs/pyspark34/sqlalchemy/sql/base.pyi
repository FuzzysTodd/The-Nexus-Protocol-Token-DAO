from . import coercions as coercions, elements as elements, roles as roles, type_api as type_api, visitors as visitors
from .. import event as event, exc as exc, util as util
from ..engine import Connection as Connection, CursorResult as CursorResult
from ..engine.interfaces import CacheStats as CacheStats, Compiled as Compiled, CompiledCacheType as CompiledCacheType, CoreExecuteOptionsParameter as CoreExecuteOptionsParameter, Dialect as Dialect, IsolationLevel as IsolationLevel, SchemaTranslateMapType as SchemaTranslateMapType, _ExecuteOptions
from ..event import dispatcher as dispatcher
from ..util import HasMemoized as HasMemoized, hybridmethod as hybridmethod, typing as compat_typing
from ..util.typing import Protocol as Protocol, Self as Self, TypeGuard as TypeGuard
from ._orm_types import DMLStrategyArgument as DMLStrategyArgument, SynchronizeSessionArgument as SynchronizeSessionArgument
from .cache_key import HasCacheKey as HasCacheKey, MemoizedHasCacheKey as MemoizedHasCacheKey
from .elements import BindParameter as BindParameter, ClauseList as ClauseList, ColumnClause as ColumnClause, ColumnElement as ColumnElement, KeyedColumnElement as KeyedColumnElement, NamedColumn as NamedColumn, SQLCoreOperations as SQLCoreOperations, TextClause as TextClause
from .schema import Column as Column, DefaultGenerator as DefaultGenerator
from .selectable import FromClause as FromClause
from .traversals import HasCopyInternals as HasCopyInternals
from .visitors import ClauseVisitor as ClauseVisitor, ExtendedInternalTraversal as ExtendedInternalTraversal, ExternallyTraversible as ExternallyTraversible, InternalTraversal as InternalTraversal
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Callable, Dict, FrozenSet, Generic, Iterable, Iterator, List, MutableMapping, NamedTuple, NoReturn, Sequence, Set, Tuple, Type, overload

class _NoArg(Enum):
    NO_ARG: int

NO_ARG: Incomplete

class _NoneName(Enum):
    NONE_NAME: int

class _DefaultDescriptionTuple(NamedTuple):
    arg: Any
    is_scalar: bool | None
    is_callable: bool | None
    is_sentinel: bool | None

class _EntityNamespace(Protocol):
    def __getattr__(self, key: str) -> SQLCoreOperations[Any]: ...

class _HasEntityNamespace(Protocol):
    def entity_namespace(self) -> _EntityNamespace: ...

class Immutable:
    '''mark a ClauseElement as \'immutable\' when expressions are cloned.

    "immutable" objects refers to the "mutability" of an object in the
    context of SQL DQL and DML generation.   Such as, in DQL, one can
    compose a SELECT or subquery of varied forms, but one cannot modify
    the structure of a specific table or column within DQL.
    :class:`.Immutable` is mostly intended to follow this concept, and as
    such the primary "immutable" objects are :class:`.ColumnClause`,
    :class:`.Column`, :class:`.TableClause`, :class:`.Table`.

    '''
    def unique_params(self, *optionaldict, **kwargs) -> None: ...
    def params(self, *optionaldict, **kwargs) -> None: ...

class SingletonConstant(Immutable):
    """Represent SQL constants like NULL, TRUE, FALSE"""
    def __new__(cls, *arg: Any, **kw: Any) -> _T: ...
    def proxy_set(self) -> FrozenSet[ColumnElement[Any]]: ...

class _GenerativeType(compat_typing.Protocol): ...

class _DialectArgView(MutableMapping[str, Any]):
    """A dictionary view of dialect-level arguments in the form
    <dialectname>_<argument_name>.

    """
    obj: Incomplete
    def __init__(self, obj) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

class _DialectArgDict(MutableMapping[str, Any]):
    """A dictionary view of dialect-level arguments for a specific
    dialect.

    Maintains a separate collection of user-specified arguments
    and dialect-specified default arguments.

    """
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...

class DialectKWArgs:
    """Establish the ability for a class to have dialect-specific arguments
    with defaults and constructor validation.

    The :class:`.DialectKWArgs` interacts with the
    :attr:`.DefaultDialect.construct_arguments` present on a dialect.

    .. seealso::

        :attr:`.DefaultDialect.construct_arguments`

    """
    @classmethod
    def argument_for(cls, dialect_name, argument_name, default) -> None:
        '''Add a new kind of dialect-specific keyword argument for this class.

        E.g.::

            Index.argument_for("mydialect", "length", None)

            some_index = Index(\'a\', \'b\', mydialect_length=5)

        The :meth:`.DialectKWArgs.argument_for` method is a per-argument
        way adding extra arguments to the
        :attr:`.DefaultDialect.construct_arguments` dictionary. This
        dictionary provides a list of argument names accepted by various
        schema-level constructs on behalf of a dialect.

        New dialects should typically specify this dictionary all at once as a
        data member of the dialect class.  The use case for ad-hoc addition of
        argument names is typically for end-user code that is also using
        a custom compilation scheme which consumes the additional arguments.

        :param dialect_name: name of a dialect.  The dialect must be
         locatable, else a :class:`.NoSuchModuleError` is raised.   The
         dialect must also include an existing
         :attr:`.DefaultDialect.construct_arguments` collection, indicating
         that it participates in the keyword-argument validation and default
         system, else :class:`.ArgumentError` is raised.  If the dialect does
         not include this collection, then any keyword argument can be
         specified on behalf of this dialect already.  All dialects packaged
         within SQLAlchemy include this collection, however for third party
         dialects, support may vary.

        :param argument_name: name of the parameter.

        :param default: default value of the parameter.

        '''
    def dialect_kwargs(self):
        """A collection of keyword arguments specified as dialect-specific
        options to this construct.

        The arguments are present here in their original ``<dialect>_<kwarg>``
        format.  Only arguments that were actually passed are included;
        unlike the :attr:`.DialectKWArgs.dialect_options` collection, which
        contains all options known by this dialect including defaults.

        The collection is also writable; keys are accepted of the
        form ``<dialect>_<kwarg>`` where the value will be assembled
        into the list of options.

        .. seealso::

            :attr:`.DialectKWArgs.dialect_options` - nested dictionary form

        """
    @property
    def kwargs(self):
        """A synonym for :attr:`.DialectKWArgs.dialect_kwargs`."""
    def dialect_options(self):
        """A collection of keyword arguments specified as dialect-specific
        options to this construct.

        This is a two-level nested registry, keyed to ``<dialect_name>``
        and ``<argument_name>``.  For example, the ``postgresql_where``
        argument would be locatable as::

            arg = my_object.dialect_options['postgresql']['where']

        .. versionadded:: 0.9.2

        .. seealso::

            :attr:`.DialectKWArgs.dialect_kwargs` - flat dictionary form

        """

class CompileState:
    '''Produces additional object state necessary for a statement to be
    compiled.

    the :class:`.CompileState` class is at the base of classes that assemble
    state for a particular statement object that is then used by the
    compiler.   This process is essentially an extension of the process that
    the SQLCompiler.visit_XYZ() method takes, however there is an emphasis
    on converting raw user intent into more organized structures rather than
    producing string output.   The top-level :class:`.CompileState` for the
    statement being executed is also accessible when the execution context
    works with invoking the statement and collecting results.

    The production of :class:`.CompileState` is specific to the compiler,  such
    as within the :meth:`.SQLCompiler.visit_insert`,
    :meth:`.SQLCompiler.visit_select` etc. methods.  These methods are also
    responsible for associating the :class:`.CompileState` with the
    :class:`.SQLCompiler` itself, if the statement is the "toplevel" statement,
    i.e. the outermost SQL statement that\'s actually being executed.
    There can be other :class:`.CompileState` objects that are not the
    toplevel, such as when a SELECT subquery or CTE-nested
    INSERT/UPDATE/DELETE is generated.

    .. versionadded:: 1.4

    '''
    plugins: Dict[Tuple[str, str], Type[CompileState]]
    @classmethod
    def create_for_statement(cls, statement, compiler, **kw): ...
    statement: Incomplete
    def __init__(self, statement, compiler, **kw) -> None: ...
    @classmethod
    def get_plugin_class(cls, statement: Executable) -> Type[CompileState] | None: ...
    @classmethod
    def plugin_for(cls, plugin_name: str, visit_name: str) -> Callable[[_Fn], _Fn]: ...

class Generative(HasMemoized):
    """Provide a method-chaining pattern in conjunction with the
    @_generative decorator."""
class InPlaceGenerative(HasMemoized):
    """Provide a method-chaining pattern in conjunction with the
    @_generative decorator that mutates in place."""
class HasCompileState(Generative):
    """A class that has a :class:`.CompileState` associated with it."""

class _MetaOptions(type):
    """metaclass for the Options class.

    This metaclass is actually necessary despite the availability of the
    ``__init_subclass__()`` hook as this type also provides custom class-level
    behavior for the ``__add__()`` method.

    """
    def __add__(self, other): ...
    def __getattr__(self, key: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __delattr__(self, key: str) -> None: ...

class Options(metaclass=_MetaOptions):
    """A cacheable option dictionary with defaults."""
    def __init_subclass__(cls) -> None: ...
    def __init__(self, **kw) -> None: ...
    def __add__(self, other): ...
    def __eq__(self, other): ...
    @classmethod
    def isinstance(cls, klass: Type[Any]) -> bool: ...
    def add_to_element(self, name, value): ...
    @classmethod
    def safe_merge(cls, other): ...
    @classmethod
    def from_execution_options(cls, key, attrs, exec_options, statement_exec_options):
        '''process Options argument in terms of execution options.


        e.g.::

            (
                load_options,
                execution_options,
            ) = QueryContext.default_load_options.from_execution_options(
                "_sa_orm_load_options",
                {
                    "populate_existing",
                    "autoflush",
                    "yield_per"
                },
                execution_options,
                statement._execution_options,
            )

        get back the Options and refresh "_sa_orm_load_options" in the
        exec options dict w/ the Options as well

        '''
    def __getattr__(self, key: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __delattr__(self, key: str) -> None: ...

class CacheableOptions(Options, HasCacheKey): ...

class ExecutableOption(HasCopyInternals):
    __visit_name__: str

class Executable(roles.StatementRole):
    '''Mark a :class:`_expression.ClauseElement` as supporting execution.

    :class:`.Executable` is a superclass for all "statement" types
    of objects, including :func:`select`, :func:`delete`, :func:`update`,
    :func:`insert`, :func:`text`.

    '''
    supports_execution: bool
    is_select: bool
    is_update: bool
    is_insert: bool
    is_text: bool
    is_delete: bool
    is_dml: bool
    __visit_name__: str
    def options(self, *options: ExecutableOption) -> Self:
        '''Apply options to this statement.

        In the general sense, options are any kind of Python object
        that can be interpreted by the SQL compiler for the statement.
        These options can be consumed by specific dialects or specific kinds
        of compilers.

        The most commonly known kind of option are the ORM level options
        that apply "eager load" and other loading behaviors to an ORM
        query.   However, options can theoretically be used for many other
        purposes.

        For background on specific kinds of options for specific kinds of
        statements, refer to the documentation for those option objects.

        .. versionchanged:: 1.4 - added :meth:`.Executable.options` to
           Core statement objects towards the goal of allowing unified
           Core / ORM querying capabilities.

        .. seealso::

            :ref:`loading_columns` - refers to options specific to the usage
            of ORM queries

            :ref:`relationship_loader_options` - refers to options specific
            to the usage of ORM queries

        '''
    @overload
    def execution_options(self, *, compiled_cache: CompiledCacheType | None = ..., logging_token: str = ..., isolation_level: IsolationLevel = ..., no_parameters: bool = False, stream_results: bool = False, max_row_buffer: int = ..., yield_per: int = ..., insertmanyvalues_page_size: int = ..., schema_translate_map: SchemaTranslateMapType | None = ..., populate_existing: bool = False, autoflush: bool = False, synchronize_session: SynchronizeSessionArgument = ..., dml_strategy: DMLStrategyArgument = ..., is_delete_using: bool = ..., is_update_from: bool = ..., **opt: Any) -> Self: ...
    @overload
    def execution_options(self, **opt: Any) -> Self: ...
    def get_execution_options(self) -> _ExecuteOptions:
        """Get the non-SQL options which will take effect during execution.

        .. versionadded:: 1.3

        .. seealso::

            :meth:`.Executable.execution_options`
        """

class SchemaEventTarget(event.EventTarget):
    """Base class for elements that are the targets of :class:`.DDLEvents`
    events.

    This includes :class:`.SchemaItem` as well as :class:`.SchemaType`.

    """
    dispatch: dispatcher[SchemaEventTarget]

class SchemaVisitor(ClauseVisitor):
    """Define the visiting for ``SchemaItem`` objects."""
    __traverse_options__: Incomplete

class _SentinelDefaultCharacterization(Enum):
    NONE: str
    UNKNOWN: str
    CLIENTSIDE: str
    SENTINEL_DEFAULT: str
    SERVERSIDE: str
    IDENTITY: str
    SEQUENCE: str

class _SentinelColumnCharacterization(NamedTuple):
    columns: Sequence[Column[Any]] | None = ...
    is_explicit: bool = ...
    is_autoinc: bool = ...
    default_characterization: _SentinelDefaultCharacterization = ...

class _ColumnMetrics(Generic[_COL_co]):
    column: _COL_co
    def __init__(self, collection: ColumnCollection[Any, _COL_co], col: _COL_co) -> None: ...
    def get_expanded_proxy_set(self): ...
    def dispose(self, collection) -> None: ...
    def embedded(self, target_set: Set[ColumnElement[Any]] | FrozenSet[ColumnElement[Any]]) -> bool: ...

class ColumnCollection(Generic[_COLKEY, _COL_co]):
    '''Collection of :class:`_expression.ColumnElement` instances,
    typically for
    :class:`_sql.FromClause` objects.

    The :class:`_sql.ColumnCollection` object is most commonly available
    as the :attr:`_schema.Table.c` or :attr:`_schema.Table.columns` collection
    on the :class:`_schema.Table` object, introduced at
    :ref:`metadata_tables_and_columns`.

    The :class:`_expression.ColumnCollection` has both mapping- and sequence-
    like behaviors. A :class:`_expression.ColumnCollection` usually stores
    :class:`_schema.Column` objects, which are then accessible both via mapping
    style access as well as attribute access style.

    To access :class:`_schema.Column` objects using ordinary attribute-style
    access, specify the name like any other object attribute, such as below
    a column named ``employee_name`` is accessed::

        >>> employee_table.c.employee_name

    To access columns that have names with special characters or spaces,
    index-style access is used, such as below which illustrates a column named
    ``employee \' payment`` is accessed::

        >>> employee_table.c["employee \' payment"]

    As the :class:`_sql.ColumnCollection` object provides a Python dictionary
    interface, common dictionary method names like
    :meth:`_sql.ColumnCollection.keys`, :meth:`_sql.ColumnCollection.values`,
    and :meth:`_sql.ColumnCollection.items` are available, which means that
    database columns that are keyed under these names also need to use indexed
    access::

        >>> employee_table.c["values"]


    The name for which a :class:`_schema.Column` would be present is normally
    that of the :paramref:`_schema.Column.key` parameter.  In some contexts,
    such as a :class:`_sql.Select` object that uses a label style set
    using the :meth:`_sql.Select.set_label_style` method, a column of a certain
    key may instead be represented under a particular label name such
    as ``tablename_columnname``::

        >>> from sqlalchemy import select, column, table
        >>> from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL
        >>> t = table("t", column("c"))
        >>> stmt = select(t).set_label_style(LABEL_STYLE_TABLENAME_PLUS_COL)
        >>> subq = stmt.subquery()
        >>> subq.c.t_c
        <sqlalchemy.sql.elements.ColumnClause at 0x7f59dcf04fa0; t_c>

    :class:`.ColumnCollection` also indexes the columns in order and allows
    them to be accessible by their integer position::

        >>> cc[0]
        Column(\'x\', Integer(), table=None)
        >>> cc[1]
        Column(\'y\', Integer(), table=None)

    .. versionadded:: 1.4 :class:`_expression.ColumnCollection`
       allows integer-based
       index access to the collection.

    Iterating the collection yields the column expressions in order::

        >>> list(cc)
        [Column(\'x\', Integer(), table=None),
         Column(\'y\', Integer(), table=None)]

    The base :class:`_expression.ColumnCollection` object can store
    duplicates, which can
    mean either two columns with the same key, in which case the column
    returned by key  access is **arbitrary**::

        >>> x1, x2 = Column(\'x\', Integer), Column(\'x\', Integer)
        >>> cc = ColumnCollection(columns=[(x1.name, x1), (x2.name, x2)])
        >>> list(cc)
        [Column(\'x\', Integer(), table=None),
         Column(\'x\', Integer(), table=None)]
        >>> cc[\'x\'] is x1
        False
        >>> cc[\'x\'] is x2
        True

    Or it can also mean the same column multiple times.   These cases are
    supported as :class:`_expression.ColumnCollection`
    is used to represent the columns in
    a SELECT statement which may include duplicates.

    A special subclass :class:`.DedupeColumnCollection` exists which instead
    maintains SQLAlchemy\'s older behavior of not allowing duplicates; this
    collection is used for schema level objects like :class:`_schema.Table`
    and
    :class:`.PrimaryKeyConstraint` where this deduping is helpful.  The
    :class:`.DedupeColumnCollection` class also has additional mutation methods
    as the schema constructs have more use cases that require removal and
    replacement of columns.

    .. versionchanged:: 1.4 :class:`_expression.ColumnCollection`
       now stores duplicate
       column keys as well as the same column in multiple positions.  The
       :class:`.DedupeColumnCollection` class is added to maintain the
       former behavior in those cases where deduplication as well as
       additional replace/remove operations are needed.


    '''
    def __init__(self, columns: Iterable[Tuple[_COLKEY, _COL_co]] | None = None) -> None: ...
    def __clause_element__(self) -> ClauseList: ...
    def keys(self) -> List[_COLKEY]:
        """Return a sequence of string key names for all columns in this
        collection."""
    def values(self) -> List[_COL_co]:
        """Return a sequence of :class:`_sql.ColumnClause` or
        :class:`_schema.Column` objects for all columns in this
        collection."""
    def items(self) -> List[Tuple[_COLKEY, _COL_co]]:
        """Return a sequence of (key, column) tuples for all columns in this
        collection each consisting of a string key name and a
        :class:`_sql.ColumnClause` or
        :class:`_schema.Column` object.
        """
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_COL_co]: ...
    @overload
    def __getitem__(self, key: str | int) -> _COL_co: ...
    @overload
    def __getitem__(self, key: Tuple[str | int, ...]) -> ReadOnlyColumnCollection[_COLKEY, _COL_co]: ...
    @overload
    def __getitem__(self, key: slice) -> ReadOnlyColumnCollection[_COLKEY, _COL_co]: ...
    def __getattr__(self, key: str) -> _COL_co: ...
    def __contains__(self, key: str) -> bool: ...
    def compare(self, other: ColumnCollection[Any, Any]) -> bool:
        """Compare this :class:`_expression.ColumnCollection` to another
        based on the names of the keys"""
    def __eq__(self, other: Any) -> bool: ...
    def get(self, key: str, default: _COL_co | None = None) -> _COL_co | None:
        """Get a :class:`_sql.ColumnClause` or :class:`_schema.Column` object
        based on a string key name from this
        :class:`_expression.ColumnCollection`."""
    def __setitem__(self, key: str, value: Any) -> NoReturn: ...
    def __delitem__(self, key: str) -> NoReturn: ...
    def __setattr__(self, key: str, obj: Any) -> NoReturn: ...
    def clear(self) -> NoReturn:
        """Dictionary clear() is not implemented for
        :class:`_sql.ColumnCollection`."""
    def remove(self, column: Any) -> None: ...
    def update(self, iter_: Any) -> NoReturn:
        """Dictionary update() is not implemented for
        :class:`_sql.ColumnCollection`."""
    __hash__: Incomplete
    def add(self, column: ColumnElement[Any], key: _COLKEY | None = None) -> None:
        """Add a column to this :class:`_sql.ColumnCollection`.

        .. note::

            This method is **not normally used by user-facing code**, as the
            :class:`_sql.ColumnCollection` is usually part of an existing
            object such as a :class:`_schema.Table`. To add a
            :class:`_schema.Column` to an existing :class:`_schema.Table`
            object, use the :meth:`_schema.Table.append_column` method.

        """
    def contains_column(self, col: ColumnElement[Any]) -> bool:
        """Checks if a column object exists in this collection"""
    def as_readonly(self) -> ReadOnlyColumnCollection[_COLKEY, _COL_co]:
        '''Return a "read only" form of this
        :class:`_sql.ColumnCollection`.'''
    def corresponding_column(self, column: _COL, require_embedded: bool = False) -> _COL | _COL_co | None:
        """Given a :class:`_expression.ColumnElement`, return the exported
        :class:`_expression.ColumnElement` object from this
        :class:`_expression.ColumnCollection`
        which corresponds to that original :class:`_expression.ColumnElement`
        via a common
        ancestor column.

        :param column: the target :class:`_expression.ColumnElement`
                      to be matched.

        :param require_embedded: only return corresponding columns for
         the given :class:`_expression.ColumnElement`, if the given
         :class:`_expression.ColumnElement`
         is actually present within a sub-element
         of this :class:`_expression.Selectable`.
         Normally the column will match if
         it merely shares a common ancestor with one of the exported
         columns of this :class:`_expression.Selectable`.

        .. seealso::

            :meth:`_expression.Selectable.corresponding_column`
            - invokes this method
            against the collection returned by
            :attr:`_expression.Selectable.exported_columns`.

        .. versionchanged:: 1.4 the implementation for ``corresponding_column``
           was moved onto the :class:`_expression.ColumnCollection` itself.

        """

class DedupeColumnCollection(ColumnCollection[str, _NAMEDCOL]):
    """A :class:`_expression.ColumnCollection`
    that maintains deduplicating behavior.

    This is useful by schema level objects such as :class:`_schema.Table` and
    :class:`.PrimaryKeyConstraint`.    The collection includes more
    sophisticated mutator methods as well to suit schema objects which
    require mutable column collections.

    .. versionadded:: 1.4

    """
    def add(self, column: ColumnElement[Any], key: str | None = None) -> None: ...
    def extend(self, iter_: Iterable[_NAMEDCOL]) -> None: ...
    def remove(self, column: _NAMEDCOL) -> None: ...
    def replace(self, column: _NAMEDCOL, extra_remove: Iterable[_NAMEDCOL] | None = None) -> None:
        """add the given column to this collection, removing unaliased
        versions of this column  as well as existing columns with the
        same key.

        e.g.::

            t = Table('sometable', metadata, Column('col1', Integer))
            t.columns.replace(Column('col1', Integer, key='columnone'))

        will remove the original 'col1' from the collection, and add
        the new column under the name 'columnname'.

        Used by schema.Column to override columns during table reflection.

        """

class ReadOnlyColumnCollection(util.ReadOnlyContainer, ColumnCollection[_COLKEY, _COL_co]):
    def __init__(self, collection) -> None: ...
    def add(self, column: Any, key: Any = ...) -> Any: ...
    def extend(self, elements: Any) -> NoReturn: ...
    def remove(self, item: Any) -> NoReturn: ...

class ColumnSet(util.OrderedSet['ColumnClause[Any]']):
    def contains_column(self, col): ...
    def extend(self, cols) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
