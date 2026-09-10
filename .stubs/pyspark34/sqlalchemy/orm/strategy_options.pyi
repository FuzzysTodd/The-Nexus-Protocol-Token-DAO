from .. import inspect as inspect, util as util
from ..sql import and_ as and_, cache_key as cache_key, coercions as coercions, roles as roles, traversals as traversals, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument, _FromClauseArgument
from ..sql.cache_key import CacheKey as CacheKey, _CacheKeyTraversalType
from ..util.typing import Final as Final, Literal as Literal, Self as Self
from ._typing import _EntityType, _InternalEntityType, insp_is_aliased_class as insp_is_aliased_class, insp_is_attribute as insp_is_attribute, insp_is_mapper as insp_is_mapper, insp_is_mapper_property as insp_is_mapper_property
from .attributes import QueryableAttribute as QueryableAttribute
from .base import InspectionAttr as InspectionAttr
from .context import ORMCompileState as ORMCompileState, QueryContext as QueryContext, _MapperEntity
from .interfaces import LoaderOption as LoaderOption, MapperProperty as MapperProperty, ORMOption as ORMOption, _StrategyKey
from .mapper import Mapper as Mapper
from .path_registry import AbstractEntityRegistry as AbstractEntityRegistry, PathRegistry as PathRegistry, TokenRegistry as TokenRegistry, _StrPathToken, path_is_property as path_is_property
from .util import AliasedInsp as AliasedInsp
from typing import Any, Iterable, Sequence, Tuple, Type

