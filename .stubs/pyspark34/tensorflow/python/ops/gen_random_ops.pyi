from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def multinomial(logits, num_samples, seed: int = 0, seed2: int = 0, output_dtype=..., name: Incomplete | None = None):
    """Draws samples from a multinomial distribution.

  Args:
    logits: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
      2-D Tensor with shape `[batch_size, num_classes]`.  Each slice `[i, :]`
      represents the unnormalized log probabilities for all classes.
    num_samples: A `Tensor` of type `int32`.
      0-D.  Number of independent samples to draw for each row slice.
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 is set to be non-zero, the internal random number
      generator is seeded by the given seed.  Otherwise, a random seed is used.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    output_dtype: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `output_dtype`.
  """

Multinomial: Incomplete

def multinomial_eager_fallback(logits, num_samples, seed, seed2, output_dtype, name, ctx): ...
def parameterized_truncated_normal(shape, means, stdevs, minvals, maxvals, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Outputs random values from a normal distribution. The parameters may each be a

  scalar which applies to the entire output, or a vector of length shape[0] which
  stores the parameters for each batch.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor. Batches are indexed by the 0th dimension.
    means: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
      The mean parameter of each batch.
    stdevs: A `Tensor`. Must have the same type as `means`.
      The standard deviation parameter of each batch. Must be greater than 0.
    minvals: A `Tensor`. Must have the same type as `means`.
      The minimum cutoff. May be -infinity.
    maxvals: A `Tensor`. Must have the same type as `means`.
      The maximum cutoff. May be +infinity, and must be more than the minval
      for each batch.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `means`.
  """

ParameterizedTruncatedNormal: Incomplete

def parameterized_truncated_normal_eager_fallback(shape, means, stdevs, minvals, maxvals, seed, seed2, name, ctx): ...
def random_gamma(shape, alpha, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    '''Outputs random values from the Gamma distribution(s) described by alpha.

  This op uses the algorithm by Marsaglia et al. to acquire samples via
  transformation-rejection from pairs of uniform and normal random variables.
  See http://dl.acm.org/citation.cfm?id=358414

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      1-D integer tensor. Shape of independent samples to draw from each
      distribution described by the shape parameters given in alpha.
    alpha: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
      A tensor in which each scalar is a "shape" parameter describing the
      associated gamma distribution.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `alpha`.
  '''

RandomGamma: Incomplete

def random_gamma_eager_fallback(shape, alpha, seed, seed2, name, ctx): ...
def random_gamma_grad(alpha, sample, name: Incomplete | None = None):
    """Computes the derivative of a Gamma random sample w.r.t. `alpha`.

  Args:
    alpha: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    sample: A `Tensor`. Must have the same type as `alpha`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `alpha`.
  """

RandomGammaGrad: Incomplete

def random_gamma_grad_eager_fallback(alpha, sample, name, ctx): ...
def random_poisson(shape, rate, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Use RandomPoissonV2 instead.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    rate: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
    seed: An optional `int`. Defaults to `0`.
    seed2: An optional `int`. Defaults to `0`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `rate`.
  """

RandomPoisson: Incomplete

def random_poisson_eager_fallback(shape, rate, seed, seed2, name, ctx): ...
def random_poisson_v2(shape, rate, seed: int = 0, seed2: int = 0, dtype=..., name: Incomplete | None = None):
    '''Outputs random values from the Poisson distribution(s) described by rate.

  This op uses two algorithms, depending on rate. If rate >= 10, then
  the algorithm by Hormann is used to acquire samples via
  transformation-rejection.
  See http://www.sciencedirect.com/science/article/pii/0167668793909974.

  Otherwise, Knuth\'s algorithm is used to acquire samples via multiplying uniform
  random variables.
  See Donald E. Knuth (1969). Seminumerical Algorithms. The Art of Computer
  Programming, Volume 2. Addison Wesley

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      1-D integer tensor. Shape of independent samples to draw from each
      distribution described by the shape parameters given in rate.
    rate: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`.
      A tensor in which each scalar is a "rate" parameter describing the
      associated poisson distribution.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    dtype: An optional `tf.DType` from: `tf.half, tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  '''

RandomPoissonV2: Incomplete

def random_poisson_v2_eager_fallback(shape, rate, seed, seed2, dtype, name, ctx): ...
def random_shuffle(value, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Randomly shuffles a tensor along its first dimension.

    The tensor is shuffled along dimension 0, such that each `value[j]` is mapped
    to one and only one `output[i]`. For example, a mapping that might occur for a
    3x2 tensor is:

  ```
  [[1, 2],       [[5, 6],
   [3, 4],  ==>   [1, 2],
   [5, 6]]        [3, 4]]
  ```

  Args:
    value: A `Tensor`. The tensor to be shuffled.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `value`.
  """

RandomShuffle: Incomplete

def random_shuffle_eager_fallback(value, seed, seed2, name, ctx): ...
def random_standard_normal(shape, dtype, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Outputs random values from a normal distribution.

  The generated values will have mean 0 and standard deviation 1.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    dtype: A `tf.DType` from: `tf.half, tf.bfloat16, tf.float32, tf.float64`.
      The type of the output.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

RandomStandardNormal: Incomplete

def random_standard_normal_eager_fallback(shape, dtype, seed, seed2, name, ctx): ...
def random_uniform(shape, dtype, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Outputs random values from a uniform distribution.

  The generated values follow a uniform distribution in the range `[0, 1)`. The
  lower bound 0 is included in the range, while the upper bound 1 is excluded.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    dtype: A `tf.DType` from: `tf.half, tf.bfloat16, tf.float32, tf.float64`.
      The type of the output.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

RandomUniform: Incomplete

def random_uniform_eager_fallback(shape, dtype, seed, seed2, name, ctx): ...
def random_uniform_int(shape, minval, maxval, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Outputs random integers from a uniform distribution.

  The generated values are uniform integers in the range `[minval, maxval)`.
  The lower bound `minval` is included in the range, while the upper bound
  `maxval` is excluded.

  The random integers are slightly biased unless `maxval - minval` is an exact
  power of two.  The bias is small for values of `maxval - minval` significantly
  smaller than the range of the output (either `2^32` or `2^64`).

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    minval: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      0-D.  Inclusive lower bound on the generated integers.
    maxval: A `Tensor`. Must have the same type as `minval`.
      0-D.  Exclusive upper bound on the generated integers.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `minval`.
  """

RandomUniformInt: Incomplete

def random_uniform_int_eager_fallback(shape, minval, maxval, seed, seed2, name, ctx): ...
def truncated_normal(shape, dtype, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Outputs random values from a truncated normal distribution.

  The generated values follow a normal distribution with mean 0 and standard
  deviation 1, except that values whose magnitude is more than 2 standard
  deviations from the mean are dropped and re-picked.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    dtype: A `tf.DType` from: `tf.half, tf.bfloat16, tf.float32, tf.float64`.
      The type of the output.
    seed: An optional `int`. Defaults to `0`.
      If either `seed` or `seed2` are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      A second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

TruncatedNormal: Incomplete

def truncated_normal_eager_fallback(shape, dtype, seed, seed2, name, ctx): ...
