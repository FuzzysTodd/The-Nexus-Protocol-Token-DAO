from . import attributes as attributes, util as orm_util
from .. import event as event, schema as schema, sql as sql, util as util
from ..engine.base import Connection as Connection
from ..engine.row import Row as Row
from ..sql import expression as expression, operators as operators
from ..sql._typing import _InfoType
from ..sql.elements import BindParameter as BindParameter, ClauseList as ClauseList, ColumnElement as ColumnElement
from ..sql.operators import OperatorType as OperatorType
from ..sql.schema import Column as Column
from ..sql.selectable import Select as Select
from ..util.typing import CallableReference as CallableReference, DescriptorReference as DescriptorReference, RODescriptorReference as RODescriptorReference, _AnnotationScanType, is_fwd_ref as is_fwd_ref, is_pep593 as is_pep593, typing_get_args as typing_get_args
from ._typing import _InstanceDict, _RegistryType
from .attributes import History as History, InstrumentedAttribute as InstrumentedAttribute, QueryableAttribute as QueryableAttribute
from .base import LoaderCallableStatus as LoaderCallableStatus, Mapped as Mapped, PassiveFlag as PassiveFlag, SQLORMOperations as SQLORMOperations, _DeclarativeMapped
from .context import ORMCompileState as ORMCompileState
from .decl_base import _ClassScanMapperConfig
from .interfaces import MapperProperty as MapperProperty, PropComparator as PropComparator, _AttributeOptions, _IntrospectsAnnotations, _MapsColumns
from .mapper import Mapper as Mapper
from .properties import ColumnProperty as ColumnProperty, MappedColumn as MappedColumn
from .state import InstanceState as InstanceState
from .util import de_stringify_annotation as de_stringify_annotation
from _typeshed import Incomplete
from typing import Any, Callable, List, Sequence, Tuple, Type

class DescriptorProperty(MapperProperty[_T]):
    """:class:`.MapperProperty` which proxies access to a
    user-defined descriptor."""
    doc: str | None
    uses_objects: bool
    descriptor: DescriptorReference[Any]
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    key: Incomplete
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...

class CompositeProperty(_MapsColumns[_CC], _IntrospectsAnnotations, DescriptorProperty[_CC]):
    '''Defines a "composite" mapped attribute, representing a collection
    of columns as one attribute.

    :class:`.CompositeProperty` is constructed using the :func:`.composite`
    function.

    .. seealso::

        :ref:`mapper_composite`

    '''
    composite_class: Type[_CC] | Callable[..., _CC]
    attrs: Tuple[_CompositeAttrType[Any], ...]
    comparator_factory: Type[Comparator[_CC]]
    active_history: Incomplete
    deferred: Incomplete
    group: Incomplete
    def __init__(self, _class_or_attr: None | Type[_CC] | Callable[..., _CC] | _CompositeAttrType[Any] = None, *attrs: _CompositeAttrType[Any], attribute_options: _AttributeOptions | None = None, active_history: bool = False, deferred: bool = False, group: str | None = None, comparator_factory: Type[Comparator[_CC]] | None = None, info: _InfoType | None = None, **kwargs: Any) -> None: ...
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...
    def do_init(self) -> None:
        """Initialization which occurs after the :class:`.Composite`
        has been associated with its parent mapper.

        """
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: str | None, key: str, mapped_container: Type[Mapped[Any]] | None, annotation: _AnnotationScanType | None, extracted_mapped_annotation: _AnnotationScanType | None, is_dataclass_field: bool) -> None: ...
    def props(self) -> Sequence[MapperProperty[Any]]: ...
    def columns(self) -> Sequence[Column[Any]]: ...
    @property
    def mapper_property_to_assign(self) -> MapperProperty[_CC] | None: ...
    @property
    def columns_to_assign(self) -> List[Tuple[schema.Column[Any], int]]: ...
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History:
        """Provided for userland code that uses attributes.get_history()."""
    class CompositeBundle(orm_util.Bundle[_T]):
        property: Incomplete
        def __init__(self, property_: Composite[_T], expr: ClauseList) -> None: ...
        def create_row_processor(self, query: Select[Any], procs: Sequence[Callable[[Row[Any]], Any]], labels: Sequence[str]) -> Callable[[Row[Any]], Any]: ...
    class Comparator(PropComparator[_PT]):
        """Produce boolean, comparison, and other operators for
        :class:`.Composite` attributes.

        See the example in :ref:`composite_operations` for an overview
        of usage , as well as the documentation for :class:`.PropComparator`.

        .. seealso::

            :class:`.PropComparator`

            :class:`.ColumnOperators`

            :ref:`types_operators`

            :attr:`.TypeEngine.comparator_factory`

        """
        __hash__: Incomplete
        prop: RODescriptorReference[Composite[_PT]]
        def clauses(self) -> ClauseList: ...
        def __clause_element__(self) -> CompositeProperty.CompositeBundle[_PT]: ...
        def expression(self) -> CompositeProperty.CompositeBundle[_PT]: ...
        def __eq__(self, other: Any) -> ColumnElement[bool]: ...
        def __ne__(self, other: Any) -> ColumnElement[bool]: ...
        def __lt__(self, other: Any) -> ColumnElement[bool]: ...
        def __gt__(self, other: Any) -> ColumnElement[bool]: ...
        def __le__(self, other: Any) -> ColumnElement[bool]: ...
        def __ge__(self, other: Any) -> ColumnElement[bool]: ...

