import typing as pt
from _typeshed import Incomplete
from collections.abc import MutableSequence
from numba import njit as njit, typeof as typeof
from numba.core import cgutils as cgutils, config as config, types as types
from numba.core.dispatcher import Dispatcher as Dispatcher
from numba.core.errors import LoweringError as LoweringError, TypingError as TypingError
from numba.core.extending import NativeValue as NativeValue, box as box, overload as overload, overload_classmethod as overload_classmethod, type_callable as type_callable, unbox as unbox
from numba.core.imputils import numba_typeref_ctor as numba_typeref_ctor
from numba.core.types import ListType as ListType
from numba.core.typing.templates import Signature as Signature
from numba.typed import listobject as listobject

Int_or_Slice: Incomplete
T_co = pt.TypeVar('T_co', covariant=True)

class _Sequence(pt.Protocol[T_co]):
    def __getitem__(self, i: int) -> T_co: ...
    def __len__(self) -> int: ...

DEFAULT_ALLOCATED: Incomplete
T = pt.TypeVar('T')
T_or_ListT: Incomplete

class List(MutableSequence, pt.Generic[T]):
    """A typed-list usable in Numba compiled functions.

    Implements the MutableSequence interface.
    """
    def __new__(cls, *args, lsttype: Incomplete | None = None, meminfo: Incomplete | None = None, allocated=..., **kwargs): ...
    @classmethod
    def empty_list(cls, item_type, allocated=...):
        """Create a new empty List.

        Parameters
        ----------
        item_type: Numba type
            type of the list item.
        allocated: int
            number of items to pre-allocate
        """
    def __init__(self, *args, **kwargs) -> None:
        """
        For users, the constructor does not take any parameters.
        The keyword arguments are for internal use only.

        Parameters
        ----------
        args: iterable
            The iterable to initialize the list from
        lsttype : numba.core.types.ListType; keyword-only
            Used internally for the list type.
        meminfo : MemInfo; keyword-only
            Used internally to pass the MemInfo object when boxing.
        allocated: int; keyword-only
            Used internally to pre-allocate space for items
        """
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def append(self, item: T) -> None: ...
    @pt.overload
    def __setitem__(self, i: int, o: T) -> None: ...
    @pt.overload
    def __setitem__(self, s: slice, o: List[T]) -> None: ...
    @pt.overload
    def __getitem__(self, i: int) -> T: ...
    @pt.overload
    def __getitem__(self, i: slice) -> List[T]: ...
    def __iter__(self) -> pt.Iterator[T]: ...
    def __contains__(self, item: T) -> bool: ...
    def __delitem__(self, i: Int_or_Slice) -> None: ...
    def insert(self, i: int, item: T) -> None: ...
    def count(self, item: T) -> int: ...
    def pop(self, i: pt.SupportsIndex = -1) -> T: ...
    def extend(self, iterable: _Sequence[T]) -> None: ...
    def remove(self, item: T) -> None: ...
    def clear(self): ...
    def reverse(self): ...
    def copy(self): ...
    def index(self, item: T, start: int | None = None, stop: int | None = None) -> int: ...
    def sort(self, key: Incomplete | None = None, reverse: bool = False):
        """Sort the list inplace.

        See also ``list.sort()``
        """

def typedlist_empty(cls, item_type, allocated=...): ...
def box_lsttype(typ, val, c): ...
def unbox_listtype(typ, val, c): ...
def typedlist_call(context):
    """Defines typing logic for ``List()`` and ``List(iterable)``.

    If no argument is given, the returned typer types a new typed-list with an
    undefined item type. If a single argument is given it must be iterable with
    a guessable 'dtype'. In this case, the typer types a new typed-list with
    the type set to the 'dtype' of the iterable arg.

    Parameters
    ----------
    arg : single iterable (optional)
        The single optional argument.

    Returns
    -------
    typer : function
        A typer suitable to type constructor calls.

    Raises
    ------
    The returned typer raises a TypingError in case of unsuitable arguments.

    """
def impl_numba_typeref_ctor(cls, *args):
    """Defines lowering for ``List()`` and ``List(iterable)``.

    This defines the lowering logic to instantiate either an empty typed-list
    or a typed-list initialised with values from a single iterable argument.

    Parameters
    ----------
    cls : TypeRef
        Expecting a TypeRef of a precise ListType.
    args: tuple
        A tuple that contains a single iterable (optional)

    Returns
    -------
    impl : function
        An implementation suitable for lowering the constructor call.

    See also: `redirect_type_ctor` in numba/cpython/bulitins.py
    """
