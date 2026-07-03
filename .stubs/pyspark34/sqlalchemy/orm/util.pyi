import enum
from . import attributes as attributes, exc as exc
from .. import event as event, inspection as inspection, sql as sql, util as util
from ..engine import Row as Row, RowMapping as RowMapping
from ..engine.result import result_tuple as result_tuple
from ..sql import coercions as coercions, expression as expression, lambdas as lambdas, roles as roles, util as sql_util, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument, _EquivalentColumnMap, _FromClauseArgument, _OnClauseArgument, is_selectable as is_selectable
from ..sql.annotation import SupportsCloneAnnotations as SupportsCloneAnnotations
from ..sql.base import ColumnCollection as ColumnCollection, ReadOnlyColumnCollection as ReadOnlyColumnCollection
from ..sql.cache_key import HasCacheKey as HasCacheKey, MemoizedHasCacheKey as MemoizedHasCacheKey
from ..sql.elements import BindParameter as BindParameter, ColumnElement as ColumnElement, KeyedColumnElement as KeyedColumnElement
from ..sql.selectable import FromClause as FromClause, Select as Select, Selectable as Selectable, _ColumnsClauseElement
from ..sql.visitors import anon_map as anon_map
from ..util.langhelpers import MemoizedSlots as MemoizedSlots
from ..util.typing import ArgsTypeProcotol as ArgsTypeProcotol, Literal as Literal, Protocol as Protocol, _AnnotationScanType, is_origin_of_cls as is_origin_of_cls, typing_get_origin as typing_get_origin
from ._typing import _EntityType, _IdentityKeyType, _InternalEntityType, _O, insp_is_aliased_class as insp_is_aliased_class, insp_is_mapper as insp_is_mapper, prop_is_relationship as prop_is_relationship
from .base import DynamicMapped as DynamicMapped, InspectionAttr as InspectionAttr, Mapped as Mapped, ORMDescriptor as ORMDescriptor, WriteOnlyMapped as WriteOnlyMapped, opt_manager_of_class as opt_manager_of_class
from .context import ORMCompileState as ORMCompileState, _MapperEntity
from .interfaces import CriteriaOption as CriteriaOption, ORMColumnsClauseRole as ORMColumnsClauseRole, ORMEntityColumnsClauseRole as ORMEntityColumnsClauseRole, ORMFromClauseRole as ORMFromClauseRole
from .mapper import Mapper as Mapper
from .path_registry import AbstractEntityRegistry as AbstractEntityRegistry
from .query import Query as Query
from .relationships import RelationshipProperty as RelationshipProperty
from _typeshed import Incomplete
from typing import AbstractSet, Any, Callable, Dict, FrozenSet, Generic, Iterable, List, Sequence, Tuple, Type

all_cascades: Incomplete

class _DeStringifyAnnotation(Protocol):
    def __call__(self, cls: Type[Any], annotation: _AnnotationScanType, originating_module: str, *, str_cleanup_fn: Callable[[str, str], str] | None = None, include_generic: bool = False) -> Type[Any]: ...

de_stringify_annotation: Incomplete

class _DeStringifyUnionElements(Protocol):
    def __call__(self, cls: Type[Any], annotation: ArgsTypeProcotol, originating_module: str, *, str_cleanup_fn: Callable[[str, str], str] | None = None) -> Type[Any]: ...

de_stringify_union_elements: Incomplete

class _EvalNameOnly(Protocol):
    def __call__(self, name: str, module_name: str) -> Any: ...

eval_name_only: Incomplete

class CascadeOptions(FrozenSet[str]):
    """Keeps track of the options sent to
    :paramref:`.relationship.cascade`"""
    save_update: bool
    delete: bool
    refresh_expire: bool
    merge: bool
    expunge: bool
    delete_orphan: bool
    def __new__(cls, value_list: Iterable[str] | str | None) -> CascadeOptions: ...
    @classmethod
    def from_string(cls, arg): ...

def polymorphic_union(table_map, typecolname, aliasname: str = 'p_union', cast_nulls: bool = True):
    '''Create a ``UNION`` statement used by a polymorphic mapper.

    See  :ref:`concrete_inheritance` for an example of how
    this is used.

    :param table_map: mapping of polymorphic identities to
     :class:`_schema.Table` objects.
    :param typecolname: string name of a "discriminator" column, which will be
     derived from the query, producing the polymorphic identity for
     each row.  If ``None``, no polymorphic discriminator is generated.
    :param aliasname: name of the :func:`~sqlalchemy.sql.expression.alias()`
     construct generated.
    :param cast_nulls: if True, non-existent columns, which are represented
     as labeled NULLs, will be passed into CAST.   This is a legacy behavior
     that is problematic on some backends such as Oracle - in which case it
     can be set to False.

    '''
