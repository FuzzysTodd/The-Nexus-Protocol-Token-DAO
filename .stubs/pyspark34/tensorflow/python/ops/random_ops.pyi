from tensorflow.python.ops.gen_random_ops import *
from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, random_seed as random_seed, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_random_ops as gen_random_ops, math_ops as math_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def random_normal(shape, mean: float = 0.0, stddev: float = 1.0, dtype=..., seed: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs random values from a normal distribution.

  Example that generates a new set of random values every time:

  >>> tf.random.set_seed(5);
  >>> tf.random.normal([4], 0, 1, tf.float32)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=..., dtype=float32)>

  Example that outputs a reproducible result:

  >>> tf.random.set_seed(5);
  >>> tf.random.normal([2,2], 0, 1, tf.float32, seed=1)
  <tf.Tensor: shape=(2, 2), dtype=float32, numpy=
  array([[-1.3768897 , -0.01258316],
        [-0.169515   ,  1.0824056 ]], dtype=float32)>

  In this case, we are setting both the global and operation-level seed to
  ensure this result is reproducible.  See `tf.random.set_seed` for more
  information.

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    mean: A Tensor or Python value of type `dtype`, broadcastable with `stddev`.
      The mean of the normal distribution.
    stddev: A Tensor or Python value of type `dtype`, broadcastable with `mean`.
      The standard deviation of the normal distribution.
    dtype: The float type of the output: `float16`, `bfloat16`, `float32`,
      `float64`. Defaults to `float32`.
    seed: A Python integer. Used to create a random seed for the distribution.
      See
      `tf.random.set_seed`
      for behavior.
    name: A name for the operation (optional).

  Returns:
    A tensor of the specified shape filled with random normal values.
  """
def parameterized_truncated_normal(shape, means: float = 0.0, stddevs: float = 1.0, minvals: float = -2.0, maxvals: float = 2.0, dtype=..., seed: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs random values from a truncated normal distribution.

  The generated values follow a normal distribution with specified mean and
  standard deviation, except that values whose magnitude is more than 2 standard
  deviations from the mean are dropped and re-picked.

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    means: A 0-D Tensor or Python value of type `dtype`. The mean of the
      truncated normal distribution.
    stddevs: A 0-D Tensor or Python value of type `dtype`. The standard
      deviation of the truncated normal distribution.
    minvals: A 0-D Tensor or Python value of type `dtype`. The minimum value of
      the truncated normal distribution.
    maxvals: A 0-D Tensor or Python value of type `dtype`. The maximum value of
      the truncated normal distribution.
    dtype: The type of the output.
    seed: A Python integer. Used to create a random seed for the distribution.
      See
      `tf.random.set_seed`
      for behavior.
    name: A name for the operation (optional).

  Returns:
    A tensor of the specified shape filled with random truncated normal values.
  """
