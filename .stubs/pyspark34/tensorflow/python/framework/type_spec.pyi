import abc
from _typeshed import Incomplete
from tensorflow.core.function import trace_type as trace_type
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, tensor_shape as tensor_shape, type_spec_registry as type_spec_registry
from tensorflow.python.types import internal as internal, trace as trace
from tensorflow.python.util import compat as compat, deprecation as deprecation, nest as nest, tf_decorator as tf_decorator
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Optional, Sequence, Type

ops: Incomplete
nested_structure_coder: Incomplete

class TypeSpec(internal.TypeSpec, trace.TraceType, trace_type.Serializable, metaclass=abc.ABCMeta):
    """Specifies a TensorFlow value type.

  A `tf.TypeSpec` provides metadata describing an object accepted or returned
  by TensorFlow APIs.  Concrete subclasses, such as `tf.TensorSpec` and
  `tf.RaggedTensorSpec`, are used to describe different value types.

  For example, `tf.function`'s `input_signature` argument accepts a list
  (or nested structure) of `TypeSpec`s.

  Creating new subclasses of `TypeSpec` (outside of TensorFlow core) is not
  currently supported.  In particular, we may make breaking changes to the
  private methods and properties defined by this base class.

  Example:

  >>> spec = tf.TensorSpec(shape=[None, None], dtype=tf.int32)
  >>> @tf.function(input_signature=[spec])
  ... def double(x):
  ...   return x * 2
  >>> double(tf.constant([[1, 2], [3, 4]]))
  <tf.Tensor: shape=(2, 2), dtype=int32,
      numpy=array([[2, 4], [6, 8]], dtype=int32)>
  """
    @property
    @abc.abstractmethod
    def value_type(self):
        """The Python type for values that are compatible with this TypeSpec.

    In particular, all values that are compatible with this TypeSpec must be an
    instance of this type.
    """
    def is_subtype_of(self, other: trace.TraceType) -> bool:
        """Returns True if `self` is a subtype of `other`.

    Implements the tf.types.experimental.func.TraceType interface.

    If not overridden by a subclass, the default behavior is to assume the
    TypeSpec is covariant upon attributes that implement TraceType and
    invariant upon rest of the attributes as well as the structure and type
    of the TypeSpec.

    Args:
      other: A TraceType object.
    """
    def most_specific_common_supertype(self, others: Sequence[trace.TraceType]) -> Optional['TypeSpec']:
        """Returns the most specific supertype TypeSpec  of `self` and `others`.

    Implements the tf.types.experimental.func.TraceType interface.

    If not overridden by a subclass, the default behavior is to assume the
    TypeSpec is covariant upon attributes that implement TraceType and
    invariant upon rest of the attributes as well as the structure and type
    of the TypeSpec.

    Args:
      others: A sequence of TraceTypes.
    """
    @classmethod
    def experimental_type_proto(cls) -> Type[struct_pb2.TypeSpecProto]:
        """Returns the type of proto associated with TypeSpec serialization.

    Do NOT override for custom non-TF types.
    """
    @classmethod
    def experimental_from_proto(cls, proto: struct_pb2.TypeSpecProto) -> TypeSpec:
        """Returns a TypeSpec instance based on the serialized proto.

    Do NOT override for custom non-TF types.

    Args:
      proto: Proto generated using 'experimental_as_proto'.
    """
    def experimental_as_proto(self) -> struct_pb2.TypeSpecProto:
        """Returns a proto representation of the TypeSpec instance.

    Do NOT override for custom non-TF types.
    """
    def placeholder_value(self, placeholder_context):
        """Value used for tracing a function signature with this TraceType.

    WARNING: Do not override.

    Args:
      placeholder_context: A class container for context information when
        creating a placeholder value.

    Returns:
      A `CompositeTensor` placeholder whose components are recursively composed
        of placeholders themselves.
    """
    def is_compatible_with(self, spec_or_value):
        '''Returns true if `spec_or_value` is compatible with this TypeSpec.

    Prefer using "is_subtype_of" and "most_specific_common_supertype" wherever
    possible.

    Args:
      spec_or_value: A TypeSpec or TypeSpec associated value to compare against.
    '''
    def most_specific_compatible_type(self, other: TypeSpec) -> TypeSpec:
        """Returns the most specific TypeSpec compatible with `self` and `other`.

    Deprecated. Please use `most_specific_common_supertype` instead.
    Do not override this function.

    Args:
      other: A `TypeSpec`.

    Raises:
      ValueError: If there is no TypeSpec that is compatible with both `self`
        and `other`.
    """
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __reduce__(self): ...
    def __tf_tracing_type__(self, context: trace.TracingContext) -> trace.TraceType: ...