def identity_key(class_: Type[_T] | None = None, ident: Any | Tuple[Any, ...] = None, *, instance: _T | None = None, row: Row[Any] | RowMapping | None = None, identity_token: Any | None = None) -> _IdentityKeyType[_T]:
    '''Generate "identity key" tuples, as are used as keys in the
    :attr:`.Session.identity_map` dictionary.

    This function has several call styles:

    * ``identity_key(class, ident, identity_token=token)``

      This form receives a mapped class and a primary key scalar or
      tuple as an argument.

      E.g.::

        >>> identity_key(MyClass, (1, 2))
        (<class \'__main__.MyClass\'>, (1, 2), None)

      :param class: mapped class (must be a positional argument)
      :param ident: primary key, may be a scalar or tuple argument.
      :param identity_token: optional identity token

        .. versionadded:: 1.2 added identity_token


    * ``identity_key(instance=instance)``

      This form will produce the identity key for a given instance.  The
      instance need not be persistent, only that its primary key attributes
      are populated (else the key will contain ``None`` for those missing
      values).

      E.g.::

        >>> instance = MyClass(1, 2)
        >>> identity_key(instance=instance)
        (<class \'__main__.MyClass\'>, (1, 2), None)

      In this form, the given instance is ultimately run though
      :meth:`_orm.Mapper.identity_key_from_instance`, which will have the
      effect of performing a database check for the corresponding row
      if the object is expired.

      :param instance: object instance (must be given as a keyword arg)

    * ``identity_key(class, row=row, identity_token=token)``

      This form is similar to the class/tuple form, except is passed a
      database result row as a :class:`.Row` or :class:`.RowMapping` object.

      E.g.::

        >>> row = engine.execute(\\\n            text("select * from table where a=1 and b=2")\\\n            ).first()
        >>> identity_key(MyClass, row=row)
        (<class \'__main__.MyClass\'>, (1, 2), None)

      :param class: mapped class (must be a positional argument)
      :param row: :class:`.Row` row returned by a :class:`_engine.CursorResult`
       (must be given as a keyword arg)
      :param identity_token: optional identity token

        .. versionadded:: 1.2 added identity_token

    '''

class _TraceAdaptRole(enum.Enum):
    '''Enumeration of all the use cases for ORMAdapter.

    ORMAdapter remains one of the most complicated aspects of the ORM, as it is
    used for in-place adaption of column expressions to be applied to a SELECT,
    replacing :class:`.Table` and other objects that are mapped to classes with
    aliases of those tables in the case of joined eager loading, or in the case
    of polymorphic loading as used with concrete mappings or other custom "with
    polymorphic" parameters, with whole user-defined subqueries. The
    enumerations provide an overview of all the use cases used by ORMAdapter, a
    layer of formality as to the introduction of new ORMAdapter use cases (of
    which none are anticipated), as well as a means to trace the origins of a
    particular ORMAdapter within runtime debugging.

    SQLAlchemy 2.0 has greatly scaled back ORM features which relied heavily on
    open-ended statement adaption, including the ``Query.with_polymorphic()``
    method and the ``Query.select_from_entity()`` methods, favoring
    user-explicit aliasing schemes using the ``aliased()`` and
    ``with_polymorphic()`` standalone constructs; these still use adaption,
    however the adaption is applied in a narrower scope.

    '''
    ALIASED_INSP: Incomplete
    JOINEDLOAD_USER_DEFINED_ALIAS: Incomplete
    JOINEDLOAD_PATH_WITH_POLYMORPHIC: Incomplete
    JOINEDLOAD_MEMOIZED_ADAPTER: Incomplete
    MAPPER_POLYMORPHIC_ADAPTER: Incomplete
    WITH_POLYMORPHIC_ADAPTER: Incomplete
    WITH_POLYMORPHIC_ADAPTER_RIGHT_JOIN: Incomplete
    DEPRECATED_JOIN_ADAPT_RIGHT_SIDE: Incomplete
    ADAPT_FROM_STATEMENT: Incomplete
    COMPOUND_EAGER_STATEMENT: Incomplete
    LEGACY_SELECT_FROM_ALIAS: Incomplete

class ORMStatementAdapter(sql_util.ColumnAdapter):
    """ColumnAdapter which includes a role attribute."""
    role: Incomplete
    def __init__(self, role: _TraceAdaptRole, selectable: Selectable, *, equivalents: _EquivalentColumnMap | None = None, adapt_required: bool = False, allow_label_resolve: bool = True, anonymize_labels: bool = False, adapt_on_names: bool = False, adapt_from_selectables: AbstractSet[FromClause] | None = None) -> None: ...

