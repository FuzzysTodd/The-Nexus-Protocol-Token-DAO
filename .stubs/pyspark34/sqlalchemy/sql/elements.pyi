from . import coercions as coercions, operators as operators, roles as roles, traversals as traversals, type_api as type_api
from .. import exc as exc, inspection as inspection, util as util
from ..engine import Connection as Connection, Dialect as Dialect, Engine as Engine
from ..engine.interfaces import CacheStats as CacheStats, CompiledCacheType as CompiledCacheType, CoreExecuteOptionsParameter as CoreExecuteOptionsParameter, SchemaTranslateMapType as SchemaTranslateMapType
from ..engine.result import Result as Result
from ..util import HasMemoized_ro_memoized_attribute as HasMemoized_ro_memoized_attribute, TypingOnly as TypingOnly
from ..util.typing import Literal as Literal, Self as Self
from ._typing import _ColumnExpressionArgument, _InfoType, _TypeEngineArgument, has_schema_attr as has_schema_attr, is_named_from_clause as is_named_from_clause, is_quoted_name as is_quoted_name, is_tuple_type as is_tuple_type
from .annotation import Annotated as Annotated, SupportsWrappingAnnotations as SupportsWrappingAnnotations
from .base import Executable as Executable, Generative as Generative, HasMemoized as HasMemoized, Immutable as Immutable, NO_ARG as NO_ARG, SingletonConstant as SingletonConstant, _NoArg
from .cache_key import CacheKey as CacheKey, MemoizedHasCacheKey as MemoizedHasCacheKey, NO_CACHE as NO_CACHE
from .compiler import Compiled as Compiled, SQLCompiler as SQLCompiler
from .functions import FunctionElement as FunctionElement
from .operators import ColumnOperators as ColumnOperators, OperatorType as OperatorType
from .schema import Column as Column, DefaultGenerator as DefaultGenerator, FetchedValue as FetchedValue, ForeignKey as ForeignKey
from .selectable import FromClause as FromClause, NamedFromClause as NamedFromClause, TextualSelect as TextualSelect
from .sqltypes import TupleType as TupleType
from .traversals import HasCopyInternals as HasCopyInternals
from .type_api import TypeEngine as TypeEngine
from .visitors import ExternallyTraversible as ExternallyTraversible, InternalTraversal as InternalTraversal, Visitable as Visitable, cloned_traverse as cloned_traverse, traverse as traverse
from _typeshed import Incomplete
from enum import IntEnum
from typing import AbstractSet, Any, Callable, Dict, FrozenSet, Generic, Iterable, Iterator, List, Mapping, Sequence, Tuple as typing_Tuple, Type, overload

@overload
def literal(value: Any, type_: _TypeEngineArgument[_T], literal_execute: bool = False) -> BindParameter[_T]: ...
@overload
def literal(value: _T, type_: None = None, literal_execute: bool = False) -> BindParameter[_T]: ...
@overload
def literal(value: Any, type_: _TypeEngineArgument[Any] | None = None, literal_execute: bool = False) -> BindParameter[Any]: ...
def literal_column(text: str, type_: _TypeEngineArgument[_T] | None = None) -> ColumnClause[_T]:
    '''Produce a :class:`.ColumnClause` object that has the
    :paramref:`_expression.column.is_literal` flag set to True.

    :func:`_expression.literal_column` is similar to
    :func:`_expression.column`, except that
    it is more often used as a "standalone" column expression that renders
    exactly as stated; while :func:`_expression.column`
    stores a string name that
    will be assumed to be part of a table and may be quoted as such,
    :func:`_expression.literal_column` can be that,
    or any other arbitrary column-oriented
    expression.

    :param text: the text of the expression; can be any SQL expression.
      Quoting rules will not be applied. To specify a column-name expression
      which should be subject to quoting rules, use the :func:`column`
      function.

    :param type\\_: an optional :class:`~sqlalchemy.types.TypeEngine`
      object which will
      provide result-set translation and additional expression semantics for
      this column. If left as ``None`` the type will be :class:`.NullType`.

    .. seealso::

        :func:`_expression.column`

        :func:`_expression.text`

        :ref:`tutorial_select_arbitrary_text`

    '''

class CompilerElement(Visitable):
    """base class for SQL elements that can be compiled to produce a
    SQL string.

    .. versionadded:: 2.0

    """
    __visit_name__: str
    supports_execution: bool
    stringify_dialect: str
    def compile(self, bind: Engine | Connection | None = None, dialect: Dialect | None = None, **kw: Any) -> Compiled:
        '''Compile this SQL expression.

        The return value is a :class:`~.Compiled` object.
        Calling ``str()`` or ``unicode()`` on the returned value will yield a
        string representation of the result. The
        :class:`~.Compiled` object also can return a
        dictionary of bind parameter names and values
        using the ``params`` accessor.

        :param bind: An :class:`.Connection` or :class:`.Engine` which
           can provide a :class:`.Dialect` in order to generate a
           :class:`.Compiled` object.  If the ``bind`` and
           ``dialect`` parameters are both omitted, a default SQL compiler
           is used.

        :param column_keys: Used for INSERT and UPDATE statements, a list of
            column names which should be present in the VALUES clause of the
            compiled statement. If ``None``, all columns from the target table
            object are rendered.

        :param dialect: A :class:`.Dialect` instance which can generate
            a :class:`.Compiled` object.  This argument takes precedence over
            the ``bind`` argument.

        :param compile_kwargs: optional dictionary of additional parameters
            that will be passed through to the compiler within all "visit"
            methods.  This allows any custom flag to be passed through to
            a custom compilation construct, for example.  It is also used
            for the case of passing the ``literal_binds`` flag through::

                from sqlalchemy.sql import table, column, select

                t = table(\'t\', column(\'x\'))

                s = select(t).where(t.c.x == 5)

                print(s.compile(compile_kwargs={"literal_binds": True}))

        .. seealso::

            :ref:`faq_sql_expression_string`

        '''

class ClauseElement(SupportsWrappingAnnotations, MemoizedHasCacheKey, HasCopyInternals, ExternallyTraversible, CompilerElement):
    """Base class for elements of a programmatically constructed SQL
    expression.

    """
    __visit_name__: str
    def description(self) -> str | None: ...
    is_clause_element: bool
    is_selectable: bool
    is_dml: bool
    negation_clause: ColumnElement[bool]
    def get_children(self, *, omit_attrs: typing_Tuple[str, ...] = ..., **kw: Any) -> Iterable[ClauseElement]: ...
    @property
    def entity_namespace(self) -> None: ...
    def unique_params(self, __optionaldict: Dict[str, Any] | None = None, **kwargs: Any) -> Self:
        """Return a copy with :func:`_expression.bindparam` elements
        replaced.

        Same functionality as :meth:`_expression.ClauseElement.params`,
        except adds `unique=True`
        to affected bind parameters so that multiple statements can be
        used.

        """
    def params(self, __optionaldict: Mapping[str, Any] | None = None, **kwargs: Any) -> Self:
        """Return a copy with :func:`_expression.bindparam` elements
        replaced.

        Returns a copy of this ClauseElement with
        :func:`_expression.bindparam`
        elements replaced with values taken from the given dictionary::

          >>> clause = column('x') + bindparam('foo')
          >>> print(clause.compile().params)
          {'foo':None}
          >>> print(clause.params({'foo':7}).compile().params)
          {'foo':7}

        """
    def compare(self, other: ClauseElement, **kw: Any) -> bool:
        """Compare this :class:`_expression.ClauseElement` to
        the given :class:`_expression.ClauseElement`.

        Subclasses should override the default behavior, which is a
        straight identity comparison.

        \\**kw are arguments consumed by subclass ``compare()`` methods and
        may be used to modify the criteria for comparison
        (see :class:`_expression.ColumnElement`).

        """
    def self_group(self, against: OperatorType | None = None) -> ClauseElement:
        '''Apply a \'grouping\' to this :class:`_expression.ClauseElement`.

        This method is overridden by subclasses to return a "grouping"
        construct, i.e. parenthesis.   In particular it\'s used by "binary"
        expressions to provide a grouping around themselves when placed into a
        larger expression, as well as by :func:`_expression.select`
        constructs when placed into the FROM clause of another
        :func:`_expression.select`.  (Note that subqueries should be
        normally created using the :meth:`_expression.Select.alias` method,
        as many
        platforms require nested SELECT statements to be named).

        As expressions are composed together, the application of
        :meth:`self_group` is automatic - end-user code should never
        need to use this method directly.  Note that SQLAlchemy\'s
        clause constructs take operator precedence into account -
        so parenthesis might not be needed, for example, in
        an expression like ``x OR (y AND z)`` - AND takes precedence
        over OR.

        The base :meth:`self_group` method of
        :class:`_expression.ClauseElement`
        just returns self.
        '''
    def __invert__(self): ...
    def __bool__(self) -> bool: ...

