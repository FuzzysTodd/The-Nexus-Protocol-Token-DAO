from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.module import module as module
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, linalg_ops as linalg_ops, math_ops as math_ops
from tensorflow.python.util import nest as nest

def convert_nonref_to_tensor(value, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None, name: Incomplete | None = None):
    """Converts the given `value` to a `Tensor` if input is nonreference type.

  This function converts Python objects of various types to `Tensor` objects
  except if the input has nonreference semantics. Reference semantics are
  characterized by `is_ref` and is any object which is a
  `tf.Variable` or instance of `tf.Module`. This function accepts any input
  which `tf.convert_to_tensor` would also.

  Note: This function diverges from default Numpy behavior for `float` and
    `string` types when `None` is present in a Python list or scalar. Rather
    than silently converting `None` values, an error will be thrown.

  Args:
    value: An object whose type has a registered `Tensor` conversion function.
    dtype: Optional element type for the returned tensor. If missing, the
      type is inferred from the type of `value`.
    dtype_hint: Optional element type for the returned tensor,
      used when dtype is None. In some cases, a caller may not have a
      dtype in mind when converting to a tensor, so dtype_hint
      can be used as a soft preference.  If the conversion to
      `dtype_hint` is not possible, this argument has no effect.
    name: Optional name to use if a new `Tensor` is created.

  Returns:
    tensor: A `Tensor` based on `value`.

  Raises:
    TypeError: If no conversion function is registered for `value` to `dtype`.
    RuntimeError: If a registered conversion function returns an invalid value.
    ValueError: If the `value` is a tensor not of given `dtype` in graph mode.


  #### Examples:

  ```python

  x = tf.Variable(0.)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> True

  x = tf.constant(0.)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> True

  x = np.array(0.)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> False
  tf.is_tensor(y)
  # ==> True

  x = tfp.util.DeferredTensor(13.37, lambda x: x)
  y = convert_nonref_to_tensor(x)
  x is y
  # ==> True
  tf.is_tensor(y)
  # ==> False
  tf.equal(y, 13.37)
  # ==> True
  ```

  """
def base_dtype(dtype):
    """Returns a non-reference `dtype` based on this `dtype`."""
def dtype_name(dtype):
    """Returns the string name for this `dtype`."""
def check_dtype(arg, dtype) -> None:
    """Check that arg.dtype == self.dtype."""
def is_ref(x):
    '''Evaluates if the object has reference semantics.

  An object is deemed "reference" if it is a `tf.Variable` instance or is
  derived from a `tf.Module` with `dtype` and `shape` properties.

  Args:
    x: Any object.

  Returns:
    is_ref: Python `bool` indicating input is has nonreference semantics, i.e.,
      is a `tf.Variable` or a `tf.Module` with `dtype` and `shape` properties.
  '''
def assert_not_ref_type(x, arg_name) -> None: ...
def assert_no_entries_with_modulus_zero(x, message: Incomplete | None = None, name: str = 'assert_no_entries_with_modulus_zero'):
    """Returns `Op` that asserts Tensor `x` has no entries with modulus zero.

  Args:
    x:  Numeric `Tensor`, real, integer, or complex.
    message:  A string message to prepend to failure message.
    name:  A name to give this `Op`.

  Returns:
    An `Op` that asserts `x` has no entries with modulus zero.
  """
def assert_zero_imag_part(x, message: Incomplete | None = None, name: str = 'assert_zero_imag_part'):
    """Returns `Op` that asserts Tensor `x` has no non-zero imaginary parts.

  Args:
    x:  Numeric `Tensor`, real, integer, or complex.
    message:  A string message to prepend to failure message.
    name:  A name to give this `Op`.

  Returns:
    An `Op` that asserts `x` has no entries with modulus zero.
  """
