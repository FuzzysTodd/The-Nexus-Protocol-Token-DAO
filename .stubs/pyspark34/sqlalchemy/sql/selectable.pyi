from . import cache_key as cache_key, coercions as coercions, operators as operators, roles as roles, traversals as traversals, type_api as type_api, visitors as visitors
from .. import exc as exc, util as util
from ..util import HasMemoized_ro_memoized_attribute as HasMemoized_ro_memoized_attribute
from ..util.typing import Literal as Literal, Protocol as Protocol, Self as Self
from ._typing import _ColumnExpressionArgument, _ColumnExpressionOrStrLabelArgument, _ColumnsClauseArgument, _FromClauseArgument, _JoinTargetArgument, _LimitOffsetType, _NOT_ENTITY, _OnClauseArgument, _SelectStatementForCompoundArgument, _T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _TP, _TextCoercedExpressionArgument, _TypedColumnClauseArgument as _TCCA, is_column_element as is_column_element, is_select_statement as is_select_statement, is_subquery as is_subquery, is_table as is_table, is_text_clause as is_text_clause
from .annotation import Annotated as Annotated, SupportsCloneAnnotations as SupportsCloneAnnotations
from .base import CacheableOptions as CacheableOptions, ColumnCollection as ColumnCollection, ColumnSet as ColumnSet, CompileState as CompileState, DedupeColumnCollection as DedupeColumnCollection, Executable as Executable, ExecutableOption as ExecutableOption, Generative as Generative, HasCompileState as HasCompileState, HasMemoized as HasMemoized, Immutable as Immutable, ReadOnlyColumnCollection as ReadOnlyColumnCollection, _EntityNamespace, _NoArg
from .compiler import SQLCompiler as SQLCompiler
from .dml import Delete as Delete, Update as Update
from .elements import BinaryExpression as BinaryExpression, BindParameter as BindParameter, BooleanClauseList as BooleanClauseList, ClauseElement as ClauseElement, ClauseList as ClauseList, ColumnClause as ColumnClause, ColumnElement as ColumnElement, DQLDMLClauseElement as DQLDMLClauseElement, GroupedElement as GroupedElement, KeyedColumnElement as KeyedColumnElement, Label as Label, NamedColumn as NamedColumn, TableValuedColumn as TableValuedColumn, TextClause as TextClause, UnaryExpression as UnaryExpression, literal_column as literal_column
from .functions import Function as Function
from .operators import OperatorType as OperatorType
from .schema import ForeignKey as ForeignKey, ForeignKeyConstraint as ForeignKeyConstraint
from .sqltypes import NULLTYPE as NULLTYPE, TableValueType as TableValueType
from .type_api import TypeEngine as TypeEngine
from .visitors import InternalTraversal as InternalTraversal, prefix_anon_map as prefix_anon_map
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Dict, Generic, Iterable, List, NamedTuple, NoReturn, Sequence, Tuple, Type, overload

and_: Incomplete

class _JoinTargetProtocol(Protocol):
    def entity_namespace(self) -> _EntityNamespace: ...

class _OffsetLimitParam(BindParameter[int]):
    inherit_cache: bool

class ReturnsRows(roles.ReturnsRowsRole, DQLDMLClauseElement):
    """The base-most class for Core constructs that have some concept of
    columns that can represent rows.

    While the SELECT statement and TABLE are the primary things we think
    of in this category,  DML like INSERT, UPDATE and DELETE can also specify
    RETURNING which means they can be used in CTEs and other forms, and
    PostgreSQL has functions that return rows also.

    .. versionadded:: 1.4

    """
    @property
    def selectable(self) -> ReturnsRows: ...
    def is_derived_from(self, fromclause: FromClause | None) -> bool:
        """Return ``True`` if this :class:`.ReturnsRows` is
        'derived' from the given :class:`.FromClause`.

        An example would be an Alias of a Table is derived from that Table.

        """
    @property
    def exported_columns(self) -> ReadOnlyColumnCollection[Any, Any]:
        '''A :class:`_expression.ColumnCollection`
        that represents the "exported"
        columns of this :class:`_expression.ReturnsRows`.

        The "exported" columns represent the collection of
        :class:`_expression.ColumnElement`
        expressions that are rendered by this SQL
        construct.   There are primary varieties which are the
        "FROM clause columns" of a FROM clause, such as a table, join,
        or subquery, the "SELECTed columns", which are the columns in
        the "columns clause" of a SELECT statement, and the RETURNING
        columns in a DML statement..

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_expression.FromClause.exported_columns`

            :attr:`_expression.SelectBase.exported_columns`
        '''

class ExecutableReturnsRows(Executable, ReturnsRows):
    """base for executable statements that return rows."""
class TypedReturnsRows(ExecutableReturnsRows, Generic[_TP]):
    """base for executable statements that return rows."""

class Selectable(ReturnsRows):
    """Mark a class as being selectable."""
    __visit_name__: str
    is_selectable: bool
    def lateral(self, name: str | None = None) -> LateralFromClause:
        """Return a LATERAL alias of this :class:`_expression.Selectable`.

        The return value is the :class:`_expression.Lateral` construct also
        provided by the top-level :func:`_expression.lateral` function.

        .. seealso::

            :ref:`tutorial_lateral_correlation` -  overview of usage.

        """
    def replace_selectable(self, old: FromClause, alias: Alias) -> Self:
        """Replace all occurrences of :class:`_expression.FromClause`
        'old' with the given :class:`_expression.Alias`
        object, returning a copy of this :class:`_expression.FromClause`.

        """
    def corresponding_column(self, column: KeyedColumnElement[Any], require_embedded: bool = False) -> KeyedColumnElement[Any] | None:
        """Given a :class:`_expression.ColumnElement`, return the exported
        :class:`_expression.ColumnElement` object from the
        :attr:`_expression.Selectable.exported_columns`
        collection of this :class:`_expression.Selectable`
        which corresponds to that
        original :class:`_expression.ColumnElement` via a common ancestor
        column.

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

            :attr:`_expression.Selectable.exported_columns` - the
            :class:`_expression.ColumnCollection`
            that is used for the operation.

            :meth:`_expression.ColumnCollection.corresponding_column`
            - implementation
            method.

        """

class HasPrefixes:
    def prefix_with(self, *prefixes: _TextCoercedExpressionArgument[Any], dialect: str = '*') -> Self:
        '''Add one or more expressions following the statement keyword, i.e.
        SELECT, INSERT, UPDATE, or DELETE. Generative.

        This is used to support backend-specific prefix keywords such as those
        provided by MySQL.

        E.g.::

            stmt = table.insert().prefix_with("LOW_PRIORITY", dialect="mysql")

            # MySQL 5.7 optimizer hints
            stmt = select(table).prefix_with(
                "/*+ BKA(t1) */", dialect="mysql")

        Multiple prefixes can be specified by multiple calls
        to :meth:`_expression.HasPrefixes.prefix_with`.

        :param \\*prefixes: textual or :class:`_expression.ClauseElement`
         construct which
         will be rendered following the INSERT, UPDATE, or DELETE
         keyword.
        :param dialect: optional string dialect name which will
         limit rendering of this prefix to only that dialect.

        '''

class HasSuffixes:
    def suffix_with(self, *suffixes: _TextCoercedExpressionArgument[Any], dialect: str = '*') -> Self:
        '''Add one or more expressions following the statement as a whole.

        This is used to support backend-specific suffix keywords on
        certain constructs.

        E.g.::

            stmt = select(col1, col2).cte().suffix_with(
                "cycle empno set y_cycle to 1 default 0", dialect="oracle")

        Multiple suffixes can be specified by multiple calls
        to :meth:`_expression.HasSuffixes.suffix_with`.

        :param \\*suffixes: textual or :class:`_expression.ClauseElement`
         construct which
         will be rendered following the target clause.
        :param dialect: Optional string dialect name which will
         limit rendering of this suffix to only that dialect.

        '''

class HasHints:
    def with_statement_hint(self, text: str, dialect_name: str = '*') -> Self:
        """Add a statement hint to this :class:`_expression.Select` or
        other selectable object.

        This method is similar to :meth:`_expression.Select.with_hint`
        except that
        it does not require an individual table, and instead applies to the
        statement as a whole.

        Hints here are specific to the backend database and may include
        directives such as isolation levels, file directives, fetch directives,
        etc.

        .. seealso::

            :meth:`_expression.Select.with_hint`

            :meth:`_expression.Select.prefix_with` - generic SELECT prefixing
            which also can suit some database-specific HINT syntaxes such as
            MySQL optimizer hints

        """
    def with_hint(self, selectable: _FromClauseArgument, text: str, dialect_name: str = '*') -> Self:
        '''Add an indexing or other executional context hint for the given
        selectable to this :class:`_expression.Select` or other selectable
        object.

        The text of the hint is rendered in the appropriate
        location for the database backend in use, relative
        to the given :class:`_schema.Table` or :class:`_expression.Alias`
        passed as the
        ``selectable`` argument. The dialect implementation
        typically uses Python string substitution syntax
        with the token ``%(name)s`` to render the name of
        the table or alias. E.g. when using Oracle, the
        following::

            select(mytable).\\\n                with_hint(mytable, "index(%(name)s ix_mytable)")

        Would render SQL as::

            select /*+ index(mytable ix_mytable) */ ... from mytable

        The ``dialect_name`` option will limit the rendering of a particular
        hint to a particular backend. Such as, to add hints for both Oracle
        and Sybase simultaneously::

            select(mytable).\\\n                with_hint(mytable, "index(%(name)s ix_mytable)", \'oracle\').\\\n                with_hint(mytable, "WITH INDEX ix_mytable", \'mssql\')

        .. seealso::

            :meth:`_expression.Select.with_statement_hint`

        '''

