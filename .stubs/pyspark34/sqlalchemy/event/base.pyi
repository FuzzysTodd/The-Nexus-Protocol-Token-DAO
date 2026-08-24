from .. import util as util
from ..util.typing import Literal as Literal
from .attr import _InstanceLevelDispatch, _JoinedListener
from .registry import _ET
from _typeshed import Incomplete
from typing import Any, Generic, Tuple, Type, overload

class _UnpickleDispatch:
    """Serializable callable that re-generates an instance of
    :class:`_Dispatch` given a particular :class:`.Events` subclass.

    """
    def __call__(self, _instance_cls: Type[_ET]) -> _Dispatch[_ET]: ...

class _DispatchCommon(Generic[_ET]):
    def __getattr__(self, name: str) -> _InstanceLevelDispatch[_ET]: ...

class _Dispatch(_DispatchCommon[_ET]):
    '''Mirror the event listening definitions of an Events class with
    listener collections.

    Classes which define a "dispatch" member will return a
    non-instantiated :class:`._Dispatch` subclass when the member
    is accessed at the class level.  When the "dispatch" member is
    accessed at the instance level of its owner, an instance
    of the :class:`._Dispatch` class is returned.

    A :class:`._Dispatch` class is generated for each :class:`.Events`
    class defined, by the :meth:`._HasEventsDispatch._create_dispatcher_class`
    method.  The original :class:`.Events` classes remain untouched.
    This decouples the construction of :class:`.Events` subclasses from
    the implementation used by the event internals, and allows
    inspecting tools like Sphinx to work in an unsurprising
    way against the public API.

    '''
    def __init__(self, parent: _Dispatch[_ET] | None, instance_cls: Type[_ET] | None = None) -> None: ...
    def __getattr__(self, name: str) -> _InstanceLevelDispatch[_ET]: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...

class _HasEventsDispatch(Generic[_ET]):
    dispatch: _Dispatch[_ET]
    def __getattr__(self, name: str) -> _InstanceLevelDispatch[_ET]: ...
    def __init_subclass__(cls) -> None:
        """Intercept new Event subclasses and create associated _Dispatch
        classes."""

class Events(_HasEventsDispatch[_ET]):
    """Define event listening functions for a particular target type."""

class _JoinedDispatcher(_DispatchCommon[_ET]):
    """Represent a connection between two _Dispatch objects."""
    local: _DispatchCommon[_ET]
    parent: _DispatchCommon[_ET]
    def __init__(self, local: _DispatchCommon[_ET], parent: _DispatchCommon[_ET]) -> None: ...
    def __getattr__(self, name: str) -> _JoinedListener[_ET]: ...

class dispatcher(Generic[_ET]):
    """Descriptor used by target classes to
    deliver the _Dispatch class at the class level
    and produce new _Dispatch instances for target
    instances.

    """
    dispatch: Incomplete
    events: Incomplete
    def __init__(self, events: Type[_HasEventsDispatch[_ET]]) -> None: ...
    @overload
    def __get__(self, obj: Literal[None], cls: Type[Any]) -> Type[_Dispatch[_ET]]: ...
    @overload
    def __get__(self, obj: Any, cls: Type[Any]) -> _DispatchCommon[_ET]: ...

class slots_dispatcher(dispatcher[_ET]):
    def __get__(self, obj: Any, cls: Type[Any]) -> Any: ...
