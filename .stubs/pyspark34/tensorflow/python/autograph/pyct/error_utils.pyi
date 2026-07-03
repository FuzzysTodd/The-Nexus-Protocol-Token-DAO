from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import origin_info as origin_info
from tensorflow.python.util import traceback_utils as traceback_utils
from typing import NamedTuple

class FrameInfo(NamedTuple('FrameInfo', [('filename', Incomplete), ('lineno', Incomplete), ('function_name', Incomplete), ('code', Incomplete), ('is_converted', Incomplete), ('is_allowlisted', Incomplete)])): ...

KNOWN_STRING_CONSTRUCTOR_ERRORS: Incomplete

class MultilineMessageKeyError(KeyError):
    def __init__(self, message, original_key) -> None: ...

class ErrorMetadataBase:
    """Container objects attached to exceptions raised in user code.

  This metadata allows re-raising exceptions that occur in generated code, with
  a custom error message that includes a stack trace relative to user-readable
  code from which the generated code originated.
  """
    translated_stack: Incomplete
    cause_message: Incomplete
    def __init__(self, callsite_tb, cause_metadata, cause_message, source_map, converter_filename) -> None: ...
    def get_message(self):
        """Returns the message for the underlying exception."""
    def create_exception(self, source_error):
        """Creates exception from source_error."""
    def to_exception(self, source_error): ...
