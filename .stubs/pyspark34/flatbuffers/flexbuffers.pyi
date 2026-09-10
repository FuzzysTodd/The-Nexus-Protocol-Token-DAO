import enum
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['Type', 'Builder', 'GetRoot', 'Dumps', 'Loads']

class BitWidth(enum.IntEnum):
    """Supported bit widths of value types.

  These are used in the lower 2 bits of a type field to determine the size of
  the elements (and or size field) of the item pointed to (e.g. vector).
  """
    W8: int
    W16: int
    W32: int
    W64: int
    @staticmethod
    def U(value):
        """Returns the minimum `BitWidth` to encode unsigned integer value."""
    @staticmethod
    def I(value):
        """Returns the minimum `BitWidth` to encode signed integer value."""
    @staticmethod
    def F(value):
        """Returns the `BitWidth` to encode floating point value."""
    @staticmethod
    def B(byte_width): ...

class Type(enum.IntEnum):
    """Supported types of encoded data.

  These are used as the upper 6 bits of a type field to indicate the actual
  type.
  """
    NULL: int
    INT: int
    UINT: int
    FLOAT: int
    KEY: int
    STRING: int
    INDIRECT_INT: int
    INDIRECT_UINT: int
    INDIRECT_FLOAT: int
    MAP: int
    VECTOR: int
    VECTOR_INT: int
    VECTOR_UINT: int
    VECTOR_FLOAT: int
    VECTOR_KEY: int
    VECTOR_STRING_DEPRECATED: int
    VECTOR_INT2: int
    VECTOR_UINT2: int
    VECTOR_FLOAT2: int
    VECTOR_INT3: int
    VECTOR_UINT3: int
    VECTOR_FLOAT3: int
    VECTOR_INT4: int
    VECTOR_UINT4: int
    VECTOR_FLOAT4: int
    BLOB: int
    BOOL: int
    VECTOR_BOOL: int
    @staticmethod
    def Pack(type_, bit_width): ...
    @staticmethod
    def Unpack(packed_type): ...
    @staticmethod
    def IsInline(type_): ...
    @staticmethod
    def IsTypedVector(type_): ...
    @staticmethod
    def IsTypedVectorElementType(type_): ...
    @staticmethod
    def ToTypedVectorElementType(type_): ...
    @staticmethod
    def IsFixedTypedVector(type_): ...
    @staticmethod
    def IsFixedTypedVectorElementType(type_): ...
    @staticmethod
    def ToFixedTypedVectorElementType(type_): ...
    @staticmethod
    def ToTypedVector(element_type, fixed_len: int = 0):
        """Converts element type to corresponding vector type.

    Args:
      element_type: vector element type
      fixed_len: number of elements: 0 for typed vector; 2, 3, or 4 for fixed
        typed vector.

    Returns:
      Typed vector type or fixed typed vector type.
    """

class Buf:
    """Class to access underlying buffer object starting from the given offset."""
    def __init__(self, buf, offset) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def Find(self, sub):
        """Returns the lowest index where the sub subsequence is found."""
    def Slice(self, offset):
        """Returns new `Buf` which starts from the given offset."""
    def Indirect(self, offset, byte_width):
        """Return new `Buf` based on the encoded offset (indirect encoding)."""

class Object:
    """Base class for all non-trivial data accessors."""
    def __init__(self, buf, byte_width) -> None: ...
    @property
    def ByteWidth(self): ...

class Sized(Object):
    """Base class for all data accessors which need to read encoded size."""
    def __init__(self, buf, byte_width, size: int = 0) -> None: ...
    @property
    def SizeBytes(self): ...
    def __len__(self) -> int: ...

class Blob(Sized):
    """Data accessor for the encoded blob bytes."""
    @property
    def Bytes(self): ...

class String(Sized):
    """Data accessor for the encoded string bytes."""
    @property
    def Bytes(self): ...
    def Mutate(self, value):
        """Mutates underlying string bytes in place.

    Args:
      value: New string to replace the existing one. New string must have less
        or equal UTF-8-encoded bytes than the existing one to successfully
        mutate underlying byte buffer.

    Returns:
      Whether the value was mutated or not.
    """

