import abc
from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.framework import common_shapes as common_shapes, dtypes as dtypes, op_callbacks as op_callbacks, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util, type_spec as type_spec, type_spec_registry as type_spec_registry
from tensorflow.python.ops import handle_data_util as handle_data_util
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.types import internal as internal
from tensorflow.python.util import compat as compat
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Type

def sanitize_spec_name(name: str) -> str:
    """Sanitizes Spec names. Matches Graph Node and Python naming conventions.

  Without sanitization, names that are not legal Python parameter names can be
  set which makes it challenging to represent callables supporting the named
  calling capability.

  Args:
    name: The name to sanitize.

  Returns:
    A string that meets Python parameter conventions.
  """

class DenseSpec(type_spec.TypeSpec, metaclass=abc.ABCMeta):
    """Describes a dense object with shape, dtype, and name."""
    def __init__(self, shape, dtype=..., name: Incomplete | None = None) -> None:
        """Creates a TensorSpec.

    Args:
      shape: Value convertible to `tf.TensorShape`. The shape of the tensor.
      dtype: Value convertible to `tf.DType`. The type of the tensor values.
      name: Optional name for the Tensor.

    Raises:
      TypeError: If shape is not convertible to a `tf.TensorShape`, or dtype is
        not convertible to a `tf.DType`.
    """
    @property
    def shape(self):
        """Returns the `TensorShape` that represents the shape of the tensor."""
    @property
    def dtype(self):
        """Returns the `dtype` of elements in the tensor."""
    @property
    def name(self):
        """Returns the (optionally provided) name of the described tensor."""
    def is_compatible_with(self, spec_or_value): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class TensorSpec(DenseSpec, type_spec.BatchableTypeSpec, trace_type.Serializable, internal.TensorSpec):
    '''Describes the type of a tf.Tensor.

  >>> t = tf.constant([[1,2,3],[4,5,6]])
  >>> tf.TensorSpec.from_tensor(t)
  TensorSpec(shape=(2, 3), dtype=tf.int32, name=None)

  Contains metadata for describing the the nature of `tf.Tensor` objects
  accepted or returned by some TensorFlow APIs.

  For example, it can be used to constrain the type of inputs accepted by
  a tf.function:

  >>> @tf.function(input_signature=[tf.TensorSpec([1, None])])
  ... def constrained_foo(t):
  ...   print("tracing...")
  ...   return t

  Now the `tf.function` is able to assume that `t` is always of the type
  `tf.TensorSpec([1, None])` which will avoid retracing as well as enforce the
  type restriction on inputs.

  As a result, the following call with tensor of type `tf.TensorSpec([1, 2])`
  triggers a trace and succeeds:
  >>> constrained_foo(tf.constant([[1., 2]])).numpy()
  tracing...
  array([[1., 2.]], dtype=float32)

  The following subsequent call with tensor of type `tf.TensorSpec([1, 4])`
  does not trigger a trace and succeeds:
  >>> constrained_foo(tf.constant([[1., 2, 3, 4]])).numpy()
  array([[1., 2., 3., 4.], dtype=float32)

  But the following call with tensor of type `tf.TensorSpec([2, 2])` fails:
  >>> constrained_foo(tf.constant([[1., 2], [3, 4]])).numpy()
  Traceback (most recent call last):
  ...
  ValueError: Python inputs incompatible with input_signature

  '''
    @classmethod
    def experimental_type_proto(cls) -> Type[struct_pb2.TensorSpecProto]:
        """Returns the type of proto associated with TensorSpec serialization."""
    @classmethod
    def experimental_from_proto(cls, proto: struct_pb2.TensorSpecProto) -> TensorSpec:
        """Returns a TensorSpec instance based on the serialized proto."""
    def experimental_as_proto(self) -> struct_pb2.TensorSpecProto:
        """Returns a proto representation of the TensorSpec instance."""
    def is_compatible_with(self, spec_or_tensor):
        """Returns True if spec_or_tensor is compatible with this TensorSpec.

    Two tensors are considered compatible if they have the same dtype
    and their shapes are compatible (see `tf.TensorShape.is_compatible_with`).

    Args:
      spec_or_tensor: A tf.TensorSpec or a tf.Tensor

    Returns:
      True if spec_or_tensor is compatible with self.
    """
    def placeholder_value(self, placeholder_context):
        """Generates a graph_placholder with the given TensorSpec information."""
    @classmethod
    def from_spec(cls, spec, name: Incomplete | None = None):
        '''Returns a `TensorSpec` with the same shape and dtype as `spec`.

    >>> spec = tf.TensorSpec(shape=[8, 3], dtype=tf.int32, name="OriginalName")
    >>> tf.TensorSpec.from_spec(spec, "NewName")
    TensorSpec(shape=(8, 3), dtype=tf.int32, name=\'NewName\')

    Args:
      spec: The `TypeSpec` used to create the new `TensorSpec`.
      name: The name for the new `TensorSpec`.  Defaults to `spec.name`.
    '''
    @classmethod
    def from_tensor(cls, tensor, name: Incomplete | None = None):
        """Returns a `TensorSpec` that describes `tensor`.

    >>> tf.TensorSpec.from_tensor(tf.constant([1, 2, 3]))
    TensorSpec(shape=(3,), dtype=tf.int32, name=None)

    Args:
      tensor: The `tf.Tensor` that should be described.
      name: A name for the `TensorSpec`.  Defaults to `tensor.op.name`.

    Returns:
      A `TensorSpec` that describes `tensor`.
    """
    @property
    def value_type(self):
        """The Python type for values that are compatible with this TypeSpec."""

