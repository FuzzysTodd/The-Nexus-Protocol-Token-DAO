import logging
import typing as t
from .wrappers.request import Request as Request
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIEnvironment as WSGIEnvironment

class _Missing:
    def __reduce__(self) -> str: ...

class _ColorStreamHandler(logging.StreamHandler):
    """On Windows, wrap stream with Colorama for ANSI style support."""
    def __init__(self) -> None: ...

class _DictAccessorProperty(t.Generic[_TAccessorValue]):
    """Baseclass for `environ_property` and `header_property`."""
    read_only: bool
    name: Incomplete
    default: Incomplete
    load_func: Incomplete
    dump_func: Incomplete
    __doc__: Incomplete
    def __init__(self, name: str, default: _TAccessorValue | None = None, load_func: t.Callable[[str], _TAccessorValue] | None = None, dump_func: t.Callable[[_TAccessorValue], str] | None = None, read_only: bool | None = None, doc: str | None = None) -> None: ...
    def lookup(self, instance: t.Any) -> t.MutableMapping[str, t.Any]: ...
    @t.overload
    def __get__(self, instance: None, owner: type) -> _DictAccessorProperty[_TAccessorValue]: ...
    @t.overload
    def __get__(self, instance: t.Any, owner: type) -> _TAccessorValue: ...
    def __set__(self, instance: t.Any, value: _TAccessorValue) -> None: ...
    def __delete__(self, instance: t.Any) -> None: ...
