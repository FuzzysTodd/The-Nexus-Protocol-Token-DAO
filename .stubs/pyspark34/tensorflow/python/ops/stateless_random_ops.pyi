import enum
from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, bitwise_ops as bitwise_ops, gen_random_index_shuffle_ops as gen_random_index_shuffle_ops, gen_stateless_random_ops as gen_stateless_random_ops, gen_stateless_random_ops_v2 as gen_stateless_random_ops_v2, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

class Algorithm(enum.Enum):
    '''A random-number-generation (RNG) algorithm.

  Many random-number generators (e.g. the `alg` argument of
  `tf.random.Generator` and `tf.random.stateless_uniform`) in TF allow
  you to choose the algorithm used to generate the (pseudo-)random
  numbers. You can set the algorithm to be one of the options below.

  * `PHILOX`: The Philox algorithm introduced in the paper ["Parallel
    Random Numbers: As Easy as 1, 2,
    3"](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf).
  * `THREEFRY`: The ThreeFry algorithm introduced in the paper
    ["Parallel Random Numbers: As Easy as 1, 2,
    3"](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf).
  * `AUTO_SELECT`: Allow TF to automatically select the algorithm
    depending on the accelerator device. Note that with this option,
    running the same TF program on different devices may result in
    different random numbers. Also note that TF may select an
    algorithm that is different from `PHILOX` and `THREEFRY`.
  '''
    PHILOX: int
    THREEFRY: int
    AUTO_SELECT: int

def unsupported_alg_error_msg(alg):
    """Produces the unsupported-algorithm error message."""
def convert_alg_to_int(alg):
    '''Converts algorithm to an integer.

  Args:
    alg: can be one of these types: integer, Algorithm, Tensor, string. Allowed
      strings are "philox" and "threefry".

  Returns:
    An integer, unless the input is a Tensor in which case a Tensor is returned.
  '''
def uint32s_to_uint64(x): ...
def split(seed, num: int = 2, alg: str = 'auto_select'):
    """Splits an RNG seed into `num` new seeds by adding a leading axis.

  Example:

  >>> seed = [1, 2]
  >>> new_seeds = tf.random.split(seed, num=3)
  >>> print(new_seeds)
  tf.Tensor(
  [[1105988140 1738052849]
   [-335576002  370444179]
   [  10670227 -246211131]], shape=(3, 2), dtype=int32)
  >>> tf.random.stateless_normal(shape=[3], seed=new_seeds[0, :])
  <tf.Tensor: shape=(3,), dtype=float32, numpy=array([-0.59835213, -0.9578608 ,
  0.9002807 ], dtype=float32)>

  Args:
    seed: an RNG seed (a tensor with shape [2] and dtype `int32` or
      `int64`). (When using XLA, only `int32` is allowed.)
    num: optional, a positive integer or scalar tensor indicating the number of
      seeds to produce (default 2).
    alg: The RNG algorithm used to generate the random numbers. See
      `tf.random.stateless_uniform` for a detailed explanation.

  Returns:
    A tensor with shape [num, 2] representing `num` new seeds. It will have the
    same dtype as `seed` (if `seed` doesn't have an explict dtype, the dtype
    will be determined by `tf.convert_to_tensor`).
  """
def fold_in(seed, data, alg: str = 'auto_select'):
    '''Folds in data to an RNG seed to form a new RNG seed.

  For example, in a distributed-training setting, suppose we have a master seed
  and a replica ID. We want to fold the replica ID into the master seed to
  form a "replica seed" to be used by that replica later on, so that different
  replicas will generate different random numbers but the reproducibility of the
  whole system can still be controlled by the master seed:

  >>> master_seed = [1, 2]
  >>> replica_id = 3
  >>> replica_seed = tf.random.experimental.stateless_fold_in(
  ...   master_seed, replica_id)
  >>> print(replica_seed)
  tf.Tensor([1105988140          3], shape=(2,), dtype=int32)
  >>> tf.random.stateless_normal(shape=[3], seed=replica_seed)
  <tf.Tensor: shape=(3,), dtype=float32, numpy=array([0.03197195, 0.8979765 ,
  0.13253039], dtype=float32)>

  Args:
    seed: an RNG seed (a tensor with shape [2] and dtype `int32` or
      `int64`). (When using XLA, only `int32` is allowed.)
    data: an `int32` or `int64` scalar representing data to be folded in to the
      seed.
    alg: The RNG algorithm used to generate the random numbers. See
      `tf.random.stateless_uniform` for a detailed explanation.

  Returns:
    A new RNG seed that is a deterministic function of the inputs and is
    statistically safe for producing a stream of new pseudo-random values. It
    will have the same dtype as `data` (if `data` doesn\'t have an explict dtype,
    the dtype will be determined by `tf.convert_to_tensor`).
  '''
