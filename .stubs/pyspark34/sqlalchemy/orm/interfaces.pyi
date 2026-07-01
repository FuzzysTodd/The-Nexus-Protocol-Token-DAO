from . import path_registry as path_registry
from .. import ColumnElement as ColumnElement, inspection as inspection, util as util
from ..engine.result import Result as Result
from ..sql import operators as operators, roles as roles, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument, _ColumnsClauseArgument, _InfoType
from ..sql.base import ExecutableOption as ExecutableOption, _NoArg
from ..sql.cache_key import HasCacheKey as HasCacheKey
from ..sql.operators import ColumnOperators as ColumnOperators, OperatorType as OperatorType
from ..sql.schema import Column as Column
from ..sql.type_api import TypeEngine as TypeEngine
from ..util import warn_deprecated as warn_deprecated
from ..util.typing import RODescriptorReference as RODescriptorReference, TypedDict as TypedDict, _AnnotationScanType
from ._typing import _EntityType, _IdentityKeyType, _InstanceDict, _InternalEntityType, _ORMAdapterProto
from .attributes import InstrumentedAttribute as InstrumentedAttribute
from .base import InspectionAttrInfo as InspectionAttrInfo, Mapped as Mapped, SQLORMOperations as SQLORMOperations, _MappedAttribute as _MappedAttribute
from .context import ORMCompileState as ORMCompileState, QueryContext as QueryContext, _MapperEntity
from .decl_api import RegistryType as RegistryType
from .decl_base import _ClassScanMapperConfig
from .loading import _PopulatorDict
from .mapper import Mapper as Mapper
from .path_registry import AbstractEntityRegistry as AbstractEntityRegistry
from .query import Query as Query
from .session import Session as Session
from .state import InstanceState as InstanceState
from .strategy_options import _LoadElement
from .util import AliasedInsp as AliasedInsp, ORMAdapter as ORMAdapter
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, Dict, Generic, Iterator, List, NamedTuple, Sequence, Set, Tuple, Type

class ORMStatementRole(roles.StatementRole): ...
class ORMColumnsClauseRole(roles.ColumnsClauseRole, roles.TypedColumnsClauseRole[_T]): ...
class ORMEntityColumnsClauseRole(ORMColumnsClauseRole[_T]): ...
class ORMFromClauseRole(roles.StrictFromClauseRole): ...

class ORMColumnDescription(TypedDict):
    name: str
    type: Type[Any] | TypeEngine[Any]
    aliased: bool
    expr: _ColumnsClauseArgument[Any]
    entity: _ColumnsClauseArgument[Any] | None

class _IntrospectsAnnotations:
    def found_in_pep593_annotated(self) -> Any:
        """return a copy of this object to use in declarative when the
        object is found inside of an Annotated object."""
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: RegistryType, cls: Type[Any], originating_module: str | None, key: str, mapped_container: Type[Mapped[Any]] | None, annotation: _AnnotationScanType | None, extracted_mapped_annotation: _AnnotationScanType | None, is_dataclass_field: bool) -> None:
        """Perform class-specific initializaton at early declarative scanning
        time.

        .. versionadded:: 2.0

        """

class _AttributeOptions(NamedTuple):
    """define Python-local attribute behavior options common to all
    :class:`.MapperProperty` objects.

    Currently this includes dataclass-generation arguments.

    .. versionadded:: 2.0

    """
    dataclasses_init: _NoArg | bool
    dataclasses_repr: _NoArg | bool
    dataclasses_default: _NoArg | Any
    dataclasses_default_factory: _NoArg | Callable[[], Any]
    dataclasses_compare: _NoArg | bool
    dataclasses_kw_only: _NoArg | bool

class _DCAttributeOptions:
    """mixin for descriptors or configurational objects that include dataclass
    field options.

    This includes :class:`.MapperProperty`, :class:`._MapsColumn` within
    the ORM, but also includes :class:`.AssociationProxy` within ext.
    Can in theory be used for other descriptors that serve a similar role
    as association proxy.   (*maybe* hybrids, not sure yet.)

    """

class _MapsColumns(_DCAttributeOptions, _MappedAttribute[_T]):
    """interface for declarative-capable construct that delivers one or more
    Column objects to the declarative process to be part of a Table.
    """
    @property
    def mapper_property_to_assign(self) -> MapperProperty[_T] | None:
        """return a MapperProperty to be assigned to the declarative mapping"""
    @property
    def columns_to_assign(self) -> List[Tuple[Column[_T], int]]:
        """A list of Column objects that should be declaratively added to the
        new Table object.

        """

