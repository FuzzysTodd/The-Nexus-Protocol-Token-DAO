from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow, tf2 as tf2
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec, type_spec_registry as type_spec_registry
from tensorflow.python.ops import gen_sparse_ops as gen_sparse_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.types import internal as internal
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class SparseTensor(internal.NativeObject, composite_tensor.CompositeTensor):
    """Represents a sparse tensor.

  TensorFlow represents a sparse tensor as three separate dense tensors:
  `indices`, `values`, and `dense_shape`.  In Python, the three tensors are
  collected into a `SparseTensor` class for ease of use.  If you have separate
  `indices`, `values`, and `dense_shape` tensors, wrap them in a `SparseTensor`
  object before passing to the ops below.

  Concretely, the sparse tensor `SparseTensor(indices, values, dense_shape)`
  comprises the following components, where `N` and `ndims` are the number
  of values and number of dimensions in the `SparseTensor`, respectively:

  * `indices`: A 2-D int64 tensor of shape `[N, ndims]`, which specifies the
    indices of the elements in the sparse tensor that contain nonzero values
    (elements are zero-indexed). For example, `indices=[[1,3], [2,4]]` specifies
    that the elements with indexes of [1,3] and [2,4] have nonzero values.

  * `values`: A 1-D tensor of any type and shape `[N]`, which supplies the
    values for each element in `indices`. For example, given `indices=[[1,3],
    [2,4]]`, the parameter `values=[18, 3.6]` specifies that element [1,3] of
    the sparse tensor has a value of 18, and element [2,4] of the tensor has a
    value of 3.6.

  * `dense_shape`: A 1-D int64 tensor of shape `[ndims]`, which specifies the
    dense_shape of the sparse tensor. Takes a list indicating the number of
    elements in each dimension. For example, `dense_shape=[3,6]` specifies a
    two-dimensional 3x6 tensor, `dense_shape=[2,3,4]` specifies a
    three-dimensional 2x3x4 tensor, and `dense_shape=[9]` specifies a
    one-dimensional tensor with 9 elements.

  The corresponding dense tensor satisfies:

  ```python
  dense.shape = dense_shape
  dense[tuple(indices[i])] = values[i]
  ```

  By convention, `indices` should be sorted in row-major order (or equivalently
  lexicographic order on the tuples `indices[i]`). This is not enforced when
  `SparseTensor` objects are constructed, but most ops assume correct ordering.
  If the ordering of sparse tensor `st` is wrong, a fixed version can be
  obtained by calling `tf.sparse.reorder(st)`.

  Example: The sparse tensor

  ```python
  SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
  ```

  represents the dense tensor

  ```python
  [[1, 0, 0, 0]
   [0, 0, 2, 0]
   [0, 0, 0, 0]]
  ```
  """
    @classmethod
    def from_value(cls, sparse_tensor_value): ...
    def __init__(self, indices, values, dense_shape) -> None:
        """Creates a `SparseTensor`.

    Args:
      indices: A 2-D int64 tensor of shape `[N, ndims]`.
      values: A 1-D tensor of any type and shape `[N]`.
      dense_shape: A 1-D int64 tensor of shape `[ndims]`.

    Raises:
      ValueError: When building an eager SparseTensor if `dense_shape` is
        unknown or contains unknown elements (None or -1).
    """
    def get_shape(self):
        """Get the `TensorShape` representing the shape of the dense tensor.

    Returns:
      A `TensorShape` object.
    """
    @property
    def indices(self):
        """The indices of non-zero values in the represented dense tensor.

    Returns:
      A 2-D Tensor of int64 with dense_shape `[N, ndims]`, where `N` is the
        number of non-zero values in the tensor, and `ndims` is the rank.
    """
    @property
    def values(self):
        """The non-zero values in the represented dense tensor.

    Returns:
      A 1-D Tensor of any data type.
    """
    def with_values(self, new_values):
        """Returns a copy of `self` with `values` replaced by `new_values`.

    This method produces a new `SparseTensor` that has the same nonzero
    `indices` and same `dense_shape`, but updated values.

    Args:
      new_values: The values of the new `SparseTensor`. Needs to have the same
        shape as the current `.values` `Tensor`. May have a different type than
        the current `values`.

    Returns:
      A `SparseTensor` with identical indices and shape but updated values.

    Example usage:

    >>> st = tf.sparse.from_dense([[1, 0, 2, 0], [3, 0, 0, 4]])
    >>> tf.sparse.to_dense(st.with_values([10, 20, 30, 40]))  # 4 nonzero values
    <tf.Tensor: shape=(2, 4), dtype=int32, numpy=
    array([[10,  0, 20,  0],
           [30,  0,  0, 40]], dtype=int32)>

    """
    @property
    def op(self):
        """The `Operation` that produces `values` as an output."""
    @property
    def dtype(self):
        """The `DType` of elements in this tensor."""
    @property
    def dense_shape(self):
        """A 1-D Tensor of int64 representing the shape of the dense tensor."""
    @property
    def shape(self):
        """Get the `TensorShape` representing the shape of the dense tensor.

    Returns:
      A `TensorShape` object.
    """
    def set_shape(self, shape) -> None:
        """Updates the `TensorShape` representing the shape of the dense tensor.

    With eager execution this operates as a shape assertion.
    Here the shapes match:

    >>> st = tf.SparseTensor(
    ...   indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
    >>> st.set_shape([3, 4])

    Passing a `None` in the new shape allows any value for that axis:

    >>> st.set_shape([3, None])

    An error is raised if an incompatible shape is passed.

    >>> st.set_shape([1, 4])
    Traceback (most recent call last):
    ...
    ValueError: Tensor's shape (3, 4) is not compatible with supplied
    shape [1, 4]

    When executing in a `tf.function`, or building a model using
    `tf.keras.Input`, `SparseTensor.set_shape` will *merge* the given `shape`
    with the current shape of this tensor, and set the tensor's shape to the
    merged value (see `tf.TensorShape.merge_with` for details):

    >>> st = tf.keras.Input(shape=[None, None, 3], sparse=True)
    >>> print(st.shape)
    (None, None, None, 3)

    Dimensions set to `None` are not updated:

    >>> st.set_shape([None, 224, 224, None])
    >>> print(st.shape)
    (None, 224, 224, 3)

    The main use case for this is to provide additional shape information
    that cannot be inferred from the graph alone.

    Caution: `set_shape` ensures that the applied shape is compatible with
    the existing shape, but it does not check at runtime. Setting
    incorrect shapes can result in inconsistencies between the
    statically-known graph and the runtime value of tensors.

    Args:
      shape: A `TensorShape` representing the shape of this tensor, a
        `TensorShapeProto`, a list, a tuple, or None.

    Raises:
      ValueError: If `shape` is not compatible with the current shape of
        this tensor.
    """
    @property
    def graph(self):
        """The `Graph` that contains the index, value, and dense_shape tensors."""
    def eval(self, feed_dict: Incomplete | None = None, session: Incomplete | None = None):
        """Evaluates this sparse tensor in a `Session`.

    Calling this method will execute all preceding operations that
    produce the inputs needed for the operation that produces this
    tensor.

    *N.B.* Before invoking `SparseTensor.eval()`, its graph must have been
    launched in a session, and either a default session must be
    available, or `session` must be specified explicitly.

    Args:
      feed_dict: A dictionary that maps `Tensor` objects to feed values. See
        `tf.Session.run` for a description of the valid feed values.
      session: (Optional.) The `Session` to be used to evaluate this sparse
        tensor. If none, the default session will be used.

    Returns:
      A `SparseTensorValue` object.
    """
    def consumers(self): ...