class _AbstractLoad(traversals.GenerativeOnTraversal, LoaderOption):
    propagate_to_loaders: bool
    def contains_eager(self, attr: _AttrType, alias: _FromClauseArgument | None = None, _is_chain: bool = False) -> Self:
        """Indicate that the given attribute should be eagerly loaded from
        columns stated manually in the query.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        The option is used in conjunction with an explicit join that loads
        the desired rows, i.e.::

            sess.query(Order).\\\n                    join(Order.user).\\\n                    options(contains_eager(Order.user))

        The above query would join from the ``Order`` entity to its related
        ``User`` entity, and the returned ``Order`` objects would have the
        ``Order.user`` attribute pre-populated.

        It may also be used for customizing the entries in an eagerly loaded
        collection; queries will normally want to use the
        :ref:`orm_queryguide_populate_existing` execution option assuming the
        primary collection of parent objects may already have been loaded::

            sess.query(User).\\\n                join(User.addresses).\\\n                filter(Address.email_address.like('%@aol.com')).\\\n                options(contains_eager(User.addresses)).\\\n                populate_existing()

        See the section :ref:`contains_eager` for complete usage details.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`contains_eager`

        """
    def load_only(self, *attrs: _AttrType, raiseload: bool = False) -> Self:
        """Indicate that for a particular entity, only the given list
        of column-based attribute names should be loaded; all others will be
        deferred.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        Example - given a class ``User``, load only the ``name`` and
        ``fullname`` attributes::

            session.query(User).options(load_only(User.name, User.fullname))

        Example - given a relationship ``User.addresses -> Address``, specify
        subquery loading for the ``User.addresses`` collection, but on each
        ``Address`` object load only the ``email_address`` attribute::

            session.query(User).options(
                subqueryload(User.addresses).load_only(Address.email_address)
            )

        For a statement that has multiple entities,
        the lead entity can be
        specifically referred to using the :class:`_orm.Load` constructor::

            stmt = select(User, Address).join(User.addresses).options(
                        Load(User).load_only(User.name, User.fullname),
                        Load(Address).load_only(Address.email_address)
                    )

        :param \\*attrs: Attributes to be loaded, all others will be deferred.

        :param raiseload: raise :class:`.InvalidRequestError` rather than
         lazy loading a value when a deferred attribute is accessed. Used
         to prevent unwanted SQL from being emitted.

         .. versionadded:: 2.0

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

        :param \\*attrs: Attributes to be loaded, all others will be deferred.

        :param raiseload: raise :class:`.InvalidRequestError` rather than
         lazy loading a value when a deferred attribute is accessed. Used
         to prevent unwanted SQL from being emitted.

         .. versionadded:: 2.0

        """
    def joinedload(self, attr: _AttrType, innerjoin: bool | None = None) -> Self:
        '''Indicate that the given attribute should be loaded using joined
        eager loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        examples::

            # joined-load the "orders" collection on "User"
            query(User).options(joinedload(User.orders))

            # joined-load Order.items and then Item.keywords
            query(Order).options(
                joinedload(Order.items).joinedload(Item.keywords))

            # lazily load Order.items, but when Items are loaded,
            # joined-load the keywords collection
            query(Order).options(
                lazyload(Order.items).joinedload(Item.keywords))

        :param innerjoin: if ``True``, indicates that the joined eager load
         should use an inner join instead of the default of left outer join::

            query(Order).options(joinedload(Order.user, innerjoin=True))

        In order to chain multiple eager joins together where some may be
        OUTER and others INNER, right-nested joins are used to link them::

            query(A).options(
                joinedload(A.bs, innerjoin=False).
                    joinedload(B.cs, innerjoin=True)
            )

        The above query, linking A.bs via "outer" join and B.cs via "inner"
        join would render the joins as "a LEFT OUTER JOIN (b JOIN c)". When
        using older versions of SQLite (< 3.7.16), this form of JOIN is
        translated to use full subqueries as this syntax is otherwise not
        directly supported.

        The ``innerjoin`` flag can also be stated with the term ``"unnested"``.
        This indicates that an INNER JOIN should be used, *unless* the join
        is linked to a LEFT OUTER JOIN to the left, in which case it
        will render as LEFT OUTER JOIN.  For example, supposing ``A.bs``
        is an outerjoin::

            query(A).options(
                joinedload(A.bs).
                    joinedload(B.cs, innerjoin="unnested")
            )

        The above join will render as "a LEFT OUTER JOIN b LEFT OUTER JOIN c",
        rather than as "a LEFT OUTER JOIN (b JOIN c)".

        .. note:: The "unnested" flag does **not** affect the JOIN rendered
            from a many-to-many association table, e.g. a table configured as
            :paramref:`_orm.relationship.secondary`, to the target table; for
            correctness of results, these joins are always INNER and are
            therefore right-nested if linked to an OUTER join.

        .. note::

            The joins produced by :func:`_orm.joinedload` are **anonymously
            aliased**. The criteria by which the join proceeds cannot be
            modified, nor can the ORM-enabled :class:`_sql.Select` or legacy
            :class:`_query.Query` refer to these joins in any way, including
            ordering. See :ref:`zen_of_eager_loading` for further detail.

            To produce a specific SQL JOIN which is explicitly available, use
            :meth:`_sql.Select.join` and :meth:`_query.Query.join`. To combine
            explicit JOINs with eager loading of collections, use
            :func:`_orm.contains_eager`; see :ref:`contains_eager`.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`joined_eager_loading`

        '''
    def subqueryload(self, attr: _AttrType) -> Self:
        '''Indicate that the given attribute should be loaded using
        subquery eager loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        examples::

            # subquery-load the "orders" collection on "User"
            query(User).options(subqueryload(User.orders))

            # subquery-load Order.items and then Item.keywords
            query(Order).options(
                subqueryload(Order.items).subqueryload(Item.keywords))

            # lazily load Order.items, but when Items are loaded,
            # subquery-load the keywords collection
            query(Order).options(
                lazyload(Order.items).subqueryload(Item.keywords))


        .. seealso::

            :ref:`loading_toplevel`

            :ref:`subquery_eager_loading`

        '''
    def selectinload(self, attr: _AttrType, recursion_depth: int | None = None) -> Self:
        '''Indicate that the given attribute should be loaded using
        SELECT IN eager loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        examples::

            # selectin-load the "orders" collection on "User"
            query(User).options(selectinload(User.orders))

            # selectin-load Order.items and then Item.keywords
            query(Order).options(
                selectinload(Order.items).selectinload(Item.keywords))

            # lazily load Order.items, but when Items are loaded,
            # selectin-load the keywords collection
            query(Order).options(
                lazyload(Order.items).selectinload(Item.keywords))

        :param recursion_depth: optional int; when set to a positive integer
         in conjunction with a self-referential relationship,
         indicates "selectin" loading will continue that many levels deep
         automatically until no items are found.

         .. note:: The :paramref:`_orm.selectinload.recursion_depth` option
            currently supports only self-referential relationships.  There
            is not yet an option to automatically traverse recursive structures
            with more than one relationship involved.

            Additionally, the :paramref:`_orm.selectinload.recursion_depth`
            parameter is new and experimental and should be treated as "alpha"
            status for the 2.0 series.

         .. versionadded:: 2.0 added
            :paramref:`_orm.selectinload.recursion_depth`


        .. seealso::

            :ref:`loading_toplevel`

            :ref:`selectin_eager_loading`

        '''
    def lazyload(self, attr: _AttrType) -> Self:
        '''Indicate that the given attribute should be loaded using "lazy"
        loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`lazy_loading`

        '''
    def immediateload(self, attr: _AttrType, recursion_depth: int | None = None) -> Self:
        '''Indicate that the given attribute should be loaded using
        an immediate load with a per-attribute SELECT statement.

        The load is achieved using the "lazyloader" strategy and does not
        fire off any additional eager loaders.

        The :func:`.immediateload` option is superseded in general
        by the :func:`.selectinload` option, which performs the same task
        more efficiently by emitting a SELECT for all loaded objects.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        :param recursion_depth: optional int; when set to a positive integer
         in conjunction with a self-referential relationship,
         indicates "selectin" loading will continue that many levels deep
         automatically until no items are found.

         .. note:: The :paramref:`_orm.immediateload.recursion_depth` option
            currently supports only self-referential relationships.  There
            is not yet an option to automatically traverse recursive structures
            with more than one relationship involved.

         .. warning:: This parameter is new and experimental and should be
            treated as "alpha" status

         .. versionadded:: 2.0 added
            :paramref:`_orm.immediateload.recursion_depth`


        .. seealso::

            :ref:`loading_toplevel`

            :ref:`selectin_eager_loading`

        '''
    def noload(self, attr: _AttrType) -> Self:
        """Indicate that the given relationship attribute should remain
        unloaded.

        The relationship attribute will return ``None`` when accessed without
        producing any loading effect.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        :func:`_orm.noload` applies to :func:`_orm.relationship` attributes
        only.

        .. note:: Setting this loading strategy as the default strategy
            for a relationship using the :paramref:`.orm.relationship.lazy`
            parameter may cause issues with flushes, such if a delete operation
            needs to load related objects and instead ``None`` was returned.

        .. seealso::

            :ref:`loading_toplevel`

        """
    def raiseload(self, attr: _AttrType, sql_only: bool = False) -> Self:
        """Indicate that the given attribute should raise an error if accessed.

        A relationship attribute configured with :func:`_orm.raiseload` will
        raise an :exc:`~sqlalchemy.exc.InvalidRequestError` upon access. The
        typical way this is useful is when an application is attempting to
        ensure that all relationship attributes that are accessed in a
        particular context would have been already loaded via eager loading.
        Instead of having to read through SQL logs to ensure lazy loads aren't
        occurring, this strategy will cause them to raise immediately.

        :func:`_orm.raiseload` applies to :func:`_orm.relationship` attributes
        only. In order to apply raise-on-SQL behavior to a column-based
        attribute, use the :paramref:`.orm.defer.raiseload` parameter on the
        :func:`.defer` loader option.

        :param sql_only: if True, raise only if the lazy load would emit SQL,
         but not if it is only checking the identity map, or determining that
         the related value should just be None due to missing keys. When False,
         the strategy will raise for all varieties of relationship loading.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        .. seealso::

            :ref:`loading_toplevel`

            :ref:`prevent_lazy_with_raiseload`

            :ref:`orm_queryguide_deferred_raiseload`

        """
    def defaultload(self, attr: _AttrType) -> Self:
        '''Indicate an attribute should load using its predefined loader style.

        The behavior of this loading option is to not change the current
        loading style of the attribute, meaning that the previously configured
        one is used or, if no previous style was selected, the default
        loading will be used.

        This method is used to link to other loader options further into
        a chain of attributes without altering the loader style of the links
        along the chain.  For example, to set joined eager loading for an
        element of an element::

            session.query(MyClass).options(
                defaultload(MyClass.someattribute).
                joinedload(MyOtherClass.someotherattribute)
            )

        :func:`.defaultload` is also useful for setting column-level options on
        a related class, namely that of :func:`.defer` and :func:`.undefer`::

            session.query(MyClass).options(
                defaultload(MyClass.someattribute).
                defer("some_column").
                undefer("some_other_column")
            )

        .. seealso::

            :ref:`orm_queryguide_relationship_sub_options`

            :meth:`_orm.Load.options`

        '''
    def defer(self, key: _AttrType, raiseload: bool = False) -> Self:
        """Indicate that the given column-oriented attribute should be
        deferred, e.g. not loaded until accessed.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        e.g.::

            from sqlalchemy.orm import defer

            session.query(MyClass).options(
                defer(MyClass.attribute_one),
                defer(MyClass.attribute_two)
            )

        To specify a deferred load of an attribute on a related class,
        the path can be specified one token at a time, specifying the loading
        style for each link along the chain.  To leave the loading style
        for a link unchanged, use :func:`_orm.defaultload`::

            session.query(MyClass).options(
                defaultload(MyClass.someattr).defer(RelatedClass.some_column)
            )

        Multiple deferral options related to a relationship can be bundled
        at once using :meth:`_orm.Load.options`::


            session.query(MyClass).options(
                defaultload(MyClass.someattr).options(
                    defer(RelatedClass.some_column),
                    defer(RelatedClass.some_other_column),
                    defer(RelatedClass.another_column)
                )
            )

        :param key: Attribute to be deferred.

        :param raiseload: raise :class:`.InvalidRequestError` rather than
         lazy loading a value when the deferred attribute is accessed. Used
         to prevent unwanted SQL from being emitted.

        .. versionadded:: 1.4

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

            :func:`_orm.load_only`

            :func:`_orm.undefer`

        """
    def undefer(self, key: _AttrType) -> Self:
        '''Indicate that the given column-oriented attribute should be
        undeferred, e.g. specified within the SELECT statement of the entity
        as a whole.

        The column being undeferred is typically set up on the mapping as a
        :func:`.deferred` attribute.

        This function is part of the :class:`_orm.Load` interface and supports
        both method-chained and standalone operation.

        Examples::

            # undefer two columns
            session.query(MyClass).options(
                undefer(MyClass.col1), undefer(MyClass.col2)
            )

            # undefer all columns specific to a single class using Load + *
            session.query(MyClass, MyOtherClass).options(
                Load(MyClass).undefer("*"))

            # undefer a column on a related object
            session.query(MyClass).options(
                defaultload(MyClass.items).undefer(MyClass.text))

        :param key: Attribute to be undeferred.

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

            :func:`_orm.defer`

            :func:`_orm.undefer_group`

        '''
    def undefer_group(self, name: str) -> Self:
        '''Indicate that columns within the given deferred group name should be
        undeferred.

        The columns being undeferred are set up on the mapping as
        :func:`.deferred` attributes and include a "group" name.

        E.g::

            session.query(MyClass).options(undefer_group("large_attrs"))

        To undefer a group of attributes on a related entity, the path can be
        spelled out using relationship loader options, such as
        :func:`_orm.defaultload`::

            session.query(MyClass).options(
                defaultload("someattr").undefer_group("large_attrs"))

        .. seealso::

            :ref:`orm_queryguide_column_deferral` - in the
            :ref:`queryguide_toplevel`

            :func:`_orm.defer`

            :func:`_orm.undefer`

        '''
    def with_expression(self, key: _AttrType, expression: _ColumnExpressionArgument[Any]) -> Self:
        '''Apply an ad-hoc SQL expression to a "deferred expression"
        attribute.

        This option is used in conjunction with the
        :func:`_orm.query_expression` mapper-level construct that indicates an
        attribute which should be the target of an ad-hoc SQL expression.

        E.g.::

            stmt = select(SomeClass).options(
                with_expression(SomeClass.x_y_expr, SomeClass.x + SomeClass.y)
            )

        .. versionadded:: 1.2

        :param key: Attribute to be populated

        :param expr: SQL expression to be applied to the attribute.

        .. seealso::

            :ref:`orm_queryguide_with_expression` - background and usage
            examples

        '''
    def selectin_polymorphic(self, classes: Iterable[Type[Any]]) -> Self:
        '''Indicate an eager load should take place for all attributes
        specific to a subclass.

        This uses an additional SELECT with IN against all matched primary
        key values, and is the per-query analogue to the ``"selectin"``
        setting on the :paramref:`.mapper.polymorphic_load` parameter.

        .. versionadded:: 1.2

        .. seealso::

            :ref:`polymorphic_selectin`

        '''
    def options(self, *opts: _AbstractLoad) -> Self:
        """Apply a series of options as sub-options to this
        :class:`_orm._AbstractLoad` object.

        Implementation is provided by subclasses.

        """
    def process_compile_state_replaced_entities(self, compile_state: ORMCompileState, mapper_entities: Sequence[_MapperEntity]) -> None: ...
    def process_compile_state(self, compile_state: ORMCompileState) -> None: ...