class Key(Object):
    """Data accessor for the encoded key bytes."""
    def __init__(self, buf, byte_width) -> None: ...
    @property
    def Bytes(self): ...
    def __len__(self) -> int: ...

class Vector(Sized):
    """Data accessor for the encoded vector bytes."""
    def __getitem__(self, index): ...
    @property
    def Value(self):
        """Returns the underlying encoded data as a list object."""

class TypedVector(Sized):
    """Data accessor for the encoded typed vector or fixed typed vector bytes."""
    def __init__(self, buf, byte_width, element_type, size: int = 0) -> None: ...
    @property
    def Bytes(self): ...
    @property
    def ElementType(self): ...
    def __getitem__(self, index): ...
    @property
    def Value(self):
        """Returns underlying data as list object."""

class Map(Vector):
    """Data accessor for the encoded map bytes."""
    @staticmethod
    def CompareKeys(a, b): ...
    def __getitem__(self, key): ...
    @property
    def Keys(self): ...
    @property
    def Values(self): ...
    @property
    def Value(self): ...

class Ref:
    """Data accessor for the encoded data bytes."""
    @staticmethod
    def PackedType(buf, parent_width, packed_type): ...
    def __init__(self, buf, parent_width, byte_width, type_) -> None: ...
    @property
    def IsNull(self): ...
    @property
    def IsBool(self): ...
    @property
    def AsBool(self): ...
    def MutateBool(self, value):
        """Mutates underlying boolean value bytes in place.

    Args:
      value: New boolean value.

    Returns:
      Whether the value was mutated or not.
    """
    @property
    def IsNumeric(self): ...
    @property
    def IsInt(self): ...
    @property
    def AsInt(self):
        """Returns current reference as integer value."""
    def MutateInt(self, value):
        """Mutates underlying integer value bytes in place.

    Args:
      value: New integer value. It must fit to the byte size of the existing
        encoded value.

    Returns:
      Whether the value was mutated or not.
    """
    @property
    def IsFloat(self): ...
    @property
    def AsFloat(self):
        """Returns current reference as floating point value."""
    def MutateFloat(self, value):
        """Mutates underlying floating point value bytes in place.

    Args:
      value: New float value. It must fit to the byte size of the existing
        encoded value.

    Returns:
      Whether the value was mutated or not.
    """
    @property
    def IsKey(self): ...
    @property
    def AsKeyBytes(self): ...
    @property
    def AsKey(self): ...
    @property
    def IsString(self): ...
    @property
    def AsStringBytes(self): ...
    @property
    def AsString(self): ...
    def MutateString(self, value): ...
    @property
    def IsBlob(self): ...
    @property
    def AsBlob(self): ...
    @property
    def IsAnyVector(self): ...
    @property
    def IsVector(self): ...
    @property
    def AsVector(self): ...
    @property
    def IsTypedVector(self): ...
    @property
    def AsTypedVector(self): ...
    @property
    def IsFixedTypedVector(self): ...
    @property
    def AsFixedTypedVector(self): ...
    @property
    def IsMap(self): ...
    @property
    def AsMap(self): ...
    @property
    def Value(self):
        """Converts current reference to value of corresponding type.

    This is equivalent to calling `AsInt` for integer values, `AsFloat` for
    floating point values, etc.

    Returns:
      Value of corresponding type.
    """

class Value:
    """Class to represent given value during the encoding process."""
    @staticmethod
    def Null(): ...
    @staticmethod
    def Bool(value): ...
    @staticmethod
    def Int(value, bit_width): ...
    @staticmethod
    def UInt(value, bit_width): ...
    @staticmethod
    def Float(value, bit_width): ...
    @staticmethod
    def Key(offset): ...
    def __init__(self, value, type_, min_bit_width) -> None: ...
    @property
    def Value(self): ...
    @property
    def Type(self): ...
    @property
    def MinBitWidth(self): ...
    def StoredPackedType(self, parent_bit_width=...): ...
    def ElemWidth(self, buf_size, elem_index: int = 0): ...
    def StoredWidth(self, parent_bit_width=...): ...

class Pool:
    """Collection of (data, offset) pairs sorted by data for quick access."""
    def __init__(self) -> None: ...
    def FindOrInsert(self, data, offset): ...
    def Clear(self) -> None: ...
    @property
    def Elements(self): ...

