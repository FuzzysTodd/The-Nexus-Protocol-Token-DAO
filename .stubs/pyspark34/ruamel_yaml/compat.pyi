import abc
import io
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Hashable as Hashable, Mapping as Mapping, MutableMapping as MutableMapping, MutableSequence
from ordereddict import OrderedDict
from typing import Any, BinaryIO, IO, List, Text, Tuple

class ordereddict(OrderedDict):
    def insert(self, pos: int, key: Any, value: Any) -> None: ...

PY2: Incomplete
PY3: Incomplete

def utf8(s: str) -> str: ...
def to_str(s: str) -> str: ...
def to_unicode(s: str) -> str: ...
string_types = str
integer_types = int
class_types = type
text_type = str
binary_type = bytes
MAXSIZE: Incomplete
unichr = chr
StringIO = io.StringIO
BytesIO = io.BytesIO
no_limit_int = int
StreamType = BinaryIO | IO[str] | StringIO
StreamTextType = Text | StreamType
VersionType = List[int] | str | Tuple[int, int]
builtins_module: str
UNICODE_SIZE: Incomplete

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

nprint: Incomplete
nprintf: Incomplete

def check_namespace_char(ch: Any) -> bool: ...
def check_anchorname_char(ch: Any) -> bool: ...
def version_tnf(t1: Any, t2: Any = None) -> Any: ...

class MutableSliceableSequence(MutableSequence, metaclass=abc.ABCMeta):
    def __getitem__(self, index: Any) -> Any: ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def __delitem__(self, index: Any) -> None: ...
    @abstractmethod
    def __getsingleitem__(self, index: Any) -> Any: ...
    @abstractmethod
    def __setsingleitem__(self, index: Any, value: Any) -> None: ...
    @abstractmethod
    def __delsingleitem__(self, index: Any) -> None: ...
