from _typeshed import Incomplete

def ReadTag(buffer, pos):
    """Read a tag from the memoryview, and return a (tag_bytes, new_pos) tuple.

  We return the raw bytes of the tag rather than decoding them.  The raw
  bytes can then be used to look up the proper decoder.  This effectively allows
  us to trade some work that would be done in pure-python (decoding a varint)
  for work that is done in C (searching for a byte string in a hash table).
  In a low-level language it would be much cheaper to decode the varint and
  use that, but not in Python.

  Args:
    buffer: memoryview object of the encoded bytes
    pos: int of the current position to start from

  Returns:
    Tuple[bytes, int] of the tag data and new position.
  """
def EnumDecoder(field_number, is_repeated, is_packed, key, new_default, clear_if_default: bool = False):
    """Returns a decoder for enum field."""

Int32Decoder: Incomplete
Int64Decoder: Incomplete
UInt32Decoder: Incomplete
UInt64Decoder: Incomplete
SInt32Decoder: Incomplete
SInt64Decoder: Incomplete
Fixed32Decoder: Incomplete
Fixed64Decoder: Incomplete
SFixed32Decoder: Incomplete
SFixed64Decoder: Incomplete
FloatDecoder: Incomplete
DoubleDecoder: Incomplete
BoolDecoder: Incomplete

def StringDecoder(field_number, is_repeated, is_packed, key, new_default, clear_if_default: bool = False):
    """Returns a decoder for a string field."""
def BytesDecoder(field_number, is_repeated, is_packed, key, new_default, clear_if_default: bool = False):
    """Returns a decoder for a bytes field."""
def GroupDecoder(field_number, is_repeated, is_packed, key, new_default):
    """Returns a decoder for a group field."""
def MessageDecoder(field_number, is_repeated, is_packed, key, new_default):
    """Returns a decoder for a message field."""

MESSAGE_SET_ITEM_TAG: Incomplete

def MessageSetItemDecoder(descriptor):
    """Returns a decoder for a MessageSet item.

  The parameter is the message Descriptor.

  The message set message looks like this:
    message MessageSet {
      repeated group Item = 1 {
        required int32 type_id = 2;
        required string message = 3;
      }
    }
  """
def UnknownMessageSetItemDecoder():
    """Returns a decoder for a Unknown MessageSet item."""
def MapDecoder(field_descriptor, new_default, is_message_map):
    """Returns a decoder for a map field."""

SkipField: Incomplete