class MapperProperty(HasCacheKey, _DCAttributeOptions, _MappedAttribute[_T], InspectionAttrInfo, util.MemoizedSlots):
    """Represent a particular class attribute mapped by :class:`_orm.Mapper`.

    The most common occurrences of :class:`.MapperProperty` are the
    mapped :class:`_schema.Column`, which is represented in a mapping as
    an instance of :class:`.ColumnProperty`,
    and a reference to another class produced by :func:`_orm.relationship`,
    represented in the mapping as an instance of
    :class:`.Relationship`.

    """
    is_property: bool
    comparator: PropComparator[_T]
    key: str
    parent: Mapper[Any]
    doc: str | None
    info: _InfoType
    def setup(self, context: ORMCompileState, query_entity: _MapperEntity, path: AbstractEntityRegistry, adapter: ORMAdapter | None, **kwargs: Any) -> None:
        """Called by Query for the purposes of constructing a SQL statement.

        Each MapperProperty associated with the target mapper processes the
        statement referenced by the query context, adding columns and/or
        criterion as appropriate.

        """
    def create_row_processor(self, context: ORMCompileState, query_entity: _MapperEntity, path: AbstractEntityRegistry, mapper: Mapper[Any], result: Result[Any], adapter: ORMAdapter | None, populators: _PopulatorDict) -> None:
        """Produce row processing functions and append to the given
        set of populators lists.

        """
    def cascade_iterator(self, type_: str, state: InstanceState[Any], dict_: _InstanceDict, visited_states: Set[InstanceState[Any]], halt_on: Callable[[InstanceState[Any]], bool] | None = None) -> Iterator[Tuple[object, Mapper[Any], InstanceState[Any], _InstanceDict]]:
        """Iterate through instances related to the given instance for
        a particular 'cascade', starting with this MapperProperty.

        Return an iterator3-tuples (instance, mapper, state).

        Note that the 'cascade' collection on this MapperProperty is
        checked first for the given type before cascade_iterator is called.

        This method typically only applies to Relationship.

        """
    def set_parent(self, parent: Mapper[Any], init: bool) -> None:
        """Set the parent mapper that references this MapperProperty.

        This method is overridden by some subclasses to perform extra
        setup when the mapper is first known.

        """
    def instrument_class(self, mapper: Mapper[Any]) -> None:
        '''Hook called by the Mapper to the property to initiate
        instrumentation of the class attribute managed by this
        MapperProperty.

        The MapperProperty here will typically call out to the
        attributes module to set up an InstrumentedAttribute.

        This step is the first of two steps to set up an InstrumentedAttribute,
        and is called early in the mapper setup process.

        The second step is typically the init_class_attribute step,
        called from StrategizedProperty via the post_instrument_class()
        hook.  This step assigns additional state to the InstrumentedAttribute
        (specifically the "impl") which has been determined after the
        MapperProperty has determined what kind of persistence
        management it needs to do (e.g. scalar, object, collection, etc).

        '''
    def __init__(self, attribute_options: _AttributeOptions | None = None, _assume_readonly_dc_attributes: bool = False) -> None: ...
    def init(self) -> None:
        """Called after all mappers are created to assemble
        relationships between mappers and perform other post-mapper-creation
        initialization steps.


        """
    @property
    def class_attribute(self) -> InstrumentedAttribute[_T]:
        """Return the class-bound descriptor corresponding to this
        :class:`.MapperProperty`.

        This is basically a ``getattr()`` call::

            return getattr(self.parent.class_, self.key)

        I.e. if this :class:`.MapperProperty` were named ``addresses``,
        and the class to which it is mapped is ``User``, this sequence
        is possible::

            >>> from sqlalchemy import inspect
            >>> mapper = inspect(User)
            >>> addresses_property = mapper.attrs.addresses
            >>> addresses_property.class_attribute is User.addresses
            True
            >>> User.addresses.property is addresses_property
            True


        """
    def do_init(self) -> None:
        """Perform subclass-specific initialization post-mapper-creation
        steps.

        This is a template method called by the ``MapperProperty``
        object's init() method.

        """
    def post_instrument_class(self, mapper: Mapper[Any]) -> None:
        """Perform instrumentation adjustments that need to occur
        after init() has completed.

        The given Mapper is the Mapper invoking the operation, which
        may not be the same Mapper as self.parent in an inheritance
        scenario; however, Mapper will always at least be a sub-mapper of
        self.parent.

        This method is typically used by StrategizedProperty, which delegates
        it to LoaderStrategy.init_class_attribute() to perform final setup
        on the class-bound InstrumentedAttribute.

        """
    def merge(self, session: Session, source_state: InstanceState[Any], source_dict: _InstanceDict, dest_state: InstanceState[Any], dest_dict: _InstanceDict, load: bool, _recursive: Dict[Any, object], _resolve_conflict_map: Dict[_IdentityKeyType[Any], object]) -> None:
        """Merge the attribute represented by this ``MapperProperty``
        from source to destination object.

        """