class Load(_AbstractLoad):
    """Represents loader options which modify the state of a
    ORM-enabled :class:`_sql.Select` or a legacy :class:`_query.Query` in
    order to affect how various mapped attributes are loaded.

    The :class:`_orm.Load` object is in most cases used implicitly behind the
    scenes when one makes use of a query option like :func:`_orm.joinedload`,
    :func:`_orm.defer`, or similar.   It typically is not instantiated directly
    except for in some very specific cases.

    .. seealso::

        :ref:`orm_queryguide_relationship_per_entity_wildcard` - illustrates an
        example where direct use of :class:`_orm.Load` may be useful

    """
    path: PathRegistry
    context: Tuple[_LoadElement, ...]
    additional_source_entities: Tuple[_InternalEntityType[Any], ...]
    propagate_to_loaders: bool
    def __init__(self, entity: _EntityType[Any]) -> None: ...
    def options(self, *opts: _AbstractLoad) -> Self:
        """Apply a series of options as sub-options to this
        :class:`_orm.Load`
        object.

        E.g.::

            query = session.query(Author)
            query = query.options(
                        joinedload(Author.book).options(
                            load_only(Book.summary, Book.excerpt),
                            joinedload(Book.citations).options(
                                joinedload(Citation.author)
                            )
                        )
                    )

        :param \\*opts: A series of loader option objects (ultimately
         :class:`_orm.Load` objects) which should be applied to the path
         specified by this :class:`_orm.Load` object.

        .. versionadded:: 1.3.6

        .. seealso::

            :func:`.defaultload`

            :ref:`orm_queryguide_relationship_sub_options`

        """

