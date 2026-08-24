from _typeshed import Incomplete
from collections.abc import Sequence
from jax import lax as lax, random as random
from jax._src import core as core, dtypes as dtypes
from jax._src.typing import Array as Array, ArrayLike as ArrayLike
from jax._src.util import set_module as set_module
from typing import Any, Literal, Protocol

export: Incomplete
KeyArray = Array
DTypeLikeFloat = Any
DTypeLikeComplex = Any
DTypeLikeInexact = Any
RealNumeric = Any

class Initializer(Protocol):
    @staticmethod
    def __call__(key: KeyArray, shape: core.Shape, dtype: DTypeLikeInexact = ...) -> Array: ...

def zeros(key: KeyArray, shape: core.Shape, dtype: DTypeLikeInexact = ...) -> Array:
    """An initializer that returns a constant array full of zeros.

  The ``key`` argument is ignored.

  >>> import jax, jax.numpy as jnp
  >>> jax.nn.initializers.zeros(jax.random.PRNGKey(42), (2, 3), jnp.float32)
  Array([[0., 0., 0.],
         [0., 0., 0.]], dtype=float32)
  """
def ones(key: KeyArray, shape: core.Shape, dtype: DTypeLikeInexact = ...) -> Array:
    """An initializer that returns a constant array full of ones.

  The ``key`` argument is ignored.

  >>> import jax, jax.numpy as jnp
  >>> jax.nn.initializers.ones(jax.random.PRNGKey(42), (3, 2), jnp.float32)
  Array([[1., 1.],
         [1., 1.],
         [1., 1.]], dtype=float32)
  """
def constant(value: ArrayLike, dtype: DTypeLikeInexact = ...) -> Initializer:
    """Builds an initializer that returns arrays full of a constant ``value``.

  Args:
    value: the constant value with which to fill the initializer.
    dtype: optional; the initializer's default dtype.

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.constant(-7)
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)
  Array([[-7., -7., -7.],
         [-7., -7., -7.]], dtype=float32)
  """
def uniform(scale: RealNumeric = 0.01, dtype: DTypeLikeInexact = ...) -> Initializer:
    """Builds an initializer that returns real uniformly-distributed random arrays.

  Args:
    scale: optional; the upper bound of the random distribution.
    dtype: optional; the initializer's default dtype.

  Returns:
    An initializer that returns arrays whose values are uniformly distributed in
    the range ``[0, scale)``.

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.uniform(10.0)
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[7.298188 , 8.691938 , 8.7230015],
         [2.0818567, 1.8662417, 5.5022564]], dtype=float32)
  """
def normal(stddev: RealNumeric = 0.01, dtype: DTypeLikeInexact = ...) -> Initializer:
    """Builds an initializer that returns real normally-distributed random arrays.

  Args:
    stddev: optional; the standard deviation of the distribution.
    dtype: optional; the initializer's default dtype.

  Returns:
    An initializer that returns arrays whose values are normally distributed
    with mean ``0`` and standard deviation ``stddev``.

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.normal(5.0)
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 3.0613258 ,  5.6129413 ,  5.6866574 ],
         [-4.063663  , -4.4520254 ,  0.63115686]], dtype=float32)
  """
def truncated_normal(stddev: RealNumeric = 0.01, dtype: DTypeLikeInexact = ..., lower: RealNumeric = -2.0, upper: RealNumeric = 2.0) -> Initializer:
    """Builds an initializer that returns truncated-normal random arrays.

  Args:
    stddev: optional; the standard deviation of the untruncated distribution.
      Note that this function does not apply the stddev correction as is done in
      the variancescaling initializers, and users are expected to apply this
      correction themselves via the stddev arg if they wish to employ it.
    dtype: optional; the initializer's default dtype.
    min_val: Float representing the lower bound for truncation. Applied before
      the output is multiplied by the stddev.
    max_val: Float representing the upper bound for truncation. Applied before
      the output is multiplied by the stddev.

  Returns:
    An initializer that returns arrays whose values follow the truncated normal
    distribution with mean ``0`` and standard deviation ``stddev``, and range
    :math:`\\rm{lower * stddev} < x < \\rm{upper * stddev}`.

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.truncated_normal(5.0)
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 2.9047365,  5.2338114,  5.29852  ],
         [-3.836303 , -4.192359 ,  0.6022964]], dtype=float32)
  """