def index_shuffle(index, seed, max_index):
    """Outputs the position of `index` in a permutation of `[0, ..., max_index]`.

  For each possible `seed` and `max_index` there is one pseudorandom
  permutation of the sequence `S=[0, ..., max_index]`. Instead of
  materializing the full array we can compute the new position of any
  integer `i` (`0 <= i <= max_index`) in `S`. This can be useful for
  very large `max_index`s by avoiding allocating large chunks of
  memory.

  In the simplest case, `index` and `max_index` are scalars, and
  `seed` is a length-2 vector (as typical for stateless RNGs). But
  you can add a leading batch dimension to all of them. If some of
  them don't have the batch dimension while others do, `index_shuffle`
  will add a batch dimension to the former by broadcasting.

  The input `index` and output can be used as indices to shuffle a
  vector.  For example:

  >>> vector = tf.constant(['e0', 'e1', 'e2', 'e3'])
  >>> indices = tf.random.experimental.index_shuffle(
  ...   index=tf.range(4), seed=[5, 9], max_index=3)
  >>> print(indices)
  tf.Tensor([2 0 1 3], shape=(4,), dtype=int32)
  >>> shuffled_vector = tf.gather(vector, indices)
  >>> print(shuffled_vector)
  tf.Tensor([b'e2' b'e0' b'e1' b'e3'], shape=(4,), dtype=string)

  More usefully, it can be used in a streaming (aka online) scenario such as
  `tf.data`, where each element of `vector` is processed individually and the
  whole `vector` is never materialized in memory.

  >>> dataset = tf.data.Dataset.range(10)
  >>> dataset = dataset.map(
  ...  lambda idx: tf.random.experimental.index_shuffle(idx, [5, 8], 9))
  >>> print(list(dataset.as_numpy_iterator()))
  [3, 8, 0, 1, 2, 7, 6, 9, 4, 5]

  This operation is stateless (like the `tf.random.stateless_*`
  functions), meaning the output is fully determined by the `seed`
  (other inputs being equal).  Each `seed` choice corresponds to one
  permutation, so when calling this function multiple times for the
  same shuffling, please make sure to use the same `seed`. For
  example:

  >>> seed = [5, 9]
  >>> idx0 = tf.random.experimental.index_shuffle(0, seed, 3)
  >>> idx1 = tf.random.experimental.index_shuffle(1, seed, 3)
  >>> idx2 = tf.random.experimental.index_shuffle(2, seed, 3)
  >>> idx3 = tf.random.experimental.index_shuffle(3, seed, 3)
  >>> shuffled_vector = tf.gather(vector, [idx0, idx1, idx2, idx3])
  >>> print(shuffled_vector)
  tf.Tensor([b'e2' b'e0' b'e1' b'e3'], shape=(4,), dtype=string)

  Args:
    index: An integer scalar tensor or vector with values in `[0,
      max_index]`.  It can be seen as either a value `v` in the
      sequence `S=[0, ..., max_index]` to be permutated, or as an
      index of an element `e` in a shuffled vector.
    seed: A tensor of shape [2] or [n, 2] with dtype `int32`,
      `uint32`, `int64` or `uint64`.  The RNG seed. If the rank is
      unknown during graph-building time it must be 1 at runtime.
    max_index: A non-negative tensor with the same shape and dtype as
      `index`.  The upper bound (inclusive).

  Returns:
    If all inputs were scalar (shape [2] for `seed`), the output will
    be a scalar with the same dtype as `index`. The output can be seen
    as the new position of `v` in `S`, or as the index of `e` in the
    vector before shuffling.  If one or multiple inputs were vectors
    (shape [n, 2] for `seed`), then the output will be a vector of the
    same size which each element shuffled independently. Scalar values
    are broadcasted in this case.
  """
