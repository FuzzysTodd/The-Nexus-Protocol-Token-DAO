from . import attributes, interfaces
from .. import log
from ..engine import Row
from ..engine.cursor import CursorResult
from ..engine.interfaces import CompiledCacheType, IsolationLevel, SchemaTranslateMapType, _ImmutableExecuteOptions
from ..engine.result import FrozenResult
from ..event import EventTarget, dispatcher
from ..sql import Select, roles
from ..sql._typing import _ColumnExpressionArgument, _ColumnExpressionOrStrLabelArgument, _ColumnsClauseArgument, _DMLColumnArgument, _FromClauseArgument, _JoinTargetArgument, _LimitOffsetType, _MAYBE_ENTITY, _NOT_ENTITY, _OnClauseArgument, _T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7, _TP, _TypedColumnClauseArgument as _TCCA
from ..sql.annotation import SupportsCloneAnnotations
from ..sql.base import Executable, ExecutableOption, Generative, _NoArg
from ..sql.elements import ColumnElement, Label
from ..sql.expression import Exists
from ..sql.selectable import Alias, CTE, ExecutableReturnsRows, HasHints, HasPrefixes, HasSuffixes, ScalarSelect, SelectLabelStyle, Subquery, _ForUpdateOfArgument, _SelectFromElements
from ..util.typing import Literal, Self
from ._typing import SynchronizeSessionArgument, _EntityType, _ExternalEntityType, _O
from .context import FromStatement, ORMCompileState, QueryContext as QueryContext
from .interfaces import ORMColumnDescription
from .session import Session, _PKIdentityArgument
from .state import InstanceState
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Generic, Iterable, Iterator, List, Sequence, Tuple, overload

__all__ = ['Query', 'QueryContext']

