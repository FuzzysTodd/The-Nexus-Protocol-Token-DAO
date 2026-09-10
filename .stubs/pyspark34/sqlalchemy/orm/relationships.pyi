import dataclasses
from . import attributes as attributes, strategy_options as strategy_options
from .. import Exists as Exists, log as log, schema as schema, sql as sql, util as util
from ..inspection import inspect as inspect
from ..sql import coercions as coercions, expression as expression, operators as operators, roles as roles, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument, _EquivalentColumnMap, _InfoType
from ..sql.annotation import SupportsAnnotations as SupportsAnnotations
from ..sql.elements import BinaryExpression as BinaryExpression, BindParameter as BindParameter, ClauseElement as ClauseElement, ColumnClause as ColumnClause, ColumnElement as ColumnElement
from ..sql.schema import Table as Table
from ..sql.selectable import FromClause as FromClause
from ..sql.util import ClauseAdapter as ClauseAdapter, adapt_criterion_to_null as adapt_criterion_to_null, join_condition as join_condition, selectables_overlap as selectables_overlap, visit_binary_product as visit_binary_product
from ..util.typing import Literal as Literal, RODescriptorReference as RODescriptorReference, _AnnotationScanType, de_optionalize_union_types as de_optionalize_union_types, resolve_name_to_real_class_name as resolve_name_to_real_class_name
from ._typing import _EntityType, _IdentityKeyType, _InstanceDict, _InternalEntityType, _RegistryType, insp_is_aliased_class as insp_is_aliased_class, is_has_collection_adapter as is_has_collection_adapter
from .base import DynamicMapped as DynamicMapped, LoaderCallableStatus as LoaderCallableStatus, Mapped as Mapped, PassiveFlag as PassiveFlag, WriteOnlyMapped as WriteOnlyMapped, _DeclarativeMapped, class_mapper as class_mapper, state_str as state_str
from .decl_base import _ClassScanMapperConfig
from .dependency import DependencyProcessor as DependencyProcessor
from .interfaces import MANYTOMANY as MANYTOMANY, MANYTOONE as MANYTOONE, ONETOMANY as ONETOMANY, PropComparator as PropComparator, RelationshipDirection as RelationshipDirection, StrategizedProperty as StrategizedProperty, _AttributeOptions, _IntrospectsAnnotations
from .mapper import Mapper as Mapper
from .query import Query as Query
from .session import Session as Session
from .state import InstanceState as InstanceState
from .strategies import LazyLoader as LazyLoader
from .util import AliasedClass as AliasedClass, AliasedInsp as AliasedInsp, CascadeOptions as CascadeOptions
from _typeshed import Incomplete
from typing import Any, Callable, Collection, Dict, Generic, Iterator, NamedTuple, NoReturn, Set, Tuple, Type

ORMBackrefArgument = str | Tuple[str, Dict[str, Any]]

def remote(expr: _CEA) -> _CEA:
    """Annotate a portion of a primaryjoin expression
    with a 'remote' annotation.

    See the section :ref:`relationship_custom_foreign` for a
    description of use.

    .. seealso::

        :ref:`relationship_custom_foreign`

        :func:`.foreign`

    """
def foreign(expr: _CEA) -> _CEA:
    """Annotate a portion of a primaryjoin expression
    with a 'foreign' annotation.

    See the section :ref:`relationship_custom_foreign` for a
    description of use.

    .. seealso::

        :ref:`relationship_custom_foreign`

        :func:`.remote`

    """

@dataclasses.dataclass
class _RelationshipArg(Generic[_T1, _T2]):
    """stores a user-defined parameter value that must be resolved and
    parsed later at mapper configuration time.

    """
    name: str
    argument: _T1
    resolved: _T2 | None
    def __init__(self, name, argument, resolved) -> None: ...

class _RelationshipArgs(NamedTuple):
    """stores user-passed parameters that are resolved at mapper configuration
    time.

    """
    secondary: _RelationshipArg[_RelationshipSecondaryArgument | None, FromClause | None]
    primaryjoin: _RelationshipArg[_RelationshipJoinConditionArgument | None, ColumnElement[Any] | None]
    secondaryjoin: _RelationshipArg[_RelationshipJoinConditionArgument | None, ColumnElement[Any] | None]
    order_by: _RelationshipArg[_ORMOrderByArgument, _RelationshipOrderByArg]
    foreign_keys: _RelationshipArg[_ORMColCollectionArgument | None, Set[ColumnElement[Any]]]
    remote_side: _RelationshipArg[_ORMColCollectionArgument | None, Set[ColumnElement[Any]]]