def variance_scaling(scale: RealNumeric, mode: Literal['fan_in'] | Literal['fan_out'] | Literal['fan_avg'], distribution: Literal['truncated_normal'] | Literal['normal'] | Literal['uniform'], in_axis: int | Sequence[int] = -2, out_axis: int | Sequence[int] = -1, batch_axis: Sequence[int] = (), dtype: DTypeLikeInexact = ...) -> Initializer:
    '''
  Initializer that adapts its scale to the shape of the weights tensor.

  With ``distribution="truncated_normal"`` or ``distribution="normal"``, samples
  are drawn from a (truncated) normal distribution with a mean of zero
  and a standard deviation (after truncation, if applicable) of
  :math:`\\sqrt{\\frac{scale}{n}}`, where `n` is:

  * the number of input units in the weights tensor, if ``mode="fan_in"``,
  * the number of output units, if ``mode="fan_out"``, or
  * the average of the numbers of input and output units, if ``mode="fan_avg"``.

  This initializer can be configured with ``in_axis``, ``out_axis``, and
  ``batch_axis`` to work with general convolutional or dense layers; axes that
  are not in any of those arguments are assumed to be the "receptive field"
  (convolution kernel spatial axes).

  With ``distribution="truncated_normal"``, the absolute values of the samples
  are truncated at 2 standard deviations before scaling.

  With ``distribution="uniform"``, samples are drawn from:

  * a uniform interval, if `dtype` is real, or
  * a uniform disk, if `dtype` is complex,

  with a mean of zero and a standard deviation of :math:`\\sqrt{\\frac{scale}{n}}`
  where `n` is defined above.

  Args:
    scale: scaling factor (positive float).
    mode: one of ``"fan_in"``, ``"fan_out"``, and ``"fan_avg"``.
    distribution: random distribution to use. One of ``"truncated_normal"``,
      ``"normal"`` and ``"uniform"``.
    in_axis: axis or sequence of axes of the input dimension in the weights
      array.
    out_axis: axis or sequence of axes of the output dimension in the weights
      array.
    batch_axis: axis or sequence of axes in the weight array that should be
      ignored.
    dtype: the dtype of the weights.
  '''
def glorot_uniform(in_axis: int | Sequence[int] = -2, out_axis: int | Sequence[int] = -1, batch_axis: Sequence[int] = (), dtype: DTypeLikeInexact = ...) -> Initializer:
    '''Builds a Glorot uniform initializer (aka Xavier uniform initializer).

  A `Glorot uniform initializer`_ is a specialization of
  :func:`jax.nn.initializers.variance_scaling` where ``scale = 1.0``,
  ``mode="fan_avg"``, and ``distribution="uniform"``.

  Args:
    in_axis: axis or sequence of axes of the input dimension in the weights
      array.
    out_axis: axis or sequence of axes of the output dimension in the weights
      array.
    batch_axis: axis or sequence of axes in the weight array that should be
      ignored.
    dtype: the dtype of the weights.

  Returns:
    An initializer.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.glorot_uniform()
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 0.50350785,  0.8088631 ,  0.81566876],
         [-0.6393332 , -0.6865721 ,  0.11003882]], dtype=float32)

  .. _Glorot uniform initializer: http://proceedings.mlr.press/v9/glorot10a.html
  '''
xavier_uniform = glorot_uniform

