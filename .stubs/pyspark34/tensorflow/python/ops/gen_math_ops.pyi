from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

Abs: Incomplete

def accumulate_nv2(inputs, shape, name: Incomplete | None = None):
    """Returns the element-wise sum of a list of tensors.

  `tf.accumulate_n_v2` performs the same operation as `tf.add_n`, but does not
  wait for all of its inputs to be ready before beginning to sum. This can
  save memory if inputs are ready at different times, since minimum temporary
  storage is proportional to the output size rather than the inputs size.

  Unlike the original `accumulate_n`, `accumulate_n_v2` is differentiable.

  Returns a `Tensor` of same shape and type as the elements of `inputs`.

  Args:
    inputs: A list of at least 1 `Tensor` objects with the same type in: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A list of `Tensor` objects, each with same shape and type.
    shape: A `tf.TensorShape` or list of `ints`.
      Shape of elements of `inputs`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `inputs`.
  """

AccumulateNV2: Incomplete

def accumulate_nv2_eager_fallback(inputs, shape, name, ctx): ...
def acos(x, name: Incomplete | None = None):
    """Computes acos of x element-wise.

  
    Provided an input tensor, the `tf.math.acos` operation returns the inverse cosine of each element of the tensor. If `y = tf.math.cos(x)` then, `x = tf.math.acos(y)`.

    Input range is `[-1, 1]` and the output has a range of `[0, pi]`.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Acos: Incomplete

def acos_eager_fallback(x, name, ctx): ...
def acosh(x, name: Incomplete | None = None):
    '''Computes inverse hyperbolic cosine of x element-wise.

  Given an input tensor, the function computes inverse hyperbolic cosine of every element.
  Input range is `[1, inf]`. It returns `nan` if the input lies outside the range.

  ```python
  x = tf.constant([-2, -0.5, 1, 1.2, 200, 10000, float("inf")])
  tf.math.acosh(x) ==> [nan nan 0. 0.62236255 5.9914584 9.903487 inf]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Acosh: Incomplete

def acosh_eager_fallback(x, name, ctx): ...
def add(x, y, name: Incomplete | None = None):
    """Returns x + y element-wise.

  *NOTE*: `Add` supports broadcasting. `AddN` does not. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Given two input tensors, the `tf.add` operation computes the sum for every element in the tensor.

  Both input and output have a range `(-inf, inf)`.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Add: Incomplete

def add_eager_fallback(x, y, name, ctx): ...
def add_n(inputs, name: Incomplete | None = None):
    """Add all input tensors element wise.

    Inputs must be of same size and shape.

    ```python
    x = [9, 7, 10]
    tf.math.add_n(x) ==> 26
    ```

  Args:
    inputs: A list of at least 1 `Tensor` objects with the same type in: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `inputs`.
  """

AddN: Incomplete

def add_n_eager_fallback(inputs, name, ctx): ...
def add_v2(x, y, name: Incomplete | None = None):
    """Returns x + y element-wise.

  *NOTE*: `Add` supports broadcasting. `AddN` does not. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

AddV2: Incomplete

def add_v2_eager_fallback(x, y, name, ctx): ...

All: Incomplete

def angle(input, Tout=..., name: Incomplete | None = None):
    """Returns the argument of a complex number.

  Given a tensor `input` of complex numbers, this operation returns a tensor of
  type `float` that is the argument of each element in `input`. All elements in
  `input` must be complex numbers of the form \\\\(a + bj\\\\), where *a*
  is the real part and *b* is the imaginary part.

  The argument returned by this operation is of the form \\\\(atan2(b, a)\\\\).

  For example:

  ```
  # tensor 'input' is [-2.25 + 4.75j, 3.25 + 5.75j]
  tf.math.angle(input) ==> [2.0132, 1.056]
  ```

  @compatibility(numpy)
  Equivalent to np.angle.
  @end_compatibility

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
    Tout: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

Angle: Incomplete

def angle_eager_fallback(input, Tout, name, ctx): ...

Any: Incomplete

def approximate_equal(x, y, tolerance: float = 1e-05, name: Incomplete | None = None):
    """Returns the truth value of abs(x-y) < tolerance element-wise.

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    tolerance: An optional `float`. Defaults to `1e-05`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

ApproximateEqual: Incomplete

def approximate_equal_eager_fallback(x, y, tolerance, name, ctx): ...
def arg_max(input, dimension, output_type=..., name: Incomplete | None = None):
    """Returns the index with the largest value across dimensions of a tensor.

  Note that in case of ties the identity of the return value is not guaranteed.

  Usage:
    ```python
    import tensorflow as tf
    a = [1, 10, 26.9, 2.8, 166.32, 62.3]
    b = tf.math.argmax(input = a)
    c = tf.keras.backend.eval(b)
    # c = 4
    # here a[4] = 166.32 which is the largest element of a across axis 0
    ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`, `quint8`, `qint32`, `qint16`, `quint16`, `bool`.
    dimension: A `Tensor`. Must be one of the following types: `int16`, `int32`, `int64`.
      int16, int32 or int64, must be in the range `[-rank(input), rank(input))`.
      Describes which dimension of the input Tensor to reduce across. For vectors,
      use dimension = 0.
    output_type: An optional `tf.DType` from: `tf.int16, tf.uint16, tf.int32, tf.int64`. Defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `output_type`.
  """

ArgMax: Incomplete

def arg_max_eager_fallback(input, dimension, output_type, name, ctx): ...
def arg_min(input, dimension, output_type=..., name: Incomplete | None = None):
    """Returns the index with the smallest value across dimensions of a tensor.

  Note that in case of ties the identity of the return value is not guaranteed.

  Usage:
    ```python
    import tensorflow as tf
    a = [1, 10, 26.9, 2.8, 166.32, 62.3]
    b = tf.math.argmin(input = a)
    c = tf.keras.backend.eval(b)
    # c = 0
    # here a[0] = 1 which is the smallest element of a across axis 0
    ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `qint8`, `quint8`, `qint32`, `qint16`, `quint16`, `bool`.
    dimension: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      int32 or int64, must be in the range `[-rank(input), rank(input))`.
      Describes which dimension of the input Tensor to reduce across. For vectors,
      use dimension = 0.
    output_type: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `output_type`.
  """

ArgMin: Incomplete

def arg_min_eager_fallback(input, dimension, output_type, name, ctx): ...
def asin(x, name: Incomplete | None = None):
    """Computes the trignometric inverse sine of x element-wise.

  The `tf.math.asin` operation returns the inverse of `tf.math.sin`, such that
  if `y = tf.math.sin(x)` then, `x = tf.math.asin(y)`.

  **Note**: The output of `tf.math.asin` will lie within the invertible range
  of sine, i.e [-pi/2, pi/2].

  For example:

  ```python
  # Note: [1.047, 0.785] ~= [(pi/3), (pi/4)]
  x = tf.constant([1.047, 0.785])
  y = tf.math.sin(x) # [0.8659266, 0.7068252]

  tf.math.asin(y) # [1.047, 0.785] = x
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Asin: Incomplete

def asin_eager_fallback(x, name, ctx): ...
def asinh(x, name: Incomplete | None = None):
    '''Computes inverse hyperbolic sine of x element-wise.

    Given an input tensor, this function computes inverse hyperbolic sine
    for every element in the tensor. Both input and output has a range of
    `[-inf, inf]`.

    ```python
    x = tf.constant([-float("inf"), -2, -0.5, 1, 1.2, 200, 10000, float("inf")])
    tf.math.asinh(x) ==> [-inf -1.4436355 -0.4812118 0.8813736 1.0159732 5.991471 9.903487 inf]
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Asinh: Incomplete

def asinh_eager_fallback(x, name, ctx): ...
def atan(x, name: Incomplete | None = None):
    """Computes the trignometric inverse tangent of x element-wise.

  The `tf.math.atan` operation returns the inverse of `tf.math.tan`, such that
  if `y = tf.math.tan(x)` then, `x = tf.math.atan(y)`.

  **Note**: The output of `tf.math.atan` will lie within the invertible range
  of tan, i.e (-pi/2, pi/2).

  For example:

  ```python
  # Note: [1.047, 0.785] ~= [(pi/3), (pi/4)]
  x = tf.constant([1.047, 0.785])
  y = tf.math.tan(x) # [1.731261, 0.99920404]

  tf.math.atan(y) # [1.047, 0.785] = x
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Atan: Incomplete

def atan_eager_fallback(x, name, ctx): ...
def atan2(y, x, name: Incomplete | None = None):
    """Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

  This is the angle \\\\( \\theta \\in [-\\pi, \\pi] \\\\) such that
  \\\\[ x = r \\cos(\\theta) \\\\]
  and
  \\\\[ y = r \\sin(\\theta) \\\\]
  where \\\\(r = \\sqrt{x^2 + y^2} \\\\).

  For example:

  >>> x = [1., 1.]
  >>> y = [1., -1.]
  >>> print((tf.math.atan2(y,x) * (180 / np.pi)).numpy())
  [ 45. -45.]

  Args:
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    x: A `Tensor`. Must have the same type as `y`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `y`.
  """

Atan2: Incomplete

def atan2_eager_fallback(y, x, name, ctx): ...
def atanh(x, name: Incomplete | None = None):
    '''Computes inverse hyperbolic tangent of x element-wise.

    Given an input tensor, this function computes inverse hyperbolic tangent
    for every element in the tensor. Input range is `[-1,1]` and output range is
    `[-inf, inf]`. If input is `-1`, output will be `-inf` and if the
    input is `1`, output will be `inf`. Values outside the range will have
    `nan` as output.

    ```python
    x = tf.constant([-float("inf"), -1, -0.5, 1, 0, 0.5, 10, float("inf")])
    tf.math.atanh(x) ==> [nan -inf -0.54930615 inf  0. 0.54930615 nan nan]
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Atanh: Incomplete

def atanh_eager_fallback(x, name, ctx): ...
def batch_mat_mul(x, y, adj_x: bool = False, adj_y: bool = False, name: Incomplete | None = None):
    """Multiplies slices of two tensors in batches.

  Multiplies all slices of `Tensor` `x` and `y` (each slice can be
  viewed as an element of a batch), and arranges the individual results
  in a single output tensor of the same batch size. Each of the
  individual slices can optionally be adjointed (to adjoint a matrix
  means to transpose and conjugate it) before multiplication by setting
  the `adj_x` or `adj_y` flag to `True`, which are by default `False`.

  The input tensors `x` and `y` are 2-D or higher with shape `[..., r_x, c_x]`
  and `[..., r_y, c_y]`.

  The output tensor is 2-D or higher with shape `[..., r_o, c_o]`, where:

      r_o = c_x if adj_x else r_x
      c_o = r_y if adj_y else c_y

  It is computed as:

      output[..., :, :] = matrix(x[..., :, :]) * matrix(y[..., :, :])

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
      2-D or higher with shape `[..., r_x, c_x]`.
    y: A `Tensor`. Must have the same type as `x`.
      2-D or higher with shape `[..., r_y, c_y]`.
    adj_x: An optional `bool`. Defaults to `False`.
      If `True`, adjoint the slices of `x`. Defaults to `False`.
    adj_y: An optional `bool`. Defaults to `False`.
      If `True`, adjoint the slices of `y`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

BatchMatMul: Incomplete

def batch_mat_mul_eager_fallback(x, y, adj_x, adj_y, name, ctx): ...
def batch_mat_mul_v2(x, y, adj_x: bool = False, adj_y: bool = False, name: Incomplete | None = None):
    """Multiplies slices of two tensors in batches.

  Multiplies all slices of `Tensor` `x` and `y` (each slice can be
  viewed as an element of a batch), and arranges the individual results
  in a single output tensor of the same batch size. Each of the
  individual slices can optionally be adjointed (to adjoint a matrix
  means to transpose and conjugate it) before multiplication by setting
  the `adj_x` or `adj_y` flag to `True`, which are by default `False`.

  The input tensors `x` and `y` are 2-D or higher with shape `[..., r_x, c_x]`
  and `[..., r_y, c_y]`.

  The output tensor is 2-D or higher with shape `[..., r_o, c_o]`, where:

      r_o = c_x if adj_x else r_x
      c_o = r_y if adj_y else c_y

  It is computed as:

      output[..., :, :] = matrix(x[..., :, :]) * matrix(y[..., :, :])

  *NOTE*: `BatchMatMulV2` supports broadcasting in the batch dimensions. More
  about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `complex64`, `complex128`.
      2-D or higher with shape `[..., r_x, c_x]`.
    y: A `Tensor`. Must have the same type as `x`.
      2-D or higher with shape `[..., r_y, c_y]`.
    adj_x: An optional `bool`. Defaults to `False`.
      If `True`, adjoint the slices of `x`. Defaults to `False`.
    adj_y: An optional `bool`. Defaults to `False`.
      If `True`, adjoint the slices of `y`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

BatchMatMulV2: Incomplete

def batch_mat_mul_v2_eager_fallback(x, y, adj_x, adj_y, name, ctx): ...
def batch_mat_mul_v3(x, y, Tout, adj_x: bool = False, adj_y: bool = False, name: Incomplete | None = None):
    """Multiplies slices of two tensors in batches.

  Multiplies all slices of `Tensor` `x` and `y` (each slice can be
  viewed as an element of a batch), and arranges the individual results
  in a single output tensor of the same batch size. Each of the
  individual slices can optionally be adjointed (to adjoint a matrix
  means to transpose and conjugate it) before multiplication by setting
  the `adj_x` or `adj_y` flag to `True`, which are by default `False`.

  The input tensors `x` and `y` are 2-D or higher with shape `[..., r_x, c_x]`
  and `[..., r_y, c_y]`.

  The output tensor is 2-D or higher with shape `[..., r_o, c_o]`, where:

      r_o = c_x if adj_x else r_x
      c_o = r_y if adj_y else c_y

  It is computed as:

      output[..., :, :] = matrix(x[..., :, :]) * matrix(y[..., :, :])

  *NOTE*: `BatchMatMulV3` supports broadcasting in the batch dimensions. More
  about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
      2-D or higher with shape `[..., r_x, c_x]`.
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
      2-D or higher with shape `[..., r_y, c_y]`.
    Tout: A `tf.DType` from: `tf.bfloat16, tf.half, tf.float32, tf.float64, tf.int16, tf.int32, tf.int64, tf.complex64, tf.complex128`.
      If not spcified, Tout is the same type to input type.
    adj_x: An optional `bool`. Defaults to `False`.
      If `True`, adjoint the slices of `x`. Defaults to `False`.
    adj_y: An optional `bool`. Defaults to `False`.
      If `True`, adjoint the slices of `y`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

BatchMatMulV3: Incomplete

def batch_mat_mul_v3_eager_fallback(x, y, Tout, adj_x, adj_y, name, ctx): ...
def betainc(a, b, x, name: Incomplete | None = None):
    """Compute the regularized incomplete beta integral \\\\(I_x(a, b)\\\\).

  The regularized incomplete beta integral is defined as:


  \\\\(I_x(a, b) = \\frac{B(x; a, b)}{B(a, b)}\\\\)

  where


  \\\\(B(x; a, b) = \\int_0^x t^{a-1} (1 - t)^{b-1} dt\\\\)


  is the incomplete beta function and \\\\(B(a, b)\\\\) is the *complete*
  beta function.

  Args:
    a: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    b: A `Tensor`. Must have the same type as `a`.
    x: A `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Betainc: Incomplete

