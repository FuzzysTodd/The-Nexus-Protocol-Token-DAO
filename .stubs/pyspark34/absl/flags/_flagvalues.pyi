from _typeshed import Incomplete
from absl.flags._flag import Flag as Flag
from typing import Any, Dict, Generic, Iterable, Iterator, List, Sequence, Text, TextIO, Tuple

class FlagValues:
    """Registry of :class:`~absl.flags.Flag` objects.

  A :class:`FlagValues` can then scan command line arguments, passing flag
  arguments through to the 'Flag' objects that it owns.  It also
  provides easy access to the flag values.  Typically only one
  :class:`FlagValues` object is needed by an application:
  :const:`FLAGS`.

  This class is heavily overloaded:

  :class:`Flag` objects are registered via ``__setitem__``::

       FLAGS['longname'] = x   # register a new flag

  The ``.value`` attribute of the registered :class:`~absl.flags.Flag` objects
  can be accessed as attributes of this :class:`FlagValues` object, through
  ``__getattr__``.  Both the long and short name of the original
  :class:`~absl.flags.Flag` objects can be used to access its value::

       FLAGS.longname  # parsed flag value
       FLAGS.x  # parsed flag value (short name)

  Command line arguments are scanned and passed to the registered
  :class:`~absl.flags.Flag` objects through the ``__call__`` method.  Unparsed
  arguments, including ``argv[0]`` (e.g. the program name) are returned::

       argv = FLAGS(sys.argv)  # scan command line arguments

  The original registered :class:`~absl.flags.Flag` objects can be retrieved
  through the use of the dictionary-like operator, ``__getitem__``::

       x = FLAGS['longname']   # access the registered Flag object

  The ``str()`` operator of a :class:`absl.flags.FlagValues` object provides
  help for all of the registered :class:`~absl.flags.Flag` objects.
  """
    __dict__: Dict[str, Any]
    def __init__(self) -> None: ...
    def set_gnu_getopt(self, gnu_getopt: bool = True) -> None:
        """Sets whether or not to use GNU style scanning.

    GNU style allows mixing of flag and non-flag arguments. See
    http://docs.python.org/library/getopt.html#getopt.gnu_getopt

    Args:
      gnu_getopt: bool, whether or not to use GNU style scanning.
    """
    def is_gnu_getopt(self) -> bool: ...
    def flags_by_module_dict(self) -> Dict[Text, List[Flag]]:
        """Returns the dictionary of module_name -> list of defined flags.

    Returns:
      A dictionary.  Its keys are module names (strings).  Its values
      are lists of Flag objects.
    """
    def flags_by_module_id_dict(self) -> Dict[int, List[Flag]]:
        """Returns the dictionary of module_id -> list of defined flags.

    Returns:
      A dictionary.  Its keys are module IDs (ints).  Its values
      are lists of Flag objects.
    """
    def key_flags_by_module_dict(self) -> Dict[Text, List[Flag]]:
        """Returns the dictionary of module_name -> list of key flags.

    Returns:
      A dictionary.  Its keys are module names (strings).  Its values
      are lists of Flag objects.
    """
    def register_flag_by_module(self, module_name: Text, flag: Flag) -> None:
        """Records the module that defines a specific flag.

    We keep track of which flag is defined by which module so that we
    can later sort the flags by module.

    Args:
      module_name: str, the name of a Python module.
      flag: Flag, the Flag instance that is key to the module.
    """
    def register_flag_by_module_id(self, module_id: int, flag: Flag) -> None:
        """Records the module that defines a specific flag.

    Args:
      module_id: int, the ID of the Python module.
      flag: Flag, the Flag instance that is key to the module.
    """
    def register_key_flag_for_module(self, module_name: Text, flag: Flag) -> None:
        """Specifies that a flag is a key flag for a module.

    Args:
      module_name: str, the name of a Python module.
      flag: Flag, the Flag instance that is key to the module.
    """
    def get_flags_for_module(self, module: Text | Any) -> List[Flag]:
        """Returns the list of flags defined by a module.

    Args:
      module: module|str, the module to get flags from.

    Returns:
      [Flag], a new list of Flag instances.  Caller may update this list as
      desired: none of those changes will affect the internals of this
      FlagValue instance.
    """
    def get_key_flags_for_module(self, module: Text | Any) -> List[Flag]:
        """Returns the list of key flags for a module.

    Args:
      module: module|str, the module to get key flags from.

    Returns:
      [Flag], a new list of Flag instances.  Caller may update this list as
      desired: none of those changes will affect the internals of this
      FlagValue instance.
    """
    def find_module_defining_flag(self, flagname: Text, default: _T | None = None) -> str | _T | None:
        """Return the name of the module defining this flag, or default.

    Args:
      flagname: str, name of the flag to lookup.
      default: Value to return if flagname is not defined. Defaults to None.

    Returns:
      The name of the module which registered the flag with this name.
      If no such module exists (i.e. no flag with this name exists),
      we return default.
    """
    def find_module_id_defining_flag(self, flagname: Text, default: _T | None = None) -> int | _T | None:
        """Return the ID of the module defining this flag, or default.

    Args:
      flagname: str, name of the flag to lookup.
      default: Value to return if flagname is not defined. Defaults to None.

    Returns:
      The ID of the module which registered the flag with this name.
      If no such module exists (i.e. no flag with this name exists),
      we return default.
    """
    def append_flag_values(self, flag_values: FlagValues) -> None:
        """Appends flags registered in another FlagValues instance.

    Args:
      flag_values: FlagValues, the FlagValues instance from which to copy flags.
    """
    def remove_flag_values(self, flag_values: FlagValues | Iterable[Text]) -> None:
        """Remove flags that were previously appended from another FlagValues.

    Args:
      flag_values: FlagValues, the FlagValues instance containing flags to
        remove.
    """
    def __setitem__(self, name: Text, flag: Flag) -> None:
        """Registers a new flag variable."""
    def __dir__(self) -> List[Text]:
        """Returns list of names of all defined flags.

    Useful for TAB-completion in ipython.

    Returns:
      [str], a list of names of all defined flags.
    """
    def __getitem__(self, name: Text) -> Flag:
        """Returns the Flag object for the flag --name."""
    def __getattr__(self, name: Text) -> Any:
        """Retrieves the 'value' attribute of the flag --name."""
    def __setattr__(self, name: Text, value: _T) -> _T:
        """Sets the 'value' attribute of the flag --name."""
    def validate_all_flags(self) -> None:
        """Verifies whether all flags pass validation.

    Raises:
      AttributeError: Raised if validators work with a non-existing flag.
      IllegalFlagValueError: Raised if validation fails for at least one
          validator.
    """
    def __delattr__(self, flag_name: Text) -> None:
        """Deletes a previously-defined flag from a flag object.

    This method makes sure we can delete a flag by using

      del FLAGS.<flag_name>

    E.g.,

      flags.DEFINE_integer('foo', 1, 'Integer flag.')
      del flags.FLAGS.foo

    If a flag is also registered by its the other name (long name or short
    name), the other name won't be deleted.

    Args:
      flag_name: str, the name of the flag to be deleted.

    Raises:
      AttributeError: Raised when there is no registered flag named flag_name.
    """
    def set_default(self, name: Text, value: Any) -> None:
        """Changes the default value of the named flag object.

    The flag's current value is also updated if the flag is currently using
    the default value, i.e. not specified in the command line, and not set
    by FLAGS.name = value.

    Args:
      name: str, the name of the flag to modify.
      value: The new default value.

    Raises:
      UnrecognizedFlagError: Raised when there is no registered flag named name.
      IllegalFlagValueError: Raised when value is not valid.
    """
    def __contains__(self, name: Text) -> bool:
        """Returns True if name is a value (flag) in the dict."""
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Text]: ...
    def __call__(self, argv: Sequence[Text], known_only: bool = False) -> List[Text]:
        """Parses flags from argv; stores parsed flags into this FlagValues object.

    All unparsed arguments are returned.

    Args:
       argv: a tuple/list of strings.
       known_only: bool, if True, parse and remove known flags; return the rest
         untouched. Unknown flags specified by --undefok are not returned.

    Returns:
       The list of arguments not parsed as options, including argv[0].

    Raises:
       Error: Raised on any parsing error.
       TypeError: Raised on passing wrong type of arguments.
       ValueError: Raised on flag value parsing error.
    """
    def __copy__(self) -> Any: ...
    def __deepcopy__(self, memo) -> Any: ...
    def is_parsed(self) -> bool:
        """Returns whether flags were parsed."""
    def mark_as_parsed(self) -> None:
        """Explicitly marks flags as parsed.

    Use this when the caller knows that this FlagValues has been parsed as if
    a ``__call__()`` invocation has happened.  This is only a public method for
    use by things like appcommands which do additional command like parsing.
    """
    def unparse_flags(self) -> None:
        """Unparses all flags to the point before any FLAGS(argv) was called."""
    def flag_values_dict(self) -> Dict[Text, Any]:
        """Returns a dictionary that maps flag names to flag values."""
    def get_help(self, prefix: Text = '', include_special_flags: bool = True) -> Text:
        """Returns a help string for all known flags.

    Args:
      prefix: str, per-line output prefix.
      include_special_flags: bool, whether to include description of
        SPECIAL_FLAGS, i.e. --flagfile and --undefok.

    Returns:
      str, formatted help message.
    """
    def module_help(self, module: Any) -> Text:
        """Describes the key flags of a module.

    Args:
      module: module|str, the module to describe the key flags for.

    Returns:
      str, describing the key flags of a module.
    """
    def main_module_help(self) -> Text:
        """Describes the key flags of the main module.

    Returns:
      str, describing the key flags of the main module.
    """
    def get_flag_value(self, name: Text, default: Any) -> Any:
        """Returns the value of a flag (if not None) or a default value.

    Args:
      name: str, the name of a flag.
      default: Default value to use if the flag value is None.

    Returns:
      Requested flag value or default.
    """
    def read_flags_from_files(self, argv: Sequence[Text], force_gnu: bool = True) -> List[Text]:
        '''Processes command line args, but also allow args to be read from file.

    Args:
      argv: [str], a list of strings, usually sys.argv[1:], which may contain
        one or more flagfile directives of the form --flagfile="./filename".
        Note that the name of the program (sys.argv[0]) should be omitted.
      force_gnu: bool, if False, --flagfile parsing obeys the
        FLAGS.is_gnu_getopt() value. If True, ignore the value and always follow
        gnu_getopt semantics.

    Returns:
      A new list which has the original list combined with what we read
      from any flagfile(s).

    Raises:
      IllegalFlagValueError: Raised when --flagfile is provided with no
          argument.

    This function is called by FLAGS(argv).
    It scans the input list for a flag that looks like:
    --flagfile=<somefile>. Then it opens <somefile>, reads all valid key
    and value pairs and inserts them into the input list in exactly the
    place where the --flagfile arg is found.

    Note that your application\'s flags are still defined the usual way
    using absl.flags DEFINE_flag() type functions.

    Notes (assuming we\'re getting a commandline of some sort as our input):

    * For duplicate flags, the last one we hit should "win".
    * Since flags that appear later win, a flagfile\'s settings can be "weak"
        if the --flagfile comes at the beginning of the argument sequence,
        and it can be "strong" if the --flagfile comes at the end.
    * A further "--flagfile=<otherfile.cfg>" CAN be nested in a flagfile.
        It will be expanded in exactly the spot where it is found.
    * In a flagfile, a line beginning with # or // is a comment.
    * Entirely blank lines _should_ be ignored.
    '''
    def flags_into_string(self) -> Text:
        """Returns a string with the flags assignments from this FlagValues object.

    This function ignores flags whose value is None.  Each flag
    assignment is separated by a newline.

    NOTE: MUST mirror the behavior of the C++ CommandlineFlagsIntoString
    from https://github.com/gflags/gflags.

    Returns:
      str, the string with the flags assignments from this FlagValues object.
      The flags are ordered by (module_name, flag_name).
    """
    def append_flags_into_file(self, filename: Text) -> None:
        """Appends all flags assignments from this FlagInfo object to a file.

    Output will be in the format of a flagfile.

    NOTE: MUST mirror the behavior of the C++ AppendFlagsIntoFile
    from https://github.com/gflags/gflags.

    Args:
      filename: str, name of the file.
    """
    def write_help_in_xml_format(self, outfile: TextIO | None = None) -> None:
        """Outputs flag documentation in XML format.

    NOTE: We use element names that are consistent with those used by
    the C++ command-line flag library, from
    https://github.com/gflags/gflags.
    We also use a few new elements (e.g., <key>), but we do not
    interfere / overlap with existing XML elements used by the C++
    library.  Please maintain this consistency.

    Args:
      outfile: File object we write to.  Default None means sys.stdout.
    """

