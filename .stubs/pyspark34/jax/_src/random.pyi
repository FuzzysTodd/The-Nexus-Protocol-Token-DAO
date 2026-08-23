from _typeshed import Incomplete
from collections.abc import Sequence
from jax import lax as lax
from jax._src import core as core, dtypes as dtypes, prng as prng, xla_bridge as xla_bridge
from jax._src.api import jit as jit, vmap as vmap
from jax._src.config import config as config
from jax._src.core import NamedShape as NamedShape
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.numpy.util import check_arraylike as check_arraylike, promote_dtypes_inexact as promote_dtypes_inexact
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DTypeLike as DTypeLike
from jax._src.util import canonicalize_axis as canonicalize_axis
from jax.numpy.linalg import cholesky as cholesky, eigh as eigh, svd as svd

RealArray = ArrayLike
IntegerArray = ArrayLike
DTypeLikeInt = DTypeLike
DTypeLikeUInt = DTypeLike
DTypeLikeFloat = DTypeLike
Shape = Sequence[int]
KeyArray: Incomplete
PRNGKeyArray: Incomplete
UINT_DTYPES: Incomplete
PRNG_IMPLS: Incomplete

def default_prng_impl():
    """Get the default PRNG implementation.

  The default implementation is determined by ``config.jax_default_prng_impl``,
  which specifies it by name. This function returns the corresponding
  ``jax.prng.PRNGImpl`` instance.
  """
def resolve_prng_impl(impl_spec: str | None): ...
def key(seed: int | Array, *, impl: str | None = None) -> PRNGKeyArray:
    """Create a pseudo-random number generator (PRNG) key given an integer seed.

  The result is a scalar array with a key that indicates the default PRNG
  implementation, as determined by the optional ``impl`` argument or,
  otherwise, by the ``jax_default_prng_impl`` config flag.

  Args:
    seed: a 64- or 32-bit integer used as the value of the key.
    impl: optional string specifying the PRNG implementation (e.g.
      ``'threefry2x32'``)

  Returns:
    A scalar PRNG key array, consumable by random functions as well as ``split``
    and ``fold_in``.
  """
def PRNGKey(seed: int | Array, *, impl: str | None = None) -> KeyArray:
    """Create a pseudo-random number generator (PRNG) key given an integer seed.

  The resulting key carries the default PRNG implementation, as
  determined by the optional ``impl`` argument or, otherwise, by the
  ``jax_default_prng_impl`` config flag.

  Args:
    seed: a 64- or 32-bit integer used as the value of the key.
    impl: optional string specifying the PRNG implementation (e.g.
      ``'threefry2x32'``)

  Returns:
    A PRNG key, consumable by random functions as well as ``split``
    and ``fold_in``.
  """
def threefry2x32_key(seed: int) -> KeyArray:
    """Creates a threefry2x32 PRNG key from an integer seed."""
def rbg_key(seed: int) -> KeyArray:
    """Creates an RBG PRNG key from an integer seed."""
def unsafe_rbg_key(seed: int) -> KeyArray:
    """Creates an unsafe RBG PRNG key from an integer seed."""
def fold_in(key: KeyArray, data: IntegerArray) -> KeyArray:
    """Folds in data to a PRNG key to form a new PRNG key.

  Args:
    key: a PRNG key (from ``PRNGKey``, ``split``, ``fold_in``).
    data: a 32bit integer representing data to be folded in to the key.

  Returns:
    A new PRNG key that is a deterministic function of the inputs and is
    statistically safe for producing a stream of new pseudo-random values.
  """
def split(key: KeyArray, num: int | tuple[int, ...] = 2) -> KeyArray:
    """Splits a PRNG key into `num` new keys by adding a leading axis.

  Args:
    key: a PRNG key (from ``PRNGKey``, ``split``, ``fold_in``).
    num: optional, a positive integer (or tuple of integers) indicating
      the number (or shape) of keys to produce. Defaults to 2.

  Returns:
    An array-like object of `num` new PRNG keys.
  """
def key_data(keys: KeyArray) -> Array:
    """Recover the bits of key data underlying a PRNG key array."""
