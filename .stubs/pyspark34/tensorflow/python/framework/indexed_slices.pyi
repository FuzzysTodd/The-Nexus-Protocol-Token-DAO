from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python import tf2 as tf2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, composite_tensor_gradient as composite_tensor_gradient, dtypes as dtypes, tensor_conversion_registry as tensor_conversion_registry, tensor_shape as tensor_shape, type_spec as type_spec
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.types import internal as internal
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

math_ops: Incomplete
ops: Incomplete
tensor_spec: Incomplete
tensor_util: Incomplete

class IndexedSlicesCompositeTensorGradient(composite_tensor_gradient.CompositeTensorGradient):
    """CompositeTensorGradient for IndexedSlices."""
    def get_gradient_components(self, value): ...
    def replace_gradient_components(self, value, component_grads): ...

class IndexedSlices(internal.NativeObject, composite_tensor.CompositeTensor):
    """A sparse representation of a set of tensor slices at given indices.

  This class is a simple wrapper for a pair of `Tensor` objects:

  * `values`: A `Tensor` of any dtype with shape `[D0, D1, ..., Dn]`.
  * `indices`: A 1-D integer `Tensor` with shape `[D0]`.

  An `IndexedSlices` is typically used to represent a subset of a larger
  tensor `dense` of shape `[LARGE0, D1, .. , DN]` where `LARGE0 >> D0`.
  The values in `indices` are the indices in the first dimension of
  the slices that have been extracted from the larger tensor.

  The dense tensor `dense` represented by an `IndexedSlices` `slices` has

  ```python
  dense[slices.indices[i], :, :, :, ...] = slices.values[i, :, :, :, ...]
  ```

  The `IndexedSlices` class is used principally in the definition of
  gradients for operations that have sparse gradients
  (e.g. `tf.gather`).

  >>> v = tf.Variable([[0.,1, 2], [2, 3, 4], [4, 5, 6], [6, 7, 8]])
  >>> with tf.GradientTape() as tape:
  ...   r = tf.gather(v, [1,3])
  >>> index_slices = tape.gradient(r,v)
  >>> index_slices
  <...IndexedSlices object ...>
  >>> index_slices.indices.numpy()
  array([1, 3], dtype=int32)
  >>> index_slices.values.numpy()
  array([[1., 1., 1.],
         [1., 1., 1.]], dtype=float32)

  Contrast this representation with
  `tf.sparse.SparseTensor`,
  which uses multi-dimensional indices and scalar values.
  """
    def __init__(self, values, indices, dense_shape: Incomplete | None = None) -> None:
        """Creates an `IndexedSlices`."""
    @property
    def values(self):
        """A `Tensor` containing the values of the slices."""
    @property
    def indices(self):
        """A 1-D `Tensor` containing the indices of the slices."""
    @property
    def dense_shape(self):
        """A 1-D `Tensor` containing the shape of the corresponding dense tensor."""
    @property
    def shape(self):
        """Gets the `tf.TensorShape` representing the shape of the dense tensor.

    Returns:
      A `tf.TensorShape` object.
    """
    @property
    def name(self):
        """The name of this `IndexedSlices`."""
    @property
    def device(self):
        """The name of the device on which `values` will be produced, or `None`."""
    @property
    def op(self):
        """The `Operation` that produces `values` as an output."""
    @property
    def dtype(self):
        """The `DType` of elements in this tensor."""
    @property
    def graph(self):
        """The `Graph` that contains the values, indices, and shape tensors."""
    def __neg__(self): ...
    __composite_gradient__: Incomplete
    def consumers(self): ...

class IndexedSlicesValue(NamedTuple):
    values: Incomplete
    indices: Incomplete
    dense_shape: Incomplete