class RelationshipProperty(_IntrospectsAnnotations, StrategizedProperty[_T], log.Identified):
    """Describes an object property that holds a single item or list
    of items that correspond to a related database table.

    Public constructor is the :func:`_orm.relationship` function.

    .. seealso::

        :ref:`relationship_config_toplevel`

    """
    strategy_wildcard_key: Incomplete
    inherit_cache: bool
    primaryjoin: ColumnElement[bool]
    secondaryjoin: ColumnElement[bool] | None
    secondary: FromClause | None
    order_by: _RelationshipOrderByArg
    remote_side: Set[ColumnElement[Any]]
    local_columns: Set[ColumnElement[Any]]
    synchronize_pairs: _ColumnPairs
    secondary_synchronize_pairs: _ColumnPairs | None
    local_remote_pairs: _ColumnPairs | None
    direction: RelationshipDirection
    uselist: Incomplete
    argument: Incomplete
    post_update: Incomplete
    viewonly: Incomplete
    sync_backref: Incomplete
    lazy: Incomplete
    single_parent: Incomplete
    collection_class: Incomplete
    passive_deletes: Incomplete
    passive_updates: Incomplete
    enable_typechecks: Incomplete
    query_class: Incomplete
    innerjoin: Incomplete
    distinct_target_key: Incomplete
    doc: Incomplete
    active_history: Incomplete
    join_depth: Incomplete
    omit_join: Incomplete
    load_on_pending: Incomplete
    comparator_factory: Incomplete
    strategy_key: Incomplete
    back_populates: Incomplete
    backref: Incomplete
    def __init__(self, argument: _RelationshipArgumentType[_T] | None = None, secondary: _RelationshipSecondaryArgument | None = None, *, uselist: bool | None = None, collection_class: Type[Collection[Any]] | Callable[[], Collection[Any]] | None = None, primaryjoin: _RelationshipJoinConditionArgument | None = None, secondaryjoin: _RelationshipJoinConditionArgument | None = None, back_populates: str | None = None, order_by: _ORMOrderByArgument = False, backref: ORMBackrefArgument | None = None, overlaps: str | None = None, post_update: bool = False, cascade: str = 'save-update, merge', viewonly: bool = False, attribute_options: _AttributeOptions | None = None, lazy: _LazyLoadArgumentType = 'select', passive_deletes: Literal['all'] | bool = False, passive_updates: bool = True, active_history: bool = False, enable_typechecks: bool = True, foreign_keys: _ORMColCollectionArgument | None = None, remote_side: _ORMColCollectionArgument | None = None, join_depth: int | None = None, comparator_factory: Type[RelationshipProperty.Comparator[Any]] | None = None, single_parent: bool = False, innerjoin: bool = False, distinct_target_key: bool | None = None, load_on_pending: bool = False, query_class: Type[Query[Any]] | None = None, info: _InfoType | None = None, omit_join: Literal[None, False] = None, sync_backref: bool | None = None, doc: str | None = None, bake_queries: Literal[True] = True, cascade_backrefs: Literal[False] = False, _local_remote_pairs: _ColumnPairs | None = None, _legacy_inactive_history_style: bool = False) -> None: ...
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...
    class Comparator(util.MemoizedSlots, PropComparator[_PT]):
        """Produce boolean, comparison, and other operators for
        :class:`.RelationshipProperty` attributes.

        See the documentation for :class:`.PropComparator` for a brief
        overview of ORM level operator definition.

        .. seealso::

            :class:`.PropComparator`

            :class:`.ColumnProperty.Comparator`

            :class:`.ColumnOperators`

            :ref:`types_operators`

            :attr:`.TypeEngine.comparator_factory`

        """
        prop: RODescriptorReference[RelationshipProperty[_PT]]
        def __init__(self, prop: RelationshipProperty[_PT], parentmapper: _InternalEntityType[Any], adapt_to_entity: AliasedInsp[Any] | None = None, of_type: _EntityType[_PT] | None = None, extra_criteria: Tuple[ColumnElement[bool], ...] = ()) -> None:
            """Construction of :class:`.RelationshipProperty.Comparator`
            is internal to the ORM's attribute mechanics.

            """
        def adapt_to_entity(self, adapt_to_entity: AliasedInsp[Any]) -> RelationshipProperty.Comparator[Any]: ...
        entity: _InternalEntityType[_PT]
        mapper: Mapper[_PT]
        def __clause_element__(self) -> ColumnElement[bool]: ...
        def of_type(self, class_: _EntityType[Any]) -> PropComparator[_PT]:
            """Redefine this object in terms of a polymorphic subclass.

            See :meth:`.PropComparator.of_type` for an example.


            """
        def and_(self, *criteria: _ColumnExpressionArgument[bool]) -> PropComparator[Any]:
            """Add AND criteria.

            See :meth:`.PropComparator.and_` for an example.

            .. versionadded:: 1.4

            """
        def in_(self, other: Any) -> NoReturn:
            """Produce an IN clause - this is not implemented
            for :func:`_orm.relationship`-based attributes at this time.

            """
        __hash__: Incomplete
        def __eq__(self, other: Any) -> ColumnElement[bool]:
            """Implement the ``==`` operator.

            In a many-to-one context, such as::

              MyClass.some_prop == <some object>

            this will typically produce a
            clause such as::

              mytable.related_id == <some id>

            Where ``<some id>`` is the primary key of the given
            object.

            The ``==`` operator provides partial functionality for non-
            many-to-one comparisons:

            * Comparisons against collections are not supported.
              Use :meth:`~.Relationship.Comparator.contains`.
            * Compared to a scalar one-to-many, will produce a
              clause that compares the target columns in the parent to
              the given target.
            * Compared to a scalar many-to-many, an alias
              of the association table will be rendered as
              well, forming a natural join that is part of the
              main body of the query. This will not work for
              queries that go beyond simple AND conjunctions of
              comparisons, such as those which use OR. Use
              explicit joins, outerjoins, or
              :meth:`~.Relationship.Comparator.has` for
              more comprehensive non-many-to-one scalar
              membership tests.
            * Comparisons against ``None`` given in a one-to-many
              or many-to-many context produce a NOT EXISTS clause.

            """
        def any(self, criterion: _ColumnExpressionArgument[bool] | None = None, **kwargs: Any) -> ColumnElement[bool]:
            """Produce an expression that tests a collection against
            particular criterion, using EXISTS.

            An expression like::

                session.query(MyClass).filter(
                    MyClass.somereference.any(SomeRelated.x==2)
                )


            Will produce a query like::

                SELECT * FROM my_table WHERE
                EXISTS (SELECT 1 FROM related WHERE related.my_id=my_table.id
                AND related.x=2)

            Because :meth:`~.Relationship.Comparator.any` uses
            a correlated subquery, its performance is not nearly as
            good when compared against large target tables as that of
            using a join.

            :meth:`~.Relationship.Comparator.any` is particularly
            useful for testing for empty collections::

                session.query(MyClass).filter(
                    ~MyClass.somereference.any()
                )

            will produce::

                SELECT * FROM my_table WHERE
                NOT (EXISTS (SELECT 1 FROM related WHERE
                related.my_id=my_table.id))

            :meth:`~.Relationship.Comparator.any` is only
            valid for collections, i.e. a :func:`_orm.relationship`
            that has ``uselist=True``.  For scalar references,
            use :meth:`~.Relationship.Comparator.has`.

            """
        def has(self, criterion: _ColumnExpressionArgument[bool] | None = None, **kwargs: Any) -> ColumnElement[bool]:
            """Produce an expression that tests a scalar reference against
            particular criterion, using EXISTS.

            An expression like::

                session.query(MyClass).filter(
                    MyClass.somereference.has(SomeRelated.x==2)
                )


            Will produce a query like::

                SELECT * FROM my_table WHERE
                EXISTS (SELECT 1 FROM related WHERE
                related.id==my_table.related_id AND related.x=2)

            Because :meth:`~.Relationship.Comparator.has` uses
            a correlated subquery, its performance is not nearly as
            good when compared against large target tables as that of
            using a join.

            :meth:`~.Relationship.Comparator.has` is only
            valid for scalar references, i.e. a :func:`_orm.relationship`
            that has ``uselist=False``.  For collection references,
            use :meth:`~.Relationship.Comparator.any`.

            """
        def contains(self, other: _ColumnExpressionArgument[Any], **kwargs: Any) -> ColumnElement[bool]:
            '''Return a simple expression that tests a collection for
            containment of a particular item.

            :meth:`~.Relationship.Comparator.contains` is
            only valid for a collection, i.e. a
            :func:`_orm.relationship` that implements
            one-to-many or many-to-many with ``uselist=True``.

            When used in a simple one-to-many context, an
            expression like::

                MyClass.contains(other)

            Produces a clause like::

                mytable.id == <some id>

            Where ``<some id>`` is the value of the foreign key
            attribute on ``other`` which refers to the primary
            key of its parent object. From this it follows that
            :meth:`~.Relationship.Comparator.contains` is
            very useful when used with simple one-to-many
            operations.

            For many-to-many operations, the behavior of
            :meth:`~.Relationship.Comparator.contains`
            has more caveats. The association table will be
            rendered in the statement, producing an "implicit"
            join, that is, includes multiple tables in the FROM
            clause which are equated in the WHERE clause::

                query(MyClass).filter(MyClass.contains(other))

            Produces a query like::

                SELECT * FROM my_table, my_association_table AS
                my_association_table_1 WHERE
                my_table.id = my_association_table_1.parent_id
                AND my_association_table_1.child_id = <some id>

            Where ``<some id>`` would be the primary key of
            ``other``. From the above, it is clear that
            :meth:`~.Relationship.Comparator.contains`
            will **not** work with many-to-many collections when
            used in queries that move beyond simple AND
            conjunctions, such as multiple
            :meth:`~.Relationship.Comparator.contains`
            expressions joined by OR. In such cases subqueries or
            explicit "outer joins" will need to be used instead.
            See :meth:`~.Relationship.Comparator.any` for
            a less-performant alternative using EXISTS, or refer
            to :meth:`_query.Query.outerjoin`
            as well as :ref:`orm_queryguide_joins`
            for more details on constructing outer joins.

            kwargs may be ignored by this operator but are required for API
            conformance.
            '''
        def __ne__(self, other: Any) -> ColumnElement[bool]:
            """Implement the ``!=`` operator.

            In a many-to-one context, such as::

              MyClass.some_prop != <some object>

            This will typically produce a clause such as::

              mytable.related_id != <some id>

            Where ``<some id>`` is the primary key of the
            given object.

            The ``!=`` operator provides partial functionality for non-
            many-to-one comparisons:

            * Comparisons against collections are not supported.
              Use
              :meth:`~.Relationship.Comparator.contains`
              in conjunction with :func:`_expression.not_`.
            * Compared to a scalar one-to-many, will produce a
              clause that compares the target columns in the parent to
              the given target.
            * Compared to a scalar many-to-many, an alias
              of the association table will be rendered as
              well, forming a natural join that is part of the
              main body of the query. This will not work for
              queries that go beyond simple AND conjunctions of
              comparisons, such as those which use OR. Use
              explicit joins, outerjoins, or
              :meth:`~.Relationship.Comparator.has` in
              conjunction with :func:`_expression.not_` for
              more comprehensive non-many-to-one scalar
              membership tests.
            * Comparisons against ``None`` given in a one-to-many
              or many-to-many context produce an EXISTS clause.

            """
    def merge(self, session: Session, source_state: InstanceState[Any], source_dict: _InstanceDict, dest_state: InstanceState[Any], dest_dict: _InstanceDict, load: bool, _recursive: Dict[Any, object], _resolve_conflict_map: Dict[_IdentityKeyType[Any], object]) -> None: ...
    def cascade_iterator(self, type_: str, state: InstanceState[Any], dict_: _InstanceDict, visited_states: Set[InstanceState[Any]], halt_on: Callable[[InstanceState[Any]], bool] | None = None) -> Iterator[Tuple[Any, Mapper[Any], InstanceState[Any], _InstanceDict]]: ...
    def entity(self) -> _InternalEntityType[_T]:
        """Return the target mapped entity, which is an inspect() of the
        class or aliased class that is referenced by this
        :class:`.RelationshipProperty`.

        """
    def mapper(self) -> Mapper[_T]:
        """Return the targeted :class:`_orm.Mapper` for this
        :class:`.RelationshipProperty`.

        """
    def do_init(self) -> None: ...
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: str | None, key: str, mapped_container: Type[Mapped[Any]] | None, annotation: _AnnotationScanType | None, extracted_mapped_annotation: _AnnotationScanType | None, is_dataclass_field: bool) -> None: ...
    @property
    def cascade(self) -> CascadeOptions:
        """Return the current cascade setting for this
        :class:`.RelationshipProperty`.
        """
    @cascade.setter
    def cascade(self, cascade: str | CascadeOptions) -> None: ...