class FromClause(roles.AnonymizedFromClauseRole, Selectable):
    '''Represent an element that can be used within the ``FROM``
    clause of a ``SELECT`` statement.

    The most common forms of :class:`_expression.FromClause` are the
    :class:`_schema.Table` and the :func:`_expression.select` constructs.  Key
    features common to all :class:`_expression.FromClause` objects include:

    * a :attr:`.c` collection, which provides per-name access to a collection
      of :class:`_expression.ColumnElement` objects.
    * a :attr:`.primary_key` attribute, which is a collection of all those
      :class:`_expression.ColumnElement`
      objects that indicate the ``primary_key`` flag.
    * Methods to generate various derivations of a "from" clause, including
      :meth:`_expression.FromClause.alias`,
      :meth:`_expression.FromClause.join`,
      :meth:`_expression.FromClause.select`.


    '''
    __visit_name__: str
    named_with_column: bool
    schema: str | None
    is_selectable: bool
    def select(self) -> Select[Any]:
        """Return a SELECT of this :class:`_expression.FromClause`.


        e.g.::

            stmt = some_table.select().where(some_table.c.id == 5)

        .. seealso::

            :func:`_expression.select` - general purpose
            method which allows for arbitrary column lists.

        """
    def join(self, right: _FromClauseArgument, onclause: _ColumnExpressionArgument[bool] | None = None, isouter: bool = False, full: bool = False) -> Join:
        """Return a :class:`_expression.Join` from this
        :class:`_expression.FromClause`
        to another :class:`FromClause`.

        E.g.::

            from sqlalchemy import join

            j = user_table.join(address_table,
                            user_table.c.id == address_table.c.user_id)
            stmt = select(user_table).select_from(j)

        would emit SQL along the lines of::

            SELECT user.id, user.name FROM user
            JOIN address ON user.id = address.user_id

        :param right: the right side of the join; this is any
         :class:`_expression.FromClause` object such as a
         :class:`_schema.Table` object, and
         may also be a selectable-compatible object such as an ORM-mapped
         class.

        :param onclause: a SQL expression representing the ON clause of the
         join.  If left at ``None``, :meth:`_expression.FromClause.join`
         will attempt to
         join the two tables based on a foreign key relationship.

        :param isouter: if True, render a LEFT OUTER JOIN, instead of JOIN.

        :param full: if True, render a FULL OUTER JOIN, instead of LEFT OUTER
         JOIN.  Implies :paramref:`.FromClause.join.isouter`.

        .. seealso::

            :func:`_expression.join` - standalone function

            :class:`_expression.Join` - the type of object produced

        """
    def outerjoin(self, right: _FromClauseArgument, onclause: _ColumnExpressionArgument[bool] | None = None, full: bool = False) -> Join:
        '''Return a :class:`_expression.Join` from this
        :class:`_expression.FromClause`
        to another :class:`FromClause`, with the "isouter" flag set to
        True.

        E.g.::

            from sqlalchemy import outerjoin

            j = user_table.outerjoin(address_table,
                            user_table.c.id == address_table.c.user_id)

        The above is equivalent to::

            j = user_table.join(
                address_table,
                user_table.c.id == address_table.c.user_id,
                isouter=True)

        :param right: the right side of the join; this is any
         :class:`_expression.FromClause` object such as a
         :class:`_schema.Table` object, and
         may also be a selectable-compatible object such as an ORM-mapped
         class.

        :param onclause: a SQL expression representing the ON clause of the
         join.  If left at ``None``, :meth:`_expression.FromClause.join`
         will attempt to
         join the two tables based on a foreign key relationship.

        :param full: if True, render a FULL OUTER JOIN, instead of
         LEFT OUTER JOIN.

        .. seealso::

            :meth:`_expression.FromClause.join`

            :class:`_expression.Join`

        '''
    def alias(self, name: str | None = None, flat: bool = False) -> NamedFromClause:
        """Return an alias of this :class:`_expression.FromClause`.

        E.g.::

            a2 = some_table.alias('a2')

        The above code creates an :class:`_expression.Alias`
        object which can be used
        as a FROM clause in any SELECT statement.

        .. seealso::

            :ref:`tutorial_using_aliases`

            :func:`_expression.alias`

        """
    def tablesample(self, sampling: float | Function[Any], name: str | None = None, seed: roles.ExpressionElementRole[Any] | None = None) -> TableSample:
        """Return a TABLESAMPLE alias of this :class:`_expression.FromClause`.

        The return value is the :class:`_expression.TableSample`
        construct also
        provided by the top-level :func:`_expression.tablesample` function.

        .. seealso::

            :func:`_expression.tablesample` - usage guidelines and parameters

        """
    def is_derived_from(self, fromclause: FromClause | None) -> bool:
        """Return ``True`` if this :class:`_expression.FromClause` is
        'derived' from the given ``FromClause``.

        An example would be an Alias of a Table is derived from that Table.

        """
    def description(self) -> str:
        """A brief description of this :class:`_expression.FromClause`.

        Used primarily for error message formatting.

        """
    def exported_columns(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]:
        '''A :class:`_expression.ColumnCollection`
        that represents the "exported"
        columns of this :class:`_expression.Selectable`.

        The "exported" columns for a :class:`_expression.FromClause`
        object are synonymous
        with the :attr:`_expression.FromClause.columns` collection.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_expression.Selectable.exported_columns`

            :attr:`_expression.SelectBase.exported_columns`


        '''
    def columns(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]:
        """A named-based collection of :class:`_expression.ColumnElement`
        objects maintained by this :class:`_expression.FromClause`.

        The :attr:`.columns`, or :attr:`.c` collection, is the gateway
        to the construction of SQL expressions using table-bound or
        other selectable-bound columns::

            select(mytable).where(mytable.c.somecolumn == 5)

        :return: a :class:`.ColumnCollection` object.

        """
    def c(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]:
        """
        A synonym for :attr:`.FromClause.columns`

        :return: a :class:`.ColumnCollection`

        """
    def entity_namespace(self) -> _EntityNamespace:
        '''Return a namespace used for name-based access in SQL expressions.

        This is the namespace that is used to resolve "filter_by()" type
        expressions, such as::

            stmt.filter_by(address=\'some address\')

        It defaults to the ``.c`` collection, however internally it can
        be overridden using the "entity_namespace" annotation to deliver
        alternative results.

        '''
    def primary_key(self) -> Iterable[NamedColumn[Any]]:
        """Return the iterable collection of :class:`_schema.Column` objects
        which comprise the primary key of this :class:`_selectable.FromClause`.

        For a :class:`_schema.Table` object, this collection is represented
        by the :class:`_schema.PrimaryKeyConstraint` which itself is an
        iterable collection of :class:`_schema.Column` objects.

        """
    def foreign_keys(self) -> Iterable[ForeignKey]:
        """Return the collection of :class:`_schema.ForeignKey` marker objects
        which this FromClause references.

        Each :class:`_schema.ForeignKey` is a member of a
        :class:`_schema.Table`-wide
        :class:`_schema.ForeignKeyConstraint`.

        .. seealso::

            :attr:`_schema.Table.foreign_key_constraints`

        """
    def self_group(self, against: OperatorType | None = None) -> FromGrouping | Self: ...

class NamedFromClause(FromClause):
    """A :class:`.FromClause` that has a name.

    Examples include tables, subqueries, CTEs, aliased tables.

    .. versionadded:: 2.0

    """
    named_with_column: bool
    name: str
    def table_valued(self) -> TableValuedColumn[Any]:
        '''Return a :class:`_sql.TableValuedColumn` object for this
        :class:`_expression.FromClause`.

        A :class:`_sql.TableValuedColumn` is a :class:`_sql.ColumnElement` that
        represents a complete row in a table. Support for this construct is
        backend dependent, and is supported in various forms by backends
        such as PostgreSQL, Oracle and SQL Server.

        E.g.:

        .. sourcecode:: pycon+sql

            >>> from sqlalchemy import select, column, func, table
            >>> a = table("a", column("id"), column("x"), column("y"))
            >>> stmt = select(func.row_to_json(a.table_valued()))
            >>> print(stmt)
            {printsql}SELECT row_to_json(a) AS row_to_json_1
            FROM a

        .. versionadded:: 1.4.0b2

        .. seealso::

            :ref:`tutorial_functions` - in the :ref:`unified_tutorial`

        '''

class SelectLabelStyle(Enum):
    """Label style constants that may be passed to
    :meth:`_sql.Select.set_label_style`."""
    LABEL_STYLE_NONE: int
    LABEL_STYLE_TABLENAME_PLUS_COL: int
    LABEL_STYLE_DISAMBIGUATE_ONLY: int
    LABEL_STYLE_DEFAULT = LABEL_STYLE_DISAMBIGUATE_ONLY
    LABEL_STYLE_LEGACY_ORM: int

LABEL_STYLE_NONE: Incomplete
LABEL_STYLE_TABLENAME_PLUS_COL: Incomplete
LABEL_STYLE_DISAMBIGUATE_ONLY: Incomplete
_: Incomplete
LABEL_STYLE_DEFAULT = LABEL_STYLE_DISAMBIGUATE_ONLY

class Join(roles.DMLTableRole, FromClause):
    """Represent a ``JOIN`` construct between two
    :class:`_expression.FromClause`
    elements.

    The public constructor function for :class:`_expression.Join`
    is the module-level
    :func:`_expression.join()` function, as well as the
    :meth:`_expression.FromClause.join` method
    of any :class:`_expression.FromClause` (e.g. such as
    :class:`_schema.Table`).

    .. seealso::

        :func:`_expression.join`

        :meth:`_expression.FromClause.join`

    """
    __visit_name__: str
    left: FromClause
    right: FromClause
    onclause: ColumnElement[bool] | None
    isouter: bool
    full: bool
    def __init__(self, left: _FromClauseArgument, right: _FromClauseArgument, onclause: _OnClauseArgument | None = None, isouter: bool = False, full: bool = False) -> None:
        """Construct a new :class:`_expression.Join`.

        The usual entrypoint here is the :func:`_expression.join`
        function or the :meth:`_expression.FromClause.join` method of any
        :class:`_expression.FromClause` object.

        """
    def description(self) -> str: ...
    def is_derived_from(self, fromclause: FromClause | None) -> bool: ...
    def self_group(self, against: OperatorType | None = None) -> FromGrouping: ...
    def select(self) -> Select[Any]:
        """Create a :class:`_expression.Select` from this
        :class:`_expression.Join`.

        E.g.::

            stmt = table_a.join(table_b, table_a.c.id == table_b.c.a_id)

            stmt = stmt.select()

        The above will produce a SQL string resembling::

            SELECT table_a.id, table_a.col, table_b.id, table_b.a_id
            FROM table_a JOIN table_b ON table_a.id = table_b.a_id

        """

class NoInit:
    def __init__(self, *arg: Any, **kw: Any) -> None: ...

class LateralFromClause(NamedFromClause):
    """mark a FROM clause as being able to render directly as LATERAL"""

class AliasedReturnsRows(NoInit, NamedFromClause):
    """Base class of aliases against tables, subqueries, and other
    selectables."""
    element: ReturnsRows
    def description(self) -> str: ...
    def implicit_returning(self) -> bool: ...
    @property
    def original(self) -> ReturnsRows:
        """Legacy for dialects that are referring to Alias.original."""
    def is_derived_from(self, fromclause: FromClause | None) -> bool: ...

class FromClauseAlias(AliasedReturnsRows):
    element: FromClause

class Alias(roles.DMLTableRole, FromClauseAlias):
    """Represents an table or selectable alias (AS).

    Represents an alias, as typically applied to any table or
    sub-select within a SQL statement using the ``AS`` keyword (or
    without the keyword on certain databases such as Oracle).

    This object is constructed from the :func:`_expression.alias` module
    level function as well as the :meth:`_expression.FromClause.alias`
    method available
    on all :class:`_expression.FromClause` subclasses.

    .. seealso::

        :meth:`_expression.FromClause.alias`

    """
    __visit_name__: str
    inherit_cache: bool
    element: FromClause

class TableValuedAlias(LateralFromClause, Alias):
    '''An alias against a "table valued" SQL function.

    This construct provides for a SQL function that returns columns
    to be used in the FROM clause of a SELECT statement.   The
    object is generated using the :meth:`_functions.FunctionElement.table_valued`
    method, e.g.:

    .. sourcecode:: pycon+sql

        >>> from sqlalchemy import select, func
        >>> fn = func.json_array_elements_text(\'["one", "two", "three"]\').table_valued("value")
        >>> print(select(fn.c.value))
        {printsql}SELECT anon_1.value
        FROM json_array_elements_text(:json_array_elements_text_1) AS anon_1

    .. versionadded:: 1.4.0b2

    .. seealso::

        :ref:`tutorial_functions_table_valued` - in the :ref:`unified_tutorial`

    '''
    __visit_name__: str
    joins_implicitly: bool
    def column(self) -> TableValuedColumn[Any]:
        '''Return a column expression representing this
        :class:`_sql.TableValuedAlias`.

        This accessor is used to implement the
        :meth:`_functions.FunctionElement.column_valued` method. See that
        method for further details.

        E.g.:

        .. sourcecode:: pycon+sql

            >>> print(select(func.some_func().table_valued("value").column))
            {printsql}SELECT anon_1 FROM some_func() AS anon_1

        .. seealso::

            :meth:`_functions.FunctionElement.column_valued`

        '''
    def alias(self, name: str | None = None, flat: bool = False) -> TableValuedAlias:
        """Return a new alias of this :class:`_sql.TableValuedAlias`.

        This creates a distinct FROM object that will be distinguished
        from the original one when used in a SQL statement.

        """
    def lateral(self, name: str | None = None) -> LateralFromClause:
        """Return a new :class:`_sql.TableValuedAlias` with the lateral flag
        set, so that it renders as LATERAL.

        .. seealso::

            :func:`_expression.lateral`

        """
    def render_derived(self, name: str | None = None, with_types: bool = False) -> TableValuedAlias:
        '''Apply "render derived" to this :class:`_sql.TableValuedAlias`.

        This has the effect of the individual column names listed out
        after the alias name in the "AS" sequence, e.g.:

        .. sourcecode:: pycon+sql

            >>> print(
            ...     select(
            ...         func.unnest(array(["one", "two", "three"])).
                        table_valued("x", with_ordinality="o").render_derived()
            ...     )
            ... )
            {printsql}SELECT anon_1.x, anon_1.o
            FROM unnest(ARRAY[%(param_1)s, %(param_2)s, %(param_3)s]) WITH ORDINALITY AS anon_1(x, o)

        The ``with_types`` keyword will render column types inline within
        the alias expression (this syntax currently applies to the
        PostgreSQL database):

        .. sourcecode:: pycon+sql

            >>> print(
            ...     select(
            ...         func.json_to_recordset(
            ...             \'[{"a":1,"b":"foo"},{"a":"2","c":"bar"}]\'
            ...         )
            ...         .table_valued(column("a", Integer), column("b", String))
            ...         .render_derived(with_types=True)
            ...     )
            ... )
            {printsql}SELECT anon_1.a, anon_1.b FROM json_to_recordset(:json_to_recordset_1)
            AS anon_1(a INTEGER, b VARCHAR)

        :param name: optional string name that will be applied to the alias
         generated.  If left as None, a unique anonymizing name will be used.

        :param with_types: if True, the derived columns will include the
         datatype specification with each column. This is a special syntax
         currently known to be required by PostgreSQL for some SQL functions.

        '''

