from _typeshed import Incomplete
from jax import custom_jvp as custom_jvp, lax as lax
from jax._src import core as core, dtypes as dtypes, util as util
from jax._src.core import AxisName as AxisName
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from typing import Any

def relu(x: ArrayLike) -> Array:
    """Rectified linear unit activation function.

  Computes the element-wise function:

  .. math::
    \\mathrm{relu}(x) = \\max(x, 0)

  except under differentiation, we take:

  .. math::
    \\nabla \\mathrm{relu}(0) = 0

  For more information see
  `Numerical influence of ReLU’(0) on backpropagation
  <https://openreview.net/forum?id=urrcVI-_jRm>`_.

  Args:
    x : input array

  Returns:
    An array.

  Example:
    >>> jax.nn.relu(jax.numpy.array([-2., -1., -0.5, 0, 0.5, 1., 2.]))
    Array([0. , 0. , 0. , 0. , 0.5, 1. , 2. ], dtype=float32)

  See also:
    :func:`relu6`

  """
def softplus(x: ArrayLike) -> Array:
    """Softplus activation function.

  Computes the element-wise function

  .. math::
    \\mathrm{softplus}(x) = \\log(1 + e^x)

  Args:
    x : input array
  """
def soft_sign(x: ArrayLike) -> Array:
    """Soft-sign activation function.

  Computes the element-wise function

  .. math::
    \\mathrm{soft\\_sign}(x) = \\frac{x}{|x| + 1}

  Args:
    x : input array
  """
def sigmoid(x: ArrayLike) -> Array:
    """Sigmoid activation function.

  Computes the element-wise function:

  .. math::
    \\mathrm{sigmoid}(x) = \\frac{1}{1 + e^{-x}}

  Args:
    x : input array

  Returns:
    An array.

  See also:
    :func:`log_sigmoid`

  """
def silu(x: ArrayLike) -> Array:
    """SiLU (a.k.a. swish) activation function.

  Computes the element-wise function:

  .. math::
    \\mathrm{silu}(x) = x \\cdot \\mathrm{sigmoid}(x) = \\frac{x}{1 + e^{-x}}

  :func:`swish` and :func:`silu` are both aliases for the same function.

  Args:
    x : input array

  Returns:
    An array.

  See also:
    :func:`sigmoid`
  """
swish = silu

def log_sigmoid(x: ArrayLike) -> Array:
    """Log-sigmoid activation function.

  Computes the element-wise function:

  .. math::
    \\mathrm{log\\_sigmoid}(x) = \\log(\\mathrm{sigmoid}(x)) = -\\log(1 + e^{-x})

  Args:
    x : input array

  Returns:
    An array.

  See also:
    :func:`sigmoid`
  """
def elu(x: ArrayLike, alpha: ArrayLike = 1.0) -> Array:
    """Exponential linear unit activation function.

  Computes the element-wise function:

  .. math::
    \\mathrm{elu}(x) = \\begin{cases}
      x, & x > 0\\\\\n      \\alpha \\left(\\exp(x) - 1\\right), & x \\le 0
    \\end{cases}

  Args:
    x : input array
    alpha : scalar or array of alpha values (default: 1.0)

  Returns:
    An array.

  See also:
    :func:`selu`
  """
def leaky_relu(x: ArrayLike, negative_slope: ArrayLike = 0.01) -> Array:
    """Leaky rectified linear unit activation function.

  Computes the element-wise function:

  .. math::
    \\mathrm{leaky\\_relu}(x) = \\begin{cases}
      x, & x \\ge 0\\\\\n      \\alpha x, & x < 0
    \\end{cases}

  where :math:`\\alpha` = :code:`negative_slope`.

  Args:
    x : input array
    negative_slope : array or scalar specifying the negative slope (default: 0.01)

  Returns:
    An array.

  See also:
    :func:`relu`
  """