class _WildcardLoad(_AbstractLoad):
    """represent a standalone '*' load operation"""
    cache_key_traversal: _CacheKeyTraversalType
    strategy: Tuple[Any, ...] | None
    local_opts: _OptsType
    path: Tuple | Tuple[str]
    propagate_to_loaders: bool
    def __init__(self) -> None: ...
    def options(self, *opts: _AbstractLoad) -> Self: ...

class _LoadElement(cache_key.HasCacheKey, traversals.HasShallowCopy, visitors.Traversible):
    """represents strategy information to select for a LoaderStrategy
    and pass options to it.

    :class:`._LoadElement` objects provide the inner datastructure
    stored by a :class:`_orm.Load` object and are also the object passed
    to methods like :meth:`.LoaderStrategy.setup_query`.

    .. versionadded:: 2.0

    """
    __visit_name__: str
    strategy: _StrategyKey | None
    path: PathRegistry
    propagate_to_loaders: bool
    local_opts: util.immutabledict[str, Any]
    is_token_strategy: bool
    is_class_strategy: bool
    def __hash__(self) -> int: ...
    def __eq__(self, other): ...
    @property
    def is_opts_only(self) -> bool: ...
    def process_compile_state(self, parent_loader, compile_state, mapper_entities, reconciled_lead_entity, raiseerr) -> None:
        """populate ORMCompileState.attributes with loader state for this
        _LoadElement.

        """
    @classmethod
    def create(cls, path: PathRegistry, attr: _AttrType | _StrPathToken | None, strategy: _StrategyKey | None, wildcard_key: _WildcardKeyType | None, local_opts: _OptsType | None, propagate_to_loaders: bool, raiseerr: bool = True, attr_group: _AttrGroupType | None = None, reconcile_to_other: bool | None = None) -> _LoadElement:
        """Create a new :class:`._LoadElement` object."""
    def __init__(self) -> None: ...

