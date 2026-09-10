from _typeshed import Incomplete

class EnumTypeWrapper:
    """A utility for finding the names of enum values."""
    DESCRIPTOR: Incomplete
    ValueType = int
    def __init__(self, enum_type) -> None:
        """Inits EnumTypeWrapper with an EnumDescriptor."""
    def Name(self, number):
        """Returns a string containing the name of an enum value."""
    def Value(self, name):
        """Returns the value corresponding to the given enum name."""
    def keys(self):
        """Return a list of the string names in the enum.

    Returns:
      A list of strs, in the order they were defined in the .proto file.
    """
    def values(self):
        """Return a list of the integer values in the enum.

    Returns:
      A list of ints, in the order they were defined in the .proto file.
    """
    def items(self):
        """Return a list of the (name, value) pairs of the enum.

    Returns:
      A list of (str, int) pairs, in the order they were defined
      in the .proto file.
    """
    def __getattr__(self, name):
        """Returns the value corresponding to the given enum name."""
