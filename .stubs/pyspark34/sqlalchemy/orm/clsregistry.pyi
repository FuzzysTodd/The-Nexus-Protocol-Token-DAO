import weakref
from . import attributes as attributes, interfaces as interfaces
from .. import exc as exc, inspection as inspection, util as util
from ..sql.schema import MetaData as MetaData, Table as Table
from ..util.typing import CallableReference as CallableReference
from .descriptor_props import SynonymProperty as SynonymProperty
from .properties import ColumnProperty as ColumnProperty
from .relationships import RelationshipProperty as RelationshipProperty
from .util import class_mapper as class_mapper
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Generator, Iterable, List, Mapping, Set, Type

def add_class(classname: str, cls: Type[_T], decl_class_registry: _ClsRegistryType) -> None:
    """Add a class to the _decl_class_registry associated with the
    given declarative class.

    """
def remove_class(classname: str, cls: Type[Any], decl_class_registry: _ClsRegistryType) -> None: ...

class ClsRegistryToken:
    """an object that can be in the registry._class_registry as a value."""

class _MultipleClassMarker(ClsRegistryToken):
    """refers to multiple classes of the same name
    within _decl_class_registry.

    """
    contents: Set[weakref.ref[Type[Any]]]
    on_remove: CallableReference[Callable[[], None] | None]
    def __init__(self, classes: Iterable[Type[Any]], on_remove: Callable[[], None] | None = None) -> None: ...
    def remove_item(self, cls: Type[Any]) -> None: ...
    def __iter__(self) -> Generator[Type[Any] | None, None, None]: ...
    def attempt_get(self, path: List[str], key: str) -> Type[Any]: ...
    def add_item(self, item: Type[Any]) -> None: ...

class _ModuleMarker(ClsRegistryToken):
    """Refers to a module name within
    _decl_class_registry.

    """
    parent: _ModuleMarker | None
    contents: Dict[str, _ModuleMarker | _MultipleClassMarker]
    mod_ns: _ModNS
    path: List[str]
    name: Incomplete
    def __init__(self, name: str, parent: _ModuleMarker | None) -> None: ...
    def __contains__(self, name: str) -> bool: ...
    def __getitem__(self, name: str) -> ClsRegistryToken: ...
    def resolve_attr(self, key: str) -> _ModNS | Type[Any]: ...
    def get_module(self, name: str) -> _ModuleMarker: ...
    def add_class(self, name: str, cls: Type[Any]) -> None: ...
    def remove_class(self, name: str, cls: Type[Any]) -> None: ...

class _ModNS:
    def __init__(self, parent: _ModuleMarker) -> None: ...
    def __getattr__(self, key: str) -> _ModNS | Type[Any]: ...

class _GetColumns:
    cls: Type[Any]
    def __init__(self, cls: Type[Any]) -> None: ...
    def __getattr__(self, key: str) -> Any: ...

class _GetTable:
    key: str
    metadata: MetaData
    def __init__(self, key: str, metadata: MetaData) -> None: ...
    def __getattr__(self, key: str) -> Table: ...

class _class_resolver:
    cls: Type[Any]
    prop: RelationshipProperty[Any]
    fallback: Mapping[str, Any]
    arg: str
    favor_tables: bool
    def __init__(self, cls: Type[Any], prop: RelationshipProperty[Any], fallback: Mapping[str, Any], arg: str, favor_tables: bool = False) -> None: ...
    def __call__(self) -> Any: ...
