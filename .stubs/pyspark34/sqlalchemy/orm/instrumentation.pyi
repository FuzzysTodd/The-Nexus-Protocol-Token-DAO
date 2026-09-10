import weakref
from . import base as base, collections as collections, exc as exc, interfaces as interfaces, state as state
from .. import util as util
from ..event import EventTarget as EventTarget, dispatcher as dispatcher
from ..util import HasMemoized as HasMemoized
from ..util.typing import Literal as Literal, Protocol as Protocol
from ._typing import _O, _RegistryType
from .attributes import AttributeImpl as AttributeImpl, QueryableAttribute as QueryableAttribute
from .collections import _AdaptedCollectionProtocol, _CollectionFactoryType
from .decl_base import _MapperConfig
from .events import InstanceEvents as InstanceEvents
from .mapper import Mapper as Mapper
from .state import InstanceState as InstanceState
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Callable, Collection, Dict, Generic, Iterable, Set, Tuple, Type

DEL_ATTR: Incomplete

class _ExpiredAttributeLoaderProto(Protocol):
    def __call__(self, state: state.InstanceState[Any], toload: Set[str], passive: base.PassiveFlag) -> None: ...

class _ManagerFactory(Protocol):
    def __call__(self, class_: Type[_O]) -> ClassManager[_O]: ...

class ClassManager(HasMemoized, Dict[str, 'QueryableAttribute[Any]'], EventTarget, Generic[_O]):
    """Tracks state information at the class level."""
    dispatch: dispatcher[ClassManager[_O]]
    MANAGER_ATTR: Incomplete
    STATE_ATTR: Incomplete
    expired_attribute_loader: _ExpiredAttributeLoaderProto
    init_method: Callable[..., None] | None
    original_init: Callable[..., None] | None
    factory: _ManagerFactory | None
    declarative_scan: weakref.ref[_MapperConfig] | None
    registry: _RegistryType
    class_: Type[_O]
    @property
    def deferred_scalar_loader(self): ...
    @deferred_scalar_loader.setter
    def deferred_scalar_loader(self, obj) -> None: ...
    info: Incomplete
    new_init: Incomplete
    local_attrs: Incomplete
    originals: Incomplete
    def __init__(self, class_) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def is_mapped(self) -> bool: ...
    def mapper(self) -> Mapper[_O]: ...
    def manage(self) -> None:
        """Mark this instance as the manager for its class."""
    def manager_getter(self): ...
    def state_getter(self):
        '''Return a (instance) -> InstanceState callable.

        "state getter" callables should raise either KeyError or
        AttributeError if no InstanceState could be found for the
        instance.
        '''
    def dict_getter(self): ...
    def instrument_attribute(self, key: str, inst: QueryableAttribute[Any], propagated: bool = False) -> None: ...
    def subclass_managers(self, recursive) -> Generator[Incomplete, Incomplete, None]: ...
    def post_configure_attribute(self, key) -> None: ...
    def uninstrument_attribute(self, key, propagated: bool = False) -> None: ...
    def unregister(self) -> None:
        """remove all instrumentation established by this ClassManager."""
    def install_descriptor(self, key: str, inst: QueryableAttribute[Any]) -> None: ...
    def uninstall_descriptor(self, key: str) -> None: ...
    def install_member(self, key: str, implementation: Any) -> None: ...
    def uninstall_member(self, key: str) -> None: ...
    def instrument_collection_class(self, key: str, collection_class: Type[Collection[Any]]) -> _CollectionFactoryType: ...
    def initialize_collection(self, key: str, state: InstanceState[_O], factory: _CollectionFactoryType) -> Tuple[collections.CollectionAdapter, _AdaptedCollectionProtocol]: ...
    def is_instrumented(self, key: str, search: bool = False) -> bool: ...
    def get_impl(self, key: str) -> AttributeImpl: ...
    @property
    def attributes(self) -> Iterable[Any]: ...
    def new_instance(self, state: InstanceState[_O] | None = None) -> _O: ...
    def setup_instance(self, instance: _O, state: InstanceState[_O] | None = None) -> None: ...
    def teardown_instance(self, instance: _O) -> None: ...
    def has_state(self, instance: _O) -> bool: ...
    def has_parent(self, state: InstanceState[_O], key: str, optimistic: bool = False) -> bool:
        """TODO"""
    def __bool__(self) -> bool:
        """All ClassManagers are non-zero regardless of attribute state."""

class _SerializeManager:
    """Provide serialization of a :class:`.ClassManager`.

    The :class:`.InstanceState` uses ``__init__()`` on serialize
    and ``__call__()`` on deserialize.

    """
    class_: Incomplete
    def __init__(self, state: state.InstanceState[Any], d: Dict[str, Any]) -> None: ...
    def __call__(self, state, inst, state_dict) -> None: ...

class InstrumentationFactory(EventTarget):
    """Factory for new ClassManager instances."""
    dispatch: dispatcher[InstrumentationFactory]
    def create_manager_for_cls(self, class_: Type[_O]) -> ClassManager[_O]: ...
    def unregister(self, class_: Type[_O]) -> None: ...
instance_state = base.instance_state
instance_dict = base.instance_dict
manager_of_class = base.manager_of_class

opt_manager_of_class: Incomplete

def register_class(class_: Type[_O], finalize: bool = True, mapper: Mapper[_O] | None = None, registry: _RegistryType | None = None, declarative_scan: _MapperConfig | None = None, expired_attribute_loader: _ExpiredAttributeLoaderProto | None = None, init_method: Callable[..., None] | None = None) -> ClassManager[_O]:
    """Register class instrumentation.

    Returns the existing or newly created class manager.

    """
def unregister_class(class_) -> None:
    """Unregister class instrumentation."""
def is_instrumented(instance, key):
    """Return True if the given attribute on the given instance is
    instrumented by the attributes package.

    This function may be used regardless of instrumentation
    applied directly to the class, i.e. no descriptors are required.

    """
