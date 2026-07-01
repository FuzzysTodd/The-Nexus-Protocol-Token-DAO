from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def stateless_random_gamma_v3(shape, key, counter, alg, alpha, name: Incomplete | None = None):
    """Outputs deterministic pseudorandom random numbers from a gamma distribution.

  Outputs random values from a gamma distribution.

  The outputs are a deterministic function of the inputs.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    key: A `Tensor` of type `uint64`.
      Key for the counter-based RNG algorithm (shape uint64[1]).
    counter: A `Tensor` of type `uint64`.
      Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
    alg: A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
    alpha: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
      The concentration of the gamma distribution. Shape must match the rightmost
      dimensions of `shape`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `alpha`.
  """

StatelessRandomGammaV3: Incomplete

def stateless_random_gamma_v3_eager_fallback(shape, key, counter, alg, alpha, name, ctx): ...
def stateless_random_get_alg(name: Incomplete | None = None):
    """Picks the best counter-based RNG algorithm based on device.

  This op picks the best counter-based RNG algorithm based on device.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

StatelessRandomGetAlg: Incomplete

def stateless_random_get_alg_eager_fallback(name, ctx): ...

class _StatelessRandomGetKeyCounterOutput(NamedTuple):
    key: Incomplete
    counter: Incomplete

def stateless_random_get_key_counter(seed, name: Incomplete | None = None):
    """Scrambles seed into key and counter, using the best algorithm based on device.

  This op scrambles a shape-[2] seed into a key and a counter, both needed by counter-based RNG algorithms. The scrambing uses the best algorithm based on device. The scrambling is opaque but approximately satisfies the property that different seed results in different key/counter pair (which will in turn result in different random numbers).

  Args:
    seed: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      2 seeds (shape [2]).
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (key, counter).

    key: A `Tensor` of type `uint64`.
    counter: A `Tensor` of type `uint64`.
  """

StatelessRandomGetKeyCounter: Incomplete

def stateless_random_get_key_counter_eager_fallback(seed, name, ctx): ...

class _StatelessRandomGetKeyCounterAlgOutput(NamedTuple):
    key: Incomplete
    counter: Incomplete
    alg: Incomplete

def stateless_random_get_key_counter_alg(seed, name: Incomplete | None = None):
    """Picks the best algorithm based on device, and scrambles seed into key and counter.

  This op picks the best counter-based RNG algorithm based on device, and scrambles a shape-[2] seed into a key and a counter, both needed by the counter-based algorithm. The scrambling is opaque but approximately satisfies the property that different seed results in different key/counter pair (which will in turn result in different random numbers).

  Args:
    seed: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      2 seeds (shape [2]).
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (key, counter, alg).

    key: A `Tensor` of type `uint64`.
    counter: A `Tensor` of type `uint64`.
    alg: A `Tensor` of type `int32`.
  """

StatelessRandomGetKeyCounterAlg: Incomplete

def stateless_random_get_key_counter_alg_eager_fallback(seed, name, ctx): ...
def stateless_random_normal_v2(shape, key, counter, alg, dtype=..., name: Incomplete | None = None):
    """Outputs deterministic pseudorandom values from a normal distribution.

  The generated values will have mean 0 and standard deviation 1.

  The outputs are a deterministic function of `shape`, `key`, `counter` and `alg`.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    key: A `Tensor` of type `uint64`.
      Key for the counter-based RNG algorithm (shape uint64[1]).
    counter: A `Tensor` of type `uint64`.
      Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
    alg: A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
    dtype: An optional `tf.DType` from: `tf.half, tf.bfloat16, tf.float32, tf.float64`. Defaults to `tf.float32`.
      The type of the output.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

StatelessRandomNormalV2: Incomplete

