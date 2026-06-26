from jax import lax as lax
from jax._src.numpy.util import promote_args_inexact as promote_args_inexact
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from jax.scipy.special import xlog1py as xlog1py

def logpmf(k: ArrayLike, p: ArrayLike, loc: ArrayLike = 0) -> Array: ...
def pmf(k: ArrayLike, p: ArrayLike, loc: ArrayLike = 0) -> Array: ...