def hard_tanh(x: ArrayLike) -> Array:
    """Hard :math:`\\mathrm{tanh}` activation function.

  Computes the element-wise function:

  .. math::
    \\mathrm{hard\\_tanh}(x) = \\begin{cases}
      -1, & x < -1\\\\\n      x, & -1 \\le x \\le 1\\\\\n      1, & 1 < x
    \\end{cases}

  Args:
    x : input array

  Returns:
    An array.
  """
def celu(x: ArrayLike, alpha: ArrayLike = 1.0) -> Array:
    """Continuously-differentiable exponential linear unit activation.

  Computes the element-wise function:

  .. math::
    \\mathrm{celu}(x) = \\begin{cases}
      x, & x > 0\\\\\n      \\alpha \\left(\\exp(\\frac{x}{\\alpha}) - 1\\right), & x \\le 0
    \\end{cases}

  For more information, see
  `Continuously Differentiable Exponential Linear Units
  <https://arxiv.org/pdf/1704.07483.pdf>`_.

  Args:
    x : input array
    alpha : array or scalar (default: 1.0)

  Returns:
    An array.
  """
def selu(x: ArrayLike) -> Array:
    """Scaled exponential linear unit activation.

  Computes the element-wise function:

  .. math::
    \\mathrm{selu}(x) = \\lambda \\begin{cases}
      x, & x > 0\\\\\n      \\alpha e^x - \\alpha, & x \\le 0
    \\end{cases}

  where :math:`\\lambda = 1.0507009873554804934193349852946` and
  :math:`\\alpha = 1.6732632423543772848170429916717`.

  For more information, see
  `Self-Normalizing Neural Networks
  <https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf>`_.

  Args:
    x : input array

  Returns:
    An array.

  See also:
    :func:`elu`
  """
def gelu(x: ArrayLike, approximate: bool = True) -> Array:
    """Gaussian error linear unit activation function.

  If ``approximate=False``, computes the element-wise function:

  .. math::
    \\mathrm{gelu}(x) = \\frac{x}{2} \\left(1 + \\mathrm{erf} \\left(
      \\frac{x}{\\sqrt{2}} \\right) \\right)

  If ``approximate=True``, uses the approximate formulation of GELU:

  .. math::
    \\mathrm{gelu}(x) = \\frac{x}{2} \\left(1 + \\mathrm{tanh} \\left(
      \\sqrt{\\frac{2}{\\pi}} \\left(x + 0.044715 x^3 \\right) \\right) \\right)

  For more information, see `Gaussian Error Linear Units (GELUs)
  <https://arxiv.org/abs/1606.08415>`_, section 2.

  Args:
    x : input array
    approximate: whether to use the approximate or exact formulation.
  """
def glu(x: ArrayLike, axis: int = -1) -> Array:
    """Gated linear unit activation function.

  Computes the function:

  .. math::
    \\mathrm{glu}(x) =  x\\left[\\ldots, 0:\\frac{n}{2}, \\ldots\\right] \\cdot
      \\mathrm{sigmoid} \\left( x\\left[\\ldots, \\frac{n}{2}:n, \\ldots\\right]
        \\right)

  where the array is split into two along ``axis``. The size of the ``axis``
  dimension must be divisible by two.

  Args:
    x : input array
    axis: the axis along which the split should be computed (default: -1)

  Returns:
    An array.

  See also:
    :func:`sigmoid`
  """

logsumexp: Incomplete

def log_softmax(x: ArrayLike, axis: int | tuple[int, ...] | None = -1, where: ArrayLike | None = None, initial: ArrayLike | None = None) -> Array:
    """Log-Softmax function.

  Computes the logarithm of the :code:`softmax` function, which rescales
  elements to the range :math:`[-\\infty, 0)`.

  .. math ::
    \\mathrm{log\\_softmax}(x)_i = \\log \\left( \\frac{\\exp(x_i)}{\\sum_j \\exp(x_j)}
    \\right)

  Args:
    x : input array
    axis: the axis or axes along which the :code:`log_softmax` should be
      computed. Either an integer or a tuple of integers.
    where: Elements to include in the :code:`log_softmax`.
    initial: The minimum value used to shift the input array. Must be present
      when :code:`where` is not None.

  Returns:
    An array.

  See also:
    :func:`softmax`
  """
