from tensorflow.python.ops.gen_math_ops import *
from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, sparse_tensor as sparse_tensor, tensor_conversion_registry as tensor_conversion_registry, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, gen_bitwise_ops as gen_bitwise_ops, gen_data_flow_ops as gen_data_flow_ops, gen_math_ops as gen_math_ops, gen_nn_ops as gen_nn_ops, gen_sparse_ops as gen_sparse_ops
from tensorflow.python.util import compat as compat, deprecation as deprecation, dispatch as dispatch, nest as nest, tf_decorator as tf_decorator, traceback_utils as traceback_utils
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export

np_dtypes: Incomplete
nextafter = gen_math_ops.next_after

def linspace_nd(start, stop, num, name: Incomplete | None = None, axis: int = 0):
    '''Generates evenly-spaced values in an interval along a given axis.

  A sequence of `num` evenly-spaced values are generated beginning at `start`
  along a given `axis`.
  If `num > 1`, the values in the sequence increase by
  `(stop - start) / (num - 1)`, so that the last one is exactly `stop`.
  If `num <= 0`, `ValueError` is raised.

  Matches
  [np.linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)\'s
  behaviour
  except when `num == 0`.

  For example:

  ```
  tf.linspace(10.0, 12.0, 3, name="linspace") => [ 10.0  11.0  12.0]
  ```

  `Start` and `stop` can be tensors of arbitrary size:

  >>> tf.linspace([0., 5.], [10., 40.], 5, axis=0)
  <tf.Tensor: shape=(5, 2), dtype=float32, numpy=
  array([[ 0.  ,  5.  ],
         [ 2.5 , 13.75],
         [ 5.  , 22.5 ],
         [ 7.5 , 31.25],
         [10.  , 40.  ]], dtype=float32)>

  `Axis` is where the values will be generated (the dimension in the
  returned tensor which corresponds to the axis will be equal to `num`)

  >>> tf.linspace([0., 5.], [10., 40.], 5, axis=-1)
  <tf.Tensor: shape=(2, 5), dtype=float32, numpy=
  array([[ 0.  ,  2.5 ,  5.  ,  7.5 , 10.  ],
         [ 5.  , 13.75, 22.5 , 31.25, 40.  ]], dtype=float32)>



  Args:
    start: A `Tensor`. Must be one of the following types: `bfloat16`,
      `float32`, `float64`. N-D tensor. First entry in the range.
    stop: A `Tensor`. Must have the same type and shape as `start`. N-D tensor.
      Last entry in the range.
    num: A `Tensor`. Must be one of the following types: `int32`, `int64`. 0-D
      tensor. Number of values to generate.
    name: A name for the operation (optional).
    axis: Axis along which the operation is performed (used only when N-D
      tensors are provided).

  Returns:
    A `Tensor`. Has the same type as `start`.
  '''
linspace = linspace_nd
arg_max: Incomplete
arg_min: Incomplete

def argmax(input, axis: Incomplete | None = None, name: Incomplete | None = None, dimension: Incomplete | None = None, output_type=...): ...
def argmax_v2(input, axis: Incomplete | None = None, output_type=..., name: Incomplete | None = None):
    """Returns the index with the largest value across axes of a tensor.

  In case of identity returns the smallest index.

  For example:

  >>> A = tf.constant([2, 20, 30, 3, 6])
  >>> tf.math.argmax(A)  # A[2] is maximum in tensor A
  <tf.Tensor: shape=(), dtype=int64, numpy=2>
  >>> B = tf.constant([[2, 20, 30, 3, 6], [3, 11, 16, 1, 8],
  ...                  [14, 45, 23, 5, 27]])
  >>> tf.math.argmax(B, 0)
  <tf.Tensor: shape=(5,), dtype=int64, numpy=array([2, 2, 0, 2, 2])>
  >>> tf.math.argmax(B, 1)
  <tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 2, 1])>
  >>> C = tf.constant([0, 0, 0, 0])
  >>> tf.math.argmax(C) # Returns smallest index in case of ties
  <tf.Tensor: shape=(), dtype=int64, numpy=0>

  Args:
    input: A `Tensor`.
    axis: An integer, the axis to reduce across. Default to 0.
    output_type: An optional output dtype (`tf.int32` or `tf.int64`). Defaults
      to `tf.int64`.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of type `output_type`.
  """
def argmin(input, axis: Incomplete | None = None, name: Incomplete | None = None, dimension: Incomplete | None = None, output_type=...): ...
def argmin_v2(input, axis: Incomplete | None = None, output_type=..., name: Incomplete | None = None):
    """Returns the index with the smallest value across axes of a tensor.

  Returns the smallest index in case of ties.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`,
      `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`,
      `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`,
      `uint64`.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      int32 or int64, must be in the range `-rank(input), rank(input))`.
      Describes which axis of the input Tensor to reduce across. For vectors,
      use axis = 0.
    output_type: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to
      `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `output_type`.

  Usage:
  ```python
  import tensorflow as tf
  a = [1, 10, 26.9, 2.8, 166.32, 62.3]
  b = tf.math.argmin(input = a)
  c = tf.keras.backend.eval(b)
  # c = 0
  # here a[0] = 1 which is the smallest element of a across axis 0
  ```
  """
def abs(x, name: Incomplete | None = None):
    """Computes the absolute value of a tensor.

  Given a tensor of integer or floating-point values, this operation returns a
  tensor of the same type, where each element contains the absolute value of the
  corresponding element in the input.

  Given a tensor `x` of complex numbers, this operation returns a tensor of type
  `float32` or `float64` that is the absolute value of each element in `x`. For
  a complex number \\\\(a + bj\\\\), its absolute value is computed as
  \\\\(\\sqrt{a^2 + b^2}\\\\).

  For example:

  >>> # real number
  >>> x = tf.constant([-2.25, 3.25])
  >>> tf.abs(x)
  <tf.Tensor: shape=(2,), dtype=float32,
  numpy=array([2.25, 3.25], dtype=float32)>

  >>> # complex number
  >>> x = tf.constant([[-2.25 + 4.75j], [-3.25 + 5.75j]])
  >>> tf.abs(x)
  <tf.Tensor: shape=(2, 1), dtype=float64, numpy=
  array([[5.25594901],
         [6.60492241]])>

  Args:
    x: A `Tensor` or `SparseTensor` of type `float16`, `float32`, `float64`,
      `int32`, `int64`, `complex64` or `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` of the same size, type and sparsity as `x`,
      with absolute values. Note, for `complex64` or `complex128` input, the
      returned `Tensor` will be of type `float32` or `float64`, respectively.
  """

class DivideDelegateWithName:
    """Use Python2/Python3 division delegation to implement divide for tensors."""
    x: Incomplete
    name: Incomplete
    def __init__(self, x, name) -> None:
        """Construct DivideDelegateWithName.

    Args:
      x: Tensor to use as left operand in operator overloads
      name: The name that is preferred for the op created.
    """
    def __truediv__(self, y): ...
    def __floordiv__(self, y): ...
    def __div__(self, y): ...

def divide(x, y, name: Incomplete | None = None):
    """Computes Python style division of `x` by `y`.

  For example:

  >>> x = tf.constant([16, 12, 11])
  >>> y = tf.constant([4, 6, 2])
  >>> tf.divide(x,y)
  <tf.Tensor: shape=(3,), dtype=float64,
  numpy=array([4. , 2. , 5.5])>

  Args:
    x: A `Tensor`
    y: A `Tensor`
    name: A name for the operation (optional).

  Returns:
    A `Tensor` with same shape as input
  """
def multiply(x, y, name: Incomplete | None = None):
    """Returns an element-wise x * y.

  For example:

  >>> x = tf.constant(([1, 2, 3, 4]))
  >>> tf.math.multiply(x, x)
  <tf.Tensor: shape=(4,), dtype=..., numpy=array([ 1,  4,  9, 16], dtype=int32)>

  Since `tf.math.multiply` will convert its arguments to `Tensor`s, you can also
  pass in non-`Tensor` arguments:

  >>> tf.math.multiply(7,6)
  <tf.Tensor: shape=(), dtype=int32, numpy=42>

  If `x.shape` is not the same as `y.shape`, they will be broadcast to a
  compatible shape. (More about broadcasting
  [here](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).)

  For example:

  >>> x = tf.ones([1, 2]);
  >>> y = tf.ones([2, 1]);
  >>> x * y  # Taking advantage of operator overriding
  <tf.Tensor: shape=(2, 2), dtype=float32, numpy=
  array([[1., 1.],
       [1., 1.]], dtype=float32)>

  The reduction version of this elementwise operation is `tf.math.reduce_prod`

  Args:
    x: A Tensor. Must be one of the following types: `bfloat16`,
      `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`,
      `int16`, `int32`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:

  A `Tensor`.  Has the same type as `x`.

  Raises:

   * InvalidArgumentError: When `x` and `y` have incompatible shapes or types.
  """
def subtract(x, y, name: Incomplete | None = None): ...
negative = gen_math_ops.neg

def scalar_mul(scalar, x, name: Incomplete | None = None):
    """Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

  This is a special case of `tf.math.multiply`, where the first value must be a
  `scalar`. Unlike the general form of `tf.math.multiply`, this is operation is
  guaranteed to be efficient for `tf.IndexedSlices`.

  >>> x = tf.reshape(tf.range(30, dtype=tf.float32), [10, 3])
  >>> with tf.GradientTape() as g:
  ...   g.watch(x)
  ...   y = tf.gather(x, [1, 2])  # IndexedSlices
  ...   z = tf.math.scalar_mul(10.0, y)

  Args:
    scalar: A 0-D scalar `Tensor`. Must have known shape.
    x: A `Tensor` or `IndexedSlices` to be scaled.
    name: A name for the operation (optional).

  Returns:
    `scalar * x` of the same type (`Tensor` or `IndexedSlices`) as `x`.

  Raises:
    ValueError: if scalar is not a 0-D `scalar`.
  """
def softplus(features, name: Incomplete | None = None):
    '''Computes elementwise softplus: `softplus(x) = log(exp(x) + 1)`.

  `softplus` is a smooth approximation of `relu`. Like `relu`, `softplus` always
  takes on positive values.

  <img style="width:100%" src="https://www.tensorflow.org/images/softplus.png">

  Example:

  >>> import tensorflow as tf
  >>> tf.math.softplus(tf.range(0, 2, dtype=tf.float32)).numpy()
  array([0.6931472, 1.3132616], dtype=float32)

  Args:
    features: `Tensor`
    name: Optional: name to associate with this operation.
  Returns:
    `Tensor`
  '''
def scalar_mul_v2(scalar, x, name: Incomplete | None = None): ...
def pow(x, y, name: Incomplete | None = None):
    """Computes the power of one value to another.

  Given a tensor `x` and a tensor `y`, this operation computes \\\\(x^y\\\\) for
  corresponding elements in `x` and `y`. For example:

  ```python
  x = tf.constant([[2, 2], [3, 3]])
  y = tf.constant([[8, 16], [2, 3]])
  tf.pow(x, y)  # [[256, 65536], [9, 27]]
  ```

  Args:
    x: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
      `complex64`, or `complex128`.
    y: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
      `complex64`, or `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`.
  """
def complex(real, imag, name: Incomplete | None = None):
    """Converts two real numbers to a complex number.

  Given a tensor `real` representing the real part of a complex number, and a
  tensor `imag` representing the imaginary part of a complex number, this
  operation returns complex numbers elementwise of the form \\\\(a + bj\\\\), where
  *a* represents the `real` part and *b* represents the `imag` part.

  The input tensors `real` and `imag` must have the same shape.

  For example:

  ```python
  real = tf.constant([2.25, 3.25])
  imag = tf.constant([4.75, 5.75])
  tf.complex(real, imag)  # [[2.25 + 4.75j], [3.25 + 5.75j]]
  ```

  Args:
    real: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    imag: A `Tensor`. Must have the same type as `real`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64` or `complex128`.

  Raises:
    TypeError: Real and imag must be correct types
  """
def sign(x, name: Incomplete | None = None):
    """Returns an element-wise indication of the sign of a number.

  `y = sign(x) = -1 if x < 0; 0 if x == 0; 1 if x > 0`.

  For complex numbers, `y = sign(x) = x / |x| if x != 0, otherwise y = 0`.

  Example usage:

  >>> # real number
  >>> tf.math.sign([0., 2., -3.])
  <tf.Tensor: shape=(3,), dtype=float32,
  numpy=array([ 0.,  1., -1.], dtype=float32)>

  >>> # complex number
  >>> tf.math.sign([1 + 1j, 0 + 0j])
  <tf.Tensor: shape=(2,), dtype=complex128,
  numpy=array([0.70710678+0.70710678j, 0.        +0.j        ])>

  Args:
   x: A Tensor. Must be one of the following types: bfloat16, half, float32,
     float64, int32, int64, complex64, complex128.
   name: A name for the operation (optional).

  Returns:
   A Tensor. Has the same type as x.

   If x is a SparseTensor, returns SparseTensor(x.indices,
     tf.math.sign(x.values, ...), x.dense_shape).
  """