class Builder:
    """Helper class to encode structural data into flexbuffers format."""
    def __init__(self, share_strings: bool = False, share_keys: bool = True, force_min_bit_width=...) -> None: ...
    def __len__(self) -> int: ...
    @property
    def StringPool(self): ...
    @property
    def KeyPool(self): ...
    def Clear(self) -> None: ...
    finished: bool
    def Finish(self):
        """Finishes encoding process and returns underlying buffer."""
    def String(self, value):
        """Encodes string value."""
    def Blob(self, value):
        """Encodes binary blob value.

    Args:
      value: A byte/bytearray value to encode

    Returns:
      Offset of the encoded value in underlying the byte buffer.
    """
    def Key(self, value):
        """Encodes key value.

    Args:
      value: A byte/bytearray/str value to encode. Byte object must not contain
        zero bytes. String object must be convertible to ASCII.

    Returns:
      Offset of the encoded value in the underlying byte buffer.
    """
    def Null(self, key: Incomplete | None = None) -> None:
        """Encodes None value."""
    def Bool(self, value) -> None:
        """Encodes boolean value.

    Args:
      value: A boolean value.
    """
    def Int(self, value, byte_width: int = 0) -> None:
        """Encodes signed integer value.

    Args:
      value: A signed integer value.
      byte_width: Number of bytes to use: 1, 2, 4, or 8.
    """
    def IndirectInt(self, value, byte_width: int = 0) -> None:
        """Encodes signed integer value indirectly.

    Args:
      value: A signed integer value.
      byte_width: Number of bytes to use: 1, 2, 4, or 8.
    """
    def UInt(self, value, byte_width: int = 0) -> None:
        """Encodes unsigned integer value.

    Args:
      value: An unsigned integer value.
      byte_width: Number of bytes to use: 1, 2, 4, or 8.
    """
    def IndirectUInt(self, value, byte_width: int = 0) -> None:
        """Encodes unsigned integer value indirectly.

    Args:
      value: An unsigned integer value.
      byte_width: Number of bytes to use: 1, 2, 4, or 8.
    """
    def Float(self, value, byte_width: int = 0) -> None:
        """Encodes floating point value.

    Args:
      value: A floating point value.
      byte_width: Number of bytes to use: 4 or 8.
    """
    def IndirectFloat(self, value, byte_width: int = 0) -> None:
        """Encodes floating point value indirectly.

    Args:
      value: A floating point value.
      byte_width: Number of bytes to use: 4 or 8.
    """
    def Vector(self, key: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def VectorFromElements(self, elements) -> None:
        """Encodes sequence of any elements as a vector.

    Args:
      elements: sequence of elements, they may have different types.
    """
    def TypedVector(self, key: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def TypedVectorFromElements(self, elements, element_type: Incomplete | None = None) -> None:
        """Encodes sequence of elements of the same type as typed vector.

    Args:
      elements: Sequence of elements, they must be of the same type.
      element_type: Suggested element type. Setting it to None means determining
        correct value automatically based on the given elements.
    """
    def FixedTypedVectorFromElements(self, elements, element_type: Incomplete | None = None, byte_width: int = 0) -> None:
        """Encodes sequence of elements of the same type as fixed typed vector.

    Args:
      elements: Sequence of elements, they must be of the same type. Allowed
        types are `Type.INT`, `Type.UINT`, `Type.FLOAT`. Allowed number of
        elements are 2, 3, or 4.
      element_type: Suggested element type. Setting it to None means determining
        correct value automatically based on the given elements.
      byte_width: Number of bytes to use per element. For `Type.INT` and
        `Type.UINT`: 1, 2, 4, or 8. For `Type.FLOAT`: 4 or 8. Setting it to 0
        means determining correct value automatically based on the given
        elements.
    """
    def Map(self, key: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def MapFromElements(self, elements) -> None: ...
    def Adder(self, type_): ...
    def Add(self, value) -> None:
        """Encodes value of any supported type."""
    @property
    def LastValue(self): ...
    def ReuseValue(self, value) -> None: ...

def GetRoot(buf):
    """Returns root `Ref` object for the given buffer."""
def Dumps(obj):
    """Returns bytearray with the encoded python object."""
def Loads(buf):
    """Returns python object decoded from the buffer."""
