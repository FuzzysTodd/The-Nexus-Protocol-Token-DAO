from _typeshed import Incomplete
from collections.abc import Generator, Hashable, Iterable
from typing import Any, Generic, TypeVar, overload

__version__: str
K = TypeVar('K', bound=Hashable)
L = TypeVar('L', bound=Hashable)
V = TypeVar('V')
U = TypeVar('U')

def concat(left: Cycler[K, V], right: Cycler[K, U]) -> Cycler[K, V | U]:
    """
    Concatenate `Cycler`\\s, as if chained using `itertools.chain`.

    The keys must match exactly.

    Examples
    --------
    >>> num = cycler('a', range(3))
    >>> let = cycler('a', 'abc')
    >>> num.concat(let)
    cycler('a', [0, 1, 2, 'a', 'b', 'c'])

    Returns
    -------
    `Cycler`
        The concatenated cycler.
    """

class Cycler(Generic[K, V]):
    """
    Composable cycles.

    This class has compositions methods:

    ``+``
      for 'inner' products (zip)

    ``+=``
      in-place ``+``

    ``*``
      for outer products (`itertools.product`) and integer multiplication

    ``*=``
      in-place ``*``

    and supports basic slicing via ``[]``.

    Parameters
    ----------
    left, right : Cycler or None
        The 'left' and 'right' cyclers.
    op : func or None
        Function which composes the 'left' and 'right' cyclers.
    """
    def __call__(self): ...
    def __init__(self, left: Cycler[K, V] | Iterable[dict[K, V]] | None, right: Cycler[K, V] | None = None, op: Any = None) -> None:
        """
        Semi-private init.

        Do not use this directly, use `cycler` function instead.
        """
    def __contains__(self, k) -> bool: ...
    @property
    def keys(self) -> set[K]:
        """The keys this Cycler knows about."""
    def change_key(self, old: K, new: K) -> None:
        """
        Change a key in this cycler to a new name.
        Modification is performed in-place.

        Does nothing if the old key is the same as the new key.
        Raises a ValueError if the new key is already a key.
        Raises a KeyError if the old key isn't a key.
        """
    def __getitem__(self, key: slice) -> Cycler[K, V]: ...
    def __iter__(self) -> Generator[dict[K, V], None, None]: ...
    def __add__(self, other: Cycler[L, U]) -> Cycler[K | L, V | U]:
        """
        Pair-wise combine two equal length cyclers (zip).

        Parameters
        ----------
        other : Cycler
        """
    @overload
    def __mul__(self, other: Cycler[L, U]) -> Cycler[K | L, V | U]: ...
    @overload
    def __mul__(self, other: int) -> Cycler[K, V]: ...
    @overload
    def __rmul__(self, other: Cycler[L, U]) -> Cycler[K | L, V | U]: ...
    @overload
    def __rmul__(self, other: int) -> Cycler[K, V]: ...
    def __len__(self) -> int: ...
    def __iadd__(self, other: Cycler[K, V]) -> Cycler[K, V]:
        """
        In-place pair-wise combine two equal length cyclers (zip).

        Parameters
        ----------
        other : Cycler
        """
    def __imul__(self, other: Cycler[K, V] | int) -> Cycler[K, V]:
        """
        In-place outer product of two cyclers (`itertools.product`).

        Parameters
        ----------
        other : Cycler
        """
    def __eq__(self, other: object) -> bool: ...
    __hash__: Incomplete
    def by_key(self) -> dict[K, list[V]]:
        """
        Values by key.

        This returns the transposed values of the cycler.  Iterating
        over a `Cycler` yields dicts with a single value for each key,
        this method returns a `dict` of `list` which are the values
        for the given key.

        The returned value can be used to create an equivalent `Cycler`
        using only `+`.

        Returns
        -------
        transpose : dict
            dict of lists of the values for each key.
        """
    def simplify(self) -> Cycler[K, V]:
        """
        Simplify the cycler into a sum (but no products) of cyclers.

        Returns
        -------
        simple : Cycler
        """
    concat = concat

@overload
def cycler(arg: Cycler[K, V]) -> Cycler[K, V]: ...
@overload
def cycler(**kwargs: Iterable[V]) -> Cycler[str, V]: ...
@overload
def cycler(label: K, itr: Iterable[V]) -> Cycler[K, V]: ...
