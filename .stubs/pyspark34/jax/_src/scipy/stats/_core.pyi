from _typeshed import Incomplete
from jax import jit as jit
from jax._src import dtypes as dtypes
from jax._src.api import vmap as vmap
from jax._src.numpy.util import check_arraylike as check_arraylike
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from jax._src.util import canonicalize_axis as canonicalize_axis
from typing import NamedTuple

class ModeResult(NamedTuple):
    mode: Incomplete
    count: Incomplete

def mode(a: ArrayLike, axis: int | None = 0, nan_policy: str = 'propagate', keepdims: bool = False) -> ModeResult: ...
def invert_permutation(i: Array) -> Array:
    """Helper function that inverts a permutation array."""
def rankdata(a: ArrayLike, method: str = 'average', *, axis: int | None = None, nan_policy: str = 'propagate') -> Array: ...