class SparseTensorValue(NamedTuple):
    indices: Incomplete
    values: Incomplete
    dense_shape: Incomplete

class SparseTensorSpec(type_spec.BatchableTypeSpec):
    """Type specification for a `tf.sparse.SparseTensor`."""
    value_type: Incomplete
    def __init__(self, shape: Incomplete | None = None, dtype=...) -> None:
        """Constructs a type specification for a `tf.sparse.SparseTensor`.

    Args:
      shape: The dense shape of the `SparseTensor`, or `None` to allow any dense
        shape.
      dtype: `tf.DType` of values in the `SparseTensor`.
    """
    @property
    def dtype(self):
        """The `tf.dtypes.DType` specified by this type for the SparseTensor."""
    @property
    def shape(self):
        """The `tf.TensorShape` specified by this type for the SparseTensor."""
    @classmethod
    def from_value(cls, value): ...

def convert_to_tensor_or_sparse_tensor(value, dtype: Incomplete | None = None, name: Incomplete | None = None):
    """Converts value to a `SparseTensor` or `Tensor`.

  Args:
    value: A `SparseTensor`, `SparseTensorValue`, or an object whose type has a
      registered `Tensor` conversion function.
    dtype: Optional element type for the returned tensor. If missing, the type
      is inferred from the type of `value`.
    name: Optional name to use if a new `Tensor` is created.

  Returns:
    A `SparseTensor` or `Tensor` based on `value`.

  Raises:
    RuntimeError: If result type is incompatible with `dtype`.
  """
def is_sparse(x):
    """Check whether `x` is sparse.

  Check whether an object is a `tf.sparse.SparseTensor` or
  `tf.compat.v1.SparseTensorValue`.

  Args:
    x: A python object to check.

  Returns:
    `True` iff `x` is a `tf.sparse.SparseTensor` or
    `tf.compat.v1.SparseTensorValue`.
  """
