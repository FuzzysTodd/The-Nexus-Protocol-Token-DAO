from . import attributes as attributes, clsregistry as clsregistry, instrumentation as instrumentation, mapperlib as mapperlib
from .. import event as event, exc as exc, util as util
from ..sql import expression as expression
from ..sql.base import _NoArg
from ..sql.elements import NamedColumn as NamedColumn
from ..sql.schema import Column as Column, MetaData as MetaData, Table as Table
from ..sql.selectable import FromClause as FromClause
from ..util import topological as topological
from ..util.typing import Protocol as Protocol, TypedDict as TypedDict, _AnnotationScanType, is_fwd_ref as is_fwd_ref, is_literal as is_literal, typing_get_args as typing_get_args
from ._typing import _ClassDict, _O, _RegistryType, attr_is_internal_proxy as attr_is_internal_proxy
from .attributes import InstrumentedAttribute as InstrumentedAttribute, QueryableAttribute as QueryableAttribute
from .base import InspectionAttr as InspectionAttr, Mapped as Mapped
from .decl_api import declared_attr as declared_attr
from .descriptor_props import CompositeProperty as CompositeProperty, SynonymProperty as SynonymProperty
from .instrumentation import ClassManager as ClassManager
from .interfaces import MapperProperty as MapperProperty
from .mapper import Mapper as Mapper
from .properties import ColumnProperty as ColumnProperty, MappedColumn as MappedColumn
from .util import class_mapper as class_mapper, de_stringify_annotation as de_stringify_annotation
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Mapping, NamedTuple, NoReturn, Sequence, Type

class MappedClassProtocol(Protocol[_O]):
    """A protocol representing a SQLAlchemy mapped class.

    The protocol is generic on the type of class, use
    ``MappedClassProtocol[Any]`` to allow any mapped class.
    """
    __mapper__: Mapper[_O]
    __table__: FromClause
    def __call__(self, **kw: Any) -> _O: ...

class _DeclMappedClassProtocol(MappedClassProtocol[_O], Protocol):
    """Internal more detailed version of ``MappedClassProtocol``."""
    metadata: MetaData
    __tablename__: str
    __mapper_args__: _MapperKwArgs
    __table_args__: _TableArgsType | None
    def __declare_first__(self) -> None: ...
    def __declare_last__(self) -> None: ...

class _DataclassArguments(TypedDict):
    init: _NoArg | bool
    repr: _NoArg | bool
    eq: _NoArg | bool
    order: _NoArg | bool
    unsafe_hash: _NoArg | bool
    match_args: _NoArg | bool
    kw_only: _NoArg | bool
    dataclass_callable: _NoArg | Callable[..., Type[Any]]

class _MapperConfig:
    cls: Type[Any]
    classname: str
    properties: util.OrderedDict[str, Sequence[NamedColumn[Any]] | NamedColumn[Any] | MapperProperty[Any]]
    declared_attr_reg: Dict[declared_attr[Any], Any]
    @classmethod
    def setup_mapping(cls, registry: _RegistryType, cls_: Type[_O], dict_: _ClassDict, table: FromClause | None, mapper_kw: _MapperKwArgs) -> _MapperConfig | None: ...
    def __init__(self, registry: _RegistryType, cls_: Type[Any], mapper_kw: _MapperKwArgs) -> None: ...
    def set_cls_attribute(self, attrname: str, value: _T) -> _T: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...

class _ImperativeMapperConfig(_MapperConfig):
    local_table: Incomplete
    def __init__(self, registry: _RegistryType, cls_: Type[_O], table: FromClause | None, mapper_kw: _MapperKwArgs) -> None: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...

class _CollectedAnnotation(NamedTuple):
    raw_annotation: _AnnotationScanType
    mapped_container: Type[Mapped[Any]] | None
    extracted_mapped_annotation: Type[Any] | str
    is_dataclass: bool
    attr_value: Any
    originating_module: str
    originating_class: Type[Any]

class _ClassScanMapperConfig(_MapperConfig):
    is_deferred: bool
    registry: _RegistryType
    clsdict_view: _ClassDict
    collected_annotations: Dict[str, _CollectedAnnotation]
    collected_attributes: Dict[str, Any]
    local_table: FromClause | None
    persist_selectable: FromClause | None
    declared_columns: util.OrderedSet[Column[Any]]
    column_ordering: Dict[Column[Any], int]
    column_copies: Dict[MappedColumn[Any] | Column[Any], MappedColumn[Any] | Column[Any]]
    tablename: str | None
    mapper_args: Mapping[str, Any]
    table_args: _TableArgsType | None
    mapper_args_fn: Callable[[], Dict[str, Any]] | None
    inherits: Type[Any] | None
    single: bool
    is_dataclass_prior_to_mapping: bool
    allow_unmapped_annotations: bool
    dataclass_setup_arguments: _DataclassArguments | None
    allow_dataclass_fields: bool
    def __init__(self, registry: _RegistryType, cls_: Type[_O], dict_: _ClassDict, table: FromClause | None, mapper_kw: _MapperKwArgs) -> None: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...

class _DeferredMapperConfig(_ClassScanMapperConfig):
    is_deferred: bool
    @property
    def cls(self) -> Type[Any]: ...
    @cls.setter
    def cls(self, class_: Type[Any]) -> None: ...
    @classmethod
    def has_cls(cls, class_: Type[Any]) -> bool: ...
    @classmethod
    def raise_unmapped_for_cls(cls, class_: Type[Any]) -> NoReturn: ...
    @classmethod
    def config_for_cls(cls, class_: Type[Any]) -> _DeferredMapperConfig: ...
    @classmethod
    def classes_for_base(cls, base_cls: Type[Any], sort: bool = True) -> List[_DeferredMapperConfig]: ...
    def map(self, mapper_kw: _MapperKwArgs = ...) -> Mapper[Any]: ...
