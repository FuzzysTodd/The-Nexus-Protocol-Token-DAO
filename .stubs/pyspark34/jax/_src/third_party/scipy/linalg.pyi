from jax import jit as jit, lax as lax
from jax._src.numpy.linalg import norm as norm
from jax._src.scipy.linalg import rsf2csf as rsf2csf, schur as schur
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from typing import Callable

def funm(A: ArrayLike, func: Callable[[Array], Array], disp: bool = True) -> Array | tuple[Array, Array]: ...
