from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec, type_spec_registry as type_spec_registry
from tensorflow.python.ops import array_ops as array_ops, control_flow_util as control_flow_util, gen_control_flow_ops as gen_control_flow_ops, gen_data_flow_ops as gen_data_flow_ops, list_ops as list_ops, math_ops as math_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import tf_should_use as tf_should_use
from tensorflow.python.util.tf_export import tf_export as tf_export

class _GraphTensorArray:
    """Graph-mode implementation of TensorArray."""
    def __init__(self, dtype, size: Incomplete | None = None, dynamic_size: Incomplete | None = None, clear_after_read: Incomplete | None = None, tensor_array_name: Incomplete | None = None, handle: Incomplete | None = None, flow: Incomplete | None = None, infer_shape: bool = True, element_shape: Incomplete | None = None, colocate_with_first_write_call: bool = True, name: Incomplete | None = None) -> None:
        """Constructs a graph mode TensorArray.

    Args:
      dtype: (required) data type of the TensorArray.
      size: (optional) int32 scalar `Tensor`: the size of the TensorArray.
        Required if handle is not provided.
      dynamic_size: (optional) Python bool: If true, writes to the TensorArray
        can grow the TensorArray past its initial size.  Default: False.
      clear_after_read: Boolean (optional, default: True).  If True, clear
        TensorArray values after reading them.  This disables read-many
        semantics, but allows early release of memory.
      tensor_array_name: (optional) Python string: the name of the TensorArray.
        This is used when creating the TensorArray handle.  If this value is
        set, handle should be None.
      handle: (optional) A `Tensor` handle to an existing TensorArray.  If this
        is set, tensor_array_name should be None. Only supported in graph mode.
      flow: (optional) A float `Tensor` scalar coming from an existing
        `TensorArray.flow`. Only supported in graph mode.
      infer_shape: (optional, default: True) If True, shape inference is
        enabled.  In this case, all elements must have the same shape.
      element_shape: (optional, default: None) A `TensorShape` object specifying
        the shape constraints of each of the elements of the TensorArray. Need
        not be fully defined.
      colocate_with_first_write_call: If `True`, the TensorArray will be
        colocated on the same device as the Tensor used on its first write
        (write operations include `write`, `unstack`, and `split`).  If `False`,
        the TensorArray will be placed on the device determined by the device
        context available during its initialization.
      name: A name for the operation (optional).

    Raises:
      ValueError: if both handle and tensor_array_name are provided.
      TypeError: if handle is provided but is not a Tensor.
    """
    @property
    def flow(self): ...
    @property
    def dtype(self): ...
    @property
    def handle(self): ...
    @property
    def element_shape(self): ...
    def identity(self):
        """See TensorArray."""
    def grad(self, source, flow: Incomplete | None = None, name: Incomplete | None = None):
        """See TensorArray."""
    def read(self, index, name: Incomplete | None = None):
        """See TensorArray."""
    def write(self, index, value, name: Incomplete | None = None):
        """See TensorArray."""
    def stack(self, name: Incomplete | None = None):
        """See TensorArray."""
    def gather(self, indices, name: Incomplete | None = None):
        """See TensorArray."""
    def concat(self, name: Incomplete | None = None):
        """See TensorArray."""
    def unstack(self, value, name: Incomplete | None = None):
        """See TensorArray."""
    def scatter(self, indices, value, name: Incomplete | None = None):
        """See TensorArray."""
    def split(self, value, lengths, name: Incomplete | None = None):
        """See TensorArray."""
    def size(self, name: Incomplete | None = None):
        """See TensorArray."""
    def close(self, name: Incomplete | None = None):
        """See TensorArray."""

