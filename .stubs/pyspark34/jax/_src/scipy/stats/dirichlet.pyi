from jax import lax as lax
from jax._src.numpy.util import promote_dtypes_inexact as promote_dtypes_inexact
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from jax.scipy.special import gammaln as gammaln, xlogy as xlogy

def logpdf(x: ArrayLike, alpha: ArrayLike) -> Array: ...
def pdf(x: ArrayLike, alpha: ArrayLike) -> Array: ...