def betainc_eager_fallback(a, b, x, name, ctx): ...
def bincount(arr, size, weights, name: Incomplete | None = None):
    """Counts the number of occurrences of each value in an integer array.

  Outputs a vector with length `size` and the same dtype as `weights`. If
  `weights` are empty, then index `i` stores the number of times the value `i` is
  counted in `arr`. If `weights` are non-empty, then index `i` stores the sum of
  the value in `weights` at each index where the corresponding value in `arr` is
  `i`.

  Values in `arr` outside of the range [0, size) are ignored.

  Args:
    arr: A `Tensor` of type `int32`. int32 `Tensor`.
    size: A `Tensor` of type `int32`. non-negative int32 scalar `Tensor`.
    weights: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      is an int32, int64, float32, or float64 `Tensor` with the same
      shape as `arr`, or a length-0 `Tensor`, in which case it acts as all weights
      equal to 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `weights`.
  """

Bincount: Incomplete

def bincount_eager_fallback(arr, size, weights, name, ctx): ...
def bucketize(input, boundaries, name: Incomplete | None = None):
    """Bucketizes 'input' based on 'boundaries'.

  For example, if the inputs are
      boundaries = [0, 10, 100]
      input = [[-5, 10000]
               [150,   10]
               [5,    100]]

  then the output will be
      output = [[0, 3]
                [3, 2]
                [1, 3]]

  Args:
    input: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      Any shape of Tensor contains with int or float type.
    boundaries: A list of `floats`.
      A sorted list of floats gives the boundary of the buckets.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

Bucketize: Incomplete

def bucketize_eager_fallback(input, boundaries, name, ctx): ...
def cast(x, DstT, Truncate: bool = False, name: Incomplete | None = None):
    """Cast x of type SrcT to y of DstT.

  Args:
    x: A `Tensor`.
    DstT: A `tf.DType`.
    Truncate: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `DstT`.
  """

Cast: Incomplete

def cast_eager_fallback(x, DstT, Truncate, name, ctx): ...
def ceil(x, name: Incomplete | None = None):
    """Returns element-wise smallest integer not less than x.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Ceil: Incomplete

def ceil_eager_fallback(x, name, ctx): ...

ClipByValue: Incomplete
Complex: Incomplete

def complex_abs(x, Tout=..., name: Incomplete | None = None):
    """Computes the complex absolute value of a tensor.

  Given a tensor `x` of complex numbers, this operation returns a tensor of type
  `float` or `double` that is the absolute value of each element in `x`. All
  elements in `x` must be complex numbers of the form \\\\(a + bj\\\\). The absolute
  value is computed as \\\\( \\sqrt{a^2 + b^2}\\\\).

  For example:

  >>> x = tf.complex(3.0, 4.0)
  >>> print((tf.raw_ops.ComplexAbs(x=x, Tout=tf.dtypes.float32, name=None)).numpy())
  5.0

  Args:
    x: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
    Tout: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

ComplexAbs: Incomplete

def complex_abs_eager_fallback(x, Tout, name, ctx): ...
def conj(input, name: Incomplete | None = None):
    """Returns the complex conjugate of a complex number.

  Given a tensor `input` of complex numbers, this operation returns a tensor of
  complex numbers that are the complex conjugate of each element in `input`. The
  complex numbers in `input` must be of the form \\\\(a + bj\\\\), where *a* is the
  real part and *b* is the imaginary part.

  The complex conjugate returned by this operation is of the form \\\\(a - bj\\\\).

  For example:

  ```
  # tensor 'input' is [-2.25 + 4.75j, 3.25 + 5.75j]
  tf.conj(input) ==> [-2.25 - 4.75j, 3.25 - 5.75j]
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`, `variant`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

Conj: Incomplete

def conj_eager_fallback(input, name, ctx): ...
def cos(x, name: Incomplete | None = None):
    '''Computes cos of x element-wise.

    Given an input tensor, this function computes cosine of every
    element in the tensor. Input range is `(-inf, inf)` and
    output range is `[-1,1]`. If input lies outside the boundary, `nan`
    is returned.

    ```python
    x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10000, float("inf")])
    tf.math.cos(x) ==> [nan -0.91113025 0.87758255 0.5403023 0.36235774 0.48718765 -0.95215535 nan]
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Cos: Incomplete

def cos_eager_fallback(x, name, ctx): ...
def cosh(x, name: Incomplete | None = None):
    '''Computes hyperbolic cosine of x element-wise.

    Given an input tensor, this function computes hyperbolic cosine of every
    element in the tensor. Input range is `[-inf, inf]` and output range
    is `[1, inf]`.

    ```python
    x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 2, 10, float("inf")])
    tf.math.cosh(x) ==> [inf 4.0515420e+03 1.1276259e+00 1.5430807e+00 1.8106556e+00 3.7621956e+00 1.1013233e+04 inf]
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Cosh: Incomplete

def cosh_eager_fallback(x, name, ctx): ...
def cross(a, b, name: Incomplete | None = None):
    """Compute the pairwise cross product.

  `a` and `b` must be the same shape; they can either be simple 3-element vectors,
  or any shape where the innermost dimension is 3. In the latter case, each pair
  of corresponding 3-element vectors is cross-multiplied independently.

  Args:
    a: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
      A tensor containing 3-element vectors.
    b: A `Tensor`. Must have the same type as `a`.
      Another tensor, of same type and shape as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Cross: Incomplete

def cross_eager_fallback(a, b, name, ctx): ...
def cumprod(x, axis, exclusive: bool = False, reverse: bool = False, name: Incomplete | None = None):
    """Compute the cumulative product of the tensor `x` along `axis`.

  By default, this op performs an inclusive cumprod, which means that the first
  element of the input is identical to the first element of the output:

  ```python
  tf.cumprod([a, b, c])  # => [a, a * b, a * b * c]
  ```

  By setting the `exclusive` kwarg to `True`, an exclusive cumprod is
  performed instead:

  ```python
  tf.cumprod([a, b, c], exclusive=True)  # => [1, a, a * b]
  ```

  By setting the `reverse` kwarg to `True`, the cumprod is performed in the
  opposite direction:

  ```python
  tf.cumprod([a, b, c], reverse=True)  # => [a * b * c, b * c, c]
  ```

  This is more efficient than using separate `tf.reverse` ops.

  The `reverse` and `exclusive` kwargs can also be combined:

  ```python
  tf.cumprod([a, b, c], exclusive=True, reverse=True)  # => [b * c, c, 1]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A `Tensor`. Must be one of the following types: `float32`, `float64`,
      `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
      `complex128`, `qint8`, `quint8`, `qint32`, `half`.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A `Tensor` of type `int32` (default: 0). Must be in the range
      `[-rank(x), rank(x))`.
    exclusive: An optional `bool`. Defaults to `False`.
      If `True`, perform exclusive cumprod.
    reverse: An optional `bool`. Defaults to `False`.
      A `bool` (default: False).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Cumprod: Incomplete

def cumprod_eager_fallback(x, axis, exclusive, reverse, name, ctx): ...
def cumsum(x, axis, exclusive: bool = False, reverse: bool = False, name: Incomplete | None = None):
    """Compute the cumulative sum of the tensor `x` along `axis`.

  By default, this op performs an inclusive cumsum, which means that the first
  element of the input is identical to the first element of the output:

  ```python
  tf.cumsum([a, b, c])  # => [a, a + b, a + b + c]
  ```

  By setting the `exclusive` kwarg to `True`, an exclusive cumsum is
  performed instead:

  ```python
  tf.cumsum([a, b, c], exclusive=True)  # => [0, a, a + b]
  ```

  By setting the `reverse` kwarg to `True`, the cumsum is performed in the
  opposite direction:

  ```python
  tf.cumsum([a, b, c], reverse=True)  # => [a + b + c, b + c, c]
  ```

  This is more efficient than using separate `tf.reverse` ops.

  The `reverse` and `exclusive` kwargs can also be combined:

  ```python
  tf.cumsum([a, b, c], exclusive=True, reverse=True)  # => [b + c, c, 0]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      A `Tensor`. Must be one of the following types: `float32`, `float64`,
      `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
      `complex128`, `qint8`, `quint8`, `qint32`, `half`.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A `Tensor` of type `int32` (default: 0). Must be in the range
      `[-rank(x), rank(x))`.
    exclusive: An optional `bool`. Defaults to `False`.
      If `True`, perform exclusive cumsum.
    reverse: An optional `bool`. Defaults to `False`.
      A `bool` (default: False).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Cumsum: Incomplete

def cumsum_eager_fallback(x, axis, exclusive, reverse, name, ctx): ...
def cumulative_logsumexp(x, axis, exclusive: bool = False, reverse: bool = False, name: Incomplete | None = None):
    """Compute the cumulative product of the tensor `x` along `axis`.

  By default, this op performs an inclusive cumulative log-sum-exp,
  which means that the first
  element of the input is identical to the first element of the output:
  ```python
  tf.math.cumulative_logsumexp([a, b, c])  # => [a, log(exp(a) + exp(b)), log(exp(a) + exp(b) + exp(c))]
  ```

  By setting the `exclusive` kwarg to `True`, an exclusive cumulative log-sum-exp is
  performed instead:
  ```python
  tf.cumulative_logsumexp([a, b, c], exclusive=True)  # => [-inf, a, log(exp(a) * exp(b))]
  ```
  Note that the neutral element of the log-sum-exp operation is `-inf`,
  however, for performance reasons, the minimal value representable by the
  floating point type is used instead.

  By setting the `reverse` kwarg to `True`, the cumulative log-sum-exp is performed in the
  opposite direction.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
      A `Tensor`. Must be one of the following types: `float16`, `float32`, `float64`.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A `Tensor` of type `int32` (default: 0). Must be in the range
      `[-rank(x), rank(x))`.
    exclusive: An optional `bool`. Defaults to `False`.
      If `True`, perform exclusive cumulative log-sum-exp.
    reverse: An optional `bool`. Defaults to `False`.
      A `bool` (default: False).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

CumulativeLogsumexp: Incomplete

def cumulative_logsumexp_eager_fallback(x, axis, exclusive, reverse, name, ctx): ...
def dense_bincount(input, size, weights, binary_output: bool = False, name: Incomplete | None = None):
    """Counts the number of occurrences of each value in an integer array.

  Outputs a vector with length `size` and the same dtype as `weights`. If
  `weights` are empty, then index `i` stores the number of times the value `i` is
  counted in `arr`. If `weights` are non-empty, then index `i` stores the sum of
  the value in `weights` at each index where the corresponding value in `arr` is
  `i`.

  Values in `arr` outside of the range [0, size) are ignored.

  Args:
    input: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      1D or 2D int `Tensor`.
    size: A `Tensor`. Must have the same type as `input`.
      non-negative int scalar `Tensor`.
    weights: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      is an int32, int64, float32, or float64 `Tensor` with the same
      shape as `arr`, or a length-0 `Tensor`, in which case it acts as all weights
      equal to 1.
    binary_output: An optional `bool`. Defaults to `False`.
      bool; Whether the kernel should count the appearance or number of occurrences.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `weights`.
  """

DenseBincount: Incomplete

def dense_bincount_eager_fallback(input, size, weights, binary_output, name, ctx): ...
def digamma(x, name: Incomplete | None = None):
    """Computes Psi, the derivative of Lgamma (the log of the absolute value of

  `Gamma(x)`), element-wise.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Digamma: Incomplete

def digamma_eager_fallback(x, name, ctx): ...
def div(x, y, name: Incomplete | None = None):
    """Returns x / y element-wise.

  *NOTE*: `Div` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `uint32`, `uint64`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Div: Incomplete

def div_eager_fallback(x, y, name, ctx): ...
def div_no_nan(x, y, name: Incomplete | None = None):
    """Returns 0 if the denominator is zero.

  
  *NOTE*: `DivNoNan` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `half`, `float32`, `bfloat16`, `float64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