def wrap_key_data(key_bits_array: Array, *, impl: str | None = None):
    """Wrap an array of key data bits into a PRNG key array.

  Args:
    key_bits_array: a ``uint32`` array with trailing shape corresponding to
      the key shape of the PRNG implementation specified by ``impl``.
    impl: optional, specifies a PRNG implementation, as in ``random.key``.

  Returns:
    A PRNG key array, whose dtype is a subdtype of ``jax.dtypes.prng_key``
      corresponding to ``impl``, and whose shape equals the leading shape
      of ``key_bits_array.shape`` up to the key bit dimensions.
  """
def bits(key: KeyArray, shape: Shape = (), dtype: DTypeLikeUInt | None = None) -> Array:
    """Sample uniform bits in the form of unsigned integers.

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ``()``.
    dtype: optional, an unsigned integer dtype for the returned values (default
      ``uint64`` if ``jax_enable_x64`` is true, otherwise ``uint32``).

  Returns:
    A random array with the specified shape and dtype.
  """
def uniform(key: KeyArray, shape: Shape | NamedShape = (), dtype: DTypeLikeFloat = ..., minval: RealArray = 0.0, maxval: RealArray = 1.0) -> Array:
    """Sample uniform random values in [minval, maxval) with given shape/dtype.

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).
    minval: optional, a minimum (inclusive) value broadcast-compatible with shape for the range (default 0).
    maxval: optional, a maximum (exclusive) value broadcast-compatible with shape for the range (default 1).

  Returns:
    A random array with the specified shape and dtype.
  """
def randint(key: KeyArray, shape: Shape, minval: IntegerArray, maxval: IntegerArray, dtype: DTypeLikeInt = ...) -> Array:
    """Sample uniform random values in [minval, maxval) with given shape/dtype.

  Args:
    key: a PRNG key used as the random key.
    shape: a tuple of nonnegative integers representing the shape.
    minval: int or array of ints broadcast-compatible with ``shape``, a minimum
      (inclusive) value for the range.
    maxval: int or array of ints broadcast-compatible with ``shape``, a maximum
      (exclusive) value for the range.
    dtype: optional, an int dtype for the returned values (default int64 if
      jax_enable_x64 is true, otherwise int32).

  Returns:
    A random array with the specified shape and dtype.
  """
def shuffle(key: KeyArray, x: ArrayLike, axis: int = 0) -> Array:
    """Shuffle the elements of an array uniformly at random along an axis.

  Args:
    key: a PRNG key used as the random key.
    x: the array to be shuffled.
    axis: optional, an int axis along which to shuffle (default 0).

  Returns:
    A shuffled version of x.
  """
def permutation(key: KeyArray, x: int | ArrayLike, axis: int = 0, independent: bool = False) -> Array:
    """Returns a randomly permuted array or range.

  Args:
    key: a PRNG key used as the random key.
    x: int or array. If x is an integer, randomly shuffle np.arange(x).
      If x is an array, randomly shuffle its elements.
    axis: int, optional. The axis which x is shuffled along. Default is 0.
    independent: bool, optional. If set to True, each individual vector along
      the given axis is shuffled independently. Default is False.

  Returns:
    A shuffled version of x or array range
  """
def choice(key: KeyArray, a: int | ArrayLike, shape: Shape = (), replace: bool = True, p: RealArray | None = None, axis: int = 0) -> Array:
    """Generates a random sample from a given array.

  .. warning::
    If ``p`` has fewer non-zero elements than the requested number of samples,
    as specified in ``shape``, and ``replace=False``, the output of this
    function is ill-defined. Please make sure to use appropriate inputs.

  Args:
    key: a PRNG key used as the random key.
    a : array or int. If an ndarray, a random sample is generated from
      its elements. If an int, the random sample is generated as if a were
      arange(a).
    shape : tuple of ints, optional. Output shape.  If the given shape is,
      e.g., ``(m, n)``, then ``m * n`` samples are drawn.  Default is (),
      in which case a single value is returned.
    replace : boolean.  Whether the sample is with or without replacement.
      default is True.
    p : 1-D array-like, The probabilities associated with each entry in a.
      If not given the sample assumes a uniform distribution over all
      entries in a.
    axis: int, optional. The axis along which the selection is performed.
      The default, 0, selects by row.

  Returns:
    An array of shape `shape` containing samples from `a`.
  """
