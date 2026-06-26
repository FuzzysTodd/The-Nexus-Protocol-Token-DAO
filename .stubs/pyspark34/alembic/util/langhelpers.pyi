from .compat import inspect_getfullargspec as inspect_getfullargspec
from _typeshed import Incomplete
from sqlalchemy.util import asbool as asbool, memoized_property as memoized_property, to_list as to_list
from typing import Any, Callable, Mapping, Tuple, overload

EMPTY_DICT: Mapping[Any, Any]

class _ModuleClsMeta(type):
    def __setattr__(cls, key: str, value: Callable) -> None: ...

class ModuleClsProxy(metaclass=_ModuleClsMeta):
    """Create module level proxy functions for the
    methods on a given class.

    The functions will have a compatible signature
    as the methods.

    """
    @classmethod
    def create_module_class_proxy(cls, globals_, locals_) -> None: ...

def rev_id() -> str: ...
@overload
def to_tuple(x: Any, default: tuple) -> tuple: ...
@overload
def to_tuple(x: None, default: _T | None = None) -> _T: ...
@overload
def to_tuple(x: Any, default: tuple | None = None) -> tuple: ...
def dedupe_tuple(tup: Tuple[str, ...]) -> Tuple[str, ...]: ...

class Dispatcher:
    uselist: Incomplete
    def __init__(self, uselist: bool = False) -> None: ...
    def dispatch_for(self, target: Any, qualifier: str = 'default') -> Callable: ...
    def dispatch(self, obj: Any, qualifier: str = 'default') -> Any: ...
    def branch(self) -> Dispatcher:
        """Return a copy of this dispatcher that is independently
        writable."""

def not_none(value: _T | None) -> _T: ...