def glorot_normal(in_axis: int | Sequence[int] = -2, out_axis: int | Sequence[int] = -1, batch_axis: Sequence[int] = (), dtype: DTypeLikeInexact = ...) -> Initializer:
    '''Builds a Glorot normal initializer (aka Xavier normal initializer).

  A `Glorot normal initializer`_ is a specialization of
  :func:`jax.nn.initializers.variance_scaling` where ``scale = 1.0``,
  ``mode="fan_avg"``, and ``distribution="truncated_normal"``.

  Args:
    in_axis: axis or sequence of axes of the input dimension in the weights
      array.
    out_axis: axis or sequence of axes of the output dimension in the weights
      array.
    batch_axis: axis or sequence of axes in the weight array that should be
      ignored.
    dtype: the dtype of the weights.

  Returns:
    An initializer.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.glorot_normal()
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 0.41770416,  0.75262755,  0.7619329 ],
         [-0.5516644 , -0.6028657 ,  0.08661086]], dtype=float32)

  .. _Glorot normal initializer: http://proceedings.mlr.press/v9/glorot10a.html
  '''
xavier_normal = glorot_normal

def lecun_uniform(in_axis: int | Sequence[int] = -2, out_axis: int | Sequence[int] = -1, batch_axis: Sequence[int] = (), dtype: DTypeLikeInexact = ...) -> Initializer:
    '''Builds a Lecun uniform initializer.

  A `Lecun uniform initializer`_ is a specialization of
  :func:`jax.nn.initializers.variance_scaling` where ``scale = 1.0``,
  ``mode="fan_in"``, and ``distribution="uniform"``.

  Args:
    in_axis: axis or sequence of axes of the input dimension in the weights
      array.
    out_axis: axis or sequence of axes of the output dimension in the weights
      array.
    batch_axis: axis or sequence of axes in the weight array that should be
      ignored.
    dtype: the dtype of the weights.

  Returns:
    An initializer.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.lecun_uniform()
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 0.56293887,  0.90433645,  0.9119454 ],
         [-0.71479625, -0.7676109 ,  0.12302713]], dtype=float32)

  .. _Lecun uniform initializer: https://arxiv.org/abs/1706.02515
  '''
def lecun_normal(in_axis: int | Sequence[int] = -2, out_axis: int | Sequence[int] = -1, batch_axis: Sequence[int] = (), dtype: DTypeLikeInexact = ...) -> Initializer:
    '''Builds a Lecun normal initializer.

  A `Lecun normal initializer`_ is a specialization of
  :func:`jax.nn.initializers.variance_scaling` where ``scale = 1.0``,
  ``mode="fan_in"``, and ``distribution="truncated_normal"``.

  Args:
    in_axis: axis or sequence of axes of the input dimension in the weights
      array.
    out_axis: axis or sequence of axes of the output dimension in the weights
      array.
    batch_axis: axis or sequence of axes in the weight array that should be
      ignored.
    dtype: the dtype of the weights.

  Returns:
    An initializer.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.lecun_normal()
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 0.46700746,  0.8414632 ,  0.8518669 ],
         [-0.61677957, -0.67402434,  0.09683388]], dtype=float32)

  .. _Lecun normal initializer: https://arxiv.org/abs/1706.02515
  '''
def he_uniform(in_axis: int | Sequence[int] = -2, out_axis: int | Sequence[int] = -1, batch_axis: Sequence[int] = (), dtype: DTypeLikeInexact = ...) -> Initializer:
    '''Builds a He uniform initializer (aka Kaiming uniform initializer).

  A `He uniform initializer`_ is a specialization of
  :func:`jax.nn.initializers.variance_scaling` where ``scale = 2.0``,
  ``mode="fan_in"``, and ``distribution="uniform"``.

  Args:
    in_axis: axis or sequence of axes of the input dimension in the weights
      array.
    out_axis: axis or sequence of axes of the output dimension in the weights
      array.
    batch_axis: axis or sequence of axes in the weight array that should be
      ignored.
    dtype: the dtype of the weights.

  Returns:
    An initializer.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.he_uniform()
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 0.79611576,  1.2789248 ,  1.2896855 ],
         [-1.0108745 , -1.0855657 ,  0.17398663]], dtype=float32)

  .. _He uniform initializer: https://arxiv.org/abs/1502.01852
  '''
