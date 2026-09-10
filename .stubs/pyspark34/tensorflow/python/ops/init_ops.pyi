from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops_impl as linalg_ops_impl, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.deprecation import deprecated as deprecated, deprecated_arg_values as deprecated_arg_values, deprecated_args as deprecated_args
from tensorflow.python.util.tf_export import tf_export as tf_export

class Initializer:
    """Initializer base class: all initializers inherit from this class."""
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None) -> None:
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. If not provided use the initializer
        dtype.
      partition_info: Optional information about the possible partitioning of a
        tensor.
    """
    def get_config(self):
        """Returns the configuration of the initializer as a JSON-serializable dict.

    Returns:
      A JSON-serializable Python dict.
    """
    @classmethod
    def from_config(cls, config):
        """Instantiates an initializer from a configuration dictionary.

    Example:

    ```python
    initializer = RandomUniform(-1, 1)
    config = initializer.get_config()
    initializer = RandomUniform.from_config(config)
    ```

    Args:
      config: A Python dictionary. It will typically be the output of
        `get_config`.

    Returns:
      An Initializer instance.
    """

class Zeros(Initializer):
    """Initializer that generates tensors initialized to 0.

  @compatibility(TF2)
  `tf.compat.v1.zeros_initializer` is compatible with eager execution
  and `tf.function`.

  To migrate to TF2, please use `tf.zeros_initializer` instead. The `dtype`
  argument in `tf.compat.v1.zeros_initializer.__init__()` does not exist in
  `tf.zeros_initializer.__init__()`. However, you can specify the `dtype` in
  `__call__()` in both cases.

  #### Structural Mapping to TF2

  Before:

  ```python
  initializer = tf.compat.v1.zeros_initializer(dtype=tf.float32)
  variable = tf.Variable(initializer(shape=[3, 3]))
  ```

  After:

  ```python
  initializer = tf.zeros_initializer()
  variable = tf.Variable(initializer(shape=[3, 3], dtype=tf.float32))
  ```

  #### How to Map Arguments

  | TF1 Arg Name         | TF2 Arg Name     | Note                       |
  | :------------------- | :--------------- | :------------------------- |
  | `dtype`              | `dtype`          | In `__call__()` method     |
  | `partition_info`     | - |  (`__call__` arg in TF1) Not supported    |


  #### Before & After Usage Example

  Before:

  >>> initializer = tf.compat.v1.zeros_initializer(dtype=tf.float32)
  >>> tf.Variable(initializer(shape=[3])).numpy()
  array([0., 0., 0.], dtype=float32)
  >>> tf.Variable(initializer(shape=[3, 3])).numpy()
  array([[0., 0., 0.],
         [0., 0., 0.],
         [0., 0., 0.]], dtype=float32)
  >>> initializer = tf.compat.v1.zeros_initializer()
  >>> tf.Variable(initializer(shape=[3], dtype=tf.float32)).numpy()
  array([0., 0., 0.], dtype=float32)
  >>> tf.Variable(initializer(shape=[3, 3], dtype=tf.float32)).numpy()
  array([[0., 0., 0.],
         [0., 0., 0.],
         [0., 0., 0.]], dtype=float32)

  After:

  >>> initializer = tf.zeros_initializer()
  >>> tf.Variable(initializer(shape=[3], dtype=tf.float32)).numpy()
  array([0., 0., 0.], dtype=float32)
  >>> tf.Variable(initializer(shape=[3, 3], dtype=tf.float32)).numpy()
  array([[0., 0., 0.],
         [0., 0., 0.],
         [0., 0., 0.]], dtype=float32)

  @end_compatibility
  """
    dtype: Incomplete
    def __init__(self, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class Ones(Initializer):
    """Initializer that generates tensors initialized to 1.

  @compatibility(TF2)
  This API is compatible with TF2 behavior and `tf.function`, and can be
  migrated immediately with `tf.keras.initializers.ones`.

  Before:
  >>> initializer = tf.compat.v1.keras.initializers.ones()
  >>> initializer((1, 1))
  <tf.Tensor: shape=(1, 1), dtype=float32, numpy=array([[1.]], dtype=float32)>

  After:
  >>> initializer = tf.keras.initializers.ones()
  >>> initializer((1, 1))
  <tf.Tensor: shape=(1, 1), dtype=float32, numpy=array([[1.]], dtype=float32)>

  @end_compatibility
  """
    dtype: Incomplete
    def __init__(self, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class Constant(Initializer):
    """Initializer that generates tensors with constant values.

  The resulting tensor is populated with values of type `dtype`, as
  specified by arguments `value` following the desired `shape` of the
  new tensor (see examples below).

  The argument `value` can be a constant value, or a list of values of type
  `dtype`. If `value` is a list, then the length of the list must be less
  than or equal to the number of elements implied by the desired shape of the
  tensor. In the case where the total number of elements in `value` is less
  than the number of elements required by the tensor shape, the last element
  in `value` will be used to fill the remaining entries. If the total number of
  elements in `value` is greater than the number of elements required by the
  tensor shape, the initializer will raise a `ValueError`.

  Args:
    value: A Python scalar, list or tuple of values, or a N-dimensional numpy
      array. All elements of the initialized variable will be set to the
      corresponding value in the `value` argument.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer.
    verify_shape: Boolean that enables verification of the shape of `value`. If
      `True`, the initializer will throw an error if the shape of `value` is not
      compatible with the shape of the initialized tensor.

  Raises:
    TypeError: If the input `value` is not one of the expected types.

  Examples:
    The following example can be rewritten using a numpy.ndarray instead
    of the `value` list, even reshaped, as shown in the two commented lines
    below the `value` list initialization.

  >>> value = [0, 1, 2, 3, 4, 5, 6, 7]
  >>> init = tf.compat.v1.constant_initializer(value)
  >>> # fitting shape
  >>> with tf.compat.v1.Session():
  ...   x = tf.compat.v1.get_variable('x', shape=[2, 4], initializer=init)
  ...   x.initializer.run()
  ...   print(x.eval())
  [[0. 1. 2. 3.]
   [4. 5. 6. 7.]]
  >>> # Larger shape
  >>> with tf.compat.v1.Session():
  ...   y = tf.compat.v1.get_variable('y', shape=[3, 4], initializer=init)
  ...   y.initializer.run()
  ...   print(y.eval())
  [[0.  1.  2.  3.]
   [4.  5.  6.  7.]
   [7.  7.  7.  7.]]
  >>> # Smaller shape
  >>> with tf.compat.v1.Session():
  ...   z = tf.compat.v1.get_variable('z', shape=[2, 3], initializer=init)
  Traceback (most recent call last):
  ...
  ValueError: Too many elements provided. Needed at most 6, but received 8
  >>> # Shape verification
  >>> init_verify = tf.compat.v1.constant_initializer(value, verify_shape=True)
  >>> with tf.compat.v1.Session():
  ...  u = tf.compat.v1.get_variable('u', shape=[3, 4],
  ...                                initializer=init_verify)
  Traceback (most recent call last):
  ...
  TypeError: Expected Tensor's shape: (3, 4), got (8,).

  @compatibility(TF2)
  Although it is a legacy API endpoint, `tf.compat.v1.constant_initializer`
  is compatible with eager execution and `tf.function`.

  To migrate to a non-legacy TF2 API, please use `tf.constant_initializer`
  instead. The `dtype`
  argument in `tf.compat.v1.constant_initializer.__init__()` does not exist in
  `tf.constant_initializer.__init__()`. However, you can specify the `dtype` in
  `__call__()` in both cases.

  In the `compat.v1` symbol, if `verify_shape` is set to `True`, an exception
  is raised when initializing a variable with a different shape from
  `value`. If set to `False`, `value` is reshaped to initialize the variable
  if necessary. An exception would only be raised when the number of
  elements are different.

  The `verify_shape` argument is not supported in TF2. Using
  `tf.constant_initializer` is equivalent to setting `verify_shape` to `False`.

  #### Structural Mapping to TF2

  Before:

  ```python
  value = [0, 1, 2, 3, 4, 5, 6, 7]
  initializer = tf.compat.v1.constant_initializer(
      value=value,
      dtype=tf.float32,
      verify_shape=False)
  variable = tf.Variable(initializer(shape=[2, 4]))
  ```

  After:

  ```python
  value = [0, 1, 2, 3, 4, 5, 6, 7]
  initializer = tf.constant_initializer(value=value)
  tf.Variable(initializer(shape=[2, 4], dtype=tf.float32))
  ```

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name     | Note                        |
  | :-------------------- | :--------------- | :-------------------------- |
  | `value`               | `value`          | In constructor              |
  | `dtype`               | `dtype`          | In `__call__()` method      |
  | `verify_shape`        | Not Supported    | Equivalent to set to `False`|
  | `partition_info`      | - |  (`__call__` arg in TF1) Not supported     |


  #### Before & After Usage Example

  Before:

  >>> value = [1., 2., 3., 4.]
  >>> initializer = tf.compat.v1.constant_initializer(
  ...     value=value, dtype=tf.float32, verify_shape=True)
  >>> tf.Variable(initializer(shape=[2, 2])).numpy()
  Traceback (most recent call last):
  ...
  TypeError: Expected Tensor's shape: (2, 2), got (4,).
  >>> initializer = tf.compat.v1.constant_initializer(
  ...     value=value, dtype=tf.float32, verify_shape=False)
  >>> tf.Variable(initializer(shape=[2, 2])).numpy()
  array([[1., 2.],
         [3., 4.]], dtype=float32)

  After:

  >>> value = [1., 2., 3., 4.]
  >>> initializer = tf.constant_initializer(value=value)
  >>> tf.Variable(initializer(shape=[2, 2], dtype=tf.float32)).numpy()
  array([[1., 2.],
         [3., 4.]], dtype=float32)

  @end_compatibility
  """
    value: Incomplete
    dtype: Incomplete
    def __init__(self, value: int = 0, dtype=..., verify_shape: bool = False) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None, verify_shape: Incomplete | None = None): ...
    def get_config(self): ...

class RandomUniform(Initializer):
    """Initializer that generates tensors with a uniform distribution.

  Args:
    minval: A python scalar or a scalar tensor. Lower bound of the range of
      random values to generate.
    maxval: A python scalar or a scalar tensor. Upper bound of the range of
      random values to generate.  Defaults to 1 for float types.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer.

  @compatibility(TF2)
  Although it is a legacy compat.v1 API, this symbol is compatible with eager
  execution and `tf.function`.

  To switch to TF2, switch to using either
  `tf.initializers.RandomUniform` or `tf.keras.initializers.RandomUniform`
  (neither from `compat.v1`) and
  pass the dtype when calling the initializer. Keep in mind that
  the default minval, maxval and the behavior of fixed seeds have changed.

  #### Structural Mapping to TF2

  Before:

  ```python
  initializer = tf.compat.v1.random_uniform_initializer(
    minval=minval,
    maxval=maxval,
    seed=seed,
    dtype=dtype)

  weight_one = tf.Variable(initializer(shape_one))
  weight_two = tf.Variable(initializer(shape_two))
  ```

  After:

  ```python
  initializer = tf.initializers.RandomUniform(
    minval=minval,
    maxval=maxval,
    seed=seed)

  weight_one = tf.Variable(initializer(shape_one, dtype=dtype))
  weight_two = tf.Variable(initializer(shape_two, dtype=dtype))
  ```

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `minval`               | `minval`    | Default changes from 0 to -0.05 |
  | `maxval`         | `maxval`        | Default changes from 1.0 to 0.05 |
  | `seed`             | `seed` |  |
  | `dtype` | `dtype`   | The TF2 native api only takes it  |
  :                     :      : as a `__call__` arg, not a constructor arg. :
  | `partition_info`     | - |  (`__call__` arg in TF1) Not supported       |

  @end_compatibility
  """
    minval: Incomplete
    maxval: Incomplete
    seed: Incomplete
    dtype: Incomplete
    def __init__(self, minval: float = 0.0, maxval: Incomplete | None = None, seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class RandomNormal(Initializer):
    """Initializer that generates tensors with a normal distribution.

  Args:
    mean: a python scalar or a scalar tensor. Mean of the random values to
      generate.
    stddev: a python scalar or a scalar tensor. Standard deviation of the random
      values to generate.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.

  @compatibility(TF2)
  Although it is a legacy `compat.v1` API, this symbol is compatible with eager
  execution and `tf.function`.

  To switch to TF2, switch to using either
  `tf.initializers.RandomNormal` or `tf.keras.initializers.RandomNormal`
  (neither from `compat.v1`) and
  pass the dtype when calling the initializer. Keep in mind that
  the default stddev and the behavior of fixed seeds have changed.

  #### Structural Mapping to TF2

  Before:

  ```python
  initializer = tf.compat.v1.random_normal_initializer(
    mean=mean,
    stddev=stddev,
    seed=seed,
    dtype=dtype)

  weight_one = tf.Variable(initializer(shape_one))
  weight_two = tf.Variable(initializer(shape_two))
  ```

  After:

  ```python
  initializer = tf.initializers.RandomNormal(
    mean=mean,
    seed=seed,
    stddev=stddev)

  weight_one = tf.Variable(initializer(shape_one, dtype=dtype))
  weight_two = tf.Variable(initializer(shape_two, dtype=dtype))
  ```

  #### How to Map Arguments

  | TF1 Arg Name       | TF2 Arg Name    | Note                       |
  | :----------------- | :-------------- | :------------------------- |
  | `mean`             | `mean`          | No change to defaults |
  | `stddev`           | `stddev`        | Default changes from 1.0 to 0.05 |
  | `seed`             | `seed`          |                                  |
  | `dtype`            | `dtype`  | The TF2 native api only takes it as a |
  :                    :          : `__call__` arg, not a constructor arg. :
  | `partition_info`   | -     |  (`__call__` arg in TF1) Not supported.  |

  @end_compatibility
  """
    mean: Incomplete
    stddev: Incomplete
    seed: Incomplete
    dtype: Incomplete
    def __init__(self, mean: float = 0.0, stddev: float = 1.0, seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class TruncatedNormal(Initializer):
    """Initializer that generates a truncated normal distribution.

  These values are similar to values from a `random_normal_initializer`
  except that values more than two standard deviations from the mean
  are discarded and re-drawn. This is the recommended initializer for
  neural network weights and filters.

  Args:
    mean: a python scalar or a scalar tensor. Mean of the random values to
      generate.
    stddev: a python scalar or a scalar tensor. Standard deviation of the random
      values to generate.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.

  @compatibility(TF2)
  Although it is a legacy `compat.v1` API, this symbol is compatible with eager
  execution and `tf.function`.

  To switch to TF2, switch to using either
  `tf.initializers.truncated_normal` or `tf.keras.initializers.TruncatedNormal`
  (neither from `compat.v1`) and
  pass the dtype when calling the initializer. Keep in mind that
  the default stddev and the behavior of fixed seeds have changed.

  #### Structural Mapping to TF2

  Before:

  ```python
  initializer = tf.compat.v1.truncated_normal_initializer(
    mean=mean,
    stddev=stddev,
    seed=seed,
    dtype=dtype)

  weight_one = tf.Variable(initializer(shape_one))
  weight_two = tf.Variable(initializer(shape_two))
  ```

  After:

  ```python
  initializer = tf.initializers.truncated_normal(
    mean=mean,
    seed=seed,
    stddev=stddev)

  weight_one = tf.Variable(initializer(shape_one, dtype=dtype))
  weight_two = tf.Variable(initializer(shape_two, dtype=dtype))
  ```

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `mean`               | `mean`        | No change to defaults |
  | `stddev`         | `stddev`        | Default changes from 1.0 to 0.05 |
  | `seed`             | `seed` | |
  | `dtype` | `dtype`   | The TF2 native api only takes it  |
  :                     :      : as a `__call__` arg, not a constructor arg. :
  | `partition_info`     | - |  (`__call__` arg in TF1) Not supported       |

  @end_compatibility
  """
    mean: Incomplete
    stddev: Incomplete
    seed: Incomplete
    dtype: Incomplete
    def __init__(self, mean: float = 0.0, stddev: float = 1.0, seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class UniformUnitScaling(Initializer):
    """Initializer that generates tensors without scaling variance.

  When initializing a deep network, it is in principle advantageous to keep
  the scale of the input variance constant, so it does not explode or diminish
  by reaching the final layer. If the input is `x` and the operation `x * W`,
  and we want to initialize `W` uniformly at random, we need to pick `W` from

      [-sqrt(3) / sqrt(dim), sqrt(3) / sqrt(dim)]

  to keep the scale intact, where `dim = W.shape[0]` (the size of the input).
  A similar calculation for convolutional networks gives an analogous result
  with `dim` equal to the product of the first 3 dimensions.  When
  nonlinearities are present, we need to multiply this by a constant `factor`.
  See (Sussillo et al., 2014) for deeper motivation, experiments
  and the calculation of constants. In section 2.3 there, the constants were
  numerically computed: for a linear layer it's 1.0, relu: ~1.43, tanh: ~1.15.

  Args:
    factor: Float.  A multiplicative factor by which the values will be scaled.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Sussillo et al., 2014](https://arxiv.org/abs/1412.6558)
      ([pdf](http://arxiv.org/pdf/1412.6558.pdf))
  """
    factor: Incomplete
    seed: Incomplete
    dtype: Incomplete
    def __init__(self, factor: float = 1.0, seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class VarianceScaling(Initializer):
    '''Initializer capable of adapting its scale to the shape of weights tensors.

  @compatibility(TF2)
  Although it is a legacy `compat.v1` API, this symbol is compatible with eager
  execution and `tf.function`.

  To switch to TF2 APIs, move to using either
  `tf.initializers.variance_scaling` or `tf.keras.initializers.VarianceScaling`
  (neither from `compat.v1`) and
  pass the dtype when calling the initializer.

  #### Structural Mapping to TF2

  Before:

  ```python
  initializer = tf.compat.v1.variance_scaling_initializer(
    scale=scale,
    mode=mode,
    distribution=distribution
    seed=seed,
    dtype=dtype)

  weight_one = tf.Variable(initializer(shape_one))
  weight_two = tf.Variable(initializer(shape_two))
  ```

  After:

  ```python
  initializer = tf.keras.initializers.VarianceScaling(
    scale=scale,
    mode=mode,
    distribution=distribution
    seed=seed)

  weight_one = tf.Variable(initializer(shape_one, dtype=dtype))
  weight_two = tf.Variable(initializer(shape_two, dtype=dtype))
  ```

  #### How to Map Arguments

  | TF1 Arg Name       | TF2 Arg Name    | Note                       |
  | :----------------- | :-------------- | :------------------------- |
  | `scale`            | `scale`        | No change to defaults       |
  | `mode`             | `mode`         | No change to defaults       |
  | `distribution`     | `distribution` | No change to defaults.      |
  :                    :                : \'normal\' maps to \'truncated_normal\' :
  | `seed`             | `seed`         | |
  | `dtype`        |  `dtype` | The TF2 api only takes it  |
  :                :          : as a `__call__` arg, not a constructor arg. :
  | `partition_info`     | - |  (`__call__` arg in TF1) Not supported       |

  @end_compatibility

  With `distribution="truncated_normal" or "untruncated_normal"`,
  samples are drawn from a truncated/untruncated normal
  distribution with a mean of zero and a standard deviation (after truncation,
  if used) `stddev = sqrt(scale / n)`
  where n is:
    - number of input units in the weight tensor, if mode = "fan_in"
    - number of output units, if mode = "fan_out"
    - average of the numbers of input and output units, if mode = "fan_avg"

  With `distribution="uniform"`, samples are drawn from a uniform distribution
  within [-limit, limit], with `limit = sqrt(3 * scale / n)`.

  Args:
    scale: Scaling factor (positive float).
    mode: One of "fan_in", "fan_out", "fan_avg".
    distribution: Random distribution to use. One of "normal", "uniform".
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.

  Raises:
    ValueError: In case of an invalid value for the "scale", mode" or
      "distribution" arguments.
  '''
    scale: Incomplete
    mode: Incomplete
    distribution: Incomplete
    seed: Incomplete
    dtype: Incomplete
    def __init__(self, scale: float = 1.0, mode: str = 'fan_in', distribution: str = 'truncated_normal', seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class Orthogonal(Initializer):
    """Initializer that generates an orthogonal matrix.

  If the shape of the tensor to initialize is two-dimensional, it is initialized
  with an orthogonal matrix obtained from the QR decomposition of a matrix of
  random numbers drawn from a normal distribution.
  If the matrix has fewer rows than columns then the output will have orthogonal
  rows. Otherwise, the output will have orthogonal columns.

  If the shape of the tensor to initialize is more than two-dimensional,
  a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])`
  is initialized, where `n` is the length of the shape vector.
  The matrix is subsequently reshaped to give a tensor of the desired shape.

  Args:
    gain: multiplicative factor to apply to the orthogonal matrix
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Saxe et al., 2014](https://openreview.net/forum?id=_wzZwKpTDF_9C)
      ([pdf](https://arxiv.org/pdf/1312.6120.pdf))
  """
    gain: Incomplete
    dtype: Incomplete
    seed: Incomplete
    def __init__(self, gain: float = 1.0, seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class ConvolutionDeltaOrthogonal(Initializer):
    """Initializer that generates a delta orthogonal kernel for ConvNets.

  The shape of the tensor must have length 3, 4 or 5. The number of input
  filters must not exceed the number of output filters. The center pixels of the
  tensor form an orthogonal matrix. Other pixels are set to be zero. See
  algorithm 2 in (Xiao et al., 2018).


  Args:
    gain: Multiplicative factor to apply to the orthogonal matrix. Default is 1.
      The 2-norm of an input is multiplied by a factor of `gain` after applying
      this convolution.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Xiao et al., 2018](http://proceedings.mlr.press/v80/xiao18a.html)
      ([pdf](http://proceedings.mlr.press/v80/xiao18a/xiao18a.pdf))
  """
    gain: Incomplete
    dtype: Incomplete
    seed: Incomplete
    def __init__(self, gain: float = 1.0, seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class ConvolutionOrthogonal(Initializer):
    """Initializer that generates orthogonal kernel for ConvNets.

  Base class used to construct 1D, 2D and 3D orthogonal kernels for convolution.

  Args:
    gain: multiplicative factor to apply to the orthogonal matrix. Default is 1.
      The 2-norm of an input is multiplied by a factor of `gain` after applying
      this convolution.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Xiao et al., 2018](http://proceedings.mlr.press/v80/xiao18a.html)
      ([pdf](http://proceedings.mlr.press/v80/xiao18a/xiao18a.pdf))
  """
    gain: Incomplete
    dtype: Incomplete
    seed: Incomplete
    def __init__(self, gain: float = 1.0, seed: Incomplete | None = None, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None) -> None: ...
    def get_config(self): ...

class ConvolutionOrthogonal2D(ConvolutionOrthogonal):
    """Initializer that generates a 2D orthogonal kernel for ConvNets.

  The shape of the tensor must have length 4. The number of input
  filters must not exceed the number of output filters.
  The orthogonality(==isometry) is exact when the inputs are circular padded.
  There are finite-width effects with non-circular padding (e.g. zero padding).
  See algorithm 1 in (Xiao et al., 2018).

  Args:
    gain: Multiplicative factor to apply to the orthogonal matrix. Default is 1.
      This has the effect of scaling the output 2-norm by a factor of `gain`.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Xiao et al., 2018](http://proceedings.mlr.press/v80/xiao18a.html)
      ([pdf](http://proceedings.mlr.press/v80/xiao18a/xiao18a.pdf))
  """
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...

class ConvolutionOrthogonal1D(ConvolutionOrthogonal):
    """Initializer that generates a 1D orthogonal kernel for ConvNets.

  The shape of the tensor must have length 3. The number of input
  filters must not exceed the number of output filters.
  The orthogonality(==isometry) is exact when the inputs are circular padded.
  There are finite-width effects with non-circular padding (e.g. zero padding).
  See algorithm 1 in (Xiao et al., 2018).

  Args:
    gain: Multiplicative factor to apply to the orthogonal matrix. Default is 1.
      The 2-norm of an input is multiplied by a factor of `gain` after applying
      this convolution.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Xiao et al., 2018](http://proceedings.mlr.press/v80/xiao18a.html)
      ([pdf](http://proceedings.mlr.press/v80/xiao18a/xiao18a.pdf))
  """
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...

class ConvolutionOrthogonal3D(ConvolutionOrthogonal):
    """Initializer that generates a 3D orthogonal kernel for ConvNets.

  The shape of the tensor must have length 5. The number of input
  filters must not exceed the number of output filters.
  The orthogonality(==isometry) is exact when the inputs are circular padded.
  There are finite-width effects with non-circular padding (e.g. zero padding).
  See algorithm 1 (Xiao et al., 2018).

  Args:
    gain: Multiplicative factor to apply to the orthogonal matrix. Default is 1.
      The 2-norm of an input is multiplied by a factor of `gain` after applying
      this convolution.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Xiao et al., 2018](http://proceedings.mlr.press/v80/xiao18a.html)
      ([pdf](http://proceedings.mlr.press/v80/xiao18a/xiao18a.pdf))
  """
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...

class Identity(Initializer):
    """Initializer that generates the identity matrix.

  Only use for 2D matrices.

  Args:
    gain: Multiplicative factor to apply to the identity matrix.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  """
    gain: Incomplete
    dtype: Incomplete
    def __init__(self, gain: float = 1.0, dtype=...) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, partition_info: Incomplete | None = None): ...
    def get_config(self): ...

class GlorotUniform(VarianceScaling):
    """The Glorot uniform initializer, also called Xavier uniform initializer.

  It draws samples from a uniform distribution within [-limit, limit]
  where `limit` is `sqrt(6 / (fan_in + fan_out))`
  where `fan_in` is the number of input units in the weight tensor
  and `fan_out` is the number of output units in the weight tensor.

  Args:
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
      ([pdf](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf))
  """
    def __init__(self, seed: Incomplete | None = None, dtype=...) -> None: ...
    def get_config(self): ...

class GlorotNormal(VarianceScaling):
    """The Glorot normal initializer, also called Xavier normal initializer.

  It draws samples from a truncated normal distribution centered on 0
  with standard deviation (after truncation) given by
  `stddev = sqrt(2 / (fan_in + fan_out))` where `fan_in` is the number
  of input units in the weight tensor and `fan_out` is the number of
  output units in the weight tensor.

  Args:
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed` for behavior.
    dtype: Default data type, used if no `dtype` argument is provided when
      calling the initializer. Only floating point types are supported.
  References:
      [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
      ([pdf](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf))
  """
    def __init__(self, seed: Incomplete | None = None, dtype=...) -> None: ...
    def get_config(self): ...
zeros_initializer = Zeros
ones_initializer = Ones
constant_initializer = Constant
random_uniform_initializer = RandomUniform
random_normal_initializer = RandomNormal
truncated_normal_initializer = TruncatedNormal
uniform_unit_scaling_initializer = UniformUnitScaling
variance_scaling_initializer = VarianceScaling
glorot_uniform_initializer = GlorotUniform
glorot_normal_initializer = GlorotNormal
orthogonal_initializer = Orthogonal
identity_initializer = Identity
convolutional_delta_orthogonal = ConvolutionDeltaOrthogonal
convolutional_orthogonal_1d = ConvolutionOrthogonal1D
convolutional_orthogonal_2d = ConvolutionOrthogonal2D
convolutional_orthogonal_3d = ConvolutionOrthogonal3D

def lecun_normal(seed: Incomplete | None = None):
    """LeCun normal initializer.

  It draws samples from a truncated normal distribution centered on 0
  with standard deviation (after truncation) given by
  `stddev = sqrt(1 / fan_in)` where `fan_in` is the number of
  input units in the weight tensor.

  Args:
      seed: A Python integer. Used to seed the random generator.

  Returns:
      An initializer.

  References:
      - Self-Normalizing Neural Networks,
      [Klambauer et al.,
      2017](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)
      # pylint: disable=line-too-long
      ([pdf](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
      - Efficient Backprop,
      [Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
  """
def lecun_uniform(seed: Incomplete | None = None):
    """LeCun uniform initializer.

  It draws samples from a uniform distribution within [-limit, limit]
  where `limit` is `sqrt(3 / fan_in)`
  where `fan_in` is the number of input units in the weight tensor.

  Args:
      seed: A Python integer. Used to seed the random generator.

  Returns:
      An initializer.

  References:
      - Self-Normalizing Neural Networks,
      [Klambauer et al.,
      2017](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)
      # pylint: disable=line-too-long
      ([pdf](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
      - Efficient Backprop,
      [Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
  """
def he_normal(seed: Incomplete | None = None):
    """He normal initializer.

  It draws samples from a truncated normal distribution centered on 0
  with standard deviation (after truncation) given by
  `stddev = sqrt(2 / fan_in)` where `fan_in` is the number of
  input units in the weight tensor.

  Args:
      seed: A Python integer. Used to seed the random generator.

  Returns:
      An initializer.

  References:
      [He et al., 2015]
      (https://www.cv-foundation.org/openaccess/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper.html)
      # pylint: disable=line-too-long
      ([pdf](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf))
  """
def he_uniform(seed: Incomplete | None = None):
    """He uniform variance scaling initializer.

  It draws samples from a uniform distribution within [-limit, limit]
  where `limit` is `sqrt(6 / fan_in)`
  where `fan_in` is the number of input units in the weight tensor.

  Args:
      seed: A Python integer. Used to seed the random generator.

  Returns:
      An initializer.

  References:
      [He et al., 2015]
      (https://www.cv-foundation.org/openaccess/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper.html)
      # pylint: disable=line-too-long
      ([pdf](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf))
  """