class ORMAdapter(sql_util.ColumnAdapter):
    """ColumnAdapter subclass which excludes adaptation of entities from
    non-matching mappers.

    """
    is_aliased_class: bool
    aliased_insp: AliasedInsp[Any] | None
    role: Incomplete
    mapper: Incomplete
    def __init__(self, role: _TraceAdaptRole, entity: _InternalEntityType[Any], *, equivalents: _EquivalentColumnMap | None = None, adapt_required: bool = False, allow_label_resolve: bool = True, anonymize_labels: bool = False, selectable: Selectable | None = None, limit_on_entity: bool = True, adapt_on_names: bool = False, adapt_from_selectables: AbstractSet[FromClause] | None = None) -> None: ...

class AliasedClass(inspection.Inspectable['AliasedInsp[_O]'], ORMColumnsClauseRole[_O]):
    '''Represents an "aliased" form of a mapped class for usage with Query.

    The ORM equivalent of a :func:`~sqlalchemy.sql.expression.alias`
    construct, this object mimics the mapped class using a
    ``__getattr__`` scheme and maintains a reference to a
    real :class:`~sqlalchemy.sql.expression.Alias` object.

    A primary purpose of :class:`.AliasedClass` is to serve as an alternate
    within a SQL statement generated by the ORM, such that an existing
    mapped entity can be used in multiple contexts.   A simple example::

        # find all pairs of users with the same name
        user_alias = aliased(User)
        session.query(User, user_alias).\\\n                        join((user_alias, User.id > user_alias.id)).\\\n                        filter(User.name == user_alias.name)

    :class:`.AliasedClass` is also capable of mapping an existing mapped
    class to an entirely new selectable, provided this selectable is column-
    compatible with the existing mapped selectable, and it can also be
    configured in a mapping as the target of a :func:`_orm.relationship`.
    See the links below for examples.

    The :class:`.AliasedClass` object is constructed typically using the
    :func:`_orm.aliased` function.   It also is produced with additional
    configuration when using the :func:`_orm.with_polymorphic` function.

    The resulting object is an instance of :class:`.AliasedClass`.
    This object implements an attribute scheme which produces the
    same attribute and method interface as the original mapped
    class, allowing :class:`.AliasedClass` to be compatible
    with any attribute technique which works on the original class,
    including hybrid attributes (see :ref:`hybrids_toplevel`).

    The :class:`.AliasedClass` can be inspected for its underlying
    :class:`_orm.Mapper`, aliased selectable, and other information
    using :func:`_sa.inspect`::

        from sqlalchemy import inspect
        my_alias = aliased(MyClass)
        insp = inspect(my_alias)

    The resulting inspection object is an instance of :class:`.AliasedInsp`.


    .. seealso::

        :func:`.aliased`

        :func:`.with_polymorphic`

        :ref:`relationship_aliased_class`

        :ref:`relationship_to_window_function`


    '''
    def __init__(self, mapped_class_or_ac: _EntityType[_O], alias: FromClause | None = None, name: str | None = None, flat: bool = False, adapt_on_names: bool = False, with_polymorphic_mappers: Sequence[Mapper[Any]] | None = None, with_polymorphic_discriminator: ColumnElement[Any] | None = None, base_alias: AliasedInsp[Any] | None = None, use_mapper_path: bool = False, represents_outer_join: bool = False) -> None: ...
    def __getattr__(self, key: str) -> Any: ...