def normal(key: KeyArray, shape: Shape | NamedShape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample standard normal random values with given shape and float dtype.

  The values are returned according to the probability density function:

  .. math::
     f(x) = \\frac{1}{\\sqrt{2\\pi}}e^{-x^2/2}

  on the domain :math:`-\\infty < x < \\infty`

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified shape and dtype.
  """
def multivariate_normal(key: KeyArray, mean: RealArray, cov: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = None, method: str = 'cholesky') -> Array:
    """Sample multivariate normal random values with given mean and covariance.

  The values are returned according to the probability density function:

  .. math::
     f(x;\\mu, \\Sigma) = (2\\pi)^{-k/2} \\det(\\Sigma)^{-1}e^{-\\frac{1}{2}(x - \\mu)^T \\Sigma^{-1} (x - \\mu)}

  where :math:`k` is the dimension, :math:`\\mu` is the mean (given by ``mean``) and
  :math:`\\Sigma` is the covariance matrix (given by ``cov``).

  Args:
    key: a PRNG key used as the random key.
    mean: a mean vector of shape ``(..., n)``.
    cov: a positive definite covariance matrix of shape ``(..., n, n)``. The
      batch shape ``...`` must be broadcast-compatible with that of ``mean``.
    shape: optional, a tuple of nonnegative integers specifying the result
      batch shape; that is, the prefix of the result shape excluding the last
      axis. Must be broadcast-compatible with ``mean.shape[:-1]`` and
      ``cov.shape[:-2]``. The default (None) produces a result batch shape by
      broadcasting together the batch shapes of ``mean`` and ``cov``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).
    method: optional, a method to compute the factor of ``cov``.
      Must be one of 'svd', 'eigh', and 'cholesky'. Default 'cholesky'. For
      singular covariance matrices, use 'svd' or 'eigh'.
  Returns:
    A random array with the specified dtype and shape given by
    ``shape + mean.shape[-1:]`` if ``shape`` is not None, or else
    ``broadcast_shapes(mean.shape[:-1], cov.shape[:-2]) + mean.shape[-1:]``.
  """
def truncated_normal(key: KeyArray, lower: RealArray, upper: RealArray, shape: Shape | NamedShape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample truncated standard normal random values with given shape and dtype.

  The values are returned according to the probability density function:

  .. math::
     f(x) \\propto e^{-x^2/2}

  on the domain :math:`\\rm{lower} < x < \\rm{upper}`.

  Args:
    key: a PRNG key used as the random key.
    lower: a float or array of floats representing the lower bound for
      truncation. Must be broadcast-compatible with ``upper``.
    upper: a float or array of floats representing the  upper bound for
      truncation. Must be broadcast-compatible with ``lower``.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``lower`` and ``upper``. The
      default (None) produces a result shape by broadcasting ``lower`` and
      ``upper``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and shape given by ``shape`` if
    ``shape`` is not None, or else by broadcasting ``lower`` and ``upper``.
    Returns values in the open interval ``(lower, upper)``.
  """
def bernoulli(key: KeyArray, p: RealArray = ..., shape: Shape | NamedShape | None = None) -> Array:
    """Sample Bernoulli random values with given shape and mean.

  The values are distributed according to the probability mass function:

  .. math::
     f(k; p) = p^k(1 - p)^{1 - k}

  where :math:`k \\in \\{0, 1\\}` and :math:`0 \\le p \\le 1`.

  Args:
    key: a PRNG key used as the random key.
    p: optional, a float or array of floats for the mean of the random
      variables. Must be broadcast-compatible with ``shape``. Default 0.5.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Must be broadcast-compatible with ``p.shape``. The default (None)
      produces a result shape equal to ``p.shape``.

  Returns:
    A random array with boolean dtype and shape given by ``shape`` if ``shape``
    is not None, or else ``p.shape``.
  """
