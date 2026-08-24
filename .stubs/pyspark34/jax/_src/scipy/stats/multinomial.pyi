from jax import lax as lax
from jax._src.numpy.util import promote_args_inexact as promote_args_inexact, promote_args_numeric as promote_args_numeric
from jax._src.scipy.special import gammaln as gammaln, xlogy as xlogy
from jax._src.typing import Array as Array, ArrayLike as ArrayLike

def logpmf(x: ArrayLike, n: ArrayLike, p: ArrayLike) -> Array:
    """JAX implementation of scipy.stats.multinomial.logpmf."""
def pmf(x: ArrayLike, n: ArrayLike, p: ArrayLike) -> Array:
    """JAX implementation of scipy.stats.multinomial.pmf."""
