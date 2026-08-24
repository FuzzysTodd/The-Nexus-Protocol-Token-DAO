import abc
from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, extension_type_field as extension_type_field, immutable_dict as immutable_dict, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, type_spec as type_spec, type_spec_registry as type_spec_registry
from tensorflow.python.ops import array_ops as array_ops, composite_tensor_ops as composite_tensor_ops, gen_math_ops as gen_math_ops, math_ops as math_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export

class ExtensionTypeMetaclass(abc.ABCMeta):
    """Metaclass for tf.ExtensionType types."""
    def __init__(cls, name, bases, namespace) -> None: ...

class ExtensionType(composite_tensor.CompositeTensor, metaclass=ExtensionTypeMetaclass):
    """Base class for TensorFlow `ExtensionType` classes.

  Tensorflow `ExtensionType` classes are specialized Python classes that can be
  used transparently with TensorFlow -- e.g., they can be used with ops
  such as `tf.cond` or `tf.while_loop` and used as inputs or outputs for
  `tf.function` and Keras layers.

  New `ExtensionType` classes are defined by creating a subclass of
  `tf.ExtensionType` that
  contains type annotations for all instance variables.  The following type
  annotations are supported:

  Type                 | Example
  -------------------- | --------------------------------------------
  Python integers      | `i: int`
  Python floats        | `f: float`
  Python strings       | `s: str`
  Python booleans      | `b: bool`
  Python None          | `n: None`
  Tensors              | `t: tf.Tensor`
  Composite Tensors    | `rt: tf.RaggedTensor`
  Extension Types      | `m: MyMaskedTensor`
  Tensor shapes        | `shape: tf.TensorShape`
  Tensor dtypes        | `dtype: tf.DType`
  Type unions          | `length: typing.Union[int, float]`
  Tuples               | `params: typing.Tuple[int, float, int, int]`
  Tuples w/ Ellipsis   | `lengths: typing.Tuple[int, ...]`
  Mappings             | `tags: typing.Mapping[str, str]`

  Fields annotated with `typing.Mapping` will be stored using an immutable
  mapping type.

  ExtensionType values are immutable -- i.e., once constructed, you can not
  modify or delete any of their instance members.

  ### Examples

  >>> class MaskedTensor(ExtensionType):
  ...   values: tf.Tensor
  ...   mask: tf.Tensor

  >>> class Toy(ExtensionType):
  ...   name: str
  ...   price: ops.Tensor
  ...   features: typing.Mapping[str, tf.Tensor]

  >>> class ToyStore(ExtensionType):
  ...   name: str
  ...   toys: typing.Tuple[Toy, ...]
  """
    def __init__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...
    def __getattr__(self, name): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __validate__(self) -> None:
        """Perform post-construction validation."""

def as_dict(value):
    """Extracts the attributes of `value` and their values to a dict format.

  Unlike `dataclasses.asdict()`, this function is not recursive and in case of
  nested `ExtensionType` objects, only the top level object is converted to a
  dict.

  Args:
    value: An `ExtensionType` object.

  Returns:
    A dict that contains the attributes of `value` and their values.
  """
def pack(value):
    """Returns a copy of `value` with fields packed in a single Variant.

  Args:
    value: An `ExtensionType` object.

  Returns:
    An `ExtensionType` object.
  """
def unpack(value):
    """Returns a copy of `value` with individual fields stored in __dict__.

  Args:
    value: An `ExtensionType` object.

  Returns:
    An `ExtensionType` object.
  """
def is_packed(value):
    """Returns true if `value`'s fields are packed in a single Variant."""

class ExtensionTypeSpec(type_spec.TypeSpec):
    """Base class for tf.ExtensionType TypeSpec."""
    def __reduce__(self): ...
    @classmethod
    def from_value(cls, value): ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...
    def __validate__(self) -> None:
        """Perform post-construction validation."""

