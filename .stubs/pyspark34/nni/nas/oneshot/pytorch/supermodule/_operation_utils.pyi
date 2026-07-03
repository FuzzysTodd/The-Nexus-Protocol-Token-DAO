from _typeshed import Incomplete
from typing import Any, Callable, Dict, Generic, Iterator, List, Tuple, TypeVar

__all__ = ['slice_type', 'multidim_slice', 'scalar_or_scalar_dict', 'int_or_int_dict', 'zeros_like', 'Slicable', 'MaybeWeighted']

T = TypeVar('T')
slice_type = slice | List[slice]
multidim_slice = Tuple[slice_type, ...]
scalar_or_scalar_dict = T | Dict[T, float]
int_or_int_dict = scalar_or_scalar_dict[int]

def zeros_like(arr: T) -> T: ...

class Slicable(Generic[T]):
    """Wraps the weight so that in can be sliced with a ``multidim_slice``.
    The value within the slice can be instances of :class:`MaybeWeighted`.

    Examples
    --------
    >>> weight = conv2d.weight
    >>> Slicable(weight)[:MaybeWeighted({32: 0.4, 64: 0.6})]
    Tensor of shape (64, 64, 3, 3)
    """
    weight: Incomplete
    def __init__(self, weight: T) -> None: ...
    def __getitem__(self, index: slice_type | multidim_slice | Any) -> T: ...

class MaybeWeighted:
    """Wrap a value (int or dict with int keys), so that the computation on it can be replayed.
    It builds a binary tree. If ``value`` is not None, it's a leaf node.
    Otherwise, it has left sub-tree and right sub-tree and an operation.

    Only support basic arithmetic operations: ``+``, ``-``, ``*``, ``//``.
    """
    value: Incomplete
    lhs: Incomplete
    rhs: Incomplete
    operation: Incomplete
    def __init__(self, value: int_or_int_dict | None = None, *, lhs: MaybeWeighted | int | None = None, rhs: MaybeWeighted | int | None = None, operation: Callable[[int_or_int_dict, int_or_int_dict], int_or_int_dict] | None = None) -> None: ...
    def leaf_values(self) -> Iterator[int_or_int_dict]:
        """Iterate over values on leaf nodes."""
    def evaluate(self, value_fn: _value_fn_type = None) -> int_or_int_dict:
        """Evaluate the value on root node, after replacing every value on leaf node with ``value_fn``.
        If ``value_fn`` is none, no replacement will happen and the raw value will be used.
        """
    def __add__(self, other: Any) -> MaybeWeighted: ...
    def __radd__(self, other: Any) -> MaybeWeighted: ...
    def __sub__(self, other: Any) -> MaybeWeighted: ...
    def __rsub__(self, other: Any) -> MaybeWeighted: ...
    def __mul__(self, other: Any) -> MaybeWeighted: ...
    def __rmul__(self, other: Any) -> MaybeWeighted: ...
    def __floordiv__(self, other: Any) -> MaybeWeighted: ...
    def __rfloordiv__(self, other: Any) -> MaybeWeighted: ...