class DQLDMLClauseElement(ClauseElement):
    """represents a :class:`.ClauseElement` that compiles to a DQL or DML
    expression, not DDL.

    .. versionadded:: 2.0

    """
    def compile(self, bind: Engine | Connection | None = None, dialect: Dialect | None = None, **kw: Any) -> SQLCompiler: ...

class CompilerColumnElement(roles.DMLColumnRole, roles.DDLConstraintColumnRole, roles.ColumnsClauseRole, CompilerElement):
    """A compiler-only column element used for ad-hoc string compilations.

    .. versionadded:: 2.0

    """

class SQLCoreOperations(ColumnOperators, TypingOnly, Generic[_T_co]):
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    @overload
    def op(self, opstring: str, precedence: int = ..., is_comparison: bool = ..., *, return_type: _TypeEngineArgument[_OPT], python_impl: Callable[..., Any] | None = None) -> Callable[[Any], BinaryExpression[_OPT]]: ...
    @overload
    def op(self, opstring: str, precedence: int = ..., is_comparison: bool = ..., return_type: _TypeEngineArgument[Any] | None = ..., python_impl: Callable[..., Any] | None = ...) -> Callable[[Any], BinaryExpression[Any]]: ...
    def bool_op(self, opstring: str, precedence: int = 0, python_impl: Callable[..., Any] | None = None) -> Callable[[Any], BinaryExpression[bool]]: ...
    def __and__(self, other: Any) -> BooleanClauseList: ...
    def __or__(self, other: Any) -> BooleanClauseList: ...
    def __invert__(self) -> ColumnElement[_T_co]: ...
    def __lt__(self, other: Any) -> ColumnElement[bool]: ...
    def __le__(self, other: Any) -> ColumnElement[bool]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> ColumnElement[bool]: ...
    def __ne__(self, other: Any) -> ColumnElement[bool]: ...
    def is_distinct_from(self, other: Any) -> ColumnElement[bool]: ...
    def is_not_distinct_from(self, other: Any) -> ColumnElement[bool]: ...
    def __gt__(self, other: Any) -> ColumnElement[bool]: ...
    def __ge__(self, other: Any) -> ColumnElement[bool]: ...
    def __neg__(self) -> UnaryExpression[_T_co]: ...
    def __contains__(self, other: Any) -> ColumnElement[bool]: ...
    def __getitem__(self, index: Any) -> ColumnElement[Any]: ...
    @overload
    def __lshift__(self, other: Any) -> ColumnElement[int]: ...
    @overload
    def __lshift__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __rshift__(self, other: Any) -> ColumnElement[int]: ...
    @overload
    def __rshift__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def concat(self, other: Any) -> ColumnElement[str]: ...
    @overload
    def concat(self, other: Any) -> ColumnElement[Any]: ...
    def like(self, other: Any, escape: str | None = None) -> BinaryExpression[bool]: ...
    def ilike(self, other: Any, escape: str | None = None) -> BinaryExpression[bool]: ...
    def bitwise_xor(self, other: Any) -> BinaryExpression[Any]: ...
    def bitwise_or(self, other: Any) -> BinaryExpression[Any]: ...
    def bitwise_and(self, other: Any) -> BinaryExpression[Any]: ...
    def bitwise_not(self) -> UnaryExpression[_T_co]: ...
    def bitwise_lshift(self, other: Any) -> BinaryExpression[Any]: ...
    def bitwise_rshift(self, other: Any) -> BinaryExpression[Any]: ...
    def in_(self, other: Iterable[Any] | BindParameter[Any] | roles.InElementRole) -> BinaryExpression[bool]: ...
    def not_in(self, other: Iterable[Any] | BindParameter[Any] | roles.InElementRole) -> BinaryExpression[bool]: ...
    def notin_(self, other: Iterable[Any] | BindParameter[Any] | roles.InElementRole) -> BinaryExpression[bool]: ...
    def not_like(self, other: Any, escape: str | None = None) -> BinaryExpression[bool]: ...
    def notlike(self, other: Any, escape: str | None = None) -> BinaryExpression[bool]: ...
    def not_ilike(self, other: Any, escape: str | None = None) -> BinaryExpression[bool]: ...
    def notilike(self, other: Any, escape: str | None = None) -> BinaryExpression[bool]: ...
    def is_(self, other: Any) -> BinaryExpression[bool]: ...
    def is_not(self, other: Any) -> BinaryExpression[bool]: ...
    def isnot(self, other: Any) -> BinaryExpression[bool]: ...
    def startswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnElement[bool]: ...
    def istartswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnElement[bool]: ...
    def endswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnElement[bool]: ...
    def iendswith(self, other: Any, escape: str | None = None, autoescape: bool = False) -> ColumnElement[bool]: ...
    def contains(self, other: Any, **kw: Any) -> ColumnElement[bool]: ...
    def icontains(self, other: Any, **kw: Any) -> ColumnElement[bool]: ...
    def match(self, other: Any, **kwargs: Any) -> ColumnElement[bool]: ...
    def regexp_match(self, pattern: Any, flags: str | None = None) -> ColumnElement[bool]: ...
    def regexp_replace(self, pattern: Any, replacement: Any, flags: str | None = None) -> ColumnElement[str]: ...
    def desc(self) -> UnaryExpression[_T_co]: ...
    def asc(self) -> UnaryExpression[_T_co]: ...
    def nulls_first(self) -> UnaryExpression[_T_co]: ...
    def nullsfirst(self) -> UnaryExpression[_T_co]: ...
    def nulls_last(self) -> UnaryExpression[_T_co]: ...
    def nullslast(self) -> UnaryExpression[_T_co]: ...
    def collate(self, collation: str) -> CollationClause: ...
    def between(self, cleft: Any, cright: Any, symmetric: bool = False) -> BinaryExpression[bool]: ...
    def distinct(self) -> UnaryExpression[_T_co]: ...
    def any_(self) -> CollectionAggregate[Any]: ...
    def all_(self) -> CollectionAggregate[Any]: ...
    @overload
    def __add__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __add__(self, other: Any) -> ColumnElement[str]: ...
    @overload
    def __radd__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __radd__(self, other: Any) -> ColumnElement[str]: ...
    @overload
    def __sub__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __sub__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __rsub__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __rsub__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __mul__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __mul__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __rmul__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __rmul__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __mod__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __mod__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __rmod__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __rmod__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __truediv__(self, other: Any) -> ColumnElement[_NUMERIC]: ...
    @overload
    def __truediv__(self, other: Any) -> ColumnElement[_NT]: ...
    @overload
    def __truediv__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __rtruediv__(self, other: Any) -> ColumnElement[_NUMERIC]: ...
    @overload
    def __rtruediv__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __floordiv__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __floordiv__(self, other: Any) -> ColumnElement[Any]: ...
    @overload
    def __rfloordiv__(self, other: Any) -> ColumnElement[_NMT]: ...
    @overload
    def __rfloordiv__(self, other: Any) -> ColumnElement[Any]: ...

