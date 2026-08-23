from _typeshed import Incomplete

class Error(Exception):
    """Top-level module error for json_format."""
class SerializeToJsonError(Error):
    """Thrown if serialization to JSON fails."""
class ParseError(Error):
    """Thrown in case of parsing error."""

def MessageToJson(message, including_default_value_fields: bool = False, preserving_proto_field_name: bool = False, indent: int = 2, sort_keys: bool = False, use_integers_for_enums: bool = False, descriptor_pool: Incomplete | None = None, float_precision: Incomplete | None = None, ensure_ascii: bool = True):
    """Converts protobuf message to JSON format.

  Args:
    message: The protocol buffers message instance to serialize.
    including_default_value_fields: If True, singular primitive fields,
        repeated fields, and map fields will always be serialized.  If
        False, only serialize non-empty fields.  Singular message fields
        and oneof fields are not affected by this option.
    preserving_proto_field_name: If True, use the original proto field
        names as defined in the .proto file. If False, convert the field
        names to lowerCamelCase.
    indent: The JSON object will be pretty-printed with this indent level.
        An indent level of 0 or negative will only insert newlines.
    sort_keys: If True, then the output will be sorted by field names.
    use_integers_for_enums: If true, print integers instead of enum names.
    descriptor_pool: A Descriptor Pool for resolving types. If None use the
        default.
    float_precision: If set, use this to specify float field valid digits.
    ensure_ascii: If True, strings with non-ASCII characters are escaped.
        If False, Unicode strings are returned unchanged.

  Returns:
    A string containing the JSON formatted protocol buffer message.
  """
def MessageToDict(message, including_default_value_fields: bool = False, preserving_proto_field_name: bool = False, use_integers_for_enums: bool = False, descriptor_pool: Incomplete | None = None, float_precision: Incomplete | None = None):
    """Converts protobuf message to a dictionary.

  When the dictionary is encoded to JSON, it conforms to proto3 JSON spec.

  Args:
    message: The protocol buffers message instance to serialize.
    including_default_value_fields: If True, singular primitive fields,
        repeated fields, and map fields will always be serialized.  If
        False, only serialize non-empty fields.  Singular message fields
        and oneof fields are not affected by this option.
    preserving_proto_field_name: If True, use the original proto field
        names as defined in the .proto file. If False, convert the field
        names to lowerCamelCase.
    use_integers_for_enums: If true, print integers instead of enum names.
    descriptor_pool: A Descriptor Pool for resolving types. If None use the
        default.
    float_precision: If set, use this to specify float field valid digits.

  Returns:
    A dict representation of the protocol buffer message.
  """

class _Printer:
    """JSON format printer for protocol message."""
    including_default_value_fields: Incomplete
    preserving_proto_field_name: Incomplete
    use_integers_for_enums: Incomplete
    descriptor_pool: Incomplete
    float_format: Incomplete
    def __init__(self, including_default_value_fields: bool = False, preserving_proto_field_name: bool = False, use_integers_for_enums: bool = False, descriptor_pool: Incomplete | None = None, float_precision: Incomplete | None = None) -> None: ...
    def ToJsonString(self, message, indent, sort_keys, ensure_ascii): ...

def Parse(text, message, ignore_unknown_fields: bool = False, descriptor_pool: Incomplete | None = None, max_recursion_depth: int = 100):
    """Parses a JSON representation of a protocol message into a message.

  Args:
    text: Message JSON representation.
    message: A protocol buffer message to merge into.
    ignore_unknown_fields: If True, do not raise errors for unknown fields.
    descriptor_pool: A Descriptor Pool for resolving types. If None use the
      default.
    max_recursion_depth: max recursion depth of JSON message to be
      deserialized. JSON messages over this depth will fail to be
      deserialized. Default value is 100.

  Returns:
    The same message passed as argument.

  Raises::
    ParseError: On JSON parsing problems.
  """
def ParseDict(js_dict, message, ignore_unknown_fields: bool = False, descriptor_pool: Incomplete | None = None, max_recursion_depth: int = 100):
    """Parses a JSON dictionary representation into a message.

  Args:
    js_dict: Dict representation of a JSON message.
    message: A protocol buffer message to merge into.
    ignore_unknown_fields: If True, do not raise errors for unknown fields.
    descriptor_pool: A Descriptor Pool for resolving types. If None use the
      default.
    max_recursion_depth: max recursion depth of JSON message to be
      deserialized. JSON messages over this depth will fail to be
      deserialized. Default value is 100.

  Returns:
    The same message passed as argument.
  """

class _Parser:
    """JSON format parser for protocol message."""
    ignore_unknown_fields: Incomplete
    descriptor_pool: Incomplete
    max_recursion_depth: Incomplete
    recursion_depth: int
    def __init__(self, ignore_unknown_fields, descriptor_pool, max_recursion_depth) -> None: ...
    def ConvertMessage(self, value, message, path) -> None:
        """Convert a JSON object into a message.

    Args:
      value: A JSON object.
      message: A WKT or regular protocol message to record the data.
      path: parent path to log parse error info.

    Raises:
      ParseError: In case of convert problems.
    """