class Lateral(FromClauseAlias, LateralFromClause):
    """Represent a LATERAL subquery.

    This object is constructed from the :func:`_expression.lateral` module
    level function as well as the :meth:`_expression.FromClause.lateral`
    method available
    on all :class:`_expression.FromClause` subclasses.

    While LATERAL is part of the SQL standard, currently only more recent
    PostgreSQL versions provide support for this keyword.

    .. seealso::

        :ref:`tutorial_lateral_correlation` -  overview of usage.

    """
    __visit_name__: str
    inherit_cache: bool

class TableSample(FromClauseAlias):
    """Represent a TABLESAMPLE clause.

    This object is constructed from the :func:`_expression.tablesample` module
    level function as well as the :meth:`_expression.FromClause.tablesample`
    method
    available on all :class:`_expression.FromClause` subclasses.

    .. seealso::

        :func:`_expression.tablesample`

    """
    __visit_name__: str

class CTE(roles.DMLTableRole, roles.IsCTERole, Generative, HasPrefixes, HasSuffixes, AliasedReturnsRows):
    """Represent a Common Table Expression.

    The :class:`_expression.CTE` object is obtained using the
    :meth:`_sql.SelectBase.cte` method from any SELECT statement. A less often
    available syntax also allows use of the :meth:`_sql.HasCTE.cte` method
    present on :term:`DML` constructs such as :class:`_sql.Insert`,
    :class:`_sql.Update` and
    :class:`_sql.Delete`.   See the :meth:`_sql.HasCTE.cte` method for
    usage details on CTEs.

    .. seealso::

        :ref:`tutorial_subqueries_ctes` - in the 2.0 tutorial

        :meth:`_sql.HasCTE.cte` - examples of calling styles

    """
    __visit_name__: str
    element: HasCTE
    def alias(self, name: str | None = None, flat: bool = False) -> CTE:
        """Return an :class:`_expression.Alias` of this
        :class:`_expression.CTE`.

        This method is a CTE-specific specialization of the
        :meth:`_expression.FromClause.alias` method.

        .. seealso::

            :ref:`tutorial_using_aliases`

            :func:`_expression.alias`

        """
    def union(self, *other: _SelectStatementForCompoundArgument) -> CTE:
        """Return a new :class:`_expression.CTE` with a SQL ``UNION``
        of the original CTE against the given selectables provided
        as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28 multiple elements are now accepted.

        .. seealso::

            :meth:`_sql.HasCTE.cte` - examples of calling styles

        """
    def union_all(self, *other: _SelectStatementForCompoundArgument) -> CTE:
        """Return a new :class:`_expression.CTE` with a SQL ``UNION ALL``
        of the original CTE against the given selectables provided
        as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28 multiple elements are now accepted.

        .. seealso::

            :meth:`_sql.HasCTE.cte` - examples of calling styles

        """

class _CTEOpts(NamedTuple):
    nesting: bool

class _ColumnsPlusNames(NamedTuple):
    required_label_name: str | None
    proxy_key: str | None
    fallback_label_name: str | None
    column: ColumnElement[Any] | TextClause
    repeated: bool

class SelectsRows(ReturnsRows):
    """Sub-base of ReturnsRows for elements that deliver rows
    directly, namely SELECT and INSERT/UPDATE/DELETE..RETURNING"""

class HasCTE(roles.HasCTERole, SelectsRows):
    """Mixin that declares a class to include CTE support."""
    def add_cte(self, *ctes: CTE, nest_here: bool = False) -> Self:
        '''Add one or more :class:`_sql.CTE` constructs to this statement.

        This method will associate the given :class:`_sql.CTE` constructs with
        the parent statement such that they will each be unconditionally
        rendered in the WITH clause of the final statement, even if not
        referenced elsewhere within the statement or any sub-selects.

        The optional :paramref:`.HasCTE.add_cte.nest_here` parameter when set
        to True will have the effect that each given :class:`_sql.CTE` will
        render in a WITH clause rendered directly along with this statement,
        rather than being moved to the top of the ultimate rendered statement,
        even if this statement is rendered as a subquery within a larger
        statement.

        This method has two general uses. One is to embed CTE statements that
        serve some purpose without being referenced explicitly, such as the use
        case of embedding a DML statement such as an INSERT or UPDATE as a CTE
        inline with a primary statement that may draw from its results
        indirectly.  The other is to provide control over the exact placement
        of a particular series of CTE constructs that should remain rendered
        directly in terms of a particular statement that may be nested in a
        larger statement.

        E.g.::

            from sqlalchemy import table, column, select
            t = table(\'t\', column(\'c1\'), column(\'c2\'))

            ins = t.insert().values({"c1": "x", "c2": "y"}).cte()

            stmt = select(t).add_cte(ins)

        Would render::

            WITH anon_1 AS
            (INSERT INTO t (c1, c2) VALUES (:param_1, :param_2))
            SELECT t.c1, t.c2
            FROM t

        Above, the "anon_1" CTE is not referenced in the SELECT
        statement, however still accomplishes the task of running an INSERT
        statement.

        Similarly in a DML-related context, using the PostgreSQL
        :class:`_postgresql.Insert` construct to generate an "upsert"::

            from sqlalchemy import table, column
            from sqlalchemy.dialects.postgresql import insert

            t = table("t", column("c1"), column("c2"))

            delete_statement_cte = (
                t.delete().where(t.c.c1 < 1).cte("deletions")
            )

            insert_stmt = insert(t).values({"c1": 1, "c2": 2})
            update_statement = insert_stmt.on_conflict_do_update(
                index_elements=[t.c.c1],
                set_={
                    "c1": insert_stmt.excluded.c1,
                    "c2": insert_stmt.excluded.c2,
                },
            ).add_cte(delete_statement_cte)

            print(update_statement)

        The above statement renders as::

            WITH deletions AS
            (DELETE FROM t WHERE t.c1 < %(c1_1)s)
            INSERT INTO t (c1, c2) VALUES (%(c1)s, %(c2)s)
            ON CONFLICT (c1) DO UPDATE SET c1 = excluded.c1, c2 = excluded.c2

        .. versionadded:: 1.4.21

        :param \\*ctes: zero or more :class:`.CTE` constructs.

         .. versionchanged:: 2.0  Multiple CTE instances are accepted

        :param nest_here: if True, the given CTE or CTEs will be rendered
         as though they specified the :paramref:`.HasCTE.cte.nesting` flag
         to ``True`` when they were added to this :class:`.HasCTE`.
         Assuming the given CTEs are not referenced in an outer-enclosing
         statement as well, the CTEs given should render at the level of
         this statement when this flag is given.

         .. versionadded:: 2.0

         .. seealso::

            :paramref:`.HasCTE.cte.nesting`


        '''
    def cte(self, name: str | None = None, recursive: bool = False, nesting: bool = False) -> CTE:
        '''Return a new :class:`_expression.CTE`,
        or Common Table Expression instance.

        Common table expressions are a SQL standard whereby SELECT
        statements can draw upon secondary statements specified along
        with the primary statement, using a clause called "WITH".
        Special semantics regarding UNION can also be employed to
        allow "recursive" queries, where a SELECT statement can draw
        upon the set of rows that have previously been selected.

        CTEs can also be applied to DML constructs UPDATE, INSERT
        and DELETE on some databases, both as a source of CTE rows
        when combined with RETURNING, as well as a consumer of
        CTE rows.

        SQLAlchemy detects :class:`_expression.CTE` objects, which are treated
        similarly to :class:`_expression.Alias` objects, as special elements
        to be delivered to the FROM clause of the statement as well
        as to a WITH clause at the top of the statement.

        For special prefixes such as PostgreSQL "MATERIALIZED" and
        "NOT MATERIALIZED", the :meth:`_expression.CTE.prefix_with`
        method may be
        used to establish these.

        .. versionchanged:: 1.3.13 Added support for prefixes.
           In particular - MATERIALIZED and NOT MATERIALIZED.

        :param name: name given to the common table expression.  Like
         :meth:`_expression.FromClause.alias`, the name can be left as
         ``None`` in which case an anonymous symbol will be used at query
         compile time.
        :param recursive: if ``True``, will render ``WITH RECURSIVE``.
         A recursive common table expression is intended to be used in
         conjunction with UNION ALL in order to derive rows
         from those already selected.
        :param nesting: if ``True``, will render the CTE locally to the
         statement in which it is referenced.   For more complex scenarios,
         the :meth:`.HasCTE.add_cte` method using the
         :paramref:`.HasCTE.add_cte.nest_here`
         parameter may also be used to more carefully
         control the exact placement of a particular CTE.

         .. versionadded:: 1.4.24

         .. seealso::

            :meth:`.HasCTE.add_cte`

        The following examples include two from PostgreSQL\'s documentation at
        https://www.postgresql.org/docs/current/static/queries-with.html,
        as well as additional examples.

        Example 1, non recursive::

            from sqlalchemy import (Table, Column, String, Integer,
                                    MetaData, select, func)

            metadata = MetaData()

            orders = Table(\'orders\', metadata,
                Column(\'region\', String),
                Column(\'amount\', Integer),
                Column(\'product\', String),
                Column(\'quantity\', Integer)
            )

            regional_sales = select(
                                orders.c.region,
                                func.sum(orders.c.amount).label(\'total_sales\')
                            ).group_by(orders.c.region).cte("regional_sales")


            top_regions = select(regional_sales.c.region).\\\n                    where(
                        regional_sales.c.total_sales >
                        select(
                            func.sum(regional_sales.c.total_sales) / 10
                        )
                    ).cte("top_regions")

            statement = select(
                        orders.c.region,
                        orders.c.product,
                        func.sum(orders.c.quantity).label("product_units"),
                        func.sum(orders.c.amount).label("product_sales")
                ).where(orders.c.region.in_(
                    select(top_regions.c.region)
                )).group_by(orders.c.region, orders.c.product)

            result = conn.execute(statement).fetchall()

        Example 2, WITH RECURSIVE::

            from sqlalchemy import (Table, Column, String, Integer,
                                    MetaData, select, func)

            metadata = MetaData()

            parts = Table(\'parts\', metadata,
                Column(\'part\', String),
                Column(\'sub_part\', String),
                Column(\'quantity\', Integer),
            )

            included_parts = select(\\\n                parts.c.sub_part, parts.c.part, parts.c.quantity\\\n                ).\\\n                where(parts.c.part==\'our part\').\\\n                cte(recursive=True)


            incl_alias = included_parts.alias()
            parts_alias = parts.alias()
            included_parts = included_parts.union_all(
                select(
                    parts_alias.c.sub_part,
                    parts_alias.c.part,
                    parts_alias.c.quantity
                ).\\\n                where(parts_alias.c.part==incl_alias.c.sub_part)
            )

            statement = select(
                        included_parts.c.sub_part,
                        func.sum(included_parts.c.quantity).
                          label(\'total_quantity\')
                    ).\\\n                    group_by(included_parts.c.sub_part)

            result = conn.execute(statement).fetchall()

        Example 3, an upsert using UPDATE and INSERT with CTEs::

            from datetime import date
            from sqlalchemy import (MetaData, Table, Column, Integer,
                                    Date, select, literal, and_, exists)

            metadata = MetaData()

            visitors = Table(\'visitors\', metadata,
                Column(\'product_id\', Integer, primary_key=True),
                Column(\'date\', Date, primary_key=True),
                Column(\'count\', Integer),
            )

            # add 5 visitors for the product_id == 1
            product_id = 1
            day = date.today()
            count = 5

            update_cte = (
                visitors.update()
                .where(and_(visitors.c.product_id == product_id,
                            visitors.c.date == day))
                .values(count=visitors.c.count + count)
                .returning(literal(1))
                .cte(\'update_cte\')
            )

            upsert = visitors.insert().from_select(
                [visitors.c.product_id, visitors.c.date, visitors.c.count],
                select(literal(product_id), literal(day), literal(count))
                    .where(~exists(update_cte.select()))
            )

            connection.execute(upsert)

        Example 4, Nesting CTE (SQLAlchemy 1.4.24 and above)::

            value_a = select(
                literal("root").label("n")
            ).cte("value_a")

            # A nested CTE with the same name as the root one
            value_a_nested = select(
                literal("nesting").label("n")
            ).cte("value_a", nesting=True)

            # Nesting CTEs takes ascendency locally
            # over the CTEs at a higher level
            value_b = select(value_a_nested.c.n).cte("value_b")

            value_ab = select(value_a.c.n.label("a"), value_b.c.n.label("b"))

        The above query will render the second CTE nested inside the first,
        shown with inline parameters below as::

            WITH
                value_a AS
                    (SELECT \'root\' AS n),
                value_b AS
                    (WITH value_a AS
                        (SELECT \'nesting\' AS n)
                    SELECT value_a.n AS n FROM value_a)
            SELECT value_a.n AS a, value_b.n AS b
            FROM value_a, value_b

        The same CTE can be set up using the :meth:`.HasCTE.add_cte` method
        as follows (SQLAlchemy 2.0 and above)::

            value_a = select(
                literal("root").label("n")
            ).cte("value_a")

            # A nested CTE with the same name as the root one
            value_a_nested = select(
                literal("nesting").label("n")
            ).cte("value_a")

            # Nesting CTEs takes ascendency locally
            # over the CTEs at a higher level
            value_b = (
                select(value_a_nested.c.n).
                add_cte(value_a_nested, nest_here=True).
                cte("value_b")
            )

            value_ab = select(value_a.c.n.label("a"), value_b.c.n.label("b"))

        Example 5, Non-Linear CTE (SQLAlchemy 1.4.28 and above)::

            edge = Table(
                "edge",
                metadata,
                Column("id", Integer, primary_key=True),
                Column("left", Integer),
                Column("right", Integer),
            )

            root_node = select(literal(1).label("node")).cte(
                "nodes", recursive=True
            )

            left_edge = select(edge.c.left).join(
                root_node, edge.c.right == root_node.c.node
            )
            right_edge = select(edge.c.right).join(
                root_node, edge.c.left == root_node.c.node
            )

            subgraph_cte = root_node.union(left_edge, right_edge)

            subgraph = select(subgraph_cte)

        The above query will render 2 UNIONs inside the recursive CTE::

            WITH RECURSIVE nodes(node) AS (
                    SELECT 1 AS node
                UNION
                    SELECT edge."left" AS "left"
                    FROM edge JOIN nodes ON edge."right" = nodes.node
                UNION
                    SELECT edge."right" AS "right"
                    FROM edge JOIN nodes ON edge."left" = nodes.node
            )
            SELECT nodes.node FROM nodes

        .. seealso::

            :meth:`_orm.Query.cte` - ORM version of
            :meth:`_expression.HasCTE.cte`.

        '''