class PropComparator(SQLORMOperations[_T_co], ColumnOperators, Generic[_T_co]):
    '''Defines SQL operations for ORM mapped attributes.

    SQLAlchemy allows for operators to
    be redefined at both the Core and ORM level.  :class:`.PropComparator`
    is the base class of operator redefinition for ORM-level operations,
    including those of :class:`.ColumnProperty`,
    :class:`.Relationship`, and :class:`.Composite`.

    User-defined subclasses of :class:`.PropComparator` may be created. The
    built-in Python comparison and math operator methods, such as
    :meth:`.operators.ColumnOperators.__eq__`,
    :meth:`.operators.ColumnOperators.__lt__`, and
    :meth:`.operators.ColumnOperators.__add__`, can be overridden to provide
    new operator behavior. The custom :class:`.PropComparator` is passed to
    the :class:`.MapperProperty` instance via the ``comparator_factory``
    argument. In each case,
    the appropriate subclass of :class:`.PropComparator` should be used::

        # definition of custom PropComparator subclasses

        from sqlalchemy.orm.properties import \\\n                                ColumnProperty,\\\n                                Composite,\\\n                                Relationship

        class MyColumnComparator(ColumnProperty.Comparator):
            def __eq__(self, other):
                return self.__clause_element__() == other

        class MyRelationshipComparator(Relationship.Comparator):
            def any(self, expression):
                "define the \'any\' operation"
                # ...

        class MyCompositeComparator(Composite.Comparator):
            def __gt__(self, other):
                "redefine the \'greater than\' operation"

                return sql.and_(*[a>b for a, b in
                                  zip(self.__clause_element__().clauses,
                                      other.__composite_values__())])


        # application of custom PropComparator subclasses

        from sqlalchemy.orm import column_property, relationship, composite
        from sqlalchemy import Column, String

        class SomeMappedClass(Base):
            some_column = column_property(Column("some_column", String),
                                comparator_factory=MyColumnComparator)

            some_relationship = relationship(SomeOtherClass,
                                comparator_factory=MyRelationshipComparator)

            some_composite = composite(
                    Column("a", String), Column("b", String),
                    comparator_factory=MyCompositeComparator
                )

    Note that for column-level operator redefinition, it\'s usually
    simpler to define the operators at the Core level, using the
    :attr:`.TypeEngine.comparator_factory` attribute.  See
    :ref:`types_operators` for more detail.

    .. seealso::

        :class:`.ColumnProperty.Comparator`

        :class:`.Relationship.Comparator`

        :class:`.Composite.Comparator`

        :class:`.ColumnOperators`

        :ref:`types_operators`

        :attr:`.TypeEngine.comparator_factory`

    '''
    __visit_name__: str
    prop: RODescriptorReference[MapperProperty[_T_co]]
    def __init__(self, prop: MapperProperty[_T], parentmapper: _InternalEntityType[Any], adapt_to_entity: AliasedInsp[Any] | None = None) -> None: ...
    def property(self) -> MapperProperty[_T]:
        """Return the :class:`.MapperProperty` associated with this
        :class:`.PropComparator`.


        Return values here will commonly be instances of
        :class:`.ColumnProperty` or :class:`.Relationship`.


        """
    def __clause_element__(self) -> roles.ColumnsClauseRole: ...
    def adapt_to_entity(self, adapt_to_entity: AliasedInsp[Any]) -> PropComparator[_T]:
        """Return a copy of this PropComparator which will use the given
        :class:`.AliasedInsp` to produce corresponding expressions.
        """
    def adapter(self) -> _ORMAdapterProto | None:
        """Produce a callable that adapts column expressions
        to suit an aliased version of this comparator.

        """
    def info(self) -> _InfoType: ...
    any_op: Incomplete
    has_op: Incomplete
    of_type_op: Incomplete
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def of_type(self, class_: _EntityType[Any]) -> PropComparator[_T]:
        """Redefine this object in terms of a polymorphic subclass,
        :func:`_orm.with_polymorphic` construct, or :func:`_orm.aliased`
        construct.

        Returns a new PropComparator from which further criterion can be
        evaluated.

        e.g.::

            query.join(Company.employees.of_type(Engineer)).\\\n               filter(Engineer.name=='foo')

        :param \\class_: a class or mapper indicating that criterion will be
            against this specific subclass.

        .. seealso::

            :ref:`orm_queryguide_joining_relationships_aliased` - in the
            :ref:`queryguide_toplevel`

            :ref:`inheritance_of_type`

        """
    def and_(self, *criteria: _ColumnExpressionArgument[bool]) -> PropComparator[bool]:
        """Add additional criteria to the ON clause that's represented by this
        relationship attribute.

        E.g.::


            stmt = select(User).join(
                User.addresses.and_(Address.email_address != 'foo')
            )

            stmt = select(User).options(
                joinedload(User.addresses.and_(Address.email_address != 'foo'))
            )

        .. versionadded:: 1.4

        .. seealso::

            :ref:`orm_queryguide_join_on_augmented`

            :ref:`loader_option_criteria`

            :func:`.with_loader_criteria`

        """
    def any(self, criterion: _ColumnExpressionArgument[bool] | None = None, **kwargs: Any) -> ColumnElement[bool]:
        """Return a SQL expression representing true if this element
        references a member which meets the given criterion.

        The usual implementation of ``any()`` is
        :meth:`.Relationship.Comparator.any`.

        :param criterion: an optional ClauseElement formulated against the
          member class' table or attributes.

        :param \\**kwargs: key/value pairs corresponding to member class
          attribute names which will be compared via equality to the
          corresponding values.

        """
    def has(self, criterion: _ColumnExpressionArgument[bool] | None = None, **kwargs: Any) -> ColumnElement[bool]:
        """Return a SQL expression representing true if this element
        references a member which meets the given criterion.

        The usual implementation of ``has()`` is
        :meth:`.Relationship.Comparator.has`.

        :param criterion: an optional ClauseElement formulated against the
          member class' table or attributes.

        :param \\**kwargs: key/value pairs corresponding to member class
          attribute names which will be compared via equality to the
          corresponding values.

        """