class JoinCondition:
    primaryjoin_initial: ColumnElement[bool] | None
    primaryjoin: ColumnElement[bool]
    secondaryjoin: ColumnElement[bool] | None
    secondary: FromClause | None
    prop: RelationshipProperty[Any]
    synchronize_pairs: _ColumnPairs
    secondary_synchronize_pairs: _ColumnPairs
    direction: RelationshipDirection
    parent_persist_selectable: FromClause
    child_persist_selectable: FromClause
    parent_local_selectable: FromClause
    child_local_selectable: FromClause
    parent_equivalents: Incomplete
    child_equivalents: Incomplete
    consider_as_foreign_keys: Incomplete
    self_referential: Incomplete
    support_sync: Incomplete
    can_be_synced_fn: Incomplete
    def __init__(self, parent_persist_selectable: FromClause, child_persist_selectable: FromClause, parent_local_selectable: FromClause, child_local_selectable: FromClause, *, primaryjoin: ColumnElement[bool] | None = None, secondary: FromClause | None = None, secondaryjoin: ColumnElement[bool] | None = None, parent_equivalents: _EquivalentColumnMap | None = None, child_equivalents: _EquivalentColumnMap | None = None, consider_as_foreign_keys: Any = None, local_remote_pairs: _ColumnPairs | None = None, remote_side: Any = None, self_referential: Any = False, prop: RelationshipProperty[Any], support_sync: bool = True, can_be_synced_fn: Callable[..., bool] = ...) -> None: ...
    @property
    def primaryjoin_minus_local(self) -> ColumnElement[bool]: ...
    @property
    def secondaryjoin_minus_local(self) -> ColumnElement[bool]: ...
    def primaryjoin_reverse_remote(self) -> ColumnElement[bool]:
        '''Return the primaryjoin condition suitable for the
        "reverse" direction.

        If the primaryjoin was delivered here with pre-existing
        "remote" annotations, the local/remote annotations
        are reversed.  Otherwise, the local/remote annotations
        are removed.

        '''
    def remote_columns(self) -> Set[ColumnElement[Any]]: ...
    def local_columns(self) -> Set[ColumnElement[Any]]: ...
    def foreign_key_columns(self) -> Set[ColumnElement[Any]]: ...
    def join_targets(self, source_selectable: FromClause | None, dest_selectable: FromClause, aliased: bool, single_crit: ColumnElement[bool] | None = None, extra_criteria: Tuple[ColumnElement[bool], ...] = ()) -> Tuple[ColumnElement[bool], ColumnElement[bool] | None, FromClause | None, ClauseAdapter | None, FromClause]:
        """Given a source and destination selectable, create a
        join between them.

        This takes into account aliasing the join clause
        to reference the appropriate corresponding columns
        in the target objects, as well as the extra child
        criterion, equivalent column sets, etc.

        """
    def create_lazy_clause(self, reverse_direction: bool = False) -> Tuple[ColumnElement[bool], Dict[str, ColumnElement[Any]], Dict[ColumnElement[Any], ColumnElement[Any]]]: ...

class _ColInAnnotations:
    """Serializable object that tests for a name in c._annotations."""
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def __call__(self, c: ClauseElement) -> bool: ...

class Relationship(RelationshipProperty[_T], _DeclarativeMapped[_T], WriteOnlyMapped[_T], DynamicMapped[_T]):
    """Describes an object property that holds a single item or list
    of items that correspond to a related database table.

    Public constructor is the :func:`_orm.relationship` function.

    .. seealso::

        :ref:`relationship_config_toplevel`

    .. versionchanged:: 2.0 Added :class:`_orm.Relationship` as a Declarative
       compatible subclass for :class:`_orm.RelationshipProperty`.

    """
    inherit_cache: bool
