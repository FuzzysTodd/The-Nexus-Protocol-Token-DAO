from .dataclasses import Dataclass
from .main import BaseModel
from .typing import AbstractSetIntStr, IntStr, MappingIntStrAny, ReprArgs
from .version import version_info as version_info
from _typeshed import Incomplete
from pathlib import Path
from typing import Any, Callable, Collection, Dict, Generator, Iterable, Iterator, List, Set, Tuple, Type, TypeVar

__all__ = ['import_string', 'sequence_like', 'validate_field_name', 'lenient_isinstance', 'lenient_issubclass', 'in_ipython', 'is_valid_identifier', 'deep_update', 'update_not_none', 'almost_equal_floats', 'get_model', 'to_camel', 'is_valid_field', 'smart_deepcopy', 'PyObjectStr', 'Representation', 'GetterDict', 'ValueItems', 'version_info', 'ClassAttribute', 'path_type', 'ROOT_KEY', 'get_unique_discriminator_alias', 'get_discriminator_alias_and_values', 'DUNDER_ATTRIBUTES']

RichReprResult = Iterable[Any | Tuple[Any] | Tuple[str, Any] | Tuple[str, Any, Any]]
ROOT_KEY: str

def import_string(dotted_path: str) -> Any:
    """
    Stolen approximately from django. Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import fails.
    """
def sequence_like(v: Any) -> bool: ...
def validate_field_name(bases: List[Type['BaseModel']], field_name: str) -> None:
    """
    Ensure that the field's name does not shadow an existing attribute of the model.
    """
def lenient_isinstance(o: Any, class_or_tuple: Type[Any] | Tuple[Type[Any], ...] | None) -> bool: ...
def lenient_issubclass(cls, class_or_tuple: Type[Any] | Tuple[Type[Any], ...] | None) -> bool: ...
def in_ipython() -> bool:
    """
    Check whether we're in an ipython environment, including jupyter notebooks.
    """
def is_valid_identifier(identifier: str) -> bool:
    """
    Checks that a string is a valid identifier and not a Python keyword.
    :param identifier: The identifier to test.
    :return: True if the identifier is valid.
    """
KeyType = TypeVar('KeyType')

def deep_update(mapping: Dict[KeyType, Any], *updating_mappings: Dict[KeyType, Any]) -> Dict[KeyType, Any]: ...
def update_not_none(mapping: Dict[Any, Any], **update: Any) -> None: ...
def almost_equal_floats(value_1: float, value_2: float, *, delta: float = 1e-08) -> bool:
    """
    Return True if two floats are almost equal
    """
def get_model(obj: Type['BaseModel'] | Type['Dataclass']) -> Type['BaseModel']: ...
def to_camel(string: str) -> str: ...
T = TypeVar('T')

class PyObjectStr(str):
    """
    String class where repr doesn't include quotes. Useful with Representation when you want to return a string
    representation of something that valid (or pseudo-valid) python.
    """

class Representation:
    """
    Mixin to provide __str__, __repr__, and __pretty__ methods. See #884 for more details.

    __pretty__ is used by [devtools](https://python-devtools.helpmanual.io/) to provide human readable representations
    of objects.
    """
    def __repr_args__(self) -> ReprArgs:
        """
        Returns the attributes to show in __str__, __repr__, and __pretty__ this is generally overridden.

        Can either return:
        * name - value pairs, e.g.: `[('foo_name', 'foo'), ('bar_name', ['b', 'a', 'r'])]`
        * or, just values, e.g.: `[(None, 'foo'), (None, ['b', 'a', 'r'])]`
        """
    def __repr_name__(self) -> str:
        """
        Name of the instance's class, used in __repr__.
        """
    def __repr_str__(self, join_str: str) -> str: ...
    def __pretty__(self, fmt: Callable[[Any], Any], **kwargs: Any) -> Generator[Any, None, None]:
        """
        Used by devtools (https://python-devtools.helpmanual.io/) to provide a human readable representations of objects
        """
    def __rich_repr__(self) -> RichReprResult:
        """Get fields for Rich library"""

class GetterDict(Representation):
    """
    Hack to make object's smell just enough like dicts for validate_model.

    We can't inherit from Mapping[str, Any] because it upsets cython so we have to implement all methods ourselves.
    """
    def __init__(self, obj: Any) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: Any, default: Any = None) -> Any: ...
    def extra_keys(self) -> Set[Any]:
        """
        We don't want to get any other attributes of obj if the model didn't explicitly ask for them
        """
    def keys(self) -> List[Any]:
        """
        Keys of the pseudo dictionary, uses a list not set so order information can be maintained like python
        dictionaries.
        """
    def values(self) -> List[Any]: ...
    def items(self) -> Iterator[Tuple[str, Any]]: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __contains__(self, item: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __repr_args__(self) -> ReprArgs: ...
    def __repr_name__(self) -> str: ...

class ValueItems(Representation):
    """
    Class for more convenient calculation of excluded or included fields on values.
    """
    def __init__(self, value: Any, items: AbstractSetIntStr | MappingIntStrAny) -> None: ...
    def is_excluded(self, item: Any) -> bool:
        """
        Check if item is fully excluded.

        :param item: key or index of a value
        """
    def is_included(self, item: Any) -> bool:
        """
        Check if value is contained in self._items

        :param item: key or index of value
        """
    def for_element(self, e: IntStr) -> AbstractSetIntStr | MappingIntStrAny | None:
        """
        :param e: key or index of element on value
        :return: raw values for element if self._items is dict and contain needed element
        """
    @classmethod
    def merge(cls, base: Any, override: Any, intersect: bool = False) -> Any:
        '''
        Merge a ``base`` item with an ``override`` item.

        Both ``base`` and ``override`` are converted to dictionaries if possible.
        Sets are converted to dictionaries with the sets entries as keys and
        Ellipsis as values.

        Each key-value pair existing in ``base`` is merged with ``override``,
        while the rest of the key-value pairs are updated recursively with this function.

        Merging takes place based on the "union" of keys if ``intersect`` is
        set to ``False`` (default) and on the intersection of keys if
        ``intersect`` is set to ``True``.
        '''
    @staticmethod
    def is_true(v: Any) -> bool: ...
    def __repr_args__(self) -> ReprArgs: ...

class ClassAttribute:
    """
    Hide class attribute from its instances
    """
    name: Incomplete
    value: Incomplete
    def __init__(self, name: str, value: Any) -> None: ...
    def __get__(self, instance: Any, owner: Type[Any]) -> None: ...

def path_type(p: Path) -> str:
    """
    Find out what sort of thing a path is.
    """
Obj = TypeVar('Obj')

def smart_deepcopy(obj: Obj) -> Obj:
    """
    Return type as is for immutable built-in types
    Use obj.copy() for built-in empty collections
    Use copy.deepcopy() for non-empty collections and unknown objects
    """
def is_valid_field(name: str) -> bool: ...

DUNDER_ATTRIBUTES: Incomplete

def get_unique_discriminator_alias(all_aliases: Collection[str], discriminator_key: str) -> str:
    """Validate that all aliases are the same and if that's the case return the alias"""
def get_discriminator_alias_and_values(tp: Any, discriminator_key: str) -> Tuple[str, Tuple[str, ...]]:
    """
    Get alias and all valid values in the `Literal` type of the discriminator field
    `tp` can be a `BaseModel` class or directly an `Annotated` `Union` of many.
    """
