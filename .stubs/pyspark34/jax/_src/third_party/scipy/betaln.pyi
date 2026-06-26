from jax import lax as lax
from jax._src.numpy.util import promote_args_inexact as promote_args_inexact
from jax._src.typing import Array as Array, ArrayLike as ArrayLike

def algdiv(a, b):
    """
    Compute ``log(gamma(a))/log(gamma(a + b))`` when ``b >= 8``.

    Derived from scipy's implementation of `algdiv`_.

    This differs from the scipy implementation in that it assumes a <= b
    because recomputing ``a, b = jnp.minimum(a, b), jnp.maximum(a, b)`` might
    be expensive and this is only called by ``betaln``.

    .. _algdiv:
        https://github.com/scipy/scipy/blob/c89dfc2b90d993f2a8174e57e0cbc8fbe6f3ee19/scipy/special/cdflib/algdiv.f
    """
def betaln(a: ArrayLike, b: ArrayLike) -> Array:
    """Compute the log of the beta function.

    Derived from scipy's implementation of `betaln`_.

    This implementation does not handle all branches of the scipy implementation, but is still much more accurate
    than just doing lgamma(a) + lgamma(b) - lgamma(a + b) when inputs are large (> 1M or so).

    .. _betaln:
        https://github.com/scipy/scipy/blob/ef2dee592ba8fb900ff2308b9d1c79e4d6a0ad8b/scipy/special/cdflib/betaln.f
    """