class Subquery(AliasedReturnsRows):
    '''Represent a subquery of a SELECT.

    A :class:`.Subquery` is created by invoking the
    :meth:`_expression.SelectBase.subquery` method, or for convenience the
    :meth:`_expression.SelectBase.alias` method, on any
    :class:`_expression.SelectBase` subclass
    which includes :class:`_expression.Select`,
    :class:`_expression.CompoundSelect`, and
    :class:`_expression.TextualSelect`.  As rendered in a FROM clause,
    it represents the
    body of the SELECT statement inside of parenthesis, followed by the usual
    "AS <somename>" that defines all "alias" objects.

    The :class:`.Subquery` object is very similar to the
    :class:`_expression.Alias`
    object and can be used in an equivalent way.    The difference between
    :class:`_expression.Alias` and :class:`.Subquery` is that
    :class:`_expression.Alias` always
    contains a :class:`_expression.FromClause` object whereas
    :class:`.Subquery`
    always contains a :class:`_expression.SelectBase` object.

    .. versionadded:: 1.4 The :class:`.Subquery` class was added which now
       serves the purpose of providing an aliased version of a SELECT
       statement.

    '''
    __visit_name__: str
    inherit_cache: bool
    element: SelectBase
    def as_scalar(self) -> ScalarSelect[Any]: ...

