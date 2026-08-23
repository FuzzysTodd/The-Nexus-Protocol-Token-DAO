from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes
from tensorflow.python.ops import array_ops as array_ops, gen_linalg_ops as gen_linalg_ops, linalg_ops_impl as linalg_ops_impl, math_ops as math_ops, random_ops as random_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class Initializer:
    """Initializer base class: all initializers inherit from this class.

  Initializers should implement a `__call__` method with the following
  signature:

  ```python
  def __call__(self, shape, dtype=None, **kwargs):
    # returns a tensor of shape `shape` and dtype `dtype`
    # containing values drawn from a distribution of your choice.
  ```
  """
    def __call__(self, shape, dtype: Incomplete | None = None, **kwargs) -> None:
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. If not provided will return tensor
        of `tf.float32`.
      **kwargs: Additional keyword arguments. Accepted values:
        `partition_shape` and `partition_offset`. Used when creating a single
        partition in a partitioned variable. `partition_shape` is the shape of
        the partition (i.e. the shape of the returned tensor) and
        `partition_offset` is a tuple of `int` specifying the offset of this
        partition w.r.t each axis. For example, a tensor of shape `(30, 100)`
        can be partitioned into two partitions: `p0` of shape `(10, 100)` and
        `p1` of shape `(20, 100)`; if the initializer is called with
        `partition_shape=(20, 100)` and `partition_offset=(10, 0)`, it should
        return the value for `p1`.
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
      config: A Python dictionary.
        It will typically be the output of `get_config`.

    Returns:
      An Initializer instance.
    """

class Zeros(Initializer):
    """Initializer that generates tensors initialized to 0.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.zeros_initializer())
  >>> v1
  <tf.Variable ... shape=(3,) ... numpy=array([0., 0., 0.], dtype=float32)>
  >>> v2
  <tf.Variable ... shape=(3, 3) ... numpy=
  array([[0., 0., 0.],
         [0., 0., 0.],
         [0., 0., 0.]], dtype=float32)>
  >>> make_variables(4, tf.random_uniform_initializer(minval=-1., maxval=1.))
  (<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...
  """
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only numeric or boolean dtypes are
       supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValuesError: If the dtype is not numeric or boolean.
    """

class Ones(Initializer):
    """Initializer that generates tensors initialized to 1.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.ones_initializer())
  >>> v1
  <tf.Variable ... shape=(3,) ... numpy=array([1., 1., 1.], dtype=float32)>
  >>> v2
  <tf.Variable ... shape=(3, 3) ... numpy=
  array([[1., 1., 1.],
         [1., 1., 1.],
         [1., 1., 1.]], dtype=float32)>
  >>> make_variables(4, tf.random_uniform_initializer(minval=-1., maxval=1.))
  (<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...
  """
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only numeric or boolean dtypes are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValuesError: If the dtype is not numeric or boolean.
    """

class Constant(Initializer):
    """Initializer that generates tensors with constant values.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  `tf.constant_initializer` returns an object which when called returns a tensor
  populated with the `value` specified in the constructor. This `value` must be
  convertible to the requested `dtype`.

  The argument `value` can be a scalar constant value, or a list of
  values. Scalars broadcast to whichever shape is requested from the
  initializer.

  If `value` is a list, then the length of the list must be equal to the number
  of elements implied by the desired shape of the tensor. If the total number of
  elements in `value` is not equal to the number of elements required by the
  tensor shape, the initializer will raise a `TypeError`.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.constant_initializer(2.))
  >>> v1
  <tf.Variable ... shape=(3,) ... numpy=array([2., 2., 2.], dtype=float32)>
  >>> v2
  <tf.Variable ... shape=(3, 3) ... numpy=
  array([[2., 2., 2.],
         [2., 2., 2.],
         [2., 2., 2.]], dtype=float32)>
  >>> make_variables(4, tf.random_uniform_initializer(minval=-1., maxval=1.))
  (<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...

  >>> value = [0, 1, 2, 3, 4, 5, 6, 7]
  >>> init = tf.constant_initializer(value)
  >>> # Fitting shape
  >>> tf.Variable(init(shape=[2, 4], dtype=tf.float32))
  <tf.Variable ...
  array([[0., 1., 2., 3.],
         [4., 5., 6., 7.]], dtype=float32)>
  >>> # Larger shape
  >>> tf.Variable(init(shape=[3, 4], dtype=tf.float32))
  Traceback (most recent call last):
  ...
  TypeError: ...value has 8 elements, shape is (3, 4) with 12 elements...
  >>> # Smaller shape
  >>> tf.Variable(init(shape=[2, 3], dtype=tf.float32))
  Traceback (most recent call last):
  ...
  TypeError: ...value has 8 elements, shape is (2, 3) with 6 elements...

  Args:
    value: A Python scalar, list or tuple of values, or a N-dimensional numpy
      array. All elements of the initialized variable will be set to the
      corresponding value in the `value` argument.

  Raises:
    TypeError: If the input `value` is not one of the expected types.
  """
    value: Incomplete
    def __init__(self, value: int = 0) -> None: ...
    def __call__(self, shape, dtype: Incomplete | None = None, **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. If not provided the dtype of the
        tensor created will be the type of the inital value.
      **kwargs: Additional keyword arguments.

    Raises:
      TypeError: If the initializer cannot create a tensor of the requested
       dtype.
    """
    def get_config(self): ...

class RandomUniform(Initializer):
    """Initializer that generates tensors with a uniform distribution.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.ones_initializer())
  >>> v1
  <tf.Variable ... shape=(3,) ... numpy=array([1., 1., 1.], dtype=float32)>
  >>> v2
  <tf.Variable ... shape=(3, 3) ... numpy=
  array([[1., 1., 1.],
         [1., 1., 1.],
         [1., 1., 1.]], dtype=float32)>
  >>> make_variables(4, tf.random_uniform_initializer(minval=-1., maxval=1.))
  (<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...

  Args:
    minval: A python scalar or a scalar tensor. Lower bound of the range of
      random values to generate (inclusive).
    maxval: A python scalar or a scalar tensor. Upper bound of the range of
      random values to generate (exclusive).
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.
  """
    minval: Incomplete
    maxval: Incomplete
    seed: Incomplete
    def __init__(self, minval: float = -0.05, maxval: float = 0.05, seed: Incomplete | None = None) -> None: ...
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point and integer
        types are supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not numeric.
    """
    def get_config(self): ...

class RandomNormal(Initializer):
    """Initializer that generates tensors with a normal distribution.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3,
  ...                         tf.random_normal_initializer(mean=1., stddev=2.))
  >>> v1
  <tf.Variable ... shape=(3,) ... numpy=array([...], dtype=float32)>
  >>> v2
  <tf.Variable ... shape=(3, 3) ... numpy=
  ...
  >>> make_variables(4, tf.random_uniform_initializer(minval=-1., maxval=1.))
  (<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...

  Args:
    mean: a python scalar or a scalar tensor. Mean of the random values to
      generate.
    stddev: a python scalar or a scalar tensor. Standard deviation of the random
      values to generate.
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.

  """
    mean: Incomplete
    stddev: Incomplete
    seed: Incomplete
    def __init__(self, mean: float = 0.0, stddev: float = 0.05, seed: Incomplete | None = None) -> None: ...
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point
    """
    def get_config(self): ...

class TruncatedNormal(Initializer):
    """Initializer that generates a truncated normal distribution.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  These values are similar to values from a `tf.initializers.RandomNormal`
  except that values more than two standard deviations from the mean are
  discarded and re-drawn. This is the recommended initializer for neural network
  weights and filters.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(
  ...     3, tf.initializers.TruncatedNormal(mean=1., stddev=2.))
  >>> v1
  <tf.Variable ... shape=(3,) ... numpy=array([...], dtype=float32)>
  >>> v2
  <tf.Variable ... shape=(3, 3) ... numpy=
  ...
  >>> make_variables(4, tf.initializers.RandomUniform(minval=-1., maxval=1.))
  (<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...

  Args:
    mean: a python scalar or a scalar tensor. Mean of the random values
      to generate.
    stddev: a python scalar or a scalar tensor. Standard deviation of the
      random values to generate.
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.
  """
    mean: Incomplete
    stddev: Incomplete
    seed: Incomplete
    def __init__(self, mean: float = 0.0, stddev: float = 0.05, seed: Incomplete | None = None) -> None: ...
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point
    """
    def get_config(self): ...

class VarianceScaling(Initializer):
    '''Initializer capable of adapting its scale to the shape of weights tensors.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  With `distribution="truncated_normal" or "untruncated_normal"`, samples are
  drawn from a truncated/untruncated normal distribution with a mean of zero and
  a standard deviation (after truncation, if used) `stddev = sqrt(scale / n)`
  where n is:

    - number of input units in the weight tensor, if mode = "fan_in"
    - number of output units, if mode = "fan_out"
    - average of the numbers of input and output units, if mode = "fan_avg"

  With `distribution="uniform"`, samples are drawn from a uniform distribution
  within [-limit, limit], with `limit = sqrt(3 * scale / n)`.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.VarianceScaling(scale=1.))
  >>> v1
  <tf.Variable ... shape=(3,) ... numpy=array([...], dtype=float32)>
  >>> v2
  <tf.Variable ... shape=(3, 3) ... numpy=
  ...
  >>> make_variables(4, tf.initializers.VarianceScaling(distribution=\'uniform\'))
  (<tf.Variable...shape=(4,) dtype=float32...>, <tf.Variable...shape=(4, 4) ...

  Args:
    scale: Scaling factor (positive float).
    mode: One of "fan_in", "fan_out", "fan_avg".
    distribution: Random distribution to use. One of "truncated_normal",
      "untruncated_normal" and  "uniform".
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.

  Raises:
    ValueError: In case of an invalid value for the "scale", mode" or
      "distribution" arguments.
  '''
    scale: Incomplete
    mode: Incomplete
    distribution: Incomplete
    seed: Incomplete
    def __init__(self, scale: float = 1.0, mode: str = 'fan_in', distribution: str = 'truncated_normal', seed: Incomplete | None = None) -> None: ...
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point
    """
    def get_config(self): ...

class Orthogonal(Initializer):
    """Initializer that generates an orthogonal matrix.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  If the shape of the tensor to initialize is two-dimensional, it is initialized
  with an orthogonal matrix obtained from the QR decomposition of a matrix of
  random numbers drawn from a normal distribution.
  If the matrix has fewer rows than columns then the output will have orthogonal
  rows. Otherwise, the output will have orthogonal columns.

  If the shape of the tensor to initialize is more than two-dimensional,
  a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])`
  is initialized, where `n` is the length of the shape vector.
  The matrix is subsequently reshaped to give a tensor of the desired shape.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.Orthogonal())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.Orthogonal(gain=0.5))
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    gain: multiplicative factor to apply to the orthogonal matrix
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.

  References:
      [Saxe et al., 2014](https://openreview.net/forum?id=_wzZwKpTDF_9C)
      ([pdf](https://arxiv.org/pdf/1312.6120.pdf))
  """
    gain: Incomplete
    seed: Incomplete
    def __init__(self, gain: float = 1.0, seed: Incomplete | None = None) -> None: ...
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
        supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point or the input shape is not
       valid.
    """
    def get_config(self): ...

class Identity(Initializer):
    """Initializer that generates the identity matrix.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Only usable for generating 2D matrices.

  Examples:

  >>> def make_variable(k, initializer):
  ...   return tf.Variable(initializer(shape=[k, k], dtype=tf.float32))
  >>> make_variable(2, tf.initializers.Identity())
  <tf.Variable ... shape=(2, 2) dtype=float32, numpy=
  array([[1., 0.],
         [0., 1.]], dtype=float32)>
  >>> make_variable(3, tf.initializers.Identity(gain=0.5))
  <tf.Variable ... shape=(3, 3) dtype=float32, numpy=
  array([[0.5, 0. , 0. ],
         [0. , 0.5, 0. ],
         [0. , 0. , 0.5]], dtype=float32)>

  Args:
    gain: Multiplicative factor to apply to the identity matrix.
  """
    gain: Incomplete
    def __init__(self, gain: float = 1.0) -> None: ...
    def __call__(self, shape, dtype=..., **kwargs):
        """Returns a tensor object initialized as specified by the initializer.

    Args:
      shape: Shape of the tensor.
      dtype: Optional dtype of the tensor. Only floating point types are
       supported.
      **kwargs: Additional keyword arguments.

    Raises:
      ValueError: If the dtype is not floating point
      ValueError: If the requested shape does not have exactly two axes.
    """
    def get_config(self): ...

class GlorotUniform(VarianceScaling):
    """The Glorot uniform initializer, also called Xavier uniform initializer.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Draws samples from a uniform distribution within [-limit, limit] where `limit`
  is `sqrt(6 / (fan_in + fan_out))` where `fan_in` is the number of input units
  in the weight tensor and `fan_out` is the number of output units in the weight
  tensor.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.GlorotUniform())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.RandomNormal())
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.

  References:
      [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
      ([pdf](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf))
  """
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def get_config(self): ...

class GlorotNormal(VarianceScaling):
    """The Glorot normal initializer, also called Xavier normal initializer.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Draws samples from a truncated normal distribution centered on 0 with `stddev
  = sqrt(2 / (fan_in + fan_out))` where `fan_in` is the number of input units in
  the weight tensor and `fan_out` is the number of output units in the weight
  tensor.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.GlorotNormal())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.RandomNormal())
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.

  References:
      [Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
      ([pdf](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf))
  """
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def get_config(self): ...
zeros_initializer = Zeros
ones_initializer = Ones
constant_initializer = Constant
random_uniform_initializer = RandomUniform
random_normal_initializer = RandomNormal
truncated_normal_initializer = TruncatedNormal
variance_scaling_initializer = VarianceScaling
glorot_uniform_initializer = GlorotUniform
glorot_normal_initializer = GlorotNormal
orthogonal_initializer = Orthogonal
identity_initializer = Identity

def lecun_normal(seed: Incomplete | None = None):
    """LeCun normal initializer.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Draws samples from a truncated normal distribution centered on 0 with `stddev
  = sqrt(1 / fan_in)` where `fan_in` is the number of input units in the weight
  tensor.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.lecun_normal())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.RandomNormal())
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    seed: A Python integer. Used to seed the random generator.

  Returns:
    A callable Initializer with `shape` and `dtype` arguments which generates a
    tensor.

  References:
      - Self-Normalizing Neural Networks,
      [Klambauer et al., 2017]
      (https://papers.nips.cc/paper/6698-self-normalizing-neural-networks)
      ([pdf]
      (https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
      - Efficient Backprop,
      [Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
  """
def lecun_uniform(seed: Incomplete | None = None):
    """LeCun uniform initializer.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Draws samples from a uniform distribution within [-limit, limit] where `limit`
  is `sqrt(3 / fan_in)` where `fan_in` is the number of input units in the
  weight tensor.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.lecun_uniform())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.RandomNormal())
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    seed: A Python integer. Used to seed the random generator.

  Returns:
    A callable Initializer with `shape` and `dtype` arguments which generates a
    tensor.

  References:
      - Self-Normalizing Neural Networks,
      [Klambauer et al., 2017](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks) # pylint: disable=line-too-long
      ([pdf](https://papers.nips.cc/paper/6698-self-normalizing-neural-networks.pdf))
      - Efficient Backprop,
      [Lecun et al., 1998](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
  """
def he_normal(seed: Incomplete | None = None):
    """He normal initializer.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  It draws samples from a truncated normal distribution centered on 0 with
  `stddev = sqrt(2 / fan_in)` where `fan_in` is the number of input units in the
  weight tensor.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.he_normal())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.RandomNormal())
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    seed: A Python integer. Used to seed the random generator.

  Returns:
    A callable Initializer with `shape` and `dtype` arguments which generates a
    tensor.

  References:
      [He et al., 2015](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper.html) # pylint: disable=line-too-long
      ([pdf](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf))
  """
def he_uniform(seed: Incomplete | None = None):
    """He uniform variance scaling initializer.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Draws samples from a uniform distribution within [-limit, limit] where `limit`
  is `sqrt(6 / fan_in)` where `fan_in` is the number of input units in the
  weight tensor.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.he_uniform())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.RandomNormal())
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    seed: A Python integer. Used to seed the random generator.

  Returns:
    A callable Initializer with `shape` and `dtype` arguments which generates a
    tensor.

  References:
      [He et al., 2015](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper.html) # pylint: disable=line-too-long
      ([pdf](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf))
  """

class _RandomGenerator:
    """Random generator that selects appropriate random ops."""
    seed: Incomplete
    def __init__(self, seed: Incomplete | None = None) -> None: ...
    def random_normal(self, shape, mean: float = 0.0, stddev: int = 1, dtype=...):
        """A deterministic random normal if seed is passed."""
    def random_uniform(self, shape, minval, maxval, dtype):
        """A deterministic random uniform if seed is passed."""
    def truncated_normal(self, shape, mean, stddev, dtype):
        """A deterministic truncated normal if seed is passed."""
zero = Zeros
zeros = Zeros
one = Ones
ones = Ones
constant = Constant
uniform = RandomUniform
random_uniform = RandomUniform
normal = RandomNormal
random_normal = RandomNormal
truncated_normal = TruncatedNormal
identity = Identity
orthogonal = Orthogonal
glorot_normal = GlorotNormal
glorot_uniform = GlorotUniform