def real(input, name: Incomplete | None = None):
    """Returns the real part of a complex (or real) tensor.

  Given a tensor `input`, this operation returns a tensor of type `float` that
  is the real part of each element in `input` considered as a complex number.

  For example:

  ```python
  x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
  tf.math.real(x)  # [-2.25, 3.25]
  ```

  If `input` is already real, it is returned unchanged.

  Args:
    input: A `Tensor`. Must have numeric type.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32` or `float64`.
  """
def imag(input, name: Incomplete | None = None):
    """Returns the imaginary part of a complex (or real) tensor.

  Given a tensor `input`, this operation returns a tensor of type `float` that
  is the imaginary part of each element in `input` considered as a complex
  number. If `input` is real, a tensor of all zeros is returned.

  For example:

  ```python
  x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
  tf.math.imag(x)  # [4.75, 5.75]
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float`, `double`,
      `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32` or `float64`.
  """
def angle(input, name: Incomplete | None = None):
    """Returns the element-wise argument of a complex (or real) tensor.

  Given a tensor `input`, this operation returns a tensor of type `float` that
  is the argument of each element in `input` considered as a complex number.

  The elements in `input` are considered to be complex numbers of the form
  \\\\(a + bj\\\\), where *a* is the real part and *b* is the imaginary part.
  If `input` is real then *b* is zero by definition.

  The argument returned by this function is of the form \\\\(atan2(b, a)\\\\).
  If `input` is real, a tensor of all zeros is returned.

  For example:

  ```
  input = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j], dtype=tf.complex64)
  tf.math.angle(input).numpy()
  # ==> array([2.0131705, 1.056345 ], dtype=float32)
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float`, `double`,
      `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32` or `float64`.
  """
def round(x, name: Incomplete | None = None):
    """Rounds the values of a tensor to the nearest integer, element-wise.

  Rounds half to even.  Also known as bankers rounding. If you want to round
  according to the current system rounding mode use tf::cint.
  For example:

  ```python
  x = tf.constant([0.9, 2.5, 2.3, 1.5, -4.5])
  tf.round(x)  # [ 1.0, 2.0, 2.0, 2.0, -4.0 ]
  ```

  Args:
    x: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, or `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of same shape and type as `x`.
  """
def cast(x, dtype, name: Incomplete | None = None):
    """Casts a tensor to a new type.

  The operation casts `x` (in case of `Tensor`) or `x.values`
  (in case of `SparseTensor` or `IndexedSlices`) to `dtype`.

  For example:

  >>> x = tf.constant([1.8, 2.2], dtype=tf.float32)
  >>> tf.cast(x, tf.int32)
  <tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 2], dtype=int32)>

  Notice `tf.cast` has an alias `tf.dtypes.cast`:

  >>> x = tf.constant([1.8, 2.2], dtype=tf.float32)
  >>> tf.dtypes.cast(x, tf.int32)
  <tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 2], dtype=int32)>

  The operation supports data types (for `x` and `dtype`) of
  `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`,
  `float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`.
  In case of casting from complex types (`complex64`, `complex128`) to real
  types, only the real part of `x` is returned. In case of casting from real
  types to complex types (`complex64`, `complex128`), the imaginary part of the
  returned value is set to `0`. The handling of complex types here matches the
  behavior of numpy.

  Note casting nan and inf values to integral types has undefined behavior.

  Note this operation can lead to a loss of precision when converting native
  Python `float` and `complex` variables to `tf.float64` or `tf.complex128`
  tensors, since the input is first converted to the `float32` data type and
  then widened. It is recommended to use `tf.convert_to_tensor` instead of
  `tf.cast` for any non-tensor inputs.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices` of numeric type. It could
      be `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`,
      `int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`,
      `bfloat16`.
    dtype: The destination type. The list of supported dtypes is the same as
      `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` and
      same type as `dtype`.

  Raises:
    TypeError: If `x` cannot be cast to the `dtype`.

  """
def saturate_cast(value, dtype, name: Incomplete | None = None):
    """Performs a safe saturating cast of `value` to `dtype`.

  This function casts the input to `dtype` without overflow.  If
  there is a danger that values would over or underflow in the cast, this op
  applies the appropriate clamping before the cast.  See `tf.cast` for more
  details.

  Args:
    value: A `Tensor`.
    dtype: The desired output `DType`.
    name: A name for the operation (optional).

  Returns:
    `value` safely cast to `dtype`.
  """
def to_float(x, name: str = 'ToFloat'):
    """Casts a tensor to type `float32`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `float32`.

  Raises:
    TypeError: If `x` cannot be cast to the `float32`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.float32)`. There are no further issues with eager execution
  or tf.function.

  Before:

  >>> tf.compat.v1.to_float(tf.constant(3.14, dtype=tf.double))
  <tf.Tensor: shape=(), dtype=float32, numpy=3.14>

  After:

  >>> tf.cast(tf.constant(3.14, dtype=tf.double), tf.float32)
  <tf.Tensor: shape=(), dtype=float32, numpy=3.14>

  @end_compatibility

  """
def to_double(x, name: str = 'ToDouble'):
    """Casts a tensor to type `float64`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `float64`.

  Raises:
    TypeError: If `x` cannot be cast to the `float64`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.double)`. There are no further issues with eager execution or
  tf.function.

  Before:

  >>> tf.compat.v1.to_double(tf.constant(3.14, dtype=tf.float32))
  <tf.Tensor: shape=(), dtype=float64, numpy=3.14>

  After:

  >>> tf.cast(tf.constant(3.14, dtype=tf.float32), tf.double)
  <tf.Tensor: shape=(), dtype=float64, numpy=3.14>

  @end_compatibility

  """
def to_int32(x, name: str = 'ToInt32'):
    """Casts a tensor to type `int32`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `int32`.

  Raises:
    TypeError: If `x` cannot be cast to the `int32`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.int32)`. There are no further issues with eager execution or
  tf.function.

  Before:

  >>> tf.compat.v1.to_int32(tf.constant(1, dtype=tf.int64))
  <tf.Tensor: shape=(), dtype=int32, numpy=1>

  After:

  >>> tf.cast(tf.constant(1, dtype=tf.int64), tf.int32)
  <tf.Tensor: shape=(), dtype=int32, numpy=1>

  @end_compatibility

  """
def to_int64(x, name: str = 'ToInt64'):
    """Casts a tensor to type `int64`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `int64`.

  Raises:
    TypeError: If `x` cannot be cast to the `int64`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.int64)`. There are no further issues with eager execution or
  tf.function.

  Before:

  >>> tf.compat.v1.to_int64(tf.constant(1, dtype=tf.int32))
  <tf.Tensor: shape=(), dtype=int64, numpy=1>

  After:

  >>> tf.cast(tf.constant(1, dtype=tf.int32), tf.int64)
  <tf.Tensor: shape=(), dtype=int64, numpy=1>

  @end_compatibility

  """
def to_bfloat16(x, name: str = 'ToBFloat16'):
    """Casts a tensor to type `bfloat16`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `bfloat16`.

  Raises:
    TypeError: If `x` cannot be cast to the `bfloat16`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.bfloat16)`. There are no further issues with eager execution
  or tf.function.

  Before:

  >>> tf.compat.v1.to_bfloat16(tf.constant(3.14, dtype=tf.float32))
  <tf.Tensor: shape=(), dtype=bfloat16, numpy=3.14>

  After:

  >>> tf.cast(tf.constant(3.14, dtype=tf.float32), tf.bfloat16)
  <tf.Tensor: shape=(), dtype=bfloat16, numpy=3.14>

  @end_compatibility

  """
def to_complex64(x, name: str = 'ToComplex64'):
    """Casts a tensor to type `complex64`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `complex64`.

  Raises:
    TypeError: If `x` cannot be cast to the `complex64`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.complex64)`. There are no further issues with eager execution
  or tf.function.

  Before:

  >>> tf.compat.v1.to_complex64(tf.constant(1. + 2.j, dtype=tf.complex128))
  <tf.Tensor: shape=(), dtype=complex64, numpy=(1+2j)>

  After:

  >>> tf.cast(tf.constant(1. + 2.j, dtype=tf.complex128), tf.complex64)
  <tf.Tensor: shape=(), dtype=complex64, numpy=(1+2j)>

  @end_compatibility

  """
def to_complex128(x, name: str = 'ToComplex128'):
    """Casts a tensor to type `complex128`.

  Args:
    x: A `Tensor` or `SparseTensor` or `IndexedSlices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` with
    type `complex128`.

  Raises:
    TypeError: If `x` cannot be cast to the `complex128`.

  @compatibility(TF2)

  This name was deprecated and removed in TF2, but has an exact replacement
  `tf.cast(..., tf.complex128)`. There are no further issues with eager
  execution or tf.function.

  Before:

  >>> tf.compat.v1.to_complex128(tf.constant(1. + 2.j, dtype=tf.complex64))
  <tf.Tensor: shape=(), dtype=complex128, numpy=(1+2j)>

  After:

  >>> tf.cast(tf.constant(1. + 2.j, dtype=tf.complex64), tf.complex128)
  <tf.Tensor: shape=(), dtype=complex128, numpy=(1+2j)>

  @end_compatibility

  """
def maybe_promote_tensors(*tensors, force_same_dtype: bool = False):
    """Promotes tensors if numpy style promotion is enabled.

  This function promotes `tensors` according to numpy promotion rules
  if numpy style promotion is enabled.  Otherwise, if
  `force_same_dtype` is `True`, it force-casts `tensors[1:]` to
  `tensor[0]`'s dtype. Note that this force-cast can be problematic.
  For example, when some `tensors[1:]` elements can be silently
  downcasted.

  Args:
    *tensors: the list of tensors to promote.
    force_same_dtype: bool (optional, default to `False`). When numpy
      style promotion is disabled and `force_same_dtype` is `True`,
      this function will force-casts `tensors[1:]` to `tensor[0]`'s
      dtype (which could be problematic).

  Returns:
    The promoted list of tensors.
  """
def truediv(x, y, name: Incomplete | None = None):
    """Divides x / y elementwise (using Python 3 division operator semantics).

  NOTE: Prefer using the Tensor operator or tf.divide which obey Python
  division operator semantics.

  This function forces Python 3 division operator semantics where all integer
  arguments are cast to floating types first.   This op is generated by normal
  `x / y` division in Python 3 and in Python 2.7 with
  `from __future__ import division`.  If you want integer division that rounds
  down, use `x // y` or `tf.math.floordiv`.

  `x` and `y` must have the same numeric type.  If the inputs are floating
  point, the output will have the same type.  If the inputs are integral, the
  inputs are cast to `float32` for `int8` and `int16` and `float64` for `int32`
  and `int64` (matching the behavior of Numpy).

  Args:
    x: `Tensor` numerator of numeric type.
    y: `Tensor` denominator of numeric type.
    name: A name for the operation (optional).

  Returns:
    `x / y` evaluated in floating point.

  Raises:
    TypeError: If `x` and `y` have different dtypes.
  """
def div(x, y, name: Incomplete | None = None):
    """Divides x / y elementwise (using Python 2 division operator semantics).

  @compatibility(TF2)
  This function is deprecated in TF2. Prefer using the Tensor division operator,
  `tf.divide`, or `tf.math.divide`, which obey the Python 3 division operator
  semantics.
  @end_compatibility


  This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
  and `y` are both integers then the result will be an integer. This is in
  contrast to Python 3, where division with `/` is always a float while division
  with `//` is always an integer.

  Args:
    x: `Tensor` numerator of real numeric type.
    y: `Tensor` denominator of real numeric type.
    name: A name for the operation (optional).

  Returns:
    `x / y` returns the quotient of x and y.
  """
def div_no_nan(x, y, name: Incomplete | None = None):
    """Computes a safe divide which returns 0 if `y` (denominator) is zero.

  For example:

  >>> tf.constant(3.0) / 0.0
  <tf.Tensor: shape=(), dtype=float32, numpy=inf>
  >>> tf.math.divide_no_nan(3.0, 0.0)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.0>

  Note that 0 is returned if `y` is 0 even if `x` is nonfinite:

  >>> tf.math.divide_no_nan(np.nan, 0.0)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.0>

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    y: A `Tensor` whose dtype is compatible with `x`.
    name: A name for the operation (optional).

  Returns:
    The element-wise value of the x divided by y.
  """
def multiply_no_nan(x, y, name: Incomplete | None = None):
    """Computes the product of x and y and returns 0 if the y is zero, even if x is NaN or infinite.

  Note this is noncommutative: if y is NaN or infinite and x is 0, the result
  will be NaN.

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    y: A `Tensor` whose dtype is compatible with `x`.
    name: A name for the operation (optional).

  Returns:
    The element-wise value of the x times y.
  """
mod = gen_math_ops.floor_mod

