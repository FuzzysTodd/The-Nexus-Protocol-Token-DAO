import abc
import numbers
from _typeshed import Incomplete
from abc import ABCMeta
from torch.utils.data.datapipes._hook_iterator import hook_iterator as hook_iterator
from typing import TypeVar

class GenericMeta(ABCMeta): ...
class Integer(numbers.Integral, metaclass=abc.ABCMeta): ...
class Boolean(numbers.Integral, metaclass=abc.ABCMeta): ...

TYPE2ABC: Incomplete

def issubtype(left, right, recursive: bool = True):
    """
    Check if the left-side type is a subtype of the right-side type.
    If any of type is a composite type like `Union` and `TypeVar` with
    bounds, it would be expanded into a list of types and check all
    of left-side types are subtypes of either one from right-side types.
    """
def issubinstance(data, data_type): ...

class _DataPipeType:
    """
    Save type annotation in `param`
    """
    param: Incomplete
    def __init__(self, param) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def issubtype(self, other): ...
    def issubtype_of_instance(self, other): ...
T_co = TypeVar('T_co', covariant=True)

class _DataPipeMeta(GenericMeta):
    """
    Metaclass for `DataPipe`. Add `type` attribute and `__init_subclass__` based
    on the type, and validate the return hint of `__iter__`.

    Note that there is subclass `_IterDataPipeMeta` specifically for `IterDataPipe`.
    """
    type: _DataPipeType
    def __new__(cls, name, bases, namespace, **kwargs): ...
    def __init__(self, name, bases, namespace, **kwargs) -> None: ...

class _IterDataPipeMeta(_DataPipeMeta):
    """
    Metaclass for `IterDataPipe` and inherits from `_DataPipeMeta`. Aad various functions for behaviors
    specific to `IterDataPipe`.
    """
    def __new__(cls, name, bases, namespace, **kwargs): ...

def reinforce_type(self, expected_type):
    """
    Reinforce the type for DataPipe instance. And the 'expected_type' is required
    to be a subtype of the original type hint to restrict the type requirement
    of DataPipe instance.
    """
