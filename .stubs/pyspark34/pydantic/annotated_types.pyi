from .fields import Required as Required
from .main import BaseModel as BaseModel, create_model as create_model
from .typing import is_typeddict as is_typeddict, is_typeddict_special as is_typeddict_special
from typing import Any, NamedTuple, Type
from typing_extensions import TypedDict

def is_legacy_typeddict(typeddict_cls: Type['TypedDict']) -> bool: ...
def create_model_from_typeddict(typeddict_cls: Type['TypedDict'], **kwargs: Any) -> Type['BaseModel']:
    """
    Create a `BaseModel` based on the fields of a `TypedDict`.
    Since `typing.TypedDict` in Python 3.8 does not store runtime information about optional keys,
    we raise an error if this happens (see https://bugs.python.org/issue38834).
    """
def create_model_from_namedtuple(namedtuple_cls: Type['NamedTuple'], **kwargs: Any) -> Type['BaseModel']:
    """
    Create a `BaseModel` based on the fields of a named tuple.
    A named tuple can be created with `typing.NamedTuple` and declared annotations
    but also with `collections.namedtuple`, in this case we consider all fields
    to have type `Any`.
    """
