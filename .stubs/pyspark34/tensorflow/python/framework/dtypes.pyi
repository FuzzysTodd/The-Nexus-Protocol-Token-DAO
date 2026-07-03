import abc
from _typeshed import Incomplete
from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.core.function import trace_type as trace_type
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.framework import _dtypes
from tensorflow.python.types import doc_typealias as doc_typealias, trace as trace
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import Optional, Sequence, Type

class DTypeMeta(Incomplete, abc.ABCMeta): ...

class DType(_dtypes.DType, trace.TraceType, trace_type.Serializable, metaclass=DTypeMeta):
    """Represents the type of the elements in a `Tensor`.

  `DType`'s are used to specify the output data type for operations which
  require it, or to inspect the data type of existing `Tensor`'s.

  Examples:

  >>> tf.constant(1, dtype=tf.int64)
  <tf.Tensor: shape=(), dtype=int64, numpy=1>
  >>> tf.constant(1.0).dtype
  tf.float32

  See `tf.dtypes` for a complete list of `DType`'s defined.
  """
    @property
    def base_dtype(self):
        """Returns a non-reference `DType` based on this `DType`."""
    @property
    def real_dtype(self):
        """Returns the `DType` corresponding to this `DType`'s real part."""
    @property
    def as_numpy_dtype(self):
        """Returns a Python `type` object based on this `DType`."""
    @property
    def min(self):
        """Returns the minimum representable value in this data type.

    Raises:
      TypeError: if this is a non-numeric, unordered, or quantized type.

    """
    @property
    def max(self):
        """Returns the maximum representable value in this data type.

    Raises:
      TypeError: if this is a non-numeric, unordered, or quantized type.

    """
    @property
    def limits(self, clip_negative: bool = True):
        """Return intensity limits, i.e.

    (min, max) tuple, of the dtype.
    Args:
      clip_negative : bool, optional If True, clip the negative range (i.e.
        return 0 for min intensity) even if the image dtype allows negative
        values. Returns
      min, max : tuple Lower and upper intensity limits.
    """
    def is_compatible_with(self, other):
        """Returns True if the `other` DType will be converted to this DType.

    The conversion rules are as follows:

    ```python
    DType(T)       .is_compatible_with(DType(T))        == True
    ```

    Args:
      other: A `DType` (or object that may be converted to a `DType`).

    Returns:
      True if a Tensor of the `other` `DType` will be implicitly converted to
      this `DType`.
    """
    def is_subtype_of(self, other: trace.TraceType) -> bool:
        """See tf.types.experimental.TraceType base class."""
    def most_specific_common_supertype(self, types: Sequence[trace.TraceType]) -> Optional['DType']:
        """See tf.types.experimental.TraceType base class."""
    def placeholder_value(self, placeholder_context: Incomplete | None = None) -> None:
        """TensorShape does not support placeholder values."""
    @classmethod
    def experimental_type_proto(cls) -> Type[types_pb2.SerializedDType]:
        """Returns the type of proto associated with DType serialization."""
    @classmethod
    def experimental_from_proto(cls, proto: types_pb2.SerializedDType) -> DType:
        """Returns a Dtype instance based on the serialized proto."""
    def experimental_as_proto(self) -> types_pb2.SerializedDType:
        """Returns a proto representation of the Dtype instance."""
    def __eq__(self, other):
        """Returns True iff this DType refers to the same type as `other`."""
    def __ne__(self, other):
        """Returns True iff self != other."""
    __hash__: Incomplete
    def __reduce__(self): ...

dtype_range: Incomplete
resource: Incomplete
variant: Incomplete
uint8: Incomplete
uint16: Incomplete
uint32: Incomplete
uint64: Incomplete
int8: Incomplete
int16: Incomplete
int32: Incomplete
int64: Incomplete
float16: Incomplete
half = float16
float32: Incomplete
float64: Incomplete
double = float64
complex64: Incomplete
complex128: Incomplete
string: Incomplete
bool: Incomplete
qint8: Incomplete
qint16: Incomplete
qint32: Incomplete
quint8: Incomplete
quint16: Incomplete
bfloat16: Incomplete
float8_e5m2: Incomplete
float8_e4m3fn: Incomplete
resource_ref: Incomplete
variant_ref: Incomplete
float16_ref: Incomplete
half_ref = float16_ref
float32_ref: Incomplete
float64_ref: Incomplete
double_ref = float64_ref
int32_ref: Incomplete
uint32_ref: Incomplete
uint8_ref: Incomplete
uint16_ref: Incomplete
int16_ref: Incomplete
int8_ref: Incomplete
string_ref: Incomplete
complex64_ref: Incomplete
complex128_ref: Incomplete
int64_ref: Incomplete
uint64_ref: Incomplete
bool_ref: Incomplete
qint8_ref: Incomplete
quint8_ref: Incomplete
qint16_ref: Incomplete
quint16_ref: Incomplete
qint32_ref: Incomplete
bfloat16_ref: Incomplete
float8_e5m2_ref: Incomplete
float8_e4m3fn_ref: Incomplete
np_resource: Incomplete
TF_VALUE_DTYPES: Incomplete
QUANTIZED_DTYPES: Incomplete

def as_dtype(type_value):
    """Converts the given `type_value` to a `tf.DType`.

  Inputs can be existing `tf.DType` objects, a [`DataType`
  enum](https://www.tensorflow.org/code/tensorflow/core/framework/types.proto),
  a string type name, or a
  [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html).

  Examples:
  >>> tf.as_dtype(2)  # Enum value for float64.
  tf.float64

  >>> tf.as_dtype('float')
  tf.float32

  >>> tf.as_dtype(np.int32)
  tf.int32

  Note: `DType` values are interned (i.e. a single instance of each dtype is
  stored in a map). When passed a new `DType` object, `as_dtype` always returns
  the interned value.

  Args:
    type_value: A value that can be converted to a `tf.DType` object.

  Returns:
    A `DType` corresponding to `type_value`.

  Raises:
    TypeError: If `type_value` cannot be converted to a `DType`.
  """
