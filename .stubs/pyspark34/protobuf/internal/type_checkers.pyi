from _typeshed import Incomplete

def TruncateToFourByteFloat(original): ...
def ToShortestFloat(original):
    """Returns the shortest float that has same value in wire."""
def SupportsOpenEnums(field_descriptor): ...
def GetTypeChecker(field):
    """Returns a type checker for a message field of the specified types.

  Args:
    field: FieldDescriptor object for this field.

  Returns:
    An instance of TypeChecker which can be used to verify the types
    of values assigned to a field of the specified type.
  """

class TypeChecker:
    """Type checker used to catch type errors as early as possible
  when the client is setting scalar fields in protocol messages.
  """
    def __init__(self, *acceptable_types) -> None: ...
    def CheckValue(self, proposed_value):
        """Type check the provided value and return it.

    The returned value might have been normalized to another type.
    """

class TypeCheckerWithDefault(TypeChecker):
    def __init__(self, default_value, *acceptable_types) -> None: ...
    def DefaultValue(self): ...

class BoolValueChecker:
    """Type checker used for bool fields."""
    def CheckValue(self, proposed_value): ...
    def DefaultValue(self): ...

class IntValueChecker:
    """Checker used for integer fields.  Performs type-check and range check."""
    def CheckValue(self, proposed_value): ...
    def DefaultValue(self): ...

class EnumValueChecker:
    """Checker used for enum fields.  Performs type-check and range check."""
    def __init__(self, enum_type) -> None: ...
    def CheckValue(self, proposed_value): ...
    def DefaultValue(self): ...

class UnicodeValueChecker:
    """Checker used for string fields.

  Always returns a unicode value, even if the input is of type str.
  """
    def CheckValue(self, proposed_value): ...
    def DefaultValue(self): ...

class Int32ValueChecker(IntValueChecker): ...
class Uint32ValueChecker(IntValueChecker): ...
class Int64ValueChecker(IntValueChecker): ...
class Uint64ValueChecker(IntValueChecker): ...

class DoubleValueChecker:
    """Checker used for double fields.

  Performs type-check and range check.
  """
    def CheckValue(self, proposed_value):
        """Check and convert proposed_value to float."""
    def DefaultValue(self): ...

class FloatValueChecker(DoubleValueChecker):
    """Checker used for float fields.

  Performs type-check and range check.

  Values exceeding a 32-bit float will be converted to inf/-inf.
  """
    def CheckValue(self, proposed_value):
        """Check and convert proposed_value to float."""

TYPE_TO_BYTE_SIZE_FN: Incomplete
TYPE_TO_ENCODER: Incomplete
TYPE_TO_SIZER: Incomplete
TYPE_TO_DECODER: Incomplete
FIELD_TYPE_TO_WIRE_TYPE: Incomplete