def floordiv(x, y, name: Incomplete | None = None):
    """Divides `x / y` elementwise, rounding toward the most negative integer.

  Mathematically, this is equivalent to floor(x / y). For example:
    floor(8.4 / 4.0) = floor(2.1) = 2.0
    floor(-8.4 / 4.0) = floor(-2.1) = -3.0
  This is equivalent to the '//' operator in Python 3.0 and above.

  Note: `x` and `y` must have the same type, and the result will have the same
  type as well.

  Args:
    x: `Tensor` numerator of real numeric type.
    y: `Tensor` denominator of real numeric type.
    name: A name for the operation (optional).

  Returns:
    `x / y` rounded toward -infinity.

  Raises:
    TypeError: If the inputs are complex.
  """
realdiv = gen_math_ops.real_div
truncatediv = gen_math_ops.truncate_div
floor_div = gen_math_ops.floor_div
truncatemod = gen_math_ops.truncate_mod
floormod = gen_math_ops.floor_mod

def logical_xor(x, y, name: str = 'LogicalXor'):
    """Logical XOR function.

  x ^ y = (x | y) & ~(x & y)

  Requires that `x` and `y` have the same shape or have
  [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  shapes. For example, `x` and `y` can be:

  - Two single elements of type `bool`
  - One `tf.Tensor` of type `bool` and one single `bool`, where the result will
    be calculated by applying logical XOR with the single element to each
    element in the larger Tensor.
  - Two `tf.Tensor` objects of type `bool` of the same shape. In this case,
    the result will be the element-wise logical XOR of the two input tensors.

  Usage:

  >>> a = tf.constant([True])
  >>> b = tf.constant([False])
  >>> tf.math.logical_xor(a, b)
  <tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>

  >>> c = tf.constant([True])
  >>> x = tf.constant([False, True, True, False])
  >>> tf.math.logical_xor(c, x)
  <tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True, False, False,  True])>

  >>> y = tf.constant([False, False, True, True])
  >>> z = tf.constant([False, True, False, True])
  >>> tf.math.logical_xor(y, z)
  <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>

  Args:
      x: A `tf.Tensor` type bool.
      y: A `tf.Tensor` of type bool.
      name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of type bool with the same size as that of x or y.
  """
def and_(x, y, name: Incomplete | None = None): ...
def or_(x, y, name: Incomplete | None = None): ...
def xor_(x, y, name: Incomplete | None = None): ...
def invert_(x, name: Incomplete | None = None): ...
def equal(x, y, name: Incomplete | None = None):
    """Returns the truth value of (x == y) element-wise.

  Performs a [broadcast](
  https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) with the
  arguments and then an element-wise equality comparison, returning a Tensor of
  boolean values.

  For example:

  >>> x = tf.constant([2, 4])
  >>> y = tf.constant(2)
  >>> tf.math.equal(x, y)
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  False])>

  >>> x = tf.constant([2, 4])
  >>> y = tf.constant([2, 4])
  >>> tf.math.equal(x, y)
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  True])>

  Args:
    x: A `tf.Tensor`.
    y: A `tf.Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of type bool with the same size as that of x or y.

  Raises:
    `tf.errors.InvalidArgumentError`: If shapes of arguments are incompatible
  """
def not_equal(x, y, name: Incomplete | None = None):
    """Returns the truth value of (x != y) element-wise.

  Performs a [broadcast](
  https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) with the
  arguments and then an element-wise inequality comparison, returning a Tensor
  of boolean values.

  For example:

  >>> x = tf.constant([2, 4])
  >>> y = tf.constant(2)
  >>> tf.math.not_equal(x, y)
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>

  >>> x = tf.constant([2, 4])
  >>> y = tf.constant([2, 4])
  >>> tf.math.not_equal(x, y)
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  False])>

  Args:
    x: A `tf.Tensor`.
    y: A `tf.Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of type bool with the same size as that of x or y.

  Raises:
    `tf.errors.InvalidArgumentError`: If shapes of arguments are incompatible
  """
def tensor_equals(self, other):
    """The operation invoked by the `Tensor.__eq__` operator.

  Compares two tensors element-wise for equality if they are
  broadcast-compatible; or returns False if they are not broadcast-compatible.
  (Note that this behavior differs from `tf.math.equal`, which raises an
  exception if the two tensors are not broadcast-compatible.)

  Purpose in the API:

    This method is exposed in TensorFlow's API so that library developers
    can register dispatching for `Tensor.__eq__` to allow it to handle
    custom composite tensors & other custom objects.

    The API symbol is not intended to be called by users directly and does
    appear in TensorFlow's generated documentation.

  Args:
    self: The left-hand side of the `==` operator.
    other: The right-hand side of the `==` operator.

  Returns:
    The result of the elementwise `==` operation, or `False` if the arguments
    are not broadcast-compatible.
  """
def tensor_not_equals(self, other):
    """The operation invoked by the `Tensor.__ne__` operator.

  Compares two tensors element-wise for inequality if they are
  broadcast-compatible; or returns True if they are not broadcast-compatible.
  (Note that this behavior differs from `tf.math.not_equal`, which raises an
  exception if the two tensors are not broadcast-compatible.)

  Purpose in the API:

    This method is exposed in TensorFlow's API so that library developers
    can register dispatching for `Tensor.__ne__` to allow it to handle
    custom composite tensors & other custom objects.

    The API symbol is not intended to be called by users directly and does
    appear in TensorFlow's generated documentation.

  Args:
    self: The left-hand side of the `!=` operator.
    other: The right-hand side of the `!=` operator.

  Returns:
    The result of the elementwise `!=` operation, or `True` if the arguments
    are not broadcast-compatible.
  """
def range(start, limit: Incomplete | None = None, delta: int = 1, dtype: Incomplete | None = None, name: str = 'range'):
    '''Creates a sequence of numbers.

  Creates a sequence of numbers that begins at `start` and extends by
  increments of `delta` up to but not including `limit`.

  The dtype of the resulting tensor is inferred from the inputs unless
  it is provided explicitly.

  Like the Python builtin `range`, `start` defaults to 0, so that
  `range(n) = range(0, n)`.

  For example:

  >>> start = 3
  >>> limit = 18
  >>> delta = 3
  >>> tf.range(start, limit, delta)
  <tf.Tensor: shape=(5,), dtype=int32,
  numpy=array([ 3,  6,  9, 12, 15], dtype=int32)>

  >>> start = 3
  >>> limit = 1
  >>> delta = -0.5
  >>> tf.range(start, limit, delta)
  <tf.Tensor: shape=(4,), dtype=float32,
  numpy=array([3. , 2.5, 2. , 1.5], dtype=float32)>

  >>> limit = 5
  >>> tf.range(limit)
  <tf.Tensor: shape=(5,), dtype=int32,
  numpy=array([0, 1, 2, 3, 4], dtype=int32)>

  Args:
    start: A 0-D `Tensor` (scalar). Acts as first entry in the range if `limit`
      is not None; otherwise, acts as range limit and first entry defaults to 0.
    limit: A 0-D `Tensor` (scalar). Upper limit of sequence, exclusive. If None,
      defaults to the value of `start` while the first entry of the range
      defaults to 0.
    delta: A 0-D `Tensor` (scalar). Number that increments `start`. Defaults to
      1.
    dtype: The type of the elements of the resulting tensor.
    name: A name for the operation. Defaults to "range".

  Returns:
    An 1-D `Tensor` of type `dtype`.

  @compatibility(numpy)
  Equivalent to np.arange
  @end_compatibility
  '''