class StrategizedProperty(MapperProperty[_T]):
    """A MapperProperty which uses selectable strategies to affect
    loading behavior.

    There is a single strategy selected by default.  Alternate
    strategies can be selected at Query time through the usage of
    ``StrategizedOption`` objects via the Query.options() method.

    The mechanics of StrategizedProperty are used for every Query
    invocation for every mapped attribute participating in that Query,
    to determine first how the attribute will be rendered in SQL
    and secondly how the attribute will retrieve a value from a result
    row and apply it to a mapped object.  The routines here are very
    performance-critical.

    """
    inherit_cache: bool
    strategy_wildcard_key: ClassVar[str]
    strategy_key: _StrategyKey
    def setup(self, context: ORMCompileState, query_entity: _MapperEntity, path: AbstractEntityRegistry, adapter: ORMAdapter | None, **kwargs: Any) -> None: ...
    def create_row_processor(self, context: ORMCompileState, query_entity: _MapperEntity, path: AbstractEntityRegistry, mapper: Mapper[Any], result: Result[Any], adapter: ORMAdapter | None, populators: _PopulatorDict) -> None: ...
    strategy: Incomplete
    def do_init(self) -> None: ...
    def post_instrument_class(self, mapper: Mapper[Any]) -> None: ...
    @classmethod
    def strategy_for(cls, **kw: Any) -> Callable[[_TLS], _TLS]: ...

class ORMOption(ExecutableOption):
    """Base class for option objects that are passed to ORM queries.

    These options may be consumed by :meth:`.Query.options`,
    :meth:`.Select.options`, or in a more general sense by any
    :meth:`.Executable.options` method.   They are interpreted at
    statement compile time or execution time in modern use.  The
    deprecated :class:`.MapperOption` is consumed at ORM query construction
    time.

    .. versionadded:: 1.4

    """
    propagate_to_loaders: bool