class FromGrouping(GroupedElement, FromClause):
    """Represent a grouping of a FROM clause"""
    element: FromClause
    def __init__(self, element: FromClause) -> None: ...
    def columns(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    def c(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    @property
    def primary_key(self) -> Iterable[NamedColumn[Any]]: ...
    @property
    def foreign_keys(self) -> Iterable[ForeignKey]: ...
    def is_derived_from(self, fromclause: FromClause | None) -> bool: ...
    def alias(self, name: str | None = None, flat: bool = False) -> NamedFromGrouping: ...

class NamedFromGrouping(FromGrouping, NamedFromClause):
    """represent a grouping of a named FROM clause

    .. versionadded:: 2.0

    """
    inherit_cache: bool

class TableClause(roles.DMLTableRole, Immutable, NamedFromClause):
    '''Represents a minimal "table" construct.

    This is a lightweight table object that has only a name, a
    collection of columns, which are typically produced
    by the :func:`_expression.column` function, and a schema::

        from sqlalchemy import table, column

        user = table("user",
                column("id"),
                column("name"),
                column("description"),
        )

    The :class:`_expression.TableClause` construct serves as the base for
    the more commonly used :class:`_schema.Table` object, providing
    the usual set of :class:`_expression.FromClause` services including
    the ``.c.`` collection and statement generation methods.

    It does **not** provide all the additional schema-level services
    of :class:`_schema.Table`, including constraints, references to other
    tables, or support for :class:`_schema.MetaData`-level services.
    It\'s useful
    on its own as an ad-hoc construct used to generate quick SQL
    statements when a more fully fledged :class:`_schema.Table`
    is not on hand.

    '''
    __visit_name__: str
    fullname: str
    implicit_returning: bool
    name: Incomplete
    primary_key: Incomplete
    foreign_keys: Incomplete
    schema: Incomplete
    def __init__(self, name: str, *columns: ColumnClause[Any], **kw: Any) -> None: ...
    def columns(self) -> ReadOnlyColumnCollection[str, ColumnClause[Any]]: ...
    def c(self) -> ReadOnlyColumnCollection[str, ColumnClause[Any]]: ...
    def description(self) -> str: ...
    def append_column(self, c: ColumnClause[Any]) -> None: ...
    def insert(self) -> util.preloaded.sql_dml.Insert:
        """Generate an :class:`_sql.Insert` construct against this
        :class:`_expression.TableClause`.

        E.g.::

            table.insert().values(name='foo')

        See :func:`_expression.insert` for argument and usage information.

        """
    def update(self) -> Update:
        """Generate an :func:`_expression.update` construct against this
        :class:`_expression.TableClause`.

        E.g.::

            table.update().where(table.c.id==7).values(name='foo')

        See :func:`_expression.update` for argument and usage information.

        """
    def delete(self) -> Delete:
        """Generate a :func:`_expression.delete` construct against this
        :class:`_expression.TableClause`.

        E.g.::

            table.delete().where(table.c.id==7)

        See :func:`_expression.delete` for argument and usage information.

        """

ForUpdateParameter: Incomplete

class ForUpdateArg(ClauseElement):
    of: Sequence[ClauseElement] | None
    nowait: bool
    read: bool
    skip_locked: bool
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    key_share: Incomplete
    def __init__(self, *, nowait: bool = False, read: bool = False, of: _ForUpdateOfArgument | None = None, skip_locked: bool = False, key_share: bool = False) -> None:
        """Represents arguments specified to
        :meth:`_expression.Select.for_update`.

        """

class Values(roles.InElementRole, Generative, LateralFromClause):
    """Represent a ``VALUES`` construct that can be used as a FROM element
    in a statement.

    The :class:`_expression.Values` object is created from the
    :func:`_expression.values` function.

    .. versionadded:: 1.4

    """
    __visit_name__: str
    name: Incomplete
    literal_binds: Incomplete
    named_with_column: Incomplete
    def __init__(self, *columns: ColumnClause[Any], name: str | None = None, literal_binds: bool = False) -> None: ...
    def alias(self, name: str | None = None, flat: bool = False) -> Self:
        """Return a new :class:`_expression.Values`
        construct that is a copy of this
        one with the given name.

        This method is a VALUES-specific specialization of the
        :meth:`_expression.FromClause.alias` method.

        .. seealso::

            :ref:`tutorial_using_aliases`

            :func:`_expression.alias`

        """
    def lateral(self, name: str | None = None) -> LateralFromClause:
        """Return a new :class:`_expression.Values` with the lateral flag set,
        so that
        it renders as LATERAL.

        .. seealso::

            :func:`_expression.lateral`

        """
    def data(self, values: Sequence[Tuple[Any, ...]]) -> Self:
        """Return a new :class:`_expression.Values` construct,
        adding the given data to the data list.

        E.g.::

            my_values = my_values.data([(1, 'value 1'), (2, 'value2')])

        :param values: a sequence (i.e. list) of tuples that map to the
         column expressions given in the :class:`_expression.Values`
         constructor.

        """
    def scalar_values(self) -> ScalarValues:
        """Returns a scalar ``VALUES`` construct that can be used as a
        COLUMN element in a statement.

        .. versionadded:: 2.0.0b4

        """

class ScalarValues(roles.InElementRole, GroupedElement, ColumnElement[Any]):
    """Represent a scalar ``VALUES`` construct that can be used as a
    COLUMN element in a statement.

    The :class:`_expression.ScalarValues` object is created from the
    :meth:`_expression.Values.scalar_values` method. It's also
    automatically generated when a :class:`_expression.Values` is used in
    an ``IN`` or ``NOT IN`` condition.

    .. versionadded:: 2.0.0b4

    """
    __visit_name__: str
    literal_binds: Incomplete
    def __init__(self, columns: Sequence[ColumnClause[Any]], data: Tuple[Sequence[Tuple[Any, ...]], ...], literal_binds: bool) -> None: ...
    def __clause_element__(self) -> ScalarValues: ...

class SelectBase(roles.SelectStatementRole, roles.DMLSelectRole, roles.CompoundElementRole, roles.InElementRole, HasCTE, SupportsCloneAnnotations, Selectable):
    """Base class for SELECT statements.


    This includes :class:`_expression.Select`,
    :class:`_expression.CompoundSelect` and
    :class:`_expression.TextualSelect`.


    """
    is_select: bool
    def selected_columns(self) -> ColumnCollection[str, ColumnElement[Any]]:
        """A :class:`_expression.ColumnCollection`
        representing the columns that
        this SELECT statement or similar construct returns in its result set.

        This collection differs from the :attr:`_expression.FromClause.columns`
        collection of a :class:`_expression.FromClause` in that the columns
        within this collection cannot be directly nested inside another SELECT
        statement; a subquery must be applied first which provides for the
        necessary parenthesization required by SQL.

        .. note::

            The :attr:`_sql.SelectBase.selected_columns` collection does not
            include expressions established in the columns clause using the
            :func:`_sql.text` construct; these are silently omitted from the
            collection. To use plain textual column expressions inside of a
            :class:`_sql.Select` construct, use the :func:`_sql.literal_column`
            construct.

        .. seealso::

            :attr:`_sql.Select.selected_columns`

        .. versionadded:: 1.4

        """
    @property
    def exported_columns(self) -> ReadOnlyColumnCollection[str, ColumnElement[Any]]:
        '''A :class:`_expression.ColumnCollection`
        that represents the "exported"
        columns of this :class:`_expression.Selectable`, not including
        :class:`_sql.TextClause` constructs.

        The "exported" columns for a :class:`_expression.SelectBase`
        object are synonymous
        with the :attr:`_expression.SelectBase.selected_columns` collection.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_expression.Select.exported_columns`

            :attr:`_expression.Selectable.exported_columns`

            :attr:`_expression.FromClause.exported_columns`


        '''
    @property
    def c(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    @property
    def columns(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    def get_label_style(self) -> SelectLabelStyle:
        """
        Retrieve the current label style.

        Implemented by subclasses.

        """
    def set_label_style(self, style: SelectLabelStyle) -> Self:
        """Return a new selectable with the specified label style.

        Implemented by subclasses.

        """
    def select(self, *arg: Any, **kw: Any) -> Select[Any]: ...
    def as_scalar(self) -> ScalarSelect[Any]: ...
    def exists(self) -> Exists:
        """Return an :class:`_sql.Exists` representation of this selectable,
        which can be used as a column expression.

        The returned object is an instance of :class:`_sql.Exists`.

        .. seealso::

            :func:`_sql.exists`

            :ref:`tutorial_exists` - in the :term:`2.0 style` tutorial.

        .. versionadded:: 1.4

        """
    def scalar_subquery(self) -> ScalarSelect[Any]:
        """Return a 'scalar' representation of this selectable, which can be
        used as a column expression.

        The returned object is an instance of :class:`_sql.ScalarSelect`.

        Typically, a select statement which has only one column in its columns
        clause is eligible to be used as a scalar expression.  The scalar
        subquery can then be used in the WHERE clause or columns clause of
        an enclosing SELECT.

        Note that the scalar subquery differentiates from the FROM-level
        subquery that can be produced using the
        :meth:`_expression.SelectBase.subquery`
        method.

        .. versionchanged: 1.4 - the ``.as_scalar()`` method was renamed to
           :meth:`_expression.SelectBase.scalar_subquery`.

        .. seealso::

            :ref:`tutorial_scalar_subquery` - in the 2.0 tutorial

        """
    def label(self, name: str | None) -> Label[Any]:
        """Return a 'scalar' representation of this selectable, embedded as a
        subquery with a label.

        .. seealso::

            :meth:`_expression.SelectBase.scalar_subquery`.

        """
    def lateral(self, name: str | None = None) -> LateralFromClause:
        """Return a LATERAL alias of this :class:`_expression.Selectable`.

        The return value is the :class:`_expression.Lateral` construct also
        provided by the top-level :func:`_expression.lateral` function.

        .. seealso::

            :ref:`tutorial_lateral_correlation` -  overview of usage.

        """
    def subquery(self, name: str | None = None) -> Subquery:
        """Return a subquery of this :class:`_expression.SelectBase`.

        A subquery is from a SQL perspective a parenthesized, named
        construct that can be placed in the FROM clause of another
        SELECT statement.

        Given a SELECT statement such as::

            stmt = select(table.c.id, table.c.name)

        The above statement might look like::

            SELECT table.id, table.name FROM table

        The subquery form by itself renders the same way, however when
        embedded into the FROM clause of another SELECT statement, it becomes
        a named sub-element::

            subq = stmt.subquery()
            new_stmt = select(subq)

        The above renders as::

            SELECT anon_1.id, anon_1.name
            FROM (SELECT table.id, table.name FROM table) AS anon_1

        Historically, :meth:`_expression.SelectBase.subquery`
        is equivalent to calling
        the :meth:`_expression.FromClause.alias`
        method on a FROM object; however,
        as a :class:`_expression.SelectBase`
        object is not directly  FROM object,
        the :meth:`_expression.SelectBase.subquery`
        method provides clearer semantics.

        .. versionadded:: 1.4

        """
    def alias(self, name: str | None = None, flat: bool = False) -> Subquery:
        """Return a named subquery against this
        :class:`_expression.SelectBase`.

        For a :class:`_expression.SelectBase` (as opposed to a
        :class:`_expression.FromClause`),
        this returns a :class:`.Subquery` object which behaves mostly the
        same as the :class:`_expression.Alias` object that is used with a
        :class:`_expression.FromClause`.

        .. versionchanged:: 1.4 The :meth:`_expression.SelectBase.alias`
           method is now
           a synonym for the :meth:`_expression.SelectBase.subquery` method.

        """

class SelectStatementGrouping(GroupedElement, SelectBase, Generic[_SB]):
    '''Represent a grouping of a :class:`_expression.SelectBase`.

    This differs from :class:`.Subquery` in that we are still
    an "inner" SELECT statement, this is strictly for grouping inside of
    compound selects.

    '''
    __visit_name__: str
    element: _SB
    def __init__(self, element: _SB) -> None: ...
    def get_label_style(self) -> SelectLabelStyle: ...
    def set_label_style(self, label_style: SelectLabelStyle) -> SelectStatementGrouping[_SB]: ...
    @property
    def select_statement(self) -> _SB: ...
    def self_group(self, against: OperatorType | None = None) -> Self: ...
    def selected_columns(self) -> ColumnCollection[str, ColumnElement[Any]]:
        """A :class:`_expression.ColumnCollection`
        representing the columns that
        the embedded SELECT statement returns in its result set, not including
        :class:`_sql.TextClause` constructs.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`_sql.Select.selected_columns`

        """

class GenerativeSelect(SelectBase, Generative):
    """Base class for SELECT statements where additional elements can be
    added.

    This serves as the base for :class:`_expression.Select` and
    :class:`_expression.CompoundSelect`
    where elements such as ORDER BY, GROUP BY can be added and column
    rendering can be controlled.  Compare to
    :class:`_expression.TextualSelect`, which,
    while it subclasses :class:`_expression.SelectBase`
    and is also a SELECT construct,
    represents a fixed textual string which cannot be altered at this level,
    only wrapped as a subquery.

    """
    def __init__(self, _label_style: SelectLabelStyle = ...) -> None: ...
    def with_for_update(self, *, nowait: bool = False, read: bool = False, of: _ForUpdateOfArgument | None = None, skip_locked: bool = False, key_share: bool = False) -> Self:
        """Specify a ``FOR UPDATE`` clause for this
        :class:`_expression.GenerativeSelect`.

        E.g.::

            stmt = select(table).with_for_update(nowait=True)

        On a database like PostgreSQL or Oracle, the above would render a
        statement like::

            SELECT table.a, table.b FROM table FOR UPDATE NOWAIT

        on other backends, the ``nowait`` option is ignored and instead
        would produce::

            SELECT table.a, table.b FROM table FOR UPDATE

        When called with no arguments, the statement will render with
        the suffix ``FOR UPDATE``.   Additional arguments can then be
        provided which allow for common database-specific
        variants.

        :param nowait: boolean; will render ``FOR UPDATE NOWAIT`` on Oracle
         and PostgreSQL dialects.

        :param read: boolean; will render ``LOCK IN SHARE MODE`` on MySQL,
         ``FOR SHARE`` on PostgreSQL.  On PostgreSQL, when combined with
         ``nowait``, will render ``FOR SHARE NOWAIT``.

        :param of: SQL expression or list of SQL expression elements,
         (typically :class:`_schema.Column` objects or a compatible expression,
         for some backends may also be a table expression) which will render
         into a ``FOR UPDATE OF`` clause; supported by PostgreSQL, Oracle, some
         MySQL versions and possibly others. May render as a table or as a
         column depending on backend.

        :param skip_locked: boolean, will render ``FOR UPDATE SKIP LOCKED``
         on Oracle and PostgreSQL dialects or ``FOR SHARE SKIP LOCKED`` if
         ``read=True`` is also specified.

        :param key_share: boolean, will render ``FOR NO KEY UPDATE``,
         or if combined with ``read=True`` will render ``FOR KEY SHARE``,
         on the PostgreSQL dialect.

        """
    def get_label_style(self) -> SelectLabelStyle:
        """
        Retrieve the current label style.

        .. versionadded:: 1.4

        """
    def set_label_style(self, style: SelectLabelStyle) -> Self:
        '''Return a new selectable with the specified label style.

        There are three "label styles" available,
        :attr:`_sql.SelectLabelStyle.LABEL_STYLE_DISAMBIGUATE_ONLY`,
        :attr:`_sql.SelectLabelStyle.LABEL_STYLE_TABLENAME_PLUS_COL`, and
        :attr:`_sql.SelectLabelStyle.LABEL_STYLE_NONE`.   The default style is
        :attr:`_sql.SelectLabelStyle.LABEL_STYLE_TABLENAME_PLUS_COL`.

        In modern SQLAlchemy, there is not generally a need to change the
        labeling style, as per-expression labels are more effectively used by
        making use of the :meth:`_sql.ColumnElement.label` method. In past
        versions, :data:`_sql.LABEL_STYLE_TABLENAME_PLUS_COL` was used to
        disambiguate same-named columns from different tables, aliases, or
        subqueries; the newer :data:`_sql.LABEL_STYLE_DISAMBIGUATE_ONLY` now
        applies labels only to names that conflict with an existing name so
        that the impact of this labeling is minimal.

        The rationale for disambiguation is mostly so that all column
        expressions are available from a given :attr:`_sql.FromClause.c`
        collection when a subquery is created.

        .. versionadded:: 1.4 - the
            :meth:`_sql.GenerativeSelect.set_label_style` method replaces the
            previous combination of ``.apply_labels()``, ``.with_labels()`` and
            ``use_labels=True`` methods and/or parameters.

        .. seealso::

            :data:`_sql.LABEL_STYLE_DISAMBIGUATE_ONLY`

            :data:`_sql.LABEL_STYLE_TABLENAME_PLUS_COL`

            :data:`_sql.LABEL_STYLE_NONE`

            :data:`_sql.LABEL_STYLE_DEFAULT`

        '''
    def limit(self, limit: _LimitOffsetType) -> Self:
        """Return a new selectable with the given LIMIT criterion
        applied.

        This is a numerical value which usually renders as a ``LIMIT``
        expression in the resulting select.  Backends that don't
        support ``LIMIT`` will attempt to provide similar
        functionality.

        .. note::

           The :meth:`_sql.GenerativeSelect.limit` method will replace
           any clause applied with :meth:`_sql.GenerativeSelect.fetch`.

        :param limit: an integer LIMIT parameter, or a SQL expression
         that provides an integer result. Pass ``None`` to reset it.

        .. seealso::

           :meth:`_sql.GenerativeSelect.fetch`

           :meth:`_sql.GenerativeSelect.offset`

        """
    def fetch(self, count: _LimitOffsetType, with_ties: bool = False, percent: bool = False) -> Self:
        """Return a new selectable with the given FETCH FIRST criterion
        applied.

        This is a numeric value which usually renders as
        ``FETCH {FIRST | NEXT} [ count ] {ROW | ROWS} {ONLY | WITH TIES}``
        expression in the resulting select. This functionality is
        is currently implemented for Oracle, PostgreSQL, MSSQL.

        Use :meth:`_sql.GenerativeSelect.offset` to specify the offset.

        .. note::

           The :meth:`_sql.GenerativeSelect.fetch` method will replace
           any clause applied with :meth:`_sql.GenerativeSelect.limit`.

        .. versionadded:: 1.4

        :param count: an integer COUNT parameter, or a SQL expression
         that provides an integer result. When ``percent=True`` this will
         represent the percentage of rows to return, not the absolute value.
         Pass ``None`` to reset it.

        :param with_ties: When ``True``, the WITH TIES option is used
         to return any additional rows that tie for the last place in the
         result set according to the ``ORDER BY`` clause. The
         ``ORDER BY`` may be mandatory in this case. Defaults to ``False``

        :param percent: When ``True``, ``count`` represents the percentage
         of the total number of selected rows to return. Defaults to ``False``

        .. seealso::

           :meth:`_sql.GenerativeSelect.limit`

           :meth:`_sql.GenerativeSelect.offset`

        """
    def offset(self, offset: _LimitOffsetType) -> Self:
        """Return a new selectable with the given OFFSET criterion
        applied.


        This is a numeric value which usually renders as an ``OFFSET``
        expression in the resulting select.  Backends that don't
        support ``OFFSET`` will attempt to provide similar
        functionality.

        :param offset: an integer OFFSET parameter, or a SQL expression
         that provides an integer result. Pass ``None`` to reset it.

        .. seealso::

           :meth:`_sql.GenerativeSelect.limit`

           :meth:`_sql.GenerativeSelect.fetch`

        """
    def slice(self, start: int, stop: int) -> Self:
        """Apply LIMIT / OFFSET to this statement based on a slice.

        The start and stop indices behave like the argument to Python's
        built-in :func:`range` function. This method provides an
        alternative to using ``LIMIT``/``OFFSET`` to get a slice of the
        query.

        For example, ::

            stmt = select(User).order_by(User).id.slice(1, 3)

        renders as

        .. sourcecode:: sql

           SELECT users.id AS users_id,
                  users.name AS users_name
           FROM users ORDER BY users.id
           LIMIT ? OFFSET ?
           (2, 1)

        .. note::

           The :meth:`_sql.GenerativeSelect.slice` method will replace
           any clause applied with :meth:`_sql.GenerativeSelect.fetch`.

        .. versionadded:: 1.4  Added the :meth:`_sql.GenerativeSelect.slice`
           method generalized from the ORM.

        .. seealso::

           :meth:`_sql.GenerativeSelect.limit`

           :meth:`_sql.GenerativeSelect.offset`

           :meth:`_sql.GenerativeSelect.fetch`

        """
    def order_by(self, __first: Literal[None, _NoArg.NO_ARG] | _ColumnExpressionOrStrLabelArgument[Any] = ..., *clauses: _ColumnExpressionOrStrLabelArgument[Any]) -> Self:
        """Return a new selectable with the given list of ORDER BY
        criteria applied.

        e.g.::

            stmt = select(table).order_by(table.c.id, table.c.name)

        Calling this method multiple times is equivalent to calling it once
        with all the clauses concatenated. All existing ORDER BY criteria may
        be cancelled by passing ``None`` by itself.  New ORDER BY criteria may
        then be added by invoking :meth:`_orm.Query.order_by` again, e.g.::

            # will erase all ORDER BY and ORDER BY new_col alone
            stmt = stmt.order_by(None).order_by(new_col)

        :param \\*clauses: a series of :class:`_expression.ColumnElement`
         constructs
         which will be used to generate an ORDER BY clause.

        .. seealso::

            :ref:`tutorial_order_by` - in the :ref:`unified_tutorial`

            :ref:`tutorial_order_by_label` - in the :ref:`unified_tutorial`

        """
    def group_by(self, __first: Literal[None, _NoArg.NO_ARG] | _ColumnExpressionOrStrLabelArgument[Any] = ..., *clauses: _ColumnExpressionOrStrLabelArgument[Any]) -> Self:
        """Return a new selectable with the given list of GROUP BY
        criterion applied.

        All existing GROUP BY settings can be suppressed by passing ``None``.

        e.g.::

            stmt = select(table.c.name, func.max(table.c.stat)).\\\n            group_by(table.c.name)

        :param \\*clauses: a series of :class:`_expression.ColumnElement`
         constructs
         which will be used to generate an GROUP BY clause.

        .. seealso::

            :ref:`tutorial_group_by_w_aggregates` - in the
            :ref:`unified_tutorial`

            :ref:`tutorial_order_by_label` - in the :ref:`unified_tutorial`

        """

class CompoundSelectState(CompileState): ...

class _CompoundSelectKeyword(Enum):
    UNION: str
    UNION_ALL: str
    EXCEPT: str
    EXCEPT_ALL: str
    INTERSECT: str
    INTERSECT_ALL: str

class CompoundSelect(HasCompileState, GenerativeSelect, ExecutableReturnsRows):
    """Forms the basis of ``UNION``, ``UNION ALL``, and other
    SELECT-based set operations.


    .. seealso::

        :func:`_expression.union`

        :func:`_expression.union_all`

        :func:`_expression.intersect`

        :func:`_expression.intersect_all`

        :func:`_expression.except`

        :func:`_expression.except_all`

    """
    __visit_name__: str
    selects: List[SelectBase]
    keyword: Incomplete
    def __init__(self, keyword: _CompoundSelectKeyword, *selects: _SelectStatementForCompoundArgument) -> None: ...
    def self_group(self, against: OperatorType | None = None) -> GroupedElement: ...
    def is_derived_from(self, fromclause: FromClause | None) -> bool: ...
    def set_label_style(self, style: SelectLabelStyle) -> CompoundSelect: ...
    def selected_columns(self) -> ColumnCollection[str, ColumnElement[Any]]:
        """A :class:`_expression.ColumnCollection`
        representing the columns that
        this SELECT statement or similar construct returns in its result set,
        not including :class:`_sql.TextClause` constructs.

        For a :class:`_expression.CompoundSelect`, the
        :attr:`_expression.CompoundSelect.selected_columns`
        attribute returns the selected
        columns of the first SELECT statement contained within the series of
        statements within the set operation.

        .. seealso::

            :attr:`_sql.Select.selected_columns`

        .. versionadded:: 1.4

        """

class SelectState(util.MemoizedSlots, CompileState):
    default_select_compile_options: CacheableOptions
    @classmethod
    def get_plugin_class(cls, statement: Executable) -> Type[SelectState]: ...
    statement: Incomplete
    from_clauses: Incomplete
    froms: Incomplete
    columns_plus_names: Incomplete
    def __init__(self, statement: Select[Any], compiler: SQLCompiler | None, **kw: Any) -> None: ...
    @classmethod
    def get_column_descriptions(cls, statement: Select[Any]) -> List[Dict[str, Any]]: ...
    @classmethod
    def from_statement(cls, statement: Select[Any], from_statement: roles.ReturnsRowsRole) -> ExecutableReturnsRows: ...
    @classmethod
    def get_columns_clause_froms(cls, statement: Select[Any]) -> List[FromClause]: ...
    @classmethod
    def determine_last_joined_entity(cls, stmt: Select[Any]) -> _JoinTargetElement | None: ...
    @classmethod
    def all_selected_columns(cls, statement: Select[Any]) -> _SelectIterable: ...

class _SelectFromElements: ...

class _MemoizedSelectEntities(cache_key.HasCacheKey, traversals.HasCopyInternals, visitors.Traversible):
    '''represents partial state from a Select object, for the case
    where Select.columns() has redefined the set of columns/entities the
    statement will be SELECTing from.  This object represents
    the entities from the SELECT before that transformation was applied,
    so that transformations that were made in terms of the SELECT at that
    time, such as join() as well as options(), can access the correct context.

    In previous SQLAlchemy versions, this wasn\'t needed because these
    constructs calculated everything up front, like when you called join()
    or options(), it did everything to figure out how that would translate
    into specific SQL constructs that would be ready to send directly to the
    SQL compiler when needed.  But as of
    1.4, all of that stuff is done in the compilation phase, during the
    "compile state" portion of the process, so that the work can all be
    cached.  So it needs to be able to resolve joins/options2 based on what
    the list of entities was when those methods were called.


    '''
    __visit_name__: str

class Select(HasPrefixes, HasSuffixes, HasHints, HasCompileState, _SelectFromElements, GenerativeSelect, TypedReturnsRows[_TP]):
    """Represents a ``SELECT`` statement.

    The :class:`_sql.Select` object is normally constructed using the
    :func:`_sql.select` function.  See that function for details.

    .. seealso::

        :func:`_sql.select`

        :ref:`tutorial_selecting_data` - in the 2.0 tutorial

    """
    __visit_name__: str
    def __init__(self, *entities: _ColumnsClauseArgument[Any]) -> None:
        """Construct a new :class:`_expression.Select`.

        The public constructor for :class:`_expression.Select` is the
        :func:`_sql.select` function.

        """
    def filter(self, *criteria: _ColumnExpressionArgument[bool]) -> Self:
        """A synonym for the :meth:`_sql.Select.where` method."""
    @overload
    def scalar_subquery(self) -> ScalarSelect[Any]: ...
    @overload
    def scalar_subquery(self) -> ScalarSelect[_NOT_ENTITY]: ...
    @overload
    def scalar_subquery(self) -> ScalarSelect[Any]: ...
    def filter_by(self, **kwargs: Any) -> Self:
        """apply the given filtering criterion as a WHERE clause
        to this select.

        """
    @property
    def column_descriptions(self) -> Any:
        """Return a :term:`plugin-enabled` 'column descriptions' structure
        referring to the columns which are SELECTed by this statement.

        This attribute is generally useful when using the ORM, as an
        extended structure which includes information about mapped
        entities is returned.  The section :ref:`queryguide_inspection`
        contains more background.

        For a Core-only statement, the structure returned by this accessor
        is derived from the same objects that are returned by the
        :attr:`.Select.selected_columns` accessor, formatted as a list of
        dictionaries which contain the keys ``name``, ``type`` and ``expr``,
        which indicate the column expressions to be selected::

            >>> stmt = select(user_table)
            >>> stmt.column_descriptions
            [
                {
                    'name': 'id',
                    'type': Integer(),
                    'expr': Column('id', Integer(), ...)},
                {
                    'name': 'name',
                    'type': String(length=30),
                    'expr': Column('name', String(length=30), ...)}
            ]

        .. versionchanged:: 1.4.33 The :attr:`.Select.column_descriptions`
           attribute returns a structure for a Core-only set of entities,
           not just ORM-only entities.

        .. seealso::

            :attr:`.UpdateBase.entity_description` - entity information for
            an :func:`.insert`, :func:`.update`, or :func:`.delete`

            :ref:`queryguide_inspection` - ORM background

        """
    def from_statement(self, statement: roles.ReturnsRowsRole) -> ExecutableReturnsRows:
        """Apply the columns which this :class:`.Select` would select
        onto another statement.

        This operation is :term:`plugin-specific` and will raise a not
        supported exception if this :class:`_sql.Select` does not select from
        plugin-enabled entities.


        The statement is typically either a :func:`_expression.text` or
        :func:`_expression.select` construct, and should return the set of
        columns appropriate to the entities represented by this
        :class:`.Select`.

        .. seealso::

            :ref:`orm_queryguide_selecting_text` - usage examples in the
            ORM Querying Guide

        """
    def join(self, target: _JoinTargetArgument, onclause: _OnClauseArgument | None = None, *, isouter: bool = False, full: bool = False) -> Self:
        """Create a SQL JOIN against this :class:`_expression.Select`
        object's criterion
        and apply generatively, returning the newly resulting
        :class:`_expression.Select`.

        E.g.::

            stmt = select(user_table).join(address_table, user_table.c.id == address_table.c.user_id)

        The above statement generates SQL similar to::

            SELECT user.id, user.name FROM user JOIN address ON user.id = address.user_id

        .. versionchanged:: 1.4 :meth:`_expression.Select.join` now creates
           a :class:`_sql.Join` object between a :class:`_sql.FromClause`
           source that is within the FROM clause of the existing SELECT,
           and a given target :class:`_sql.FromClause`, and then adds
           this :class:`_sql.Join` to the FROM clause of the newly generated
           SELECT statement.    This is completely reworked from the behavior
           in 1.3, which would instead create a subquery of the entire
           :class:`_expression.Select` and then join that subquery to the
           target.

           This is a **backwards incompatible change** as the previous behavior
           was mostly useless, producing an unnamed subquery rejected by
           most databases in any case.   The new behavior is modeled after
           that of the very successful :meth:`_orm.Query.join` method in the
           ORM, in order to support the functionality of :class:`_orm.Query`
           being available by using a :class:`_sql.Select` object with an
           :class:`_orm.Session`.

           See the notes for this change at :ref:`change_select_join`.


        :param target: target table to join towards

        :param onclause: ON clause of the join.  If omitted, an ON clause
         is generated automatically based on the :class:`_schema.ForeignKey`
         linkages between the two tables, if one can be unambiguously
         determined, otherwise an error is raised.

        :param isouter: if True, generate LEFT OUTER join.  Same as
         :meth:`_expression.Select.outerjoin`.

        :param full: if True, generate FULL OUTER join.

        .. seealso::

            :ref:`tutorial_select_join` - in the :doc:`/tutorial/index`

            :ref:`orm_queryguide_joins` - in the :ref:`queryguide_toplevel`

            :meth:`_expression.Select.join_from`

            :meth:`_expression.Select.outerjoin`

        """
    def outerjoin_from(self, from_: _FromClauseArgument, target: _JoinTargetArgument, onclause: _OnClauseArgument | None = None, *, full: bool = False) -> Self:
        """Create a SQL LEFT OUTER JOIN against this
        :class:`_expression.Select` object's criterion and apply generatively,
        returning the newly resulting :class:`_expression.Select`.

        Usage is the same as that of :meth:`_selectable.Select.join_from`.

        """
    def join_from(self, from_: _FromClauseArgument, target: _JoinTargetArgument, onclause: _OnClauseArgument | None = None, *, isouter: bool = False, full: bool = False) -> Self:
        """Create a SQL JOIN against this :class:`_expression.Select`
        object's criterion
        and apply generatively, returning the newly resulting
        :class:`_expression.Select`.

        E.g.::

            stmt = select(user_table, address_table).join_from(
                user_table, address_table, user_table.c.id == address_table.c.user_id
            )

        The above statement generates SQL similar to::

            SELECT user.id, user.name, address.id, address.email, address.user_id
            FROM user JOIN address ON user.id = address.user_id

        .. versionadded:: 1.4

        :param from\\_: the left side of the join, will be rendered in the
         FROM clause and is roughly equivalent to using the
         :meth:`.Select.select_from` method.

        :param target: target table to join towards

        :param onclause: ON clause of the join.

        :param isouter: if True, generate LEFT OUTER join.  Same as
         :meth:`_expression.Select.outerjoin`.

        :param full: if True, generate FULL OUTER join.

        .. seealso::

            :ref:`tutorial_select_join` - in the :doc:`/tutorial/index`

            :ref:`orm_queryguide_joins` - in the :ref:`queryguide_toplevel`

            :meth:`_expression.Select.join`

        """
    def outerjoin(self, target: _JoinTargetArgument, onclause: _OnClauseArgument | None = None, *, full: bool = False) -> Self:
        """Create a left outer join.

        Parameters are the same as that of :meth:`_expression.Select.join`.

        .. versionchanged:: 1.4 :meth:`_expression.Select.outerjoin` now
           creates a :class:`_sql.Join` object between a
           :class:`_sql.FromClause` source that is within the FROM clause of
           the existing SELECT, and a given target :class:`_sql.FromClause`,
           and then adds this :class:`_sql.Join` to the FROM clause of the
           newly generated SELECT statement.    This is completely reworked
           from the behavior in 1.3, which would instead create a subquery of
           the entire
           :class:`_expression.Select` and then join that subquery to the
           target.

           This is a **backwards incompatible change** as the previous behavior
           was mostly useless, producing an unnamed subquery rejected by
           most databases in any case.   The new behavior is modeled after
           that of the very successful :meth:`_orm.Query.join` method in the
           ORM, in order to support the functionality of :class:`_orm.Query`
           being available by using a :class:`_sql.Select` object with an
           :class:`_orm.Session`.

           See the notes for this change at :ref:`change_select_join`.

        .. seealso::

            :ref:`tutorial_select_join` - in the :doc:`/tutorial/index`

            :ref:`orm_queryguide_joins` - in the :ref:`queryguide_toplevel`

            :meth:`_expression.Select.join`

        """
    def get_final_froms(self) -> Sequence[FromClause]:
        '''Compute the final displayed list of :class:`_expression.FromClause`
        elements.

        This method will run through the full computation required to
        determine what FROM elements will be displayed in the resulting
        SELECT statement, including shadowing individual tables with
        JOIN objects, as well as full computation for ORM use cases including
        eager loading clauses.

        For ORM use, this accessor returns the **post compilation**
        list of FROM objects; this collection will include elements such as
        eagerly loaded tables and joins.  The objects will **not** be
        ORM enabled and not work as a replacement for the
        :meth:`_sql.Select.select_froms` collection; additionally, the
        method is not well performing for an ORM enabled statement as it
        will incur the full ORM construction process.

        To retrieve the FROM list that\'s implied by the "columns" collection
        passed to the :class:`_sql.Select` originally, use the
        :attr:`_sql.Select.columns_clause_froms` accessor.

        To select from an alternative set of columns while maintaining the
        FROM list, use the :meth:`_sql.Select.with_only_columns` method and
        pass the
        :paramref:`_sql.Select.with_only_columns.maintain_column_froms`
        parameter.

        .. versionadded:: 1.4.23 - the :meth:`_sql.Select.get_final_froms`
           method replaces the previous :attr:`_sql.Select.froms` accessor,
           which is deprecated.

        .. seealso::

            :attr:`_sql.Select.columns_clause_froms`

        '''
    @property
    def froms(self) -> Sequence[FromClause]:
        """Return the displayed list of :class:`_expression.FromClause`
        elements.


        """
    @property
    def columns_clause_froms(self) -> List[FromClause]:
        '''Return the set of :class:`_expression.FromClause` objects implied
        by the columns clause of this SELECT statement.

        .. versionadded:: 1.4.23

        .. seealso::

            :attr:`_sql.Select.froms` - "final" FROM list taking the full
            statement into account

            :meth:`_sql.Select.with_only_columns` - makes use of this
            collection to set up a new FROM list

        '''
    @property
    def inner_columns(self) -> _SelectIterable:
        """An iterator of all :class:`_expression.ColumnElement`
        expressions which would
        be rendered into the columns clause of the resulting SELECT statement.

        This method is legacy as of 1.4 and is superseded by the
        :attr:`_expression.Select.exported_columns` collection.

        """
    def is_derived_from(self, fromclause: FromClause | None) -> bool: ...
    def get_children(self, **kw: Any) -> Iterable[ClauseElement]: ...
    def add_columns(self, *entities: _ColumnsClauseArgument[Any]) -> Select[Any]:
        """Return a new :func:`_expression.select` construct with
        the given entities appended to its columns clause.

        E.g.::

            my_select = my_select.add_columns(table.c.new_column)

        The original expressions in the columns clause remain in place.
        To replace the original expressions with new ones, see the method
        :meth:`_expression.Select.with_only_columns`.

        :param \\*entities: column, table, or other entity expressions to be
         added to the columns clause

        .. seealso::

            :meth:`_expression.Select.with_only_columns` - replaces existing
            expressions rather than appending.

            :ref:`orm_queryguide_select_multiple_entities` - ORM-centric
            example

        """
    def column(self, column: _ColumnsClauseArgument[Any]) -> Select[Any]:
        """Return a new :func:`_expression.select` construct with
        the given column expression added to its columns clause.

        E.g.::

            my_select = my_select.column(table.c.new_column)

        See the documentation for
        :meth:`_expression.Select.with_only_columns`
        for guidelines on adding /replacing the columns of a
        :class:`_expression.Select` object.

        """
    def reduce_columns(self, only_synonyms: bool = True) -> Select[Any]:
        '''Return a new :func:`_expression.select` construct with redundantly
        named, equivalently-valued columns removed from the columns clause.

        "Redundant" here means two columns where one refers to the
        other either based on foreign key, or via a simple equality
        comparison in the WHERE clause of the statement.   The primary purpose
        of this method is to automatically construct a select statement
        with all uniquely-named columns, without the need to use
        table-qualified labels as
        :meth:`_expression.Select.set_label_style`
        does.

        When columns are omitted based on foreign key, the referred-to
        column is the one that\'s kept.  When columns are omitted based on
        WHERE equivalence, the first column in the columns clause is the
        one that\'s kept.

        :param only_synonyms: when True, limit the removal of columns
         to those which have the same name as the equivalent.   Otherwise,
         all columns that are equivalent to another are removed.

        '''
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0]) -> Select[Tuple[_T0]]: ...
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1]) -> Select[Tuple[_T0, _T1]]: ...
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2]) -> Select[Tuple[_T0, _T1, _T2]]: ...
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3]) -> Select[Tuple[_T0, _T1, _T2, _T3]]: ...
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4]) -> Select[Tuple[_T0, _T1, _T2, _T3, _T4]]: ...
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5]) -> Select[Tuple[_T0, _T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6]) -> Select[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6]]: ...
    @overload
    def with_only_columns(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6], __ent7: _TCCA[_T7]) -> Select[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
    @overload
    def with_only_columns(self, *entities: _ColumnsClauseArgument[Any], maintain_column_froms: bool = False, **__kw: Any) -> Select[Any]: ...
    @property
    def whereclause(self) -> ColumnElement[Any] | None:
        """Return the completed WHERE clause for this
        :class:`_expression.Select` statement.

        This assembles the current collection of WHERE criteria
        into a single :class:`_expression.BooleanClauseList` construct.


        .. versionadded:: 1.4

        """
    def where(self, *whereclause: _ColumnExpressionArgument[bool]) -> Self:
        """Return a new :func:`_expression.select` construct with
        the given expression added to
        its WHERE clause, joined to the existing clause via AND, if any.

        """
    def having(self, *having: _ColumnExpressionArgument[bool]) -> Self:
        """Return a new :func:`_expression.select` construct with
        the given expression added to
        its HAVING clause, joined to the existing clause via AND, if any.

        """
    def distinct(self, *expr: _ColumnExpressionArgument[Any]) -> Self:
        """Return a new :func:`_expression.select` construct which
        will apply DISTINCT to its columns clause.

        :param \\*expr: optional column expressions.  When present,
         the PostgreSQL dialect will render a ``DISTINCT ON (<expressions>>)``
         construct.

         .. deprecated:: 1.4 Using \\*expr in other dialects is deprecated
            and will raise :class:`_exc.CompileError` in a future version.

        """
    def select_from(self, *froms: _FromClauseArgument) -> Self:
        '''Return a new :func:`_expression.select` construct with the
        given FROM expression(s)
        merged into its list of FROM objects.

        E.g.::

            table1 = table(\'t1\', column(\'a\'))
            table2 = table(\'t2\', column(\'b\'))
            s = select(table1.c.a).\\\n                select_from(
                    table1.join(table2, table1.c.a==table2.c.b)
                )

        The "from" list is a unique set on the identity of each element,
        so adding an already present :class:`_schema.Table`
        or other selectable
        will have no effect.   Passing a :class:`_expression.Join` that refers
        to an already present :class:`_schema.Table`
        or other selectable will have
        the effect of concealing the presence of that selectable as
        an individual element in the rendered FROM list, instead
        rendering it into a JOIN clause.

        While the typical purpose of :meth:`_expression.Select.select_from`
        is to
        replace the default, derived FROM clause with a join, it can
        also be called with individual table elements, multiple times
        if desired, in the case that the FROM clause cannot be fully
        derived from the columns clause::

            select(func.count(\'*\')).select_from(table1)

        '''
    def correlate(self, *fromclauses: Literal[None, False] | _FromClauseArgument) -> Self:
        '''Return a new :class:`_expression.Select`
        which will correlate the given FROM
        clauses to that of an enclosing :class:`_expression.Select`.

        Calling this method turns off the :class:`_expression.Select` object\'s
        default behavior of "auto-correlation".  Normally, FROM elements
        which appear in a :class:`_expression.Select`
        that encloses this one via
        its :term:`WHERE clause`, ORDER BY, HAVING or
        :term:`columns clause` will be omitted from this
        :class:`_expression.Select`
        object\'s :term:`FROM clause`.
        Setting an explicit correlation collection using the
        :meth:`_expression.Select.correlate`
        method provides a fixed list of FROM objects
        that can potentially take place in this process.

        When :meth:`_expression.Select.correlate`
        is used to apply specific FROM clauses
        for correlation, the FROM elements become candidates for
        correlation regardless of how deeply nested this
        :class:`_expression.Select`
        object is, relative to an enclosing :class:`_expression.Select`
        which refers to
        the same FROM object.  This is in contrast to the behavior of
        "auto-correlation" which only correlates to an immediate enclosing
        :class:`_expression.Select`.
        Multi-level correlation ensures that the link
        between enclosed and enclosing :class:`_expression.Select`
        is always via
        at least one WHERE/ORDER BY/HAVING/columns clause in order for
        correlation to take place.

        If ``None`` is passed, the :class:`_expression.Select`
        object will correlate
        none of its FROM entries, and all will render unconditionally
        in the local FROM clause.

        :param \\*fromclauses: one or more :class:`.FromClause` or other
         FROM-compatible construct such as an ORM mapped entity to become part
         of the correlate collection; alternatively pass a single value
         ``None`` to remove all existing correlations.

        .. seealso::

            :meth:`_expression.Select.correlate_except`

            :ref:`tutorial_scalar_subquery`

        '''
    def correlate_except(self, *fromclauses: Literal[None, False] | _FromClauseArgument) -> Self:
        '''Return a new :class:`_expression.Select`
        which will omit the given FROM
        clauses from the auto-correlation process.

        Calling :meth:`_expression.Select.correlate_except` turns off the
        :class:`_expression.Select` object\'s default behavior of
        "auto-correlation" for the given FROM elements.  An element
        specified here will unconditionally appear in the FROM list, while
        all other FROM elements remain subject to normal auto-correlation
        behaviors.

        If ``None`` is passed, or no arguments are passed,
        the :class:`_expression.Select` object will correlate all of its
        FROM entries.

        :param \\*fromclauses: a list of one or more
         :class:`_expression.FromClause`
         constructs, or other compatible constructs (i.e. ORM-mapped
         classes) to become part of the correlate-exception collection.

        .. seealso::

            :meth:`_expression.Select.correlate`

            :ref:`tutorial_scalar_subquery`

        '''
    def selected_columns(self) -> ColumnCollection[str, ColumnElement[Any]]:
        '''A :class:`_expression.ColumnCollection`
        representing the columns that
        this SELECT statement or similar construct returns in its result set,
        not including :class:`_sql.TextClause` constructs.

        This collection differs from the :attr:`_expression.FromClause.columns`
        collection of a :class:`_expression.FromClause` in that the columns
        within this collection cannot be directly nested inside another SELECT
        statement; a subquery must be applied first which provides for the
        necessary parenthesization required by SQL.

        For a :func:`_expression.select` construct, the collection here is
        exactly what would be rendered inside the "SELECT" statement, and the
        :class:`_expression.ColumnElement` objects are directly present as they
        were given, e.g.::

            col1 = column(\'q\', Integer)
            col2 = column(\'p\', Integer)
            stmt = select(col1, col2)

        Above, ``stmt.selected_columns`` would be a collection that contains
        the ``col1`` and ``col2`` objects directly. For a statement that is
        against a :class:`_schema.Table` or other
        :class:`_expression.FromClause`, the collection will use the
        :class:`_expression.ColumnElement` objects that are in the
        :attr:`_expression.FromClause.c` collection of the from element.

        A use case for the :attr:`_sql.Select.selected_columns` collection is
        to allow the existing columns to be referenced when adding additional
        criteria, e.g.::

            def filter_on_id(my_select, id):
                return my_select.where(my_select.selected_columns[\'id\'] == id)

            stmt = select(MyModel)

            # adds "WHERE id=:param" to the statement
            stmt = filter_on_id(stmt, 42)

        .. note::

            The :attr:`_sql.Select.selected_columns` collection does not
            include expressions established in the columns clause using the
            :func:`_sql.text` construct; these are silently omitted from the
            collection. To use plain textual column expressions inside of a
            :class:`_sql.Select` construct, use the :func:`_sql.literal_column`
            construct.


        .. versionadded:: 1.4

        '''
    def self_group(self, against: OperatorType | None = None) -> SelectStatementGrouping[Self] | Self: ...
    def union(self, *other: _SelectStatementForCompoundArgument) -> CompoundSelect:
        """Return a SQL ``UNION`` of this select() construct against
        the given selectables provided as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28

            multiple elements are now accepted.

        :param \\**kwargs: keyword arguments are forwarded to the constructor
         for the newly created :class:`_sql.CompoundSelect` object.

        """
    def union_all(self, *other: _SelectStatementForCompoundArgument) -> CompoundSelect:
        """Return a SQL ``UNION ALL`` of this select() construct against
        the given selectables provided as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28

            multiple elements are now accepted.

        :param \\**kwargs: keyword arguments are forwarded to the constructor
         for the newly created :class:`_sql.CompoundSelect` object.

        """
    def except_(self, *other: _SelectStatementForCompoundArgument) -> CompoundSelect:
        """Return a SQL ``EXCEPT`` of this select() construct against
        the given selectable provided as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28

            multiple elements are now accepted.

        """
    def except_all(self, *other: _SelectStatementForCompoundArgument) -> CompoundSelect:
        """Return a SQL ``EXCEPT ALL`` of this select() construct against
        the given selectables provided as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28

            multiple elements are now accepted.

        """
    def intersect(self, *other: _SelectStatementForCompoundArgument) -> CompoundSelect:
        """Return a SQL ``INTERSECT`` of this select() construct against
        the given selectables provided as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28

            multiple elements are now accepted.

        :param \\**kwargs: keyword arguments are forwarded to the constructor
         for the newly created :class:`_sql.CompoundSelect` object.

        """
    def intersect_all(self, *other: _SelectStatementForCompoundArgument) -> CompoundSelect:
        """Return a SQL ``INTERSECT ALL`` of this select() construct
        against the given selectables provided as positional arguments.

        :param \\*other: one or more elements with which to create a
         UNION.

         .. versionchanged:: 1.4.28

            multiple elements are now accepted.

        :param \\**kwargs: keyword arguments are forwarded to the constructor
         for the newly created :class:`_sql.CompoundSelect` object.

        """

class ScalarSelect(roles.InElementRole, Generative, GroupedElement, ColumnElement[_T]):
    """Represent a scalar subquery.


    A :class:`_sql.ScalarSelect` is created by invoking the
    :meth:`_sql.SelectBase.scalar_subquery` method.   The object
    then participates in other SQL expressions as a SQL column expression
    within the :class:`_sql.ColumnElement` hierarchy.

    .. seealso::

        :meth:`_sql.SelectBase.scalar_subquery`

        :ref:`tutorial_scalar_subquery` - in the 2.0 tutorial

    """
    inherit_cache: bool
    element: SelectBase
    type: Incomplete
    def __init__(self, element: SelectBase) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    @property
    def columns(self) -> NoReturn: ...
    c = columns
    def where(self, crit: _ColumnExpressionArgument[bool]) -> Self:
        """Apply a WHERE clause to the SELECT statement referred to
        by this :class:`_expression.ScalarSelect`.

        """
    @overload
    def self_group(self, against: OperatorType | None = None) -> ScalarSelect[Any]: ...
    @overload
    def self_group(self, against: OperatorType | None = None) -> ColumnElement[Any]: ...
    def correlate(self, *fromclauses: Literal[None, False] | _FromClauseArgument) -> Self:
        """Return a new :class:`_expression.ScalarSelect`
        which will correlate the given FROM
        clauses to that of an enclosing :class:`_expression.Select`.

        This method is mirrored from the :meth:`_sql.Select.correlate` method
        of the underlying :class:`_sql.Select`.  The method applies the
        :meth:_sql.Select.correlate` method, then returns a new
        :class:`_sql.ScalarSelect` against that statement.

        .. versionadded:: 1.4 Previously, the
           :meth:`_sql.ScalarSelect.correlate`
           method was only available from :class:`_sql.Select`.

        :param \\*fromclauses: a list of one or more
         :class:`_expression.FromClause`
         constructs, or other compatible constructs (i.e. ORM-mapped
         classes) to become part of the correlate collection.

        .. seealso::

            :meth:`_expression.ScalarSelect.correlate_except`

            :ref:`tutorial_scalar_subquery` - in the 2.0 tutorial


        """
    def correlate_except(self, *fromclauses: Literal[None, False] | _FromClauseArgument) -> Self:
        """Return a new :class:`_expression.ScalarSelect`
        which will omit the given FROM
        clauses from the auto-correlation process.

        This method is mirrored from the
        :meth:`_sql.Select.correlate_except` method of the underlying
        :class:`_sql.Select`.  The method applies the
        :meth:_sql.Select.correlate_except` method, then returns a new
        :class:`_sql.ScalarSelect` against that statement.

        .. versionadded:: 1.4 Previously, the
           :meth:`_sql.ScalarSelect.correlate_except`
           method was only available from :class:`_sql.Select`.

        :param \\*fromclauses: a list of one or more
         :class:`_expression.FromClause`
         constructs, or other compatible constructs (i.e. ORM-mapped
         classes) to become part of the correlate-exception collection.

        .. seealso::

            :meth:`_expression.ScalarSelect.correlate`

            :ref:`tutorial_scalar_subquery` - in the 2.0 tutorial


        """

class Exists(UnaryExpression[bool]):
    """Represent an ``EXISTS`` clause.

    See :func:`_sql.exists` for a description of usage.

    An ``EXISTS`` clause can also be constructed from a :func:`_sql.select`
    instance by calling :meth:`_sql.SelectBase.exists`.

    """
    inherit_cache: bool
    element: SelectStatementGrouping[Select[Any]] | ScalarSelect[Any]
    def __init__(self, __argument: _ColumnsClauseArgument[Any] | SelectBase | ScalarSelect[Any] | None = None) -> None: ...
    def select(self) -> Select[Any]:
        """Return a SELECT of this :class:`_expression.Exists`.

        e.g.::

            stmt = exists(some_table.c.id).where(some_table.c.id == 5).select()

        This will produce a statement resembling::

            SELECT EXISTS (SELECT id FROM some_table WHERE some_table = :param) AS anon_1

        .. seealso::

            :func:`_expression.select` - general purpose
            method which allows for arbitrary column lists.

        """
    def correlate(self, *fromclauses: Literal[None, False] | _FromClauseArgument) -> Self:
        """Apply correlation to the subquery noted by this
        :class:`_sql.Exists`.

        .. seealso::

            :meth:`_sql.ScalarSelect.correlate`

        """
    def correlate_except(self, *fromclauses: Literal[None, False] | _FromClauseArgument) -> Self:
        """Apply correlation to the subquery noted by this
        :class:`_sql.Exists`.

        .. seealso::

            :meth:`_sql.ScalarSelect.correlate_except`

        """
    def select_from(self, *froms: _FromClauseArgument) -> Self:
        """Return a new :class:`_expression.Exists` construct,
        applying the given
        expression to the :meth:`_expression.Select.select_from`
        method of the select
        statement contained.

        .. note:: it is typically preferable to build a :class:`_sql.Select`
           statement first, including the desired WHERE clause, then use the
           :meth:`_sql.SelectBase.exists` method to produce an
           :class:`_sql.Exists` object at once.

        """
    def where(self, *clause: _ColumnExpressionArgument[bool]) -> Self:
        """Return a new :func:`_expression.exists` construct with the
        given expression added to
        its WHERE clause, joined to the existing clause via AND, if any.


        .. note:: it is typically preferable to build a :class:`_sql.Select`
           statement first, including the desired WHERE clause, then use the
           :meth:`_sql.SelectBase.exists` method to produce an
           :class:`_sql.Exists` object at once.

        """

class TextualSelect(SelectBase, ExecutableReturnsRows, Generative):
    """Wrap a :class:`_expression.TextClause` construct within a
    :class:`_expression.SelectBase`
    interface.

    This allows the :class:`_expression.TextClause` object to gain a
    ``.c`` collection
    and other FROM-like capabilities such as
    :meth:`_expression.FromClause.alias`,
    :meth:`_expression.SelectBase.cte`, etc.

    The :class:`_expression.TextualSelect` construct is produced via the
    :meth:`_expression.TextClause.columns`
    method - see that method for details.

    .. versionchanged:: 1.4 the :class:`_expression.TextualSelect`
       class was renamed
       from ``TextAsFrom``, to more correctly suit its role as a
       SELECT-oriented object and not a FROM clause.

    .. seealso::

        :func:`_expression.text`

        :meth:`_expression.TextClause.columns` - primary creation interface.

    """
    __visit_name__: str
    is_text: bool
    is_select: bool
    def __init__(self, text: TextClause, columns: List[_ColumnExpressionArgument[Any]], positional: bool = False) -> None: ...
    def selected_columns(self) -> ColumnCollection[str, KeyedColumnElement[Any]]:
        """A :class:`_expression.ColumnCollection`
        representing the columns that
        this SELECT statement or similar construct returns in its result set,
        not including :class:`_sql.TextClause` constructs.

        This collection differs from the :attr:`_expression.FromClause.columns`
        collection of a :class:`_expression.FromClause` in that the columns
        within this collection cannot be directly nested inside another SELECT
        statement; a subquery must be applied first which provides for the
        necessary parenthesization required by SQL.

        For a :class:`_expression.TextualSelect` construct, the collection
        contains the :class:`_expression.ColumnElement` objects that were
        passed to the constructor, typically via the
        :meth:`_expression.TextClause.columns` method.


        .. versionadded:: 1.4

        """
    def set_label_style(self, style: SelectLabelStyle) -> TextualSelect: ...
    element: Incomplete
    def bindparams(self, *binds: BindParameter[Any], **bind_as_values: Any) -> Self: ...
TextAsFrom = TextualSelect

class AnnotatedFromClause(Annotated):
    def c(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]:
        """proxy the .c collection of the underlying FromClause.

        Originally implemented in 2008 as a simple load of the .c collection
        when the annotated construct was created (see d3621ae961a), in modern
        SQLAlchemy versions this can be expensive for statements constructed
        with ORM aliases.   So for #8796 SQLAlchemy 2.0 we instead proxy
        it, which works just as well.

        Two different use cases seem to require the collection either copied
        from the underlying one, or unique to this AnnotatedFromClause.

        See test_selectable->test_annotated_corresponding_column

        """
