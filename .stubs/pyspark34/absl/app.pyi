from _typeshed import Incomplete
from absl import command_name as command_name, flags as flags, logging as logging

FLAGS: Incomplete
EXCEPTION_HANDLERS: Incomplete

class Error(Exception): ...

class UsageError(Error):
    """Exception raised when the arguments supplied by the user are invalid.

  Raise this when the arguments supplied are invalid from the point of
  view of the application. For example when two mutually exclusive
  flags have been supplied or when there are not enough non-flag
  arguments. It is distinct from flags.Error which covers the lower
  level of parsing and validating individual flags.
  """
    exitcode: Incomplete
    def __init__(self, message, exitcode: int = 1) -> None: ...

class HelpFlag(flags.BooleanFlag):
    """Special boolean flag that displays usage and raises SystemExit."""
    NAME: str
    SHORT_NAME: str
    def __init__(self) -> None: ...
    def parse(self, arg) -> None: ...

class HelpshortFlag(HelpFlag):
    """--helpshort is an alias for --help."""
    NAME: str
    SHORT_NAME: Incomplete

class HelpfullFlag(flags.BooleanFlag):
    """Display help for flags in the main module and all dependent modules."""
    def __init__(self) -> None: ...
    def parse(self, arg) -> None: ...

class HelpXMLFlag(flags.BooleanFlag):
    """Similar to HelpfullFlag, but generates output in XML format."""
    def __init__(self) -> None: ...
    def parse(self, arg) -> None: ...

def parse_flags_with_usage(args):
    """Tries to parse the flags, print usage, and exit if unparsable.

  Args:
    args: [str], a non-empty list of the command line arguments including
        program name.

  Returns:
    [str], a non-empty list of remaining command line arguments after parsing
    flags, including program name.
  """
def define_help_flags() -> None:
    """Registers help flags. Idempotent."""
def run(main, argv: Incomplete | None = None, flags_parser=...) -> None:
    '''Begins executing the program.

  Args:
    main: The main function to execute. It takes an single argument "argv",
        which is a list of command line arguments with parsed flags removed.
        The return value is passed to `sys.exit`, and so for example
        a return value of 0 or None results in a successful termination, whereas
        a return value of 1 results in abnormal termination.
        For more details, see https://docs.python.org/3/library/sys#sys.exit
    argv: A non-empty list of the command line arguments including program name,
        sys.argv is used if None.
    flags_parser: Callable[[List[Text]], Any], the function used to parse flags.
        The return value of this function is passed to `main` untouched.
        It must guarantee FLAGS is parsed after this function is called.
        Should be passed as a keyword-only arg which will become mandatory in a
        future release.
  - Parses command line flags with the flag module.
  - If there are any errors, prints usage().
  - Calls main() with the remaining arguments.
  - If main() raises a UsageError, prints usage and the error message.
  '''
def call_after_init(callback) -> None:
    """Calls the given callback only once ABSL has finished initialization.

  If ABSL has already finished initialization when ``call_after_init`` is
  called then the callback is executed immediately, otherwise `callback` is
  stored to be executed after ``app.run`` has finished initializing (aka. just
  before the main function is called).

  If called after ``app.run``, this is equivalent to calling ``callback()`` in
  the caller thread. If called before ``app.run``, callbacks are run
  sequentially (in an undefined order) in the same thread as ``app.run``.

  Args:
    callback: a callable to be called once ABSL has finished initialization.
      This may be immediate if initialization has already finished. It
      takes no arguments and returns nothing.
  """
def usage(shorthelp: bool = False, writeto_stdout: bool = False, detailed_error: Incomplete | None = None, exitcode: Incomplete | None = None) -> None:
    """Writes __main__'s docstring to stderr with some help text.

  Args:
    shorthelp: bool, if True, prints only flags from the main module,
        rather than all flags.
    writeto_stdout: bool, if True, writes help message to stdout,
        rather than to stderr.
    detailed_error: str, additional detail about why usage info was presented.
    exitcode: optional integer, if set, exits with this status code after
        writing help.
  """

class ExceptionHandler:
    """Base exception handler from which other may inherit."""
    def wants(self, exc):
        """Returns whether this handler wants to handle the exception or not.

    This base class returns True for all exceptions by default. Override in
    subclass if it wants to be more selective.

    Args:
      exc: Exception, the current exception.
    """
    def handle(self, exc) -> None:
        """Do something with the current exception.

    Args:
      exc: Exception, the current exception

    This method must be overridden.
    """

def install_exception_handler(handler) -> None:
    """Installs an exception handler.

  Args:
    handler: ExceptionHandler, the exception handler to install.

  Raises:
    TypeError: Raised when the handler was not of the correct type.

  All installed exception handlers will be called if main() exits via
  an abnormal exception, i.e. not one of SystemExit, KeyboardInterrupt,
  FlagsError or UsageError.
  """