DivNoNan: Incomplete

def div_no_nan_eager_fallback(x, y, name, ctx): ...
def equal(x, y, incompatible_shape_error: bool = True, name: Incomplete | None = None):
    """Returns the truth value of (x == y) element-wise.

  *NOTE*: `Equal` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  ```python
  x = tf.constant([2, 4])
  y = tf.constant(2)
  tf.math.equal(x, y) ==> array([True, False])

  x = tf.constant([2, 4])
  y = tf.constant([2, 4])
  tf.math.equal(x, y) ==> array([True,  True])
  ```

  Args:
    x: A `Tensor`.
    y: A `Tensor`. Must have the same type as `x`.
    incompatible_shape_error: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

Equal: Incomplete

def equal_eager_fallback(x, y, incompatible_shape_error, name, ctx): ...
def erf(x, name: Incomplete | None = None):
    """Computes the [Gauss error function](https://en.wikipedia.org/wiki/Error_function) of `x` element-wise. In statistics, for non-negative values of $x$, the error function has the following interpretation: for a random variable $Y$ that is normally distributed with mean 0 and variance $1/\\sqrt{2}$, $erf(x)$ is the probability that $Y$ falls in the range $[−x, x]$.

  For example:

  >>> tf.math.erf([[1.0, 2.0, 3.0], [0.0, -1.0, -2.0]])
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
  array([[ 0.8427007,  0.9953223,  0.999978 ],
         [ 0.       , -0.8427007, -0.9953223]], dtype=float32)>

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Erf: Incomplete

def erf_eager_fallback(x, name, ctx): ...
def erfc(x, name: Incomplete | None = None):
    """Computes the complementary error function of `x` element-wise.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Erfc: Incomplete

def erfc_eager_fallback(x, name, ctx): ...
def erfinv(x, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Erfinv: Incomplete

def erfinv_eager_fallback(x, name, ctx): ...
def euclidean_norm(input, axis, keep_dims: bool = False, name: Incomplete | None = None):
    """Computes the euclidean norm of elements across dimensions of a tensor.

  Reduces `input` along the dimensions given in `axis`. Unless
  `keep_dims` is true, the rank of the tensor is reduced by 1 for each entry in
  `axis`. If `keep_dims` is true, the reduced dimensions are
  retained with length 1.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      The tensor to reduce.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The dimensions to reduce. Must be in the range
      `[-rank(input), rank(input))`.
    keep_dims: An optional `bool`. Defaults to `False`.
      If true, retain reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

EuclideanNorm: Incomplete

def euclidean_norm_eager_fallback(input, axis, keep_dims, name, ctx): ...
def exp(x, name: Incomplete | None = None):
    """Computes exponential of x element-wise.  \\\\(y = e^x\\\\).

    This function computes the exponential of every element in the input tensor.
    i.e. `exp(x)` or `e^(x)`, where `x` is the input tensor.
    `e` denotes Euler's number and is approximately equal to 2.718281.
    Output is positive for any real input.

    ```python
    x = tf.constant(2.0)
    tf.math.exp(x) ==> 7.389056

    x = tf.constant([2.0, 8.0])
    tf.math.exp(x) ==> array([7.389056, 2980.958], dtype=float32)
    ```

    For complex numbers, the exponential value is calculated as follows:

    ```
    e^(x+iy) = e^x * e^iy = e^x * (cos y + i sin y)
    ```

    Let's consider complex number 1+1j as an example.
    e^1 * (cos 1 + i sin 1) = 2.7182818284590 * (0.54030230586+0.8414709848j)

    ```python
    x = tf.constant(1 + 1j)
    tf.math.exp(x) ==> 1.4686939399158851+2.2873552871788423j
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Exp: Incomplete

def exp_eager_fallback(x, name, ctx): ...
def expm1(x, name: Incomplete | None = None):
    """Computes `exp(x) - 1` element-wise.

    i.e. `exp(x) - 1` or `e^(x) - 1`, where `x` is the input tensor.
    `e` denotes Euler's number and is approximately equal to 2.718281.

    ```python
    x = tf.constant(2.0)
    tf.math.expm1(x) ==> 6.389056

    x = tf.constant([2.0, 8.0])
    tf.math.expm1(x) ==> array([6.389056, 2979.958], dtype=float32)

    x = tf.constant(1 + 1j)
    tf.math.expm1(x) ==> (0.46869393991588515+2.2873552871788423j)
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Expm1: Incomplete

def expm1_eager_fallback(x, name, ctx): ...
def floor(x, name: Incomplete | None = None):
    """Returns element-wise largest integer not greater than x.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Floor: Incomplete

def floor_eager_fallback(x, name, ctx): ...
def floor_div(x, y, name: Incomplete | None = None):
    """Returns x // y element-wise.

  *NOTE*: `floor_div` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `uint32`, `uint64`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

FloorDiv: Incomplete

def floor_div_eager_fallback(x, y, name, ctx): ...
def floor_mod(x, y, name: Incomplete | None = None):
    """Returns element-wise remainder of division.

  This follows Python semantics in that the
  result here is consistent with a flooring divide. E.g.
  `floor(x / y) * y + floormod(x, y) = x`, regardless of the signs of x and y.

  *NOTE*: `math.floormod` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `bfloat16`, `half`, `float32`, `float64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

FloorMod: Incomplete

def floor_mod_eager_fallback(x, y, name, ctx): ...
def greater(x, y, name: Incomplete | None = None):
    """Returns the truth value of (x > y) element-wise.

  *NOTE*: `math.greater` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Example:

  ```python
  x = tf.constant([5, 4, 6])
  y = tf.constant([5, 2, 5])
  tf.math.greater(x, y) ==> [False, True, True]

  x = tf.constant([5, 4, 6])
  y = tf.constant([5])
  tf.math.greater(x, y) ==> [False, False, True]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

Greater: Incomplete

def greater_eager_fallback(x, y, name, ctx): ...
def greater_equal(x, y, name: Incomplete | None = None):
    """Returns the truth value of (x >= y) element-wise.

  *NOTE*: `math.greater_equal` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Example:

  ```python
  x = tf.constant([5, 4, 6, 7])
  y = tf.constant([5, 2, 5, 10])
  tf.math.greater_equal(x, y) ==> [True, True, True, False]

  x = tf.constant([5, 4, 6, 7])
  y = tf.constant([5])
  tf.math.greater_equal(x, y) ==> [True, False, True, True]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

GreaterEqual: Incomplete

def greater_equal_eager_fallback(x, y, name, ctx): ...

HistogramFixedWidth: Incomplete

def igamma(a, x, name: Incomplete | None = None):
    """Compute the lower regularized incomplete Gamma function `P(a, x)`.

  The lower regularized incomplete Gamma function is defined as:


  \\\\(P(a, x) = gamma(a, x) / Gamma(a) = 1 - Q(a, x)\\\\)

  where

  \\\\(gamma(a, x) = \\\\int_{0}^{x} t^{a-1} exp(-t) dt\\\\)

  is the lower incomplete Gamma function.

  Note, above `Q(a, x)` (`Igammac`) is the upper regularized complete
  Gamma function.

  Args:
    a: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    x: A `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Igamma: Incomplete

def igamma_eager_fallback(a, x, name, ctx): ...
def igamma_grad_a(a, x, name: Incomplete | None = None):
    """Computes the gradient of `igamma(a, x)` wrt `a`.

  Args:
    a: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    x: A `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

IgammaGradA: Incomplete

def igamma_grad_a_eager_fallback(a, x, name, ctx): ...
def igammac(a, x, name: Incomplete | None = None):
    """Compute the upper regularized incomplete Gamma function `Q(a, x)`.

  The upper regularized incomplete Gamma function is defined as:

  \\\\(Q(a, x) = Gamma(a, x) / Gamma(a) = 1 - P(a, x)\\\\)

  where

  \\\\(Gamma(a, x) = \\int_{x}^{\\infty} t^{a-1} exp(-t) dt\\\\)

  is the upper incomplete Gamma function.

  Note, above `P(a, x)` (`Igamma`) is the lower regularized complete
  Gamma function.

  Args:
    a: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    x: A `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Igammac: Incomplete

def igammac_eager_fallback(a, x, name, ctx): ...
def imag(input, Tout=..., name: Incomplete | None = None):
    """Returns the imaginary part of a complex number.

  Given a tensor `input` of complex numbers, this operation returns a tensor of
  type `float` that is the imaginary part of each element in `input`. All
  elements in `input` must be complex numbers of the form \\\\(a + bj\\\\), where *a*
  is the real part and *b* is the imaginary part returned by this operation.

  For example:

  ```
  # tensor 'input' is [-2.25 + 4.75j, 3.25 + 5.75j]
  tf.imag(input) ==> [4.75, 5.75]
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
    Tout: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

Imag: Incomplete

def imag_eager_fallback(input, Tout, name, ctx): ...
def inv(x, name: Incomplete | None = None):
    """Computes the reciprocal of x element-wise.

  I.e., \\\\(y = 1 / x\\\\).

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Inv: Incomplete

def inv_eager_fallback(x, name, ctx): ...
def inv_grad(y, dy, name: Incomplete | None = None):
    """Computes the gradient for the inverse of `x` wrt its input.

  Specifically, `grad = -dy * y*y`, where `y = 1/x`, and `dy`
  is the corresponding input gradient.

  Args:
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    dy: A `Tensor`. Must have the same type as `y`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `y`.
  """

InvGrad: Incomplete

def inv_grad_eager_fallback(y, dy, name, ctx): ...
def is_finite(x, name: Incomplete | None = None):
    """Returns which elements of x are finite.

  @compatibility(numpy)
  Equivalent to np.isfinite
  @end_compatibility

  Example:

  ```python
  x = tf.constant([5.0, 4.8, 6.8, np.inf, np.nan])
  tf.math.is_finite(x) ==> [True, True, True, False, False]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

IsFinite: Incomplete

def is_finite_eager_fallback(x, name, ctx): ...
def is_inf(x, name: Incomplete | None = None):
    """Returns which elements of x are Inf.

  @compatibility(numpy)
  Equivalent to np.isinf
  @end_compatibility

  Example:

  ```python
  x = tf.constant([5.0, np.inf, 6.8, np.inf])
  tf.math.is_inf(x) ==> [False, True, False, True]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

IsInf: Incomplete

def is_inf_eager_fallback(x, name, ctx): ...
def is_nan(x, name: Incomplete | None = None):
    """Returns which elements of x are NaN.

  @compatibility(numpy)
  Equivalent to np.isnan
  @end_compatibility

  Example:

  ```python
  x = tf.constant([5.0, np.nan, 6.8, np.nan, np.inf])
  tf.math.is_nan(x) ==> [False, True, False, True, False]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

IsNan: Incomplete

def is_nan_eager_fallback(x, name, ctx): ...
def less(x, y, name: Incomplete | None = None):
    """Returns the truth value of (x < y) element-wise.

  *NOTE*: `math.less` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Example:

  ```python
  x = tf.constant([5, 4, 6])
  y = tf.constant([5])
  tf.math.less(x, y) ==> [False, True, False]

  x = tf.constant([5, 4, 6])
  y = tf.constant([5, 6, 7])
  tf.math.less(x, y) ==> [False, True, True]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

Less: Incomplete

def less_eager_fallback(x, y, name, ctx): ...
def less_equal(x, y, name: Incomplete | None = None):
    """Returns the truth value of (x <= y) element-wise.

  *NOTE*: `math.less_equal` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Example:

  ```python
  x = tf.constant([5, 4, 6])
  y = tf.constant([5])
  tf.math.less_equal(x, y) ==> [True, True, False]

  x = tf.constant([5, 4, 6])
  y = tf.constant([5, 6, 6])
  tf.math.less_equal(x, y) ==> [True, True, True]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

LessEqual: Incomplete

def less_equal_eager_fallback(x, y, name, ctx): ...
def lgamma(x, name: Incomplete | None = None):
    """Computes the log of the absolute value of `Gamma(x)` element-wise.

    For positive numbers, this function computes log((input - 1)!) for every element in the tensor.
    `lgamma(5) = log((5-1)!) = log(4!) = log(24) = 3.1780539`

  Example:

  ```python
  x = tf.constant([0, 0.5, 1, 4.5, -4, -5.6])
  tf.math.lgamma(x) ==> [inf, 0.5723649, 0., 2.4537368, inf, -4.6477685]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Lgamma: Incomplete

def lgamma_eager_fallback(x, name, ctx): ...
def lin_space(start, stop, num, name: Incomplete | None = None):
    '''Generates values in an interval.

  A sequence of `num` evenly-spaced values are generated beginning at `start`.
  If `num > 1`, the values in the sequence increase by `stop - start / num - 1`,
  so that the last one is exactly `stop`.

  For example:

  ```
  tf.linspace(10.0, 12.0, 3, name="linspace") => [ 10.0  11.0  12.0]
  ```

  Args:
    start: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
      0-D tensor. First entry in the range.
    stop: A `Tensor`. Must have the same type as `start`.
      0-D tensor. Last entry in the range.
    num: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      0-D tensor. Number of values to generate.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `start`.
  '''

LinSpace: Incomplete

def lin_space_eager_fallback(start, stop, num, name, ctx): ...
def log(x, name: Incomplete | None = None):
    """Computes natural logarithm of x element-wise.

  I.e., \\\\(y = \\log_e x\\\\).

  Example:
  >>> x = tf.constant([0, 0.5, 1, 5])
  >>> tf.math.log(x)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=array([      -inf, -0.6931472,  0.       ,  1.609438 ], dtype=float32)>

  See: https://en.wikipedia.org/wiki/Logarithm

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Log: Incomplete

def log_eager_fallback(x, name, ctx): ...
def log1p(x, name: Incomplete | None = None):
    """Computes natural logarithm of (1 + x) element-wise.

  I.e., \\\\(y = \\log_e (1 + x)\\\\).

  Example:
  >>> x = tf.constant([0, 0.5, 1, 5])
  >>> tf.math.log1p(x)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=array([0.       , 0.4054651, 0.6931472, 1.7917595], dtype=float32)>

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Log1p: Incomplete

def log1p_eager_fallback(x, name, ctx): ...
def logical_and(x, y, name: Incomplete | None = None):
    """Returns the truth value of x AND y element-wise.

  Logical AND function.

  Requires that `x` and `y` have the same shape or have
  [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  shapes. For example, `x` and `y` can be:

    - Two single elements of type `bool`.
    - One `tf.Tensor` of type `bool` and one single `bool`, where the result will
      be calculated by applying logical AND with the single element to each
      element in the larger Tensor.
    - Two `tf.Tensor` objects of type `bool` of the same shape. In this case,
      the result will be the element-wise logical AND of the two input tensors.

  You can also use the `&` operator instead.

  Usage:

    >>> a = tf.constant([True])
    >>> b = tf.constant([False])
    >>> tf.math.logical_and(a, b)
    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])>
    >>> a & b
    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])>

    >>> c = tf.constant([True])
    >>> x = tf.constant([False, True, True, False])
    >>> tf.math.logical_and(c, x)
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
    >>> c & x
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>

    >>> y = tf.constant([False, False, True, True])
    >>> z = tf.constant([False, True, False, True])
    >>> tf.math.logical_and(y, z)
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, False, False, True])>
    >>> y & z
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, False, False, True])>

    This op also supports broadcasting

    >>> tf.logical_and([[True, False]], [[True], [False]])
    <tf.Tensor: shape=(2, 2), dtype=bool, numpy=
      array([[ True, False],
             [False, False]])>

  The reduction version of this elementwise operation is `tf.math.reduce_all`.

  Args:
      x: A `tf.Tensor` of type bool.
      y: A `tf.Tensor` of type bool.
      name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of type bool with the shape that `x` and `y` broadcast to.

  Args:
    x: A `Tensor` of type `bool`.
    y: A `Tensor` of type `bool`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

