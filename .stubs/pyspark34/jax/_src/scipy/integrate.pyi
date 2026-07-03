from jax import jit as jit
from jax._src.numpy import util as util
from jax._src.typing import Array as Array, ArrayLike as ArrayLike

def trapezoid(y: ArrayLike, x: ArrayLike | None = None, dx: ArrayLike = 1.0, axis: int = -1) -> Array: ...
