from _typeshed import Incomplete
from typing import Generic, Iterable, List, Sequence, Text, Type
from xml.dom import minidom as minidom

class _ArgumentParserCache(type):
    """Metaclass used to cache and share argument parsers among flags."""
    def __call__(cls, *args, **kwargs):
        """Returns an instance of the argument parser cls.

    This method overrides behavior of the __new__ methods in
    all subclasses of ArgumentParser (inclusive). If an instance
    for cls with the same set of arguments exists, this instance is
    returned, otherwise a new instance is created.

    If any keyword arguments are defined, or the values in args
    are not hashable, this method always returns a new instance of
    cls.

    Args:
      *args: Positional initializer arguments.
      **kwargs: Initializer keyword arguments.

    Returns:
      An instance of cls, shared or new.
    """

class ArgumentParser(Generic[_T], metaclass=_ArgumentParserCache):
    """Base class used to parse and convert arguments.

  The :meth:`parse` method checks to make sure that the string argument is a
  legal value and convert it to a native type.  If the value cannot be
  converted, it should throw a ``ValueError`` exception with a human
  readable explanation of why the value is illegal.

  Subclasses should also define a syntactic_help string which may be
  presented to the user to describe the form of the legal values.

  Argument parser classes must be stateless, since instances are cached
  and shared between flags. Initializer arguments are allowed, but all
  member variables must be derived from initializer arguments only.
  """
    syntactic_help: Text
    def parse(self, argument: Text) -> _T | None:
        """Parses the string argument and returns the native value.

    By default it returns its argument unmodified.

    Args:
      argument: string argument passed in the commandline.

    Raises:
      ValueError: Raised when it fails to parse the argument.
      TypeError: Raised when the argument has the wrong type.

    Returns:
      The parsed value in native type.
    """
    def flag_type(self) -> Text:
        """Returns a string representing the type of the flag."""

class ArgumentSerializer(Generic[_T]):
    """Base class for generating string representations of a flag value."""
    def serialize(self, value: _T) -> Text:
        """Returns a serialized string of the value."""

class NumericParser(ArgumentParser[_N]):
    """Parser of numeric values.

  Parsed value may be bounded to a given upper and lower bound.
  """
    lower_bound: _N | None
    upper_bound: _N | None
    def is_outside_bounds(self, val: _N) -> bool:
        """Returns whether the value is outside the bounds or not."""
    def parse(self, argument: Text) -> _N:
        """See base class."""
    def convert(self, argument: Text) -> _N:
        """Returns the correct numeric value of argument.

    Subclass must implement this method, and raise TypeError if argument is not
    string or has the right numeric type.

    Args:
      argument: string argument passed in the commandline, or the numeric type.

    Raises:
      TypeError: Raised when argument is not a string or the right numeric type.
      ValueError: Raised when failed to convert argument to the numeric value.
    """

class FloatParser(NumericParser[float]):
    """Parser of floating point values.

  Parsed value may be bounded to a given upper and lower bound.
  """
    number_article: str
    number_name: str
    syntactic_help: Incomplete
    lower_bound: Incomplete
    upper_bound: Incomplete
    def __init__(self, lower_bound: float | None = None, upper_bound: float | None = None) -> None: ...
    def convert(self, argument: int | float | str) -> float:
        """Returns the float value of argument."""
    def flag_type(self) -> Text:
        """See base class."""

class IntegerParser(NumericParser[int]):
    """Parser of an integer value.

  Parsed value may be bounded to a given upper and lower bound.
  """
    number_article: str
    number_name: str
    syntactic_help: Incomplete
    lower_bound: Incomplete
    upper_bound: Incomplete
    def __init__(self, lower_bound: int | None = None, upper_bound: int | None = None) -> None: ...
    def convert(self, argument: int | Text) -> int:
        """Returns the int value of argument."""
    def flag_type(self) -> Text:
        """See base class."""

class BooleanParser(ArgumentParser[bool]):
    """Parser of boolean values."""
    def parse(self, argument: Text | int) -> bool:
        """See base class."""
    def flag_type(self) -> Text:
        """See base class."""