def stateless_shuffle(value, seed, alg: str = 'auto_select', name: Incomplete | None = None):
    """Randomly and deterministically shuffles a tensor along its first dimension.

  The tensor is shuffled along dimension 0, such that each `value[j]` is mapped
  to one and only one `output[i]`. For example, a mapping that might occur for a
  3x2 tensor is:

  ```python
  [[1, 2],       [[5, 6],
   [3, 4],  ==>   [1, 2],
   [5, 6]]        [3, 4]]
  ```

  >>> v = tf.constant([[1, 2], [3, 4], [5, 6]])
  >>> shuffled = tf.random.experimental.stateless_shuffle(v, seed=[8, 9])
  >>> print(shuffled)
  tf.Tensor(
  [[5 6]
    [1 2]
    [3 4]], shape=(3, 2), dtype=int32)

  This is a stateless version of `tf.random.shuffle`: if run twice with the
  same `value` and `seed`, it will produce the same result.  The
  output is consistent across multiple runs on the same hardware (and between
  CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
  hardware.

  Args:
    value: A Tensor to be shuffled.
    seed: A shape [2] Tensor. The seed to the random number generator. Must have
      dtype `int32` or `int64`.
    alg: The RNG algorithm used to generate the random numbers. See
      `tf.random.stateless_uniform` for a detailed explanation.
    name: A name for the operation.

  Returns:
    A tensor of same shape and type as `value`, shuffled along its first
    dimension.
  """
def stateless_random_uniform(shape, seed, minval: int = 0, maxval: Incomplete | None = None, dtype=..., name: Incomplete | None = None, alg: str = 'auto_select'):
    '''Outputs deterministic pseudorandom values from a uniform distribution.

  This is a stateless version of `tf.random.uniform`: if run twice with the
  same seeds and shapes, it will produce the same pseudorandom numbers.  The
  output is consistent across multiple runs on the same hardware (and between
  CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
  hardware.

  The generated values follow a uniform distribution in the range
  `[minval, maxval)`. The lower bound `minval` is included in the range, while
  the upper bound `maxval` is excluded.

  For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
  be specified explicitly.

  In the integer case, the random integers are slightly biased unless
  `maxval - minval` is an exact power of two.  The bias is small for values of
  `maxval - minval` significantly smaller than the range of the output (either
  `2**32` or `2**64`).

  For full-range (i.e. inclusive of both max and min) random integers, pass
  `minval=None` and `maxval=None` with an integer `dtype`. For an integer dtype
  either both `minval` and `maxval` must be `None` or neither may be `None`. For
  example:
  ```python
  ints = tf.random.stateless_uniform(
      [10], seed=(2, 3), minval=None, maxval=None, dtype=tf.int32)
  ```

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    minval: A Tensor or Python value of type `dtype`, broadcastable with
      `shape` (for integer types, broadcasting is not supported, so it needs to
      be a scalar). The lower bound on the range of random values to
      generate. Pass `None` for full-range integers.  Defaults to 0.
    maxval: A Tensor or Python value of type `dtype`, broadcastable with
      `shape` (for integer types, broadcasting is not supported, so it needs to
      be a scalar). The upper bound on the range of random values to generate.
      Defaults to 1 if `dtype` is floating point. Pass `None` for full-range
      integers.
    dtype: The type of the output: `float16`, `bfloat16`, `float32`, `float64`,
      `int32`, or `int64`. For unbounded uniform ints (`minval`, `maxval` both
      `None`), `uint32` and `uint64` may be used. Defaults to `float32`.
    name: A name for the operation (optional).
    alg: The RNG algorithm used to generate the random numbers. Valid
      choices are `"philox"` for [the Philox
      algorithm](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf),
      `"threefry"` for [the ThreeFry
      algorithm](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf),
      and `"auto_select"` (default) for the system to automatically
      select an algorithm based the device type. Values of
      `tf.random.Algorithm` can also be used. Note that with
      `"auto_select"`, the outputs of this function may change when
      it is running on a different device.

  Returns:
    A tensor of the specified shape filled with random uniform values.

  Raises:
    ValueError: If `dtype` is integral and only one of `minval` or `maxval` is
      specified.
  '''
