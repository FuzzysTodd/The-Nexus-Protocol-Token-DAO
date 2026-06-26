from _typeshed import Incomplete
from enum import Enum
from jax._src import dtypes as dtypes
from jax._src.interpreters import ad as ad, mlir as mlir
from jax._src.lax.control_flow import while_loop as while_loop
from jax._src.lax.lax import add as add, bitwise_and as bitwise_and, bitwise_not as bitwise_not, bitwise_or as bitwise_or, broadcast_in_dim as broadcast_in_dim, broadcast_shapes as broadcast_shapes, convert_element_type as convert_element_type, div as div, eq as eq, exp as exp, full_like as full_like, ge as ge, gt as gt, le as le, log as log, log1p as log1p, lt as lt, mul as mul, ne as ne, neg as neg, reciprocal as reciprocal, reduce as reduce, select as select, sign as sign, sqrt as sqrt, square as square, standard_naryop as standard_naryop, standard_unop as standard_unop, sub as sub
from jax._src.lib.mlir.dialects import chlo as chlo
from jax._src.typing import Array as Array, ArrayLike as ArrayLike

def betainc(a: ArrayLike, b: ArrayLike, x: ArrayLike) -> Array:
    """Elementwise regularized incomplete beta integral."""
def lgamma(x: ArrayLike) -> Array:
    """Elementwise log gamma: :math:`\\mathrm{log}(\\Gamma(x))`."""
def digamma(x: ArrayLike) -> Array:
    """Elementwise digamma: :math:`\\psi(x)`."""
def polygamma(m: ArrayLike, x: ArrayLike) -> Array:
    """Elementwise polygamma: :math:`\\psi^{(m)}(x)`."""
def igamma(a: ArrayLike, x: ArrayLike) -> Array:
    """Elementwise regularized incomplete gamma function."""
def igammac(a: ArrayLike, x: ArrayLike) -> Array:
    """Elementwise complementary regularized incomplete gamma function."""
def igamma_grad_a(a: ArrayLike, x: ArrayLike) -> Array:
    """Elementwise derivative of the regularized incomplete gamma function."""
def random_gamma_grad(a: ArrayLike, x: ArrayLike) -> Array:
    """Elementwise derivative of samples from `Gamma(a, 1)`."""
def zeta(x: ArrayLike, q: ArrayLike) -> Array:
    """Elementwise Hurwitz zeta function: :math:`\\zeta(x, q)`"""
def bessel_i0e(x: ArrayLike) -> Array:
    """Exponentially scaled modified Bessel function of order 0:
  :math:`\\mathrm{i0e}(x) = e^{-|x|} \\mathrm{i0}(x)`
  """
def bessel_i1e(x: ArrayLike) -> Array:
    """Exponentially scaled modified Bessel function of order 1:
  :math:`\\mathrm{i1e}(x) = e^{-|x|} \\mathrm{i1}(x)`
  """
def erf(x: ArrayLike) -> Array:
    """Elementwise error function: :math:`\\mathrm{erf}(x)`."""
def erfc(x: ArrayLike) -> Array:
    """Elementwise complementary error function:
    :math:`\\mathrm{erfc}(x) = 1 - \\mathrm{erf}(x)`."""
def erf_inv(x: ArrayLike) -> Array:
    """Elementwise inverse error function: :math:`\\mathrm{erf}^{-1}(x)`."""
def betainc_gradx(g, a, b, x): ...
def betainc_grad_not_implemented(g, a, b, x) -> None: ...
def igamma_gradx(g, a, x): ...
def igamma_grada(g, a, x): ...
def igammac_gradx(g, a, x): ...
def igammac_grada(g, a, x): ...
def polygamma_gradm(g, m, x) -> None: ...
def polygamma_gradx(g, m, x): ...
def lentz_thompson_barnett_algorithm(*, num_iterations, small, threshold, nth_partial_numerator, nth_partial_denominator, inputs): ...
def regularized_incomplete_beta_impl(a, b, x, *, dtype): ...

class IgammaMode(Enum):
    VALUE: int
    DERIVATIVE: int
    SAMPLE_DERIVATIVE: int

def igamma_impl(a, x, *, dtype): ...
def igammac_impl(a, x, *, dtype): ...
def igamma_grad_a_impl(a, x, *, dtype): ...
def random_gamma_grad_impl(a, x, *, dtype): ...
def evaluate_chebyshev_polynomial(x, coefficients): ...
def bessel_i0e_impl(x): ...

regularized_incomplete_beta_p: Incomplete
lgamma_p: Incomplete
digamma_p: Incomplete
polygamma_p: Incomplete
igamma_p: Incomplete
igamma_grad_a_p: Incomplete
igammac_p: Incomplete
random_gamma_grad_p: Incomplete
zeta_p: Incomplete
bessel_i0e_p: Incomplete
bessel_i1e_p: Incomplete
erf_p: Incomplete
erfc_p: Incomplete
erf_inv_p: Incomplete