class Composite(CompositeProperty[_T], _DeclarativeMapped[_T]):
    """Declarative-compatible front-end for the :class:`.CompositeProperty`
    class.

    Public constructor is the :func:`_orm.composite` function.

    .. versionchanged:: 2.0 Added :class:`_orm.Composite` as a Declarative
       compatible subclass of :class:`_orm.CompositeProperty`.

    .. seealso::

        :ref:`mapper_composite`

    """
    inherit_cache: bool

class ConcreteInheritedProperty(DescriptorProperty[_T]):
    '''A \'do nothing\' :class:`.MapperProperty` that disables
    an attribute on a concrete subclass that is only present
    on the inherited mapper, not the concrete classes\' mapper.

    Cases where this occurs include:

    * When the superclass mapper is mapped against a
      "polymorphic union", which includes all attributes from
      all subclasses.
    * When a relationship() is configured on an inherited mapper,
      but not on the subclass mapper.  Concrete mappers require
      that relationship() is configured explicitly on each
      subclass.

    '''
    descriptor: Incomplete
    def __init__(self) -> None: ...

class SynonymProperty(DescriptorProperty[_T]):
    """Denote an attribute name as a synonym to a mapped property,
    in that the attribute will mirror the value and expression behavior
    of another attribute.

    :class:`.Synonym` is constructed using the :func:`_orm.synonym`
    function.

    .. seealso::

        :ref:`synonyms` - Overview of synonyms

    """
    comparator_factory: Type[PropComparator[_T]] | None
    name: Incomplete
    map_column: Incomplete
    descriptor: Incomplete
    doc: Incomplete
    def __init__(self, name: str, map_column: bool | None = None, descriptor: Any | None = None, comparator_factory: Type[PropComparator[_T]] | None = None, attribute_options: _AttributeOptions | None = None, info: _InfoType | None = None, doc: str | None = None) -> None: ...
    def get_history(self, state: InstanceState[Any], dict_: _InstanceDict, passive: PassiveFlag = ...) -> History: ...
    parent: Incomplete
    def set_parent(self, parent: Mapper[Any], init: bool) -> None: ...

class Synonym(SynonymProperty[_T], _DeclarativeMapped[_T]):
    """Declarative front-end for the :class:`.SynonymProperty` class.

    Public constructor is the :func:`_orm.synonym` function.

    .. versionchanged:: 2.0 Added :class:`_orm.Synonym` as a Declarative
       compatible subclass for :class:`_orm.SynonymProperty`

    .. seealso::

        :ref:`synonyms` - Overview of synonyms

    """
    inherit_cache: bool