LogicalAnd: Incomplete

def logical_and_eager_fallback(x, y, name, ctx): ...
def logical_not(x, name: Incomplete | None = None):
    """Returns the truth value of `NOT x` element-wise.

  Example:

  >>> tf.math.logical_not(tf.constant([True, False]))
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([False,  True])>

  Args:
    x: A `Tensor` of type `bool`. A `Tensor` of type `bool`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

LogicalNot: Incomplete

def logical_not_eager_fallback(x, name, ctx): ...
def logical_or(x, y, name: Incomplete | None = None):
    """Returns the truth value of x OR y element-wise.

  Logical OR function.

  Requires that `x` and `y` have the same shape or have
  [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  shapes. For example, `x` and `y` can be:

  - Two single elements of type `bool`.
  - One `tf.Tensor` of type `bool` and one single `bool`, where the result will
    be calculated by applying logical OR with the single element to each
    element in the larger Tensor.
  - Two `tf.Tensor` objects of type `bool` of the same shape. In this case,
    the result will be the element-wise logical OR of the two input tensors.

  You can also use the `|` operator instead.

  Usage:

    >>> a = tf.constant([True])
    >>> b = tf.constant([False])
    >>> tf.math.logical_or(a, b)
    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
    >>> a | b
    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>

    >>> c = tf.constant([False])
    >>> x = tf.constant([False, True, True, False])
    >>> tf.math.logical_or(c, x)
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True,  True, False])>
    >>> c | x
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True,  True, False])>

    >>> y = tf.constant([False, False, True, True])
    >>> z = tf.constant([False, True, False, True])
    >>> tf.math.logical_or(y, z)
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True, True, True])>
    >>> y | z
    <tf.Tensor: shape=(4,), dtype=bool, numpy=array([False, True, True, True])>

    This op also supports broadcasting

    >>> tf.logical_or([[True, False]], [[True], [False]])
    <tf.Tensor: shape=(2, 2), dtype=bool, numpy=
    array([[ True,  True],
         [ True, False]])>

  The reduction version of this elementwise operation is `tf.math.reduce_any`.

  Args:
      x: A `tf.Tensor` of type bool.
      y: A `tf.Tensor` of type bool.
      name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of type bool with the shape that `x` and `y` broadcast to.

  Args:
    x: A `Tensor` of type `bool`.
    y: A `Tensor` of type `bool`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

LogicalOr: Incomplete

def logical_or_eager_fallback(x, y, name, ctx): ...
def mat_mul(a, b, transpose_a: bool = False, transpose_b: bool = False, name: Incomplete | None = None):
    '''Multiply the matrix "a" by the matrix "b".

  The inputs must be two-dimensional matrices and the inner dimension of
  "a" (after being transposed if transpose_a is true) must match the
  outer dimension of "b" (after being transposed if transposed_b is
  true).

  *Note*: The default kernel implementation for MatMul on GPUs uses
  cublas.

  Args:
    a: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `complex64`, `complex128`.
    b: A `Tensor`. Must have the same type as `a`.
    transpose_a: An optional `bool`. Defaults to `False`.
      If true, "a" is transposed before multiplication.
    transpose_b: An optional `bool`. Defaults to `False`.
      If true, "b" is transposed before multiplication.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  '''

MatMul: Incomplete

def mat_mul_eager_fallback(a, b, transpose_a, transpose_b, name, ctx): ...

Max: Incomplete

def maximum(x, y, name: Incomplete | None = None):
    """Returns the max of x and y (i.e. x > y ? x : y) element-wise.

  Example:

  >>> x = tf.constant([0., 0., 0., 0.])
  >>> y = tf.constant([-2., 0., 2., 5.])
  >>> tf.math.maximum(x, y)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=array([0., 0., 2., 5.], dtype=float32)>

  Note that `maximum` supports [broadcast semantics](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) for `x` and `y`.

  >>> x = tf.constant([-5., 0., 0., 0.])
  >>> y = tf.constant([-3.])
  >>> tf.math.maximum(x, y)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=array([-3., 0., 0., 0.], dtype=float32)>

  The reduction version of this elementwise operation is `tf.math.reduce_max`

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Maximum: Incomplete

def maximum_eager_fallback(x, y, name, ctx): ...
def mean(input, axis, keep_dims: bool = False, name: Incomplete | None = None):
    """Computes the mean of elements across dimensions of a tensor.

  Reduces `input` along the dimensions given in `axis`. Unless
  `keep_dims` is true, the rank of the tensor is reduced by 1 for each entry in
  `axis`. If `keep_dims` is true, the reduced dimensions are
  retained with length 1.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      The tensor to reduce.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The dimensions to reduce. Must be in the range
      `[-rank(input), rank(input))`.
    keep_dims: An optional `bool`. Defaults to `False`.
      If true, retain reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

Mean: Incomplete

def mean_eager_fallback(input, axis, keep_dims, name, ctx): ...

Min: Incomplete

def minimum(x, y, name: Incomplete | None = None):
    """Returns the min of x and y (i.e. x < y ? x : y) element-wise.

  Both inputs are number-type tensors (except complex).  `minimum` expects that
  both tensors have the same `dtype`.

  Examples:

  >>> x = tf.constant([0., 0., 0., 0.])
  >>> y = tf.constant([-5., -2., 0., 3.])
  >>> tf.math.minimum(x, y)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=array([-5., -2., 0., 0.], dtype=float32)>

  Note that `minimum` supports [broadcast semantics](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) for `x` and `y`.

  >>> x = tf.constant([-5., 0., 0., 0.])
  >>> y = tf.constant([-3.])
  >>> tf.math.minimum(x, y)
  <tf.Tensor: shape=(4,), dtype=float32, numpy=array([-5., -3., -3., -3.], dtype=float32)>

  The reduction version of this elementwise operation is `tf.math.reduce_min`

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Minimum: Incomplete

def minimum_eager_fallback(x, y, name, ctx): ...
def mod(x, y, name: Incomplete | None = None):
    """Returns element-wise remainder of division. This emulates C semantics in that

  the result here is consistent with a truncating divide. E.g.
  `tf.truncatediv(x, y) * y + truncate_mod(x, y) = x`.

  *NOTE*: `Mod` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `int32`, `int64`, `half`, `half`, `bfloat16`, `float32`, `float64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Mod: Incomplete

def mod_eager_fallback(x, y, name, ctx): ...
def mul(x, y, name: Incomplete | None = None):
    """Returns x * y element-wise.

  *NOTE*: `Multiply` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `uint32`, `uint64`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Mul: Incomplete

def mul_eager_fallback(x, y, name, ctx): ...
def mul_no_nan(x, y, name: Incomplete | None = None):
    """Returns x * y element-wise. Returns zero if y is zero, even if x if infinite or NaN.

  *NOTE*: `MulNoNan` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

MulNoNan: Incomplete

def mul_no_nan_eager_fallback(x, y, name, ctx): ...
def ndtri(x, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Ndtri: Incomplete

def ndtri_eager_fallback(x, name, ctx): ...
def neg(x, name: Incomplete | None = None):
    """Computes numerical negative value element-wise.

  I.e., \\\\(y = -x\\\\).

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Neg: Incomplete

def neg_eager_fallback(x, name, ctx): ...
def next_after(x1, x2, name: Incomplete | None = None):
    """Returns the next representable value of `x1` in the direction of `x2`, element-wise.

  This operation returns the same result as the C++ std::nextafter function.

  It can also return a subnormal number.

  @compatibility(cpp)
  Equivalent to C++ std::nextafter function.
  @end_compatibility

  Args:
    x1: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    x2: A `Tensor`. Must have the same type as `x1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x1`.
  """

NextAfter: Incomplete

def next_after_eager_fallback(x1, x2, name, ctx): ...
def not_equal(x, y, incompatible_shape_error: bool = True, name: Incomplete | None = None):
    """Returns the truth value of (x != y) element-wise.

  *NOTE*: `NotEqual` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`.
    y: A `Tensor`. Must have the same type as `x`.
    incompatible_shape_error: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

NotEqual: Incomplete

def not_equal_eager_fallback(x, y, incompatible_shape_error, name, ctx): ...
def polygamma(a, x, name: Incomplete | None = None):
    """Compute the polygamma function \\\\(\\psi^{(n)}(x)\\\\).

  The polygamma function is defined as:


  \\\\(\\psi^{(a)}(x) = \\frac{d^a}{dx^a} \\psi(x)\\\\)

  where \\\\(\\psi(x)\\\\) is the digamma function.
  The polygamma function is defined only for non-negative integer orders \\\\a\\\\.

  Args:
    a: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    x: A `Tensor`. Must have the same type as `a`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

Polygamma: Incomplete

def polygamma_eager_fallback(a, x, name, ctx): ...

Pow: Incomplete

def prod(input, axis, keep_dims: bool = False, name: Incomplete | None = None):
    """Computes the product of elements across dimensions of a tensor.

  Reduces `input` along the dimensions given in `axis`. Unless
  `keep_dims` is true, the rank of the tensor is reduced by 1 for each entry in
  `axis`. If `keep_dims` is true, the reduced dimensions are
  retained with length 1.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      The tensor to reduce.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The dimensions to reduce. Must be in the range
      `[-rank(input), rank(input))`.
    keep_dims: An optional `bool`. Defaults to `False`.
      If true, retain reduced dimensions with length 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

Prod: Incomplete

def prod_eager_fallback(input, axis, keep_dims, name, ctx): ...

class _QuantizeDownAndShrinkRangeOutput(NamedTuple):
    output: Incomplete
    output_min: Incomplete
    output_max: Incomplete