def beta(key: KeyArray, a: RealArray, b: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    '''Sample Beta random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(x;a,b) \\propto x^{a - 1}(1 - x)^{b - 1}

  on the domain :math:`0 \\le x \\le 1`.

  Args:
    key: a PRNG key used as the random key.
    a: a float or array of floats broadcast-compatible with ``shape``
      representing the first parameter "alpha".
    b: a float or array of floats broadcast-compatible with ``shape``
      representing the second parameter "beta".
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``a`` and ``b``. The default
      (None) produces a result shape by broadcasting ``a`` and ``b``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and shape given by ``shape`` if
    ``shape`` is not None, or else by broadcasting ``a`` and ``b``.
  '''
def cauchy(key: KeyArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Cauchy random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(x) \\propto \\frac{1}{x^2 + 1}

  on the domain :math:`-\\infty < x < \\infty`

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified shape and dtype.
  """
def dirichlet(key: KeyArray, alpha: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Dirichlet random values with given shape and float dtype.

  The values are distributed according the the probability density function:

  .. math::
     f(\\{x_i\\}; \\{\\alpha_i\\}) = \\propto \\prod_{i=1}^k x_i^{\\alpha_i - 1}

  Where :math:`k` is the dimension, and :math:`\\{x_i\\}` satisfies

  .. math::
     \\sum_{i=1}^k x_i = 1

  and :math:`0 \\le x_i \\le 1` for all :math:`x_i`.

  Args:
    key: a PRNG key used as the random key.
    alpha: an array of shape ``(..., n)`` used as the concentration
      parameter of the random variables.
    shape: optional, a tuple of nonnegative integers specifying the result
      batch shape; that is, the prefix of the result shape excluding the last
      element of value ``n``. Must be broadcast-compatible with
      ``alpha.shape[:-1]``. The default (None) produces a result shape equal to
      ``alpha.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and shape given by
    ``shape + (alpha.shape[-1],)`` if ``shape`` is not None, or else
    ``alpha.shape``.
  """
def exponential(key: KeyArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Exponential random values with given shape and float dtype.

  The values are distributed according the the probability density function:

  .. math::
     f(x) = e^{-x}

  on the domain :math:`0 \\le x < \\infty`.

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified shape and dtype.
  """

random_gamma_p: Incomplete

def gamma(key: KeyArray, a: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Gamma random values with given shape and float dtype.

  The values are distributed according the the probability density function:

  .. math::
     f(x;a) \\propto x^{a - 1} e^{-x}

  on the domain :math:`0 \\le x < \\infty`, with :math:`a > 0`.

  This is the standard gamma density, with a unit scale/rate parameter.
  Dividing the sample output by the rate is equivalent to sampling from
  *gamma(a, rate)*, and multiplying the sample output by the scale is equivalent
  to sampling from *gamma(a, scale)*.

  Args:
    key: a PRNG key used as the random key.
    a: a float or array of floats broadcast-compatible with ``shape``
      representing the parameter of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``a``. The default (None)
      produces a result shape equal to ``a.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``a.shape``.

  See Also:
    loggamma : sample gamma values in log-space, which can provide improved
      accuracy for small values of ``a``.
  """
def loggamma(key: KeyArray, a: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample log-gamma random values with given shape and float dtype.

  This function is implemented such that the following will hold for a
  dtype-appropriate tolerance::

    np.testing.assert_allclose(jnp.exp(loggamma(*args)), gamma(*args), rtol=rtol)

  The benefit of log-gamma is that for samples very close to zero (which occur frequently
  when `a << 1`) sampling in log space provides better precision.

  Args:
    key: a PRNG key used as the random key.
    a: a float or array of floats broadcast-compatible with ``shape``
      representing the parameter of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``a``. The default (None)
      produces a result shape equal to ``a.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``a.shape``.

  See Also:
    gamma : standard gamma sampler.
  """
def poisson(key: KeyArray, lam: RealArray, shape: Shape | None = None, dtype: DTypeLikeInt = ...) -> Array:
    """Sample Poisson random values with given shape and integer dtype.

  The values are distributed according to the probability mass function:

  .. math::
     f(k; \\lambda) = \\frac{\\lambda^k e^{-\\lambda}}{k!}

  Where `k` is a non-negative integer and :math:`\\lambda > 0`.

  Args:
    key: a PRNG key used as the random key.
    lam: rate parameter (mean of the distribution), must be >= 0. Must be broadcast-compatible with ``shape``
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default (None) produces a result shape equal to ``lam.shape``.
    dtype: optional, a integer dtype for the returned values (default int64 if
      jax_enable_x64 is true, otherwise int32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape is not None, or else by ``lam.shape``.
  """
def gumbel(key: KeyArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Gumbel random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(x) = e^{-(x + e^{-x})}

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified shape and dtype.
  """
def categorical(key: KeyArray, logits: RealArray, axis: int = -1, shape: Shape | None = None) -> Array:
    """Sample random values from categorical distributions.

  Args:
    key: a PRNG key used as the random key.
    logits: Unnormalized log probabilities of the categorical distribution(s) to sample from,
      so that `softmax(logits, axis)` gives the corresponding probabilities.
    axis: Axis along which logits belong to the same categorical distribution.
    shape: Optional, a tuple of nonnegative integers representing the result shape.
      Must be broadcast-compatible with ``np.delete(logits.shape, axis)``.
      The default (None) produces a result shape equal to ``np.delete(logits.shape, axis)``.

  Returns:
    A random array with int dtype and shape given by ``shape`` if ``shape``
    is not None, or else ``np.delete(logits.shape, axis)``.
  """
def laplace(key: KeyArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Laplace random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
    f(x) = \\frac{1}{2}e^{-|x|}

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified shape and dtype.
  """
def logistic(key: KeyArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample logistic random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(x) = \\frac{e^{-x}}{(1 + e^{-x})^2}

  Args:
    key: a PRNG key used as the random key.
    shape: optional, a tuple of nonnegative integers representing the result
      shape. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified shape and dtype.
  """
def pareto(key: KeyArray, b: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Pareto random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(x; b) = b / x^{b + 1}

  on the domain :math:`1 \\le x < \\infty` with :math:`b > 0`

  Args:
    key: a PRNG key used as the random key.
    b: a float or array of floats broadcast-compatible with ``shape``
      representing the parameter of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``b``. The default (None)
      produces a result shape equal to ``b.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``b.shape``.
  """
def t(key: KeyArray, df: RealArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Student's t random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(t; \\nu) \\propto \\left(1 + \\frac{t^2}{\\nu}\\right)^{-(\\nu + 1)/2}

  Where :math:`\\nu > 0` is the degrees of freedom, given by the parameter ``df``.

  Args:
    key: a PRNG key used as the random key.
    df: a float or array of floats broadcast-compatible with ``shape``
      representing the degrees of freedom parameter of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``df``. The default (None)
      produces a result shape equal to ``df.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``df.shape``.
  """
def chisquare(key: KeyArray, df: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Chisquare random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(x; \\nu) \\propto x^{k/2 - 1}e^{-x/2}

  on the domain :math:`0 < x < \\infty`, where :math:`\\nu > 0` represents the
  degrees of freedom, given by the parameter ``df``.

  Args:
    key: a PRNG key used as the random key.
    df: a float or array of floats broadcast-compatible with ``shape``
      representing the parameter of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``df``. The default (None)
      produces a result shape equal to ``df.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``df.shape``.
  """
def f(key: KeyArray, dfnum: RealArray, dfden: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample F-distribution random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
     f(x; \\nu) \\propto x^{\\nu_1/2 - 1}\\left(1 + \\frac{\\nu_1}{\\nu_2}x\\right)^{
      -(\\nu_1 + \\nu_2) / 2}

  on the domain :math:`0 < x < \\infty`. Here :math:`\\nu_1` is the degrees of
  freedom of the numerator (``dfnum``), and :math:`\\nu_2` is the degrees of
  freedom of the denominator (``dfden``).

  Args:
    key: a PRNG key used as the random key.
    dfnum: a float or array of floats broadcast-compatible with ``shape``
      representing the numerator's ``df`` of the distribution.
    dfden: a float or array of floats broadcast-compatible with ``shape``
      representing the denominator's ``df`` of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``dfnum`` and ``dfden``.
      The default (None) produces a result shape equal to ``dfnum.shape``,
      and ``dfden.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``df.shape``.
  """
def rademacher(key: KeyArray, shape: Shape, dtype: DTypeLikeInt = ...) -> Array:
    """Sample from a Rademacher distribution.

  The values are distributed according to the probability mass function:

  .. math::
     f(k) = \\frac{1}{2}(\\delta(k - 1) + \\delta(k + 1))

  on the domain :math:`k \\in \\{-1, 1}`, where `\\delta(x)` is the dirac delta function.

  Args:
    key: a PRNG key.
    shape: The shape of the returned samples.
    dtype: The type used for samples.

  Returns:
    A jnp.array of samples, of shape `shape`. Each element in the output has
    a 50% change of being 1 or -1.

  """
def maxwell(key: KeyArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample from a one sided Maxwell distribution.

  The values are distributed according to the probability density function:

  .. math::
     f(x) \\propto x^2 e^{-x^2 / 2}

  on the domain :math:`0 \\le x < \\infty`.

  Args:
    key: a PRNG key.
    shape: The shape of the returned samples.
    dtype: The type used for samples.

  Returns:
    A jnp.array of samples, of shape `shape`.

  """
def double_sided_maxwell(key: KeyArray, loc: RealArray, scale: RealArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample from a double sided Maxwell distribution.

  The values are distributed according to the probability density function:

  .. math::
     f(x;\\mu,\\sigma) \\propto z^2 e^{-z^2 / 2}

  where :math:`z = (x - \\mu) / \\sigma`, with the center :math:`\\mu` specified by
  ``loc`` and the scale :math:`\\sigma` specified by ``scale``.

  Args:
    key: a PRNG key.
    loc: The location parameter of the distribution.
    scale: The scale parameter of the distribution.
    shape: The shape added to the parameters loc and scale broadcastable shape.
    dtype: The type used for samples.

  Returns:
    A jnp.array of samples.

  """
def weibull_min(key: KeyArray, scale: RealArray, concentration: RealArray, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample from a Weibull distribution.

  The values are distributed according to the probability density function:

  .. math::
     f(x;\\sigma,c) \\propto x^{c - 1} \\exp(-(x / \\sigma)^c)

  on the domain :math:`0 < x < \\infty`, where :math:`c > 0` is the concentration
  parameter, and :math:`\\sigma > 0` is the scale parameter.

  Args:
    key: a PRNG key.
    scale: The scale parameter of the distribution.
    concentration: The concentration parameter of the distribution.
    shape: The shape added to the parameters loc and scale broadcastable shape.
    dtype: The type used for samples.

  Returns:
    A jnp.array of samples.

  """

threefry2x32_p: Incomplete

def threefry_2x32(keypair, count): ...
def orthogonal(key: KeyArray, n: int, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample uniformly from the orthogonal group O(n).

  If the dtype is complex, sample uniformly from the unitary group U(n).

  Args:
    key: a PRNG key used as the random key.
    n: an integer indicating the resulting dimension.
    shape: optional, the batch dimensions of the result. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array of shape `(*shape, n, n)` and specified dtype.
  """
def generalized_normal(key: KeyArray, p: float, shape: Shape = (), dtype: DTypeLikeFloat = ...) -> Array:
    """Sample from the generalized normal distribution.

  The values are returned according to the probability density function:

  .. math::
     f(x;p) \\propto e^{-|x|^p}

  on the domain :math:`-\\infty < x < \\infty`, where :math:`p > 0` is the
  shape parameter.

  Args:
    key: a PRNG key used as the random key.
    p: a float representing the shape parameter.
    shape: optional, the batch dimensions of the result. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified shape and dtype.
  """
def ball(key: KeyArray, d: int, p: float = 2, shape: Shape = (), dtype: DTypeLikeFloat = ...):
    """Sample uniformly from the unit Lp ball.

  Reference: https://arxiv.org/abs/math/0503650.

  Args:
    key: a PRNG key used as the random key.
    d: a nonnegative int representing the dimensionality of the ball.
    p: a float representing the p parameter of the Lp norm.
    shape: optional, the batch dimensions of the result. Default ().
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array of shape `(*shape, d)` and specified dtype.
  """
def rayleigh(key: KeyArray, scale: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Rayleigh random values with given shape and float dtype.

  The values are returned according to the probability density function:

  .. math::
     f(x;\\sigma) \\propto xe^{-x^2/(2\\sigma^2)}

  on the domain :math:`-\\infty < x < \\infty`, and where `\\sigma > 0` is the scale
  parameter of the distribution.

  Args:
    key: a PRNG key used as the random key.
    scale: a float or array of floats broadcast-compatible with ``shape``
      representing the parameter of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``scale``. The default (None)
      produces a result shape equal to ``scale.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``scale.shape``.
  """
def wald(key: KeyArray, mean: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Wald random values with given shape and float dtype.

  The values are returned according to the probability density function:

  .. math::
     f(x;\\mu) = \\frac{1}{\\sqrt{2\\pi x^3}} \\exp\\left(-\\frac{(x - \\mu)^2}{2\\mu^2 x}\\right)

  on the domain :math:`-\\infty < x < \\infty`, and where :math:`\\mu > 0` is the location
  parameter of the distribution.


  Args:
    key: a PRNG key used as the random key.
    mean: a float or array of floats broadcast-compatible with ``shape``
      representing the mean parameter of the distribution.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``mean``. The default
      (None) produces a result shape equal to ``np.shape(mean)``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``mean.shape``.
  """
def geometric(key: KeyArray, p: RealArray, shape: Shape | None = None, dtype: DTypeLikeInt = ...) -> Array:
    """Sample Geometric random values with given shape and float dtype.

  The values are returned according to the probability mass function:

  .. math::
      f(k;p) = p(1-p)^{k-1}

  on the domain :math:`0 < p < 1`.

  Args:
    key: a PRNG key used as the random key.
    p: a float or array of floats broadcast-compatible with ``shape``
      representing the the probability of success of an individual trial.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``p``. The default
      (None) produces a result shape equal to ``np.shape(p)``.
    dtype: optional, a int dtype for the returned values (default int64 if
      jax_enable_x64 is true, otherwise int32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``p.shape``.
  """
def triangular(key: KeyArray, left: RealArray, mode: RealArray, right: RealArray, shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """Sample Triangular random values with given shape and float dtype.

  The values are returned according to the probability density function:

  .. math::
      f(x; a, b, c) = \\frac{2}{c-a} \\left\\{ \\begin{array}{ll} \\frac{x-a}{b-a} & a \\leq x \\leq b \\\\ \\frac{c-x}{c-b} & b \\leq x \\leq c \\end{array} \\right.

  on the domain :math:`a \\leq x \\leq c`.

  Args:
    key: a PRNG key used as the random key.
    left: a float or array of floats broadcast-compatible with ``shape``
      representing the lower limit parameter of the distribution.
    mode: a float or array of floats broadcast-compatible with ``shape``
      representing the peak value parameter of the distribution, value must
      fulfill the condition ``left <= mode <= right``.
    right: a float or array of floats broadcast-compatible with ``shape``
      representing the upper limit parameter of the distribution, must be
      larger than ``left``.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. Must be broadcast-compatible with ``left``,``mode`` and ``right``.
      The default (None) produces a result shape equal to ``left.shape``, ``mode.shape``
      and ``right.shape``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape`` if
    ``shape`` is not None, or else by ``left.shape``, ``mode.shape`` and ``right.shape``.
  """
def lognormal(key: KeyArray, sigma: RealArray = ..., shape: Shape | None = None, dtype: DTypeLikeFloat = ...) -> Array:
    """ Sample lognormal random values with given shape and float dtype.

  The values are distributed according to the probability density function:

  .. math::
      f(x) = \\frac{1}{x\\sqrt{2\\pi\\sigma^2}}\\exp\\left(-\\frac{(\\log x)^2}{2\\sigma^2}\\right)

  on the domain :math:`x > 0`.

  Args:
    key: a PRNG key used as the random key.
    sigma: a float or array of floats broadcast-compatible with ``shape`` representing
      the standard deviation of the underlying normal distribution. Default 1.
    shape: optional, a tuple of nonnegative integers specifying the result
      shape. The default (None) produces a result shape equal to ``()``.
    dtype: optional, a float dtype for the returned values (default float64 if
      jax_enable_x64 is true, otherwise float32).

  Returns:
    A random array with the specified dtype and with shape given by ``shape``.
  """