class _GraphTensorArrayV2:
    """Graph-mode implementation of TensorArray backed by TensorLists.

  The backing tensor of this TensorArray is a TensorList variant tensor which is
  stored in the `flow`. The `handle` is always none here. The reason we use the
  `flow` field and not the `handle` field is to ensure backwards compatibility
  with legacy control flow.
  """
    def __init__(self, dtype, size: Incomplete | None = None, dynamic_size: Incomplete | None = None, clear_after_read: Incomplete | None = None, tensor_array_name: Incomplete | None = None, handle: Incomplete | None = None, flow: Incomplete | None = None, infer_shape: bool = True, element_shape: Incomplete | None = None, colocate_with_first_write_call: bool = True, name: Incomplete | None = None) -> None:
        """Constructs a graph mode TensorArray.

    Args:
      dtype: (required) data type of the TensorArray.
      size: (optional) int32 scalar `Tensor`: the size of the TensorArray.
        Required if flow is not provided.
      dynamic_size: (optional) Python bool: If true, writes to the TensorArray
        can grow the TensorArray past its initial size.  Default: False.
      clear_after_read: (optional) unused. Not supported in TensorLists.
      tensor_array_name: (optional) unused.
      handle: (optional) Must always be None.
      flow: (optional) A variant `Tensor` scalar for a TensorList.
      infer_shape: (optional, default: True) If True, shape inference is
        enabled.  In this case, all elements must have the same shape.
      element_shape: (optional, default: None) A `TensorShape` object specifying
        the shape constraints of each of the elements of the TensorArray. Need
        not be fully defined.
      colocate_with_first_write_call: (optional). unused.
      name: (optional) A name for the operation.

    Raises:
      ValueError: if both handle and tensor_array_name are provided.
      TypeError: if handle is provided but is not a Tensor.
    """
    @property
    def flow(self): ...
    @property
    def dtype(self): ...
    @property
    def element_shape(self): ...
    @property
    def handle(self) -> None: ...
    def identity(self):
        """See TensorArray."""
    def grad(self, source, flow: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Not supported."""
    def read(self, index, name: Incomplete | None = None):
        """See TensorArray."""
    def write(self, index, value, name: Incomplete | None = None):
        """See TensorArray."""
    def stack(self, name: Incomplete | None = None):
        """See TensorArray."""
    def gather(self, indices, name: Incomplete | None = None):
        """See TensorArray."""
    def concat(self, name: Incomplete | None = None):
        """See TensorArray."""
    def unstack(self, value, name: Incomplete | None = None):
        """See TensorArray."""
    def scatter(self, indices, value, name: Incomplete | None = None):
        """See TensorArray."""
    def split(self, value, lengths, name: Incomplete | None = None):
        """See TensorArray."""
    def size(self, name: Incomplete | None = None):
        """See TensorArray."""
    def close(self, name: Incomplete | None = None):
        """See TensorArray."""

class _EagerTensorArray:
    """Eager-compatible implementation of TensorArray."""
    def __init__(self, dtype, size: Incomplete | None = None, dynamic_size: Incomplete | None = None, clear_after_read: Incomplete | None = None, tensor_array_name: Incomplete | None = None, handle: Incomplete | None = None, flow: Incomplete | None = None, infer_shape: bool = True, element_shape: Incomplete | None = None, colocate_with_first_write_call: bool = True, name: Incomplete | None = None) -> None:
        """Constructs a TensorArray compatible with eager execution.

    Args:
      dtype: (required) data type of the TensorArray.
      size: (optional) int32 scalar `Tensor`: the size of the TensorArray.
        Required if handle is not provided.
      dynamic_size: (optional) Python bool: If true, writes to the TensorArray
        can grow the TensorArray past its initial size.  Default: False.
      clear_after_read: Boolean (optional, default: True).  If True, clear
        TensorArray values after reading them.  This disables read-many
        semantics, but allows early release of memory.
      tensor_array_name: unused.
      handle: unsupported.
      flow: unsupported.
      infer_shape: used for error checking, same semantics as TensorArray.
      element_shape: used for error checking, same semantics as TensorArray.
      colocate_with_first_write_call: unsupported.
      name: unsupported.

    Raises:
      ValueError: handle or flow are supplied, or if size is not supplied.
    """
    @property
    def flow(self):
        """For compatibility; flows are not meaningful when eager is enabled."""
    @property
    def dtype(self): ...
    @property
    def handle(self):
        """For compatibility; handles are not meaningful when eager is enabled."""
    @property
    def element_shape(self): ...
    def identity(self):
        """See TensorArray."""
    def grad(self, source, flow: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def read(self, index, name: Incomplete | None = None):
        """See TensorArray."""
    def write(self, index, value, name: Incomplete | None = None):
        """See TensorArray."""
    def stack(self, name: Incomplete | None = None):
        """See TensorArray."""
    def gather(self, indices, name: Incomplete | None = None):
        """See TensorArray."""
    def concat(self, name: Incomplete | None = None):
        """See TensorArray."""
    def unstack(self, value, name: Incomplete | None = None):
        """See TensorArray."""
    def scatter(self, indices, value, name: Incomplete | None = None):
        """See TensorArray."""
    def split(self, value, lengths, name: Incomplete | None = None):
        """See TensorArray."""
    def size(self, name: Incomplete | None = None):
        """See TensorArray."""
    def close(self, name: Incomplete | None = None) -> None: ...

class TensorArray:
    '''Class wrapping dynamic-sized, per-time-step, Tensor arrays.

  This class is meant to be used with dynamic iteration primitives such as
  `while_loop` and `map_fn`.  It supports gradient back-propagation via special
  "flow" control flow dependencies.

  Note that although the array can be read multiple times and positions can be
  overwritten, behavior may be undefined when storing multiple references to
  the same array and clear_after_read is False. In particular, avoid using
  methods like concat() to convert an intermediate TensorArray to a Tensor,
  then further modifying the TensorArray, particularly if you need to backprop
  through it later.

  Example 1: Plain reading and writing.

  >>> ta = tf.TensorArray(tf.float32, size=0, dynamic_size=True, clear_after_read=False)
  >>> ta = ta.write(0, 10)
  >>> ta = ta.write(1, 20)
  >>> ta = ta.write(2, 30)
  >>>
  >>> ta.read(0)
  <tf.Tensor: shape=(), dtype=float32, numpy=10.0>
  >>> ta.read(1)
  <tf.Tensor: shape=(), dtype=float32, numpy=20.0>
  >>> ta.read(2)
  <tf.Tensor: shape=(), dtype=float32, numpy=30.0>
  >>> ta.stack()
  <tf.Tensor: shape=(3,), dtype=float32, numpy=array([10., 20., 30.],
  dtype=float32)>

  Example 2: Fibonacci sequence algorithm that writes in a loop then returns.

  >>> @tf.function
  ... def fibonacci(n):
  ...   ta = tf.TensorArray(tf.float32, size=0, dynamic_size=True)
  ...   ta = ta.unstack([0., 1.])
  ...
  ...   for i in range(2, n):
  ...     ta = ta.write(i, ta.read(i - 1) + ta.read(i - 2))
  ...
  ...   return ta.stack()
  >>>
  >>> fibonacci(7)
  <tf.Tensor: shape=(7,), dtype=float32,
  numpy=array([0., 1., 1., 2., 3., 5., 8.], dtype=float32)>

  Example 3: A simple loop interacting with a `tf.Variable`.

  >>> v = tf.Variable(1)
  >>> @tf.function
  ... def f(x):
  ...   ta = tf.TensorArray(tf.int32, size=0, dynamic_size=True)
  ...   for i in tf.range(x):
  ...     v.assign_add(i)
  ...     ta = ta.write(i, v)
  ...   return ta.stack()
  >>> f(5)
  <tf.Tensor: shape=(5,), dtype=int32, numpy=array([ 1,  2,  4,  7, 11],
  dtype=int32)>
  '''
    def __init__(self, dtype, size: Incomplete | None = None, dynamic_size: Incomplete | None = None, clear_after_read: Incomplete | None = None, tensor_array_name: Incomplete | None = None, handle: Incomplete | None = None, flow: Incomplete | None = None, infer_shape: bool = True, element_shape: Incomplete | None = None, colocate_with_first_write_call: bool = True, name: Incomplete | None = None) -> None:
        """Construct a new TensorArray or wrap an existing TensorArray handle.

    A note about the parameter `name`:

    The name of the `TensorArray` (even if passed in) is uniquified: each time
    a new `TensorArray` is created at runtime it is assigned its own name for
    the duration of the run.  This avoids name collisions if a `TensorArray`
    is created within a `while_loop`.

    Args:
      dtype: (required) data type of the TensorArray.
      size: (optional) int32 scalar `Tensor`: the size of the TensorArray.
        Required if handle is not provided.
      dynamic_size: (optional) Python bool: If true, writes to the TensorArray
        can grow the TensorArray past its initial size.  Default: False.
      clear_after_read: Boolean (optional, default: True).  If True, clear
        TensorArray values after reading them.  This disables read-many
        semantics, but allows early release of memory.
      tensor_array_name: (optional) Python string: the name of the TensorArray.
        This is used when creating the TensorArray handle.  If this value is
        set, handle should be None.
      handle: (optional) A `Tensor` handle to an existing TensorArray.  If this
        is set, tensor_array_name should be None. Only supported in graph mode.
      flow: (optional) A float `Tensor` scalar coming from an existing
        `TensorArray.flow`. Only supported in graph mode.
      infer_shape: (optional, default: True) If True, shape inference is
        enabled.  In this case, all elements must have the same shape.
      element_shape: (optional, default: None) A `TensorShape` object specifying
        the shape constraints of each of the elements of the TensorArray. Need
        not be fully defined.
      colocate_with_first_write_call: If `True`, the TensorArray will be
        colocated on the same device as the Tensor used on its first write
        (write operations include `write`, `unstack`, and `split`).  If `False`,
        the TensorArray will be placed on the device determined by the device
        context available during its initialization.
      name: A name for the operation (optional).

    Raises:
      ValueError: if both handle and tensor_array_name are provided.
      TypeError: if handle is provided but is not a Tensor.
    """
    @property
    def flow(self):
        """The flow `Tensor` forcing ops leading to this TensorArray state."""
    @property
    def dtype(self):
        """The data type of this TensorArray."""
    @property
    def handle(self):
        """The reference to the TensorArray."""
    @property
    def element_shape(self):
        """The `tf.TensorShape` of elements in this TensorArray."""
    @property
    def dynamic_size(self):
        """Python bool; if `True` the TensorArray can grow dynamically."""
    def identity(self):
        """Returns a TensorArray with the same content and properties.

    Returns:
      A new TensorArray object with flow that ensures the control dependencies
      from the contexts will become control dependencies for writes, reads, etc.
      Use this object for all subsequent operations.
    """
    def grad(self, source, flow: Incomplete | None = None, name: Incomplete | None = None): ...
    def read(self, index, name: Incomplete | None = None):
        """Read the value at location `index` in the TensorArray.

    Args:
      index: 0-D.  int32 tensor with the index to read from.
      name: A name for the operation (optional).

    Returns:
      The tensor at index `index`.
    """
    def write(self, index, value, name: Incomplete | None = None):
        """Write `value` into index `index` of the TensorArray.

    Args:
      index: 0-D.  int32 scalar with the index to write to.
      value: N-D.  Tensor of type `dtype`.  The Tensor to write to this index.
      name: A name for the operation (optional).

    Returns:
      A new TensorArray object with flow that ensures the write occurs.
      Use this object for all subsequent operations.

    Raises:
      ValueError: if there are more writers than specified.
    """
    def stack(self, name: Incomplete | None = None):
        """Return the values in the TensorArray as a stacked `Tensor`.

    All of the values must have been written and their shapes must all match.
    If input shapes have rank-`R`, then output shape will have rank-`(R+1)`.

    For example:


    >>> ta = tf.TensorArray(tf.int32, size=3)
    >>> ta = ta.write(0, tf.constant([1, 2]))
    >>> ta = ta.write(1, tf.constant([3, 4]))
    >>> ta = ta.write(2, tf.constant([5, 6]))
    >>> ta.stack()
    <tf.Tensor: shape=(3, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [5, 6]], dtype=int32)>


    Args:
      name: A name for the operation (optional).

    Returns:
      All the tensors in the TensorArray stacked into one tensor.
    """
    def gather(self, indices, name: Incomplete | None = None):
        """Return selected values in the TensorArray as a packed `Tensor`.

    All of selected values must have been written and their shapes
    must all match.

    Args:
      indices: A `1-D` `Tensor` taking values in `[0, max_value)`.  If the
        `TensorArray` is not dynamic, `max_value=size()`.
      name: A name for the operation (optional).

    Returns:
      The tensors in the `TensorArray` selected by `indices`, packed into one
      tensor.
    """
    def concat(self, name: Incomplete | None = None):
        """Return the values in the TensorArray as a concatenated `Tensor`.

    All of the values must have been written, their ranks must match, and
    and their shapes must all match for all dimensions except the first.

    Args:
      name: A name for the operation (optional).

    Returns:
      All the tensors in the TensorArray concatenated into one tensor.
    """
    def unstack(self, value, name: Incomplete | None = None):
        """Unstack the values of a `Tensor` in the TensorArray.

    If input value shapes have rank-`R`, then the output TensorArray will
    contain elements whose shapes are rank-`(R-1)`.

    Args:
      value: (N+1)-D.  Tensor of type `dtype`.  The Tensor to unstack.
      name: A name for the operation (optional).

    Returns:
      A new TensorArray object with flow that ensures the unstack occurs.
      Use this object for all subsequent operations.

    Raises:
      ValueError: if the shape inference fails.
    """
    def scatter(self, indices, value, name: Incomplete | None = None):
        """Scatter the values of a `Tensor` in specific indices of a `TensorArray`.

    Args:
      indices: A `1-D` `Tensor` taking values in `[0, max_value)`.  If the
        `TensorArray` is not dynamic, `max_value=size()`.
      value: (N+1)-D.  Tensor of type `dtype`.  The Tensor to unpack.
      name: A name for the operation (optional).

    Returns:
      A new TensorArray object with flow that ensures the scatter occurs.
      Use this object for all subsequent operations.

    Raises:
      ValueError: if the shape inference fails.
    """
    def split(self, value, lengths, name: Incomplete | None = None):
        """Split the values of a `Tensor` into the TensorArray.

    Args:
      value: (N+1)-D.  Tensor of type `dtype`.  The Tensor to split.
      lengths: 1-D.  int32 vector with the lengths to use when splitting `value`
        along its first dimension.
      name: A name for the operation (optional).

    Returns:
      A new TensorArray object with flow that ensures the split occurs.
      Use this object for all subsequent operations.

    Raises:
      ValueError: if the shape inference fails.
    """
    def size(self, name: Incomplete | None = None):
        """Return the size of the TensorArray."""
    def close(self, name: Incomplete | None = None):
        """Close the current TensorArray."""

def build_ta_with_new_flow(old_ta, flow):
    """Builds a TensorArray with a new `flow` tensor."""

class TensorArraySpec(type_spec.TypeSpec):
    """Type specification for a `tf.TensorArray`."""
    value_type: Incomplete
    def __init__(self, element_shape: Incomplete | None = None, dtype=..., dynamic_size: bool = False, infer_shape: bool = True) -> None:
        """Constructs a type specification for a `tf.TensorArray`.

    Args:
      element_shape: The shape of each element in the `TensorArray`.
      dtype: Data type of the `TensorArray`.
      dynamic_size: Whether the `TensorArray` can grow past its initial size.
      infer_shape: Whether shape inference is enabled.
    """
    def is_subtype_of(self, other): ...
    def most_specific_common_supertype(self, others):
        """Returns the most specific supertype of `self` and `others`.

    Args:
      others: A Sequence of `TypeSpec`.

    Returns `None` if a supertype does not exist.
    """
    def is_compatible_with(self, other): ...
    @staticmethod
    def from_value(value): ...