class SQLColumnExpression(SQLCoreOperations[_T_co], roles.ExpressionElementRole[_T_co], TypingOnly):
    """A type that may be used to indicate any SQL column element or object
    that acts in place of one.

    :class:`.SQLColumnExpression` is a base of
    :class:`.ColumnElement`, as well as within the bases of ORM elements
    such as :class:`.InstrumentedAttribute`, and may be used in :pep:`484`
    typing to indicate arguments or return values that should behave
    as column expressions.

    .. versionadded:: 2.0.0b4


    """

class ColumnElement(roles.ColumnArgumentOrKeyRole, roles.StatementOptionRole, roles.WhereHavingRole, roles.BinaryElementRole[_T], roles.OrderByRole, roles.ColumnsClauseRole, roles.LimitOffsetRole, roles.DMLColumnRole, roles.DDLConstraintColumnRole, roles.DDLExpressionRole, SQLColumnExpression[_T], DQLDMLClauseElement):
    '''Represent a column-oriented SQL expression suitable for usage in the
    "columns" clause, WHERE clause etc. of a statement.

    While the most familiar kind of :class:`_expression.ColumnElement` is the
    :class:`_schema.Column` object, :class:`_expression.ColumnElement`
    serves as the basis
    for any unit that may be present in a SQL expression, including
    the expressions themselves, SQL functions, bound parameters,
    literal expressions, keywords such as ``NULL``, etc.
    :class:`_expression.ColumnElement`
    is the ultimate base class for all such elements.

    A wide variety of SQLAlchemy Core functions work at the SQL expression
    level, and are intended to accept instances of
    :class:`_expression.ColumnElement` as
    arguments.  These functions will typically document that they accept a
    "SQL expression" as an argument.  What this means in terms of SQLAlchemy
    usually refers to an input which is either already in the form of a
    :class:`_expression.ColumnElement` object,
    or a value which can be **coerced** into
    one.  The coercion rules followed by most, but not all, SQLAlchemy Core
    functions with regards to SQL expressions are as follows:

        * a literal Python value, such as a string, integer or floating
          point value, boolean, datetime, ``Decimal`` object, or virtually
          any other Python object, will be coerced into a "literal bound
          value".  This generally means that a :func:`.bindparam` will be
          produced featuring the given value embedded into the construct; the
          resulting :class:`.BindParameter` object is an instance of
          :class:`_expression.ColumnElement`.
          The Python value will ultimately be sent
          to the DBAPI at execution time as a parameterized argument to the
          ``execute()`` or ``executemany()`` methods, after SQLAlchemy
          type-specific converters (e.g. those provided by any associated
          :class:`.TypeEngine` objects) are applied to the value.

        * any special object value, typically ORM-level constructs, which
          feature an accessor called ``__clause_element__()``.  The Core
          expression system looks for this method when an object of otherwise
          unknown type is passed to a function that is looking to coerce the
          argument into a :class:`_expression.ColumnElement` and sometimes a
          :class:`_expression.SelectBase` expression.
          It is used within the ORM to
          convert from ORM-specific objects like mapped classes and
          mapped attributes into Core expression objects.

        * The Python ``None`` value is typically interpreted as ``NULL``,
          which in SQLAlchemy Core produces an instance of :func:`.null`.

    A :class:`_expression.ColumnElement` provides the ability to generate new
    :class:`_expression.ColumnElement`
    objects using Python expressions.  This means that Python operators
    such as ``==``, ``!=`` and ``<`` are overloaded to mimic SQL operations,
    and allow the instantiation of further :class:`_expression.ColumnElement`
    instances
    which are composed from other, more fundamental
    :class:`_expression.ColumnElement`
    objects.  For example, two :class:`.ColumnClause` objects can be added
    together with the addition operator ``+`` to produce
    a :class:`.BinaryExpression`.
    Both :class:`.ColumnClause` and :class:`.BinaryExpression` are subclasses
    of :class:`_expression.ColumnElement`:

    .. sourcecode:: pycon+sql

        >>> from sqlalchemy.sql import column
        >>> column(\'a\') + column(\'b\')
        <sqlalchemy.sql.expression.BinaryExpression object at 0x101029dd0>
        >>> print(column(\'a\') + column(\'b\'))
        {printsql}a + b

    .. seealso::

        :class:`_schema.Column`

        :func:`_expression.column`

    '''
    __visit_name__: str
    primary_key: bool
    foreign_keys: AbstractSet[ForeignKey]
    key: str | None
    @overload
    def self_group(self, against: OperatorType | None = None) -> ColumnElement[_T]: ...
    @overload
    def self_group(self, against: OperatorType | None = None) -> ColumnElement[Any]: ...
    type: TypeEngine[_T]
    def comparator(self) -> TypeEngine.Comparator[_T]: ...
    def __getattr__(self, key: str) -> Any: ...
    def operate(self, op: operators.OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: operators.OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    @property
    def expression(self) -> ColumnElement[Any]:
        """Return a column expression.

        Part of the inspection interface; returns self.

        """
    def base_columns(self) -> FrozenSet[ColumnElement[Any]]: ...
    def proxy_set(self) -> FrozenSet[ColumnElement[Any]]:
        """set of all columns we are proxying

        as of 2.0 this is explicitly deannotated columns.  previously it was
        effectively deannotated columns but wasn't enforced.  annotated
        columns should basically not go into sets if at all possible because
        their hashing behavior is very non-performant.

        """
    def shares_lineage(self, othercolumn: ColumnElement[Any]) -> bool:
        """Return True if the given :class:`_expression.ColumnElement`
        has a common ancestor to this :class:`_expression.ColumnElement`."""
    def cast(self, type_: _TypeEngineArgument[_OPT]) -> Cast[_OPT]:
        """Produce a type cast, i.e. ``CAST(<expression> AS <type>)``.

        This is a shortcut to the :func:`_expression.cast` function.

        .. seealso::

            :ref:`tutorial_casts`

            :func:`_expression.cast`

            :func:`_expression.type_coerce`

        """
    def label(self, name: str | None) -> Label[_T]:
        """Produce a column label, i.e. ``<columnname> AS <name>``.

        This is a shortcut to the :func:`_expression.label` function.

        If 'name' is ``None``, an anonymous label name will be generated.

        """
    @property
    def anon_label(self) -> str: ...
    @property
    def anon_key_label(self) -> str: ...

class KeyedColumnElement(ColumnElement[_T]):
    """ColumnElement where ``.key`` is non-None."""
    key: str

class WrapsColumnExpression(ColumnElement[_T]):
    """Mixin that defines a :class:`_expression.ColumnElement`
    as a wrapper with special
    labeling behavior for an expression that already has a name.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`change_4449`


    """
    @property
    def wrapped_column_expression(self) -> ColumnElement[_T]: ...

class BindParameter(roles.InElementRole, KeyedColumnElement[_T]):
    '''Represent a "bound expression".

    :class:`.BindParameter` is invoked explicitly using the
    :func:`.bindparam` function, as in::

        from sqlalchemy import bindparam

        stmt = select(users_table).\\\n                    where(users_table.c.name == bindparam(\'username\'))

    Detailed discussion of how :class:`.BindParameter` is used is
    at :func:`.bindparam`.

    .. seealso::

        :func:`.bindparam`

    '''
    __visit_name__: str
    key: str
    type: TypeEngine[_T]
    value: _T | None
    inherit_cache: bool
    unique: Incomplete
    callable: Incomplete
    isoutparam: Incomplete
    required: Incomplete
    expanding: Incomplete
    expand_op: Incomplete
    literal_execute: Incomplete
    def __init__(self, key: str | None, value: Any = ..., type_: _TypeEngineArgument[_T] | None = None, unique: bool = False, required: bool | Literal[_NoArg.NO_ARG] = ..., quote: bool | None = None, callable_: Callable[[], Any] | None = None, expanding: bool = False, isoutparam: bool = False, literal_execute: bool = False, _compared_to_operator: OperatorType | None = None, _compared_to_type: TypeEngine[Any] | None = None, _is_crud: bool = False) -> None: ...
    @property
    def effective_value(self) -> _T | None:
        """Return the value of this bound parameter,
        taking into account if the ``callable`` parameter
        was set.

        The ``callable`` value will be evaluated
        and returned if present, else ``value``.

        """
    def render_literal_execute(self) -> BindParameter[_T]:
        """Produce a copy of this bound parameter that will enable the
        :paramref:`_sql.BindParameter.literal_execute` flag.

        The :paramref:`_sql.BindParameter.literal_execute` flag will
        have the effect of the parameter rendered in the compiled SQL
        string using ``[POSTCOMPILE]`` form, which is a special form that
        is converted to be a rendering of the literal value of the parameter
        at SQL execution time.    The rationale is to support caching
        of SQL statement strings that can embed per-statement literal values,
        such as LIMIT and OFFSET parameters, in the final SQL string that
        is passed to the DBAPI.   Dialects in particular may want to use
        this method within custom compilation schemes.

        .. versionadded:: 1.4.5

        .. seealso::

            :ref:`engine_thirdparty_caching`

        """

class TypeClause(DQLDMLClauseElement):
    """Handle a type keyword in a SQL statement.

    Used by the ``Case`` statement.

    """
    __visit_name__: str
    type: Incomplete
    def __init__(self, type_) -> None: ...

class TextClause(roles.DDLConstraintColumnRole, roles.DDLExpressionRole, roles.StatementOptionRole, roles.WhereHavingRole, roles.OrderByRole, roles.FromClauseRole, roles.SelectStatementRole, roles.InElementRole, Generative, Executable, DQLDMLClauseElement, roles.BinaryElementRole[Any], inspection.Inspectable['TextClause']):
    '''Represent a literal SQL text fragment.

    E.g.::

        from sqlalchemy import text

        t = text("SELECT * FROM users")
        result = connection.execute(t)


    The :class:`_expression.TextClause` construct is produced using the
    :func:`_expression.text`
    function; see that function for full documentation.

    .. seealso::

        :func:`_expression.text`

    '''
    __visit_name__: str
    def __and__(self, other): ...
    key: str | None
    text: Incomplete
    def __init__(self, text: str) -> None: ...
    def bindparams(self, *binds: BindParameter[Any], **names_to_values: Any) -> Self:
        '''Establish the values and/or types of bound parameters within
        this :class:`_expression.TextClause` construct.

        Given a text construct such as::

            from sqlalchemy import text
            stmt = text("SELECT id, name FROM user WHERE name=:name "
                        "AND timestamp=:timestamp")

        the :meth:`_expression.TextClause.bindparams`
        method can be used to establish
        the initial value of ``:name`` and ``:timestamp``,
        using simple keyword arguments::

            stmt = stmt.bindparams(name=\'jack\',
                        timestamp=datetime.datetime(2012, 10, 8, 15, 12, 5))

        Where above, new :class:`.BindParameter` objects
        will be generated with the names ``name`` and ``timestamp``, and
        values of ``jack`` and ``datetime.datetime(2012, 10, 8, 15, 12, 5)``,
        respectively.  The types will be
        inferred from the values given, in this case :class:`.String` and
        :class:`.DateTime`.

        When specific typing behavior is needed, the positional ``*binds``
        argument can be used in which to specify :func:`.bindparam` constructs
        directly.  These constructs must include at least the ``key``
        argument, then an optional value and type::

            from sqlalchemy import bindparam
            stmt = stmt.bindparams(
                            bindparam(\'name\', value=\'jack\', type_=String),
                            bindparam(\'timestamp\', type_=DateTime)
                        )

        Above, we specified the type of :class:`.DateTime` for the
        ``timestamp`` bind, and the type of :class:`.String` for the ``name``
        bind.  In the case of ``name`` we also set the default value of
        ``"jack"``.

        Additional bound parameters can be supplied at statement execution
        time, e.g.::

            result = connection.execute(stmt,
                        timestamp=datetime.datetime(2012, 10, 8, 15, 12, 5))

        The :meth:`_expression.TextClause.bindparams`
        method can be called repeatedly,
        where it will re-use existing :class:`.BindParameter` objects to add
        new information.  For example, we can call
        :meth:`_expression.TextClause.bindparams`
        first with typing information, and a
        second time with value information, and it will be combined::

            stmt = text("SELECT id, name FROM user WHERE name=:name "
                        "AND timestamp=:timestamp")
            stmt = stmt.bindparams(
                bindparam(\'name\', type_=String),
                bindparam(\'timestamp\', type_=DateTime)
            )
            stmt = stmt.bindparams(
                name=\'jack\',
                timestamp=datetime.datetime(2012, 10, 8, 15, 12, 5)
            )

        The :meth:`_expression.TextClause.bindparams`
        method also supports the concept of
        **unique** bound parameters.  These are parameters that are
        "uniquified" on name at statement compilation time, so that  multiple
        :func:`_expression.text`
        constructs may be combined together without the names
        conflicting.  To use this feature, specify the
        :paramref:`.BindParameter.unique` flag on each :func:`.bindparam`
        object::

            stmt1 = text("select id from table where name=:name").bindparams(
                bindparam("name", value=\'name1\', unique=True)
            )
            stmt2 = text("select id from table where name=:name").bindparams(
                bindparam("name", value=\'name2\', unique=True)
            )

            union = union_all(
                stmt1.columns(column("id")),
                stmt2.columns(column("id"))
            )

        The above statement will render as::

            select id from table where name=:name_1
            UNION ALL select id from table where name=:name_2

        .. versionadded:: 1.3.11  Added support for the
           :paramref:`.BindParameter.unique` flag to work with
           :func:`_expression.text`
           constructs.

        '''
    def columns(self, *cols: _ColumnExpressionArgument[Any], **types: TypeEngine[Any]) -> TextualSelect:
        '''Turn this :class:`_expression.TextClause` object into a
        :class:`_expression.TextualSelect`
        object that serves the same role as a SELECT
        statement.

        The :class:`_expression.TextualSelect` is part of the
        :class:`_expression.SelectBase`
        hierarchy and can be embedded into another statement by using the
        :meth:`_expression.TextualSelect.subquery` method to produce a
        :class:`.Subquery`
        object, which can then be SELECTed from.

        This function essentially bridges the gap between an entirely
        textual SELECT statement and the SQL expression language concept
        of a "selectable"::

            from sqlalchemy.sql import column, text

            stmt = text("SELECT id, name FROM some_table")
            stmt = stmt.columns(column(\'id\'), column(\'name\')).subquery(\'st\')

            stmt = select(mytable).\\\n                    select_from(
                        mytable.join(stmt, mytable.c.name == stmt.c.name)
                    ).where(stmt.c.id > 5)

        Above, we pass a series of :func:`_expression.column` elements to the
        :meth:`_expression.TextClause.columns` method positionally.  These
        :func:`_expression.column`
        elements now become first class elements upon the
        :attr:`_expression.TextualSelect.selected_columns` column collection,
        which then
        become part of the :attr:`.Subquery.c` collection after
        :meth:`_expression.TextualSelect.subquery` is invoked.

        The column expressions we pass to
        :meth:`_expression.TextClause.columns` may
        also be typed; when we do so, these :class:`.TypeEngine` objects become
        the effective return type of the column, so that SQLAlchemy\'s
        result-set-processing systems may be used on the return values.
        This is often needed for types such as date or boolean types, as well
        as for unicode processing on some dialect configurations::

            stmt = text("SELECT id, name, timestamp FROM some_table")
            stmt = stmt.columns(
                        column(\'id\', Integer),
                        column(\'name\', Unicode),
                        column(\'timestamp\', DateTime)
                    )

            for id, name, timestamp in connection.execute(stmt):
                print(id, name, timestamp)

        As a shortcut to the above syntax, keyword arguments referring to
        types alone may be used, if only type conversion is needed::

            stmt = text("SELECT id, name, timestamp FROM some_table")
            stmt = stmt.columns(
                        id=Integer,
                        name=Unicode,
                        timestamp=DateTime
                    )

            for id, name, timestamp in connection.execute(stmt):
                print(id, name, timestamp)

        The positional form of :meth:`_expression.TextClause.columns`
        also provides the
        unique feature of **positional column targeting**, which is
        particularly useful when using the ORM with complex textual queries. If
        we specify the columns from our model to
        :meth:`_expression.TextClause.columns`,
        the result set will match to those columns positionally, meaning the
        name or origin of the column in the textual SQL doesn\'t matter::

            stmt = text("SELECT users.id, addresses.id, users.id, "
                 "users.name, addresses.email_address AS email "
                 "FROM users JOIN addresses ON users.id=addresses.user_id "
                 "WHERE users.id = 1").columns(
                    User.id,
                    Address.id,
                    Address.user_id,
                    User.name,
                    Address.email_address
                 )

            query = session.query(User).from_statement(stmt).options(
                contains_eager(User.addresses))

        The :meth:`_expression.TextClause.columns` method provides a direct
        route to calling :meth:`_expression.FromClause.subquery` as well as
        :meth:`_expression.SelectBase.cte`
        against a textual SELECT statement::

            stmt = stmt.columns(id=Integer, name=String).cte(\'st\')

            stmt = select(sometable).where(sometable.c.id == stmt.c.id)

        :param \\*cols: A series of :class:`_expression.ColumnElement` objects,
         typically
         :class:`_schema.Column` objects from a :class:`_schema.Table`
         or ORM level
         column-mapped attributes, representing a set of columns that this
         textual string will SELECT from.

        :param \\**types: A mapping of string names to :class:`.TypeEngine`
         type objects indicating the datatypes to use for names that are
         SELECTed from the textual string.  Prefer to use the ``*cols``
         argument as it also indicates positional ordering.

        '''
    @property
    def type(self) -> TypeEngine[Any]: ...
    @property
    def comparator(self): ...
    def self_group(self, against: Incomplete | None = None): ...

class Null(SingletonConstant, roles.ConstExprRole[None], ColumnElement[None]):
    """Represent the NULL keyword in a SQL statement.

    :class:`.Null` is accessed as a constant via the
    :func:`.null` function.

    """
    __visit_name__: str
    def type(self): ...

class False_(SingletonConstant, roles.ConstExprRole[bool], ColumnElement[bool]):
    """Represent the ``false`` keyword, or equivalent, in a SQL statement.

    :class:`.False_` is accessed as a constant via the
    :func:`.false` function.

    """
    __visit_name__: str
    def type(self): ...

class True_(SingletonConstant, roles.ConstExprRole[bool], ColumnElement[bool]):
    """Represent the ``true`` keyword, or equivalent, in a SQL statement.

    :class:`.True_` is accessed as a constant via the
    :func:`.true` function.

    """
    __visit_name__: str
    def type(self): ...

class ClauseList(roles.InElementRole, roles.OrderByRole, roles.ColumnsClauseRole, roles.DMLColumnRole, DQLDMLClauseElement):
    """Describe a list of clauses, separated by an operator.

    By default, is comma-separated, such as a column listing.

    """
    __visit_name__: str
    clauses: List[ColumnElement[Any]]
    operator: Incomplete
    group: Incomplete
    group_contents: Incomplete
    def __init__(self, *clauses: _ColumnExpressionArgument[Any], operator: OperatorType = ..., group: bool = True, group_contents: bool = True, _literal_as_text_role: Type[roles.SQLRole] = ...) -> None: ...
    def __iter__(self) -> Iterator[ColumnElement[Any]]: ...
    def __len__(self) -> int: ...
    def append(self, clause) -> None: ...
    def self_group(self, against: Incomplete | None = None): ...

class OperatorExpression(ColumnElement[_T]):
    """base for expressions that contain an operator and operands

    .. versionadded:: 2.0

    """
    operator: OperatorType
    type: TypeEngine[_T]
    group: bool
    @property
    def is_comparison(self): ...
    def self_group(self, against: Incomplete | None = None): ...

class ExpressionClauseList(OperatorExpression[_T]):
    """Describe a list of clauses, separated by an operator,
    in a column expression context.

    :class:`.ExpressionClauseList` differs from :class:`.ClauseList` in that
    it represents a column-oriented DQL expression only, not an open ended
    list of anything comma separated.

    .. versionadded:: 2.0

    """
    __visit_name__: str
    clauses: typing_Tuple[ColumnElement[Any], ...]
    group: bool
    operator: Incomplete
    type: Incomplete
    def __init__(self, operator: OperatorType, *clauses: _ColumnExpressionArgument[Any], type_: _TypeEngineArgument[_T] | None = None) -> None: ...
    def __iter__(self) -> Iterator[ColumnElement[Any]]: ...
    def __len__(self) -> int: ...

class BooleanClauseList(ExpressionClauseList[bool]):
    __visit_name__: str
    inherit_cache: bool
    def __init__(self, *arg, **kw) -> None: ...
    @classmethod
    def and_(cls, initial_clause: Literal[True] | _ColumnExpressionArgument[bool] | _NoArg = ..., *clauses: _ColumnExpressionArgument[bool]) -> ColumnElement[bool]:
        """Produce a conjunction of expressions joined by ``AND``.

        See :func:`_sql.and_` for full documentation.
        """
    @classmethod
    def or_(cls, initial_clause: Literal[False] | _ColumnExpressionArgument[bool] | _NoArg = ..., *clauses: _ColumnExpressionArgument[bool]) -> ColumnElement[bool]:
        """Produce a conjunction of expressions joined by ``OR``.

        See :func:`_sql.or_` for full documentation.
        """
    def self_group(self, against: Incomplete | None = None): ...

and_: Incomplete
or_: Incomplete

class Tuple(ClauseList, ColumnElement[typing_Tuple[Any, ...]]):
    """Represent a SQL tuple."""
    __visit_name__: str
    type: TupleType
    def __init__(self, *clauses: _ColumnExpressionArgument[Any], types: Sequence[_TypeEngineArgument[Any]] | None = None) -> None: ...
    def self_group(self, against: Incomplete | None = None): ...

class Case(ColumnElement[_T]):
    """Represent a ``CASE`` expression.

    :class:`.Case` is produced using the :func:`.case` factory function,
    as in::

        from sqlalchemy import case

        stmt = select(users_table).                    where(
                        case(
                            (users_table.c.name == 'wendy', 'W'),
                            (users_table.c.name == 'jack', 'J'),
                            else_='E'
                        )
                    )

    Details on :class:`.Case` usage is at :func:`.case`.

    .. seealso::

        :func:`.case`

    """
    __visit_name__: str
    whens: List[typing_Tuple[ColumnElement[bool], ColumnElement[_T]]]
    else_: ColumnElement[_T] | None
    value: ColumnElement[Any] | None
    type: Incomplete
    def __init__(self, *whens: typing_Tuple[_ColumnExpressionArgument[bool], Any] | Mapping[Any, Any], value: Any | None = None, else_: Any | None = None) -> None: ...

class Cast(WrapsColumnExpression[_T]):
    """Represent a ``CAST`` expression.

    :class:`.Cast` is produced using the :func:`.cast` factory function,
    as in::

        from sqlalchemy import cast, Numeric

        stmt = select(cast(product_table.c.unit_price, Numeric(10, 4)))

    Details on :class:`.Cast` usage is at :func:`.cast`.

    .. seealso::

        :ref:`tutorial_casts`

        :func:`.cast`

        :func:`.try_cast`

        :func:`.type_coerce` - an alternative to CAST that coerces the type
        on the Python side only, which is often sufficient to generate the
        correct SQL and data coercion.

    """
    __visit_name__: str
    clause: ColumnElement[Any]
    type: TypeEngine[_T]
    typeclause: TypeClause
    def __init__(self, expression: _ColumnExpressionArgument[Any], type_: _TypeEngineArgument[_T]) -> None: ...
    @property
    def wrapped_column_expression(self): ...

class TryCast(Cast[_T]):
    """Represent a TRY_CAST expression.

    Details on :class:`.TryCast` usage is at :func:`.try_cast`.

    .. seealso::

        :func:`.try_cast`

        :ref:`tutorial_casts`
    """
    __visit_name__: str
    inherit_cache: bool

class TypeCoerce(WrapsColumnExpression[_T]):
    """Represent a Python-side type-coercion wrapper.

    :class:`.TypeCoerce` supplies the :func:`_expression.type_coerce`
    function; see that function for usage details.

    .. seealso::

        :func:`_expression.type_coerce`

        :func:`.cast`

    """
    __visit_name__: str
    clause: ColumnElement[Any]
    type: TypeEngine[_T]
    def __init__(self, expression: _ColumnExpressionArgument[Any], type_: _TypeEngineArgument[_T]) -> None: ...
    def typed_expression(self): ...
    @property
    def wrapped_column_expression(self): ...
    def self_group(self, against: Incomplete | None = None): ...

class Extract(ColumnElement[int]):
    """Represent a SQL EXTRACT clause, ``extract(field FROM expr)``."""
    __visit_name__: str
    expr: ColumnElement[Any]
    field: str
    type: Incomplete
    def __init__(self, field: str, expr: _ColumnExpressionArgument[Any]) -> None: ...

class _label_reference(ColumnElement[_T]):
    """Wrap a column expression as it appears in a 'reference' context.

    This expression is any that includes an _order_by_label_element,
    which is a Label, or a DESC / ASC construct wrapping a Label.

    The production of _label_reference() should occur when an expression
    is added to this context; this includes the ORDER BY or GROUP BY of a
    SELECT statement, as well as a few other places, such as the ORDER BY
    within an OVER clause.

    """
    __visit_name__: str
    element: ColumnElement[_T]
    def __init__(self, element: ColumnElement[_T]) -> None: ...

class _textual_label_reference(ColumnElement[Any]):
    __visit_name__: str
    element: Incomplete
    def __init__(self, element: str) -> None: ...

class UnaryExpression(ColumnElement[_T]):
    """Define a 'unary' expression.

    A unary expression has a single column expression
    and an operator.  The operator can be placed on the left
    (where it is called the 'operator') or right (where it is called the
    'modifier') of the column expression.

    :class:`.UnaryExpression` is the basis for several unary operators
    including those used by :func:`.desc`, :func:`.asc`, :func:`.distinct`,
    :func:`.nulls_first` and :func:`.nulls_last`.

    """
    __visit_name__: str
    element: ClauseElement
    operator: Incomplete
    modifier: Incomplete
    type: Incomplete
    wraps_column_expression: Incomplete
    def __init__(self, element: ColumnElement[Any], operator: OperatorType | None = None, modifier: OperatorType | None = None, type_: _TypeEngineArgument[_T] | None = None, wraps_column_expression: bool = False) -> None: ...
    def self_group(self, against: Incomplete | None = None): ...

class CollectionAggregate(UnaryExpression[_T]):
    """Forms the basis for right-hand collection operator modifiers
    ANY and ALL.

    The ANY and ALL keywords are available in different ways on different
    backends.  On PostgreSQL, they only work for an ARRAY type.  On
    MySQL, they only work for subqueries.

    """
    inherit_cache: bool
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs) -> None: ...