def stateless_random_normal_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
def stateless_random_uniform_full_int_v2(shape, key, counter, alg, dtype=..., name: Incomplete | None = None):
    """Outputs deterministic pseudorandom random integers from a uniform distribution.

  The generated values are uniform integers covering the whole range of `dtype`.

  The outputs are a deterministic function of `shape`, `key`, `counter` and `alg`.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    key: A `Tensor` of type `uint64`.
      Key for the counter-based RNG algorithm (shape uint64[1]).
    counter: A `Tensor` of type `uint64`.
      Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
    alg: A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
    dtype: An optional `tf.DType` from: `tf.int32, tf.int64, tf.uint32, tf.uint64`. Defaults to `tf.uint64`.
      The type of the output.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

StatelessRandomUniformFullIntV2: Incomplete

def stateless_random_uniform_full_int_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
def stateless_random_uniform_int_v2(shape, key, counter, alg, minval, maxval, name: Incomplete | None = None):
    """Outputs deterministic pseudorandom random integers from a uniform distribution.

  The generated values follow a uniform distribution in the range `[minval, maxval)`.

  The outputs are a deterministic function of `shape`, `key`, `counter`, `alg`, `minval` and `maxval`.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    key: A `Tensor` of type `uint64`.
      Key for the counter-based RNG algorithm (shape uint64[1]).
    counter: A `Tensor` of type `uint64`.
      Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
    alg: A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
    minval: A `Tensor`. Must be one of the following types: `int32`, `int64`, `uint32`, `uint64`.
      Minimum value (inclusive, scalar).
    maxval: A `Tensor`. Must have the same type as `minval`.
      Maximum value (exclusive, scalar).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `minval`.
  """

StatelessRandomUniformIntV2: Incomplete

def stateless_random_uniform_int_v2_eager_fallback(shape, key, counter, alg, minval, maxval, name, ctx): ...
def stateless_random_uniform_v2(shape, key, counter, alg, dtype=..., name: Incomplete | None = None):
    """Outputs deterministic pseudorandom random values from a uniform distribution.

  The generated values follow a uniform distribution in the range `[0, 1)`. The
  lower bound 0 is included in the range, while the upper bound 1 is excluded.

  The outputs are a deterministic function of `shape`, `key`, `counter` and `alg`.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    key: A `Tensor` of type `uint64`.
      Key for the counter-based RNG algorithm (shape uint64[1]).
    counter: A `Tensor` of type `uint64`.
      Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
    alg: A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
    dtype: An optional `tf.DType` from: `tf.half, tf.bfloat16, tf.float32, tf.float64`. Defaults to `tf.float32`.
      The type of the output.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

StatelessRandomUniformV2: Incomplete

def stateless_random_uniform_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
def stateless_shuffle(value, key, counter, alg, name: Incomplete | None = None):
    """Randomly and deterministically shuffles a tensor along its first dimension.

  The tensor is shuffled along dimension 0, such that each `value[j]` is mapped
  to one and only one `output[i]`. For example, a mapping that might occur for a
  3x2 tensor is:

  ```
  [[1, 2],       [[5, 6],
   [3, 4],  ==>   [1, 2],
   [5, 6]]        [3, 4]]
  ```

  The outputs are a deterministic function of `value`, `key`, `counter` and `alg`.

  Args:
    value: A `Tensor`. The tensor to be shuffled.
    key: A `Tensor` of type `uint64`.
      Key for the counter-based RNG algorithm (shape uint64[1]).
    counter: A `Tensor` of type `uint64`.
      Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
    alg: A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `value`.
  """

StatelessShuffle: Incomplete

def stateless_shuffle_eager_fallback(value, key, counter, alg, name, ctx): ...
def stateless_truncated_normal_v2(shape, key, counter, alg, dtype=..., name: Incomplete | None = None):
    """Outputs deterministic pseudorandom values from a truncated normal distribution.

  The generated values follow a normal distribution with mean 0 and standard
  deviation 1, except that values whose magnitude is more than 2 standard
  deviations from the mean are dropped and re-picked.

  The outputs are a deterministic function of `shape`, `key`, `counter` and `alg`.

  Args:
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The shape of the output tensor.
    key: A `Tensor` of type `uint64`.
      Key for the counter-based RNG algorithm (shape uint64[1]).
    counter: A `Tensor` of type `uint64`.
      Initial counter for the counter-based RNG algorithm (shape uint64[2] or uint64[1] depending on the algorithm). If a larger vector is given, only the needed portion on the left (i.e. [:N]) will be used.
    alg: A `Tensor` of type `int32`. The RNG algorithm (shape int32[]).
    dtype: An optional `tf.DType` from: `tf.half, tf.bfloat16, tf.float32, tf.float64`. Defaults to `tf.float32`.
      The type of the output.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

StatelessTruncatedNormalV2: Incomplete

def stateless_truncated_normal_v2_eager_fallback(shape, key, counter, alg, dtype, name, ctx): ...
