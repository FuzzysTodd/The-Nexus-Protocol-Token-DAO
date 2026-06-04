import types
import typing
from ._has_cy import HAS_CYEXTENSION as HAS_CYEXTENSION
from ._py_collections import IdentitySet as IdentitySet, ImmutableDictBase as ImmutableDictBase, OrderedSet as OrderedSet, ReadOnlyContainer as ReadOnlyContainer, immutabledict as immutabledict
from .typing import Literal as Literal, Protocol as Protocol
from _typeshed import Incomplete
from typing import Any, Callable, Dict, FrozenSet, Generic, Iterable, Iterator, List, Mapping, NoReturn, Sequence, Set, Tuple, ValuesView, overload

EMPTY_SET: FrozenSet[Any]
NONE_SET: FrozenSet[Any]

def merge_lists_w_ordering(a: List[Any], b: List[Any]) -> List[Any]:
    '''merge two lists, maintaining ordering as much as possible.

    this is to reconcile vars(cls) with cls.__annotations__.

    Example::

        >>> a = [\'__tablename__\', \'id\', \'x\', \'created_at\']
        >>> b = [\'id\', \'name\', \'data\', \'y\', \'created_at\']
        >>> merge_lists_w_ordering(a, b)
        [\'__tablename__\', \'id\', \'name\', \'data\', \'y\', \'x\', \'created_at\']

    This is not necessarily the ordering that things had on the class,
    in this case the class is::

        class User(Base):
            __tablename__ = "users"

            id: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str]
            data: Mapped[Optional[str]]
            x = Column(Integer)
            y: Mapped[int]
            created_at: Mapped[datetime.datetime] = mapped_column()

    But things are *mostly* ordered.

    The algorithm could also be done by creating a partial ordering for
    all items in both lists and then using topological_sort(), but that
    is too much overhead.

    Background on how I came up with this is at:
    https://gist.github.com/zzzeek/89de958cf0803d148e74861bd682ebae

    '''
def coerce_to_immutabledict(d: Mapping[_KT, _VT]) -> immutabledict[_KT, _VT]: ...

EMPTY_DICT: immutabledict[Any, Any]

class FacadeDict(ImmutableDictBase[_KT, _VT]):
    """A dictionary that is not publicly mutable."""
    def __new__(cls, *args: Any) -> FacadeDict[Any, Any]: ...
    def copy(self) -> NoReturn: ...
    def __reduce__(self) -> Any: ...

class Properties(Generic[_T]):
    """Provide a __getattr__/__setattr__ interface over a dict."""
    def __init__(self, data: Dict[str, _T]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __dir__(self) -> List[str]: ...
    def __add__(self, other: Properties[_F]) -> List[_T | _F]: ...
    def __setitem__(self, key: str, obj: _T) -> None: ...
    def __getitem__(self, key: str) -> _T: ...
    def __delitem__(self, key: str) -> None: ...
    def __setattr__(self, key: str, obj: _T) -> None: ...
    def __getattr__(self, key: str) -> _T: ...
    def __contains__(self, key: str) -> bool: ...
    def as_readonly(self) -> ReadOnlyProperties[_T]:
        """Return an immutable proxy for this :class:`.Properties`."""
    def update(self, value: Dict[str, _T]) -> None: ...
    @overload
    def get(self, key: str) -> _T | None: ...
    @overload
    def get(self, key: str, default: _DT | _T) -> _DT | _T: ...
    def keys(self) -> List[str]: ...
    def values(self) -> List[_T]: ...
    def items(self) -> List[Tuple[str, _T]]: ...
    def has_key(self, key: str) -> bool: ...
    def clear(self) -> None: ...

class OrderedProperties(Properties[_T]):
    """Provide a __getattr__/__setattr__ interface with an OrderedDict
    as backing store."""
    def __init__(self) -> None: ...

class ReadOnlyProperties(ReadOnlyContainer, Properties[_T]):
    """Provide immutable dict/object attribute to an underlying dictionary."""
OrderedDict = dict
sort_dictionary: Incomplete

class WeakSequence(Sequence[_T]):
    def __init__(self, __elements: Sequence[_T] = ()) -> None: ...
    def append(self, item) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, index): ...

class OrderedIdentitySet(IdentitySet):
    def __init__(self, iterable: Iterable[Any] | None = None) -> None: ...

