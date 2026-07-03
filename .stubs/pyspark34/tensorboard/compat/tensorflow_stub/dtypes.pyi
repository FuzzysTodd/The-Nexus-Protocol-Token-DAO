from . import pywrap_tensorflow as pywrap_tensorflow
from _typeshed import Incomplete
from tensorboard.compat.proto import types_pb2 as types_pb2

class DType:
    """Represents the type of the elements in a `Tensor`.

    The following `DType` objects are defined:

    * `tf.float16`: 16-bit half-precision floating-point.
    * `tf.float32`: 32-bit single-precision floating-point.
    * `tf.float64`: 64-bit double-precision floating-point.
    * `tf.bfloat16`: 16-bit truncated floating-point.
    * `tf.complex64`: 64-bit single-precision complex.
    * `tf.complex128`: 128-bit double-precision complex.
    * `tf.int8`: 8-bit signed integer.
    * `tf.uint8`: 8-bit unsigned integer.
    * `tf.uint16`: 16-bit unsigned integer.
    * `tf.uint32`: 32-bit unsigned integer.
    * `tf.uint64`: 64-bit unsigned integer.
    * `tf.int16`: 16-bit signed integer.
    * `tf.int32`: 32-bit signed integer.
    * `tf.int64`: 64-bit signed integer.
    * `tf.bool`: Boolean.
    * `tf.string`: String.
    * `tf.qint8`: Quantized 8-bit signed integer.
    * `tf.quint8`: Quantized 8-bit unsigned integer.
    * `tf.qint16`: Quantized 16-bit signed integer.
    * `tf.quint16`: Quantized 16-bit unsigned integer.
    * `tf.qint32`: Quantized 32-bit signed integer.
    * `tf.resource`: Handle to a mutable resource.
    * `tf.variant`: Values of arbitrary types.

    In addition, variants of these types with the `_ref` suffix are
    defined for reference-typed tensors.

    The `tf.as_dtype()` function converts numpy types and string type
    names to a `DType` object.
    """
    def __init__(self, type_enum) -> None:
        """Creates a new `DataType`.

        NOTE(mrry): In normal circumstances, you should not need to
        construct a `DataType` object directly. Instead, use the
        `tf.as_dtype()` function.

        Args:
          type_enum: A `types_pb2.DataType` enum value.

        Raises:
          TypeError: If `type_enum` is not a value `types_pb2.DataType`.
        """
    @property
    def base_dtype(self):
        """Returns a non-reference `DType` based on this `DType`."""
    @property
    def real_dtype(self):
        """Returns the dtype correspond to this dtype's real part."""
    @property
    def is_numpy_compatible(self): ...
    @property
    def as_numpy_dtype(self):
        """Returns a `numpy.dtype` based on this `DType`."""
    @property
    def as_datatype_enum(self):
        """Returns a `types_pb2.DataType` enum value based on this `DType`."""
    @property
    def is_bool(self):
        """Returns whether this is a boolean data type."""
    @property
    def is_integer(self):
        """Returns whether this is a (non-quantized) integer type."""
    @property
    def is_floating(self):
        """Returns whether this is a (non-quantized, real) floating point
        type."""
    @property
    def is_complex(self):
        """Returns whether this is a complex floating point type."""
    @property
    def is_quantized(self):
        """Returns whether this is a quantized data type."""
    @property
    def is_unsigned(self):
        """Returns whether this type is unsigned.

        Non-numeric, unordered, and quantized types are not considered unsigned, and
        this function returns `False`.

        Returns:
          Whether a `DType` is unsigned.
        """
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
        """Return intensity limits, i.e. (min, max) tuple, of the dtype.

        Args:
          clip_negative : bool, optional
              If True, clip the negative range (i.e. return 0 for min intensity)
              even if the image dtype allows negative values.
        Returns
          min, max : tuple
            Lower and upper intensity limits.
        """
    def is_compatible_with(self, other):
        """Returns True if the `other` DType will be converted to this DType.

        The conversion rules are as follows:

        ```python
        DType(T)       .is_compatible_with(DType(T))        == True
        DType(T)       .is_compatible_with(DType(T).as_ref) == True
        DType(T).as_ref.is_compatible_with(DType(T))        == False
        DType(T).as_ref.is_compatible_with(DType(T).as_ref) == True
        ```

        Args:
          other: A `DType` (or object that may be converted to a `DType`).

        Returns:
          True if a Tensor of the `other` `DType` will be implicitly converted to
          this `DType`.
        """
    def __eq__(self, other):
        """Returns True iff this DType refers to the same type as `other`."""
    def __ne__(self, other):
        """Returns True iff self != other."""
    @property
    def name(self):
        """Returns the string name for this `DType`."""
    def __int__(self) -> int: ...
    def __hash__(self): ...
    def __reduce__(self): ...
    @property
    def size(self): ...

dtype_range: Incomplete
resource: Incomplete
variant: Incomplete
float16: Incomplete
half = float16
float32: Incomplete
float64: Incomplete
double = float64
int32: Incomplete
uint8: Incomplete
uint16: Incomplete
uint32: Incomplete
uint64: Incomplete
int16: Incomplete
int8: Incomplete
string: Incomplete
complex64: Incomplete
complex128: Incomplete
int64: Incomplete
bool: Incomplete
qint8: Incomplete
quint8: Incomplete
qint16: Incomplete
quint16: Incomplete
qint32: Incomplete
resource_ref: Incomplete
variant_ref: Incomplete
bfloat16: Incomplete
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
np_resource: Incomplete
QUANTIZED_DTYPES: Incomplete

def as_dtype(type_value):
    """Converts the given `type_value` to a `DType`.

    Args:
      type_value: A value that can be converted to a `tf.DType` object. This may
        currently be a `tf.DType` object, a [`DataType`
        enum](https://www.tensorflow.org/code/tensorflow/core/framework/types.proto),
        a string type name, or a `numpy.dtype`.

    Returns:
      A `DType` corresponding to `type_value`.

    Raises:
      TypeError: If `type_value` cannot be converted to a `DType`.
    """