class CompileStateOption(HasCacheKey, ORMOption):
    """base for :class:`.ORMOption` classes that affect the compilation of
    a SQL query and therefore need to be part of the cache key.

    .. note::  :class:`.CompileStateOption` is generally non-public and
       should not be used as a base class for user-defined options; instead,
       use :class:`.UserDefinedOption`, which is easier to use as it does not
       interact with ORM compilation internals or caching.

    :class:`.CompileStateOption` defines an internal attribute
    ``_is_compile_state=True`` which has the effect of the ORM compilation
    routines for SELECT and other statements will call upon these options when
    a SQL string is being compiled. As such, these classes implement
    :class:`.HasCacheKey` and need to provide robust ``_cache_key_traversal``
    structures.

    The :class:`.CompileStateOption` class is used to implement the ORM
    :class:`.LoaderOption` and :class:`.CriteriaOption` classes.

    .. versionadded:: 1.4.28


    """
    def process_compile_state(self, compile_state: ORMCompileState) -> None:
        """Apply a modification to a given :class:`.ORMCompileState`.

        This method is part of the implementation of a particular
        :class:`.CompileStateOption` and is only invoked internally
        when an ORM query is compiled.

        """
    def process_compile_state_replaced_entities(self, compile_state: ORMCompileState, mapper_entities: Sequence[_MapperEntity]) -> None:
        """Apply a modification to a given :class:`.ORMCompileState`,
        given entities that were replaced by with_only_columns() or
        with_entities().

        This method is part of the implementation of a particular
        :class:`.CompileStateOption` and is only invoked internally
        when an ORM query is compiled.

        .. versionadded:: 1.4.19

        """

class LoaderOption(CompileStateOption):
    """Describe a loader modification to an ORM statement at compilation time.

    .. versionadded:: 1.4

    """
    def process_compile_state_replaced_entities(self, compile_state: ORMCompileState, mapper_entities: Sequence[_MapperEntity]) -> None: ...

class CriteriaOption(CompileStateOption):
    """Describe a WHERE criteria modification to an ORM statement at
    compilation time.

    .. versionadded:: 1.4

    """
    def get_global_criteria(self, attributes: Dict[str, Any]) -> None:
        """update additional entity criteria options in the given
        attributes dictionary.

        """

class UserDefinedOption(ORMOption):
    """Base class for a user-defined option that can be consumed from the
    :meth:`.SessionEvents.do_orm_execute` event hook.

    """
    propagate_to_loaders: bool
    payload: Incomplete
    def __init__(self, payload: Any | None = None) -> None: ...

class MapperOption(ORMOption):
    """Describe a modification to a Query"""
    propagate_to_loaders: bool
    def process_query(self, query: Query[Any]) -> None:
        """Apply a modification to the given :class:`_query.Query`."""
    def process_query_conditionally(self, query: Query[Any]) -> None:
        """same as process_query(), except that this option may not
        apply to the given query.

        This is typically applied during a lazy load or scalar refresh
        operation to propagate options stated in the original Query to the
        new Query being used for the load.  It occurs for those options that
        specify propagate_to_loaders=True.

        """

class LoaderStrategy:
    '''Describe the loading behavior of a StrategizedProperty object.

    The ``LoaderStrategy`` interacts with the querying process in three
    ways:

    * it controls the configuration of the ``InstrumentedAttribute``
      placed on a class to handle the behavior of the attribute.  this
      may involve setting up class-level callable functions to fire
      off a select operation when the attribute is first accessed
      (i.e. a lazy load)

    * it processes the ``QueryContext`` at statement construction time,
      where it can modify the SQL statement that is being produced.
      For example, simple column attributes will add their represented
      column to the list of selected columns, a joined eager loader
      may establish join clauses to add to the statement.

    * It produces "row processor" functions at result fetching time.
      These "row processor" functions populate a particular attribute
      on a particular mapped instance.

    '''
    parent_property: Incomplete
    is_class_level: bool
    parent: Incomplete
    key: Incomplete
    strategy_key: Incomplete
    strategy_opts: Incomplete
    def __init__(self, parent: MapperProperty[Any], strategy_key: _StrategyKey) -> None: ...
    def init_class_attribute(self, mapper: Mapper[Any]) -> None: ...
    def setup_query(self, compile_state: ORMCompileState, query_entity: _MapperEntity, path: AbstractEntityRegistry, loadopt: _LoadElement | None, adapter: ORMAdapter | None, **kwargs: Any) -> None:
        """Establish column and other state for a given QueryContext.

        This method fulfills the contract specified by MapperProperty.setup().

        StrategizedProperty delegates its setup() method
        directly to this method.

        """
    def create_row_processor(self, context: ORMCompileState, query_entity: _MapperEntity, path: AbstractEntityRegistry, loadopt: _LoadElement | None, mapper: Mapper[Any], result: Result[Any], adapter: ORMAdapter | None, populators: _PopulatorDict) -> None:
        """Establish row processing functions for a given QueryContext.

        This method fulfills the contract specified by
        MapperProperty.create_row_processor().

        StrategizedProperty delegates its create_row_processor() method
        directly to this method.

        """