def assert_compatible_matrix_dimensions(operator, x):
    '''Assert that an argument to solve/matmul has proper domain dimension.

  If `operator.shape[-2:] = [M, N]`, and `x.shape[-2:] = [Q, R]`, then
  `operator.matmul(x)` is defined only if `N = Q`.  This `Op` returns an
  `Assert` that "fires" if this is not the case.  Static checks are already
  done by the base class `LinearOperator`.

  Args:
    operator:  `LinearOperator`.
    x:  `Tensor`.

  Returns:
    `Assert` `Op`.
  '''
def assert_is_batch_matrix(tensor) -> None:
    """Static assert that `tensor` has rank `2` or higher."""
def shape_tensor(shape, name: Incomplete | None = None):
    """Convert Tensor using default type, unless empty list or tuple."""
def broadcast_matrix_batch_dims(batch_matrices, name: Incomplete | None = None):
    """Broadcast leading dimensions of zero or more [batch] matrices.

  Example broadcasting one batch dim of two simple matrices.

  ```python
  x = [[1, 2],
       [3, 4]]  # Shape [2, 2], no batch dims

  y = [[[1]]]   # Shape [1, 1, 1], 1 batch dim of shape [1]

  x_bc, y_bc = broadcast_matrix_batch_dims([x, y])

  x_bc
  ==> [[[1, 2],
        [3, 4]]]  # Shape [1, 2, 2], 1 batch dim of shape [1].

  y_bc
  ==> same as y
  ```

  Example broadcasting many batch dims

  ```python
  x = tf.random.normal(shape=(2, 3, 1, 4, 4))
  y = tf.random.normal(shape=(1, 3, 2, 5, 5))
  x_bc, y_bc = broadcast_matrix_batch_dims([x, y])

  x_bc.shape
  ==> (2, 3, 2, 4, 4)

  y_bc.shape
  ==> (2, 3, 2, 5, 5)
  ```

  Args:
    batch_matrices:  Iterable of `Tensor`s, each having two or more dimensions.
    name:  A string name to prepend to created ops.

  Returns:
    bcast_matrices: List of `Tensor`s, with `bcast_matrices[i]` containing
      the values from `batch_matrices[i]`, with possibly broadcast batch dims.

  Raises:
    ValueError:  If any input `Tensor` is statically determined to have less
      than two dimensions.
  """
def matrix_solve_with_broadcast(matrix, rhs, adjoint: bool = False, name: Incomplete | None = None):
    """Solve systems of linear equations."""
def is_adjoint_pair(x, y):
    """True iff x and y are adjoints of each other (by id, not entries)."""
def is_aat_form(operators):
    """Returns True if operators is of the form A @ A.H, possibly recursively."""
def use_operator_or_provided_hint_unless_contradicting(operator, hint_attr_name, provided_hint_value, message):
    """Get combined hint in the case where operator.hint should equal hint.

  Args:
    operator:  LinearOperator that a meta-operator was initialized with.
    hint_attr_name:  String name for the attribute.
    provided_hint_value:  Bool or None. Value passed by user in initialization.
    message:  Error message to print if hints contradict.

  Returns:
    True, False, or None.

  Raises:
    ValueError: If hints contradict.
  """
def arg_is_blockwise(block_dimensions, arg, arg_split_dim):
    """Detect if input should be interpreted as a list of blocks."""
def split_arg_into_blocks(block_dims, block_dims_fn, arg, axis: int = -1):
    """Split `x` into blocks matching `operators`'s `domain_dimension`.

  Specifically, if we have a blockwise lower-triangular matrix, with block
  sizes along the diagonal `[M_j, M_j] j = 0,1,2..J`,  this method splits `arg`
  on `axis` into `J` tensors, whose shape at `axis` is `M_j`.

  Args:
    block_dims: Iterable of `TensorShapes`.
    block_dims_fn: Callable returning an iterable of `Tensor`s.
    arg: `Tensor`. `arg` is split into `J` tensors.
    axis: Python `Integer` representing the axis to split `arg` on.

  Returns:
    A list of `Tensor`s.
  """