def quantize_down_and_shrink_range(input, input_min, input_max, out_type, name: Incomplete | None = None):
    """Convert the quantized 'input' tensor into a lower-precision 'output', using the

  actual distribution of the values to maximize the usage of the lower bit depth
  and adjusting the output min and max ranges accordingly.

  [input_min, input_max] are scalar floats that specify the range for the float
  interpretation of the 'input' data. For example, if input_min is -1.0f and
  input_max is 1.0f, and we are dealing with quint16 quantized data, then a 0
  value in the 16-bit data should be interpreted as -1.0f, and a 65535 means 1.0f.

  This operator tries to squeeze as much precision as possible into an output with
  a lower bit depth by calculating the actual min and max values found in the
  data. For example, maybe that quint16 input has no values lower than 16,384 and
  none higher than 49,152. That means only half the range is actually needed, all
  the float interpretations are between -0.5f and 0.5f, so if we want to compress
  the data into a quint8 output, we can use that range rather than the theoretical
  -1.0f to 1.0f that is suggested by the input min and max.

  In practice, this is most useful for taking output from operations like
  QuantizedMatMul that can produce higher bit-depth outputs than their inputs and
  may have large potential output ranges, but in practice have a distribution of
  input values that only uses a small fraction of the possible range. By feeding
  that output into this operator, we can reduce it from 32 bits down to 8 with
  minimal loss of accuracy.

  Args:
    input: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
    input_min: A `Tensor` of type `float32`.
      The float value that the minimum quantized input value represents.
    input_max: A `Tensor` of type `float32`.
      The float value that the maximum quantized input value represents.
    out_type: A `tf.DType` from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`.
      The type of the output. Should be a lower bit depth than Tinput.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, output_min, output_max).

    output: A `Tensor` of type `out_type`.
    output_min: A `Tensor` of type `float32`.
    output_max: A `Tensor` of type `float32`.
  """

QuantizeDownAndShrinkRange: Incomplete

def quantize_down_and_shrink_range_eager_fallback(input, input_min, input_max, out_type, name, ctx): ...

class _QuantizedAddOutput(NamedTuple):
    z: Incomplete
    min_z: Incomplete
    max_z: Incomplete

def quantized_add(x, y, min_x, max_x, min_y, max_y, Toutput=..., name: Incomplete | None = None):
    """Returns x + y element-wise, working on quantized buffers.

  Args:
    x: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
    y: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
    min_x: A `Tensor` of type `float32`.
      The float value that the lowest quantized `x` value represents.
    max_x: A `Tensor` of type `float32`.
      The float value that the highest quantized `x` value represents.
    min_y: A `Tensor` of type `float32`.
      The float value that the lowest quantized `y` value represents.
    max_y: A `Tensor` of type `float32`.
      The float value that the highest quantized `y` value represents.
    Toutput: An optional `tf.DType` from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to `tf.qint32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (z, min_z, max_z).

    z: A `Tensor` of type `Toutput`.
    min_z: A `Tensor` of type `float32`.
    max_z: A `Tensor` of type `float32`.
  """

QuantizedAdd: Incomplete

def quantized_add_eager_fallback(x, y, min_x, max_x, min_y, max_y, Toutput, name, ctx): ...

class _QuantizedMatMulOutput(NamedTuple):
    out: Incomplete
    min_out: Incomplete
    max_out: Incomplete

def quantized_mat_mul(a, b, min_a, max_a, min_b, max_b, Toutput=..., transpose_a: bool = False, transpose_b: bool = False, Tactivation=..., name: Incomplete | None = None):
    """Perform a quantized matrix multiplication of  `a` by the matrix `b`.

  The inputs must be two-dimensional matrices and the inner dimension of
  `a` (after being transposed if `transpose_a` is non-zero) must match the
  outer dimension of `b` (after being transposed if `transposed_b` is
  non-zero).

  Args:
    a: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
      Must be a two-dimensional tensor.
    b: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
      Must be a two-dimensional tensor.
    min_a: A `Tensor` of type `float32`.
      The float value that the lowest quantized `a` value represents.
    max_a: A `Tensor` of type `float32`.
      The float value that the highest quantized `a` value represents.
    min_b: A `Tensor` of type `float32`.
      The float value that the lowest quantized `b` value represents.
    max_b: A `Tensor` of type `float32`.
      The float value that the highest quantized `b` value represents.
    Toutput: An optional `tf.DType` from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to `tf.qint32`.
    transpose_a: An optional `bool`. Defaults to `False`.
      If true, `a` is transposed before multiplication.
    transpose_b: An optional `bool`. Defaults to `False`.
      If true, `b` is transposed before multiplication.
    Tactivation: An optional `tf.DType` from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to `tf.quint8`.
      The type of output produced by activation function
      following this operation.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (out, min_out, max_out).

    out: A `Tensor` of type `Toutput`.
    min_out: A `Tensor` of type `float32`.
    max_out: A `Tensor` of type `float32`.
  """

QuantizedMatMul: Incomplete

def quantized_mat_mul_eager_fallback(a, b, min_a, max_a, min_b, max_b, Toutput, transpose_a, transpose_b, Tactivation, name, ctx): ...

class _QuantizedMulOutput(NamedTuple):
    z: Incomplete
    min_z: Incomplete
    max_z: Incomplete

def quantized_mul(x, y, min_x, max_x, min_y, max_y, Toutput=..., name: Incomplete | None = None):
    """Returns x * y element-wise, working on quantized buffers.

  Args:
    x: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
    y: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
    min_x: A `Tensor` of type `float32`.
      The float value that the lowest quantized `x` value represents.
    max_x: A `Tensor` of type `float32`.
      The float value that the highest quantized `x` value represents.
    min_y: A `Tensor` of type `float32`.
      The float value that the lowest quantized `y` value represents.
    max_y: A `Tensor` of type `float32`.
      The float value that the highest quantized `y` value represents.
    Toutput: An optional `tf.DType` from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to `tf.qint32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (z, min_z, max_z).

    z: A `Tensor` of type `Toutput`.
    min_z: A `Tensor` of type `float32`.
    max_z: A `Tensor` of type `float32`.
  """

QuantizedMul: Incomplete

def quantized_mul_eager_fallback(x, y, min_x, max_x, min_y, max_y, Toutput, name, ctx): ...
def ragged_bincount(splits, values, size, weights, binary_output: bool = False, name: Incomplete | None = None):
    """Counts the number of occurrences of each value in an integer array.

  Outputs a vector with length `size` and the same dtype as `weights`. If
  `weights` are empty, then index `i` stores the number of times the value `i` is
  counted in `arr`. If `weights` are non-empty, then index `i` stores the sum of
  the value in `weights` at each index where the corresponding value in `arr` is
  `i`.

  Values in `arr` outside of the range [0, size) are ignored.

  Args:
    splits: A `Tensor` of type `int64`. 1D int64 `Tensor`.
    values: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      2D int `Tensor`.
    size: A `Tensor`. Must have the same type as `values`.
      non-negative int scalar `Tensor`.
    weights: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      is an int32, int64, float32, or float64 `Tensor` with the same
      shape as `input`, or a length-0 `Tensor`, in which case it acts as all weights
      equal to 1.
    binary_output: An optional `bool`. Defaults to `False`.
      bool; Whether the kernel should count the appearance or number of occurrences.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `weights`.
  """

RaggedBincount: Incomplete

def ragged_bincount_eager_fallback(splits, values, size, weights, binary_output, name, ctx): ...

Range: Incomplete

def real(input, Tout=..., name: Incomplete | None = None):
    """Returns the real part of a complex number.

  Given a tensor `input` of complex numbers, this operation returns a tensor of
  type `float` that is the real part of each element in `input`. All elements in
  `input` must be complex numbers of the form \\\\(a + bj\\\\), where *a* is the real
   part returned by this operation and *b* is the imaginary part.

  For example:

  ```
  # tensor 'input' is [-2.25 + 4.75j, 3.25 + 5.75j]
  tf.real(input) ==> [-2.25, 3.25]
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
    Tout: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

Real: Incomplete

def real_eager_fallback(input, Tout, name, ctx): ...
def real_div(x, y, name: Incomplete | None = None):
    """Returns x / y element-wise for real types.

  If `x` and `y` are reals, this will return the floating-point division.

  *NOTE*: `Div` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `uint32`, `uint64`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

RealDiv: Incomplete

def real_div_eager_fallback(x, y, name, ctx): ...
def reciprocal(x, name: Incomplete | None = None):
    """Computes the reciprocal of x element-wise.

  I.e., \\\\(y = 1 / x\\\\).

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Reciprocal: Incomplete

def reciprocal_eager_fallback(x, name, ctx): ...
def reciprocal_grad(y, dy, name: Incomplete | None = None):
    """Computes the gradient for the inverse of `x` wrt its input.

  Specifically, `grad = -dy * y*y`, where `y = 1/x`, and `dy`
  is the corresponding input gradient.

  Args:
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    dy: A `Tensor`. Must have the same type as `y`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `y`.
  """

ReciprocalGrad: Incomplete

def reciprocal_grad_eager_fallback(y, dy, name, ctx): ...

class _RequantizationRangeOutput(NamedTuple):
    output_min: Incomplete
    output_max: Incomplete

def requantization_range(input, input_min, input_max, name: Incomplete | None = None):
    """Computes a range that covers the actual values present in a quantized tensor.

  Given a quantized tensor described by `(input, input_min, input_max)`, outputs a
  range that covers the actual values present in that tensor. This op is typically
  used to produce the `requested_output_min` and `requested_output_max` for
  `Requantize`.

  Args:
    input: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
    input_min: A `Tensor` of type `float32`.
      The float value that the minimum quantized input value represents.
    input_max: A `Tensor` of type `float32`.
      The float value that the maximum quantized input value represents.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_min, output_max).

    output_min: A `Tensor` of type `float32`.
    output_max: A `Tensor` of type `float32`.
  """

RequantizationRange: Incomplete

def requantization_range_eager_fallback(input, input_min, input_max, name, ctx): ...

class _RequantizationRangePerChannelOutput(NamedTuple):
    output_min: Incomplete
    output_max: Incomplete

def requantization_range_per_channel(input, input_min, input_max, clip_value_max, name: Incomplete | None = None):
    """Computes requantization range per channel.

  Args:
    input: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
      The original input tensor.
    input_min: A `Tensor` of type `float32`.
      The minimum value of the input tensor
    input_max: A `Tensor` of type `float32`.
      The maximum value of the input tensor.
    clip_value_max: A `float`.
      The maximum value of the output that needs to be clipped.
      Example: set this to 6 for Relu6.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_min, output_max).

    output_min: A `Tensor` of type `float32`.
    output_max: A `Tensor` of type `float32`.
  """

RequantizationRangePerChannel: Incomplete

def requantization_range_per_channel_eager_fallback(input, input_min, input_max, clip_value_max, name, ctx): ...

class _RequantizeOutput(NamedTuple):
    output: Incomplete
    output_min: Incomplete
    output_max: Incomplete

def requantize(input, input_min, input_max, requested_output_min, requested_output_max, out_type, name: Incomplete | None = None):
    """Converts the quantized `input` tensor into a lower-precision `output`.

  Converts the quantized `input` tensor into a lower-precision `output`, using the
  output range specified with `requested_output_min` and `requested_output_max`.

  `[input_min, input_max]` are scalar floats that specify the range for the float
  interpretation of the `input` data. For example, if `input_min` is -1.0f and
  `input_max` is 1.0f, and we are dealing with `quint16` quantized data, then a 0
  value in the 16-bit data should be interpreted as -1.0f, and a 65535 means 1.0f.

  Args:
    input: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
    input_min: A `Tensor` of type `float32`.
      The float value that the minimum quantized input value represents.
    input_max: A `Tensor` of type `float32`.
      The float value that the maximum quantized input value represents.
    requested_output_min: A `Tensor` of type `float32`.
      The float value that the minimum quantized output value represents.
    requested_output_max: A `Tensor` of type `float32`.
      The float value that the maximum quantized output value represents.
    out_type: A `tf.DType` from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`.
      The type of the output. Should be a lower bit depth than Tinput.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, output_min, output_max).

    output: A `Tensor` of type `out_type`.
    output_min: A `Tensor` of type `float32`.
    output_max: A `Tensor` of type `float32`.
  """

Requantize: Incomplete

def requantize_eager_fallback(input, input_min, input_max, requested_output_min, requested_output_max, out_type, name, ctx): ...

class _RequantizePerChannelOutput(NamedTuple):
    output: Incomplete
    output_min: Incomplete
    output_max: Incomplete

def requantize_per_channel(input, input_min, input_max, requested_output_min, requested_output_max, out_type=..., name: Incomplete | None = None):
    """Requantizes input with min and max values known per channel.

  Args:
    input: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
      The original input tensor.
    input_min: A `Tensor` of type `float32`.
      The minimum value of the input tensor
    input_max: A `Tensor` of type `float32`.
      The maximum value of the input tensor.
    requested_output_min: A `Tensor` of type `float32`.
      The minimum value of the output tensor requested.
    requested_output_max: A `Tensor` of type `float32`.
      The maximum value of the output tensor requested.
    out_type: An optional `tf.DType` from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to `tf.quint8`.
      The quantized type of output tensor that needs to be converted.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, output_min, output_max).

    output: A `Tensor` of type `out_type`.
    output_min: A `Tensor` of type `float32`.
    output_max: A `Tensor` of type `float32`.
  """

RequantizePerChannel: Incomplete

def requantize_per_channel_eager_fallback(input, input_min, input_max, requested_output_min, requested_output_max, out_type, name, ctx): ...
def rint(x, name: Incomplete | None = None):
    """Returns element-wise integer closest to x.

  If the result is midway between two representable values,
  the even representable is chosen.
  For example:

  ```
  rint(-1.5) ==> -2.0
  rint(0.5000001) ==> 1.0
  rint([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]) ==> [-2., -2., -0., 0., 2., 2., 2.]
  ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Rint: Incomplete

