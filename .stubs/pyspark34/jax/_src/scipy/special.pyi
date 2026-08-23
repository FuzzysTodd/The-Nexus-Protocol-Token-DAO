from _typeshed import Incomplete
from jax import jit as jit, jvp as jvp, lax as lax, vmap as vmap
from jax._src import core as core, custom_derivatives as custom_derivatives, dtypes as dtypes
from jax._src.numpy.util import promote_args_inexact as promote_args_inexact, promote_dtypes_inexact as promote_dtypes_inexact
from jax._src.typing import Array as Array, ArrayLike as ArrayLike

def gammaln(x: ArrayLike) -> Array: ...
def gamma(x: ArrayLike) -> Array: ...

betaln: Incomplete

def betainc(a: ArrayLike, b: ArrayLike, x: ArrayLike) -> Array: ...
def digamma(x: ArrayLike) -> Array: ...
def gammainc(a: ArrayLike, x: ArrayLike) -> Array: ...
def gammaincc(a: ArrayLike, x: ArrayLike) -> Array: ...
def erf(x: ArrayLike) -> Array: ...
def erfc(x: ArrayLike) -> Array: ...
def erfinv(x: ArrayLike) -> Array: ...
def logit(x: ArrayLike) -> Array: ...
def expit(x: ArrayLike) -> Array: ...

logsumexp: Incomplete

def xlogy(x: ArrayLike, y: ArrayLike) -> Array: ...
def xlog1py(x: ArrayLike, y: ArrayLike) -> Array: ...
def entr(x: ArrayLike) -> Array: ...
def multigammaln(a: ArrayLike, d: ArrayLike) -> Array: ...
def kl_div(p: ArrayLike, q: ArrayLike) -> Array: ...
def rel_entr(p: ArrayLike, q: ArrayLike) -> Array: ...
def zeta(x: ArrayLike, q: ArrayLike | None = None) -> Array: ...
def polygamma(n: ArrayLike, x: ArrayLike) -> Array: ...
def ndtr(x: ArrayLike) -> Array:
    """Normal distribution function.

  Returns the area under the Gaussian probability density function, integrated
  from minus infinity to x:

  .. math::
    \\begin{align}
    \\mathrm{ndtr}(x) =&
      \\ \\frac{1}{\\sqrt{2 \\pi}}\\int_{-\\infty}^{x} e^{-\\frac{1}{2}t^2} dt \\\\\n    =&\\ \\frac{1}{2} (1 + \\mathrm{erf}(\\frac{x}{\\sqrt{2}})) \\\\\n    =&\\ \\frac{1}{2} \\mathrm{erfc}(\\frac{x}{\\sqrt{2}})
    \\end{align}

  Args:
    x: An array of type `float32`, `float64`.

  Returns:
    An array with `dtype=x.dtype`.

  Raises:
    TypeError: if `x` is not floating-type.
  """
def ndtri(p: ArrayLike) -> Array:
    """The inverse of the CDF of the Normal distribution function.

  Returns `x` such that the area under the PDF from :math:`-\\infty` to `x` is equal
  to `p`.

  A piece-wise rational approximation is done for the function.
  This is a based on the implementation in netlib.

  Args:
    p: an array of type `float32`, `float64`.

  Returns:
    an array with `dtype=p.dtype`.

  Raises:
    TypeError: if `p` is not floating-type.
  """