class _ExtensionTypeSpecCodec:
    """Codec for `tf.ExtensionTypeSpec`."""
    def can_encode(self, pyobj):
        """Returns true if `pyobj` can be encoded as an ExtensionTypeSpec."""
    def do_encode(self, extension_type_spec_value, encode_fn):
        """Returns an encoded proto for the given `tf.ExtensionTypeSpec`."""
    def can_decode(self, value):
        """Returns true if `value` can be decoded into a `tf.ExtensionTypeSpec`."""
    def do_decode(self, value, decode_fn):
        """Returns the `tf.TypeSpec` encoded by the proto `value`."""

class ExtensionTypeBatchEncoder(type_spec.TypeSpecBatchEncoder):
    '''Class used to encode and decode extension type values for batching.

  In order to be batched and unbatched by APIs such as `tf.data.Dataset`,
  `tf.keras`, and `tf.map_fn`, extension type values must be encoded as a list
  of `tf.Tensor`s, where stacking, unstacking, or concatenating these encoded
  tensors and then decoding the result must be equivalent to stacking,
  unstacking, or concatenating the original values. `ExtensionTypeBatchEncoder`s
  are responsible for implementing this encoding.

  The default `ExtensionTypeBatchEncoder` that is used by
  `BatchableExtensionType` assumes that extension type values can be stacked,
  unstacked, or concatenated by simply stacking, unstacking, or concatenating
  every nested `Tensor`, `ExtensionType`, `CompositeTensor`, and `TensorShape`
  field.

  Extension types where this is not the case will need to override
  `__batch_encoder__` with a custom encoder that overrides the `batch`,
  `unbatch`, `encode`, and `decode` methods. E.g.:

  >>> class CustomBatchEncoder(ExtensionTypeBatchEncoder):
  ...   pass # Override batch(), unbatch(), encode(), and decode().

  >>> class CustomType(BatchableExtensionType):
  ...   x: tf.Tensor
  ...   y: tf.Tensor
  ...   shape: tf.TensorShape
  ...   __batch_encoder__ = CustomBatchEncoder()

  For example, `tf.RaggedTensor` and `tf.SparseTensor` both use custom batch
  encodings which define ops to "box" and "unbox" individual values into
  `tf.variant` tensors.
  '''
    def batch(self, spec, batch_size):
        """Returns the TypeSpec representing a batch of values described by `spec`.

    The default definition returns a `TypeSpec` that is equal to `spec`, except
    that an outer axis with size `batch_size` is added to every nested
    `TypeSpec` and `TensorShape` field.  Subclasses may override this default
    definition, when necessary.

    Args:
      spec: The `TypeSpec` for an individual value.
      batch_size: An `int` indicating the number of values that are batched
        together, or `None` if the batch size is not known.

    Returns:
      A `TypeSpec` for a batch of values.
    """
    def unbatch(self, spec):
        """Returns the TypeSpec for a single unbatched element in `spec`.

    The default definition returns a `TypeSpec` that is equal to `spec`, except
    that the outermost axis is removed from every nested `TypeSpec`, and
    `TensorShape` field.  Subclasses may override this default definition, when
    necessary.

    Args:
      spec: The `TypeSpec` for a batch of values.

    Returns:
      A `TypeSpec` for an individual value.
    """
    def encode(self, spec, value, minimum_rank: int = 0):
        """Encodes `value` as a nest of batchable Tensors or CompositeTensors.

    The default definition returns a flat tuple of all the `Tensor`s,
    `CompositeTensor`s, and `ExtensionType`s from a depth-first traversal of
    `value`'s fields. Subclasses may override this default definition, when
    necessary.

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
    def decode(self, spec, encoded_value):
        """Decodes `value` from a batchable tensor encoding.

    See `encode` for a description of the default encoding.  Subclasses may
    override this default definition, when necessary.

    Args:
      spec: The TypeSpec for the result value.  If encoded values with spec `s`
        were batched, then `spec` should be `s.batch(batch_size)`; or if encoded
        values with spec `s` were unbatched, then `spec` should be
        `s.unbatch()`.
      encoded_value: A nest of values returned by `encode`; or a nest of
        values that was formed by stacking, unstacking, or concatenating the
        corresponding elements of values returned by `encode`.

    Returns:
      A value compatible with `type_spec`.
    """
    def encoding_specs(self, spec):
        """Returns a list of `TensorSpec`(s) describing the encoding for `spec`.

    See `encode` for a description of the default encoding.  Subclasses may
    override this default definition, when necessary.

    Args:
      spec: The TypeSpec whose encoding should be described.

    Returns:
      A nest (as defined by `tf.nest) of `tf.TypeSpec`, describing the values
      that are returned by `self.encode(spec, ...)`.  All TypeSpecs in this
      nest must be batchable.
    """

class BatchableExtensionTypeSpec(ExtensionTypeSpec, type_spec.BatchableTypeSpec):
    """Base class for TypeSpecs for BatchableExtensionTypes."""
    __batch_encoder__: Incomplete

class BatchableExtensionType(ExtensionType):
    """An ExtensionType that can be batched and unbatched.

  `BatchableExtensionType`s can be used with APIs that require batching or
  unbatching, including `Keras`, `tf.data.Dataset`, and `tf.map_fn`.  E.g.:

  >>> class Vehicle(tf.experimental.BatchableExtensionType):
  ...   top_speed: tf.Tensor
  ...   mpg: tf.Tensor
  >>> batch = Vehicle([120, 150, 80], [30, 40, 12])
  >>> tf.map_fn(lambda vehicle: vehicle.top_speed * vehicle.mpg, batch,
  ...           fn_output_signature=tf.int32).numpy()
  array([3600, 6000,  960], dtype=int32)

  An `ExtensionTypeBatchEncoder` is used by these APIs to encode `ExtensionType`
  values. The default encoder assumes that values can be stacked, unstacked, or
  concatenated by simply stacking, unstacking, or concatenating every nested
  `Tensor`, `ExtensionType`, `CompositeTensor`, or `TensorShape` field.
  Extension types where this is not the case will need to override
  `__batch_encoder__` with a custom `ExtensionTypeBatchEncoder`.  See
  `tf.experimental.ExtensionTypeBatchEncoder` for more details.
  """

class AnonymousExtensionType(ExtensionType):
    """Fallback used to decode `tf.ExtensionType` when the original type is unavailable.

  When a SavedModel is serialized, the signatures of any functions in the
  SavedModel can include `tf.ExtensionType` subclasses.  These subclasses are
  usually
  registered, so they can be restored when the SavedModel is loaded.  However,
  if a SavedModel is loaded without first registering the ExtensionType types in
  its
  signature, then the SavedModel will fall back to using the
  `AnonymousExtensionType`
  type instead.

  If necessary, `AnonymousExtensionType` objects can be converted to a concrete
  `tf.ExtensionType` subclass (and vice versa) using `reinterpret`.
  """
    def __init__(self, **fields) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...

class AnonymousExtensionTypeSpec(ExtensionTypeSpec):
    """TypeSpec for AnonymousExtensionType."""
    def __init__(self, **fields) -> None: ...
    value_type = AnonymousExtensionType
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...

def reinterpret(value, new_type):
    """Converts a given `ExtensionType` to a new type with compatible fields.

  In particular, this can be used to convert a concrete subclass of
  `ExtensionType` to an `AnonymousExtensionType`, or vice versa.  When
  converting to a non-anonymous ExtensionType, field values are type-checked to
  ensure they are consistent with `new_type`'s type annotations, and validated
  with `new_type.__validate__`.

  Args:
    value: An instance of a subclass of `tf.ExtensionType`
    new_type: A subclass of `tf.ExtensionType`

  Returns:
    An instance of `new_type`, whose fields are copied from `value`.
  """