class IndexedSlicesSpec(type_spec.TypeSpec):
    """Type specification for a `tf.IndexedSlices`."""
    value_type: Incomplete
    def __init__(self, shape: Incomplete | None = None, dtype=..., indices_dtype=..., dense_shape_dtype: Incomplete | None = None, indices_shape: Incomplete | None = None) -> None:
        """Constructs a type specification for a `tf.IndexedSlices`.

    Args:
      shape: The dense shape of the `IndexedSlices`, or `None` to allow any
        dense shape.
      dtype: `tf.DType` of values in the `IndexedSlices`.
      indices_dtype: `tf.DType` of the `indices` in the `IndexedSlices`.  One
        of `tf.int32` or `tf.int64`.
      dense_shape_dtype: `tf.DType` of the `dense_shape` in the `IndexedSlices`.
        One of `tf.int32`, `tf.int64`, or `None` (if the `IndexedSlices` has
        no `dense_shape` tensor).
      indices_shape: The shape of the `indices` component, which indicates
        how many slices are in the `IndexedSlices`.
    """

def convert_to_tensor_or_indexed_slices(value, dtype: Incomplete | None = None, name: Incomplete | None = None):
    """Converts the given object to a `Tensor` or an `IndexedSlices`.

  If `value` is an `IndexedSlices` or `SparseTensor` it is returned
  unmodified. Otherwise, it is converted to a `Tensor` using
  `convert_to_tensor()`.

  Args:
    value: An `IndexedSlices`, `SparseTensor`, or an object that can be consumed
      by `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor` or
      `IndexedSlices`.
    name: (Optional.) A name to use if a new `Tensor` is created.

  Returns:
    A `Tensor`, `IndexedSlices`, or `SparseTensor` based on `value`.

  Raises:
    ValueError: If `dtype` does not match the element type of `value`.
  """
def internal_convert_to_tensor_or_indexed_slices(value, dtype: Incomplete | None = None, name: Incomplete | None = None, as_ref: bool = False):
    """Converts the given object to a `Tensor` or an `IndexedSlices`.

  If `value` is an `IndexedSlices` or `SparseTensor` it is returned
  unmodified. Otherwise, it is converted to a `Tensor` using
  `convert_to_tensor()`.

  Args:
    value: An `IndexedSlices`, `SparseTensor`, or an object that can be consumed
      by `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor` or
      `IndexedSlices`.
    name: (Optional.) A name to use if a new `Tensor` is created.
    as_ref: True if the caller wants the results as ref tensors.

  Returns:
    A `Tensor`, `IndexedSlices`, or `SparseTensor` based on `value`.

  Raises:
    ValueError: If `dtype` does not match the element type of `value`.
  """
def internal_convert_n_to_tensor_or_indexed_slices(values, dtype: Incomplete | None = None, name: Incomplete | None = None, as_ref: bool = False):
    """Converts `values` to a list of `Tensor` or `IndexedSlices` objects.

  Any `IndexedSlices` or `SparseTensor` objects in `values` are returned
  unmodified.

  Args:
    values: An iterable of `None`, `IndexedSlices`, `SparseTensor`, or objects
      that can be consumed by `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor` or
      `IndexedSlices`.
    name: (Optional.) A name prefix to used when a new `Tensor` is created, in
      which case element `i` will be given the name `name + '_' + i`.
    as_ref: True if the caller wants the results as ref tensors.

  Returns:
    A list of `Tensor`, `IndexedSlices`, `SparseTensor` and/or `None` objects.

  Raises:
    TypeError: If no conversion function is registered for an element in
      `values`.
    RuntimeError: If a registered conversion function returns an invalid
      value.
  """
def convert_n_to_tensor_or_indexed_slices(values, dtype: Incomplete | None = None, name: Incomplete | None = None):
    """Converts `values` to a list of `Output` or `IndexedSlices` objects.

  Any `IndexedSlices` or `SparseTensor` objects in `values` are returned
  unmodified.

  Args:
    values: A list of `None`, `IndexedSlices`, `SparseTensor`, or objects that
      can be consumed by `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor`
      `IndexedSlices`.
    name: (Optional.) A name prefix to used when a new `Tensor` is created, in
      which case element `i` will be given the name `name + '_' + i`.

  Returns:
    A list of `Tensor`, `IndexedSlices`, and/or `SparseTensor` objects.

  Raises:
    TypeError: If no conversion function is registered for an element in
      `values`.
    RuntimeError: If a registered conversion function returns an invalid
      value.
  """