class AsBoolean(WrapsColumnExpression[bool], UnaryExpression[bool]):
    inherit_cache: bool
    element: Incomplete
    type: Incomplete
    operator: Incomplete
    negate: Incomplete
    modifier: Incomplete
    wraps_column_expression: bool
    def __init__(self, element, operator, negate) -> None: ...
    @property
    def wrapped_column_expression(self): ...
    def self_group(self, against: Incomplete | None = None): ...

class BinaryExpression(OperatorExpression[_T]):
    """Represent an expression that is ``LEFT <operator> RIGHT``.

    A :class:`.BinaryExpression` is generated automatically
    whenever two column expressions are used in a Python binary expression:

    .. sourcecode:: pycon+sql

        >>> from sqlalchemy.sql import column
        >>> column('a') + column('b')
        <sqlalchemy.sql.expression.BinaryExpression object at 0x101029dd0>
        >>> print(column('a') + column('b'))
        {printsql}a + b

    """
    __visit_name__: str
    modifiers: Mapping[str, Any] | None
    left: ColumnElement[Any]
    right: ColumnElement[Any]
    operator: Incomplete
    type: Incomplete
    negate: Incomplete
    def __init__(self, left: ColumnElement[Any], right: ColumnElement[Any], operator: OperatorType, type_: _TypeEngineArgument[_T] | None = None, negate: OperatorType | None = None, modifiers: Mapping[str, Any] | None = None) -> None: ...
    def __bool__(self) -> bool:
        '''Implement Python-side "bool" for BinaryExpression as a
        simple "identity" check for the left and right attributes,
        if the operator is "eq" or "ne".  Otherwise the expression
        continues to not support "bool" like all other column expressions.

        The rationale here is so that ColumnElement objects can be hashable.
        What?  Well, suppose you do this::

            c1, c2 = column(\'x\'), column(\'y\')
            s1 = set([c1, c2])

        We do that **a lot**, columns inside of sets is an extremely basic
        thing all over the ORM for example.

        So what happens if we do this? ::

            c1 in s1

        Hashing means it will normally use ``__hash__()`` of the object,
        but in case of hash collision, it\'s going to also do ``c1 == c1``
        and/or ``c1 == c2`` inside.  Those operations need to return a
        True/False value.   But because we override ``==`` and ``!=``, they\'re
        going to get a BinaryExpression.  Hence we implement ``__bool__`` here
        so that these comparisons behave in this particular context mostly
        like regular object comparisons.  Thankfully Python is OK with
        that!  Otherwise we\'d have to use special set classes for columns
        (which we used to do, decades ago).

        '''
    def __invert__(self) -> BinaryExpression[_T]: ...