class _TensorSpecCodec:
    """Codec for `TensorSpec`."""
    def can_encode(self, pyobj): ...
    def do_encode(self, tensor_spec_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class BoundedTensorSpec(TensorSpec, trace_type.Serializable):
    """A `TensorSpec` that specifies minimum and maximum values.

  Example usage:
  ```python
  spec = tensor_spec.BoundedTensorSpec((1, 2, 3), tf.float32, 0, (5, 5, 5))
  tf_minimum = tf.convert_to_tensor(spec.minimum, dtype=spec.dtype)
  tf_maximum = tf.convert_to_tensor(spec.maximum, dtype=spec.dtype)
  ```

  Bounds are meant to be inclusive. This is especially important for
  integer types. The following spec will be satisfied by tensors
  with values in the set {0, 1, 2}:
  ```python
  spec = tensor_spec.BoundedTensorSpec((3, 5), tf.int32, 0, 2)
  ```
  """
    def __init__(self, shape, dtype, minimum, maximum, name: Incomplete | None = None) -> None:
        """Initializes a new `BoundedTensorSpec`.

    Args:
      shape: Value convertible to `tf.TensorShape`. The shape of the tensor.
      dtype: Value convertible to `tf.DType`. The type of the tensor values.
      minimum: Number or sequence specifying the minimum element bounds
        (inclusive). Must be broadcastable to `shape`.
      maximum: Number or sequence specifying the maximum element bounds
        (inclusive). Must be broadcastable to `shape`.
      name: Optional string containing a semantic name for the corresponding
        array. Defaults to `None`.

    Raises:
      ValueError: If `minimum` or `maximum` are not provided or not
        broadcastable to `shape`.
      TypeError: If the shape is not an iterable or if the `dtype` is an invalid
        numpy dtype.
    """
    @classmethod
    def experimental_type_proto(cls) -> Type[struct_pb2.BoundedTensorSpecProto]:
        """Returns the type of proto associated with BoundedTensorSpec serialization."""
    @classmethod
    def experimental_from_proto(cls, proto: struct_pb2.BoundedTensorSpecProto) -> BoundedTensorSpec:
        """Returns a BoundedTensorSpec instance based on the serialized proto."""
    def experimental_as_proto(self) -> struct_pb2.BoundedTensorSpecProto:
        """Returns a proto representation of the BoundedTensorSpec instance."""
    @classmethod
    def from_spec(cls, spec):
        '''Returns a `TensorSpec` with the same shape and dtype as `spec`.

    If `spec` is a `BoundedTensorSpec`, then the new spec\'s bounds are set to
    `spec.minimum` and `spec.maximum`; otherwise, the bounds are set to
    `spec.dtype.min` and `spec.dtype.max`.

    >>> spec = tf.TensorSpec(shape=[8, 3], dtype=tf.int32, name="x")
    >>> BoundedTensorSpec.from_spec(spec)
    BoundedTensorSpec(shape=(8, 3), dtype=tf.int32, name=\'x\',
        minimum=array(-2147483648, dtype=int32),
        maximum=array(2147483647, dtype=int32))

    Args:
      spec: The `TypeSpec` used to create the new `BoundedTensorSpec`.
    '''
    @property
    def minimum(self):
        """Returns a NumPy array specifying the minimum bounds (inclusive)."""
    @property
    def maximum(self):
        """Returns a NumPy array specifying the maximum bounds (inclusive)."""
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __reduce__(self): ...

class _BoundedTensorSpecCodec:
    """Codec for `BoundedTensorSpec`."""
    def can_encode(self, pyobj): ...
    def do_encode(self, bounded_tensor_spec_value, encode_fn):
        """Returns an encoded proto for the given `tf.BoundedTensorSpec`."""
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...