class EnumParser(ArgumentParser[Text]):
    """Parser of a string enum value (a string value from a given set)."""
    enum_values: Incomplete
    case_sensitive: Incomplete
    def __init__(self, enum_values: Iterable[Text], case_sensitive: bool = True) -> None:
        """Initializes EnumParser.

    Args:
      enum_values: [str], a non-empty list of string values in the enum.
      case_sensitive: bool, whether or not the enum is to be case-sensitive.

    Raises:
      ValueError: When enum_values is empty.
    """
    def parse(self, argument: Text) -> Text:
        """Determines validity of argument and returns the correct element of enum.

    Args:
      argument: str, the supplied flag value.

    Returns:
      The first matching element from enum_values.

    Raises:
      ValueError: Raised when argument didn't match anything in enum.
    """
    def flag_type(self) -> Text:
        """See base class."""

class EnumClassParser(ArgumentParser[_ET]):
    """Parser of an Enum class member."""
    enum_class: Incomplete
    def __init__(self, enum_class: Type[_ET], case_sensitive: bool = True) -> None:
        """Initializes EnumParser.

    Args:
      enum_class: class, the Enum class with all possible flag values.
      case_sensitive: bool, whether or not the enum is to be case-sensitive. If
        False, all member names must be unique when case is ignored.

    Raises:
      TypeError: When enum_class is not a subclass of Enum.
      ValueError: When enum_class is empty.
    """
    @property
    def member_names(self) -> Sequence[Text]:
        """The accepted enum names, in lowercase if not case sensitive."""
    def parse(self, argument: _ET | Text) -> _ET:
        """Determines validity of argument and returns the correct element of enum.

    Args:
      argument: str or Enum class member, the supplied flag value.

    Returns:
      The first matching Enum class member in Enum class.

    Raises:
      ValueError: Raised when argument didn't match anything in enum.
    """
    def flag_type(self) -> Text:
        """See base class."""

class ListSerializer(ArgumentSerializer[List[_T]], Generic[_T]):
    list_sep: Incomplete
    def __init__(self, list_sep: Text) -> None: ...
    def serialize(self, value: List[_T]) -> Text:
        """See base class."""

class EnumClassListSerializer(ListSerializer[_ET]):
    """A serializer for :class:`MultiEnumClass` flags.

  This serializer simply joins the output of `EnumClassSerializer` using a
  provided separator.
  """
    def __init__(self, list_sep: Text, **kwargs) -> None:
        """Initializes EnumClassListSerializer.

    Args:
      list_sep: String to be used as a separator when serializing
      **kwargs: Keyword arguments to the `EnumClassSerializer` used to serialize
        individual values.
    """
    def serialize(self, value: _ET | List[_ET]) -> Text:
        """See base class."""

class CsvListSerializer(ListSerializer[Text]):
    def serialize(self, value: List[Text]) -> Text:
        """Serializes a list as a CSV string or unicode."""

class EnumClassSerializer(ArgumentSerializer):
    """Class for generating string representations of an enum class flag value."""
    def __init__(self, lowercase: bool) -> None:
        """Initializes EnumClassSerializer.

    Args:
      lowercase: If True, enum member names are lowercased during serialization.
    """
    def serialize(self, value: _ET) -> Text:
        """Returns a serialized string of the Enum class value."""

class BaseListParser(ArgumentParser):
    """Base class for a parser of lists of strings.

  To extend, inherit from this class; from the subclass ``__init__``, call::

      super().__init__(token, name)

  where token is a character used to tokenize, and name is a description
  of the separator.
  """
    syntactic_help: Incomplete
    def __init__(self, token: Text | None = None, name: Text | None = None) -> None: ...
    def parse(self, argument: Text) -> List[Text]:
        """See base class."""
    def flag_type(self) -> Text:
        """See base class."""

class ListParser(BaseListParser):
    """Parser for a comma-separated list of strings."""
    def __init__(self) -> None: ...
    def parse(self, argument: Text | List[Text]) -> List[Text]:
        """Parses argument as comma-separated list of strings."""

class WhitespaceSeparatedListParser(BaseListParser):
    """Parser for a whitespace-separated list of strings."""
    def __init__(self, comma_compat: bool = False) -> None:
        """Initializer.

    Args:
      comma_compat: bool, whether to support comma as an additional separator.
          If False then only whitespace is supported.  This is intended only for
          backwards compatibility with flags that used to be comma-separated.
    """
    def parse(self, argument: Text | List[Text]) -> List[Text]:
        """Parses argument as whitespace-separated list of strings.

    It also parses argument as comma-separated list of strings if requested.

    Args:
      argument: string argument passed in the commandline.

    Returns:
      [str], the parsed flag value.
    """