def log_ndtr(x: ArrayLike, series_order: int = 3) -> Array:
    """Log Normal distribution function.

  For details of the Normal distribution function see `ndtr`.

  This function calculates :math:`\\log(\\mathrm{ndtr}(x))` by either calling
  :math:`\\log(\\mathrm{ndtr}(x))` or using an asymptotic series. Specifically:

  - For `x > upper_segment`, use the approximation `-ndtr(-x)` based on
    :math:`\\log(1-x) \\approx -x, x \\ll 1`.
  - For `lower_segment < x <= upper_segment`, use the existing `ndtr` technique
    and take a log.
  - For `x <= lower_segment`, we use the series approximation of `erf` to compute
    the log CDF directly.

  The `lower_segment` is set based on the precision of the input:

  .. math::
    \\begin{align}
    \\mathit{lower\\_segment} =&
      \\ \\begin{cases}
        -20 &  x.\\mathrm{dtype}=\\mathit{float64} \\\\\n        -10 &  x.\\mathrm{dtype}=\\mathit{float32} \\\\\n        \\end{cases} \\\\\n    \\mathit{upper\\_segment} =&
      \\ \\begin{cases}
        8&  x.\\mathrm{dtype}=\\mathit{float64} \\\\\n        5&  x.\\mathrm{dtype}=\\mathit{float32} \\\\\n        \\end{cases}
    \\end{align}


  When `x < lower_segment`, the `ndtr` asymptotic series approximation is:

  .. math::
    \\begin{align}
     \\mathrm{ndtr}(x) =&\\  \\mathit{scale} * (1 + \\mathit{sum}) + R_N \\\\\n     \\mathit{scale}   =&\\  \\frac{e^{-0.5 x^2}}{-x \\sqrt{2 \\pi}} \\\\\n     \\mathit{sum}     =&\\  \\sum_{n=1}^N {-1}^n (2n-1)!! / (x^2)^n \\\\\n     R_N     =&\\  O(e^{-0.5 x^2} (2N+1)!! / |x|^{2N+3})
    \\end{align}

  where :math:`(2n-1)!! = (2n-1) (2n-3) (2n-5) ...  (3) (1)` is a
  `double-factorial
  <https://en.wikipedia.org/wiki/Double_factorial>`_ operator.


  Args:
    x: an array of type `float32`, `float64`.
    series_order: Positive Python integer. Maximum depth to
      evaluate the asymptotic expansion. This is the `N` above.

  Returns:
    an array with `dtype=x.dtype`.

  Raises:
    TypeError: if `x.dtype` is not handled.
    TypeError: if `series_order` is a not Python `integer.`
    ValueError:  if `series_order` is not in `[0, 30]`.
  """
def i0e(x: ArrayLike) -> Array: ...
def i0(x: ArrayLike) -> Array: ...
def i1e(x: ArrayLike) -> Array: ...
def i1(x: ArrayLike) -> Array: ...
def bessel_jn(z: ArrayLike, *, v: int, n_iter: int = 50) -> Array:
    """Bessel function of the first kind of integer order and real argument.

  Reference:
  Shanjie Zhang and Jian-Ming Jin. Computation of special functions.
  Wiley-Interscience, 1996.

  Args:
    z: The sampling point(s) at which the Bessel function of the first kind are
      computed.
    v: The order (int) of the Bessel function.
    n_iter: The number of iterations required for updating the function
      values. As a rule of thumb, `n_iter` is the smallest nonnegative integer
      that satisfies the condition
      `int(0.5 * log10(6.28 + n_iter) - n_iter *  log10(1.36 + abs(z) / n_iter)) > 20`.
      Details in `BJNDD` (https://people.sc.fsu.edu/~jburkardt/f77_src/special_functions/special_functions.f)

  Returns:
    An array of shape `(v+1, *z.shape)` containing the values of the Bessel
    function of orders 0, 1, ..., v. The return type matches the type of `z`.

  Raises:
    TypeError if `v` is not integer.
    ValueError if elements of array `z` are not float.
  """
def lpmn(m: int, n: int, z: Array) -> tuple[Array, Array]:
    """The associated Legendre functions (ALFs) of the first kind.

  Args:
    m: The maximum order of the associated Legendre functions.
    n: The maximum degree of the associated Legendre function, often called
      `l` in describing ALFs. Both the degrees and orders are
      `[0, 1, 2, ..., l_max]`, where `l_max` denotes the maximum degree.
    z: A vector of type `float32` or `float64` containing the sampling
      points at which the ALFs are computed.

  Returns:
    A 2-tuple of 3D arrays of shape `(l_max + 1, l_max + 1, len(z))` containing
    the values and derivatives of the associated Legendre functions of the
    first kind. The return type matches the type of `z`.

  Raises:
    TypeError if elements of array `z` are not in (float32, float64).
    ValueError if array `z` is not 1D.
    NotImplementedError if `m!=n`.
  """
