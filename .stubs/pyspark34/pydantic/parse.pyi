from .types import StrBytes as StrBytes
from enum import Enum
from pathlib import Path
from typing import Any, Callable

class Protocol(str, Enum):
    json: str
    pickle: str

def load_str_bytes(b: StrBytes, *, content_type: str = None, encoding: str = 'utf8', proto: Protocol = None, allow_pickle: bool = False, json_loads: Callable[[str], Any] = ...) -> Any: ...
def load_file(path: str | Path, *, content_type: str = None, encoding: str = 'utf8', proto: Protocol = None, allow_pickle: bool = False, json_loads: Callable[[str], Any] = ...) -> Any: ...