class TypeSpecBatchEncoder(metaclass=abc.ABCMeta):
    """Class used to encode and decode composite tensor values for batching.

  In order to be batched and unbatched by APIs such as `tf.data.Dataset` and
  `tf.map_fn`, composite tensors must be encoded using flat tensors that can
  themselves be batched or unbatched.  `TypeSpecBatchEncoder`s are
  responsible for implementing this encoding.

  If a composite tensor's shape is a prefix of the shape of all of its
  component tensors, then this encoding can usually be performed by just
  returning those component tensors as a list.  But if the composite tensor
  has components whose shape has a more complex relationship to the shape
  of the composite tensor, then a custom `TypeSpecBatchEncoder` may
  need to be implemented.
  """
    @abc.abstractmethod
    def batch(self, spec, batch_size):
        """Returns the TypeSpec representing a batch of values described by `spec`.

    Args:
      spec: The `TypeSpec` for an individual value.
      batch_size: An `int` indicating the number of values that are batched
        together, or `None` if the batch size is not known.

    Returns:
      A `TypeSpec` for a batch of values.
    """
    @abc.abstractmethod
    def unbatch(self, spec):
        """Returns the TypeSpec for a single unbatched element in `spec`.

    Args:
      spec: The `TypeSpec` for a batch of values.

    Returns:
      A `TypeSpec` for an individual value.
    """
    @abc.abstractmethod
    def encode(self, spec, value, minimum_rank: int = 0):
        """Encodes `value` as a nest of batchable `Tensor` or `CompositeTensor`.

    Args:
      spec: The TypeSpec of the value to encode.
      value: A value compatible with `spec`.
      minimum_rank: The minimum rank for the returned Tensors, CompositeTensors,
        and ExtensionType values.  This can be used to ensure that the encoded
        values can be unbatched this number of times.   If `minimum_rank>0`,
        then `t.shape[:minimum_rank]` must be compatible for all values `t`
        returned by `encode`.

    Returns:
      A nest (as defined by `tf.nest`) of `tf.Tensor`s, batchable
      `tf.CompositeTensor`s, or `tf.ExtensionType`s.  Stacking, unstacking, or
      concatenating these encoded values and then decoding the result must be
      equivalent to stacking, unstacking, or concatenating the original values.
    """
    @abc.abstractmethod
    def decode(self, spec, encoded_value):
        """Decodes `value` from a batchable tensor encoding.

    Args:
      spec: The TypeSpec for the result value.  If encoded values with spec `s`
        were batched, then `spec` should be `s.batch(batch_size)`; or if encoded
        values with spec `s` were unbatched, then `spec` should be
        `s.unbatch()`.
      encoded_value: A nest of values returned by `encode`; or a nest of values
        that was formed by stacking, unstacking, or concatenating the
        corresponding elements of values returned by `encode`.

    Returns:
      A value compatible with `type_spec`.
    """
    @abc.abstractmethod
    def encoding_specs(self, spec):
        """Returns a nest of `TypeSpec`(s) describing the encoding for `spec`.

    Args:
      spec: The TypeSpec whose encoding should be described.

    Returns:
      A nest (as defined by `tf.nest) of `tf.TypeSpec`, describing the values
      that are returned by `self.encode(spec, ...)`.  All TypeSpecs in this
      nest must be batchable.
    """

