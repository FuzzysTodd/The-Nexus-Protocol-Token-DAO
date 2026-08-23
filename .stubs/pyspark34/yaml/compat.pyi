import abc
import collections.abc
import io
from _typeshed import Incomplete
from abc import abstractmethod
from ordereddict import OrderedDict
from typing import Any, List, Tuple

SupportsIndex = int

class ordereddict(OrderedDict):
    def insert(self, pos: int, key: Any, value: Any) -> None: ...

PY2: Incomplete
PY3: Incomplete
StringIO = io.StringIO
BytesIO = io.BytesIO
StreamType = Any
StreamTextType = StreamType
VersionType = List[int] | str | Tuple[int, int]
builtins_module: str

def with_metaclass(meta: Any, *bases: Any) -> Any:
    """Create a base class with a metaclass."""

DBG_TOKEN: int
DBG_EVENT: int
DBG_NODE: int

class ObjectCounter:
    map: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, k: Any) -> None: ...
    def dump(self) -> None: ...

object_counter: Incomplete

def dbg(val: Any = None) -> Any: ...

class Nprint:
    def __init__(self, file_name: Any = None) -> None: ...
    def __call__(self, *args: Any, **kw: Any) -> None: ...
    def set_max_print(self, i: int) -> None: ...
    def fp(self, mode: str = 'a') -> Any: ...

nprint: Incomplete
nprintf: Incomplete

def check_namespace_char(ch: Any) -> bool: ...
def check_anchorname_char(ch: Any) -> bool: ...
def version_tnf(t1: Any, t2: Any = None) -> Any:
    """
    return True if ruamel.yaml version_info < t1, None if t2 is specified and bigger else False
    """

class MutableSliceableSequence(collections.abc.MutableSequence, metaclass=abc.ABCMeta):
    def __getitem__(self, index: Any) -> Any: ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def __delitem__(self, index: Any) -> None: ...
    @abstractmethod
    def __getsingleitem__(self, index: Any) -> Any: ...
    @abstractmethod
    def __setsingleitem__(self, index: Any, value: Any) -> None: ...
    @abstractmethod
    def __delsingleitem__(self, index: Any) -> None: ...