class Slice(ColumnElement[Any]):
    """Represent SQL for a Python array-slice object.

    This is not a specific SQL construct at this level, but
    may be interpreted by specific dialects, e.g. PostgreSQL.

    """
    __visit_name__: str
    start: Incomplete
    stop: Incomplete
    step: Incomplete
    type: Incomplete
    def __init__(self, start, stop, step, _name: Incomplete | None = None) -> None: ...
    def self_group(self, against: Incomplete | None = None): ...

class IndexExpression(BinaryExpression[Any]):
    '''Represent the class of expressions that are like an "index"
    operation.'''
    inherit_cache: bool

class GroupedElement(DQLDMLClauseElement):
    """Represent any parenthesized expression"""
    __visit_name__: str
    element: ClauseElement
    def self_group(self, against: Incomplete | None = None): ...

class Grouping(GroupedElement, ColumnElement[_T]):
    """Represent a grouping within a column expression"""
    element: TextClause | ClauseList | ColumnElement[_T]
    type: Incomplete
    def __init__(self, element: TextClause | ClauseList | ColumnElement[_T]) -> None: ...
    def __getattr__(self, attr): ...

class _OverRange(IntEnum):
    RANGE_UNBOUNDED: int
    RANGE_CURRENT: int

RANGE_UNBOUNDED: Incomplete
RANGE_CURRENT: Incomplete