def rint_eager_fallback(x, name, ctx): ...
def round(x, name: Incomplete | None = None):
    """Rounds the values of a tensor to the nearest integer, element-wise.

  Rounds half to even.  Also known as bankers rounding. If you want to round
  according to the current system rounding mode use std::cint.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Round: Incomplete

def round_eager_fallback(x, name, ctx): ...
def rsqrt(x, name: Incomplete | None = None):
    """Computes reciprocal of square root of x element-wise.

  I.e., \\\\(y = 1 / \\sqrt{x}\\\\).

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Rsqrt: Incomplete

def rsqrt_eager_fallback(x, name, ctx): ...
def rsqrt_grad(y, dy, name: Incomplete | None = None):
    """Computes the gradient for the rsqrt of `x` wrt its input.

  Specifically, `grad = dy * -0.5 * y^3`, where `y = rsqrt(x)`, and `dy`
  is the corresponding input gradient.

  Args:
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    dy: A `Tensor`. Must have the same type as `y`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `y`.
  """

RsqrtGrad: Incomplete

def rsqrt_grad_eager_fallback(y, dy, name, ctx): ...
def segment_max(data, segment_ids, name: Incomplete | None = None):
    '''Computes the maximum along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output_i = \\max_j(data_j)\\\\) where `max` is over `j` such
  that `segment_ids[j] == i`.

  If the max is empty for a given segment ID `i`, `output[i] = 0`.

  Caution: On CPU, values in `segment_ids` are always validated to be sorted,
  and an error is thrown for indices that are not increasing. On GPU, this
  does not throw an error for unsorted indices. On GPU, out-of-order indices
  result in safe but unspecified behavior, which may include treating
  out-of-order indices as the same as a smaller following index.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/SegmentMax.png" alt>
  </div>

  For example:

  >>> c = tf.constant([[1,2,3,4], [4, 3, 2, 1], [5,6,7,8]])
  >>> tf.math.segment_max(c, tf.constant([0, 0, 1])).numpy()
  array([[4, 3, 3, 4],
         [5, 6, 7, 8]], dtype=int32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor whose size is equal to the size of `data`\'s
      first dimension.  Values should be sorted and can be repeated.

      Caution: The values are always validated to be sorted on CPU, never validated
      on GPU.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  '''

SegmentMax: Incomplete

def segment_max_eager_fallback(data, segment_ids, name, ctx): ...
def segment_mean(data, segment_ids, name: Incomplete | None = None):
    '''Computes the mean along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output_i = \\frac{\\sum_j data_j}{N}\\\\) where `mean` is
  over `j` such that `segment_ids[j] == i` and `N` is the total number of
  values summed.

  If the mean is empty for a given segment ID `i`, `output[i] = 0`.

  Caution: On CPU, values in `segment_ids` are always validated to be sorted,
  and an error is thrown for indices that are not increasing. On GPU, this
  does not throw an error for unsorted indices. On GPU, out-of-order indices
  result in safe but unspecified behavior, which may include treating
  out-of-order indices as a smaller following index when computing the numerator
  of the mean.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/SegmentMean.png" alt>
  </div>

  For example:

  >>> c = tf.constant([[1.0,2,3,4], [4, 3, 2, 1], [5,6,7,8]])
  >>> tf.math.segment_mean(c, tf.constant([0, 0, 1])).numpy()
  array([[2.5, 2.5, 2.5, 2.5],
         [5., 6., 7., 8.]], dtype=float32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor whose size is equal to the size of `data`\'s
      first dimension.  Values should be sorted and can be repeated.

      Caution: The values are always validated to be sorted on CPU, never validated
      on GPU.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  '''

SegmentMean: Incomplete

def segment_mean_eager_fallback(data, segment_ids, name, ctx): ...
def segment_min(data, segment_ids, name: Incomplete | None = None):
    '''Computes the minimum along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output_i = \\min_j(data_j)\\\\) where `min` is over `j` such
  that `segment_ids[j] == i`.

  If the min is empty for a given segment ID `i`, `output[i] = 0`.

  Caution: On CPU, values in `segment_ids` are always validated to be sorted,
  and an error is thrown for indices that are not increasing. On GPU, this
  does not throw an error for unsorted indices. On GPU, out-of-order indices
  result in safe but unspecified behavior, which may include treating
  out-of-order indices as the same as a smaller following index.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/SegmentMin.png" alt>
  </div>

  For example:

  >>> c = tf.constant([[1,2,3,4], [4, 3, 2, 1], [5,6,7,8]])
  >>> tf.math.segment_min(c, tf.constant([0, 0, 1])).numpy()
  array([[1, 2, 2, 1],
         [5, 6, 7, 8]], dtype=int32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor whose size is equal to the size of `data`\'s
      first dimension.  Values should be sorted and can be repeated.

      Caution: The values are always validated to be sorted on CPU, never validated
      on GPU.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  '''

SegmentMin: Incomplete

def segment_min_eager_fallback(data, segment_ids, name, ctx): ...
def segment_prod(data, segment_ids, name: Incomplete | None = None):
    '''Computes the product along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output_i = \\prod_j data_j\\\\) where the product is over `j` such
  that `segment_ids[j] == i`.

  If the product is empty for a given segment ID `i`, `output[i] = 1`.

  Caution: On CPU, values in `segment_ids` are always validated to be sorted,
  and an error is thrown for indices that are not increasing. On GPU, this
  does not throw an error for unsorted indices. On GPU, out-of-order indices
  result in safe but unspecified behavior, which may include treating
  out-of-order indices as the same as a smaller following index.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/SegmentProd.png" alt>
  </div>

  For example:

  >>> c = tf.constant([[1,2,3,4], [4, 3, 2, 1], [5,6,7,8]])
  >>> tf.math.segment_prod(c, tf.constant([0, 0, 1])).numpy()
  array([[4, 6, 6, 4],
         [5, 6, 7, 8]], dtype=int32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor whose size is equal to the size of `data`\'s
      first dimension.  Values should be sorted and can be repeated.

      Caution: The values are always validated to be sorted on CPU, never validated
      on GPU.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  '''

SegmentProd: Incomplete