def lpmn_values(m: int, n: int, z: Array, is_normalized: bool) -> Array:
    """The associated Legendre functions (ALFs) of the first kind.

  Unlike `lpmn`, this function only computes the values of ALFs.
  The ALFs of the first kind can be used in spherical harmonics. The
  spherical harmonic of degree `l` and order `m` can be written as
  :math:`Y_l^m(\\theta, \\phi) = N_l^m * P_l^m(\\cos \\theta) * \\exp(i m \\phi)`,
  where :math:`N_l^m` is the normalization factor and θ and φ are the
  colatitude and longitude, respectively. :math:`N_l^m` is chosen in the
  way that the spherical harmonics form a set of orthonormal basis function
  of :math:`L^2(S^2)`. Normalizing :math:`P_l^m` avoids overflow/underflow
  and achieves better numerical stability.

  Args:
    m: The maximum order of the associated Legendre functions.
    n: The maximum degree of the associated Legendre function, often called
      `l` in describing ALFs. Both the degrees and orders are
      `[0, 1, 2, ..., l_max]`, where `l_max` denotes the maximum degree.
    z: A vector of type `float32` or `float64` containing the sampling
      points at which the ALFs are computed.
    is_normalized: True if the associated Legendre functions are normalized.
      With normalization, :math:`N_l^m` is applied such that the spherical
      harmonics form a set of orthonormal basis functions of :math:`L^2(S^2)`.

  Returns:
    A 3D array of shape `(l_max + 1, l_max + 1, len(z))` containing
    the values of the associated Legendre functions of the first kind. The
    return type matches the type of `z`.

  Raises:
    TypeError if elements of array `z` are not in (float32, float64).
    ValueError if array `z` is not 1D.
    NotImplementedError if `m!=n`.
  """
def sph_harm(m: Array, n: Array, theta: Array, phi: Array, n_max: int | None = None) -> Array:
    """Computes the spherical harmonics.

  The JAX version has one extra argument `n_max`, the maximum value in `n`.

  The spherical harmonic of degree `n` and order `m` can be written as
  :math:`Y_n^m(\\theta, \\phi) = N_n^m * P_n^m(\\cos \\phi) * \\exp(i m \\theta)`,
  where :math:`N_n^m = \\sqrt{\\frac{\\left(2n+1\\right) \\left(n-m\\right)!}
  {4 \\pi \\left(n+m\\right)!}}` is the normalization factor and :math:`\\phi` and
  :math:`\\theta` are the colatitude and longitude, respectively. :math:`N_n^m` is
  chosen in the way that the spherical harmonics form a set of orthonormal basis
  functions of :math:`L^2(S^2)`.

  Args:
    m: The order of the harmonic; must have `|m| <= n`. Return values for
      `|m| > n` ara undefined.
    n: The degree of the harmonic; must have `n >= 0`. The standard notation for
      degree in descriptions of spherical harmonics is `l (lower case L)`. We
      use `n` here to be consistent with `scipy.special.sph_harm`. Return
      values for `n < 0` are undefined.
    theta: The azimuthal (longitudinal) coordinate; must be in [0, 2*pi].
    phi: The polar (colatitudinal) coordinate; must be in [0, pi].
    n_max: The maximum degree `max(n)`. If the supplied `n_max` is not the true
      maximum value of `n`, the results are clipped to `n_max`. For example,
      `sph_harm(m=jnp.array([2]), n=jnp.array([10]), theta, phi, n_max=6)`
      acutually returns
      `sph_harm(m=jnp.array([2]), n=jnp.array([6]), theta, phi, n_max=6)`
  Returns:
    A 1D array containing the spherical harmonics at (m, n, theta, phi).
  """
def expi(x: ArrayLike) -> Array: ...
def expi_jvp(primals, tangents): ...
def expn(n: ArrayLike, x: ArrayLike) -> Array: ...
def expn_jvp(n, primals, tangents): ...
def exp1(x: ArrayLike, module: str = 'scipy.special') -> Array: ...
def spence(x: Array) -> Array:
    """
  Spence's function, also known as the dilogarithm for real values.
  It is defined to be:

  .. math::
    \\begin{equation}
    \\int_1^z \\frac{\\log(t)}{1 - t}dt
    \\end{equation}

  Unlike the SciPy implementation, this is only defined for positive
  real values of `z`. For negative values, `NaN` is returned.

  Args:
    z: An array of type `float32`, `float64`.

  Returns:
    An array with `dtype=z.dtype`.
    computed values of Spence's function.

  Raises:
    TypeError: if elements of array `z` are not in (float32, float64).

  Notes:
  There is a different convention which defines Spence's function by the
  integral:

  .. math::
    \\begin{equation}
    -\\int_0^z \\frac{\\log(1 - t)}{t}dt
    \\end{equation}

  this is our spence(1 - z).
  """
def bernoulli(n: int) -> Array: ...
