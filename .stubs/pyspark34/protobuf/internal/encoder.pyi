from _typeshed import Incomplete

Int32Sizer: Incomplete
Int64Sizer: Incomplete
EnumSizer: Incomplete
UInt32Sizer: Incomplete
UInt64Sizer: Incomplete
SInt32Sizer: Incomplete
SInt64Sizer: Incomplete
Fixed32Sizer: Incomplete
SFixed32Sizer: Incomplete
FloatSizer: Incomplete
Fixed64Sizer: Incomplete
SFixed64Sizer: Incomplete
DoubleSizer: Incomplete
BoolSizer: Incomplete

def StringSizer(field_number, is_repeated, is_packed):
    """Returns a sizer for a string field."""
def BytesSizer(field_number, is_repeated, is_packed):
    """Returns a sizer for a bytes field."""
def GroupSizer(field_number, is_repeated, is_packed):
    """Returns a sizer for a group field."""
def MessageSizer(field_number, is_repeated, is_packed):
    """Returns a sizer for a message field."""
def MessageSetItemSizer(field_number):
    """Returns a sizer for extensions of MessageSet.

  The message set message looks like this:
    message MessageSet {
      repeated group Item = 1 {
        required int32 type_id = 2;
        required string message = 3;
      }
    }
  """
def MapSizer(field_descriptor, is_message_map):
    """Returns a sizer for a map field."""
def TagBytes(field_number, wire_type):
    """Encode the given tag and return the bytes.  Only called at startup."""

Int32Encoder: Incomplete

Int64Encoder: Incomplete

EnumEncoder: Incomplete
UInt32Encoder: Incomplete
UInt64Encoder: Incomplete
SInt32Encoder: Incomplete
SInt64Encoder: Incomplete
Fixed32Encoder: Incomplete
Fixed64Encoder: Incomplete
SFixed32Encoder: Incomplete
SFixed64Encoder: Incomplete
FloatEncoder: Incomplete
DoubleEncoder: Incomplete

def BoolEncoder(field_number, is_repeated, is_packed):
    """Returns an encoder for a boolean field."""
def StringEncoder(field_number, is_repeated, is_packed):
    """Returns an encoder for a string field."""
def BytesEncoder(field_number, is_repeated, is_packed):
    """Returns an encoder for a bytes field."""
def GroupEncoder(field_number, is_repeated, is_packed):
    """Returns an encoder for a group field."""
def MessageEncoder(field_number, is_repeated, is_packed):
    """Returns an encoder for a message field."""
def MessageSetItemEncoder(field_number):
    """Encoder for extensions of MessageSet.

  The message set message looks like this:
    message MessageSet {
      repeated group Item = 1 {
        required int32 type_id = 2;
        required string message = 3;
      }
    }
  """
def MapEncoder(field_descriptor):
    """Encoder for extensions of MessageSet.

  Maps always have a wire format like this:
    message MapEntry {
      key_type key = 1;
      value_type value = 2;
    }
    repeated MapEntry map = N;
  """