def segment_prod_eager_fallback(data, segment_ids, name, ctx): ...
def segment_prod_v2(data, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the product along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output_i = \\prod_j data_j\\\\) where the product is over `j` such
  that `segment_ids[j] == i`.

  If the product is empty for a given segment ID `i`, `output[i] = 1`.

  Note: That this op is currently only supported with jit_compile=True.

  The only difference with SegmentProd is the additional input  `num_segments`.
  This helps in evaluating the output shape in compile time.
  `num_segments` should be consistent with segment_ids.
  e.g. Max(segment_ids) - 1 should be equal to `num_segments` for a 1-d segment_ids
  With inconsistent num_segments, the op still runs. only difference is, 
  the output takes the size of num_segments irrespective of size of segment_ids and data.
  for num_segments less than expected output size, the last elements are ignored
  for num_segments more than the expected output size, last elements are assigned 1.

  For example:

  >>> @tf.function(jit_compile=True)
  ... def test(c):
  ...   return tf.raw_ops.SegmentProdV2(data=c, segment_ids=tf.constant([0, 0, 1]), num_segments=2)
  >>> c = tf.constant([[1,2,3,4], [4, 3, 2, 1], [5,6,7,8]])
  >>> test(c).numpy()
  array([[4, 6, 6, 4],
         [5, 6, 7, 8]], dtype=int32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor whose size is equal to the size of `data`'s
      first dimension.  Values should be sorted and can be repeated.
      The values must be less than `num_segments`.

      Caution: The values are always validated to be sorted on CPU, never validated
      on GPU.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SegmentProdV2: Incomplete

def segment_prod_v2_eager_fallback(data, segment_ids, num_segments, name, ctx): ...
def segment_sum(data, segment_ids, name: Incomplete | None = None):
    '''Computes the sum along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output_i = \\sum_j data_j\\\\) where sum is over `j` such
  that `segment_ids[j] == i`.

  If the sum is empty for a given segment ID `i`, `output[i] = 0`.

  Caution: On CPU, values in `segment_ids` are always validated to be sorted,
  and an error is thrown for indices that are not increasing. On GPU, this
  does not throw an error for unsorted indices. On GPU, out-of-order indices
  result in safe but unspecified behavior, which may include treating
  out-of-order indices as the same as a smaller following index.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/SegmentSum.png" alt>
  </div>

  For example:

  >>> c = tf.constant([[1,2,3,4], [4, 3, 2, 1], [5,6,7,8]])
  >>> tf.math.segment_sum(c, tf.constant([0, 0, 1])).numpy()
  array([[5, 5, 5, 5],
         [5, 6, 7, 8]], dtype=int32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor whose size is equal to the size of `data`\'s
      first dimension.  Values should be sorted and can be repeated.

      Caution: The values are always validated to be sorted on CPU, never validated
      on GPU.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  '''

SegmentSum: Incomplete

def segment_sum_eager_fallback(data, segment_ids, name, ctx): ...
def segment_sum_v2(data, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the sum along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output_i = \\sum_j data_j\\\\) where sum is over `j` such
  that `segment_ids[j] == i`.

  If the sum is empty for a given segment ID `i`, `output[i] = 0`.

  Note that this op is currently only supported with jit_compile=True.
  </div>

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor whose size is equal to the size of `data`'s
      first dimension.  Values should be sorted and can be repeated.
      The values must be less than `num_segments`.

      Caution: The values are always validated to be sorted on CPU, never validated
      on GPU.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SegmentSumV2: Incomplete

def segment_sum_v2_eager_fallback(data, segment_ids, num_segments, name, ctx): ...
def select(condition, x, y, name: Incomplete | None = None):
    """Selects elements from `x` or `y`, depending on `condition`.

  The `x`, and `y` tensors must all have the same shape, and the
  output will also have that shape.

  The `condition` tensor must be a scalar if `x` and `y` are scalars.
  If `x` and `y` are vectors or higher rank, then `condition` must be either a
  scalar, a vector with size matching the first dimension of `x`, or must have
  the same shape as `x`.

  The `condition` tensor acts as a mask that chooses, based on the value at each
  element, whether the corresponding element / row in the output should be
  taken from `x` (if true) or `y` (if false).

  If `condition` is a vector and `x` and `y` are higher rank matrices, then
  it chooses which row (outer dimension) to copy from `x` and `y`.
  If `condition` has the same shape as `x` and `y`, then it chooses which
  element to copy from `x` and `y`.

  For example:

  ```python
  # 'condition' tensor is [[True,  False]
  #                        [False, True]]
  # 't' is [[1, 2],
  #         [3, 4]]
  # 'e' is [[5, 6],
  #         [7, 8]]
  select(condition, t, e)  # => [[1, 6], [7, 4]]


  # 'condition' tensor is [True, False]
  # 't' is [[1, 2],
  #         [3, 4]]
  # 'e' is [[5, 6],
  #         [7, 8]]
  select(condition, t, e) ==> [[1, 2],
                               [7, 8]]

  ```

  Args:
    condition: A `Tensor` of type `bool`.
    x:  A `Tensor` which may have the same shape as `condition`.
      If `condition` is rank 1, `x` may have higher rank,
      but its first dimension must match the size of `condition`.
    y:  A `Tensor` with the same type and shape as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `t`.
  """

Select: Incomplete

def select_eager_fallback(condition, x, y, name, ctx): ...
def select_v2(condition, t, e, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    condition: A `Tensor` of type `bool`.
    t: A `Tensor`.
    e: A `Tensor`. Must have the same type as `t`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `t`.
  """

SelectV2: Incomplete

def select_v2_eager_fallback(condition, t, e, name, ctx): ...
def sigmoid(x, name: Incomplete | None = None):
    """Computes sigmoid of `x` element-wise.

  Specifically, `y = 1 / (1 + exp(-x))`.

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Sigmoid: Incomplete

def sigmoid_eager_fallback(x, name, ctx): ...
def sigmoid_grad(y, dy, name: Incomplete | None = None):
    """Computes the gradient of the sigmoid of `x` wrt its input.

  Specifically, `grad = dy * y * (1 - y)`, where `y = sigmoid(x)`, and
  `dy` is the corresponding input gradient.

  Args:
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    dy: A `Tensor`. Must have the same type as `y`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `y`.
  """

SigmoidGrad: Incomplete

def sigmoid_grad_eager_fallback(y, dy, name, ctx): ...
def sign(x, name: Incomplete | None = None):
    """Returns an element-wise indication of the sign of a number.

  `y = sign(x) = -1` if `x < 0`; 0 if `x == 0`; 1 if `x > 0`.

  For complex numbers, `y = sign(x) = x / |x|` if `x != 0`, otherwise `y = 0`.

  Example usage:
  >>> tf.math.sign([0., 2., -3.])
  <tf.Tensor: shape=(3,), dtype=float32, numpy=array([ 0.,  1., -1.], dtype=float32)>

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Sign: Incomplete

def sign_eager_fallback(x, name, ctx): ...
def sin(x, name: Incomplete | None = None):
    '''Computes sine of x element-wise.

    Given an input tensor, this function computes sine of every
    element in the tensor. Input range is `(-inf, inf)` and
    output range is `[-1,1]`.

    ```python
    x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10, float("inf")])
    tf.math.sin(x) ==> [nan -0.4121185 -0.47942555 0.84147096 0.9320391 -0.87329733 -0.54402107 nan]
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Sin: Incomplete

def sin_eager_fallback(x, name, ctx): ...
def sinh(x, name: Incomplete | None = None):
    '''Computes hyperbolic sine of x element-wise.

    Given an input tensor, this function computes hyperbolic sine of every
    element in the tensor. Input range is `[-inf,inf]` and output range
    is `[-inf,inf]`.

    ```python
    x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 2, 10, float("inf")])
    tf.math.sinh(x) ==> [-inf -4.0515420e+03 -5.2109528e-01 1.1752012e+00 1.5094614e+00 3.6268604e+00 1.1013232e+04 inf]
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Sinh: Incomplete

def sinh_eager_fallback(x, name, ctx): ...
def sobol_sample(dim, num_results, skip, dtype=..., name: Incomplete | None = None):
    """Generates points from the Sobol sequence.

  Creates a Sobol sequence with `num_results` samples. Each sample has dimension
  `dim`. Skips the first `skip` samples.

  Args:
    dim: A `Tensor` of type `int32`.
      Positive scalar `Tensor` representing each sample's dimension.
    num_results: A `Tensor` of type `int32`.
      Positive scalar `Tensor` of dtype int32. The number of Sobol points to return
      in the output.
    skip: A `Tensor` of type `int32`.
      Positive scalar `Tensor` of dtype int32. The number of initial points of the
      Sobol sequence to skip.
    dtype: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
      The type of the sample. One of: `float32` or `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

SobolSample: Incomplete

def sobol_sample_eager_fallback(dim, num_results, skip, dtype, name, ctx): ...
def sparse_bincount(indices, values, dense_shape, size, weights, binary_output: bool = False, name: Incomplete | None = None):
    """Counts the number of occurrences of each value in an integer array.

  Outputs a vector with length `size` and the same dtype as `weights`. If
  `weights` are empty, then index `i` stores the number of times the value `i` is
  counted in `arr`. If `weights` are non-empty, then index `i` stores the sum of
  the value in `weights` at each index where the corresponding value in `arr` is
  `i`.

  Values in `arr` outside of the range [0, size) are ignored.

  Args:
    indices: A `Tensor` of type `int64`. 2D int64 `Tensor`.
    values: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      1D int `Tensor`.
    dense_shape: A `Tensor` of type `int64`. 1D int64 `Tensor`.
    size: A `Tensor`. Must have the same type as `values`.
      non-negative int scalar `Tensor`.
    weights: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      is an int32, int64, float32, or float64 `Tensor` with the same
      shape as `input`, or a length-0 `Tensor`, in which case it acts as all weights
      equal to 1.
    binary_output: An optional `bool`. Defaults to `False`.
      bool; Whether the kernel should count the appearance or number of occurrences.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `weights`.
  """

SparseBincount: Incomplete

def sparse_bincount_eager_fallback(indices, values, dense_shape, size, weights, binary_output, name, ctx): ...
def sparse_mat_mul(a, b, transpose_a: bool = False, transpose_b: bool = False, a_is_sparse: bool = False, b_is_sparse: bool = False, name: Incomplete | None = None):
    '''Multiply matrix "a" by matrix "b".

  The inputs must be two-dimensional matrices and the inner dimension of "a" must
  match the outer dimension of "b". Both "a" and "b" must be `Tensor`s not
  `SparseTensor`s.  This op is optimized for the case where at least one of "a" or
  "b" is sparse, in the sense that they have a large proportion of zero values.
  The breakeven for using this versus a dense matrix multiply on one platform was
  30% zero values in the sparse matrix.

  The gradient computation of this operation will only take advantage of sparsity
  in the input gradient when that gradient comes from a Relu.

  Args:
    a: A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
    b: A `Tensor`. Must be one of the following types: `float32`, `bfloat16`.
    transpose_a: An optional `bool`. Defaults to `False`.
    transpose_b: An optional `bool`. Defaults to `False`.
    a_is_sparse: An optional `bool`. Defaults to `False`.
    b_is_sparse: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  '''

SparseMatMul: Incomplete

def sparse_mat_mul_eager_fallback(a, b, transpose_a, transpose_b, a_is_sparse, b_is_sparse, name, ctx): ...
def sparse_segment_mean(data, indices, segment_ids, name: Incomplete | None = None):
    """Computes the mean along sparse segments of a tensor.

  See `tf.sparse.segment_sum` for usage examples.

  Like `SegmentMean`, but `segment_ids` can have rank less than `data`'s first
  dimension, selecting a subset of dimension 0, specified by `indices`.

  Args:
    data: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Has same rank as `segment_ids`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Values should be sorted and can be repeated.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SparseSegmentMean: Incomplete

def sparse_segment_mean_eager_fallback(data, indices, segment_ids, name, ctx): ...
def sparse_segment_mean_grad(grad, indices, segment_ids, output_dim0, name: Incomplete | None = None):
    '''Computes gradients for SparseSegmentMean.

  Returns tensor "output" with same shape as grad, except for dimension 0 whose
  value is output_dim0.

  Args:
    grad: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
      gradient propagated to the SparseSegmentMean op.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      indices passed to the corresponding SparseSegmentMean op.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      segment_ids passed to the corresponding SparseSegmentMean op.
    output_dim0: A `Tensor` of type `int32`.
      dimension 0 of "data" passed to SparseSegmentMean op.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `grad`.
  '''

SparseSegmentMeanGrad: Incomplete

def sparse_segment_mean_grad_eager_fallback(grad, indices, segment_ids, output_dim0, name, ctx): ...
def sparse_segment_mean_with_num_segments(data, indices, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the mean along sparse segments of a tensor.

  Like `SparseSegmentMean`, but allows missing ids in `segment_ids`. If an id is
  missing, the `output` tensor at that position will be zeroed.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Args:
    data: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Has same rank as `segment_ids`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Values should be sorted and can be repeated.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Should equal the number of distinct segment IDs.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SparseSegmentMeanWithNumSegments: Incomplete

def sparse_segment_mean_with_num_segments_eager_fallback(data, indices, segment_ids, num_segments, name, ctx): ...
def sparse_segment_sqrt_n(data, indices, segment_ids, name: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor divided by the sqrt of N.

  N is the size of the segment being reduced.

  See `tf.sparse.segment_sum` for usage examples.

  Args:
    data: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Has same rank as `segment_ids`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Values should be sorted and can be repeated.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SparseSegmentSqrtN: Incomplete

def sparse_segment_sqrt_n_eager_fallback(data, indices, segment_ids, name, ctx): ...
def sparse_segment_sqrt_n_grad(grad, indices, segment_ids, output_dim0, name: Incomplete | None = None):
    '''Computes gradients for SparseSegmentSqrtN.

  Returns tensor "output" with same shape as grad, except for dimension 0 whose
  value is output_dim0.

  Args:
    grad: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
      gradient propagated to the SparseSegmentSqrtN op.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      indices passed to the corresponding SparseSegmentSqrtN op.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      segment_ids passed to the corresponding SparseSegmentSqrtN op.
    output_dim0: A `Tensor` of type `int32`.
      dimension 0 of "data" passed to SparseSegmentSqrtN op.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `grad`.
  '''

SparseSegmentSqrtNGrad: Incomplete

def sparse_segment_sqrt_n_grad_eager_fallback(grad, indices, segment_ids, output_dim0, name, ctx): ...
def sparse_segment_sqrt_n_with_num_segments(data, indices, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor divided by the sqrt of N.

  N is the size of the segment being reduced.

  Like `SparseSegmentSqrtN`, but allows missing ids in `segment_ids`. If an id is
  missing, the `output` tensor at that position will be zeroed.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Args:
    data: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Has same rank as `segment_ids`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Values should be sorted and can be repeated.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Should equal the number of distinct segment IDs.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SparseSegmentSqrtNWithNumSegments: Incomplete

def sparse_segment_sqrt_n_with_num_segments_eager_fallback(data, indices, segment_ids, num_segments, name, ctx): ...
def sparse_segment_sum(data, indices, segment_ids, name: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Like `SegmentSum`, but `segment_ids` can have rank less than `data`'s first
  dimension, selecting a subset of dimension 0, specified by `indices`.

  For example:

  ```python
  c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])

  # Select two rows, one segment.
  tf.sparse_segment_sum(c, tf.constant([0, 1]), tf.constant([0, 0]))
  # => [[0 0 0 0]]

  # Select two rows, two segment.
  tf.sparse_segment_sum(c, tf.constant([0, 1]), tf.constant([0, 1]))
  # => [[ 1  2  3  4]
  #     [-1 -2 -3 -4]]

  # Select all rows, two segments.
  tf.sparse_segment_sum(c, tf.constant([0, 1, 2]), tf.constant([0, 0, 1]))
  # => [[0 0 0 0]
  #     [5 6 7 8]]

  # Which is equivalent to:
  tf.segment_sum(c, tf.constant([0, 0, 1]))
  ```

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Has same rank as `segment_ids`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Values should be sorted and can be repeated.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SparseSegmentSum: Incomplete

def sparse_segment_sum_eager_fallback(data, indices, segment_ids, name, ctx): ...
def sparse_segment_sum_grad(grad, indices, segment_ids, output_dim0, name: Incomplete | None = None):
    '''Computes gradients for SparseSegmentSum.

  Returns tensor "output" with same shape as grad, except for dimension 0 whose
  value is output_dim0.

  Args:
    grad: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
      gradient propagated to the SparseSegmentSum op.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      indices passed to the corresponding SparseSegmentSum op.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      segment_ids passed to the corresponding SparseSegmentSum op.
    output_dim0: A `Tensor` of type `int32`.
      dimension 0 of "data" passed to SparseSegmentSum op.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `grad`.
  '''

SparseSegmentSumGrad: Incomplete

def sparse_segment_sum_grad_eager_fallback(grad, indices, segment_ids, output_dim0, name, ctx): ...
def sparse_segment_sum_with_num_segments(data, indices, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the sum along sparse segments of a tensor.

  Like `SparseSegmentSum`, but allows missing ids in `segment_ids`. If an id is
  missing, the `output` tensor at that position will be zeroed.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/sparse#Segmentation)
  for an explanation of segments.

  For example:

  ```python
  c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])

  tf.sparse_segment_sum_with_num_segments(
      c, tf.constant([0, 1]), tf.constant([0, 0]), num_segments=3)
  # => [[0 0 0 0]
  #     [0 0 0 0]
  #     [0 0 0 0]]

  tf.sparse_segment_sum_with_num_segments(c,
                                          tf.constant([0, 1]),
                                          tf.constant([0, 2],
                                          num_segments=4))
  # => [[ 1  2  3  4]
  #     [ 0  0  0  0]
  #     [-1 -2 -3 -4]
  #     [ 0  0  0  0]]
  ```

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Has same rank as `segment_ids`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A 1-D tensor. Values should be sorted and can be repeated.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Should equal the number of distinct segment IDs.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

SparseSegmentSumWithNumSegments: Incomplete

def sparse_segment_sum_with_num_segments_eager_fallback(data, indices, segment_ids, num_segments, name, ctx): ...
def sqrt(x, name: Incomplete | None = None):
    """Computes square root of x element-wise.

  I.e., \\\\(y = \\sqrt{x} = x^{1/2}\\\\).

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Sqrt: Incomplete

def sqrt_eager_fallback(x, name, ctx): ...
def sqrt_grad(y, dy, name: Incomplete | None = None):
    """Computes the gradient for the sqrt of `x` wrt its input.

  Specifically, `grad = dy * 0.5 / y`, where `y = sqrt(x)`, and `dy`
  is the corresponding input gradient.

  Args:
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    dy: A `Tensor`. Must have the same type as `y`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `y`.
  """

SqrtGrad: Incomplete

def sqrt_grad_eager_fallback(y, dy, name, ctx): ...
def square(x, name: Incomplete | None = None):
    """Computes square of x element-wise.

  I.e., \\\\(y = x * x = x^2\\\\).

  >>> tf.math.square([-2., 0., 3.])
  <tf.Tensor: shape=(3,), dtype=float32, numpy=array([4., 0., 9.], dtype=float32)>

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Square: Incomplete

def square_eager_fallback(x, name, ctx): ...
def squared_difference(x, y, name: Incomplete | None = None):
    """Returns conj(x - y)(x - y) element-wise.

  *NOTE*: `math.squared_difference` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

SquaredDifference: Incomplete

def squared_difference_eager_fallback(x, y, name, ctx): ...
def sub(x, y, name: Incomplete | None = None):
    """Returns x - y element-wise.

  *NOTE*: `tf.subtract` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Both input and output have a range `(-inf, inf)`.

  Example usages below.

  Subtract operation between an array and a scalar:

  >>> x = [1, 2, 3, 4, 5]
  >>> y = 1
  >>> tf.subtract(x, y)
  <tf.Tensor: shape=(5,), dtype=int32, numpy=array([0, 1, 2, 3, 4], dtype=int32)>
  >>> tf.subtract(y, x)
  <tf.Tensor: shape=(5,), dtype=int32,
  numpy=array([ 0, -1, -2, -3, -4], dtype=int32)>

  Note that binary `-` operator can be used instead:

  >>> x = tf.convert_to_tensor([1, 2, 3, 4, 5])
  >>> y = tf.convert_to_tensor(1)
  >>> x - y
  <tf.Tensor: shape=(5,), dtype=int32, numpy=array([0, 1, 2, 3, 4], dtype=int32)>

  Subtract operation between an array and a tensor of same shape:

  >>> x = [1, 2, 3, 4, 5]
  >>> y = tf.constant([5, 4, 3, 2, 1])
  >>> tf.subtract(y, x)
  <tf.Tensor: shape=(5,), dtype=int32,
  numpy=array([ 4,  2,  0, -2, -4], dtype=int32)>

  **Warning**: If one of the inputs (`x` or `y`) is a tensor and the other is a
  non-tensor, the non-tensor input will adopt (or get casted to) the data type
  of the tensor input. This can potentially cause unwanted overflow or underflow
  conversion.

  For example,

  >>> x = tf.constant([1, 2], dtype=tf.int8)
  >>> y = [2**8 + 1, 2**8 + 2]
  >>> tf.subtract(x, y)
  <tf.Tensor: shape=(2,), dtype=int8, numpy=array([0, 0], dtype=int8)>

  When subtracting two input values of different shapes, `tf.subtract` follows the
  [general broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html#general-broadcasting-rules)
  . The two input array shapes are compared element-wise. Starting with the
  trailing dimensions, the two dimensions either have to be equal or one of them
  needs to be `1`.

  For example,

  >>> x = np.ones(6).reshape(2, 3, 1)
  >>> y = np.ones(6).reshape(2, 1, 3)
  >>> tf.subtract(x, y)
  <tf.Tensor: shape=(2, 3, 3), dtype=float64, numpy=
  array([[[0., 0., 0.],
          [0., 0., 0.],
          [0., 0., 0.]],
         [[0., 0., 0.],
          [0., 0., 0.],
          [0., 0., 0.]]])>

  Example with inputs of different dimensions:

  >>> x = np.ones(6).reshape(2, 3, 1)
  >>> y = np.ones(6).reshape(1, 6)
  >>> tf.subtract(x, y)
  <tf.Tensor: shape=(2, 3, 6), dtype=float64, numpy=
  array([[[0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0.]],
         [[0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0.]]])>

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `uint32`, `uint64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Sub: Incomplete

