from .parse import Protocol
from .types import StrBytes
from .typing import DictStrAny
from pathlib import Path
from typing import Any, Callable, Type, TypeVar

__all__ = ['parse_file_as', 'parse_obj_as', 'parse_raw_as', 'schema_of', 'schema_json_of']

NameFactory = str | Callable[[Type[Any]], str]
T = TypeVar('T')

def parse_obj_as(type_: Type[T], obj: Any, *, type_name: NameFactory | None = None) -> T: ...
def parse_file_as(type_: Type[T], path: str | Path, *, content_type: str = None, encoding: str = 'utf8', proto: Protocol = None, allow_pickle: bool = False, json_loads: Callable[[str], Any] = ..., type_name: NameFactory | None = None) -> T: ...
def parse_raw_as(type_: Type[T], b: StrBytes, *, content_type: str = None, encoding: str = 'utf8', proto: Protocol = None, allow_pickle: bool = False, json_loads: Callable[[str], Any] = ..., type_name: NameFactory | None = None) -> T: ...
def schema_of(type_: Any, *, title: NameFactory | None = None, **schema_kwargs: Any) -> DictStrAny:
    """Generate a JSON schema (as dict) for the passed model or dynamically generated one"""
def schema_json_of(type_: Any, *, title: NameFactory | None = None, **schema_json_kwargs: Any) -> str:
    """Generate a JSON schema (as JSON) for the passed model or dynamically generated one"""
