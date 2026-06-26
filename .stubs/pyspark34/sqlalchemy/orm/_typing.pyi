from ..engine.interfaces import _CoreKnownExecutionOptions
from ..sql import roles as roles
from ..sql._orm_types import DMLStrategyArgument as DMLStrategyArgument, SynchronizeSessionArgument as SynchronizeSessionArgument
from ..sql._typing import _CE
from ..sql.base import ExecutableOption as ExecutableOption
from ..sql.elements import ColumnElement as ColumnElement
from ..util.typing import Protocol as Protocol, TypeGuard as TypeGuard
from .attributes import AttributeImpl as AttributeImpl, CollectionAttributeImpl as CollectionAttributeImpl, HasCollectionAdapter as HasCollectionAdapter, QueryableAttribute as QueryableAttribute
from .base import PassiveFlag as PassiveFlag
from .interfaces import InspectionAttr as InspectionAttr, MapperProperty as MapperProperty, ORMOption as ORMOption, UserDefinedOption as UserDefinedOption
from .mapper import Mapper as Mapper
from .relationships import RelationshipProperty as RelationshipProperty
from .state import InstanceState as InstanceState
from .util import AliasedClass as AliasedClass, AliasedInsp as AliasedInsp
from _typeshed import Incomplete
from typing import Any

class _OrmKnownExecutionOptions(_CoreKnownExecutionOptions, total=False):
    populate_existing: bool
    autoflush: bool
    synchronize_session: SynchronizeSessionArgument
    dml_strategy: DMLStrategyArgument
    is_delete_using: bool
    is_update_from: bool

OrmExecuteOptionsParameter: Incomplete

class _ORMAdapterProto(Protocol):
    """protocol for the :class:`.AliasedInsp._orm_adapt_element` method
    which is a synonym for :class:`.AliasedInsp._adapt_element`.


    """
    def __call__(self, obj: _CE, key: str | None = None) -> _CE: ...

class _LoaderCallable(Protocol):
    def __call__(self, state: InstanceState[Any], passive: PassiveFlag) -> Any: ...

def is_orm_option(opt: ExecutableOption) -> TypeGuard[ORMOption]: ...
def is_user_defined_option(opt: ExecutableOption) -> TypeGuard[UserDefinedOption]: ...
def is_composite_class(obj: Any) -> bool: ...
def insp_is_mapper_property(obj: Any) -> TypeGuard[MapperProperty[Any]]: ...
def insp_is_mapper(obj: Any) -> TypeGuard[Mapper[Any]]: ...
def insp_is_aliased_class(obj: Any) -> TypeGuard[AliasedInsp[Any]]: ...
def insp_is_attribute(obj: InspectionAttr) -> TypeGuard[QueryableAttribute[Any]]: ...
def attr_is_internal_proxy(obj: InspectionAttr) -> TypeGuard[QueryableAttribute[Any]]: ...
def prop_is_relationship(prop: MapperProperty[Any]) -> TypeGuard[RelationshipProperty[Any]]: ...
def is_collection_impl(impl: AttributeImpl) -> TypeGuard[CollectionAttributeImpl]: ...
def is_has_collection_adapter(impl: AttributeImpl) -> TypeGuard[HasCollectionAdapter]: ...