class AliasedInsp(ORMEntityColumnsClauseRole[_O], ORMFromClauseRole, HasCacheKey, InspectionAttr, MemoizedSlots, inspection.Inspectable['AliasedInsp[_O]'], Generic[_O]):
    '''Provide an inspection interface for an
    :class:`.AliasedClass` object.

    The :class:`.AliasedInsp` object is returned
    given an :class:`.AliasedClass` using the
    :func:`_sa.inspect` function::

        from sqlalchemy import inspect
        from sqlalchemy.orm import aliased

        my_alias = aliased(MyMappedClass)
        insp = inspect(my_alias)

    Attributes on :class:`.AliasedInsp`
    include:

    * ``entity`` - the :class:`.AliasedClass` represented.
    * ``mapper`` - the :class:`_orm.Mapper` mapping the underlying class.
    * ``selectable`` - the :class:`_expression.Alias`
      construct which ultimately
      represents an aliased :class:`_schema.Table` or
      :class:`_expression.Select`
      construct.
    * ``name`` - the name of the alias.  Also is used as the attribute
      name when returned in a result tuple from :class:`_query.Query`.
    * ``with_polymorphic_mappers`` - collection of :class:`_orm.Mapper`
      objects
      indicating all those mappers expressed in the select construct
      for the :class:`.AliasedClass`.
    * ``polymorphic_on`` - an alternate column or SQL expression which
      will be used as the "discriminator" for a polymorphic load.

    .. seealso::

        :ref:`inspection_toplevel`

    '''
    mapper: Mapper[_O]
    selectable: FromClause
    with_polymorphic_mappers: Sequence[Mapper[Any]]
    name: Incomplete
    polymorphic_on: Incomplete
    represents_outer_join: Incomplete
    def __init__(self, entity: AliasedClass[_O], inspected: _InternalEntityType[_O], selectable: FromClause, name: str | None, with_polymorphic_mappers: Sequence[Mapper[Any]] | None, polymorphic_on: ColumnElement[Any] | None, _base_alias: AliasedInsp[Any] | None, _use_mapper_path: bool, adapt_on_names: bool, represents_outer_join: bool, nest_adapters: bool) -> None: ...
    @property
    def entity(self) -> AliasedClass[_O]: ...
    is_aliased_class: bool
    @property
    def entity_namespace(self) -> AliasedClass[_O]: ...
    @property
    def class_(self) -> Type[_O]:
        """Return the mapped class ultimately represented by this
        :class:`.AliasedInsp`."""

class _WrapUserEntity:
    """A wrapper used within the loader_criteria lambda caller so that
    we can bypass declared_attr descriptors on unmapped mixins, which
    normally emit a warning for such use.

    might also be useful for other per-lambda instrumentations should
    the need arise.

    """
    subject: Incomplete
    def __init__(self, subject) -> None: ...
    def __getattribute__(self, name): ...

class LoaderCriteriaOption(CriteriaOption):
    """Add additional WHERE criteria to the load for all occurrences of
    a particular entity.

    :class:`_orm.LoaderCriteriaOption` is invoked using the
    :func:`_orm.with_loader_criteria` function; see that function for
    details.

    .. versionadded:: 1.4

    """
    root_entity: Type[Any] | None
    entity: _InternalEntityType[Any] | None
    where_criteria: ColumnElement[bool] | lambdas.DeferredLambdaElement
    deferred_where_criteria: bool
    include_aliases: bool
    propagate_to_loaders: bool
    def __init__(self, entity_or_base: _EntityType[Any], where_criteria: _ColumnExpressionArgument[bool], loader_only: bool = False, include_aliases: bool = False, propagate_to_loaders: bool = True, track_closure_variables: bool = True) -> None: ...
    def __reduce__(self): ...
    def process_compile_state_replaced_entities(self, compile_state: ORMCompileState, mapper_entities: Iterable[_MapperEntity]) -> None: ...
    def process_compile_state(self, compile_state: ORMCompileState) -> None:
        """Apply a modification to a given :class:`.CompileState`."""
    def get_global_criteria(self, attributes: Dict[Any, Any]) -> None: ...

GenericAlias: Incomplete