class Over(ColumnElement[_T]):
    '''Represent an OVER clause.

    This is a special operator against a so-called
    "window" function, as well as any aggregate function,
    which produces results relative to the result set
    itself.  Most modern SQL backends now support window functions.

    '''
    __visit_name__: str
    order_by: ClauseList | None
    partition_by: ClauseList | None
    element: ColumnElement[_T]
    range_: typing_Tuple[int, int] | None
    rows: Incomplete
    def __init__(self, element: ColumnElement[_T], partition_by: Iterable[_ColumnExpressionArgument[Any]] | _ColumnExpressionArgument[Any] | None = None, order_by: Iterable[_ColumnExpressionArgument[Any]] | _ColumnExpressionArgument[Any] | None = None, range_: typing_Tuple[int | None, int | None] | None = None, rows: typing_Tuple[int | None, int | None] | None = None) -> None: ...
    def __reduce__(self): ...
    def type(self): ...

class WithinGroup(ColumnElement[_T]):
    '''Represent a WITHIN GROUP (ORDER BY) clause.

    This is a special operator against so-called
    "ordered set aggregate" and "hypothetical
    set aggregate" functions, including ``percentile_cont()``,
    ``rank()``, ``dense_rank()``, etc.

    It\'s supported only by certain database backends, such as PostgreSQL,
    Oracle and MS SQL Server.

    The :class:`.WithinGroup` construct extracts its type from the
    method :meth:`.FunctionElement.within_group_type`.  If this returns
    ``None``, the function\'s ``.type`` is used.

    '''
    __visit_name__: str
    order_by: ClauseList | None
    element: Incomplete
    def __init__(self, element: FunctionElement[_T], *order_by: _ColumnExpressionArgument[Any]) -> None: ...
    def __reduce__(self): ...
    def over(self, partition_by: Incomplete | None = None, order_by: Incomplete | None = None, range_: Incomplete | None = None, rows: Incomplete | None = None):
        """Produce an OVER clause against this :class:`.WithinGroup`
        construct.

        This function has the same signature as that of
        :meth:`.FunctionElement.over`.

        """
    def type(self): ...