class Query(_SelectFromElements, SupportsCloneAnnotations, HasPrefixes, HasSuffixes, HasHints, EventTarget, log.Identified, Generative, Executable, Generic[_T]):
    """ORM-level SQL construction object.

    .. legacy:: The ORM :class:`.Query` object is a legacy construct
       as of SQLAlchemy 2.0.   See the notes at the top of
       :ref:`query_api_toplevel` for an overview, including links to migration
       documentation.

    :class:`_query.Query` objects are normally initially generated using the
    :meth:`~.Session.query` method of :class:`.Session`, and in
    less common cases by instantiating the :class:`_query.Query` directly and
    associating with a :class:`.Session` using the
    :meth:`_query.Query.with_session`
    method.

    """
    load_options: Incomplete
    session: Session
    dispatch: dispatcher[Query[_T]]
    def __init__(self, entities: _ColumnsClauseArgument[Any] | Sequence[_ColumnsClauseArgument[Any]], session: Session | None = None) -> None:
        """Construct a :class:`_query.Query` directly.

        E.g.::

            q = Query([User, Address], session=some_session)

        The above is equivalent to::

            q = some_session.query(User, Address)

        :param entities: a sequence of entities and/or SQL expressions.

        :param session: a :class:`.Session` with which the
         :class:`_query.Query`
         will be associated.   Optional; a :class:`_query.Query`
         can be associated
         with a :class:`.Session` generatively via the
         :meth:`_query.Query.with_session` method as well.

        .. seealso::

            :meth:`.Session.query`

            :meth:`_query.Query.with_session`

        """
    def tuples(self) -> Query[Tuple[_O]]:
        '''return a tuple-typed form of this :class:`.Query`.

        This method invokes the :meth:`.Query.only_return_tuples`
        method with a value of ``True``, which by itself ensures that this
        :class:`.Query` will always return :class:`.Row` objects, even
        if the query is made against a single entity.  It then also
        at the typing level will return a "typed" query, if possible,
        that will type result rows as ``Tuple`` objects with typed
        elements.

        This method can be compared to the :meth:`.Result.tuples` method,
        which returns "self", but from a typing perspective returns an object
        that will yield typed ``Tuple`` objects for results.   Typing
        takes effect only if this :class:`.Query` object is a typed
        query object already.

        .. versionadded:: 2.0

        .. seealso::

            :meth:`.Result.tuples` - v2 equivalent method.

        '''
    @property
    def statement(self) -> Select[_T] | FromStatement[_T]:
        """The full SELECT statement represented by this Query.

        The statement by default will not have disambiguating labels
        applied to the construct unless with_labels(True) is called
        first.

        """
    def subquery(self, name: str | None = None, with_labels: bool = False, reduce_columns: bool = False) -> Subquery:
        """Return the full SELECT statement represented by
        this :class:`_query.Query`, embedded within an
        :class:`_expression.Alias`.

        Eager JOIN generation within the query is disabled.

        .. seealso::

            :meth:`_sql.Select.subquery` - v2 comparable method.

        :param name: string name to be assigned as the alias;
            this is passed through to :meth:`_expression.FromClause.alias`.
            If ``None``, a name will be deterministically generated
            at compile time.

        :param with_labels: if True, :meth:`.with_labels` will be called
         on the :class:`_query.Query` first to apply table-qualified labels
         to all columns.

        :param reduce_columns: if True,
         :meth:`_expression.Select.reduce_columns` will
         be called on the resulting :func:`_expression.select` construct,
         to remove same-named columns where one also refers to the other
         via foreign key or WHERE clause equivalence.

        """
    def cte(self, name: str | None = None, recursive: bool = False, nesting: bool = False) -> CTE:
        '''Return the full SELECT statement represented by this
        :class:`_query.Query` represented as a common table expression (CTE).

        Parameters and usage are the same as those of the
        :meth:`_expression.SelectBase.cte` method; see that method for
        further details.

        Here is the `PostgreSQL WITH
        RECURSIVE example
        <https://www.postgresql.org/docs/current/static/queries-with.html>`_.
        Note that, in this example, the ``included_parts`` cte and the
        ``incl_alias`` alias of it are Core selectables, which
        means the columns are accessed via the ``.c.`` attribute.  The
        ``parts_alias`` object is an :func:`_orm.aliased` instance of the
        ``Part`` entity, so column-mapped attributes are available
        directly::

            from sqlalchemy.orm import aliased

            class Part(Base):
                __tablename__ = \'part\'
                part = Column(String, primary_key=True)
                sub_part = Column(String, primary_key=True)
                quantity = Column(Integer)

            included_parts = session.query(
                            Part.sub_part,
                            Part.part,
                            Part.quantity).\\\n                                filter(Part.part=="our part").\\\n                                cte(name="included_parts", recursive=True)

            incl_alias = aliased(included_parts, name="pr")
            parts_alias = aliased(Part, name="p")
            included_parts = included_parts.union_all(
                session.query(
                    parts_alias.sub_part,
                    parts_alias.part,
                    parts_alias.quantity).\\\n                        filter(parts_alias.part==incl_alias.c.sub_part)
                )

            q = session.query(
                    included_parts.c.sub_part,
                    func.sum(included_parts.c.quantity).
                        label(\'total_quantity\')
                ).\\\n                group_by(included_parts.c.sub_part)

        .. seealso::

            :meth:`_sql.Select.cte` - v2 equivalent method.

        '''
    def label(self, name: str | None) -> Label[Any]:
        """Return the full SELECT statement represented by this
        :class:`_query.Query`, converted
        to a scalar subquery with a label of the given name.

        .. seealso::

            :meth:`_sql.Select.label` - v2 comparable method.

        """
    @overload
    def as_scalar(self) -> ScalarSelect[_MAYBE_ENTITY]: ...
    @overload
    def as_scalar(self) -> ScalarSelect[_NOT_ENTITY]: ...
    @overload
    def as_scalar(self) -> ScalarSelect[Any]: ...
    @overload
    def scalar_subquery(self) -> ScalarSelect[Any]: ...
    @overload
    def scalar_subquery(self) -> ScalarSelect[_NOT_ENTITY]: ...
    @overload
    def scalar_subquery(self) -> ScalarSelect[Any]: ...
    @property
    def selectable(self) -> Select[_T] | FromStatement[_T]:
        """Return the :class:`_expression.Select` object emitted by this
        :class:`_query.Query`.

        Used for :func:`_sa.inspect` compatibility, this is equivalent to::

            query.enable_eagerloads(False).with_labels().statement

        """
    def __clause_element__(self) -> Select[_T] | FromStatement[_T]: ...
    @overload
    def only_return_tuples(self, value: Literal[True]) -> RowReturningQuery[Tuple[_O]]: ...
    @overload
    def only_return_tuples(self, value: Literal[False]) -> Query[_O]: ...
    @property
    def is_single_entity(self) -> bool:
        """Indicates if this :class:`_query.Query`
        returns tuples or single entities.

        Returns True if this query returns a single entity for each instance
        in its result list, and False if this query returns a tuple of entities
        for each result.

        .. versionadded:: 1.3.11

        .. seealso::

            :meth:`_query.Query.only_return_tuples`

        """
    def enable_eagerloads(self, value: bool) -> Self:
        """Control whether or not eager joins and subqueries are
        rendered.

        When set to False, the returned Query will not render
        eager joins regardless of :func:`~sqlalchemy.orm.joinedload`,
        :func:`~sqlalchemy.orm.subqueryload` options
        or mapper-level ``lazy='joined'``/``lazy='subquery'``
        configurations.

        This is used primarily when nesting the Query's
        statement into a subquery or other
        selectable, or when using :meth:`_query.Query.yield_per`.

        """
    def with_labels(self) -> Self: ...
    apply_labels = with_labels
    @property
    def get_label_style(self) -> SelectLabelStyle:
        """
        Retrieve the current label style.

        .. versionadded:: 1.4

        .. seealso::

            :meth:`_sql.Select.get_label_style` - v2 equivalent method.

        """
    def set_label_style(self, style: SelectLabelStyle) -> Self:
        """Apply column labels to the return value of Query.statement.

        Indicates that this Query's `statement` accessor should return
        a SELECT statement that applies labels to all columns in the
        form <tablename>_<columnname>; this is commonly used to
        disambiguate columns from multiple tables which have the same
        name.

        When the `Query` actually issues SQL to load rows, it always
        uses column labeling.

        .. note:: The :meth:`_query.Query.set_label_style` method *only* applies
           the output of :attr:`_query.Query.statement`, and *not* to any of
           the result-row invoking systems of :class:`_query.Query` itself,
           e.g.
           :meth:`_query.Query.first`, :meth:`_query.Query.all`, etc.
           To execute
           a query using :meth:`_query.Query.set_label_style`, invoke the
           :attr:`_query.Query.statement` using :meth:`.Session.execute`::

                result = session.execute(
                    query
                    .set_label_style(LABEL_STYLE_TABLENAME_PLUS_COL)
                    .statement
                )

        .. versionadded:: 1.4


        .. seealso::

            :meth:`_sql.Select.set_label_style` - v2 equivalent method.

        """
    def enable_assertions(self, value: bool) -> Self:
        '''Control whether assertions are generated.

        When set to False, the returned Query will
        not assert its state before certain operations,
        including that LIMIT/OFFSET has not been applied
        when filter() is called, no criterion exists
        when get() is called, and no "from_statement()"
        exists when filter()/order_by()/group_by() etc.
        is called.  This more permissive mode is used by
        custom Query subclasses to specify criterion or
        other modifiers outside of the usual usage patterns.

        Care should be taken to ensure that the usage
        pattern is even possible.  A statement applied
        by from_statement() will override any criterion
        set by filter() or order_by(), for example.

        '''
    @property
    def whereclause(self) -> ColumnElement[bool] | None:
        """A readonly attribute which returns the current WHERE criterion for
        this Query.

        This returned value is a SQL expression construct, or ``None`` if no
        criterion has been established.

        .. seealso::

            :attr:`_sql.Select.whereclause` - v2 equivalent property.

        """
    def yield_per(self, count: int) -> Self:
        """Yield only ``count`` rows at a time.

        The purpose of this method is when fetching very large result sets
        (> 10K rows), to batch results in sub-collections and yield them
        out partially, so that the Python interpreter doesn't need to declare
        very large areas of memory which is both time consuming and leads
        to excessive memory use.   The performance from fetching hundreds of
        thousands of rows can often double when a suitable yield-per setting
        (e.g. approximately 1000) is used, even with DBAPIs that buffer
        rows (which are most).

        As of SQLAlchemy 1.4, the :meth:`_orm.Query.yield_per` method is
        equivalent to using the ``yield_per`` execution option at the ORM
        level. See the section :ref:`orm_queryguide_yield_per` for further
        background on this option.

        .. seealso::

            :ref:`orm_queryguide_yield_per`

        """
    def get(self, ident: _PKIdentityArgument) -> Any | None:
        '''Return an instance based on the given primary key identifier,
        or ``None`` if not found.

        E.g.::

            my_user = session.query(User).get(5)

            some_object = session.query(VersionedFoo).get((5, 10))

            some_object = session.query(VersionedFoo).get(
                {"id": 5, "version_id": 10})

        :meth:`_query.Query.get` is special in that it provides direct
        access to the identity map of the owning :class:`.Session`.
        If the given primary key identifier is present
        in the local identity map, the object is returned
        directly from this collection and no SQL is emitted,
        unless the object has been marked fully expired.
        If not present,
        a SELECT is performed in order to locate the object.

        :meth:`_query.Query.get` also will perform a check if
        the object is present in the identity map and
        marked as expired - a SELECT
        is emitted to refresh the object as well as to
        ensure that the row is still present.
        If not, :class:`~sqlalchemy.orm.exc.ObjectDeletedError` is raised.

        :meth:`_query.Query.get` is only used to return a single
        mapped instance, not multiple instances or
        individual column constructs, and strictly
        on a single primary key value.  The originating
        :class:`_query.Query` must be constructed in this way,
        i.e. against a single mapped entity,
        with no additional filtering criterion.  Loading
        options via :meth:`_query.Query.options` may be applied
        however, and will be used if the object is not
        yet locally present.

        :param ident: A scalar, tuple, or dictionary representing the
         primary key.  For a composite (e.g. multiple column) primary key,
         a tuple or dictionary should be passed.

         For a single-column primary key, the scalar calling form is typically
         the most expedient.  If the primary key of a row is the value "5",
         the call looks like::

            my_object = query.get(5)

         The tuple form contains primary key values typically in
         the order in which they correspond to the mapped
         :class:`_schema.Table`
         object\'s primary key columns, or if the
         :paramref:`_orm.Mapper.primary_key` configuration parameter were
         used, in
         the order used for that parameter. For example, if the primary key
         of a row is represented by the integer
         digits "5, 10" the call would look like::

             my_object = query.get((5, 10))

         The dictionary form should include as keys the mapped attribute names
         corresponding to each element of the primary key.  If the mapped class
         has the attributes ``id``, ``version_id`` as the attributes which
         store the object\'s primary key value, the call would look like::

            my_object = query.get({"id": 5, "version_id": 10})

         .. versionadded:: 1.3 the :meth:`_query.Query.get`
            method now optionally
            accepts a dictionary of attribute names to values in order to
            indicate a primary key identifier.


        :return: The object instance, or ``None``.

        '''
    @property
    def lazy_loaded_from(self) -> InstanceState[Any] | None:
        """An :class:`.InstanceState` that is using this :class:`_query.Query`
        for a lazy load operation.

        .. deprecated:: 1.4  This attribute should be viewed via the
           :attr:`.ORMExecuteState.lazy_loaded_from` attribute, within
           the context of the :meth:`.SessionEvents.do_orm_execute`
           event.

        .. seealso::

            :attr:`.ORMExecuteState.lazy_loaded_from`

        """
    def correlate(self, *fromclauses: Literal[None, False] | _FromClauseArgument) -> Self:
        """Return a :class:`.Query` construct which will correlate the given
        FROM clauses to that of an enclosing :class:`.Query` or
        :func:`~.expression.select`.

        The method here accepts mapped classes, :func:`.aliased` constructs,
        and :class:`_orm.Mapper` constructs as arguments, which are resolved
        into expression constructs, in addition to appropriate expression
        constructs.

        The correlation arguments are ultimately passed to
        :meth:`_expression.Select.correlate`
        after coercion to expression constructs.

        The correlation arguments take effect in such cases
        as when :meth:`_query.Query.from_self` is used, or when
        a subquery as returned by :meth:`_query.Query.subquery` is
        embedded in another :func:`_expression.select` construct.

        .. seealso::

            :meth:`_sql.Select.correlate` - v2 equivalent method.

        """
    def autoflush(self, setting: bool) -> Self:
        """Return a Query with a specific 'autoflush' setting.

        As of SQLAlchemy 1.4, the :meth:`_orm.Query.autoflush` method
        is equivalent to using the ``autoflush`` execution option at the
        ORM level. See the section :ref:`orm_queryguide_autoflush` for
        further background on this option.

        """
    def populate_existing(self) -> Self:
        """Return a :class:`_query.Query`
        that will expire and refresh all instances
        as they are loaded, or reused from the current :class:`.Session`.

        As of SQLAlchemy 1.4, the :meth:`_orm.Query.populate_existing` method
        is equivalent to using the ``populate_existing`` execution option at
        the ORM level. See the section :ref:`orm_queryguide_populate_existing`
        for further background on this option.

        """
    def with_parent(self, instance: object, property: attributes.QueryableAttribute[Any] | None = None, from_entity: _ExternalEntityType[Any] | None = None) -> Self:
        '''Add filtering criterion that relates the given instance
        to a child object or collection, using its attribute state
        as well as an established :func:`_orm.relationship()`
        configuration.

        The method uses the :func:`.with_parent` function to generate
        the clause, the result of which is passed to
        :meth:`_query.Query.filter`.

        Parameters are the same as :func:`.with_parent`, with the exception
        that the given property can be None, in which case a search is
        performed against this :class:`_query.Query` object\'s target mapper.

        :param instance:
          An instance which has some :func:`_orm.relationship`.

        :param property:
          Class bound attribute which indicates
          what relationship from the instance should be used to reconcile the
          parent/child relationship.

        :param from_entity:
          Entity in which to consider as the left side.  This defaults to the
          "zero" entity of the :class:`_query.Query` itself.

        '''
    def add_entity(self, entity: _EntityType[Any], alias: Alias | Subquery | None = None) -> Query[Any]:
        """add a mapped entity to the list of result columns
        to be returned.

        .. seealso::

            :meth:`_sql.Select.add_columns` - v2 comparable method.
        """
    def with_session(self, session: Session) -> Self:
        """Return a :class:`_query.Query` that will use the given
        :class:`.Session`.

        While the :class:`_query.Query`
        object is normally instantiated using the
        :meth:`.Session.query` method, it is legal to build the
        :class:`_query.Query`
        directly without necessarily using a :class:`.Session`.  Such a
        :class:`_query.Query` object, or any :class:`_query.Query`
        already associated
        with a different :class:`.Session`, can produce a new
        :class:`_query.Query`
        object associated with a target session using this method::

            from sqlalchemy.orm import Query

            query = Query([MyClass]).filter(MyClass.id == 5)

            result = query.with_session(my_session).one()

        """
    def values(self, *columns: _ColumnsClauseArgument[Any]) -> Iterable[Any]:
        """Return an iterator yielding result tuples corresponding
        to the given list of columns

        """
    def value(self, column: _ColumnExpressionArgument[Any]) -> Any:
        """Return a scalar result corresponding to the given
        column expression.

        """
    @overload
    def with_entities(self, _entity: _EntityType[_O]) -> Query[_O]: ...
    @overload
    def with_entities(self, _colexpr: roles.TypedColumnsClauseRole[_T]) -> RowReturningQuery[Tuple[_T]]: ...
    @overload
    def with_entities(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1]) -> RowReturningQuery[Tuple[_T0, _T1]]: ...
    @overload
    def with_entities(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2]) -> RowReturningQuery[Tuple[_T0, _T1, _T2]]: ...
    @overload
    def with_entities(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3]]: ...
    @overload
    def with_entities(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4]]: ...
    @overload
    def with_entities(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def with_entities(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6]]: ...
    @overload
    def with_entities(self, __ent0: _TCCA[_T0], __ent1: _TCCA[_T1], __ent2: _TCCA[_T2], __ent3: _TCCA[_T3], __ent4: _TCCA[_T4], __ent5: _TCCA[_T5], __ent6: _TCCA[_T6], __ent7: _TCCA[_T7]) -> RowReturningQuery[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]]: ...
    @overload
    def with_entities(self, *entities: _ColumnsClauseArgument[Any]) -> Query[Any]: ...
    def add_columns(self, *column: _ColumnExpressionArgument[Any]) -> Query[Any]:
        """Add one or more column expressions to the list
        of result columns to be returned.

        .. seealso::

            :meth:`_sql.Select.add_columns` - v2 comparable method.
        """
    def add_column(self, column: _ColumnExpressionArgument[Any]) -> Query[Any]:
        """Add a column expression to the list of result columns to be
        returned.

        """
    def options(self, *args: ExecutableOption) -> Self:
        """Return a new :class:`_query.Query` object,
        applying the given list of
        mapper options.

        Most supplied options regard changing how column- and
        relationship-mapped attributes are loaded.

        .. seealso::

            :ref:`loading_columns`

            :ref:`relationship_loader_options`

        """
    def with_transformation(self, fn: Callable[[Query[Any]], Query[Any]]) -> Query[Any]:
        """Return a new :class:`_query.Query` object transformed by
        the given function.

        E.g.::

            def filter_something(criterion):
                def transform(q):
                    return q.filter(criterion)
                return transform

            q = q.with_transformation(filter_something(x==5))

        This allows ad-hoc recipes to be created for :class:`_query.Query`
        objects.

        """
    def get_execution_options(self) -> _ImmutableExecuteOptions:
        """Get the non-SQL options which will take effect during execution.

        .. versionadded:: 1.3

        .. seealso::

            :meth:`_query.Query.execution_options`

            :meth:`_sql.Select.get_execution_options` - v2 comparable method.

        """
    @overload
    def execution_options(self, *, compiled_cache: CompiledCacheType | None = ..., logging_token: str = ..., isolation_level: IsolationLevel = ..., no_parameters: bool = False, stream_results: bool = False, max_row_buffer: int = ..., yield_per: int = ..., insertmanyvalues_page_size: int = ..., schema_translate_map: SchemaTranslateMapType | None = ..., populate_existing: bool = False, autoflush: bool = False, **opt: Any) -> Self: ...
    @overload
    def execution_options(self, **opt: Any) -> Self: ...
    def with_for_update(self, *, nowait: bool = False, read: bool = False, of: _ForUpdateOfArgument | None = None, skip_locked: bool = False, key_share: bool = False) -> Self:
        """return a new :class:`_query.Query`
        with the specified options for the
        ``FOR UPDATE`` clause.

        The behavior of this method is identical to that of
        :meth:`_expression.GenerativeSelect.with_for_update`.
        When called with no arguments,
        the resulting ``SELECT`` statement will have a ``FOR UPDATE`` clause
        appended.  When additional arguments are specified, backend-specific
        options such as ``FOR UPDATE NOWAIT`` or ``LOCK IN SHARE MODE``
        can take effect.

        E.g.::

            q = sess.query(User).populate_existing().with_for_update(nowait=True, of=User)

        The above query on a PostgreSQL backend will render like::

            SELECT users.id AS users_id FROM users FOR UPDATE OF users NOWAIT

        .. warning::

            Using ``with_for_update`` in the context of eager loading
            relationships is not officially supported or recommended by
            SQLAlchemy and may not work with certain queries on various
            database backends.  When ``with_for_update`` is successfully used
            with a query that involves :func:`_orm.joinedload`, SQLAlchemy will
            attempt to emit SQL that locks all involved tables.

        .. note::  It is generally a good idea to combine the use of the
           :meth:`_orm.Query.populate_existing` method when using the
           :meth:`_orm.Query.with_for_update` method.   The purpose of
           :meth:`_orm.Query.populate_existing` is to force all the data read
           from the SELECT to be populated into the ORM objects returned,
           even if these objects are already in the :term:`identity map`.

        .. seealso::

            :meth:`_expression.GenerativeSelect.with_for_update`
            - Core level method with
            full argument and behavioral description.

            :meth:`_orm.Query.populate_existing` - overwrites attributes of
            objects already loaded in the identity map.

        """
    def params(self, __params: Dict[str, Any] | None = None, **kw: Any) -> Self:
        """Add values for bind parameters which may have been
        specified in filter().

        Parameters may be specified using \\**kwargs, or optionally a single
        dictionary as the first positional argument. The reason for both is
        that \\**kwargs is convenient, however some parameter dictionaries
        contain unicode keys in which case \\**kwargs cannot be used.

        """
    def where(self, *criterion: _ColumnExpressionArgument[bool]) -> Self:
        """A synonym for :meth:`.Query.filter`.

        .. versionadded:: 1.4

        .. seealso::

            :meth:`_sql.Select.where` - v2 equivalent method.

        """
    def filter(self, *criterion: _ColumnExpressionArgument[bool]) -> Self:
        """Apply the given filtering criterion to a copy
        of this :class:`_query.Query`, using SQL expressions.

        e.g.::

            session.query(MyClass).filter(MyClass.name == 'some name')

        Multiple criteria may be specified as comma separated; the effect
        is that they will be joined together using the :func:`.and_`
        function::

            session.query(MyClass).\\\n                filter(MyClass.name == 'some name', MyClass.id > 5)

        The criterion is any SQL expression object applicable to the
        WHERE clause of a select.   String expressions are coerced
        into SQL expression constructs via the :func:`_expression.text`
        construct.

        .. seealso::

            :meth:`_query.Query.filter_by` - filter on keyword expressions.

            :meth:`_sql.Select.where` - v2 equivalent method.

        """
    def filter_by(self, **kwargs: Any) -> Self:
        """Apply the given filtering criterion to a copy
        of this :class:`_query.Query`, using keyword expressions.

        e.g.::

            session.query(MyClass).filter_by(name = 'some name')

        Multiple criteria may be specified as comma separated; the effect
        is that they will be joined together using the :func:`.and_`
        function::

            session.query(MyClass).\\\n                filter_by(name = 'some name', id = 5)

        The keyword expressions are extracted from the primary
        entity of the query, or the last entity that was the
        target of a call to :meth:`_query.Query.join`.

        .. seealso::

            :meth:`_query.Query.filter` - filter on SQL expressions.

            :meth:`_sql.Select.filter_by` - v2 comparable method.

        """
    def order_by(self, __first: Literal[None, False, _NoArg.NO_ARG] | _ColumnExpressionOrStrLabelArgument[Any] = ..., *clauses: _ColumnExpressionOrStrLabelArgument[Any]) -> Self:
        """Apply one or more ORDER BY criteria to the query and return
        the newly resulting :class:`_query.Query`.

        e.g.::

            q = session.query(Entity).order_by(Entity.id, Entity.name)

        Calling this method multiple times is equivalent to calling it once
        with all the clauses concatenated. All existing ORDER BY criteria may
        be cancelled by passing ``None`` by itself.  New ORDER BY criteria may
        then be added by invoking :meth:`_orm.Query.order_by` again, e.g.::

            # will erase all ORDER BY and ORDER BY new_col alone
            q = q.order_by(None).order_by(new_col)

        .. seealso::

            These sections describe ORDER BY in terms of :term:`2.0 style`
            invocation but apply to :class:`_orm.Query` as well:

            :ref:`tutorial_order_by` - in the :ref:`unified_tutorial`

            :ref:`tutorial_order_by_label` - in the :ref:`unified_tutorial`

            :meth:`_sql.Select.order_by` - v2 equivalent method.

        """
    def group_by(self, __first: Literal[None, False, _NoArg.NO_ARG] | _ColumnExpressionOrStrLabelArgument[Any] = ..., *clauses: _ColumnExpressionOrStrLabelArgument[Any]) -> Self:
        """Apply one or more GROUP BY criterion to the query and return
        the newly resulting :class:`_query.Query`.

        All existing GROUP BY settings can be suppressed by
        passing ``None`` - this will suppress any GROUP BY configured
        on mappers as well.

        .. seealso::

            These sections describe GROUP BY in terms of :term:`2.0 style`
            invocation but apply to :class:`_orm.Query` as well:

            :ref:`tutorial_group_by_w_aggregates` - in the
            :ref:`unified_tutorial`

            :ref:`tutorial_order_by_label` - in the :ref:`unified_tutorial`

            :meth:`_sql.Select.group_by` - v2 equivalent method.

        """
    def having(self, *having: _ColumnExpressionArgument[bool]) -> Self:
        """Apply a HAVING criterion to the query and return the
        newly resulting :class:`_query.Query`.

        :meth:`_query.Query.having` is used in conjunction with
        :meth:`_query.Query.group_by`.

        HAVING criterion makes it possible to use filters on aggregate
        functions like COUNT, SUM, AVG, MAX, and MIN, eg.::

            q = session.query(User.id).\\\n                        join(User.addresses).\\\n                        group_by(User.id).\\\n                        having(func.count(Address.id) > 2)

        .. seealso::

            :meth:`_sql.Select.having` - v2 equivalent method.

        """
    def union(self, *q: Query[Any]) -> Self:
        """Produce a UNION of this Query against one or more queries.

        e.g.::

            q1 = sess.query(SomeClass).filter(SomeClass.foo=='bar')
            q2 = sess.query(SomeClass).filter(SomeClass.bar=='foo')

            q3 = q1.union(q2)

        The method accepts multiple Query objects so as to control
        the level of nesting.  A series of ``union()`` calls such as::

            x.union(y).union(z).all()

        will nest on each ``union()``, and produces::

            SELECT * FROM (SELECT * FROM (SELECT * FROM X UNION
                            SELECT * FROM y) UNION SELECT * FROM Z)

        Whereas::

            x.union(y, z).all()

        produces::

            SELECT * FROM (SELECT * FROM X UNION SELECT * FROM y UNION
                            SELECT * FROM Z)

        Note that many database backends do not allow ORDER BY to
        be rendered on a query called within UNION, EXCEPT, etc.
        To disable all ORDER BY clauses including those configured
        on mappers, issue ``query.order_by(None)`` - the resulting
        :class:`_query.Query` object will not render ORDER BY within
        its SELECT statement.

        .. seealso::

            :meth:`_sql.Select.union` - v2 equivalent method.

        """
    def union_all(self, *q: Query[Any]) -> Self:
        """Produce a UNION ALL of this Query against one or more queries.

        Works the same way as :meth:`~sqlalchemy.orm.query.Query.union`. See
        that method for usage examples.

        .. seealso::

            :meth:`_sql.Select.union_all` - v2 equivalent method.

        """
    def intersect(self, *q: Query[Any]) -> Self:
        """Produce an INTERSECT of this Query against one or more queries.

        Works the same way as :meth:`~sqlalchemy.orm.query.Query.union`. See
        that method for usage examples.

        .. seealso::

            :meth:`_sql.Select.intersect` - v2 equivalent method.

        """
    def intersect_all(self, *q: Query[Any]) -> Self:
        """Produce an INTERSECT ALL of this Query against one or more queries.

        Works the same way as :meth:`~sqlalchemy.orm.query.Query.union`. See
        that method for usage examples.

        .. seealso::

            :meth:`_sql.Select.intersect_all` - v2 equivalent method.

        """
    def except_(self, *q: Query[Any]) -> Self:
        """Produce an EXCEPT of this Query against one or more queries.

        Works the same way as :meth:`~sqlalchemy.orm.query.Query.union`. See
        that method for usage examples.

        .. seealso::

            :meth:`_sql.Select.except_` - v2 equivalent method.

        """
    def except_all(self, *q: Query[Any]) -> Self:
        """Produce an EXCEPT ALL of this Query against one or more queries.

        Works the same way as :meth:`~sqlalchemy.orm.query.Query.union`. See
        that method for usage examples.

        .. seealso::

            :meth:`_sql.Select.except_all` - v2 equivalent method.

        """
    def join(self, target: _JoinTargetArgument, onclause: _OnClauseArgument | None = None, *, isouter: bool = False, full: bool = False) -> Self:
        '''Create a SQL JOIN against this :class:`_query.Query`
        object\'s criterion
        and apply generatively, returning the newly resulting
        :class:`_query.Query`.

        **Simple Relationship Joins**

        Consider a mapping between two classes ``User`` and ``Address``,
        with a relationship ``User.addresses`` representing a collection
        of ``Address`` objects associated with each ``User``.   The most
        common usage of :meth:`_query.Query.join`
        is to create a JOIN along this
        relationship, using the ``User.addresses`` attribute as an indicator
        for how this should occur::

            q = session.query(User).join(User.addresses)

        Where above, the call to :meth:`_query.Query.join` along
        ``User.addresses`` will result in SQL approximately equivalent to::

            SELECT user.id, user.name
            FROM user JOIN address ON user.id = address.user_id

        In the above example we refer to ``User.addresses`` as passed to
        :meth:`_query.Query.join` as the "on clause", that is, it indicates
        how the "ON" portion of the JOIN should be constructed.

        To construct a chain of joins, multiple :meth:`_query.Query.join`
        calls may be used.  The relationship-bound attribute implies both
        the left and right side of the join at once::

            q = session.query(User).\\\n                    join(User.orders).\\\n                    join(Order.items).\\\n                    join(Item.keywords)

        .. note:: as seen in the above example, **the order in which each
           call to the join() method occurs is important**.    Query would not,
           for example, know how to join correctly if we were to specify
           ``User``, then ``Item``, then ``Order``, in our chain of joins; in
           such a case, depending on the arguments passed, it may raise an
           error that it doesn\'t know how to join, or it may produce invalid
           SQL in which case the database will raise an error. In correct
           practice, the
           :meth:`_query.Query.join` method is invoked in such a way that lines
           up with how we would want the JOIN clauses in SQL to be
           rendered, and each call should represent a clear link from what
           precedes it.

        **Joins to a Target Entity or Selectable**

        A second form of :meth:`_query.Query.join` allows any mapped entity or
        core selectable construct as a target.   In this usage,
        :meth:`_query.Query.join` will attempt to create a JOIN along the
        natural foreign key relationship between two entities::

            q = session.query(User).join(Address)

        In the above calling form, :meth:`_query.Query.join` is called upon to
        create the "on clause" automatically for us.  This calling form will
        ultimately raise an error if either there are no foreign keys between
        the two entities, or if there are multiple foreign key linkages between
        the target entity and the entity or entities already present on the
        left side such that creating a join requires more information.  Note
        that when indicating a join to a target without any ON clause, ORM
        configured relationships are not taken into account.

        **Joins to a Target with an ON Clause**

        The third calling form allows both the target entity as well
        as the ON clause to be passed explicitly.    A example that includes
        a SQL expression as the ON clause is as follows::

            q = session.query(User).join(Address, User.id==Address.user_id)

        The above form may also use a relationship-bound attribute as the
        ON clause as well::

            q = session.query(User).join(Address, User.addresses)

        The above syntax can be useful for the case where we wish
        to join to an alias of a particular target entity.  If we wanted
        to join to ``Address`` twice, it could be achieved using two
        aliases set up using the :func:`~sqlalchemy.orm.aliased` function::

            a1 = aliased(Address)
            a2 = aliased(Address)

            q = session.query(User).\\\n                    join(a1, User.addresses).\\\n                    join(a2, User.addresses).\\\n                    filter(a1.email_address==\'ed@foo.com\').\\\n                    filter(a2.email_address==\'ed@bar.com\')

        The relationship-bound calling form can also specify a target entity
        using the :meth:`_orm.PropComparator.of_type` method; a query
        equivalent to the one above would be::

            a1 = aliased(Address)
            a2 = aliased(Address)

            q = session.query(User).\\\n                    join(User.addresses.of_type(a1)).\\\n                    join(User.addresses.of_type(a2)).\\\n                    filter(a1.email_address == \'ed@foo.com\').\\\n                    filter(a2.email_address == \'ed@bar.com\')

        **Augmenting Built-in ON Clauses**

        As a substitute for providing a full custom ON condition for an
        existing relationship, the :meth:`_orm.PropComparator.and_` function
        may be applied to a relationship attribute to augment additional
        criteria into the ON clause; the additional criteria will be combined
        with the default criteria using AND::

            q = session.query(User).join(
                User.addresses.and_(Address.email_address != \'foo@bar.com\')
            )

        .. versionadded:: 1.4

        **Joining to Tables and Subqueries**


        The target of a join may also be any table or SELECT statement,
        which may be related to a target entity or not.   Use the
        appropriate ``.subquery()`` method in order to make a subquery
        out of a query::

            subq = session.query(Address).\\\n                filter(Address.email_address == \'ed@foo.com\').\\\n                subquery()


            q = session.query(User).join(
                subq, User.id == subq.c.user_id
            )

        Joining to a subquery in terms of a specific relationship and/or
        target entity may be achieved by linking the subquery to the
        entity using :func:`_orm.aliased`::

            subq = session.query(Address).\\\n                filter(Address.email_address == \'ed@foo.com\').\\\n                subquery()

            address_subq = aliased(Address, subq)

            q = session.query(User).join(
                User.addresses.of_type(address_subq)
            )


        **Controlling what to Join From**

        In cases where the left side of the current state of
        :class:`_query.Query` is not in line with what we want to join from,
        the :meth:`_query.Query.select_from` method may be used::

            q = session.query(Address).select_from(User).\\\n                            join(User.addresses).\\\n                            filter(User.name == \'ed\')

        Which will produce SQL similar to::

            SELECT address.* FROM user
                JOIN address ON user.id=address.user_id
                WHERE user.name = :name_1

        .. seealso::

            :meth:`_sql.Select.join` - v2 equivalent method.

        :param \\*props: Incoming arguments for :meth:`_query.Query.join`,
         the props collection in modern use should be considered to be a  one
         or two argument form, either as a single "target" entity or ORM
         attribute-bound relationship, or as a target entity plus an "on
         clause" which  may be a SQL expression or ORM attribute-bound
         relationship.

        :param isouter=False: If True, the join used will be a left outer join,
         just as if the :meth:`_query.Query.outerjoin` method were called.

        :param full=False: render FULL OUTER JOIN; implies ``isouter``.

        '''
    def outerjoin(self, target: _JoinTargetArgument, onclause: _OnClauseArgument | None = None, *, full: bool = False) -> Self:
        """Create a left outer join against this ``Query`` object's criterion
        and apply generatively, returning the newly resulting ``Query``.

        Usage is the same as the ``join()`` method.

        .. seealso::

            :meth:`_sql.Select.outerjoin` - v2 equivalent method.

        """
    def reset_joinpoint(self) -> Self:
        '''Return a new :class:`.Query`, where the "join point" has
        been reset back to the base FROM entities of the query.

        This method is usually used in conjunction with the
        ``aliased=True`` feature of the :meth:`~.Query.join`
        method.  See the example in :meth:`~.Query.join` for how
        this is used.

        '''
    def select_from(self, *from_obj: _FromClauseArgument) -> Self:
        '''Set the FROM clause of this :class:`.Query` explicitly.

        :meth:`.Query.select_from` is often used in conjunction with
        :meth:`.Query.join` in order to control which entity is selected
        from on the "left" side of the join.

        The entity or selectable object here effectively replaces the
        "left edge" of any calls to :meth:`~.Query.join`, when no
        joinpoint is otherwise established - usually, the default "join
        point" is the leftmost entity in the :class:`~.Query` object\'s
        list of entities to be selected.

        A typical example::

            q = session.query(Address).select_from(User).\\\n                join(User.addresses).\\\n                filter(User.name == \'ed\')

        Which produces SQL equivalent to::

            SELECT address.* FROM user
            JOIN address ON user.id=address.user_id
            WHERE user.name = :name_1

        :param \\*from_obj: collection of one or more entities to apply
         to the FROM clause.  Entities can be mapped classes,
         :class:`.AliasedClass` objects, :class:`.Mapper` objects
         as well as core :class:`.FromClause` elements like subqueries.

        .. seealso::

            :meth:`~.Query.join`

            :meth:`.Query.select_entity_from`

            :meth:`_sql.Select.select_from` - v2 equivalent method.

        '''
    def __getitem__(self, item: Any) -> Any: ...
    def slice(self, start: int, stop: int) -> Self:
        '''Computes the "slice" of the :class:`_query.Query` represented by
        the given indices and returns the resulting :class:`_query.Query`.

        The start and stop indices behave like the argument to Python\'s
        built-in :func:`range` function. This method provides an
        alternative to using ``LIMIT``/``OFFSET`` to get a slice of the
        query.

        For example, ::

            session.query(User).order_by(User.id).slice(1, 3)

        renders as

        .. sourcecode:: sql

           SELECT users.id AS users_id,
                  users.name AS users_name
           FROM users ORDER BY users.id
           LIMIT ? OFFSET ?
           (2, 1)

        .. seealso::

           :meth:`_query.Query.limit`

           :meth:`_query.Query.offset`

           :meth:`_sql.Select.slice` - v2 equivalent method.

        '''
    def limit(self, limit: _LimitOffsetType) -> Self:
        """Apply a ``LIMIT`` to the query and return the newly resulting
        ``Query``.

        .. seealso::

            :meth:`_sql.Select.limit` - v2 equivalent method.

        """
    def offset(self, offset: _LimitOffsetType) -> Self:
        """Apply an ``OFFSET`` to the query and return the newly resulting
        ``Query``.

        .. seealso::

            :meth:`_sql.Select.offset` - v2 equivalent method.
        """
    def distinct(self, *expr: _ColumnExpressionArgument[Any]) -> Self:
        """Apply a ``DISTINCT`` to the query and return the newly resulting
        ``Query``.


        .. note::

            The ORM-level :meth:`.distinct` call includes logic that will
            automatically add columns from the ORDER BY of the query to the
            columns clause of the SELECT statement, to satisfy the common need
            of the database backend that ORDER BY columns be part of the SELECT
            list when DISTINCT is used.   These columns *are not* added to the
            list of columns actually fetched by the :class:`_query.Query`,
            however,
            so would not affect results. The columns are passed through when
            using the :attr:`_query.Query.statement` accessor, however.

            .. deprecated:: 2.0  This logic is deprecated and will be removed
               in SQLAlchemy 2.0.     See :ref:`migration_20_query_distinct`
               for a description of this use case in 2.0.

        .. seealso::

            :meth:`_sql.Select.distinct` - v2 equivalent method.

        :param \\*expr: optional column expressions.  When present,
         the PostgreSQL dialect will render a ``DISTINCT ON (<expressions>)``
         construct.

         .. deprecated:: 1.4 Using \\*expr in other dialects is deprecated
            and will raise :class:`_exc.CompileError` in a future version.

        """
    def all(self) -> List[_T]:
        """Return the results represented by this :class:`_query.Query`
        as a list.

        This results in an execution of the underlying SQL statement.

        .. warning::  The :class:`_query.Query` object,
           when asked to return either
           a sequence or iterator that consists of full ORM-mapped entities,
           will **deduplicate entries based on primary key**.  See the FAQ for
           more details.

            .. seealso::

                :ref:`faq_query_deduplicating`

        .. seealso::

            :meth:`_engine.Result.all` - v2 comparable method.

            :meth:`_engine.Result.scalars` - v2 comparable method.
        """
    def from_statement(self, statement: ExecutableReturnsRows) -> Self:
        """Execute the given SELECT statement and return results.

        This method bypasses all internal statement compilation, and the
        statement is executed without modification.

        The statement is typically either a :func:`_expression.text`
        or :func:`_expression.select` construct, and should return the set
        of columns
        appropriate to the entity class represented by this
        :class:`_query.Query`.

        .. seealso::

            :meth:`_sql.Select.from_statement` - v2 comparable method.

        """
    def first(self) -> _T | None:
        """Return the first result of this ``Query`` or
        None if the result doesn't contain any row.

        first() applies a limit of one within the generated SQL, so that
        only one primary entity row is generated on the server side
        (note this may consist of multiple result rows if join-loaded
        collections are present).

        Calling :meth:`_query.Query.first`
        results in an execution of the underlying
        query.

        .. seealso::

            :meth:`_query.Query.one`

            :meth:`_query.Query.one_or_none`

            :meth:`_engine.Result.first` - v2 comparable method.

            :meth:`_engine.Result.scalars` - v2 comparable method.

        """
    def one_or_none(self) -> _T | None:
        """Return at most one result or raise an exception.

        Returns ``None`` if the query selects
        no rows.  Raises ``sqlalchemy.orm.exc.MultipleResultsFound``
        if multiple object identities are returned, or if multiple
        rows are returned for a query that returns only scalar values
        as opposed to full identity-mapped entities.

        Calling :meth:`_query.Query.one_or_none`
        results in an execution of the
        underlying query.

        .. seealso::

            :meth:`_query.Query.first`

            :meth:`_query.Query.one`

            :meth:`_engine.Result.one_or_none` - v2 comparable method.

            :meth:`_engine.Result.scalar_one_or_none` - v2 comparable method.

        """
    def one(self) -> _T:
        """Return exactly one result or raise an exception.

        Raises ``sqlalchemy.orm.exc.NoResultFound`` if the query selects
        no rows.  Raises ``sqlalchemy.orm.exc.MultipleResultsFound``
        if multiple object identities are returned, or if multiple
        rows are returned for a query that returns only scalar values
        as opposed to full identity-mapped entities.

        Calling :meth:`.one` results in an execution of the underlying query.

        .. seealso::

            :meth:`_query.Query.first`

            :meth:`_query.Query.one_or_none`

            :meth:`_engine.Result.one` - v2 comparable method.

            :meth:`_engine.Result.scalar_one` - v2 comparable method.

        """
    def scalar(self) -> Any:
        """Return the first element of the first result or None
        if no rows present.  If multiple rows are returned,
        raises MultipleResultsFound.

          >>> session.query(Item).scalar()
          <Item>
          >>> session.query(Item.id).scalar()
          1
          >>> session.query(Item.id).filter(Item.id < 0).scalar()
          None
          >>> session.query(Item.id, Item.name).scalar()
          1
          >>> session.query(func.count(Parent.id)).scalar()
          20

        This results in an execution of the underlying query.

        .. seealso::

            :meth:`_engine.Result.scalar` - v2 comparable method.

        """
    def __iter__(self) -> Iterator[_T]: ...
    @property
    def column_descriptions(self) -> List[ORMColumnDescription]:
        """Return metadata about the columns which would be
        returned by this :class:`_query.Query`.

        Format is a list of dictionaries::

            user_alias = aliased(User, name='user2')
            q = sess.query(User, User.id, user_alias)

            # this expression:
            q.column_descriptions

            # would return:
            [
                {
                    'name':'User',
                    'type':User,
                    'aliased':False,
                    'expr':User,
                    'entity': User
                },
                {
                    'name':'id',
                    'type':Integer(),
                    'aliased':False,
                    'expr':User.id,
                    'entity': User
                },
                {
                    'name':'user2',
                    'type':User,
                    'aliased':True,
                    'expr':user_alias,
                    'entity': user_alias
                }
            ]

        .. seealso::

            This API is available using :term:`2.0 style` queries as well,
            documented at:

            * :ref:`queryguide_inspection`

            * :attr:`.Select.column_descriptions`

        """
    def instances(self, result_proxy: CursorResult[Any], context: QueryContext | None = None) -> Any:
        """Return an ORM result given a :class:`_engine.CursorResult` and
        :class:`.QueryContext`.

        """
    def merge_result(self, iterator: FrozenResult[Any] | Iterable[Sequence[Any]] | Iterable[object], load: bool = True) -> FrozenResult[Any] | Iterable[Any]:
        """Merge a result into this :class:`_query.Query` object's Session.

        Given an iterator returned by a :class:`_query.Query`
        of the same structure
        as this one, return an identical iterator of results, with all mapped
        instances merged into the session using :meth:`.Session.merge`. This
        is an optimized method which will merge all mapped instances,
        preserving the structure of the result rows and unmapped columns with
        less method overhead than that of calling :meth:`.Session.merge`
        explicitly for each value.

        The structure of the results is determined based on the column list of
        this :class:`_query.Query` - if these do not correspond,
        unchecked errors
        will occur.

        The 'load' argument is the same as that of :meth:`.Session.merge`.

        For an example of how :meth:`_query.Query.merge_result` is used, see
        the source code for the example :ref:`examples_caching`, where
        :meth:`_query.Query.merge_result` is used to efficiently restore state
        from a cache back into a target :class:`.Session`.

        """
    def exists(self) -> Exists:
        """A convenience method that turns a query into an EXISTS subquery
        of the form EXISTS (SELECT 1 FROM ... WHERE ...).

        e.g.::

            q = session.query(User).filter(User.name == 'fred')
            session.query(q.exists())

        Producing SQL similar to::

            SELECT EXISTS (
                SELECT 1 FROM users WHERE users.name = :name_1
            ) AS anon_1

        The EXISTS construct is usually used in the WHERE clause::

            session.query(User.id).filter(q.exists()).scalar()

        Note that some databases such as SQL Server don't allow an
        EXISTS expression to be present in the columns clause of a
        SELECT.    To select a simple boolean value based on the exists
        as a WHERE, use :func:`.literal`::

            from sqlalchemy import literal

            session.query(literal(True)).filter(q.exists()).scalar()

        .. seealso::

            :meth:`_sql.Select.exists` - v2 comparable method.

        """
    def count(self) -> int:
        '''Return a count of rows this the SQL formed by this :class:`Query`
        would return.

        This generates the SQL for this Query as follows::

            SELECT count(1) AS count_1 FROM (
                SELECT <rest of query follows...>
            ) AS anon_1

        The above SQL returns a single row, which is the aggregate value
        of the count function; the :meth:`_query.Query.count`
        method then returns
        that single integer value.

        .. warning::

            It is important to note that the value returned by
            count() is **not the same as the number of ORM objects that this
            Query would return from a method such as the .all() method**.
            The :class:`_query.Query` object,
            when asked to return full entities,
            will **deduplicate entries based on primary key**, meaning if the
            same primary key value would appear in the results more than once,
            only one object of that primary key would be present.  This does
            not apply to a query that is against individual columns.

            .. seealso::

                :ref:`faq_query_deduplicating`

        For fine grained control over specific columns to count, to skip the
        usage of a subquery or otherwise control of the FROM clause, or to use
        other aggregate functions, use :attr:`~sqlalchemy.sql.expression.func`
        expressions in conjunction with :meth:`~.Session.query`, i.e.::

            from sqlalchemy import func

            # count User records, without
            # using a subquery.
            session.query(func.count(User.id))

            # return count of user "id" grouped
            # by "name"
            session.query(func.count(User.id)).\\\n                    group_by(User.name)

            from sqlalchemy import distinct

            # count distinct "name" values
            session.query(func.count(distinct(User.name)))

        .. seealso::

            :ref:`migration_20_query_usage`

        '''
    def delete(self, synchronize_session: SynchronizeSessionArgument = 'auto') -> int:
        '''Perform a DELETE with an arbitrary WHERE clause.

        Deletes rows matched by this query from the database.

        E.g.::

            sess.query(User).filter(User.age == 25).\\\n                delete(synchronize_session=False)

            sess.query(User).filter(User.age == 25).\\\n                delete(synchronize_session=\'evaluate\')

        .. warning::

            See the section :ref:`orm_expression_update_delete` for important
            caveats and warnings, including limitations when using bulk UPDATE
            and DELETE with mapper inheritance configurations.

        :param synchronize_session: chooses the strategy to update the
         attributes on objects in the session.   See the section
         :ref:`orm_expression_update_delete` for a discussion of these
         strategies.

        :return: the count of rows matched as returned by the database\'s
          "row count" feature.

        .. seealso::

            :ref:`orm_expression_update_delete`

        '''
    def update(self, values: Dict[_DMLColumnArgument, Any], synchronize_session: SynchronizeSessionArgument = 'auto', update_args: Dict[Any, Any] | None = None) -> int:
        '''Perform an UPDATE with an arbitrary WHERE clause.

        Updates rows matched by this query in the database.

        E.g.::

            sess.query(User).filter(User.age == 25).\\\n                update({User.age: User.age - 10}, synchronize_session=False)

            sess.query(User).filter(User.age == 25).\\\n                update({"age": User.age - 10}, synchronize_session=\'evaluate\')

        .. warning::

            See the section :ref:`orm_expression_update_delete` for important
            caveats and warnings, including limitations when using arbitrary
            UPDATE and DELETE with mapper inheritance configurations.

        :param values: a dictionary with attributes names, or alternatively
         mapped attributes or SQL expressions, as keys, and literal
         values or sql expressions as values.   If :ref:`parameter-ordered
         mode <tutorial_parameter_ordered_updates>` is desired, the values can
         be passed as a list of 2-tuples; this requires that the
         :paramref:`~sqlalchemy.sql.expression.update.preserve_parameter_order`
         flag is passed to the :paramref:`.Query.update.update_args` dictionary
         as well.

        :param synchronize_session: chooses the strategy to update the
         attributes on objects in the session.   See the section
         :ref:`orm_expression_update_delete` for a discussion of these
         strategies.

        :param update_args: Optional dictionary, if present will be passed
         to the underlying :func:`_expression.update`
         construct as the ``**kw`` for
         the object.  May be used to pass dialect-specific arguments such
         as ``mysql_limit``, as well as other special arguments such as
         :paramref:`~sqlalchemy.sql.expression.update.preserve_parameter_order`.

        :return: the count of rows matched as returned by the database\'s
         "row count" feature.


        .. seealso::

            :ref:`orm_expression_update_delete`

        '''

class AliasOption(interfaces.LoaderOption):
    inherit_cache: bool
    def __init__(self, alias: Alias | Subquery) -> None:
        """Return a :class:`.MapperOption` that will indicate to the
        :class:`_query.Query`
        that the main table has been aliased.

        """
    def process_compile_state(self, compile_state: ORMCompileState) -> None: ...

class BulkUD:
    """State used for the orm.Query version of update() / delete().

    This object is now specific to Query only.

    """
    query: Incomplete
    mapper: Incomplete
    def __init__(self, query: Query[Any]) -> None: ...
    @property
    def session(self) -> Session: ...

class BulkUpdate(BulkUD):
    """BulkUD which handles UPDATEs."""
    values: Incomplete
    update_kwargs: Incomplete
    def __init__(self, query: Query[Any], values: Dict[_DMLColumnArgument, Any], update_kwargs: Dict[Any, Any] | None) -> None: ...

class BulkDelete(BulkUD):
    """BulkUD which handles DELETEs."""

class RowReturningQuery(Query[Row[_TP]]):
    def tuples(self) -> Query[_TP]: ...
