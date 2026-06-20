from jax import lax as lax
from jax._src.numpy.reductions import Axis as Axis
from jax._src.numpy.util import promote_args_inexact as promote_args_inexact
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from typing import Literal, overload

@overload
def logsumexp(a: ArrayLike, axis: Axis = None, b: ArrayLike | None = None, keepdims: bool = False, return_sign: Literal[False] = False) -> Array: ...
@overload
def logsumexp(a: ArrayLike, axis: Axis = None, b: ArrayLike | None = None, keepdims: bool = False, *, return_sign: Literal[True]) -> tuple[Array, Array]: ...
@overload
def logsumexp(a: ArrayLike, axis: Axis = None, b: ArrayLike | None = None, keepdims: bool = False, return_sign: bool = False) -> Array | tuple[Array, Array]: ...