class FunctionFilter(ColumnElement[_T]):
    """Represent a function FILTER clause.

    This is a special operator against aggregate and window functions,
    which controls which rows are passed to it.
    It's supported only by certain database backends.

    Invocation of :class:`.FunctionFilter` is via
    :meth:`.FunctionElement.filter`::

        func.count(1).filter(True)

    .. seealso::

        :meth:`.FunctionElement.filter`

    """
    __visit_name__: str
    criterion: ColumnElement[bool] | None
    func: Incomplete
    def __init__(self, func: FunctionElement[_T], *criterion: _ColumnExpressionArgument[bool]) -> None: ...
    def filter(self, *criterion):
        """Produce an additional FILTER against the function.

        This method adds additional criteria to the initial criteria
        set up by :meth:`.FunctionElement.filter`.

        Multiple criteria are joined together at SQL render time
        via ``AND``.


        """
    def over(self, partition_by: Iterable[_ColumnExpressionArgument[Any]] | _ColumnExpressionArgument[Any] | None = None, order_by: Iterable[_ColumnExpressionArgument[Any]] | _ColumnExpressionArgument[Any] | None = None, range_: typing_Tuple[int | None, int | None] | None = None, rows: typing_Tuple[int | None, int | None] | None = None) -> Over[_T]:
        '''Produce an OVER clause against this filtered function.

        Used against aggregate or so-called "window" functions,
        for database backends that support window functions.

        The expression::

            func.rank().filter(MyClass.y > 5).over(order_by=\'x\')

        is shorthand for::

            from sqlalchemy import over, funcfilter
            over(funcfilter(func.rank(), MyClass.y > 5), order_by=\'x\')

        See :func:`_expression.over` for a full description.

        '''
    def self_group(self, against: Incomplete | None = None): ...
    def type(self): ...

class NamedColumn(KeyedColumnElement[_T]):
    is_literal: bool
    table: FromClause | None
    name: str
    key: str
    def description(self) -> str: ...

class Label(roles.LabeledColumnExprRole[_T], NamedColumn[_T]):
    """Represents a column label (AS).

    Represent a label, as typically applied to any column-level
    element using the ``AS`` sql keyword.

    """
    __visit_name__: str
    name: str
    key: Incomplete
    type: Incomplete
    def __init__(self, name: str | None, element: _ColumnExpressionArgument[_T], type_: _TypeEngineArgument[_T] | None = None) -> None: ...
    def __reduce__(self): ...
    def element(self) -> ColumnElement[_T]: ...
    def self_group(self, against: Incomplete | None = None): ...
    @property
    def primary_key(self): ...
    @property
    def foreign_keys(self): ...