class LegacyTypeSpecBatchEncoder(TypeSpecBatchEncoder):
    """TypeSpecBatchEncoder for legacy composite tensor classes.

  TODO(edloper): Update existing composite tensors to use non-legacy
    CompositTensorBatchEncoders.
  """
    def batch(self, type_spec, batch_size): ...
    def unbatch(self, type_spec): ...
    def encode(self, type_spec, value, minimum_rank: int = 0): ...
    def decode(self, type_spec, encoded_value): ...
    def encoding_specs(self, spec): ...

class BatchableTypeSpec(TypeSpec, metaclass=abc.ABCMeta):
    """TypeSpec with a batchable tensor encoding.

  The batchable tensor encoding is a list of `tf.Tensor`s that supports
  batching and unbatching.  In particular, stacking (or unstacking)
  values with the same `TypeSpec` must be equivalent to stacking (or
  unstacking) each of their tensor lists.  Unlike the component encoding
  (returned by `self._to_components)`, the batchable tensor encoding
  may require using encoding/decoding ops.

  If a subclass's batchable tensor encoding is not simply a flattened version
  of the component encoding, then the subclass must override `_to_tensor_list`,
  `_from_tensor_list`, and _flat_tensor_specs`.
  """
    __batch_encoder__: Incomplete

def get_batchable_flat_tensor_specs(spec, context_spec: Incomplete | None = None):
    """Returns the flat tensor specs for `spec`."""
def batchable_to_tensor_list(spec, value, minimum_rank: int = 0):
    """Returns a list of tensors encoding `value`, whose type is `spec`."""
def batchable_from_tensor_list(spec, tensor_list):
    """Returns a value with type `spec` decoded from `tensor_list`."""
def type_spec_from_value(value) -> TypeSpec:
    """Returns a `tf.TypeSpec` that represents the given `value`.

  Examples:

    >>> tf.type_spec_from_value(tf.constant([1, 2, 3]))
    TensorSpec(shape=(3,), dtype=tf.int32, name=None)
    >>> tf.type_spec_from_value(np.array([4.0, 5.0], np.float64))
    TensorSpec(shape=(2,), dtype=tf.float64, name=None)
    >>> tf.type_spec_from_value(tf.ragged.constant([[1, 2], [3, 4, 5]]))
    RaggedTensorSpec(TensorShape([2, None]), tf.int32, 1, tf.int64)

    >>> example_input = tf.ragged.constant([[1, 2], [3]])
    >>> @tf.function(input_signature=[tf.type_spec_from_value(example_input)])
    ... def f(x):
    ...   return tf.reduce_sum(x, axis=1)

  Args:
    value: A value that can be accepted or returned by TensorFlow APIs. Accepted
      types for `value` include `tf.Tensor`, any value that can be converted to
      `tf.Tensor` using `tf.convert_to_tensor`, and any subclass of
      `CompositeTensor` (such as `tf.RaggedTensor`).

  Returns:
    A `TypeSpec` that is compatible with `value`.

  Raises:
    TypeError: If a TypeSpec cannot be built for `value`, because its type
      is not supported.
  """
def register_type_spec_from_value_converter(type_object, converter_fn, allow_subclass: bool = False) -> None:
    """Registers a function for converting values with a given type to TypeSpecs.

  If multiple registered `type_object`s match a value, then the most recent
  registration takes precedence.  Custom converters should not be defined for
  `CompositeTensor`s; use `CompositeTensor._type_spec` instead.

  Args:
    type_object: A Python `type` object representing the type of values accepted
      by `converter_fn`.
    converter_fn: A function that takes one argument (an instance of the type
      represented by `type_object`) and returns a `TypeSpec`.
    allow_subclass: If true, then use `isinstance(value, type_object)` to check
      for matches.  If false, then use `type(value) is type_object`.
  """
lookup = type_spec_registry.lookup
get_name = type_spec_registry.get_name
register = type_spec_registry.register
