import jax
from _typeshed import Incomplete
from jax._src.numpy import reductions as reductions
from jax._src.numpy.lax_numpy import append as append, take as take
from jax._src.numpy.util import check_arraylike as check_arraylike
from jax._src.numpy.vectorize import vectorize as vectorize
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DTypeLike as DTypeLike
from jax._src.util import canonicalize_axis as canonicalize_axis, set_module as set_module
from typing import Any, Callable

def get_if_single_primitive(fun: Callable[..., Any], *args: Any) -> jax.core.Primitive | None:
    """
  If fun(*args) lowers to a single primitive with inputs and outputs matching
  function inputs and outputs, return that primitive. Otherwise return None.
  """

class ufunc:
    """Functions that operate element-by-element on whole arrays.

  This is a class for LAX-backed implementations of numpy ufuncs.
  """
    __doc__: Incomplete
    def __init__(self, func: Callable[..., Any], nin: int, nout: int, *, name: str | None = None, nargs: int | None = None, identity: Any = None, update_doc: bool = False) -> None: ...
    nin: Incomplete
    nout: Incomplete
    nargs: Incomplete
    identity: Incomplete
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __call__(self, *args: ArrayLike, out: None = None, where: None = None, **kwargs: Any) -> Any: ...
    def reduce(self, a: ArrayLike, axis: int = 0, dtype: DTypeLike | None = None, out: None = None, keepdims: bool = False, initial: ArrayLike | None = None, where: ArrayLike | None = None) -> Array: ...
    def accumulate(self, a: ArrayLike, axis: int = 0, dtype: DTypeLike | None = None, out: None = None) -> Array: ...
    def at(self, a: ArrayLike, indices: Any, b: ArrayLike | None = None, *, inplace: bool = True) -> Array: ...
    def reduceat(self, a: ArrayLike, indices: Any, axis: int = 0, dtype: DTypeLike | None = None, out: None = None) -> Array: ...
    def outer(self, A: ArrayLike, B: ArrayLike, **kwargs) -> Array: ...

def frompyfunc(func: Callable[..., Any], nin: int, nout: int, *, identity: Any = None) -> ufunc:
    """Create a JAX ufunc from an arbitrary JAX-compatible scalar function.

  Args:
    func : a callable that takes `nin` scalar arguments and return `nout` outputs.
    nin: integer specifying the number of scalar inputs
    nout: integer specifying the number of scalar outputs
    identity: (optional) a scalar specifying the identity of the operation, if any.

  Returns:
    wrapped : jax.numpy.ufunc wrapper of func.
  """