class ColumnClause(roles.DDLReferredColumnRole, roles.LabeledColumnExprRole[_T], roles.StrAsPlainColumnRole, Immutable, NamedColumn[_T]):
    '''Represents a column expression from any textual string.

    The :class:`.ColumnClause`, a lightweight analogue to the
    :class:`_schema.Column` class, is typically invoked using the
    :func:`_expression.column` function, as in::

        from sqlalchemy import column

        id, name = column("id"), column("name")
        stmt = select(id, name).select_from("user")

    The above statement would produce SQL like::

        SELECT id, name FROM user

    :class:`.ColumnClause` is the immediate superclass of the schema-specific
    :class:`_schema.Column` object.  While the :class:`_schema.Column`
    class has all the
    same capabilities as :class:`.ColumnClause`, the :class:`.ColumnClause`
    class is usable by itself in those cases where behavioral requirements
    are limited to simple SQL expression generation.  The object has none of
    the associations with schema-level metadata or with execution-time
    behavior that :class:`_schema.Column` does,
    so in that sense is a "lightweight"
    version of :class:`_schema.Column`.

    Full details on :class:`.ColumnClause` usage is at
    :func:`_expression.column`.

    .. seealso::

        :func:`_expression.column`

        :class:`_schema.Column`

    '''
    table: FromClause | None
    is_literal: bool
    __visit_name__: str
    onupdate: DefaultGenerator | None
    default: DefaultGenerator | None
    server_default: FetchedValue | None
    server_onupdate: FetchedValue | None
    key: Incomplete
    type: Incomplete
    def __init__(self, text: str, type_: _TypeEngineArgument[_T] | None = None, is_literal: bool = False, _selectable: FromClause | None = None) -> None: ...
    def get_children(self, *, column_tables: bool = False, **kw): ...
    @property
    def entity_namespace(self): ...

class TableValuedColumn(NamedColumn[_T]):
    __visit_name__: str
    scalar_alias: Incomplete
    key: Incomplete
    type: Incomplete
    def __init__(self, scalar_alias: NamedFromClause, type_: TypeEngine[_T]) -> None: ...

class CollationClause(ColumnElement[str]):
    __visit_name__: str
    collation: Incomplete
    def __init__(self, collation) -> None: ...

class _IdentifiedClause(Executable, ClauseElement):
    __visit_name__: str
    ident: Incomplete
    def __init__(self, ident) -> None: ...

class SavepointClause(_IdentifiedClause):
    __visit_name__: str
    inherit_cache: bool

class RollbackToSavepointClause(_IdentifiedClause):
    __visit_name__: str
    inherit_cache: bool

class ReleaseSavepointClause(_IdentifiedClause):
    __visit_name__: str
    inherit_cache: bool

class quoted_name(util.MemoizedSlots, str):
    '''Represent a SQL identifier combined with quoting preferences.

    :class:`.quoted_name` is a Python unicode/str subclass which
    represents a particular identifier name along with a
    ``quote`` flag.  This ``quote`` flag, when set to
    ``True`` or ``False``, overrides automatic quoting behavior
    for this identifier in order to either unconditionally quote
    or to not quote the name.  If left at its default of ``None``,
    quoting behavior is applied to the identifier on a per-backend basis
    based on an examination of the token itself.

    A :class:`.quoted_name` object with ``quote=True`` is also
    prevented from being modified in the case of a so-called
    "name normalize" option.  Certain database backends, such as
    Oracle, Firebird, and DB2 "normalize" case-insensitive names
    as uppercase.  The SQLAlchemy dialects for these backends
    convert from SQLAlchemy\'s lower-case-means-insensitive convention
    to the upper-case-means-insensitive conventions of those backends.
    The ``quote=True`` flag here will prevent this conversion from occurring
    to support an identifier that\'s quoted as all lower case against
    such a backend.

    The :class:`.quoted_name` object is normally created automatically
    when specifying the name for key schema constructs such as
    :class:`_schema.Table`, :class:`_schema.Column`, and others.
    The class can also be
    passed explicitly as the name to any function that receives a name which
    can be quoted.  Such as to use the :meth:`_engine.Engine.has_table`
    method with
    an unconditionally quoted name::

        from sqlalchemy import create_engine
        from sqlalchemy import inspect
        from sqlalchemy.sql import quoted_name

        engine = create_engine("oracle+cx_oracle://some_dsn")
        print(inspect(engine).has_table(quoted_name("some_table", True)))

    The above logic will run the "has table" logic against the Oracle backend,
    passing the name exactly as ``"some_table"`` without converting to
    upper case.

    .. versionchanged:: 1.2 The :class:`.quoted_name` construct is now
       importable from ``sqlalchemy.sql``, in addition to the previous
       location of ``sqlalchemy.sql.elements``.

    '''
    quote: bool | None
    @overload
    @classmethod
    def construct(cls, value: str, quote: bool | None) -> quoted_name: ...
    @overload
    @classmethod
    def construct(cls, value: None, quote: bool | None) -> None: ...
    def __new__(cls, value: str, quote: bool | None) -> quoted_name: ...
    def __reduce__(self): ...

class AnnotatedColumnElement(Annotated):
    def __init__(self, element, values) -> None: ...
    def name(self):
        """pull 'name' from parent, if not present"""
    def table(self):
        """pull 'table' from parent, if not present"""
    def key(self):
        """pull 'key' from parent, if not present"""
    def info(self) -> _InfoType: ...

class _truncated_label(quoted_name):
    '''A unicode subclass used to identify symbolic "
    "names that may require truncation.'''
    def __new__(cls, value: str, quote: bool | None = None) -> Any: ...
    def __reduce__(self) -> Any: ...
    def apply_map(self, map_: Mapping[str, Any]) -> str: ...

class conv(_truncated_label):
    '''Mark a string indicating that a name has already been converted
    by a naming convention.

    This is a string subclass that indicates a name that should not be
    subject to any further naming conventions.

    E.g. when we create a :class:`.Constraint` using a naming convention
    as follows::

        m = MetaData(naming_convention={
            "ck": "ck_%(table_name)s_%(constraint_name)s"
        })
        t = Table(\'t\', m, Column(\'x\', Integer),
                        CheckConstraint(\'x > 5\', name=\'x5\'))

    The name of the above constraint will be rendered as ``"ck_t_x5"``.
    That is, the existing name ``x5`` is used in the naming convention as the
    ``constraint_name`` token.

    In some situations, such as in migration scripts, we may be rendering
    the above :class:`.CheckConstraint` with a name that\'s already been
    converted.  In order to make sure the name isn\'t double-modified, the
    new name is applied using the :func:`_schema.conv` marker.  We can
    use this explicitly as follows::


        m = MetaData(naming_convention={
            "ck": "ck_%(table_name)s_%(constraint_name)s"
        })
        t = Table(\'t\', m, Column(\'x\', Integer),
                        CheckConstraint(\'x > 5\', name=conv(\'ck_t_x5\')))

    Where above, the :func:`_schema.conv` marker indicates that the constraint
    name here is final, and the name will render as ``"ck_t_x5"`` and not
    ``"ck_t_ck_t_x5"``

    .. seealso::

        :ref:`constraint_naming_conventions`

    '''

class _anonymous_label(_truncated_label):
    """A unicode subclass used to identify anonymously
    generated names."""
    @classmethod
    def safe_construct(cls, seed: int, body: str, enclosing_label: str | None = None, sanitize_key: bool = False) -> _anonymous_label: ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def apply_map(self, map_): ...
