from _typeshed import Incomplete

__all__ = ['MessageToString', 'Parse', 'PrintMessage', 'PrintField', 'PrintFieldValue', 'Merge', 'MessageToBytes']

class Error(Exception):
    """Top-level module error for text_format."""

class ParseError(Error):
    """Thrown in case of text parsing or tokenizing error."""
    def __init__(self, message: Incomplete | None = None, line: Incomplete | None = None, column: Incomplete | None = None) -> None: ...
    def GetLine(self): ...
    def GetColumn(self): ...

class TextWriter:
    def __init__(self, as_utf8) -> None: ...
    def write(self, val): ...
    def close(self): ...
    def getvalue(self): ...

def MessageToString(message, as_utf8: bool = False, as_one_line: bool = False, use_short_repeated_primitives: bool = False, pointy_brackets: bool = False, use_index_order: bool = False, float_format: Incomplete | None = None, double_format: Incomplete | None = None, use_field_number: bool = False, descriptor_pool: Incomplete | None = None, indent: int = 0, message_formatter: Incomplete | None = None, print_unknown_fields: bool = False, force_colon: bool = False) -> str:
    '''Convert protobuf message to text format.

  Double values can be formatted compactly with 15 digits of
  precision (which is the most that IEEE 754 "double" can guarantee)
  using double_format=\'.15g\'. To ensure that converting to text and back to a
  proto will result in an identical value, double_format=\'.17g\' should be used.

  Args:
    message: The protocol buffers message.
    as_utf8: Return unescaped Unicode for non-ASCII characters.
    as_one_line: Don\'t introduce newlines between fields.
    use_short_repeated_primitives: Use short repeated format for primitives.
    pointy_brackets: If True, use angle brackets instead of curly braces for
      nesting.
    use_index_order: If True, fields of a proto message will be printed using
      the order defined in source code instead of the field number, extensions
      will be printed at the end of the message and their relative order is
      determined by the extension number. By default, use the field number
      order.
    float_format (str): If set, use this to specify float field formatting
      (per the "Format Specification Mini-Language"); otherwise, shortest float
      that has same value in wire will be printed. Also affect double field
      if double_format is not set but float_format is set.
    double_format (str): If set, use this to specify double field formatting
      (per the "Format Specification Mini-Language"); if it is not set but
      float_format is set, use float_format. Otherwise, use ``str()``
    use_field_number: If True, print field numbers instead of names.
    descriptor_pool (DescriptorPool): Descriptor pool used to resolve Any types.
    indent (int): The initial indent level, in terms of spaces, for pretty
      print.
    message_formatter (function(message, indent, as_one_line) -> unicode|None):
      Custom formatter for selected sub-messages (usually based on message
      type). Use to pretty print parts of the protobuf for easier diffing.
    print_unknown_fields: If True, unknown fields will be printed.
    force_colon: If set, a colon will be added after the field name even if the
      field is a proto message.

  Returns:
    str: A string of the text formatted protocol buffer message.
  '''
def MessageToBytes(message, **kwargs) -> bytes:
    """Convert protobuf message to encoded text format.  See MessageToString."""
def PrintMessage(message, out, indent: int = 0, as_utf8: bool = False, as_one_line: bool = False, use_short_repeated_primitives: bool = False, pointy_brackets: bool = False, use_index_order: bool = False, float_format: Incomplete | None = None, double_format: Incomplete | None = None, use_field_number: bool = False, descriptor_pool: Incomplete | None = None, message_formatter: Incomplete | None = None, print_unknown_fields: bool = False, force_colon: bool = False) -> None:
    '''Convert the message to text format and write it to the out stream.

  Args:
    message: The Message object to convert to text format.
    out: A file handle to write the message to.
    indent: The initial indent level for pretty print.
    as_utf8: Return unescaped Unicode for non-ASCII characters.
    as_one_line: Don\'t introduce newlines between fields.
    use_short_repeated_primitives: Use short repeated format for primitives.
    pointy_brackets: If True, use angle brackets instead of curly braces for
      nesting.
    use_index_order: If True, print fields of a proto message using the order
      defined in source code instead of the field number. By default, use the
      field number order.
    float_format: If set, use this to specify float field formatting
      (per the "Format Specification Mini-Language"); otherwise, shortest
      float that has same value in wire will be printed. Also affect double
      field if double_format is not set but float_format is set.
    double_format: If set, use this to specify double field formatting
      (per the "Format Specification Mini-Language"); if it is not set but
      float_format is set, use float_format. Otherwise, str() is used.
    use_field_number: If True, print field numbers instead of names.
    descriptor_pool: A DescriptorPool used to resolve Any types.
    message_formatter: A function(message, indent, as_one_line): unicode|None
      to custom format selected sub-messages (usually based on message type).
      Use to pretty print parts of the protobuf for easier diffing.
    print_unknown_fields: If True, unknown fields will be printed.
    force_colon: If set, a colon will be added after the field name even if
      the field is a proto message.
  '''
