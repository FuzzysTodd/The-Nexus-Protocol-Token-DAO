from _typeshed import Incomplete
from absl.flags import _argument_parser
from typing import Any, Dict, Generic, Iterable, List, Text, Type
from xml.dom import minidom as minidom

class Flag(Generic[_T]):
    '''Information about a command-line flag.

  Attributes:
    name: the name for this flag
    default: the default value for this flag
    default_unparsed: the unparsed default value for this flag.
    default_as_str: default value as repr\'d string, e.g., "\'true\'"
      (or None)
    value: the most recent parsed value of this flag set by :meth:`parse`
    help: a help string or None if no help is available
    short_name: the single letter alias for this flag (or None)
    boolean: if \'true\', this flag does not accept arguments
    present: true if this flag was parsed from command line flags
    parser: an :class:`~absl.flags.ArgumentParser` object
    serializer: an ArgumentSerializer object
    allow_override: the flag may be redefined without raising an error,
      and newly defined flag overrides the old one.
    allow_override_cpp: use the flag from C++ if available the flag
      definition is replaced by the C++ flag after init
    allow_hide_cpp: use the Python flag despite having a C++ flag with
      the same name (ignore the C++ flag)
    using_default_value: the flag value has not been set by user
    allow_overwrite: the flag may be parsed more than once without
      raising an error, the last set value will be used
    allow_using_method_names: whether this flag can be defined even if
      it has a name that conflicts with a FlagValues method.
    validators: list of the flag validators.

  The only public method of a ``Flag`` object is :meth:`parse`, but it is
  typically only called by a :class:`~absl.flags.FlagValues` object.  The
  :meth:`parse` method is a thin wrapper around the
  :meth:`ArgumentParser.parse()<absl.flags.ArgumentParser.parse>` method.  The
  parsed value is saved in ``.value``, and the ``.present`` attribute is
  updated.  If this flag was already present, an Error is raised.

  :meth:`parse` is also called during ``__init__`` to parse the default value
  and initialize the ``.value`` attribute.  This enables other python modules to
  safely use flags even if the ``__main__`` module neglects to parse the
  command line arguments.  The ``.present`` attribute is cleared after
  ``__init__`` parsing.  If the default value is set to ``None``, then the
  ``__init__`` parsing step is skipped and the ``.value`` attribute is
  initialized to None.

  Note: The default value is also presented to the user in the help
  string, so it is important that it be a legal value for this flag.
  '''
    default: _T | None
    default_as_str: Text | None
    default_unparsed: _T | None | Text
    name: Incomplete
    help: Incomplete
    short_name: Incomplete
    boolean: Incomplete
    present: int
    parser: Incomplete
    serializer: Incomplete
    allow_override: Incomplete
    allow_override_cpp: Incomplete
    allow_hide_cpp: Incomplete
    allow_overwrite: Incomplete
    allow_using_method_names: Incomplete
    using_default_value: bool
    validators: Incomplete
    def __init__(self, parser: _argument_parser.ArgumentParser[_T], serializer: _argument_parser.ArgumentSerializer[_T] | None, name: Text, default: _T | None | Text, help_string: Text | None, short_name: Text | None = None, boolean: bool = False, allow_override: bool = False, allow_override_cpp: bool = False, allow_hide_cpp: bool = False, allow_overwrite: bool = True, allow_using_method_names: bool = False) -> None: ...
    @property
    def value(self) -> _T | None: ...
    @value.setter
    def value(self, value: _T | None): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...
    def __deepcopy__(self, memo: Dict[int, Any]) -> Flag[_T]: ...
    def parse(self, argument: Text | _T | None) -> None:
        """Parses string and sets flag value.

    Args:
      argument: str or the correct flag value type, argument to be parsed.
    """
    def unparse(self) -> None: ...
    def serialize(self) -> Text:
        """Serializes the flag."""
    def flag_type(self) -> Text:
        """Returns a str that describes the type of the flag.

    NOTE: we use strings, and not the types.*Type constants because
    our flags can have more exotic types, e.g., 'comma separated list
    of strings', 'whitespace separated list of strings', etc.
    """

class BooleanFlag(Flag[bool]):
    """Basic boolean flag.

  Boolean flags do not take any arguments, and their value is either
  ``True`` (1) or ``False`` (0).  The false value is specified on the command
  line by prepending the word ``'no'`` to either the long or the short flag
  name.

  For example, if a Boolean flag was created whose long name was
  ``'update'`` and whose short name was ``'x'``, then this flag could be
  explicitly unset through either ``--noupdate`` or ``--nox``.
  """
    def __init__(self, name: Text, default: bool | None | Text, help: Text | None, short_name: Text | None = None, **args) -> None: ...

class EnumFlag(Flag[Text]):
    """Basic enum flag; its value can be any string from list of enum_values."""
    parser: Incomplete
    help: Incomplete
    def __init__(self, name: Text, default: Text | None, help: Text | None, enum_values: Iterable[Text], short_name: Text | None = None, case_sensitive: bool = True, **args) -> None: ...

class EnumClassFlag(Flag[_ET]):
    """Basic enum flag; its value is an enum class's member."""
    parser: Incomplete
    help: Incomplete
    def __init__(self, name: Text, default: _ET | None | Text, help: Text | None, enum_class: Type[_ET], short_name: Text | None = None, case_sensitive: bool = False, **args) -> None: ...

class MultiFlag(Flag[List[_T]], Generic[_T]):
    """A flag that can appear multiple time on the command-line.

  The value of such a flag is a list that contains the individual values
  from all the appearances of that flag on the command-line.

  See the __doc__ for Flag for most behavior of this class.  Only
  differences in behavior are described here:

    * The default value may be either a single value or an iterable of values.
      A single value is transformed into a single-item list of that value.

    * The value of the flag is always a list, even if the option was
      only supplied once, and even if the default value is a single
      value
  """
    def __init__(self, *args, **kwargs) -> None: ...
    value: Incomplete
    def parse(self, arguments: Text | _T | Iterable[_T]):
        """Parses one or more arguments with the installed parser.

    Args:
      arguments: a single argument or a list of arguments (typically a
        list of default values); a single argument is converted
        internally into a list containing one item.
    """
    def flag_type(self):
        """See base class."""

class MultiEnumClassFlag(MultiFlag[_ET]):
    """A multi_enum_class flag.

  See the __doc__ for MultiFlag for most behaviors of this class.  In addition,
  this class knows how to handle enum.Enum instances as values for this flag
  type.
  """
    parser: Incomplete
    serializer: Incomplete
    help: Incomplete
    def __init__(self, name: str, default: None | Iterable[_ET] | _ET | Iterable[Text] | Text, help_string: str, enum_class: Type[_ET], case_sensitive: bool = False, **args) -> None: ...