def stateless_random_binomial(shape, seed, counts, probs, output_dtype=..., name: Incomplete | None = None):
    """Outputs deterministic pseudorandom values from a binomial distribution.

  The generated values follow a binomial distribution with specified count and
  probability of success parameters.

  This is a stateless version of `tf.random.Generator.binomial`: if run twice
  with the same seeds and shapes, it will produce the same pseudorandom numbers.
  The output is consistent across multiple runs on the same hardware (and
  between CPU and GPU), but may change between versions of TensorFlow or on
  non-CPU/GPU hardware.

  Example:

  ```python
  counts = [10., 20.]
  # Probability of success.
  probs = [0.8]

  binomial_samples = tf.random.stateless_binomial(
      shape=[2], seed=[123, 456], counts=counts, probs=probs)

  counts = ... # Shape [3, 1, 2]
  probs = ...  # Shape [1, 4, 2]
  shape = [3, 4, 3, 4, 2]
  # Sample shape will be [3, 4, 3, 4, 2]
  binomial_samples = tf.random.stateless_binomial(
      shape=shape, seed=[123, 456], counts=counts, probs=probs)
  ```

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    counts: Tensor. The counts of the binomial distribution. Must be
      broadcastable with `probs`, and broadcastable with the rightmost
      dimensions of `shape`.
    probs: Tensor. The probability of success for the binomial distribution.
      Must be broadcastable with `counts` and broadcastable with the rightmost
      dimensions of `shape`.
    output_dtype: The type of the output. Default: tf.int32
    name: A name for the operation (optional).

  Returns:
    samples: A Tensor of the specified shape filled with random binomial
      values.  For each i, each samples[..., i] is an independent draw from
      the binomial distribution on counts[i] trials with probability of
      success probs[i].

  """
def stateless_random_gamma(shape, seed, alpha, beta: Incomplete | None = None, dtype=..., name: Incomplete | None = None):
    """Outputs deterministic pseudorandom values from a gamma distribution.

  The generated values follow a gamma distribution with specified concentration
  (`alpha`) and inverse scale (`beta`) parameters.

  This is a stateless version of `tf.random.gamma`: if run twice with the same
  seeds and shapes, it will produce the same pseudorandom numbers. The output is
  consistent across multiple runs on the same hardware (and between CPU and
  GPU),
  but may change between versions of TensorFlow or on non-CPU/GPU hardware.

  A slight difference exists in the interpretation of the `shape` parameter
  between `stateless_gamma` and `gamma`: in `gamma`, the `shape` is always
  prepended to the shape of the broadcast of `alpha` with `beta`; whereas in
  `stateless_gamma` the `shape` parameter must always encompass the shapes of
  each of `alpha` and `beta` (which must broadcast together to match the
  trailing dimensions of `shape`).

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
  samples = tf.random.stateless_gamma([10, 2], seed=[12, 34], alpha=[0.5, 1.5])
  # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
  # the samples drawn from each distribution

  samples = tf.random.stateless_gamma([7, 5, 2], seed=[12, 34], alpha=[.5, 1.5])
  # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
  # represents the 7x5 samples drawn from each of the two distributions

  alpha = tf.constant([[1.], [3.], [5.]])
  beta = tf.constant([[3., 4.]])
  samples = tf.random.stateless_gamma(
      [30, 3, 2], seed=[12, 34], alpha=alpha, beta=beta)
  # samples has shape [30, 3, 2], with 30 samples each of 3x2 distributions.

  with tf.GradientTape() as tape:
    tape.watch([alpha, beta])
    loss = tf.reduce_mean(tf.square(tf.random.stateless_gamma(
        [30, 3, 2], seed=[12, 34], alpha=alpha, beta=beta)))
  dloss_dalpha, dloss_dbeta = tape.gradient(loss, [alpha, beta])
  # unbiased stochastic derivatives of the loss function
  alpha.shape == dloss_dalpha.shape  # True
  beta.shape == dloss_dbeta.shape  # True
  ```

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    alpha: Tensor. The concentration parameter of the gamma distribution. Must
      be broadcastable with `beta`, and broadcastable with the rightmost
      dimensions of `shape`.
    beta: Tensor. The inverse scale parameter of the gamma distribution. Must be
      broadcastable with `alpha` and broadcastable with the rightmost dimensions
      of `shape`.
    dtype: Floating point dtype of `alpha`, `beta`, and the output.
    name: A name for the operation (optional).

  Returns:
    samples: A Tensor of the specified shape filled with random gamma values.
      For each i, each `samples[..., i] is an independent draw from the gamma
      distribution with concentration alpha[i] and scale beta[i].

  """
