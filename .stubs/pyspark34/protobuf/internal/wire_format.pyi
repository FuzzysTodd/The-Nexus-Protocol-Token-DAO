from _typeshed import Incomplete

TAG_TYPE_BITS: int
TAG_TYPE_MASK: Incomplete
WIRETYPE_VARINT: int
WIRETYPE_FIXED64: int
WIRETYPE_LENGTH_DELIMITED: int
WIRETYPE_START_GROUP: int
WIRETYPE_END_GROUP: int
WIRETYPE_FIXED32: int
INT32_MAX: Incomplete
INT32_MIN: Incomplete
UINT32_MAX: Incomplete
INT64_MAX: Incomplete
INT64_MIN: Incomplete
UINT64_MAX: Incomplete
FORMAT_UINT32_LITTLE_ENDIAN: str
FORMAT_UINT64_LITTLE_ENDIAN: str
FORMAT_FLOAT_LITTLE_ENDIAN: str
FORMAT_DOUBLE_LITTLE_ENDIAN: str

def PackTag(field_number, wire_type):
    """Returns an unsigned 32-bit integer that encodes the field number and
  wire type information in standard protocol message wire format.

  Args:
    field_number: Expected to be an integer in the range [1, 1 << 29)
    wire_type: One of the WIRETYPE_* constants.
  """
def UnpackTag(tag):
    """The inverse of PackTag().  Given an unsigned 32-bit number,
  returns a (field_number, wire_type) tuple.
  """
def ZigZagEncode(value):
    """ZigZag Transform:  Encodes signed integers so that they can be
  effectively used with varint encoding.  See wire_format.h for
  more details.
  """
def ZigZagDecode(value):
    """Inverse of ZigZagEncode()."""
def Int32ByteSize(field_number, int32): ...
def Int32ByteSizeNoTag(int32): ...
def Int64ByteSize(field_number, int64): ...
def UInt32ByteSize(field_number, uint32): ...
def UInt64ByteSize(field_number, uint64): ...
def SInt32ByteSize(field_number, int32): ...
def SInt64ByteSize(field_number, int64): ...
def Fixed32ByteSize(field_number, fixed32): ...
def Fixed64ByteSize(field_number, fixed64): ...
def SFixed32ByteSize(field_number, sfixed32): ...
def SFixed64ByteSize(field_number, sfixed64): ...
def FloatByteSize(field_number, flt): ...
def DoubleByteSize(field_number, double): ...
def BoolByteSize(field_number, b): ...
def EnumByteSize(field_number, enum): ...
def StringByteSize(field_number, string): ...
def BytesByteSize(field_number, b): ...
def GroupByteSize(field_number, message): ...
def MessageByteSize(field_number, message): ...
def MessageSetItemByteSize(field_number, msg): ...
def TagByteSize(field_number):
    """Returns the bytes required to serialize a tag with this field number."""

NON_PACKABLE_TYPES: Incomplete

def IsTypePackable(field_type):
    """Return true iff packable = true is valid for fields of this type.

  Args:
    field_type: a FieldDescriptor::Type value.

  Returns:
    True iff fields of this type are packable.
  """