def PrintField(field, value, out, indent: int = 0, as_utf8: bool = False, as_one_line: bool = False, use_short_repeated_primitives: bool = False, pointy_brackets: bool = False, use_index_order: bool = False, float_format: Incomplete | None = None, double_format: Incomplete | None = None, message_formatter: Incomplete | None = None, print_unknown_fields: bool = False, force_colon: bool = False) -> None:
    """Print a single field name/value pair."""
def PrintFieldValue(field, value, out, indent: int = 0, as_utf8: bool = False, as_one_line: bool = False, use_short_repeated_primitives: bool = False, pointy_brackets: bool = False, use_index_order: bool = False, float_format: Incomplete | None = None, double_format: Incomplete | None = None, message_formatter: Incomplete | None = None, print_unknown_fields: bool = False, force_colon: bool = False) -> None:
    """Print a single field value (not including name)."""

class _Printer:
    """Text format printer for protocol message."""
    out: Incomplete
    indent: Incomplete
    as_utf8: Incomplete
    as_one_line: Incomplete
    use_short_repeated_primitives: Incomplete
    pointy_brackets: Incomplete
    use_index_order: Incomplete
    float_format: Incomplete
    double_format: Incomplete
    use_field_number: Incomplete
    descriptor_pool: Incomplete
    message_formatter: Incomplete
    print_unknown_fields: Incomplete
    force_colon: Incomplete
    def __init__(self, out, indent: int = 0, as_utf8: bool = False, as_one_line: bool = False, use_short_repeated_primitives: bool = False, pointy_brackets: bool = False, use_index_order: bool = False, float_format: Incomplete | None = None, double_format: Incomplete | None = None, use_field_number: bool = False, descriptor_pool: Incomplete | None = None, message_formatter: Incomplete | None = None, print_unknown_fields: bool = False, force_colon: bool = False) -> None:
        '''Initialize the Printer.

    Double values can be formatted compactly with 15 digits of precision
    (which is the most that IEEE 754 "double" can guarantee) using
    double_format=\'.15g\'. To ensure that converting to text and back to a proto
    will result in an identical value, double_format=\'.17g\' should be used.

    Args:
      out: To record the text format result.
      indent: The initial indent level for pretty print.
      as_utf8: Return unescaped Unicode for non-ASCII characters.
      as_one_line: Don\'t introduce newlines between fields.
      use_short_repeated_primitives: Use short repeated format for primitives.
      pointy_brackets: If True, use angle brackets instead of curly braces for
        nesting.
      use_index_order: If True, print fields of a proto message using the order
        defined in source code instead of the field number. By default, use the
        field number order.
      float_format: If set, use this to specify float field formatting
        (per the "Format Specification Mini-Language"); otherwise, shortest
        float that has same value in wire will be printed. Also affect double
        field if double_format is not set but float_format is set.
      double_format: If set, use this to specify double field formatting
        (per the "Format Specification Mini-Language"); if it is not set but
        float_format is set, use float_format. Otherwise, str() is used.
      use_field_number: If True, print field numbers instead of names.
      descriptor_pool: A DescriptorPool used to resolve Any types.
      message_formatter: A function(message, indent, as_one_line): unicode|None
        to custom format selected sub-messages (usually based on message type).
        Use to pretty print parts of the protobuf for easier diffing.
      print_unknown_fields: If True, unknown fields will be printed.
      force_colon: If set, a colon will be added after the field name even if
        the field is a proto message.
    '''
    def PrintMessage(self, message):
        """Convert protobuf message to text format.

    Args:
      message: The protocol buffers message.
    """
    def PrintField(self, field, value) -> None:
        """Print a single field name/value pair."""
    def PrintFieldValue(self, field, value) -> None:
        """Print a single field value (not including name).

    For repeated fields, the value should be a single element.

    Args:
      field: The descriptor of the field to be printed.
      value: The value of the field.
    """

def Parse(text, message, allow_unknown_extension: bool = False, allow_field_number: bool = False, descriptor_pool: Incomplete | None = None, allow_unknown_field: bool = False):
    '''Parses a text representation of a protocol message into a message.

  NOTE: for historical reasons this function does not clear the input
  message. This is different from what the binary msg.ParseFrom(...) does.
  If text contains a field already set in message, the value is appended if the
  field is repeated. Otherwise, an error is raised.

  Example::

    a = MyProto()
    a.repeated_field.append(\'test\')
    b = MyProto()

    # Repeated fields are combined
    text_format.Parse(repr(a), b)
    text_format.Parse(repr(a), b) # repeated_field contains ["test", "test"]

    # Non-repeated fields cannot be overwritten
    a.singular_field = 1
    b.singular_field = 2
    text_format.Parse(repr(a), b) # ParseError

    # Binary version:
    b.ParseFromString(a.SerializeToString()) # repeated_field is now "test"

  Caller is responsible for clearing the message as needed.

  Args:
    text (str): Message text representation.
    message (Message): A protocol buffer message to merge into.
    allow_unknown_extension: if True, skip over missing extensions and keep
      parsing
    allow_field_number: if True, both field number and field name are allowed.
    descriptor_pool (DescriptorPool): Descriptor pool used to resolve Any types.
    allow_unknown_field: if True, skip over unknown field and keep
      parsing. Avoid to use this option if possible. It may hide some
      errors (e.g. spelling error on field name)

  Returns:
    Message: The same message passed as argument.

  Raises:
    ParseError: On text parsing problems.
  '''