def stateless_random_poisson(shape, seed, lam, dtype=..., name: Incomplete | None = None):
    '''Outputs deterministic pseudorandom values from a Poisson distribution.

  The generated values follow a Poisson distribution with specified rate
  parameter.

  This is a stateless version of `tf.random.poisson`: if run twice with the same
  seeds and shapes, it will produce the same pseudorandom numbers. The output is
  consistent across multiple runs on the same hardware, but may change between
  versions of TensorFlow or on non-CPU/GPU hardware.

  A slight difference exists in the interpretation of the `shape` parameter
  between `stateless_poisson` and `poisson`: in `poisson`, the `shape` is always
  prepended to the shape of `lam`; whereas in `stateless_poisson` the shape of
  `lam` must match the trailing dimensions of `shape`.

  Example:

  ```python
  samples = tf.random.stateless_poisson([10, 2], seed=[12, 34], lam=[5, 15])
  # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
  # the samples drawn from each distribution

  samples = tf.random.stateless_poisson([7, 5, 2], seed=[12, 34], lam=[5, 15])
  # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
  # represents the 7x5 samples drawn from each of the two distributions

  rate = tf.constant([[1.], [3.], [5.]])
  samples = tf.random.stateless_poisson([30, 3, 1], seed=[12, 34], lam=rate)
  # samples has shape [30, 3, 1], with 30 samples each of 3x1 distributions.
  ```

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    lam: Tensor. The rate parameter "lambda" of the Poisson distribution. Shape
      must match the rightmost dimensions of `shape`.
    dtype: Dtype of the samples (int or float dtypes are permissible, as samples
      are discrete). Default: int32.
    name: A name for the operation (optional).

  Returns:
    samples: A Tensor of the specified shape filled with random Poisson values.
      For each i, each `samples[..., i]` is an independent draw from the Poisson
      distribution with rate `lam[i]`.

  '''
def stateless_random_normal(shape, seed, mean: float = 0.0, stddev: float = 1.0, dtype=..., name: Incomplete | None = None, alg: str = 'auto_select'):
    """Outputs deterministic pseudorandom values from a normal distribution.

  This is a stateless version of `tf.random.normal`: if run twice with the
  same seeds and shapes, it will produce the same pseudorandom numbers.  The
  output is consistent across multiple runs on the same hardware (and between
  CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
  hardware.

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    mean: A 0-D Tensor or Python value of type `dtype`. The mean of the normal
      distribution.
    stddev: A 0-D Tensor or Python value of type `dtype`. The standard deviation
      of the normal distribution.
    dtype: The float type of the output: `float16`, `bfloat16`, `float32`,
      `float64`. Defaults to `float32`.
    name: A name for the operation (optional).
    alg: The RNG algorithm used to generate the random numbers. See
      `tf.random.stateless_uniform` for a detailed explanation.

  Returns:
    A tensor of the specified shape filled with random normal values.
  """
def stateless_truncated_normal(shape, seed, mean: float = 0.0, stddev: float = 1.0, dtype=..., name: Incomplete | None = None, alg: str = 'auto_select'):
    """Outputs deterministic pseudorandom values, truncated normally distributed.

  This is a stateless version of `tf.random.truncated_normal`: if run twice with
  the same seeds and shapes, it will produce the same pseudorandom numbers.  The
  output is consistent across multiple runs on the same hardware (and between
  CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
  hardware.

  The generated values follow a normal distribution with specified mean and
  standard deviation, except that values whose magnitude is more than 2 standard
  deviations from the mean are dropped and re-picked.

  Args:
    shape: A 1-D integer Tensor or Python array. The shape of the output tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    mean: A 0-D Tensor or Python value of type `dtype`. The mean of the
      truncated normal distribution.
    stddev: A 0-D Tensor or Python value of type `dtype`. The standard deviation
      of the normal distribution, before truncation.
    dtype: The type of the output.
    name: A name for the operation (optional).
    alg: The RNG algorithm used to generate the random numbers. See
      `tf.random.stateless_uniform` for a detailed explanation.

  Returns:
    A tensor of the specified shape filled with random truncated normal values.
  """
