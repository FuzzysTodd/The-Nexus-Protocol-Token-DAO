from .. import exc as exc, util as util
from .attr import RefCollection as RefCollection
from .base import dispatcher as dispatcher
from _typeshed import Incomplete
from typing import Any, Deque, Generic

class EventTarget:
    """represents an event target, that is, something we can listen on
    either with that target as a class or as an instance.

    Examples include:  Connection, Mapper, Table, Session,
    InstrumentedAttribute, Engine, Pool, Dialect.

    """
    dispatch: dispatcher[Any]

class _EventKey(Generic[_ET]):
    """Represent :func:`.listen` arguments."""
    target: _ET
    identifier: str
    fn: _ListenerFnType
    fn_key: _ListenerFnKeyType
    dispatch_target: Any
    fn_wrap: Incomplete
    def __init__(self, target: _ET, identifier: str, fn: _ListenerFnType, dispatch_target: Any, _fn_wrap: _ListenerFnType | None = None) -> None: ...
    def with_wrapper(self, fn_wrap: _ListenerFnType) -> _EventKey[_ET]: ...
    def with_dispatch_target(self, dispatch_target: Any) -> _EventKey[_ET]: ...
    def listen(self, *args: Any, **kw: Any) -> None: ...
    def remove(self) -> None: ...
    def contains(self) -> bool:
        """Return True if this event key is registered to listen."""
    def base_listen(self, propagate: bool = False, insert: bool = False, named: bool = False, retval: bool | None = None, asyncio: bool = False) -> None: ...
    def append_to_list(self, owner: RefCollection[_ET], list_: Deque[_ListenerFnType]) -> bool: ...
    def remove_from_list(self, owner: RefCollection[_ET], list_: Deque[_ListenerFnType]) -> None: ...
    def prepend_to_list(self, owner: RefCollection[_ET], list_: Deque[_ListenerFnType]) -> bool: ...