def Merge(text, message, allow_unknown_extension: bool = False, allow_field_number: bool = False, descriptor_pool: Incomplete | None = None, allow_unknown_field: bool = False):
    """Parses a text representation of a protocol message into a message.

  Like Parse(), but allows repeated values for a non-repeated field, and uses
  the last one. This means any non-repeated, top-level fields specified in text
  replace those in the message.

  Args:
    text (str): Message text representation.
    message (Message): A protocol buffer message to merge into.
    allow_unknown_extension: if True, skip over missing extensions and keep
      parsing
    allow_field_number: if True, both field number and field name are allowed.
    descriptor_pool (DescriptorPool): Descriptor pool used to resolve Any types.
    allow_unknown_field: if True, skip over unknown field and keep
      parsing. Avoid to use this option if possible. It may hide some
      errors (e.g. spelling error on field name)

  Returns:
    Message: The same message passed as argument.

  Raises:
    ParseError: On text parsing problems.
  """

class _Parser:
    """Text format parser for protocol message."""
    allow_unknown_extension: Incomplete
    allow_field_number: Incomplete
    descriptor_pool: Incomplete
    allow_unknown_field: Incomplete
    def __init__(self, allow_unknown_extension: bool = False, allow_field_number: bool = False, descriptor_pool: Incomplete | None = None, allow_unknown_field: bool = False) -> None: ...
    def ParseLines(self, lines, message):
        """Parses a text representation of a protocol message into a message."""
    def MergeLines(self, lines, message):
        """Merges a text representation of a protocol message into a message."""

class Tokenizer:
    """Protocol buffer text representation tokenizer.

  This class handles the lower level string parsing by splitting it into
  meaningful tokens.

  It was directly ported from the Java protocol buffer API.
  """
    token: str
    def __init__(self, lines, skip_comments: bool = True) -> None: ...
    def LookingAt(self, token): ...
    def AtEnd(self):
        """Checks the end of the text was reached.

    Returns:
      True iff the end was reached.
    """
    def TryConsume(self, token):
        """Tries to consume a given piece of text.

    Args:
      token: Text to consume.

    Returns:
      True iff the text was consumed.
    """
    def Consume(self, token) -> None:
        """Consumes a piece of text.

    Args:
      token: Text to consume.

    Raises:
      ParseError: If the text couldn't be consumed.
    """
    def ConsumeComment(self): ...
    def ConsumeCommentOrTrailingComment(self):
        """Consumes a comment, returns a 2-tuple (trailing bool, comment str)."""
    def TryConsumeIdentifier(self): ...
    def ConsumeIdentifier(self):
        """Consumes protocol message field identifier.

    Returns:
      Identifier string.

    Raises:
      ParseError: If an identifier couldn't be consumed.
    """
    def TryConsumeIdentifierOrNumber(self): ...
    def ConsumeIdentifierOrNumber(self):
        """Consumes protocol message field identifier.

    Returns:
      Identifier string.

    Raises:
      ParseError: If an identifier couldn't be consumed.
    """
    def TryConsumeInteger(self): ...
    def ConsumeInteger(self):
        """Consumes an integer number.

    Returns:
      The integer parsed.

    Raises:
      ParseError: If an integer couldn't be consumed.
    """
    def TryConsumeFloat(self): ...
    def ConsumeFloat(self):
        """Consumes an floating point number.

    Returns:
      The number parsed.

    Raises:
      ParseError: If a floating point number couldn't be consumed.
    """
    def ConsumeBool(self):
        """Consumes a boolean value.

    Returns:
      The bool parsed.

    Raises:
      ParseError: If a boolean value couldn't be consumed.
    """
    def TryConsumeByteString(self): ...
    def ConsumeString(self):
        """Consumes a string value.

    Returns:
      The string parsed.

    Raises:
      ParseError: If a string value couldn't be consumed.
    """
    def ConsumeByteString(self):
        """Consumes a byte array value.

    Returns:
      The array parsed (as a string).

    Raises:
      ParseError: If a byte array value couldn't be consumed.
    """
    def ConsumeEnum(self, field): ...
    def ParseErrorPreviousToken(self, message):
        """Creates and *returns* a ParseError for the previously read token.

    Args:
      message: A message to set for the exception.

    Returns:
      A ParseError instance.
    """
    def ParseError(self, message):
        """Creates and *returns* a ParseError for the current token."""
    def NextToken(self) -> None:
        """Reads the next meaningful token."""