def stateless_multinomial(logits, num_samples, seed, output_dtype=..., name: Incomplete | None = None):
    """Draws deterministic pseudorandom samples from a multinomial distribution.

  This is a stateless version of `tf.random.categorical`: if run twice with the
  same seeds and shapes, it will produce the same pseudorandom numbers.  The
  output is consistent across multiple runs on the same hardware (and between
  CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
  hardware.

  Example:

  ```python
  # samples has shape [1, 5], where each value is either 0 or 1 with equal
  # probability.
  samples = tf.random.stateless_categorical(
      tf.math.log([[0.5, 0.5]]), 5, seed=[7, 17])
  ```

  Args:
    logits: 2-D Tensor with shape `[batch_size, num_classes]`.  Each slice
      `[i, :]` represents the unnormalized log-probabilities for all classes.
    num_samples: 0-D.  Number of independent samples to draw for each row slice.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    output_dtype: The integer type of the output: `int32` or `int64`. Defaults
      to `int64`.
    name: Optional name for the operation.

  Returns:
    The drawn samples of shape `[batch_size, num_samples]`.
  """
def stateless_categorical(logits, num_samples, seed, dtype=..., name: Incomplete | None = None):
    """Draws deterministic pseudorandom samples from a categorical distribution.

  This is a stateless version of `tf.categorical`: if run twice with the
  same seeds and shapes, it will produce the same pseudorandom numbers.  The
  output is consistent across multiple runs on the same hardware (and between
  CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
  hardware.


  Example:

  ```python
  # samples has shape [1, 5], where each value is either 0 or 1 with equal
  # probability.
  samples = tf.random.stateless_categorical(
      tf.math.log([[0.5, 0.5]]), 5, seed=[7, 17])
  ```

  Args:
    logits: 2-D Tensor with shape `[batch_size, num_classes]`.  Each slice
      `[i, :]` represents the unnormalized log-probabilities for all classes.
    num_samples: 0-D.  Number of independent samples to draw for each row slice.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    dtype: The integer type of the output: `int32` or `int64`. Defaults to
      `int64`.
    name: Optional name for the operation.

  Returns:
    The drawn samples of shape `[batch_size, num_samples]`.
  """
def stateless_multinomial_categorical_impl(logits, num_samples, dtype, seed):
    """Implementation for stateless multinomial/categorical ops (v1/v2)."""
def stateless_parameterized_truncated_normal(shape, seed, means: float = 0.0, stddevs: float = 1.0, minvals: float = -2.0, maxvals: float = 2.0, name: Incomplete | None = None):
    """Outputs random values from a truncated normal distribution.

  The generated values follow a normal distribution with specified mean and
  standard deviation, except that values whose magnitude is more than 2 standard
  deviations from the mean are dropped and re-picked.


  Examples:

  Sample from a Truncated normal, with deferring shape parameters that
  broadcast.

  >>> means = 0.
  >>> stddevs = tf.math.exp(tf.random.uniform(shape=[2, 3]))
  >>> minvals = [-1., -2., -1000.]
  >>> maxvals = [[10000.], [1.]]
  >>> y = tf.random.stateless_parameterized_truncated_normal(
  ...   shape=[10, 2, 3], seed=[7, 17],
  ...   means=means, stddevs=stddevs, minvals=minvals, maxvals=maxvals)
  >>> y.shape
  TensorShape([10, 2, 3])

  Args:
    shape: A 1-D integer `Tensor` or Python array. The shape of the output
      tensor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    means: A `Tensor` or Python value of type `dtype`. The mean of the truncated
      normal distribution. This must broadcast with `stddevs`, `minvals` and
      `maxvals`, and the broadcasted shape must be dominated by `shape`.
    stddevs: A `Tensor` or Python value of type `dtype`. The standard deviation
      of the truncated normal distribution. This must broadcast with `means`,
      `minvals` and `maxvals`, and the broadcasted shape must be dominated by
      `shape`.
    minvals: A `Tensor` or Python value of type `dtype`. The minimum value of
      the truncated normal distribution. This must broadcast with `means`,
      `stddevs` and `maxvals`, and the broadcasted shape must be dominated by
      `shape`.
    maxvals: A `Tensor` or Python value of type `dtype`. The maximum value of
      the truncated normal distribution. This must broadcast with `means`,
      `stddevs` and `minvals`, and the broadcasted shape must be dominated by
      `shape`.
    name: A name for the operation (optional).

  Returns:
    A tensor of the specified shape filled with random truncated normal values.
  """