def reduce_sum_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes the sum of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.add` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> # x has a shape of (2, 3) (two rows and three columns):
    >>> x = tf.constant([[1, 1, 1], [1, 1, 1]])
    >>> x.numpy()
    array([[1, 1, 1],
           [1, 1, 1]], dtype=int32)
    >>> # sum all the elements
    >>> # 1 + 1 + 1 + 1 + 1+ 1 = 6
    >>> tf.reduce_sum(x).numpy()
    6
    >>> # reduce along the first dimension
    >>> # the result is [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
    >>> tf.reduce_sum(x, 0).numpy()
    array([2, 2, 2], dtype=int32)
    >>> # reduce along the second dimension
    >>> # the result is [1, 1] + [1, 1] + [1, 1] = [3, 3]
    >>> tf.reduce_sum(x, 1).numpy()
    array([3, 3], dtype=int32)
    >>> # keep the original dimensions
    >>> tf.reduce_sum(x, 1, keepdims=True).numpy()
    array([[3],
           [3]], dtype=int32)
    >>> # reduce along both dimensions
    >>> # the result is 1 + 1 + 1 + 1 + 1 + 1 = 6
    >>> # or, equivalently, reduce along rows, then reduce the resultant array
    >>> # [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
    >>> # 2 + 2 + 2 = 6
    >>> tf.reduce_sum(x, [0, 1]).numpy()
    6

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor, of the same dtype as the input_tensor.

  @compatibility(numpy)
  Equivalent to np.sum apart the fact that numpy upcast uint8 and int32 to
  int64 while tensorflow returns the same dtype as the input.
  @end_compatibility
  """
def reduce_sum(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes the sum of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.add` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> # x has a shape of (2, 3) (two rows and three columns):
    >>> x = tf.constant([[1, 1, 1], [1, 1, 1]])
    >>> x.numpy()
    array([[1, 1, 1],
           [1, 1, 1]], dtype=int32)
    >>> # sum all the elements
    >>> # 1 + 1 + 1 + 1 + 1+ 1 = 6
    >>> tf.reduce_sum(x).numpy()
    6
    >>> # reduce along the first dimension
    >>> # the result is [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
    >>> tf.reduce_sum(x, 0).numpy()
    array([2, 2, 2], dtype=int32)
    >>> # reduce along the second dimension
    >>> # the result is [1, 1] + [1, 1] + [1, 1] = [3, 3]
    >>> tf.reduce_sum(x, 1).numpy()
    array([3, 3], dtype=int32)
    >>> # keep the original dimensions
    >>> tf.reduce_sum(x, 1, keepdims=True).numpy()
    array([[3],
           [3]], dtype=int32)
    >>> # reduce along both dimensions
    >>> # the result is 1 + 1 + 1 + 1 + 1 + 1 = 6
    >>> # or, equivalently, reduce along rows, then reduce the resultant array
    >>> # [1, 1, 1] + [1, 1, 1] = [2, 2, 2]
    >>> # 2 + 2 + 2 = 6
    >>> tf.reduce_sum(x, [0, 1]).numpy()
    6

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor)]`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor, of the same dtype as the input_tensor.

  @compatibility(numpy)
  Equivalent to np.sum apart the fact that numpy upcast uint8 and int32 to
  int64 while tensorflow returns the same dtype as the input.
  @end_compatibility
  """
def reduce_sum_with_dims(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None, dims: Incomplete | None = None): ...
def reduce_euclidean_norm(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes the Euclidean norm of elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

  ```python
  x = tf.constant([[1, 2, 3], [1, 1, 1]]) # x.dtype is tf.int32
  tf.math.reduce_euclidean_norm(x)  # returns 4 as dtype is tf.int32
  y = tf.constant([[1, 2, 3], [1, 1, 1]], dtype = tf.float32)
  tf.math.reduce_euclidean_norm(y)  # returns 4.1231055 which is sqrt(17)
  tf.math.reduce_euclidean_norm(y, 0)  # [sqrt(2), sqrt(5), sqrt(10)]
  tf.math.reduce_euclidean_norm(y, 1)  # [sqrt(14), sqrt(3)]
  tf.math.reduce_euclidean_norm(y, 1, keepdims=True)  # [[sqrt(14)], [sqrt(3)]]
  tf.math.reduce_euclidean_norm(y, [0, 1])  # sqrt(17)
  ```

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor, of the same dtype as the input_tensor.
  """
def count_nonzero(input_tensor: Incomplete | None = None, axis: Incomplete | None = None, keepdims: Incomplete | None = None, dtype=..., name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None, input: Incomplete | None = None):
    '''Computes number of nonzero elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  entry in `axis`. If `keepdims` is true, the reduced dimensions
  are retained with length 1.

  If `axis` has no entries, all dimensions are reduced, and a
  tensor with a single element is returned.

  **NOTE** Floating point comparison to zero is done by exact floating point
  equality check.  Small values are **not** rounded to zero for purposes of
  the nonzero check.

  For example:

  ```python
  x = tf.constant([[0, 1, 0], [1, 1, 0]])
  tf.math.count_nonzero(x)  # 3
  tf.math.count_nonzero(x, 0)  # [1, 2, 0]
  tf.math.count_nonzero(x, 1)  # [1, 2]
  tf.math.count_nonzero(x, 1, keepdims=True)  # [[1], [2]]
  tf.math.count_nonzero(x, [0, 1])  # 3
  ```

  **NOTE** Strings are compared against zero-length empty string `""`. Any
  string with a size greater than zero is already considered as nonzero.

  For example:
  ```python
  x = tf.constant(["", "a", "  ", "b", ""])
  tf.math.count_nonzero(x) # 3, with "a", "  ", and "b" as nonzero strings.
  ```

  Args:
    input_tensor: The tensor to reduce. Should be of numeric type, `bool`, or
      `string`.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    dtype: The output dtype; defaults to `tf.int64`.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.
    input: Overrides input_tensor. For compatibility.

  Returns:
    The reduced tensor (number of nonzero values).
  '''
def count_nonzero_v2(input, axis: Incomplete | None = None, keepdims: Incomplete | None = None, dtype=..., name: Incomplete | None = None):
    '''Computes number of nonzero elements across dimensions of a tensor.

  Reduces `input` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  entry in `axis`. If `keepdims` is true, the reduced dimensions
  are retained with length 1.

  If `axis` has no entries, all dimensions are reduced, and a
  tensor with a single element is returned.

  **NOTE** Floating point comparison to zero is done by exact floating point
  equality check.  Small values are **not** rounded to zero for purposes of
  the nonzero check.

  For example:

  ```python
  x = tf.constant([[0, 1, 0], [1, 1, 0]])
  tf.math.count_nonzero(x)  # 3
  tf.math.count_nonzero(x, 0)  # [1, 2, 0]
  tf.math.count_nonzero(x, 1)  # [1, 2]
  tf.math.count_nonzero(x, 1, keepdims=True)  # [[1], [2]]
  tf.math.count_nonzero(x, [0, 1])  # 3
  ```

  **NOTE** Strings are compared against zero-length empty string `""`. Any
  string with a size greater than zero is already considered as nonzero.

  For example:
  ```python
  x = tf.constant(["", "a", "  ", "b", ""])
  tf.math.count_nonzero(x) # 3, with "a", "  ", and "b" as nonzero strings.
  ```

  Args:
    input: The tensor to reduce. Should be of numeric type, `bool`, or `string`.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input), rank(input))`.
    keepdims: If true, retains reduced dimensions with length 1.
    dtype: The output dtype; defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor (number of nonzero values).
  '''
def reduce_mean_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes the mean of elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `axis` by computing the
  mean of elements across the dimensions in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a tensor with a single
  element is returned.

  For example:

  >>> x = tf.constant([[1., 1.], [2., 2.]])
  >>> tf.reduce_mean(x)
  <tf.Tensor: shape=(), dtype=float32, numpy=1.5>
  >>> tf.reduce_mean(x, 0)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([1.5, 1.5], dtype=float32)>
  >>> tf.reduce_mean(x, 1)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 2.], dtype=float32)>

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.mean

  Please note that `np.mean` has a `dtype` parameter that could be used to
  specify the output type. By default this is `dtype=float64`. On the other
  hand, `tf.reduce_mean` has an aggressive type inference from `input_tensor`,
  for example:

  >>> x = tf.constant([1, 0, 1, 0])
  >>> tf.reduce_mean(x)
  <tf.Tensor: shape=(), dtype=int32, numpy=0>
  >>> y = tf.constant([1., 0., 1., 0.])
  >>> tf.reduce_mean(y)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.5>

  @end_compatibility
  """
def reduce_mean(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes the mean of elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `axis` by computing the
  mean of elements across the dimensions in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a tensor with a single
  element is returned.

  For example:

  >>> x = tf.constant([[1., 1.], [2., 2.]])
  >>> tf.reduce_mean(x)
  <tf.Tensor: shape=(), dtype=float32, numpy=1.5>
  >>> tf.reduce_mean(x, 0)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([1.5, 1.5], dtype=float32)>
  >>> tf.reduce_mean(x, 1)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 2.], dtype=float32)>

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.mean

  Please note that `np.mean` has a `dtype` parameter that could be used to
  specify the output type. By default this is `dtype=float64`. On the other
  hand, `tf.reduce_mean` has an aggressive type inference from `input_tensor`,
  for example:

  >>> x = tf.constant([1, 0, 1, 0])
  >>> tf.reduce_mean(x)
  <tf.Tensor: shape=(), dtype=int32, numpy=0>
  >>> y = tf.constant([1., 0., 1., 0.])
  >>> tf.reduce_mean(y)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.5>

  @end_compatibility
  """
def reduce_variance(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes the variance of elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

  >>> x = tf.constant([[1., 2.], [3., 4.]])
  >>> tf.math.reduce_variance(x)
  <tf.Tensor: shape=(), dtype=float32, numpy=1.25>
  >>> tf.math.reduce_variance(x, 0)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 1.], ...)>
  >>> tf.math.reduce_variance(x, 1)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([0.25, 0.25], ...)>

  Args:
    input_tensor: The tensor to reduce. Should have real or complex type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name scope for the associated operations (optional).

  Returns:
    The reduced tensor, of the same dtype as the input_tensor. Note,  for
    `complex64` or `complex128` input, the returned `Tensor` will be of type
    `float32` or `float64`, respectively.

  @compatibility(numpy)
  Equivalent to np.var

  Please note `np.var` has a `dtype` parameter that could be used to specify the
  output type. By default this is `dtype=float64`. On the other hand,
  `tf.math.reduce_variance` has aggressive type inference from `input_tensor`.
  @end_compatibility
  """
def reduce_std(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes the standard deviation of elements across dimensions of a tensor.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

  >>> x = tf.constant([[1., 2.], [3., 4.]])
  >>> tf.math.reduce_std(x)
  <tf.Tensor: shape=(), dtype=float32, numpy=1.118034>
  >>> tf.math.reduce_std(x, 0)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([1., 1.], dtype=float32)>
  >>> tf.math.reduce_std(x, 1)
  <tf.Tensor: shape=(2,), dtype=float32, numpy=array([0.5, 0.5], dtype=float32)>

  Args:
    input_tensor: The tensor to reduce. Should have real or complex type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name scope for the associated operations (optional).

  Returns:
    The reduced tensor, of the same dtype as the input_tensor. Note,  for
    `complex64` or `complex128` input, the returned `Tensor` will be of type
    `float32` or `float64`, respectively.

  @compatibility(numpy)
  Equivalent to np.std

  Please note `np.std` has a `dtype` parameter that could be used to specify the
  output type. By default this is `dtype=float64`. On the other hand,
  `tf.math.reduce_std` has aggressive type inference from `input_tensor`.
  @end_compatibility
  """
def reduce_prod(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes `tf.math.multiply` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.multiply` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  entry in `axis`. If `keepdims` is true, the reduced dimensions
  are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> x = tf.constant([[1., 2.], [3., 4.]])
    >>> tf.math.reduce_prod(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=24.>
    >>> tf.math.reduce_prod(x, 0)
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([3., 8.], dtype=float32)>
    >>> tf.math.reduce_prod(x, 1)
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([2., 12.],
    dtype=float32)>

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.prod
  @end_compatibility
  """
def reduce_prod_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes `tf.math.multiply` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.multiply` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> x = tf.constant([[1., 2.], [3., 4.]])
    >>> tf.math.reduce_prod(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=24.>
    >>> tf.math.reduce_prod(x, 0)
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([3., 8.], dtype=float32)>
    >>> tf.math.reduce_prod(x, 1)
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([2., 12.],
    dtype=float32)>

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.prod
  @end_compatibility
  """
def reduce_min_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes the `tf.math.minimum` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.minimum` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  Usage example:

    >>> x = tf.constant([5, 1, 2, 4])
    >>> tf.reduce_min(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=1>
    >>> x = tf.constant([-5, -1, -2, -4])
    >>> tf.reduce_min(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=-5>
    >>> x = tf.constant([4, float('nan')])
    >>> tf.reduce_min(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=nan>
    >>> x = tf.constant([float('nan'), float('nan')])
    >>> tf.reduce_min(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=nan>
    >>> x = tf.constant([float('-inf'), float('inf')])
    >>> tf.reduce_min(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=-inf>

  See the numpy docs for `np.amin` and `np.nanmin` behavior.

  Args:
    input_tensor: The tensor to reduce. Should have real numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.
  """
def reduce_min(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes the `tf.math.minimum` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.minimum` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

  >>> a = tf.constant([
  ...   [[1, 2], [3, 4]],
  ...   [[1, 2], [3, 4]]
  ... ])
  >>> tf.reduce_min(a)
  <tf.Tensor: shape=(), dtype=int32, numpy=1>

  Choosing a specific axis returns minimum element in the given axis:

  >>> b = tf.constant([[1, 2, 3], [4, 5, 6]])
  >>> tf.reduce_min(b, axis=0)
  <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 2, 3], dtype=int32)>
  >>> tf.reduce_min(b, axis=1)
  <tf.Tensor: shape=(2,), dtype=int32, numpy=array([1, 4], dtype=int32)>

  Setting `keepdims` to `True` retains the dimension of `input_tensor`:

  >>> tf.reduce_min(a, keepdims=True)
  <tf.Tensor: shape=(1, 1, 1), dtype=int32, numpy=array([[[1]]], dtype=int32)>
  >>> tf.math.reduce_min(a, axis=0, keepdims=True)
  <tf.Tensor: shape=(1, 2, 2), dtype=int32, numpy=
  array([[[1, 2],
          [3, 4]]], dtype=int32)>

  Args:
    input_tensor: The tensor to reduce. Should have real numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.min
  @end_compatibility
  """
def reduce_max_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes `tf.math.maximum` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.maximum` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  Usage example:

    >>> x = tf.constant([5, 1, 2, 4])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=5>
    >>> x = tf.constant([-5, -1, -2, -4])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=-1>
    >>> x = tf.constant([4, float('nan')])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=nan>
    >>> x = tf.constant([float('nan'), float('nan')])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=nan>
    >>> x = tf.constant([float('-inf'), float('inf')])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=inf>

  See the numpy docs for `np.amax` and `np.nanmax` behavior.

  Args:
    input_tensor: The tensor to reduce. Should have real numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.
  """
def reduce_max(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes `tf.math.maximum` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.maximum` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  Usage example:

    >>> x = tf.constant([5, 1, 2, 4])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=5>
    >>> x = tf.constant([-5, -1, -2, -4])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=-1>
    >>> x = tf.constant([4, float('nan')])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=nan>
    >>> x = tf.constant([float('nan'), float('nan')])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=nan>
    >>> x = tf.constant([float('-inf'), float('inf')])
    >>> tf.reduce_max(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=inf>

  See the numpy docs for `np.amax` and `np.nanmax` behavior.

  Args:
    input_tensor: The tensor to reduce. Should have real numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.
  """
def reduce_max_with_dims(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None, dims: Incomplete | None = None): ...
def reduce_all_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes `tf.math.logical_and` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.logical_and` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> x = tf.constant([[True,  True], [False, False]])
    >>> tf.math.reduce_all(x)
    <tf.Tensor: shape=(), dtype=bool, numpy=False>
    >>> tf.math.reduce_all(x, 0)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([False, False])>
    >>> tf.math.reduce_all(x, 1)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>

  Args:
    input_tensor: The boolean tensor to reduce.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.all
  @end_compatibility
  """
def reduce_all(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes `tf.math.logical_and` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.logical_and` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> x = tf.constant([[True,  True], [False, False]])
    >>> tf.math.reduce_all(x)
    <tf.Tensor: shape=(), dtype=bool, numpy=False>
    >>> tf.math.reduce_all(x, 0)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([False, False])>
    >>> tf.math.reduce_all(x, 1)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>

  Args:
    input_tensor: The boolean tensor to reduce.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.all
  @end_compatibility
  """
def reduce_any_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes `tf.math.logical_or` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.logical_or` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> x = tf.constant([[True,  True], [False, False]])
    >>> tf.reduce_any(x)
    <tf.Tensor: shape=(), dtype=bool, numpy=True>
    >>> tf.reduce_any(x, 0)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  True])>
    >>> tf.reduce_any(x, 1)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>

  Args:
    input_tensor: The boolean tensor to reduce.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.any
  @end_compatibility
  """
def reduce_any(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes `tf.math.logical_or` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.logical_or` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> x = tf.constant([[True,  True], [False, False]])
    >>> tf.reduce_any(x)
    <tf.Tensor: shape=(), dtype=bool, numpy=True>
    >>> tf.reduce_any(x, 0)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  True])>
    >>> tf.reduce_any(x, 1)
    <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True, False])>

  Args:
    input_tensor: The boolean tensor to reduce.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.any
  @end_compatibility
  """
def reduce_logsumexp_v1(input_tensor, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None, reduction_indices: Incomplete | None = None, keep_dims: Incomplete | None = None):
    """Computes log(sum(exp(elements across dimensions of a tensor))).

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` has no entries, all dimensions are reduced, and a
  tensor with a single element is returned.

  This function is more numerically stable than log(sum(exp(input))). It avoids
  overflows caused by taking the exp of large inputs and underflows caused by
  taking the log of small inputs.

  For example:

  ```python
  x = tf.constant([[0., 0., 0.], [0., 0., 0.]])
  tf.reduce_logsumexp(x)  # log(6)
  tf.reduce_logsumexp(x, 0)  # [log(2), log(2), log(2)]
  tf.reduce_logsumexp(x, 1)  # [log(3), log(3)]
  tf.reduce_logsumexp(x, 1, keepdims=True)  # [[log(3)], [log(3)]]
  tf.reduce_logsumexp(x, [0, 1])  # log(6)
  ```

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.
  """
def reduce_logsumexp(input_tensor, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """Computes log(sum(exp(elements across dimensions of a tensor))).

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` has no entries, all dimensions are reduced, and a
  tensor with a single element is returned.

  This function is more numerically stable than log(sum(exp(input))). It avoids
  overflows caused by taking the exp of large inputs and underflows caused by
  taking the log of small inputs.

  For example:

  ```python
  x = tf.constant([[0., 0., 0.], [0., 0., 0.]])
  tf.reduce_logsumexp(x)  # log(6)
  tf.reduce_logsumexp(x, 0)  # [log(2), log(2), log(2)]
  tf.reduce_logsumexp(x, 1)  # [log(3), log(3)]
  tf.reduce_logsumexp(x, 1, keepdims=True)  # [[log(3)], [log(3)]]
  tf.reduce_logsumexp(x, [0, 1])  # log(6)
  ```

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    The reduced tensor.
  """
def trace(x, name: Incomplete | None = None):
    """Compute the trace of a tensor `x`.

  `trace(x)` returns the sum along the main diagonal of each inner-most matrix
  in x. If x is of rank `k` with shape `[I, J, K, ..., L, M, N]`, then output
  is a tensor of rank `k-2` with dimensions `[I, J, K, ..., L]` where

  `output[i, j, k, ..., l] = trace(x[i, j, k, ..., l, :, :])`

  For example:

  ```python
  x = tf.constant([[1, 2], [3, 4]])
  tf.linalg.trace(x)  # 5

  x = tf.constant([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
  tf.linalg.trace(x)  # 15

  x = tf.constant([[[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[-1, -2, -3],
                    [-4, -5, -6],
                    [-7, -8, -9]]])
  tf.linalg.trace(x)  # [15, -15]
  ```

  Args:
    x: tensor.
    name: A name for the operation (optional).

  Returns:
    The trace of input tensor.
  """
def matmul(a, b, transpose_a: bool = False, transpose_b: bool = False, adjoint_a: bool = False, adjoint_b: bool = False, a_is_sparse: bool = False, b_is_sparse: bool = False, output_type: Incomplete | None = None, name: Incomplete | None = None):
    """Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

  The inputs must, following any transpositions, be tensors of rank >= 2
  where the inner 2 dimensions specify valid matrix multiplication dimensions,
  and any further outer dimensions specify matching batch size.

  Both matrices must be of the same type. The supported types are:
  `bfloat16`, `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, `complex128`.

  Either matrix can be transposed or adjointed (conjugated and transposed) on
  the fly by setting one of the corresponding flag to `True`. These are `False`
  by default.

  If one or both of the matrices contain a lot of zeros, a more efficient
  multiplication algorithm can be used by setting the corresponding
  `a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default.
  This optimization is only available for plain matrices (rank-2 tensors) with
  datatypes `bfloat16` or `float32`.

  A simple 2-D tensor matrix multiplication:

  >>> a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
  >>> a  # 2-D tensor
  <tf.Tensor: shape=(2, 3), dtype=int32, numpy=
  array([[1, 2, 3],
         [4, 5, 6]], dtype=int32)>
  >>> b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
  >>> b  # 2-D tensor
  <tf.Tensor: shape=(3, 2), dtype=int32, numpy=
  array([[ 7,  8],
         [ 9, 10],
         [11, 12]], dtype=int32)>
  >>> c = tf.matmul(a, b)
  >>> c  # `a` * `b`
  <tf.Tensor: shape=(2, 2), dtype=int32, numpy=
  array([[ 58,  64],
         [139, 154]], dtype=int32)>

  A batch matrix multiplication with batch shape [2]:

  >>> a = tf.constant(np.arange(1, 13, dtype=np.int32), shape=[2, 2, 3])
  >>> a  # 3-D tensor
  <tf.Tensor: shape=(2, 2, 3), dtype=int32, numpy=
  array([[[ 1,  2,  3],
          [ 4,  5,  6]],
         [[ 7,  8,  9],
          [10, 11, 12]]], dtype=int32)>
  >>> b = tf.constant(np.arange(13, 25, dtype=np.int32), shape=[2, 3, 2])
  >>> b  # 3-D tensor
  <tf.Tensor: shape=(2, 3, 2), dtype=int32, numpy=
  array([[[13, 14],
          [15, 16],
          [17, 18]],
         [[19, 20],
          [21, 22],
          [23, 24]]], dtype=int32)>
  >>> c = tf.matmul(a, b)
  >>> c  # `a` * `b`
  <tf.Tensor: shape=(2, 2, 2), dtype=int32, numpy=
  array([[[ 94, 100],
          [229, 244]],
         [[508, 532],
          [697, 730]]], dtype=int32)>

  Since python >= 3.5 the @ operator is supported
  (see [PEP 465](https://www.python.org/dev/peps/pep-0465/)). In TensorFlow,
  it simply calls the `tf.matmul()` function, so the following lines are
  equivalent:

  >>> d = a @ b @ [[10], [11]]
  >>> d = tf.matmul(tf.matmul(a, b), [[10], [11]])

  Args:
    a: `tf.Tensor` of type `float16`, `float32`, `float64`, `int32`,
      `complex64`, `complex128` and rank > 1.
    b: `tf.Tensor` with same type and rank as `a`.
    transpose_a: If `True`, `a` is transposed before multiplication.
    transpose_b: If `True`, `b` is transposed before multiplication.
    adjoint_a: If `True`, `a` is conjugated and transposed before
      multiplication.
    adjoint_b: If `True`, `b` is conjugated and transposed before
      multiplication.
    a_is_sparse: If `True`, `a` is treated as a sparse matrix. Notice, this
      **does not support `tf.sparse.SparseTensor`**, it just makes optimizations
      that assume most values in `a` are zero.
      See `tf.sparse.sparse_dense_matmul`
      for some support for `tf.sparse.SparseTensor` multiplication.
    b_is_sparse: If `True`, `b` is treated as a sparse matrix. Notice, this
      **does not support `tf.sparse.SparseTensor`**, it just makes optimizations
      that assume most values in `b` are zero.
      See `tf.sparse.sparse_dense_matmul`
      for some support for `tf.sparse.SparseTensor` multiplication.
    output_type: The output datatype if needed. Defaults to None in which case
      the output_type is the same as input type. Currently only works when input
      tensors are type (u)int8 and output_type can be int32.
    name: Name for the operation (optional).

  Returns:
    A `tf.Tensor` of the same type as `a` and `b` where each inner-most matrix
    is the product of the corresponding matrices in `a` and `b`, e.g. if all
    transpose or adjoint attributes are `False`:

    `output[..., i, j] = sum_k (a[..., i, k] * b[..., k, j])`,
    for all indices `i`, `j`.

    Note: This is matrix product, not element-wise product.


  Raises:
    ValueError: If `transpose_a` and `adjoint_a`, or `transpose_b` and
      `adjoint_b` are both set to `True`.
    TypeError: If output_type is specified but the types of `a`, `b` and
      `output_type` is not (u)int8, (u)int8 and int32.
  """
def matvec(a, b, transpose_a: bool = False, adjoint_a: bool = False, a_is_sparse: bool = False, b_is_sparse: bool = False, name: Incomplete | None = None):
    """Multiplies matrix `a` by vector `b`, producing `a` * `b`.

  The matrix `a` must, following any transpositions, be a tensor of rank >= 2,
  with `shape(a)[-1] == shape(b)[-1]`, and `shape(a)[:-2]` able to broadcast
  with `shape(b)[:-1]`.

  Both `a` and `b` must be of the same type. The supported types are:
  `float16`, `float32`, `float64`, `int32`, `complex64`, `complex128`.

  Matrix `a` can be transposed or adjointed (conjugated and transposed) on
  the fly by setting one of the corresponding flag to `True`. These are `False`
  by default.

  If one or both of the inputs contain a lot of zeros, a more efficient
  multiplication algorithm can be used by setting the corresponding
  `a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default.
  This optimization is only available for plain matrices/vectors (rank-2/1
  tensors) with datatypes `bfloat16` or `float32`.

  For example:

  ```python
  # 2-D tensor `a`
  # [[1, 2, 3],
  #  [4, 5, 6]]
  a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

  # 1-D tensor `b`
  # [7, 9, 11]
  b = tf.constant([7, 9, 11], shape=[3])

  # `a` * `b`
  # [ 58,  64]
  c = tf.linalg.matvec(a, b)


  # 3-D tensor `a`
  # [[[ 1,  2,  3],
  #   [ 4,  5,  6]],
  #  [[ 7,  8,  9],
  #   [10, 11, 12]]]
  a = tf.constant(np.arange(1, 13, dtype=np.int32),
                  shape=[2, 2, 3])

  # 2-D tensor `b`
  # [[13, 14, 15],
  #  [16, 17, 18]]
  b = tf.constant(np.arange(13, 19, dtype=np.int32),
                  shape=[2, 3])

  # `a` * `b`
  # [[ 86, 212],
  #  [410, 563]]
  c = tf.linalg.matvec(a, b)
  ```

  Args:
    a: `Tensor` of type `float16`, `float32`, `float64`, `int32`, `complex64`,
      `complex128` and rank > 1.
    b: `Tensor` with same type as `a` and compatible dimensions.
    transpose_a: If `True`, `a` is transposed before multiplication.
    adjoint_a: If `True`, `a` is conjugated and transposed before
      multiplication.
    a_is_sparse: If `True`, `a` is treated as a sparse matrix.
    b_is_sparse: If `True`, `b` is treated as a sparse matrix.
    name: Name for the operation (optional).

  Returns:
    A `Tensor` of the same type as `a` and `b` where each inner-most vector is
    the product of the corresponding matrices in `a` and vectors in `b`, e.g. if
    all transpose or adjoint attributes are `False`:

    `output`[..., i] = sum_k (`a`[..., i, k] * `b`[..., k]), for all indices i.

    Note: This is matrix-vector product, not element-wise product.


  Raises:
    ValueError: If transpose_a and adjoint_a are both set to True.
  """
def matmul_wrapper(a, b, name: Incomplete | None = None): ...

sparse_matmul: Incomplete

def add(x, y, name: Incomplete | None = None):
    """Returns x + y element-wise.

  Example usages below.

  Add a scalar and a list:

  >>> x = [1, 2, 3, 4, 5]
  >>> y = 1
  >>> tf.add(x, y)
  <tf.Tensor: shape=(5,), dtype=int32, numpy=array([2, 3, 4, 5, 6],
  dtype=int32)>

  Note that binary `+` operator can be used instead:

  >>> x = tf.convert_to_tensor([1, 2, 3, 4, 5])
  >>> y = tf.convert_to_tensor(1)
  >>> x + y
  <tf.Tensor: shape=(5,), dtype=int32, numpy=array([2, 3, 4, 5, 6],
  dtype=int32)>

  Add a tensor and a list of same shape:

  >>> x = [1, 2, 3, 4, 5]
  >>> y = tf.constant([1, 2, 3, 4, 5])
  >>> tf.add(x, y)
  <tf.Tensor: shape=(5,), dtype=int32,
  numpy=array([ 2,  4,  6,  8, 10], dtype=int32)>

  **Warning**: If one of the inputs (`x` or `y`) is a tensor and the other is a
  non-tensor, the non-tensor input will adopt (or get casted to) the data type
  of the tensor input. This can potentially cause unwanted overflow or underflow
  conversion.

  For example,

  >>> x = tf.constant([1, 2], dtype=tf.int8)
  >>> y = [2**7 + 1, 2**7 + 2]
  >>> tf.add(x, y)
  <tf.Tensor: shape=(2,), dtype=int8, numpy=array([-126, -124], dtype=int8)>

  When adding two input values of different shapes, `Add` follows NumPy
  broadcasting rules. The two input array shapes are compared element-wise.
  Starting with the trailing dimensions, the two dimensions either have to be
  equal or one of them needs to be `1`.

  For example,

  >>> x = np.ones(6).reshape(1, 2, 1, 3)
  >>> y = np.ones(6).reshape(2, 1, 3, 1)
  >>> tf.add(x, y).shape.as_list()
  [2, 2, 3, 3]

  Another example with two arrays of different dimension.

  >>> x = np.ones([1, 2, 1, 4])
  >>> y = np.ones([3, 4])
  >>> tf.add(x, y).shape.as_list()
  [1, 2, 3, 4]

  The reduction version of this elementwise operation is `tf.math.reduce_sum`

  Args:
    x: A `tf.Tensor`. Must be one of the following types: bfloat16, half,
      float16, float32, float64, uint8, uint16, uint32, uint64, int8, int16,
      int32, int64, complex64, complex128, string.
    y: A `tf.Tensor`. Must have the same type as x.
    name: A name for the operation (optional)
  """
def add_n(inputs, name: Incomplete | None = None):
    """Returns the element-wise sum of a list of tensors.

  All inputs in the list must have the same shape. This op does not
  [broadcast](https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)
  its inputs. If you need broadcasting, use `tf.math.add` (or the `+` operator)
  instead.

  For example:

  >>> a = tf.constant([[3, 5], [4, 8]])
  >>> b = tf.constant([[1, 6], [2, 9]])
  >>> tf.math.add_n([a, b, a]).numpy()
  array([[ 7, 16],
         [10, 25]], dtype=int32)

  See Also:

  * `tf.reduce_sum(inputs, axis=0)` - This performs the same mathematical
    operation, but `tf.add_n` may be more efficient because it sums the
    tensors directly. `reduce_sum` on the other hand calls
    `tf.convert_to_tensor` on the list of tensors, unnecessarily stacking them
    into a single tensor before summing.

  Args:
    inputs: A list of `tf.Tensor` or `tf.IndexedSlices` objects, each with the
      same shape and type. `tf.IndexedSlices` objects will be converted into
      dense tensors prior to adding.
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of the same shape and type as the elements of `inputs`.

  Raises:
    ValueError: If `inputs` don't all have same shape and dtype or the shape
    cannot be inferred.
  """
def accumulate_n(inputs, shape: Incomplete | None = None, tensor_dtype: Incomplete | None = None, name: Incomplete | None = None):
    '''Returns the element-wise sum of a list of tensors.

  Optionally, pass `shape` and `tensor_dtype` for shape and type checking,
  otherwise, these are inferred.

  For example:

  >>> a = tf.constant([[1, 2], [3, 4]])
  >>> b = tf.constant([[5, 0], [0, 6]])
  >>> tf.math.accumulate_n([a, b, a]).numpy()
  array([[ 7, 4],
         [ 6, 14]], dtype=int32)

  >>> # Explicitly pass shape and type
  >>> tf.math.accumulate_n(
  ...     [a, b, a], shape=[2, 2], tensor_dtype=tf.int32).numpy()
  array([[ 7,  4],
         [ 6, 14]], dtype=int32)

  Note: The input must be a list or tuple. This function does not handle
  `IndexedSlices`

  See Also:

  * `tf.reduce_sum(inputs, axis=0)` - This performe the same mathematical
    operation, but `tf.add_n` may be more efficient because it sums the
    tensors directly. `reduce_sum` on the other hand calls
    `tf.convert_to_tensor` on the list of tensors, unncessairly stacking them
    into a single tensor before summing.
  * `tf.add_n` - This is another python wrapper for the same Op. It has
    nearly identical functionality.

  Args:
    inputs: A list of `Tensor` objects, each with same shape and type.
    shape: Expected shape of elements of `inputs` (optional). Also controls the
      output shape of this op, which may affect type inference in other ops. A
      value of `None` means "infer the input shape from the shapes in `inputs`".
    tensor_dtype: Expected data type of `inputs` (optional). A value of `None`
      means "infer the input dtype from `inputs[0]`".
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of same shape and type as the elements of `inputs`.

  Raises:
    ValueError: If `inputs` don\'t all have same shape and dtype or the shape
    cannot be inferred.
  '''
def sigmoid(x, name: Incomplete | None = None):
    """Computes sigmoid of `x` element-wise.

  Formula for calculating $\\mathrm{sigmoid}(x) = y = 1 / (1 + \\exp(-x))$.

  For $x \\in (-\\infty, \\infty)$, $\\mathrm{sigmoid}(x) \\in (0, 1)$.

  Example Usage:

  If a positive number is large, then its sigmoid will approach to 1 since the
  formula will be `y = <large_num> / (1 + <large_num>)`

  >>> x = tf.constant([0.0, 1.0, 50.0, 100.0])
  >>> tf.math.sigmoid(x)
  <tf.Tensor: shape=(4,), dtype=float32,
  numpy=array([0.5, 0.7310586, 1.0, 1.0], dtype=float32)>

  If a negative number is large, its sigmoid will approach to 0 since the
  formula will be `y = 1 / (1 + <large_num>)`

  >>> x = tf.constant([-100.0, -50.0, -1.0, 0.0])
  >>> tf.math.sigmoid(x)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=
  array([0.0000000e+00, 1.9287499e-22, 2.6894143e-01, 0.5],
        dtype=float32)>

  Args:
    x: A Tensor with type `float16`, `float32`, `float64`, `complex64`, or
      `complex128`.
    name: A name for the operation (optional).

  Returns:
    A Tensor with the same type as `x`.

  Usage Example:

  >>> x = tf.constant([-128.0, 0.0, 128.0], dtype=tf.float32)
  >>> tf.sigmoid(x)
  <tf.Tensor: shape=(3,), dtype=float32,
  numpy=array([0. , 0.5, 1. ], dtype=float32)>

  @compatibility(scipy)
  Equivalent to scipy.special.expit
  @end_compatibility
  """
def log_sigmoid(x, name: Incomplete | None = None):
    """Computes log sigmoid of `x` element-wise.

  Specifically, `y = log(1 / (1 + exp(-x)))`.  For numerical stability,
  we use `y = -tf.nn.softplus(-x)`.

  Args:
    x: A Tensor with type `float32` or `float64`.
    name: A name for the operation (optional).

  Returns:
    A Tensor with the same type as `x`.

  Usage Example:

  If a positive number is large, then its log_sigmoid will approach to 0 since
  the formula will be `y = log( <large_num> / (1 + <large_num>) )` which
  approximates to `log (1)` which is 0.

  >>> x = tf.constant([0.0, 1.0, 50.0, 100.0])
  >>> tf.math.log_sigmoid(x)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=
  array([-6.9314718e-01, -3.1326169e-01, -1.9287499e-22, -0.0000000e+00],
        dtype=float32)>

  If a negative number is large, its log_sigmoid will approach to the number
  itself since the formula will be `y = log( 1 / (1 + <large_num>) )` which is
  `log (1) - log ( (1 + <large_num>) )` which approximates to `- <large_num>`
  that is the number itself.

  >>> x = tf.constant([-100.0, -50.0, -1.0, 0.0])
  >>> tf.math.log_sigmoid(x)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=
  array([-100.       ,  -50.       ,   -1.3132616,   -0.6931472],
        dtype=float32)>
  """
def cumsum(x, axis: int = 0, exclusive: bool = False, reverse: bool = False, name: Incomplete | None = None):
    """Compute the cumulative sum of the tensor `x` along `axis`.

  By default, this op performs an inclusive cumsum, which means that the first
  element of the input is identical to the first element of the output:
  For example:

  >>> # tf.cumsum([a, b, c])   # [a, a + b, a + b + c]
  >>> x = tf.constant([2, 4, 6, 8])
  >>> tf.cumsum(x)
  <tf.Tensor: shape=(4,), dtype=int32,
  numpy=array([ 2,  6, 12, 20], dtype=int32)>

  >>> # using varying `axis` values
  >>> y = tf.constant([[2, 4, 6, 8], [1,3,5,7]])
  >>> tf.cumsum(y, axis=0)
  <tf.Tensor: shape=(2, 4), dtype=int32, numpy=
  array([[ 2,  4,  6,  8],
         [ 3,  7, 11, 15]], dtype=int32)>
  >>> tf.cumsum(y, axis=1)
  <tf.Tensor: shape=(2, 4), dtype=int32, numpy=
  array([[ 2,  6, 12, 20],
         [ 1,  4,  9, 16]], dtype=int32)>

  By setting the `exclusive` kwarg to `True`, an exclusive cumsum is performed
  instead:

  >>> # tf.cumsum([a, b, c], exclusive=True)  => [0, a, a + b]
  >>> x = tf.constant([2, 4, 6, 8])
  >>> tf.cumsum(x, exclusive=True)
  <tf.Tensor: shape=(4,), dtype=int32,
  numpy=array([ 0,  2,  6, 12], dtype=int32)>

  By setting the `reverse` kwarg to `True`, the cumsum is performed in the
  opposite direction:

  >>> # tf.cumsum([a, b, c], reverse=True)  # [a + b + c, b + c, c]
  >>> x = tf.constant([2, 4, 6, 8])
  >>> tf.cumsum(x, reverse=True)
  <tf.Tensor: shape=(4,), dtype=int32,
  numpy=array([20, 18, 14,  8], dtype=int32)>

  This is more efficient than using separate `tf.reverse` ops.
  The `reverse` and `exclusive` kwargs can also be combined:

  >>> # tf.cumsum([a, b, c], exclusive=True, reverse=True)  # [b + c, c, 0]
  >>> x = tf.constant([2, 4, 6, 8])
  >>> tf.cumsum(x, exclusive=True, reverse=True)
  <tf.Tensor: shape=(4,), dtype=int32,
  numpy=array([18, 14,  8,  0], dtype=int32)>

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`,
      `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
      `complex128`, `qint8`, `quint8`, `qint32`, `half`.
    axis: A `Tensor` of type `int32` (default: 0). Must be in the range
      `[-rank(x), rank(x))`.
    exclusive: If `True`, perform exclusive cumsum.
    reverse: A `bool` (default: False).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """
def cumprod(x, axis: int = 0, exclusive: bool = False, reverse: bool = False, name: Incomplete | None = None):
    """Compute the cumulative product of the tensor `x` along `axis`.

  By default, this op performs an inclusive cumprod, which means that the
  first element of the input is identical to the first element of the output:

  ```python
  tf.math.cumprod([a, b, c])  # [a, a * b, a * b * c]
  ```

  By setting the `exclusive` kwarg to `True`, an exclusive cumprod is
  performed
  instead:

  ```python
  tf.math.cumprod([a, b, c], exclusive=True)  # [1, a, a * b]
  ```

  By setting the `reverse` kwarg to `True`, the cumprod is performed in the
  opposite direction:

  ```python
  tf.math.cumprod([a, b, c], reverse=True)  # [a * b * c, b * c, c]
  ```

  This is more efficient than using separate `tf.reverse` ops.
  The `reverse` and `exclusive` kwargs can also be combined:

  ```python
  tf.math.cumprod([a, b, c], exclusive=True, reverse=True)  # [b * c, c, 1]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`,
      `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
      `complex128`, `qint8`, `quint8`, `qint32`, `half`.
    axis: A `Tensor` of type `int32` (default: 0). Must be in the range
      `[-rank(x), rank(x))`.
    exclusive: If `True`, perform exclusive cumprod.
    reverse: A `bool` (default: False).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """
def cumulative_logsumexp(x, axis: int = 0, exclusive: bool = False, reverse: bool = False, name: Incomplete | None = None):
    '''Compute the cumulative log-sum-exp of the tensor `x` along `axis`.

  By default, this op performs an inclusive cumulative log-sum-exp, which means
  that the first element of the input is identical to the first element of
  the output.

  This operation is significantly more numerically stable than the equivalent
  tensorflow operation `tf.math.log(tf.math.cumsum(tf.math.exp(x)))`, although
  computes the same result given infinite numerical precision. However, note
  that in some cases, it may be less stable than `tf.math.reduce_logsumexp`
  for a given element, as it applies the "log-sum-exp trick" in a different
  way.

  More precisely, where `tf.math.reduce_logsumexp` uses the following trick:

  ```
  log(sum(exp(x))) == log(sum(exp(x - max(x)))) + max(x)
  ```

  it cannot be directly used here as there is no fast way of applying it
  to each prefix `x[:i]`. Instead, this function implements a prefix
  scan using pairwise log-add-exp, which is a commutative and associative
  (up to floating point precision) operator:

  ```
  log_add_exp(x, y) = log(exp(x) + exp(y))
                    = log(1 + exp(min(x, y) - max(x, y))) + max(x, y)
  ```

  However, reducing using the above operator leads to a different computation
  tree (logs are taken repeatedly instead of only at the end), and the maximum
  is only computed pairwise instead of over the entire prefix. In general, this
  leads to a different and slightly less precise computation.

  Args:
    x: A `Tensor`. Must be one of the following types: `float16`, `float32`,
      `float64`.
    axis: A `Tensor` of type `int32` or `int64` (default: 0). Must be in the
      range `[-rank(x), rank(x))`.
    exclusive: If `True`, perform exclusive cumulative log-sum-exp.
    reverse: If `True`, performs the cumulative log-sum-exp in the reverse
      direction.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same shape and type as `x`.
  '''
def conj(x, name: Incomplete | None = None):
    """Returns the complex conjugate of a complex number.

  Given a tensor `x` of complex numbers, this operation returns a tensor of
  complex numbers that are the complex conjugate of each element in `x`. The
  complex numbers in `x` must be of the form \\\\(a + bj\\\\), where `a` is the
  real part and `b` is the imaginary part.

  The complex conjugate returned by this operation is of the form \\\\(a - bj\\\\).

  For example:

  >>> x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
  >>> tf.math.conj(x)
  <tf.Tensor: shape=(2,), dtype=complex128,
  numpy=array([-2.25-4.75j,  3.25-5.75j])>

  If `x` is real, it is returned unchanged.

  For example:

  >>> x = tf.constant([-2.25, 3.25])
  >>> tf.math.conj(x)
  <tf.Tensor: shape=(2,), dtype=float32,
  numpy=array([-2.25,  3.25], dtype=float32)>

  Args:
    x: `Tensor` to conjugate.  Must have numeric or variant type.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` that is the conjugate of `x` (with the same type).

  Raises:
    TypeError: If `x` is not a numeric tensor.

  @compatibility(numpy)
  Equivalent to numpy.conj.
  @end_compatibility
  """
def reduced_shape(input_shape, axes):
    """Helper function for reduction ops.

  Args:
    input_shape: 1-D Tensor, the shape of the Tensor being reduced.
    axes: 1-D Tensor, the reduction axes.

  Returns:
    A 1-D Tensor, the output shape as if keepdims were set to True.
  """
def unsorted_segment_mean(data, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the mean along segments of a tensor.

  Read [the section on
  segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
  for an explanation of segments.

  This operator is similar to the `tf.math.unsorted_segment_sum` operator.
  Instead of computing the sum over segments, it computes the mean of all
  entries belonging to a segment such that:

  \\\\(output_i = 1/N_i \\sum_{j...} data[j...]\\\\) where the sum is over tuples
  `j...` such that `segment_ids[j...] == i` with \\\\N_i\\\\ being the number of
  occurrences of id \\\\i\\\\.

  If there is no entry for a given segment ID `i`, it outputs 0.

  If the given segment ID `i` is negative, the value is dropped and will not
  be added to the sum of the segment.

  Caution: On CPU, values in `segment_ids` are always validated to be less than
  `num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
  does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
  result in safe but unspecified behavior, which may include ignoring
  out-of-bound indices or outputting a tensor with a 0 stored in the first
  dimension of its shape if `num_segments` is 0.

  Args:
    data: A `Tensor` with floating point or complex dtype.
    segment_ids: An integer tensor whose shape is a prefix of `data.shape`.
      The values must be less than `num_segments`.
      The values are always validated to be in range on CPU,
      never validated on GPU.
    num_segments: An integer scalar `Tensor`.  The number of distinct segment
      IDs.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`.  Has same shape as data, except for the first `segment_ids.rank`
    dimensions, which are replaced with a single dimension which has size
   `num_segments`.
  """
def unsorted_segment_sqrt_n(data, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the sum along segments of a tensor divided by the sqrt(N).

  Read [the section on
  segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
  for an explanation of segments.

  This operator is similar to the `tf.math.unsorted_segment_sum` operator.
  Additionally to computing the sum over segments, it divides the results by
  sqrt(N).

  \\\\(output_i = 1/sqrt(N_i) \\sum_{j...} data[j...]\\\\) where the sum is over
  tuples `j...` such that `segment_ids[j...] == i` with \\\\N_i\\\\ being the
  number of occurrences of id \\\\i\\\\.

  If there is no entry for a given segment ID `i`, it outputs 0.

  Note that this op only supports floating point and complex dtypes,
  due to tf.sqrt only supporting these types.

  If the given segment ID `i` is negative, the value is dropped and will not
  be added to the sum of the segment.

  Caution: On CPU, values in `segment_ids` are always validated to be less than
  `num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
  does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
  result in safe but unspecified behavior, which may include ignoring
  out-of-bound indices or outputting a tensor with a 0 stored in the first
  dimension of its shape if `num_segments` is 0.

  Args:
    data: A `Tensor` with floating point or complex dtype.
    segment_ids: An integer tensor whose shape is a prefix of `data.shape`.
      The values must be in the range `[0, num_segments)`.
      The values are always validated to be in range on CPU,
      never validated on GPU.
    num_segments: An integer scalar `Tensor`.  The number of distinct segment
      IDs.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`.  Has same shape as data, except for the first `segment_ids.rank`
    dimensions, which are replaced with a single dimension which has size
   `num_segments`.
  """
def sparse_segment_sum(data, indices, segment_ids, name: Incomplete | None = None, num_segments: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor.

  Read [the section on
  segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
  for an explanation of segments.

  Like `tf.math.segment_sum`, but `segment_ids` can have rank less than `data`'s
  first dimension, selecting a subset of dimension 0, specified by `indices`.
  `segment_ids` is allowed to have missing ids, in which case the output will
  be zeros at those indices. In those cases `num_segments` is used to determine
  the size of the output.

  For example:

  ```python
  c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])

  # Select two rows, one segment.
  tf.sparse.segment_sum(c, tf.constant([0, 1]), tf.constant([0, 0]))
  # => [[0 0 0 0]]

  # Select two rows, two segment.
  tf.sparse.segment_sum(c, tf.constant([0, 1]), tf.constant([0, 1]))
  # => [[ 1  2  3  4]
  #     [-1 -2 -3 -4]]

  # With missing segment ids.
  tf.sparse.segment_sum(c, tf.constant([0, 1]), tf.constant([0, 2]),
                        num_segments=4)
  # => [[ 1  2  3  4]
  #     [ 0  0  0  0]
  #     [-1 -2 -3 -4]
  #     [ 0  0  0  0]]

  # Select all rows, two segments.
  tf.sparse.segment_sum(c, tf.constant([0, 1, 2]), tf.constant([0, 0, 1]))
  # => [[0 0 0 0]
  #     [5 6 7 8]]

  # Which is equivalent to:
  tf.math.segment_sum(c, tf.constant([0, 0, 1]))
  ```

  Args:
    data: A `Tensor` with data that will be assembled in the output.
    indices: A 1-D `Tensor` with indices into `data`. Has same rank as
      `segment_ids`.
    segment_ids: A 1-D `Tensor` with indices into the output `Tensor`. Values
      should be sorted and can be repeated.
    name: A name for the operation (optional).
    num_segments: An optional int32 scalar. Indicates the size of the output
      `Tensor`.

  Returns:
    A `tensor` of the shape as data, except for dimension 0 which
    has size `k`, the number of segments specified via `num_segments` or
    inferred for the last element in `segments_ids`.
  """
def sparse_segment_sum_v2(data, indices, segment_ids, num_segments: Incomplete | None = None, name: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor.

  Read [the section on
  segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
  for an explanation of segments.

  Like `tf.math.segment_sum`, but `segment_ids` can have rank less than `data`'s
  first dimension, selecting a subset of dimension 0, specified by `indices`.
  `segment_ids` is allowed to have missing ids, in which case the output will
  be zeros at those indices. In those cases `num_segments` is used to determine
  the size of the output.

  For example:

  ```python
  c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])

  # Select two rows, one segment.
  tf.sparse.segment_sum(c, tf.constant([0, 1]), tf.constant([0, 0]))
  # => [[0 0 0 0]]

  # Select two rows, two segment.
  tf.sparse.segment_sum(c, tf.constant([0, 1]), tf.constant([0, 1]))
  # => [[ 1  2  3  4]
  #     [-1 -2 -3 -4]]

  # With missing segment ids.
  tf.sparse.segment_sum(c, tf.constant([0, 1]), tf.constant([0, 2]),
                        num_segments=4)
  # => [[ 1  2  3  4]
  #     [ 0  0  0  0]
  #     [-1 -2 -3 -4]
  #     [ 0  0  0  0]]

  # Select all rows, two segments.
  tf.sparse.segment_sum(c, tf.constant([0, 1, 2]), tf.constant([0, 0, 1]))
  # => [[0 0 0 0]
  #     [5 6 7 8]]

  # Which is equivalent to:
  tf.math.segment_sum(c, tf.constant([0, 0, 1]))
  ```

  Args:
    data: A `Tensor` with data that will be assembled in the output.
    indices: A 1-D `Tensor` with indices into `data`. Has same rank as
      `segment_ids`.
    segment_ids: A 1-D `Tensor` with indices into the output `Tensor`. Values
      should be sorted and can be repeated.
    num_segments: An optional int32 scalar. Indicates the size of the output
      `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `tensor` of the shape as data, except for dimension 0 which
    has size `k`, the number of segments specified via `num_segments` or
    inferred for the last element in `segments_ids`.
  """
def sparse_segment_mean(data, indices, segment_ids, name: Incomplete | None = None, num_segments: Incomplete | None = None):
    """Computes the mean along sparse segments of a tensor.

  Read [the section on
  segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
  for an explanation of segments.

  Like `tf.math.segment_mean`, but `segment_ids` can have rank less than
  `data`'s first dimension, selecting a subset of dimension 0, specified by
  `indices`.
  `segment_ids` is allowed to have missing ids, in which case the output will
  be zeros at those indices. In those cases `num_segments` is used to determine
  the size of the output.

  Args:
    data: A `Tensor` with data that will be assembled in the output.
    indices: A 1-D `Tensor` with indices into `data`. Has same rank as
      `segment_ids`.
    segment_ids: A 1-D `Tensor` with indices into the output `Tensor`. Values
      should be sorted and can be repeated.
    name: A name for the operation (optional).
    num_segments: An optional int32 scalar. Indicates the size of the output
      `Tensor`.

  Returns:
    A `tensor` of the shape as data, except for dimension 0 which
    has size `k`, the number of segments specified via `num_segments` or
    inferred for the last element in `segments_ids`.
  """
def sparse_segment_mean_v2(data, indices, segment_ids, num_segments: Incomplete | None = None, name: Incomplete | None = None):
    """Computes the mean along sparse segments of a tensor.

  Read [the section on
  segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
  for an explanation of segments.

  Like `tf.math.segment_mean`, but `segment_ids` can have rank less than
  `data`'s first dimension, selecting a subset of dimension 0, specified by
  `indices`.
  `segment_ids` is allowed to have missing ids, in which case the output will
  be zeros at those indices. In those cases `num_segments` is used to determine
  the size of the output.

  Args:
    data: A `Tensor` with data that will be assembled in the output.
    indices: A 1-D `Tensor` with indices into `data`. Has same rank as
      `segment_ids`.
    segment_ids: A 1-D `Tensor` with indices into the output `Tensor`. Values
      should be sorted and can be repeated.
    num_segments: An optional int32 scalar. Indicates the size of the output
      `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `tensor` of the shape as data, except for dimension 0 which
    has size `k`, the number of segments specified via `num_segments` or
    inferred for the last element in `segments_ids`.
  """
def sparse_segment_sqrt_n(data, indices, segment_ids, name: Incomplete | None = None, num_segments: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor divided by the sqrt(N).

  `N` is the size of the segment being reduced.

  Args:
    data: A `Tensor` with data that will be assembled in the output.
    indices: A 1-D `Tensor` with indices into `data`. Has same rank as
      `segment_ids`.
    segment_ids: A 1-D `Tensor` with indices into the output `Tensor`. Values
      should be sorted and can be repeated.
    name: A name for the operation (optional).
    num_segments: An optional int32 scalar. Indicates the size of the output
      `Tensor`.

  Returns:
    A `tensor` of the shape as data, except for dimension 0 which
    has size `k`, the number of segments specified via `num_segments` or
    inferred for the last element in `segments_ids`.
  """
def sparse_segment_sqrt_n_v2(data, indices, segment_ids, num_segments: Incomplete | None = None, name: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor divided by the sqrt(N).

  Read [the section on
  segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
  for an explanation of segments.

  Like `tf.sparse.segment_mean`, but instead of dividing by the size of the
  segment, `N`, divide by `sqrt(N)` instead.

  Args:
    data: A `Tensor` with data that will be assembled in the output.
    indices: A 1-D `Tensor` with indices into `data`. Has same rank as
      `segment_ids`.
    segment_ids: A 1-D `Tensor` with indices into the output `Tensor`. Values
      should be sorted and can be repeated.
    num_segments: An optional int32 scalar. Indicates the size of the output
      `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `tensor` of the shape as data, except for dimension 0 which
    has size `k`, the number of segments specified via `num_segments` or
    inferred for the last element in `segments_ids`.
  """
def tensordot(a, b, axes, name: Incomplete | None = None):
    """Tensor contraction of a and b along specified axes and outer product.

  Tensordot (also known as tensor contraction) sums the product of elements
  from `a` and `b` over the indices specified by `axes`.

  This operation corresponds to `numpy.tensordot(a, b, axes)`.

  Example 1: When `a` and `b` are matrices (order 2), the case `axes=1`
  is equivalent to matrix multiplication.

  Example 2: When `a` and `b` are matrices (order 2), the case
  `axes = [[1], [0]]` is equivalent to matrix multiplication.

  Example 3: When `a` and `b` are matrices (order 2), the case `axes=0` gives
  the outer product, a tensor of order 4.

  Example 4: Suppose that \\\\(a_{ijk}\\\\) and \\\\(b_{lmn}\\\\) represent two
  tensors of order 3. Then, `contract(a, b, [[0], [2]])` is the order 4 tensor
  \\\\(c_{jklm}\\\\) whose entry
  corresponding to the indices \\\\((j,k,l,m)\\\\) is given by:

  \\\\( c_{jklm} = \\sum_i a_{ijk} b_{lmi} \\\\).

  In general, `order(c) = order(a) + order(b) - 2*len(axes[0])`.

  Args:
    a: `Tensor` of type `float32` or `float64`.
    b: `Tensor` with the same type as `a`.
    axes: Either a scalar `N`, or a list or an `int32` `Tensor` of shape [2, k].
      If axes is a scalar, sum over the last N axes of a and the first N axes of
      b in order. If axes is a list or `Tensor` the first and second row contain
      the set of unique integers specifying axes along which the contraction is
      computed, for `a` and `b`, respectively. The number of axes for `a` and
      `b` must be equal. If `axes=0`, computes the outer product between `a` and
      `b`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` with the same type as `a`.

  Raises:
    ValueError: If the shapes of `a`, `b`, and `axes` are incompatible.
    IndexError: If the values in axes exceed the rank of the corresponding
      tensor.
  """
def polyval(coeffs, x, name: Incomplete | None = None):
    """Computes the elementwise value of a polynomial.

  If `x` is a tensor and `coeffs` is a list n + 1 tensors,
  this function returns the value of the n-th order polynomial

  `p(x) = coeffs[n-1] + coeffs[n-2] * x + ...  + coeffs[0] * x**(n-1)`

  evaluated using Horner's method, i.e.

  ```python
  p(x) = coeffs[n-1] + x * (coeffs[n-2] + ... + x * (coeffs[1] + x * coeffs[0]))
  ```

  Usage Example:

  >>> coefficients = [1.0, 2.5, -4.2]
  >>> x = 5.0
  >>> y = tf.math.polyval(coefficients, x)
  >>> y
  <tf.Tensor: shape=(), dtype=float32, numpy=33.3>

  Usage Example:

  >>> tf.math.polyval([2, 1, 0], 3) # evaluates 2 * (3**2) + 1 * (3**1) + 0 * (3**0)
  <tf.Tensor: shape=(), dtype=int32, numpy=21>

  `tf.math.polyval` can also be used in polynomial regression. Taking
  advantage of this function can facilitate writing a polynomial equation
  as compared to explicitly writing it out, especially for higher degree
  polynomials.

  >>> x = tf.constant(3)
  >>> theta1 = tf.Variable(2)
  >>> theta2 = tf.Variable(1)
  >>> theta3 = tf.Variable(0)
  >>> tf.math.polyval([theta1, theta2, theta3], x)
  <tf.Tensor: shape=(), dtype=int32, numpy=21>

  Args:
    coeffs: A list of `Tensor` representing the coefficients of the polynomial.
    x: A `Tensor` representing the variable of the polynomial.
    name: A name for the operation (optional).

  Returns:
    A `tensor` of the shape as the expression p(x) with usual broadcasting
    rules for element-wise addition and multiplication applied.

  @compatibility(numpy)
  Equivalent to numpy.polyval.
  @end_compatibility
  """
def reciprocal_no_nan(x, name: Incomplete | None = None):
    """Performs a safe reciprocal operation, element wise.

  If a particular element is zero, the reciprocal for that element is
  also set to zero.

  For example:
  ```python
  x = tf.constant([2.0, 0.5, 0, 1], dtype=tf.float32)
  tf.math.reciprocal_no_nan(x)  # [ 0.5, 2, 0.0, 1.0 ]
  ```

  Args:
    x: A `Tensor` of type `float16`, `float32`, `float64` `complex64` or
      `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of same shape and type as `x`.

  Raises:
    TypeError: x must be of a valid dtype.

  """
def xdivy(x, y, name: Incomplete | None = None):
    """Computes `x / y`.

  Given `x` and `y`, computes `x / y`. This function safely returns
  zero when `x = 0`, no matter what the value of `y` is.

  Example:

  >>> tf.math.xdivy(1., 2.)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.5>
  >>> tf.math.xdivy(0., 1.)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.0>
  >>> tf.math.xdivy(0., 0.)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.0>
  >>> tf.math.xdivy(1., 0.)
  <tf.Tensor: shape=(), dtype=float32, numpy=inf>

  Args:
    x: A `tf.Tensor` of type `half`, `float32`, `float64`, `complex64`,
      `complex128`
    y: A `tf.Tensor` of type `half`, `float32`, `float64`, `complex64`,
      `complex128`
    name: A name for the operation (optional).

  Returns:
    `x / y`.
  """
def xlog1py(x, y, name: Incomplete | None = None):
    """Compute x * log1p(y).

  Given `x` and `y`, compute `x * log1p(y)`. This function safely returns
  zero when `x = 0`, no matter what the value of `y` is.

  Example:

  >>> tf.math.xlog1py(0., 1.)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.>
  >>> tf.math.xlog1py(1., 1.)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.6931472>
  >>> tf.math.xlog1py(2., 2.)
  <tf.Tensor: shape=(), dtype=float32, numpy=2.1972246>
  >>> tf.math.xlog1py(0., -1.)
  <tf.Tensor: shape=(), dtype=float32, numpy=0.>

  Args:
    x: A `tf.Tensor` of type `half`, `float32`, `float64`, `complex64`,
      `complex128`
    y: A `tf.Tensor` of type `half`, `float32`, `float64`, `complex64`,
      `complex128`
    name: A name for the operation (optional).

  Returns:
    `x * log1p(y)`.

  @compatibility(scipy)
  Equivalent to scipy.special.xlog1py
  @end_compatibility
  """
def erfinv(x, name: Incomplete | None = None):
    """Compute inverse error function.

  Given `x`, compute the inverse error function of `x`. This function
  is the inverse of `tf.math.erf`.

  Args:
    x: `Tensor` with type `float` or `double`.
    name: A name for the operation (optional).
  Returns:
    Inverse error function of `x`.
  """
def ndtri(x, name: Incomplete | None = None):
    """Compute quantile of Standard Normal.

  Args:
    x: `Tensor` with type `float` or `double`.
    name: A name for the operation (optional).
  Returns:
    Inverse error function of `x`.
  """
def erfcinv(x, name: Incomplete | None = None):
    """Computes the inverse of complementary error function.

  Given `x`, compute the inverse complementary error function of `x`.
  This function is the inverse of `tf.math.erfc`, and is defined on
  `[0, 2]`.

  >>> tf.math.erfcinv([0., 0.2, 1., 1.5, 2.])
  <tf.Tensor: shape=(5,), dtype=float32, numpy=
  array([       inf,  0.9061935, -0.       , -0.4769363,       -inf],
        dtype=float32)>

  Args:
    x: `Tensor` with type `float` or `double`.
    name: A name for the operation (optional).
  Returns:
    Inverse complementary error function of `x`.

  @compatibility(numpy)
  Equivalent to scipy.special.erfcinv
  @end_compatibility
  """
def ceil(x, name: Incomplete | None = None):
    """Return the ceiling of the input, element-wise.

  For example:

  >>> tf.math.ceil([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
  <tf.Tensor: shape=(7,), dtype=float32,
  numpy=array([-1., -1., -0.,  1.,  2.,  2.,  2.], dtype=float32)>

  Args:
    x: A `tf.Tensor`. Must be one of the following types: `bfloat16`, `half`,
      `float32`, `float64`. `int32`
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor`. Has the same type as `x`.

  @compatibility(numpy)
  Equivalent to np.ceil
  @end_compatibility
  """
def sqrt(x, name: Incomplete | None = None):
    """Computes element-wise square root of the input tensor.

  Note: This operation does not support integer types.

  >>> x = tf.constant([[4.0], [16.0]])
  >>> tf.sqrt(x)
  <tf.Tensor: shape=(2, 1), dtype=float32, numpy=
    array([[2.],
           [4.]], dtype=float32)>
  >>> y = tf.constant([[-4.0], [16.0]])
  >>> tf.sqrt(y)
  <tf.Tensor: shape=(2, 1), dtype=float32, numpy=
    array([[nan],
           [ 4.]], dtype=float32)>
  >>> z = tf.constant([[-1.0], [16.0]], dtype=tf.complex128)
  >>> tf.sqrt(z)
  <tf.Tensor: shape=(2, 1), dtype=complex128, numpy=
    array([[0.0+1.j],
           [4.0+0.j]])>

  Note: In order to support complex type, please provide an input tensor
  of `complex64` or `complex128`.

  Args:
    x: A `tf.Tensor` of type `bfloat16`, `half`, `float32`, `float64`,
      `complex64`, `complex128`
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of same size, type and sparsity as `x`.
  """
def exp(x, name: Incomplete | None = None):
    """Computes exponential of x element-wise.  \\\\(y = e^x\\\\).

  This function computes the exponential of the input tensor element-wise.
  i.e. `math.exp(x)` or \\\\(e^x\\\\), where `x` is the input tensor.
  \\\\(e\\\\) denotes Euler's number and is approximately equal to 2.718281.
  Output is positive for any real input.

  >>> x = tf.constant(2.0)
  >>> tf.math.exp(x)
  <tf.Tensor: shape=(), dtype=float32, numpy=7.389056>

  >>> x = tf.constant([2.0, 8.0])
  >>> tf.math.exp(x)
  <tf.Tensor: shape=(2,), dtype=float32,
  numpy=array([   7.389056, 2980.958   ], dtype=float32)>

  For complex numbers, the exponential value is calculated as
  $$
  e^{x+iy} = {e^x} {e^{iy}} = {e^x} ({\\cos (y) + i \\sin (y)})
  $$

  For `1+1j` the value would be computed as:
  $$
  e^1 (\\cos (1) + i \\sin (1)) = 2.7182817 \\times (0.5403023+0.84147096j)
  $$

  >>> x = tf.constant(1 + 1j)
  >>> tf.math.exp(x)
  <tf.Tensor: shape=(), dtype=complex128,
  numpy=(1.4686939399158851+2.2873552871788423j)>

  Args:
    x: A `tf.Tensor`. Must be one of the following types: `bfloat16`, `half`,
      `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor`. Has the same type as `x`.

  @compatibility(numpy)
  Equivalent to np.exp
  @end_compatibility
  """
def sobol_sample(dim, num_results, skip: int = 0, dtype=..., name: Incomplete | None = None):
    """Generates points from the Sobol sequence.

  Creates a Sobol sequence with `num_results` samples. Each sample has dimension
  `dim`. Skips the first `skip` samples.

  Args:
    dim: Positive scalar `Tensor` representing each sample's dimension.
    num_results: Positive scalar `Tensor` of dtype int32. The number of Sobol
        points to return in the output.
    skip: (Optional) Positive scalar `Tensor` of dtype int32. The number of
        initial points of the Sobol sequence to skip. Default value is 0.
    dtype: (Optional) The `tf.Dtype` of the sample. One of: `tf.float32` or
        `tf.float64`. Defaults to `tf.float32`.
    name: (Optional) Python `str` name prefixed to ops created by this function.

  Returns:
    `Tensor` of samples from Sobol sequence with `shape` [num_results, dim].
  """
def rsqrt(x, name: Incomplete | None = None):
    """Computes reciprocal of square root of x element-wise.

  For example:

  >>> x = tf.constant([2., 0., -2.])
  >>> tf.math.rsqrt(x)
  <tf.Tensor: shape=(3,), dtype=float32,
  numpy=array([0.707, inf, nan], dtype=float32)>

  Args:
    x: A `tf.Tensor`. Must be one of the following types: `bfloat16`, `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor`. Has the same type as `x`.
  """
def acos(x, name: Incomplete | None = None):
    """Computes acos of x element-wise.

  Provided an input tensor, the `tf.math.acos` operation
  returns the inverse cosine of each element of the tensor.
  If `y = tf.math.cos(x)` then, `x = tf.math.acos(y)`.

  Input range is `[-1, 1]` and the output has a range of `[0, pi]`.

  For example:

  >>> x = tf.constant([1.0, -0.5, 3.4, 0.2, 0.0, -2], dtype = tf.float32)
  >>> tf.math.acos(x)
  <tf.Tensor: shape=(6,), dtype=float32,
  numpy= array([0. , 2.0943952, nan, 1.3694383, 1.5707964, nan],
  dtype=float32)>

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`,
      `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as x.
  """
def floor(x, name: Incomplete | None = None):
    '''Returns element-wise largest integer not greater than x.

  Both input range is `(-inf, inf)` and the
  output range consists of all integer values.

  For example:

  >>> x = tf.constant([1.3324, -1.5, 5.555, -2.532, 0.99, float("inf")])
  >>> tf.floor(x).numpy()
  array([ 1., -2.,  5., -3.,  0., inf], dtype=float32)

  Args:
    x:  A `Tensor`. Must be one of the following types: `bfloat16`, `half`,
      `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as x.
  '''
