import abc
from _typeshed import Incomplete
from abc import abstractmethod
from typing import Any, AnyStr, List, Tuple

class AtomicSlicer:
    """ Wrapping object that will unify slicing across data structures.

    What we support:
        Basic indexing (return references):
        - (start:stop:step) slicing
        - support ellipses
        Advanced indexing (return references):
        - integer array indexing

    Numpy Reference:
        Basic indexing (return views):
        - (start:stop:step) slicing
        - support ellipses and newaxis (alias for None)
        Advanced indexing (return copy):
        - integer array indexing, i.e. X[[1,2], [3,4]]
        - boolean array indexing
        - mixed array indexing (has integer array, ellipses, newaxis in same slice)
    """
    o: Incomplete
    max_dim: Incomplete
    def __init__(self, o: Any, max_dim: None | int | AnyStr = 'auto') -> None:
        ''' Provides a consistent slicing API to the object provided.

        Args:
            o: Object to enable consistent slicing.
                Currently supports numpy dense arrays, recursive lists ending with list or numpy.
            max_dim: Max number of dimensions the wrapped object has.
                If set to "auto", max dimensions will be inferred. This comes at compute cost.
        '''
    def __getitem__(self, item: Any) -> Any:
        """ Consistent slicing into wrapped object.

        Args:
            item: Slicing key of type integer or slice.

        Returns:
            Sliced object.

        Raises:
            ValueError: If slicing is not compatible with wrapped object.
        """

def unify_slice(item: Any, max_dim: int, alias_lookup: Incomplete | None = None) -> Tuple:
    """ Resolves aliases and ellipses in a slice item.

    Args:
        item: Slicing key that is passed to __getitem__.
        max_dim: Max dimension of object to be sliced.
        alias_lookup: AliasLookup structure.

    Returns:
        A tuple representation of the item.
    """

class Tracked(AtomicSlicer):
    """ Tracked defines an object that slicer wraps."""
    dim: Incomplete
    def __init__(self, o: Any, dim: int | List | tuple | None | str = 'auto') -> None:
        """ Defines an object that will be wrapped by slicer.

        Args:
            o: Object that will be tracked for slicer.
            dim: Target dimension(s) slicer will index on for this object.
        """

class Obj(Tracked):
    """ An object that slicer wraps. """
    def __init__(self, o, dim: str = 'auto') -> None: ...

class Alias(Tracked):
    """ Defines a tracked object as well as additional __getitem__ keys. """
    def __init__(self, o, dim) -> None: ...

class AliasLookup:
    def __init__(self, aliases) -> None: ...
    def update(self, alias) -> None: ...
    def delete(self, alias) -> None:
        """Delete an alias that exists from lookup"""
    def get(self, dim, target, default: Incomplete | None = None): ...

def resolve_dim(slicer_index: Tuple, slicer_dim: List) -> List:
    """ Extracts new dim after applying slicing index and maps it back to the original index list. """
def reduced_o(tracked: Tracked) -> List | Any: ...

class BaseHandler(metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def head_slice(cls, o, index_tup, max_dim): ...
    @classmethod
    @abstractmethod
    def tail_slice(cls, o, tail_index, max_dim, flatten: bool = True): ...
    @classmethod
    @abstractmethod
    def max_dim(cls, o): ...
    @classmethod
    def default_alias(cls, o): ...

class SeriesHandler(BaseHandler):
    @classmethod
    def head_slice(cls, o, index_tup, max_dim): ...
    @classmethod
    def tail_slice(cls, o, tail_index, max_dim, flatten: bool = True): ...
    @classmethod
    def max_dim(cls, o): ...
    @classmethod
    def default_alias(cls, o): ...

class DataFrameHandler(BaseHandler):
    @classmethod
    def head_slice(cls, o, index_tup, max_dim): ...
    @classmethod
    def tail_slice(cls, o, tail_index, max_dim, flatten: bool = True): ...
    @classmethod
    def max_dim(cls, o): ...
    @classmethod
    def default_alias(cls, o): ...

class ArrayHandler(BaseHandler):
    @classmethod
    def head_slice(cls, o, index_tup, max_dim): ...
    @classmethod
    def tail_slice(cls, o, tail_index, max_dim, flatten: bool = True): ...
    @classmethod
    def max_dim(cls, o): ...

class DictHandler(BaseHandler):
    @classmethod
    def head_slice(cls, o, index_tup, max_dim): ...
    @classmethod
    def tail_slice(cls, o, tail_index, max_dim, flatten: bool = True): ...
    @classmethod
    def max_dim(cls, o): ...

class ListTupleHandler(BaseHandler):
    @classmethod
    def head_slice(cls, o, index_tup, max_dim): ...
    @classmethod
    def tail_slice(cls, o, tail_index, max_dim, flatten: bool = True): ...
    @classmethod
    def max_dim(cls, o): ...

class UnifiedDataHandler:
    """ Registry that maps types to their unified slice calls."""
    type_map: Incomplete
    @classmethod
    def slice(cls, o, index_tup, max_dim): ...
    @classmethod
    def max_dim(cls, o): ...
    @classmethod
    def default_alias(cls, o): ...
