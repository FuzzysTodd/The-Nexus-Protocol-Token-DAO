from .. import ForeignKey, log, util
from ..sql import roles
from ..sql._typing import _InfoType
from ..sql.base import _NoArg
from ..sql.elements import ColumnElement, NamedColumn
from ..sql.operators import OperatorType
from ..sql.schema import Column
from ..util.typing import RODescriptorReference, _AnnotationScanType
from ._typing import _IdentityKeyType, _InstanceDict, _ORMColumnExprArgument, _RegistryType
from .base import Mapped, _DeclarativeMapped
from .decl_base import _ClassScanMapperConfig
from .descriptor_props import CompositeProperty as CompositeProperty, ConcreteInheritedProperty as ConcreteInheritedProperty, SynonymProperty as SynonymProperty
from .interfaces import MapperProperty, PropComparator, StrategizedProperty, _AttributeOptions, _IntrospectsAnnotations, _MapsColumns
from .mapper import Mapper
from .relationships import RelationshipProperty as RelationshipProperty
from .session import Session
from .state import InstanceState
from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence, Set, Tuple, Type

__all__ = ['ColumnProperty', 'CompositeProperty', 'ConcreteInheritedProperty', 'RelationshipProperty', 'SynonymProperty']

class ColumnProperty(_MapsColumns[_T], StrategizedProperty[_T], _IntrospectsAnnotations, log.Identified):
    """Describes an object attribute that corresponds to a table column
    or other column expression.

    Public constructor is the :func:`_orm.column_property` function.

    """
    strategy_wildcard_key: Incomplete
    inherit_cache: bool
    columns: List[NamedColumn[Any]]
    comparator_factory: Type[PropComparator[_T]]
    group: Incomplete
    deferred: Incomplete
    raiseload: Incomplete
    instrument: Incomplete
    active_history: Incomplete
    expire_on_flush: Incomplete
    doc: Incomplete
    strategy_key: Incomplete
    def __init__(self, column: _ORMColumnExprArgument[_T], *additional_columns: _ORMColumnExprArgument[Any], attribute_options: _AttributeOptions | None = None, group: str | None = None, deferred: bool = False, raiseload: bool = False, comparator_factory: Type[PropComparator[_T]] | None = None, active_history: bool = False, expire_on_flush: bool = True, info: _InfoType | None = None, doc: str | None = None, _instrument: bool = True, _assume_readonly_dc_attributes: bool = False) -> None: ...
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: str | None, key: str, mapped_container: Type[Mapped[Any]] | None, annotation: _AnnotationScanType | None, extracted_mapped_annotation: _AnnotationScanType | None, is_dataclass_field: bool) -> None: ...
    @property
    def mapper_property_to_assign(self) -> MapperProperty[_T] | None: ...
    @property
    def columns_to_assign(self) -> List[Tuple[Column[Any], int]]: ...
    def __clause_element__(self) -> roles.ColumnsClauseRole:
        """Allow the ColumnProperty to work in expression before it is turned
        into an instrumented attribute.
        """
    @property
    def expression(self) -> roles.ColumnsClauseRole:
        """Return the primary column or expression for this ColumnProperty.

        E.g.::


            class File(Base):
                # ...

                name = Column(String(64))
                extension = Column(String(8))
                filename = column_property(name + '.' + extension)
                path = column_property('C:/' + filename.expression)

        .. seealso::

            :ref:`mapper_column_property_sql_expressions_composed`

        """
    def instrument_class(self, mapper: Mapper[Any]) -> None: ...
    def do_init(self) -> None: ...
    def copy(self) -> ColumnProperty[_T]: ...
    def merge(self, session: Session, source_state: InstanceState[Any], source_dict: _InstanceDict, dest_state: InstanceState[Any], dest_dict: _InstanceDict, load: bool, _recursive: Dict[Any, object], _resolve_conflict_map: Dict[_IdentityKeyType[Any], object]) -> None: ...
    class Comparator(util.MemoizedSlots, PropComparator[_PT]):
        """Produce boolean, comparison, and other operators for
        :class:`.ColumnProperty` attributes.

        See the documentation for :class:`.PropComparator` for a brief
        overview.

        .. seealso::

            :class:`.PropComparator`

            :class:`.ColumnOperators`

            :ref:`types_operators`

            :attr:`.TypeEngine.comparator_factory`

        """
        prop: RODescriptorReference[ColumnProperty[_PT]]
        expressions: Sequence[NamedColumn[Any]]
        def __clause_element__(self) -> NamedColumn[_PT]: ...
        def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
        def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...

class MappedSQLExpression(ColumnProperty[_T], _DeclarativeMapped[_T]):
    """Declarative front-end for the :class:`.ColumnProperty` class.

    Public constructor is the :func:`_orm.column_property` function.

    .. versionchanged:: 2.0 Added :class:`_orm.MappedSQLExpression` as
       a Declarative compatible subclass for :class:`_orm.ColumnProperty`.

    .. seealso::

        :class:`.MappedColumn`

    """
    inherit_cache: bool

class MappedColumn(_IntrospectsAnnotations, _MapsColumns[_T], _DeclarativeMapped[_T]):
    """Maps a single :class:`_schema.Column` on a class.

    :class:`_orm.MappedColumn` is a specialization of the
    :class:`_orm.ColumnProperty` class and is oriented towards declarative
    configuration.

    To construct :class:`_orm.MappedColumn` objects, use the
    :func:`_orm.mapped_column` constructor function.

    .. versionadded:: 2.0


    """
    deferred: _NoArg | bool
    deferred_raiseload: bool
    deferred_group: str | None
    column: Column[_T]
    foreign_keys: Set[ForeignKey] | None
    active_history: Incomplete
    def __init__(self, *arg: Any, **kw: Any) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def mapper_property_to_assign(self) -> MapperProperty[_T] | None: ...
    @property
    def columns_to_assign(self) -> List[Tuple[Column[Any], int]]: ...
    def __clause_element__(self) -> Column[_T]: ...
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def found_in_pep593_annotated(self) -> Any: ...
    def declarative_scan(self, decl_scan: _ClassScanMapperConfig, registry: _RegistryType, cls: Type[Any], originating_module: str | None, key: str, mapped_container: Type[Mapped[Any]] | None, annotation: _AnnotationScanType | None, extracted_mapped_annotation: _AnnotationScanType | None, is_dataclass_field: bool) -> None: ...
    def declarative_scan_for_composite(self, registry: _RegistryType, cls: Type[Any], originating_module: str | None, key: str, param_name: str, param_annotation: _AnnotationScanType) -> None: ...