class Bundle(ORMColumnsClauseRole[_T], SupportsCloneAnnotations, MemoizedHasCacheKey, inspection.Inspectable['Bundle[_T]'], InspectionAttr):
    """A grouping of SQL expressions that are returned by a :class:`.Query`
    under one namespace.

    The :class:`.Bundle` essentially allows nesting of the tuple-based
    results returned by a column-oriented :class:`_query.Query` object.
    It also
    is extensible via simple subclassing, where the primary capability
    to override is that of how the set of expressions should be returned,
    allowing post-processing as well as custom return types, without
    involving ORM identity-mapped classes.

    .. seealso::

        :ref:`bundles`


    """
    single_entity: bool
    is_clause_element: bool
    is_mapper: bool
    is_aliased_class: bool
    is_bundle: bool
    proxy_set: Incomplete
    exprs: List[_ColumnsClauseElement]
    name: Incomplete
    c: Incomplete
    def __init__(self, name: str, *exprs: _ColumnExpressionArgument[Any], **kw: Any) -> None:
        '''Construct a new :class:`.Bundle`.

        e.g.::

            bn = Bundle("mybundle", MyClass.x, MyClass.y)

            for row in session.query(bn).filter(
                    bn.c.x == 5).filter(bn.c.y == 4):
                print(row.mybundle.x, row.mybundle.y)

        :param name: name of the bundle.
        :param \\*exprs: columns or SQL expressions comprising the bundle.
        :param single_entity=False: if True, rows for this :class:`.Bundle`
         can be returned as a "single entity" outside of any enclosing tuple
         in the same manner as a mapped entity.

        '''
    @property
    def mapper(self) -> Mapper[Any] | None: ...
    @property
    def entity(self) -> _InternalEntityType[Any] | None: ...
    @property
    def entity_namespace(self) -> ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]: ...
    columns: ReadOnlyColumnCollection[str, KeyedColumnElement[Any]]
    def __clause_element__(self): ...
    @property
    def clauses(self): ...
    def label(self, name):
        """Provide a copy of this :class:`.Bundle` passing a new label."""
    def create_row_processor(self, query: Select[Any], procs: Sequence[Callable[[Row[Any]], Any]], labels: Sequence[str]) -> Callable[[Row[Any]], Any]:
        '''Produce the "row processing" function for this :class:`.Bundle`.

        May be overridden by subclasses to provide custom behaviors when
        results are fetched. The method is passed the statement object and a
        set of "row processor" functions at query execution time; these
        processor functions when given a result row will return the individual
        attribute value, which can then be adapted into any kind of return data
        structure.

        The example below illustrates replacing the usual :class:`.Row`
        return structure with a straight Python dictionary::

            from sqlalchemy.orm import Bundle

            class DictBundle(Bundle):
                def create_row_processor(self, query, procs, labels):
                    \'Override create_row_processor to return values as
                    dictionaries\'

                    def proc(row):
                        return dict(
                            zip(labels, (proc(row) for proc in procs))
                        )
                    return proc

        A result from the above :class:`_orm.Bundle` will return dictionary
        values::

            bn = DictBundle(\'mybundle\', MyClass.data1, MyClass.data2)
            for row in session.execute(select(bn)).where(bn.c.data1 == \'d1\'):
                print(row.mybundle[\'data1\'], row.mybundle[\'data2\'])

        '''

class _ORMJoin(expression.Join):
    """Extend Join to support ORM constructs as input."""
    __visit_name__: Incomplete
    inherit_cache: bool
    onclause: Incomplete
    def __init__(self, left: _FromClauseArgument, right: _FromClauseArgument, onclause: _OnClauseArgument | None = None, isouter: bool = False, full: bool = False, _left_memo: Any | None = None, _right_memo: Any | None = None, _extra_criteria: Tuple[ColumnElement[bool], ...] = ()) -> None: ...
    def join(self, right: _FromClauseArgument, onclause: _OnClauseArgument | None = None, isouter: bool = False, full: bool = False) -> _ORMJoin: ...
    def outerjoin(self, right: _FromClauseArgument, onclause: _OnClauseArgument | None = None, full: bool = False) -> _ORMJoin: ...

def with_parent(instance: object, prop: attributes.QueryableAttribute[Any], from_entity: _EntityType[Any] | None = None) -> ColumnElement[bool]:
    '''Create filtering criterion that relates this query\'s primary entity
    to the given related instance, using established
    :func:`_orm.relationship()`
    configuration.

    E.g.::

        stmt = select(Address).where(with_parent(some_user, User.addresses))


    The SQL rendered is the same as that rendered when a lazy loader
    would fire off from the given parent on that attribute, meaning
    that the appropriate state is taken from the parent object in
    Python without the need to render joins to the parent table
    in the rendered statement.

    The given property may also make use of :meth:`_orm.PropComparator.of_type`
    to indicate the left side of the criteria::


        a1 = aliased(Address)
        a2 = aliased(Address)
        stmt = select(a1, a2).where(
            with_parent(u1, User.addresses.of_type(a2))
        )

    The above use is equivalent to using the
    :func:`_orm.with_parent.from_entity` argument::

        a1 = aliased(Address)
        a2 = aliased(Address)
        stmt = select(a1, a2).where(
            with_parent(u1, User.addresses, from_entity=a2)
        )

    :param instance:
      An instance which has some :func:`_orm.relationship`.

    :param property:
      Class-bound attribute, which indicates
      what relationship from the instance should be used to reconcile the
      parent/child relationship.

    :param from_entity:
      Entity in which to consider as the left side.  This defaults to the
      "zero" entity of the :class:`_query.Query` itself.

      .. versionadded:: 1.2

    '''
def has_identity(object_: object) -> bool:
    """Return True if the given object has a database
    identity.

    This typically corresponds to the object being
    in either the persistent or detached state.

    .. seealso::

        :func:`.was_deleted`

    """
def was_deleted(object_: object) -> bool:
    """Return True if the given object was deleted
    within a session flush.

    This is regardless of whether or not the object is
    persistent or detached.

    .. seealso::

        :attr:`.InstanceState.was_deleted`

    """

class _CleanupError(Exception): ...