def truncated_normal(shape, mean: float = 0.0, stddev: float = 1.0, dtype=..., seed: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs random values from a truncated normal distribution.

  The values are drawn from a normal distribution with specified mean and
  standard deviation, discarding and re-drawing any samples that are more than
  two standard deviations from the mean.

  Examples:

  >>> tf.random.truncated_normal(shape=[2])
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>

  >>> tf.random.truncated_normal(shape=[2], mean=3, stddev=1, dtype=tf.float32)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    mean: A 0-D Tensor or Python value of type `dtype`. The mean of the
      truncated normal distribution.
    stddev: A 0-D Tensor or Python value of type `dtype`. The standard deviation
      of the normal distribution, before truncation.
    dtype: The type of the output. Restricted to floating-point types:
      `tf.half`, `tf.float`, `tf.double`, etc.
    seed: A Python integer. Used to create a random seed for the distribution.
      See `tf.random.set_seed` for more information.
    name: A name for the operation (optional).

  Returns:
    A tensor of the specified shape filled with random truncated normal values.
  """
def random_uniform(shape, minval: int = 0, maxval: Incomplete | None = None, dtype=..., seed: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs random values from a uniform distribution.

  The generated values follow a uniform distribution in the range
  `[minval, maxval)`. The lower bound `minval` is included in the range, while
  the upper bound `maxval` is excluded.

  For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
  be specified explicitly.

  In the integer case, the random integers are slightly biased unless
  `maxval - minval` is an exact power of two.  The bias is small for values of
  `maxval - minval` significantly smaller than the range of the output (either
  `2**32` or `2**64`).

  Examples:

  >>> tf.random.uniform(shape=[2])
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([..., ...], dtype=float32)>
  >>> tf.random.uniform(shape=[], minval=-1., maxval=0.)
  <tf.Tensor: shape=(), dtype=float32, numpy=-...>
  >>> tf.random.uniform(shape=[], minval=5, maxval=10, dtype=tf.int64)
  <tf.Tensor: shape=(), dtype=int64, numpy=...>

  The `seed` argument produces a deterministic sequence of tensors across
  multiple calls. To repeat that sequence, use `tf.random.set_seed`:

  >>> tf.random.set_seed(5)
  >>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
  <tf.Tensor: shape=(), dtype=int32, numpy=2>
  >>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
  <tf.Tensor: shape=(), dtype=int32, numpy=0>
  >>> tf.random.set_seed(5)
  >>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
  <tf.Tensor: shape=(), dtype=int32, numpy=2>
  >>> tf.random.uniform(shape=[], maxval=3, dtype=tf.int32, seed=10)
  <tf.Tensor: shape=(), dtype=int32, numpy=0>

  Without `tf.random.set_seed` but with a `seed` argument is specified, small
  changes to function graphs or previously executed operations will change the
  returned value. See `tf.random.set_seed` for details.

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    minval: A Tensor or Python value of type `dtype`, broadcastable with
      `shape` (for integer types, broadcasting is not supported, so it needs to
      be a scalar). The lower bound on the range of random values to generate
      (inclusive).  Defaults to 0.
    maxval: A Tensor or Python value of type `dtype`, broadcastable with
      `shape` (for integer types, broadcasting is not supported, so it needs to
      be a scalar). The upper bound on the range of random values to generate
      (exclusive). Defaults to 1 if `dtype` is floating point.
    dtype: The type of the output: `float16`, `bfloat16`, `float32`, `float64`,
      `int32`, or `int64`. Defaults to `float32`.
    seed: A Python integer. Used in combination with `tf.random.set_seed` to
      create a reproducible sequence of tensors across multiple calls.
    name: A name for the operation (optional).

  Returns:
    A tensor of the specified shape filled with random uniform values.

  Raises:
    ValueError: If `dtype` is integral and `maxval` is not specified.
  """
def random_shuffle(value, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Randomly shuffles a tensor along its first dimension.

  The tensor is shuffled along dimension 0, such that each `value[j]` is mapped
  to one and only one `output[i]`. For example, a mapping that might occur for a
  3x2 tensor is:

  ```python
  [[1, 2],       [[5, 6],
   [3, 4],  ==>   [1, 2],
   [5, 6]]        [3, 4]]
  ```

  Args:
    value: A Tensor to be shuffled.
    seed: A Python integer. Used to create a random seed for the distribution.
      See
      `tf.random.set_seed`
      for behavior.
    name: A name for the operation (optional).

  Returns:
    A tensor of same shape and type as `value`, shuffled along its first
    dimension.
  """
def random_crop(value, size, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Randomly crops a tensor to a given size.

  Slices a shape `size` portion out of `value` at a uniformly chosen offset.
  Requires `value.shape >= size`.

  If a dimension should not be cropped, pass the full size of that dimension.
  For example, RGB images can be cropped with
  `size = [crop_height, crop_width, 3]`.

  Example usage:

  >>> image = [[1, 2, 3], [4, 5, 6]]
  >>> result = tf.image.random_crop(value=image, size=(1, 3))
  >>> result.shape.as_list()
  [1, 3]

  For producing deterministic results given a `seed` value, use
  `tf.image.stateless_random_crop`. Unlike using the `seed` param with
  `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the same
  results given the same seed independent of how many times the function is
  called, and independent of global seed settings (e.g. tf.random.set_seed).

  Args:
    value: Input tensor to crop.
    size: 1-D tensor with size the rank of `value`.
    seed: Python integer. Used to create a random seed. See
      `tf.random.set_seed`
      for behavior.
    name: A name for this operation (optional).

  Returns:
    A cropped tensor of the same rank as `value` and shape `size`.
  """
def stateless_random_crop(value, size, seed, name: Incomplete | None = None):
    """Randomly crops a tensor to a given size in a deterministic manner.

  Slices a shape `size` portion out of `value` at a uniformly chosen offset.
  Requires `value.shape >= size`.

  If a dimension should not be cropped, pass the full size of that dimension.
  For example, RGB images can be cropped with
  `size = [crop_height, crop_width, 3]`.

  Guarantees the same results given the same `seed` independent of how many
  times the function is called, and independent of global seed settings (e.g.
  `tf.random.set_seed`).

  Usage Example:

  >>> image = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
  >>> seed = (1, 2)
  >>> tf.image.stateless_random_crop(value=image, size=(1, 2, 3), seed=seed)
  <tf.Tensor: shape=(1, 2, 3), dtype=int32, numpy=
  array([[[1, 2, 3],
          [4, 5, 6]]], dtype=int32)>

  Args:
    value: Input tensor to crop.
    size: 1-D tensor with size the rank of `value`.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    name: A name for this operation (optional).

  Returns:
    A cropped tensor of the same rank as `value` and shape `size`.
  """
def multinomial(logits, num_samples, seed: Incomplete | None = None, name: Incomplete | None = None, output_dtype: Incomplete | None = None):
    """Draws samples from a multinomial distribution.

  Example:

  ```python
  # samples has shape [1, 5], where each value is either 0 or 1 with equal
  # probability.
  samples = tf.random.categorical(tf.math.log([[0.5, 0.5]]), 5)
  ```

  Args:
    logits: 2-D Tensor with shape `[batch_size, num_classes]`.  Each slice
      `[i, :]` represents the unnormalized log-probabilities for all classes.
    num_samples: 0-D.  Number of independent samples to draw for each row slice.
    seed: A Python integer. Used to create a random seed for the distribution.
      See `tf.random.set_seed` for behavior.
    name: Optional name for the operation.
    output_dtype: The integer type of the output: `int32` or `int64`. Defaults
      to `int64`.

  Returns:
    The drawn samples of shape `[batch_size, num_samples]`.
  """
def categorical(logits, num_samples, dtype: Incomplete | None = None, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Draws samples from a categorical distribution.

  Example:

  ```python
  # samples has shape [1, 5], where each value is either 0 or 1 with equal
  # probability.
  samples = tf.random.categorical(tf.math.log([[0.5, 0.5]]), 5)
  ```

  Args:
    logits: 2-D Tensor with shape `[batch_size, num_classes]`.  Each slice
      `[i, :]` represents the unnormalized log-probabilities for all classes.
    num_samples: 0-D.  Number of independent samples to draw for each row slice.
    dtype: The integer type of the output: `int32` or `int64`. Defaults to
      `int64`.
    seed: A Python integer. Used to create a random seed for the distribution.
      See `tf.random.set_seed` for behavior.
    name: Optional name for the operation.

  Returns:
    The drawn samples of shape `[batch_size, num_samples]`.
  """
def multinomial_categorical_impl(logits, num_samples, dtype, seed):
    """Implementation for random.categorical (v1) and random.categorical (v2)."""
def random_gamma(shape, alpha, beta: Incomplete | None = None, dtype=..., seed: Incomplete | None = None, name: Incomplete | None = None):
    """Draws `shape` samples from each of the given Gamma distribution(s).

  `alpha` is the shape parameter describing the distribution(s), and `beta` is
  the inverse scale parameter(s).

  Note: Because internal calculations are done using `float64` and casting has
  `floor` semantics, we must manually map zero outcomes to the smallest
  possible positive floating-point value, i.e., `np.finfo(dtype).tiny`.  This
  means that `np.finfo(dtype).tiny` occurs more frequently than it otherwise
  should.  This bias can only happen for small values of `alpha`, i.e.,
  `alpha << 1` or large values of `beta`, i.e., `beta >> 1`.

  The samples are differentiable w.r.t. alpha and beta.
  The derivatives are computed using the approach described in
  (Figurnov et al., 2018).

  Example:

  ```python
  samples = tf.random.gamma([10], [0.5, 1.5])
  # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
  # the samples drawn from each distribution

  samples = tf.random.gamma([7, 5], [0.5, 1.5])
  # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
  # represents the 7x5 samples drawn from each of the two distributions

  alpha = tf.constant([[1.],[3.],[5.]])
  beta = tf.constant([[3., 4.]])
  samples = tf.random.gamma([30], alpha=alpha, beta=beta)
  # samples has shape [30, 3, 2], with 30 samples each of 3x2 distributions.

  loss = tf.reduce_mean(tf.square(samples))
  dloss_dalpha, dloss_dbeta = tf.gradients(loss, [alpha, beta])
  # unbiased stochastic derivatives of the loss function
  alpha.shape == dloss_dalpha.shape  # True
  beta.shape == dloss_dbeta.shape  # True
  ```

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output samples
      to be drawn per alpha/beta-parameterized distribution.
    alpha: A Tensor or Python value or N-D array of type `dtype`. `alpha`
      provides the shape parameter(s) describing the gamma distribution(s) to
      sample. Must be broadcastable with `beta`.
    beta: A Tensor or Python value or N-D array of type `dtype`. Defaults to 1.
      `beta` provides the inverse scale parameter(s) of the gamma
      distribution(s) to sample. Must be broadcastable with `alpha`.
    dtype: The type of alpha, beta, and the output: `float16`, `float32`, or
      `float64`.
    seed: A Python integer. Used to create a random seed for the distributions.
      See
      `tf.random.set_seed`
      for behavior.
    name: Optional name for the operation.

  Returns:
    samples: a `Tensor` of shape
      `tf.concat([shape, tf.shape(alpha + beta)], axis=0)` with values of type
      `dtype`.

  References:
    Implicit Reparameterization Gradients:
      [Figurnov et al., 2018]
      (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients)
      ([pdf]
      (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients.pdf))
  """
def random_poisson(lam, shape, dtype=..., seed: Incomplete | None = None, name: Incomplete | None = None):
    '''Draws `shape` samples from each of the given Poisson distribution(s).

  `lam` is the rate parameter describing the distribution(s).

  Example:

  ```python
  samples = tf.random.poisson([0.5, 1.5], [10])
  # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
  # the samples drawn from each distribution

  samples = tf.random.poisson([12.2, 3.3], [7, 5])
  # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
  # represents the 7x5 samples drawn from each of the two distributions
  ```

  Args:
    lam: A Tensor or Python value or N-D array of type `dtype`.
      `lam` provides the rate parameter(s) describing the poisson
      distribution(s) to sample.
    shape: A 1-D integer Tensor or Python array. The shape of the output samples
      to be drawn per "rate"-parameterized distribution.
    dtype: The type of the output: `float16`, `float32`, `float64`, `int32` or
      `int64`.
    seed: A Python integer. Used to create a random seed for the distributions.
      See
      `tf.random.set_seed`
      for behavior.
    name: Optional name for the operation.

  Returns:
    samples: a `Tensor` of shape `tf.concat([shape, tf.shape(lam)], axis=0)`
      with values of type `dtype`.
  '''
def random_poisson_v2(shape, lam, dtype=..., seed: Incomplete | None = None, name: Incomplete | None = None):
    '''Draws `shape` samples from each of the given Poisson distribution(s).

  `lam` is the rate parameter describing the distribution(s).

  Example:

  ```python
  samples = tf.random.poisson([10], [0.5, 1.5])
  # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
  # the samples drawn from each distribution

  samples = tf.random.poisson([7, 5], [12.2, 3.3])
  # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
  # represents the 7x5 samples drawn from each of the two distributions
  ```

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output samples
      to be drawn per "rate"-parameterized distribution.
    lam: A Tensor or Python value or N-D array of type `dtype`.
      `lam` provides the rate parameter(s) describing the poisson
      distribution(s) to sample.
    dtype: The type of the output: `float16`, `float32`, `float64`, `int32` or
      `int64`.
    seed: A Python integer. Used to create a random seed for the distributions.
      See
      `tf.random.set_seed`
      for behavior.
    name: Optional name for the operation.

  Returns:
    samples: a `Tensor` of shape `tf.concat([shape, tf.shape(lam)], axis=0)`
      with values of type `dtype`.
  '''