kaiming_uniform = he_uniform

def he_normal(in_axis: int | Sequence[int] = -2, out_axis: int | Sequence[int] = -1, batch_axis: Sequence[int] = (), dtype: DTypeLikeInexact = ...) -> Initializer:
    '''Builds a He normal initializer (aka Kaiming normal initializer).

  A `He normal initializer`_ is a specialization of
  :func:`jax.nn.initializers.variance_scaling` where ``scale = 2.0``,
  ``mode="fan_in"``, and ``distribution="truncated_normal"``.

  Args:
    in_axis: axis or sequence of axes of the input dimension in the weights
      array.
    out_axis: axis or sequence of axes of the output dimension in the weights
      array.
    batch_axis: axis or sequence of axes in the weight array that should be
      ignored.
    dtype: the dtype of the weights.

  Returns:
    An initializer.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.he_normal()
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 0.6604483 ,  1.1900088 ,  1.2047218 ],
         [-0.87225807, -0.95321447,  0.1369438 ]], dtype=float32)

  .. _He normal initializer: https://arxiv.org/abs/1502.01852
  '''
kaiming_normal = he_normal

def orthogonal(scale: RealNumeric = 1.0, column_axis: int = -1, dtype: DTypeLikeInexact = ...) -> Initializer:
    """
  Builds an initializer that returns uniformly distributed orthogonal matrices.

  If the shape is not square, the matrices will have orthonormal rows or columns
  depending on which side is smaller.

  Args:
    scale: the upper bound of the uniform distribution.
    column_axis: the axis that contains the columns that should be orthogonal.
    dtype: the default dtype of the weights.

  Returns:
    An orthogonal initializer.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.orthogonal()
  >>> initializer(jax.random.PRNGKey(42), (2, 3), jnp.float32)  # doctest: +SKIP
  Array([[ 3.9026976e-01,  7.2495741e-01, -5.6756169e-01],
         [ 8.8047469e-01, -4.7409311e-01, -1.3157725e-04]],            dtype=float32)
  """
def delta_orthogonal(scale: RealNumeric = 1.0, column_axis: int = -1, dtype: DTypeLikeInexact = ...) -> Initializer:
    """
  Builds an initializer for delta orthogonal kernels.

  Args:
    scale: the upper bound of the uniform distribution.
    column_axis: the axis that contains the columns that should be orthogonal.
    dtype: the default dtype of the weights.

  Returns:
    A `delta orthogonal initializer`_. The shape passed to the initializer must
    be 3D, 4D, or 5D.

  Example:

  >>> import jax, jax.numpy as jnp
  >>> initializer = jax.nn.initializers.delta_orthogonal()
  >>> initializer(jax.random.PRNGKey(42), (3, 3, 3), jnp.float32)  # doctest: +SKIP
  Array([[[ 0.        ,  0.        ,  0.        ],
          [ 0.        ,  0.        ,  0.        ],
          [ 0.        ,  0.        ,  0.        ]],
  <BLANKLINE>
         [[ 0.27858758, -0.7949833 , -0.53887904],
          [ 0.9120717 ,  0.04322892,  0.40774566],
          [-0.30085585, -0.6050892 ,  0.73712474]],
  <BLANKLINE>
         [[ 0.        ,  0.        ,  0.        ],
          [ 0.        ,  0.        ,  0.        ],
          [ 0.        ,  0.        ,  0.        ]]], dtype=float32)


  .. _delta orthogonal initializer: https://arxiv.org/abs/1806.05393
  """
