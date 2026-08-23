from _typeshed import Incomplete
from tensorflow.core.protobuf import struct_pb2 as struct_pb2
from tensorflow.python.framework import dtypes as dtypes, tensor_shape as tensor_shape, type_spec_registry as type_spec_registry
from tensorflow.python.types import internal as internal
from tensorflow.python.util import compat as compat, nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

class NotEncodableError(Exception):
    """Error raised when a coder cannot encode an object."""

def register_codec(x) -> None:
    """Registers a codec to use for encoding/decoding.

  Args:
    x: The codec object to register. The object must implement can_encode,
      do_encode, can_decode, and do_decode. See the various _*Codec classes for
      examples.
  """
def encode_structure(nested_structure):
    """Encodes nested structures composed of encodable types into a proto.

  Args:
    nested_structure: Structure to encode.

  Returns:
    Encoded proto.

  Raises:
    NotEncodableError: For values for which there are no encoders.
  """
def can_encode(nested_structure):
    """Determines whether a nested structure can be encoded into a proto.

  Args:
    nested_structure: Structure to encode.

  Returns:
    True if the nested structured can be encoded.
  """
def decode_proto(proto):
    """Decodes proto representing a nested structure.

  Args:
    proto: Proto to decode.

  Returns:
    Decoded structure.

  Raises:
    NotEncodableError: For values for which there are no encoders.
  """

class _ListCodec:
    """Codec for lists."""
    def can_encode(self, pyobj): ...
    def do_encode(self, list_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _TupleCodec:
    """Codec for tuples."""
    def can_encode(self, pyobj): ...
    def do_encode(self, tuple_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _DictCodec:
    """Codec for dicts."""
    def can_encode(self, pyobj): ...
    def do_encode(self, dict_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _NamedTupleCodec:
    """Codec for namedtuples.

  Encoding and decoding a namedtuple reconstructs a namedtuple with a different
  actual Python type, but with the same `typename` and `fields`.
  """
    def can_encode(self, pyobj): ...
    def do_encode(self, named_tuple_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _Float64Codec:
    """Codec for floats."""
    def can_encode(self, pyobj): ...
    def do_encode(self, float64_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _Int64Codec:
    """Codec for Python integers (limited to 64 bit values)."""
    def can_encode(self, pyobj): ...
    def do_encode(self, int_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _StringCodec:
    """Codec for strings.

  See StructuredValue.string_value in proto/struct.proto for more detailed
  explanation.
  """
    def can_encode(self, pyobj): ...
    def do_encode(self, string_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _NoneCodec:
    """Codec for None."""
    def can_encode(self, pyobj): ...
    def do_encode(self, none_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn) -> None: ...

class _BoolCodec:
    """Codec for booleans."""
    def can_encode(self, pyobj): ...
    def do_encode(self, bool_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _TensorShapeCodec:
    """Codec for `TensorShape`."""
    def can_encode(self, pyobj): ...
    def do_encode(self, tensor_shape_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class _TensorTypeCodec:
    """Codec for `TensorType`."""
    def can_encode(self, pyobj): ...
    def do_encode(self, tensor_dtype_value, encode_fn): ...
    def can_decode(self, value): ...
    def do_decode(self, value, decode_fn): ...

class BuiltInTypeSpecCodec:
    """Codec for built-in `TypeSpec` classes.

  Built-in TypeSpec's that do not require a custom codec implementation
  register themselves by instantiating this class and passing it to
  register_codec.

  Attributes:
    type_spec_class: The built-in TypeSpec class that the
      codec is instantiated for.
    type_spec_proto_enum: The proto enum value for the built-in TypeSpec class.
  """
    type_spec_class: Incomplete
    type_spec_proto_enum: Incomplete
    def __init__(self, type_spec_class, type_spec_proto_enum) -> None: ...
    def can_encode(self, pyobj):
        """Returns true if `pyobj` can be encoded as the built-in TypeSpec."""
    def do_encode(self, type_spec_value, encode_fn):
        """Returns an encoded proto for the given built-in TypeSpec."""
    def can_decode(self, value):
        """Returns true if `value` can be decoded into its built-in TypeSpec."""
    def do_decode(self, value, decode_fn):
        """Returns the built in `TypeSpec` encoded by the proto `value`."""

class _TypeSpecCodec:
    """Codec for `tf.TypeSpec`."""
    TYPE_SPEC_CLASS_FROM_PROTO: Incomplete
    TYPE_SPEC_CLASS_TO_PROTO: Incomplete
    def can_encode(self, pyobj):
        """Returns true if `pyobj` can be encoded as a TypeSpec."""
    def do_encode(self, type_spec_value, encode_fn):
        """Returns an encoded proto for the given `tf.TypeSpec`."""
    def can_decode(self, value):
        """Returns true if `value` can be decoded into a `tf.TypeSpec`."""
    def do_decode(self, value, decode_fn):
        """Returns the `tf.TypeSpec` encoded by the proto `value`."""