class PopulateDict(Dict[_KT, _VT]):
    """A dict which populates missing values via a creation function.

    Note the creation function takes a key, unlike
    collections.defaultdict.

    """
    creator: Incomplete
    def __init__(self, creator: Callable[[_KT], _VT]) -> None: ...
    def __missing__(self, key: Any) -> Any: ...

class WeakPopulateDict(Dict[_KT, _VT]):
    """Like PopulateDict, but assumes a self + a method and does not create
    a reference cycle.

    """
    creator: Incomplete
    weakself: Incomplete
    def __init__(self, creator_method: types.MethodType) -> None: ...
    def __missing__(self, key: Any) -> Any: ...
column_set = set
column_dict = dict
ordered_column_set = OrderedSet

class UniqueAppender(Generic[_T]):
    """Appends items to a collection ensuring uniqueness.

    Additional appends() of the same object are ignored.  Membership is
    determined by identity (``is a``) not equality (``==``).
    """
    data: Iterable[_T] | Set[_T] | List[_T]
    def __init__(self, data: Iterable[_T] | Set[_T] | List[_T], via: str | None = None) -> None: ...
    def append(self, item: _T) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...

def coerce_generator_arg(arg: Any) -> List[Any]: ...
def to_list(x: Any, default: List[Any] | None = None) -> List[Any]: ...
def has_intersection(set_, iterable):
    """return True if any items of set\\_ are present in iterable.

    Goes through special effort to ensure __hash__ is not called
    on items in iterable that don't support it.

    """
def to_set(x): ...
def to_column_set(x: Any) -> Set[Any]: ...
def update_copy(d, _new: Incomplete | None = None, **kw):
    """Copy the given dict and update with the given values."""
def flatten_iterator(x: Iterable[_T]) -> Iterator[_T]:
    """Given an iterator of which further sub-elements may also be
    iterators, flatten the sub-elements into a single iterator.

    """

class LRUCache(typing.MutableMapping[_KT, _VT]):
    '''Dictionary with \'squishy\' removal of least
    recently used items.

    Note that either get() or [] should be used here, but
    generally its not safe to do an "in" check first as the dictionary
    can change subsequent to that call.

    '''
    capacity: int
    threshold: float
    size_alert: Callable[[LRUCache[_KT, _VT]], None] | None
    def __init__(self, capacity: int = 100, threshold: float = 0.5, size_alert: Callable[..., None] | None = None) -> None: ...
    @overload
    def get(self, key: _KT) -> _VT | None: ...
    @overload
    def get(self, key: _KT, default: _VT | _T) -> _VT | _T: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...
    def values(self) -> ValuesView[_VT]: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, __v: _KT) -> None: ...
    @property
    def size_threshold(self) -> float: ...

class _CreateFuncType(Protocol[_T_co]):
    def __call__(self) -> _T_co: ...

class _ScopeFuncType(Protocol):
    def __call__(self) -> Any: ...

class ScopedRegistry(Generic[_T]):
    '''A Registry that can store one or multiple instances of a single
    class on the basis of a "scope" function.

    The object implements ``__call__`` as the "getter", so by
    calling ``myregistry()`` the contained object is returned
    for the current scope.

    :param createfunc:
      a callable that returns a new object to be placed in the registry

    :param scopefunc:
      a callable that will return a key to store/retrieve an object.
    '''
    createfunc: _CreateFuncType[_T]
    scopefunc: _ScopeFuncType
    registry: Any
    def __init__(self, createfunc: Callable[[], _T], scopefunc: Callable[[], Any]) -> None:
        """Construct a new :class:`.ScopedRegistry`.

        :param createfunc:  A creation function that will generate
          a new value for the current scope, if none is present.

        :param scopefunc:  A function that returns a hashable
          token representing the current scope (such as, current
          thread identifier).

        """
    def __call__(self) -> _T: ...
    def has(self) -> bool:
        """Return True if an object is present in the current scope."""
    def set(self, obj: _T) -> None:
        """Set the value for the current scope."""
    def clear(self) -> None:
        """Clear the current scope, if any."""

class ThreadLocalRegistry(ScopedRegistry[_T]):
    """A :class:`.ScopedRegistry` that uses a ``threading.local()``
    variable for storage.

    """
    createfunc: Incomplete
    registry: Incomplete
    def __init__(self, createfunc: Callable[[], _T]) -> None: ...
    def __call__(self) -> _T: ...
    def has(self) -> bool: ...
    def set(self, obj: _T) -> None: ...
    def clear(self) -> None: ...

def has_dupes(sequence, target):
    """Given a sequence and search object, return True if there's more
    than one, False if zero or one of them.


    """