def sub_eager_fallback(x, y, name, ctx): ...

Sum: Incomplete

def tan(x, name: Incomplete | None = None):
    '''Computes tan of x element-wise.

    Given an input tensor, this function computes tangent of every
    element in the tensor. Input range is `(-inf, inf)` and
    output range is `(-inf, inf)`. If input lies outside the boundary, `nan`
    is returned.

    ```python
    x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10000, float("inf")])
    tf.math.tan(x) ==> [nan 0.45231566 -0.5463025 1.5574077 2.572152 -1.7925274 0.32097113 nan]
    ```

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Tan: Incomplete

def tan_eager_fallback(x, name, ctx): ...
def tanh(x, name: Incomplete | None = None):
    '''Computes hyperbolic tangent of `x` element-wise.

    Given an input tensor, this function computes hyperbolic tangent of every
    element in the tensor. Input range is `[-inf, inf]` and
    output range is `[-1,1]`.

    >>> x = tf.constant([-float("inf"), -5, -0.5, 1, 1.2, 2, 3, float("inf")])
    >>> tf.math.tanh(x)
    <tf.Tensor: shape=(8,), dtype=float32, numpy=
    array([-1.0, -0.99990916, -0.46211717,  0.7615942 ,  0.8336547 ,
            0.9640276 ,  0.9950547 ,  1.0], dtype=float32)>

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  '''

Tanh: Incomplete

def tanh_eager_fallback(x, name, ctx): ...
def tanh_grad(y, dy, name: Incomplete | None = None):
    """Computes the gradient for the tanh of `x` wrt its input.

  Specifically, `grad = dy * (1 - y*y)`, where `y = tanh(x)`, and `dy`
  is the corresponding input gradient.

  Args:
    y: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
    dy: A `Tensor`. Must have the same type as `y`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `y`.
  """

TanhGrad: Incomplete

def tanh_grad_eager_fallback(y, dy, name, ctx): ...
def truncate_div(x, y, name: Incomplete | None = None):
    """Returns x / y element-wise, rounded towards zero.

  Truncation designates that negative numbers will round fractional quantities
  toward zero. I.e. -7 / 5 = -1. This matches C semantics but it is different
  than Python semantics. See `FloorDiv` for a division function that matches
  Python Semantics.

  *NOTE*: `truncatediv` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `uint32`, `uint64`, `int64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

TruncateDiv: Incomplete

def truncate_div_eager_fallback(x, y, name, ctx): ...
def truncate_mod(x, y, name: Incomplete | None = None):
    """Returns element-wise remainder of division. This emulates C semantics in that

  the result here is consistent with a truncating divide. E.g. `truncate(x / y) *
  y + truncate_mod(x, y) = x`.

  *NOTE*: `truncatemod` supports broadcasting. More about broadcasting
  [here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

  Args:
    x: A `Tensor`. Must be one of the following types: `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

TruncateMod: Incomplete

def truncate_mod_eager_fallback(x, y, name, ctx): ...
def unsorted_segment_max(data, segment_ids, num_segments, name: Incomplete | None = None):
    '''Computes the maximum along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  This operator is similar to `tf.math.unsorted_segment_sum`,
  Instead of computing the sum over segments, it computes the maximum such that:

  \\\\(output_i = \\max_{j...} data[j...]\\\\) where max is over tuples `j...` such
  that `segment_ids[j...] == i`.

  If the maximum is empty for a given segment ID `i`, it outputs the smallest
  possible value for the specific numeric type,
  `output[i] = numeric_limits<T>::lowest()`.

  If the given segment ID `i` is negative, then the corresponding value is
  dropped, and will not be included in the result.

  Caution: On CPU, values in `segment_ids` are always validated to be less than
  `num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
  does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
  result in safe but unspecified behavior, which may include ignoring
  out-of-bound indices or outputting a tensor with a 0 stored in the first
  dimension of its shape if `num_segments` is 0.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/UnsortedSegmentMax.png" alt>
  </div>

  For example:

  >>> c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])
  >>> tf.math.unsorted_segment_max(c, tf.constant([0, 1, 0]), num_segments=2).numpy()
  array([[4, 3, 3, 4],
         [5,  6, 7, 8]], dtype=int32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor whose shape is a prefix of `data.shape`.
      The values must be less than `num_segments`.

      Caution: The values are always validated to be in range on CPU, never validated
      on GPU.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  '''

UnsortedSegmentMax: Incomplete

def unsorted_segment_max_eager_fallback(data, segment_ids, num_segments, name, ctx): ...
def unsorted_segment_min(data, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the minimum along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  This operator is similar to `tf.math.unsorted_segment_sum`,
  Instead of computing the sum over segments, it computes the minimum such that:

  \\\\(output_i = \\min_{j...} data_[j...]\\\\) where min is over tuples `j...` such
  that `segment_ids[j...] == i`.

  If the minimum is empty for a given segment ID `i`, it outputs the largest
  possible value for the specific numeric type,
  `output[i] = numeric_limits<T>::max()`.

  For example:

  >>> c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])
  >>> tf.math.unsorted_segment_min(c, tf.constant([0, 1, 0]), num_segments=2).numpy()
  array([[1, 2, 2, 1],
         [5, 6, 7, 8]], dtype=int32)

  If the given segment ID `i` is negative, then the corresponding value is
  dropped, and will not be included in the result.

  Caution: On CPU, values in `segment_ids` are always validated to be less than
  `num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
  does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
  result in safe but unspecified behavior, which may include ignoring
  out-of-bound indices or outputting a tensor with a 0 stored in the first
  dimension of its shape if `num_segments` is 0.

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor whose shape is a prefix of `data.shape`.
      The values must be less than `num_segments`.

      Caution: The values are always validated to be in range on CPU, never validated
      on GPU.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

UnsortedSegmentMin: Incomplete

def unsorted_segment_min_eager_fallback(data, segment_ids, num_segments, name, ctx): ...
def unsorted_segment_prod(data, segment_ids, num_segments, name: Incomplete | None = None):
    """Computes the product along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  This operator is similar to `tf.math.unsorted_segment_sum`,
  Instead of computing the sum over segments, it computes the product of all
  entries belonging to a segment such that:

  \\\\(output_i = \\prod_{j...} data[j...]\\\\) where the product is over tuples
  `j...` such that `segment_ids[j...] == i`.

  For example:

  >>> c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])
  >>> tf.math.unsorted_segment_prod(c, tf.constant([0, 1, 0]), num_segments=2).numpy()
  array([[4, 6, 6, 4],
         [5, 6, 7, 8]], dtype=int32)

  If there is no entry for a given segment ID `i`, it outputs 1.

  If the given segment ID `i` is negative, then the corresponding value is
  dropped, and will not be included in the result.
  Caution: On CPU, values in `segment_ids` are always validated to be less than
  `num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
  does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
  result in safe but unspecified behavior, which may include ignoring
  out-of-bound indices or outputting a tensor with a 0 stored in the first
  dimension of its shape if `num_segments` is 0.

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor whose shape is a prefix of `data.shape`.
      The values must be less than `num_segments`.

      Caution: The values are always validated to be in range on CPU, never validated
      on GPU.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

UnsortedSegmentProd: Incomplete

def unsorted_segment_prod_eager_fallback(data, segment_ids, num_segments, name, ctx): ...
def unsorted_segment_sum(data, segment_ids, num_segments, name: Incomplete | None = None):
    '''Computes the sum along segments of a tensor.

  Read
  [the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
  for an explanation of segments.

  Computes a tensor such that
  \\\\(output[i] = \\sum_{j...} data[j...]\\\\) where the sum is over tuples `j...` such
  that `segment_ids[j...] == i`.  Unlike `SegmentSum`, `segment_ids`
  need not be sorted and need not cover all values in the full
  range of valid values.

  If the sum is empty for a given segment ID `i`, `output[i] = 0`.
  If the given segment ID `i` is negative, the value is dropped and will not be
  added to the sum of the segment.

  `num_segments` should equal the number of distinct segment IDs.

  Caution: On CPU, values in `segment_ids` are always validated to be less than
  `num_segments`, and an error is thrown for out-of-bound indices. On GPU, this
  does not throw an error for out-of-bound indices. On Gpu, out-of-bound indices
  result in safe but unspecified behavior, which may include ignoring
  out-of-bound indices or outputting a tensor with a 0 stored in the first
  dimension of its shape if `num_segments` is 0.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/UnsortedSegmentSum.png" alt>
  </div>

  >>> c = [[1,2,3,4], [5,6,7,8], [4,3,2,1]]
  >>> tf.math.unsorted_segment_sum(c, [0, 1, 0], num_segments=2).numpy()
  array([[5, 5, 5, 5],
         [5, 6, 7, 8]], dtype=int32)

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
    segment_ids: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor whose shape is a prefix of `data.shape`.
      The values must be less than `num_segments`.

      Caution: The values are always validated to be in range on CPU, never validated
      on GPU.
    num_segments: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  '''

UnsortedSegmentSum: Incomplete

def unsorted_segment_sum_eager_fallback(data, segment_ids, num_segments, name, ctx): ...
def xdivy(x, y, name: Incomplete | None = None):
    """Returns 0 if x == 0, and x / y otherwise, elementwise.

  Args:
    x: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Xdivy: Incomplete

def xdivy_eager_fallback(x, y, name, ctx): ...
def xlog1py(x, y, name: Incomplete | None = None):
    """Returns 0 if x == 0, and x * log1p(y) otherwise, elementwise.

  Args:
    x: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Xlog1py: Incomplete

def xlog1py_eager_fallback(x, y, name, ctx): ...
def xlogy(x, y, name: Incomplete | None = None):
    """Returns 0 if x == 0, and x * log(y) otherwise, elementwise.

  Args:
    x: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `complex64`, `complex128`.
    y: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Xlogy: Incomplete

def xlogy_eager_fallback(x, y, name, ctx): ...
def zeta(x, q, name: Incomplete | None = None):
    """Compute the Hurwitz zeta function \\\\(\\zeta(x, q)\\\\).

  The Hurwitz zeta function is defined as:


  \\\\(\\zeta(x, q) = \\sum_{n=0}^{\\infty} (q + n)^{-x}\\\\)

  Args:
    x: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    q: A `Tensor`. Must have the same type as `x`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `x`.
  """

Zeta: Incomplete

def zeta_eager_fallback(x, q, name, ctx): ...