FLAGS: Incomplete

class FlagHolder(Generic[_T]):
    """Holds a defined flag.

  This facilitates a cleaner api around global state. Instead of::

      flags.DEFINE_integer('foo', ...)
      flags.DEFINE_integer('bar', ...)

      def method():
        # prints parsed value of 'bar' flag
        print(flags.FLAGS.foo)
        # runtime error due to typo or possibly bad coding style.
        print(flags.FLAGS.baz)

  it encourages code like::

      _FOO_FLAG = flags.DEFINE_integer('foo', ...)
      _BAR_FLAG = flags.DEFINE_integer('bar', ...)

      def method():
        print(_FOO_FLAG.value)
        print(_BAR_FLAG.value)

  since the name of the flag appears only once in the source code.
  """
    value: _T
    def __init__(self, flag_values: FlagValues, flag: Flag[_T], ensure_non_none_value: bool = False) -> None:
        """Constructs a FlagHolder instance providing typesafe access to flag.

    Args:
      flag_values: The container the flag is registered to.
      flag: The flag object for this flag.
      ensure_non_none_value: Is the value of the flag allowed to be None.
    """
    def __eq__(self, other): ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    @property
    def name(self) -> Text: ...
    @property
    def value(self) -> _T:
        """Returns the value of the flag.

    If ``_ensure_non_none_value`` is ``True``, then return value is not
    ``None``.

    Raises:
      UnparsedFlagAccessError: if flag parsing has not finished.
      IllegalFlagValueError: if value is None unexpectedly.
    """
    @property
    def default(self) -> _T:
        """Returns the default value of the flag."""
    @property
    def present(self) -> bool:
        """Returns True if the flag was parsed from command-line flags."""

def resolve_flag_ref(flag_ref: str | FlagHolder, flag_values: FlagValues) -> Tuple[str, FlagValues]:
    """Helper to validate and resolve a flag reference argument."""
def resolve_flag_refs(flag_refs: Sequence[str | FlagHolder], flag_values: FlagValues) -> Tuple[List[str], FlagValues]:
    """Helper to validate and resolve flag reference list arguments."""
