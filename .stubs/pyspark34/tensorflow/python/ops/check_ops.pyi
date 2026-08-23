from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['assert_negative', 'assert_positive', 'assert_proper_iterable', 'assert_non_negative', 'assert_non_positive', 'assert_equal', 'assert_none_equal', 'assert_near', 'assert_integer', 'assert_less', 'assert_less_equal', 'assert_greater', 'assert_greater_equal', 'assert_rank', 'assert_rank_at_least', 'assert_rank_in', 'assert_same_float_dtype', 'assert_scalar', 'assert_type', 'assert_shapes', 'is_non_decreasing', 'is_numeric_tensor', 'is_strictly_increasing']

def assert_proper_iterable(values) -> None:
    '''Static assert that values is a "proper" iterable.

  `Ops` that expect iterables of `Tensor` can call this to validate input.
  Useful since `Tensor`, `ndarray`, byte/text type are all iterables themselves.

  Args:
    values:  Object to be checked.

  Raises:
    TypeError:  If `values` is not iterable or is one of
      `Tensor`, `SparseTensor`, `np.array`, `tf.compat.bytes_or_text_types`.
  '''
def assert_negative(x, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_positive(x, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_non_negative(x, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_non_positive(x, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_equal(x, y, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_none_equal(x, y, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_near(x, y, rtol: Incomplete | None = None, atol: Incomplete | None = None, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None):
    '''Assert the condition `x` and `y` are close element-wise.

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.compat.v1.assert_near(x, y)]):
    output = tf.reduce_sum(x)
  ```

  This condition holds if for every pair of (possibly broadcast) elements
  `x[i]`, `y[i]`, we have

  ```tf.abs(x[i] - y[i]) <= atol + rtol * tf.abs(y[i])```.

  If both `x` and `y` are empty, this is trivially satisfied.

  The default `atol` and `rtol` is `10 * eps`, where `eps` is the smallest
  representable positive number such that `1 + eps != 1`.  This is about
  `1.2e-6` in `32bit`, `2.22e-15` in `64bit`, and `0.00977` in `16bit`.
  See `numpy.finfo`.

  Args:
    x:  Float or complex `Tensor`.
    y:  Float or complex `Tensor`, same `dtype` as, and broadcastable to, `x`.
    rtol:  `Tensor`.  Same `dtype` as, and broadcastable to, `x`.
      The relative tolerance.  Default is `10 * eps`.
    atol:  `Tensor`.  Same `dtype` as, and broadcastable to, `x`.
      The absolute tolerance.  Default is `10 * eps`.
    data:  The tensors to print out if the condition is False.  Defaults to
      error message and first few entries of `x`, `y`.
    summarize: Print this many entries of each tensor.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).  Defaults to "assert_near".

  Returns:
    Op that raises `InvalidArgumentError` if `x` and `y` are not close enough.

  @compatibility(numpy)
  Similar to `numpy.testing.assert_allclose`, except tolerance depends on data
  type. This is due to the fact that `TensorFlow` is often used with `32bit`,
  `64bit`, and even `16bit` data.
  @end_compatibility
  '''
def assert_less(x, y, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_less_equal(x, y, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_greater(x, y, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_greater_equal(x, y, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None): ...
def assert_rank(x, rank, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None):
    '''Assert `x` has rank equal to `rank`.

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.compat.v1.assert_rank(x, 2)]):
    output = tf.reduce_sum(x)
  ```

  Args:
    x:  Numeric `Tensor`.
    rank:  Scalar integer `Tensor`.
    data:  The tensors to print out if the condition is False.  Defaults to
      error message and the shape of `x`.
    summarize: Print this many entries of each tensor.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).  Defaults to "assert_rank".

  Returns:
    Op raising `InvalidArgumentError` unless `x` has specified rank.
    If static checks determine `x` has correct rank, a `no_op` is returned.

  Raises:
    ValueError:  If static checks determine `x` has wrong rank.
  '''
def assert_rank_at_least(x, rank, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None):
    '''Assert `x` has rank equal to `rank` or higher.

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.compat.v1.assert_rank_at_least(x, 2)]):
    output = tf.reduce_sum(x)
  ```

  Args:
    x:  Numeric `Tensor`.
    rank:  Scalar `Tensor`.
    data:  The tensors to print out if the condition is False.  Defaults to
      error message and first few entries of `x`.
    summarize: Print this many entries of each tensor.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).
      Defaults to "assert_rank_at_least".

  Returns:
    Op raising `InvalidArgumentError` unless `x` has specified rank or higher.
    If static checks determine `x` has correct rank, a `no_op` is returned.

  Raises:
    ValueError:  If static checks determine `x` has wrong rank.
  '''
def assert_rank_in(x, ranks, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None):
    '''Assert `x` has rank in `ranks`.

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.compat.v1.assert_rank_in(x, (2, 4))]):
    output = tf.reduce_sum(x)
  ```

  Args:
    x:  Numeric `Tensor`.
    ranks:  Iterable of scalar `Tensor` objects.
    data:  The tensors to print out if the condition is False.  Defaults to
      error message and first few entries of `x`.
    summarize: Print this many entries of each tensor.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).
      Defaults to "assert_rank_in".

  Returns:
    Op raising `InvalidArgumentError` unless rank of `x` is in `ranks`.
    If static checks determine `x` has matching rank, a `no_op` is returned.

  Raises:
    ValueError:  If static checks determine `x` has mismatched rank.
  '''
def assert_integer(x, message: Incomplete | None = None, name: Incomplete | None = None):
    '''Assert that `x` is of integer dtype.

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.compat.v1.assert_integer(x)]):
    output = tf.reduce_sum(x)
  ```

  Args:
    x: `Tensor` whose basetype is integer and is not quantized.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).  Defaults to "assert_integer".

  Raises:
    TypeError:  If `x.dtype` is anything other than non-quantized integer.

  Returns:
    A `no_op` that does nothing.  Type can be determined statically.
  '''
def assert_type(tensor, tf_type, message: Incomplete | None = None, name: Incomplete | None = None):
    '''Statically asserts that the given `Tensor` is of the specified type.

  Args:
    tensor: A `Tensor` or `SparseTensor`.
    tf_type: A tensorflow type (`dtypes.float32`, `tf.int64`, `dtypes.bool`,
      etc).
    message: A string to prefix to the default message.
    name:  A name to give this `Op`.  Defaults to "assert_type"

  Raises:
    TypeError: If the tensors data type doesn\'t match `tf_type`.

  Returns:
    A `no_op` that does nothing.  Type can be determined statically.
  '''

class _TensorDimSizes(NamedTuple):
    x: Incomplete
    unspecified_dim: Incomplete
    actual_sizes: Incomplete
    symbolic_sizes: Incomplete

def assert_shapes(shapes, data: Incomplete | None = None, summarize: Incomplete | None = None, message: Incomplete | None = None, name: Incomplete | None = None):
    '''Assert tensor shapes and dimension size relationships between tensors.

  This Op checks that a collection of tensors shape relationships
  satisfies given constraints.

  Example:

  >>> n = 10
  >>> q = 3
  >>> d = 7
  >>> x = tf.zeros([n,q])
  >>> y = tf.ones([n,d])
  >>> param = tf.Variable([1.0, 2.0, 3.0])
  >>> scalar = 1.0
  >>> tf.debugging.assert_shapes([
  ...  (x, (\'N\', \'Q\')),
  ...  (y, (\'N\', \'D\')),
  ...  (param, (\'Q\',)),
  ...  (scalar, ()),
  ... ])

  >>> tf.debugging.assert_shapes([
  ...   (x, (\'N\', \'D\')),
  ...   (y, (\'N\', \'D\'))
  ... ])
  Traceback (most recent call last):
  ...
  ValueError: ...

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.assert_shapes(shapes)]):
    output = tf.matmul(x, y, transpose_a=True)
  ```

  If `x`, `y`, `param` or `scalar` does not have a shape that satisfies
  all specified constraints, `message`, as well as the first `summarize` entries
  of the first encountered violating tensor are printed, and
  `InvalidArgumentError` is raised.

  Size entries in the specified shapes are checked against other entries by
  their __hash__, except:
    - a size entry is interpreted as an explicit size if it can be parsed as an
      integer primitive.
    - a size entry is interpreted as *any* size if it is None or \'.\'.

  If the first entry of a shape is `...` (type `Ellipsis`) or \'*\' that indicates
  a variable number of outer dimensions of unspecified size, i.e. the constraint
  applies to the inner-most dimensions only.

  Scalar tensors and specified shapes of length zero (excluding the \'inner-most\'
  prefix) are both treated as having a single dimension of size one.

  Args:
    shapes: A list of (`Tensor`, `shape`) tuples, wherein `shape` is the
      expected shape of `Tensor`. See the example code above. The `shape` must
      be an iterable. Each element of the iterable can be either a concrete
      integer value or a string that abstractly represents the dimension.
      For example,
        - `(\'N\', \'Q\')` specifies a 2D shape wherein the first and second
          dimensions of shape may or may not be equal.
        - `(\'N\', \'N\', \'Q\')` specifies a 3D shape wherein the first and second
          dimensions are equal.
        - `(1, \'N\')` specifies a 2D shape wherein the first dimension is
          exactly 1 and the second dimension can be any value.
      Note that the abstract dimension letters take effect across different
      tuple elements of the list. For example,
      `tf.debugging.assert_shapes([(x, (\'N\', \'A\')), (y, (\'N\', \'B\'))]` asserts
      that both `x` and `y` are rank-2 tensors and their first dimensions are
      equal (`N`).
      `shape` can also be a `tf.TensorShape`.
    data: The tensors to print out if the condition is False.  Defaults to error
      message and first few entries of the violating tensor.
    summarize: Print this many entries of the tensor.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).  Defaults to "assert_shapes".

  Returns:
    Op raising `InvalidArgumentError` unless all shape constraints are
    satisfied.
    If static checks determine all constraints are satisfied, a `no_op` is
    returned.

  Raises:
    ValueError:  If static checks determine any shape constraint is violated.
  '''
def is_numeric_tensor(tensor):
    """Returns `True` if the elements of `tensor` are numbers.

  Specifically, returns `True` if the dtype of `tensor` is one of the following:

  * `tf.float16`
  * `tf.float32`
  * `tf.float64`
  * `tf.int8`
  * `tf.int16`
  * `tf.int32`
  * `tf.int64`
  * `tf.uint8`
  * `tf.uint16`
  * `tf.uint32`
  * `tf.uint64`
  * `tf.qint8`
  * `tf.qint16`
  * `tf.qint32`
  * `tf.quint8`
  * `tf.quint16`
  * `tf.complex64`
  * `tf.complex128`
  * `tf.bfloat16`

  Returns `False` if `tensor` is of a non-numeric type or if `tensor` is not
  a `tf.Tensor` object.
  """
def is_non_decreasing(x, name: Incomplete | None = None):
    '''Returns `True` if `x` is non-decreasing.

  Elements of `x` are compared in row-major order.  The tensor `[x[0],...]`
  is non-decreasing if for every adjacent pair we have `x[i] <= x[i+1]`.
  If `x` has less than two elements, it is trivially non-decreasing.

  See also:  `is_strictly_increasing`

  >>> x1 = tf.constant([1.0, 1.0, 3.0])
  >>> tf.math.is_non_decreasing(x1)
  <tf.Tensor: shape=(), dtype=bool, numpy=True>
  >>> x2 = tf.constant([3.0, 1.0, 2.0])
  >>> tf.math.is_non_decreasing(x2)
  <tf.Tensor: shape=(), dtype=bool, numpy=False>

  Args:
    x: Numeric `Tensor`.
    name: A name for this operation (optional).  Defaults to "is_non_decreasing"

  Returns:
    Boolean `Tensor`, equal to `True` iff `x` is non-decreasing.

  Raises:
    TypeError: if `x` is not a numeric tensor.
  '''
def is_strictly_increasing(x, name: Incomplete | None = None):
    '''Returns `True` if `x` is strictly increasing.

  Elements of `x` are compared in row-major order.  The tensor `[x[0],...]`
  is strictly increasing if for every adjacent pair we have `x[i] < x[i+1]`.
  If `x` has less than two elements, it is trivially strictly increasing.

  See also:  `is_non_decreasing`

  >>> x1 = tf.constant([1.0, 2.0, 3.0])
  >>> tf.math.is_strictly_increasing(x1)
  <tf.Tensor: shape=(), dtype=bool, numpy=True>
  >>> x2 = tf.constant([3.0, 1.0, 2.0])
  >>> tf.math.is_strictly_increasing(x2)
  <tf.Tensor: shape=(), dtype=bool, numpy=False>

  Args:
    x: Numeric `Tensor`.
    name: A name for this operation (optional).
      Defaults to "is_strictly_increasing"

  Returns:
    Boolean `Tensor`, equal to `True` iff `x` is strictly increasing.

  Raises:
    TypeError: if `x` is not a numeric tensor.
  '''
def assert_same_float_dtype(tensors: Incomplete | None = None, dtype: Incomplete | None = None):
    """Validate and return float type based on `tensors` and `dtype`.

  For ops such as matrix multiplication, inputs and weights must be of the
  same float type. This function validates that all `tensors` are the same type,
  validates that type is `dtype` (if supplied), and returns the type. Type must
  be a floating point type. If neither `tensors` nor `dtype` is supplied,
  the function will return `dtypes.float32`.

  Args:
    tensors: Tensors of input values. Can include `None` elements, which will be
        ignored.
    dtype: Expected type.

  Returns:
    Validated type.

  Raises:
    ValueError: if neither `tensors` nor `dtype` is supplied, or result is not
        float, or the common type of the inputs is not a floating point type.
  """
def assert_scalar(tensor, name: Incomplete | None = None, message: Incomplete | None = None):
    '''Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

  This function raises `ValueError` unless it can be certain that the given
  `tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is
  unknown.

  Args:
    tensor: A `Tensor`.
    name:  A name for this operation. Defaults to "assert_scalar"
    message: A string to prefix to the default message.

  Returns:
    The input tensor (potentially converted to a `Tensor`).

  Raises:
    ValueError: If the tensor is not scalar (rank 0), or if its shape is
      unknown.
  '''