class _AttributeStrategyLoad(_LoadElement):
    """Loader strategies against specific relationship or column paths.

    e.g.::

        joinedload(User.addresses)
        defer(Order.name)
        selectinload(User.orders).lazyload(Order.items)

    """
    __visit_name__: str
    is_class_strategy: bool
    is_token_strategy: bool

class _TokenStrategyLoad(_LoadElement):
    """Loader strategies against wildcard attributes

    e.g.::

        raiseload('*')
        Load(User).lazyload('*')
        defer('*')
        load_only(User.name, User.email)  # will create a defer('*')
        joinedload(User.addresses).raiseload('*')

    """
    __visit_name__: str
    inherit_cache: bool
    is_class_strategy: bool
    is_token_strategy: bool

class _ClassStrategyLoad(_LoadElement):
    """Loader strategies that deals with a class as a target, not
    an attribute path

    e.g.::

        q = s.query(Person).options(
            selectin_polymorphic(Person, [Engineer, Manager])
        )

    """
    inherit_cache: bool
    is_class_strategy: bool
    is_token_strategy: bool
    __visit_name__: str

def loader_unbound_fn(fn: _FN) -> _FN:
    """decorator that applies docstrings between standalone loader functions
    and the loader methods on :class:`._AbstractLoad`.

    """