def softmax(x: ArrayLike, axis: int | tuple[int, ...] | None = -1, where: ArrayLike | None = None, initial: ArrayLike | None = None) -> Array:
    """Softmax function.

  Computes the function which rescales elements to the range :math:`[0, 1]`
  such that the elements along :code:`axis` sum to :math:`1`.

  .. math ::
    \\mathrm{softmax}(x) = \\frac{\\exp(x_i)}{\\sum_j \\exp(x_j)}

  Args:
    x : input array
    axis: the axis or axes along which the softmax should be computed. The
      softmax output summed across these dimensions should sum to :math:`1`.
      Either an integer or a tuple of integers.
    where: Elements to include in the :code:`softmax`.
    initial: The minimum value used to shift the input array. Must be present
      when :code:`where` is not None.

  Returns:
    An array.

  See also:
    :func:`log_softmax`
  """
def standardize(x: ArrayLike, axis: int | tuple[int, ...] | None = -1, mean: ArrayLike | None = None, variance: ArrayLike | None = None, epsilon: ArrayLike = 1e-05, where: ArrayLike | None = None) -> Array:
    """Normalizes an array by subtracting ``mean`` and dividing by :math:`\\sqrt{\\mathrm{variance}}`."""
def normalize(x: ArrayLike, axis: int | tuple[int, ...] | None = -1, mean: ArrayLike | None = None, variance: ArrayLike | None = None, epsilon: ArrayLike = 1e-05, where: ArrayLike | None = None) -> Array:
    """Normalizes an array by subtracting ``mean`` and dividing by :math:`\\sqrt{\\mathrm{variance}}`."""
def one_hot(x: Any, num_classes: int, *, dtype: Any = ..., axis: int | AxisName = -1) -> Array:
    """One-hot encodes the given indices.

  Each index in the input ``x`` is encoded as a vector of zeros of length
  ``num_classes`` with the element at ``index`` set to one::

    >>> jax.nn.one_hot(jnp.array([0, 1, 2]), 3)
    Array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]], dtype=float32)

  Indices outside the range [0, num_classes) will be encoded as zeros::

    >>> jax.nn.one_hot(jnp.array([-1, 3]), 3)
    Array([[0., 0., 0.],
           [0., 0., 0.]], dtype=float32)

  Args:
    x: A tensor of indices.
    num_classes: Number of classes in the one-hot dimension.
    dtype: optional, a float dtype for the returned values (default :obj:`jnp.float_`).
    axis: the axis or axes along which the function should be
      computed.
  """
def relu6(x: ArrayLike) -> Array:
    """Rectified Linear Unit 6 activation function.

  Computes the element-wise function

  .. math::
    \\mathrm{relu6}(x) = \\min(\\max(x, 0), 6)

  except under differentiation, we take:

  .. math::
    \\nabla \\mathrm{relu}(0) = 0

  and

  .. math::
    \\nabla \\mathrm{relu}(6) = 0

  Args:
    x : input array

  Returns:
    An array.

  See also:
    :func:`relu`
  """
def hard_sigmoid(x: ArrayLike) -> Array:
    """Hard Sigmoid activation function.

  Computes the element-wise function

  .. math::
    \\mathrm{hard\\_sigmoid}(x) = \\frac{\\mathrm{relu6}(x + 3)}{6}

  Args:
    x : input array

  Returns:
    An array.

  See also:
    :func:`relu6`
  """
def hard_silu(x: ArrayLike) -> Array:
    """Hard SiLU (swish) activation function

  Computes the element-wise function

  .. math::
    \\mathrm{hard\\_silu}(x) = x \\cdot \\mathrm{hard\\_sigmoid}(x)

  Both :func:`hard_silu` and :func:`hard_swish` are aliases for the same
  function.

  Args:
    x : input array

  Returns:
    An array.

  See also:
    :func:`hard_sigmoid`
  """
hard_swish = hard_silu
