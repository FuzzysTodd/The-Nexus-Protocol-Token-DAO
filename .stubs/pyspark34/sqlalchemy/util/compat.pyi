import dataclasses
import typing
from _typeshed import Incomplete
from typing import Any, AsyncGenerator, Awaitable, Callable, Dict, Iterable, List, Mapping, Sequence, Tuple

py312: Incomplete
py311: Incomplete
py310: Incomplete
py39: Incomplete
py38: Incomplete
pypy: Incomplete
cpython: Incomplete
win32: Incomplete
osx: Incomplete
arm: Incomplete
is64bit: Incomplete
has_refcount_gc: Incomplete
dottedgetter: Incomplete

class FullArgSpec(typing.NamedTuple):
    args: List[str]
    varargs: str | None
    varkw: str | None
    defaults: Tuple[Any, ...] | None
    kwonlyargs: List[str]
    kwonlydefaults: Dict[str, Any]
    annotations: Dict[str, Any]

def inspect_getfullargspec(func: Callable[..., Any]) -> FullArgSpec:
    """Fully vendored version of getfullargspec from Python 3.3."""
def athrow(gen: AsyncGenerator[_T_co, Any], typ: Any, value: Any, traceback: Any) -> Awaitable[_T_co]: ...
def md5_not_for_security() -> Any: ...

dict_union: Incomplete
anext_ = anext

def importlib_metadata_get(group): ...
def b(s): ...
def b64decode(x: str) -> bytes: ...
def b64encode(x: bytes) -> str: ...
def decode_backslashreplace(text: bytes, encoding: str) -> str: ...
def cmp(a, b): ...
def inspect_formatargspec(args: List[str], varargs: str | None = None, varkw: str | None = None, defaults: Sequence[Any] | None = None, kwonlyargs: Sequence[str] | None = (), kwonlydefaults: Mapping[str, Any] | None = {}, annotations: Mapping[str, Any] = {}, formatarg: Callable[[str], str] = ..., formatvarargs: Callable[[str], str] = ..., formatvarkw: Callable[[str], str] = ..., formatvalue: Callable[[Any], str] = ..., formatreturns: Callable[[Any], str] = ..., formatannotation: Callable[[Any], str] = ...) -> str:
    '''Copy formatargspec from python 3.7 standard library.

    Python 3 has deprecated formatargspec and requested that Signature
    be used instead, however this requires a full reimplementation
    of formatargspec() in terms of creating Parameter objects and such.
    Instead of introducing all the object-creation overhead and having
    to reinvent from scratch, just copy their compatibility routine.

    Ultimately we would need to rewrite our "decorator" routine completely
    which is not really worth it right now, until all Python 2.x support
    is dropped.

    '''
def dataclass_fields(cls) -> Iterable[dataclasses.Field[Any]]:
    """Return a sequence of all dataclasses.Field objects associated
    with a class as an already processed dataclass.

    The class must **already be a dataclass** for Field objects to be returned.

    """
def local_dataclass_fields(cls) -> Iterable[dataclasses.Field[Any]]:
    """Return a sequence of all dataclasses.Field objects associated with
    an already processed dataclass, excluding those that originate from a
    superclass.

    The class must **already be a dataclass** for Field objects to be returned.

    """