def contains_eager(*keys: _AttrType, **kw: Any) -> _AbstractLoad: ...
def load_only(*attrs: _AttrType, raiseload: bool = False) -> _AbstractLoad: ...
def joinedload(*keys: _AttrType, **kw: Any) -> _AbstractLoad: ...
def subqueryload(*keys: _AttrType) -> _AbstractLoad: ...
def selectinload(*keys: _AttrType, recursion_depth: int | None = None) -> _AbstractLoad: ...
def lazyload(*keys: _AttrType) -> _AbstractLoad: ...
def immediateload(*keys: _AttrType, recursion_depth: int | None = None) -> _AbstractLoad: ...
def noload(*keys: _AttrType) -> _AbstractLoad: ...
def raiseload(*keys: _AttrType, **kw: Any) -> _AbstractLoad: ...
def defaultload(*keys: _AttrType) -> _AbstractLoad: ...
def defer(key: _AttrType, *addl_attrs: _AttrType, raiseload: bool = False) -> _AbstractLoad: ...
def undefer(key: _AttrType, *addl_attrs: _AttrType) -> _AbstractLoad: ...
def undefer_group(name: str) -> _AbstractLoad: ...
def with_expression(key: _AttrType, expression: _ColumnExpressionArgument[Any]) -> _AbstractLoad: ...
def selectin_polymorphic(base_cls: _EntityType[Any], classes: Iterable[Type[Any]]) -> _AbstractLoad: ...
