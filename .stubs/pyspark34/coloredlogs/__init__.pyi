import logging
from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

__version__: str
DEFAULT_LOG_LEVEL: Incomplete
DEFAULT_LOG_FORMAT: str
DEFAULT_DATE_FORMAT: str
CHROOT_FILES: Incomplete
DEFAULT_FIELD_STYLES: Incomplete
DEFAULT_LEVEL_STYLES: Incomplete
DEFAULT_FORMAT_STYLE: str
FORMAT_STYLE_PATTERNS: Incomplete

def auto_install() -> None:
    """
    Automatically call :func:`install()` when ``$COLOREDLOGS_AUTO_INSTALL`` is set.

    The `coloredlogs` package includes a `path configuration file`_ that
    automatically imports the :mod:`coloredlogs` module and calls
    :func:`auto_install()` when the environment variable
    ``$COLOREDLOGS_AUTO_INSTALL`` is set.

    This function uses :func:`~humanfriendly.coerce_boolean()` to check whether
    the value of ``$COLOREDLOGS_AUTO_INSTALL`` should be considered :data:`True`.

    .. _path configuration file: https://docs.python.org/2/library/site.html#module-site
    """
def install(level: Incomplete | None = None, **kw):
    """
    Enable colored terminal output for Python's :mod:`logging` module.

    :param level: The default logging level (an integer or a string with a
                  level name, defaults to :data:`DEFAULT_LOG_LEVEL`).
    :param logger: The logger to which the stream handler should be attached (a
                   :class:`~logging.Logger` object, defaults to the root logger).
    :param fmt: Set the logging format (a string like those accepted by
                :class:`~logging.Formatter`, defaults to
                :data:`DEFAULT_LOG_FORMAT`).
    :param datefmt: Set the date/time format (a string, defaults to
                    :data:`DEFAULT_DATE_FORMAT`).
    :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                  :data:`DEFAULT_FORMAT_STYLE`). See the documentation of the
                  :class:`python3:logging.Formatter` class in Python 3.2+. On
                  older Python versions only ``%`` is supported.
    :param milliseconds: :data:`True` to show milliseconds like :mod:`logging`
                         does by default, :data:`False` to hide milliseconds
                         (the default is :data:`False`, see `#16`_).
    :param level_styles: A dictionary with custom level styles (defaults to
                         :data:`DEFAULT_LEVEL_STYLES`).
    :param field_styles: A dictionary with custom field styles (defaults to
                         :data:`DEFAULT_FIELD_STYLES`).
    :param stream: The stream where log messages should be written to (a
                   file-like object). This defaults to :data:`None` which
                   means :class:`StandardErrorHandler` is used.
    :param isatty: :data:`True` to use a :class:`ColoredFormatter`,
                   :data:`False` to use a normal :class:`~logging.Formatter`
                   (defaults to auto-detection using
                   :func:`~humanfriendly.terminal.terminal_supports_colors()`).
    :param reconfigure: If :data:`True` (the default) multiple calls to
                        :func:`coloredlogs.install()` will each override
                        the previous configuration.
    :param use_chroot: Refer to :class:`HostNameFilter`.
    :param programname: Refer to :class:`ProgramNameFilter`.
    :param username: Refer to :class:`UserNameFilter`.
    :param syslog: If :data:`True` then :func:`.enable_system_logging()` will
                   be called without arguments (defaults to :data:`False`). The
                   `syslog` argument may also be a number or string, in this
                   case it is assumed to be a logging level which is passed on
                   to :func:`.enable_system_logging()`.

    The :func:`coloredlogs.install()` function is similar to
    :func:`logging.basicConfig()`, both functions take a lot of optional
    keyword arguments but try to do the right thing by default:

    1. If `reconfigure` is :data:`True` (it is by default) and an existing
       :class:`~logging.StreamHandler` is found that is connected to either
       :data:`~sys.stdout` or :data:`~sys.stderr` the handler will be removed.
       This means that first calling :func:`logging.basicConfig()` and then
       calling :func:`coloredlogs.install()` will replace the stream handler
       instead of adding a duplicate stream handler. If `reconfigure` is
       :data:`False` and an existing handler is found no further steps are
       taken (to avoid installing a duplicate stream handler).

    2. A :class:`~logging.StreamHandler` is created and connected to the stream
       given by the `stream` keyword argument (:data:`sys.stderr` by
       default). The stream handler's level is set to the value of the `level`
       keyword argument.

    3. A :class:`ColoredFormatter` is created if the `isatty` keyword argument
       allows it (or auto-detection allows it), otherwise a normal
       :class:`~logging.Formatter` is created. The formatter is initialized
       with the `fmt` and `datefmt` keyword arguments (or their computed
       defaults).

       The environment variable ``$NO_COLOR`` is taken as a hint by
       auto-detection that colors should not be used.

    4. :func:`HostNameFilter.install()`, :func:`ProgramNameFilter.install()`
       and :func:`UserNameFilter.install()` are called to enable the use of
       additional fields in the log format.

    5. If the logger's level is too restrictive it is relaxed (refer to `notes
       about log levels`_ for details).

    6. The formatter is added to the handler and the handler is added to the
       logger.

    .. _#16: https://github.com/xolox/python-coloredlogs/issues/16
    """
def check_style(value):
    """
    Validate a logging format style.

    :param value: The logging format style to validate (any value).
    :returns: The logging format character (a string of one character).
    :raises: :exc:`~exceptions.ValueError` when the given style isn't supported.

    On Python 3.2+ this function accepts the logging format styles ``%``, ``{``
    and ``$`` while on older versions only ``%`` is accepted (because older
    Python versions don't support alternative logging format styles).
    """
def increase_verbosity() -> None:
    """
    Increase the verbosity of the root handler by one defined level.

    Understands custom logging levels like defined by my ``verboselogs``
    module.
    """
def decrease_verbosity() -> None:
    """
    Decrease the verbosity of the root handler by one defined level.

    Understands custom logging levels like defined by my ``verboselogs``
    module.
    """
def is_verbose():
    """
    Check whether the log level of the root handler is set to a verbose level.

    :returns: ``True`` if the root handler is verbose, ``False`` if not.
    """
def get_level():
    """
    Get the logging level of the root handler.

    :returns: The logging level of the root handler (an integer) or
              :data:`DEFAULT_LOG_LEVEL` (if no root handler exists).
    """
def set_level(level) -> None:
    """
    Set the logging level of the root handler.

    :param level: The logging level to filter on (an integer or string).

    If no root handler exists yet this automatically calls :func:`install()`.
    """
def adjust_level(logger, level) -> None:
    '''
    Increase a logger\'s verbosity up to the requested level.

    :param logger: The logger to change (a :class:`~logging.Logger` object).
    :param level: The log level to enable (a string or number).

    This function is used by functions like :func:`install()`,
    :func:`increase_verbosity()` and :func:`.enable_system_logging()` to adjust
    a logger\'s level so that log messages up to the requested log level are
    propagated to the configured output handler(s).

    It uses :func:`logging.Logger.getEffectiveLevel()` to check whether
    `logger` propagates or swallows log messages of the requested `level` and
    sets the logger\'s level to the requested level if it would otherwise
    swallow log messages.

    Effectively this function will "widen the scope of logging" when asked to
    do so but it will never "narrow the scope of logging". This is because I am
    convinced that filtering of log messages should (primarily) be decided by
    handlers.
    '''
def find_defined_levels():
    """
    Find the defined logging levels.

    :returns: A dictionary with level names as keys and integers as values.

    Here's what the result looks like by default (when
    no custom levels or level names have been defined):

    >>> find_defined_levels()
    {'NOTSET': 0,
     'DEBUG': 10,
     'INFO': 20,
     'WARN': 30,
     'WARNING': 30,
     'ERROR': 40,
     'FATAL': 50,
     'CRITICAL': 50}
    """
def level_to_number(value):
    """
    Coerce a logging level name to a number.

    :param value: A logging level (integer or string).
    :returns: The number of the log level (an integer).

    This function translates log level names into their numeric values..
    """
def find_level_aliases():
    """
    Find log level names which are aliases of each other.

    :returns: A dictionary that maps aliases to their canonical name.

    .. note:: Canonical names are chosen to be the alias with the longest
              string length so that e.g. ``WARN`` is an alias for ``WARNING``
              instead of the other way around.

    Here's what the result looks like by default (when
    no custom levels or level names have been defined):

    >>> from coloredlogs import find_level_aliases
    >>> find_level_aliases()
    {'WARN': 'WARNING', 'FATAL': 'CRITICAL'}
    """
def parse_encoded_styles(text, normalize_key: Incomplete | None = None):
    """
    Parse text styles encoded in a string into a nested data structure.

    :param text: The encoded styles (a string).
    :returns: A dictionary in the structure of the :data:`DEFAULT_FIELD_STYLES`
              and :data:`DEFAULT_LEVEL_STYLES` dictionaries.

    Here's an example of how this function works:

    >>> from coloredlogs import parse_encoded_styles
    >>> from pprint import pprint
    >>> encoded_styles = 'debug=green;warning=yellow;error=red;critical=red,bold'
    >>> pprint(parse_encoded_styles(encoded_styles))
    {'debug': {'color': 'green'},
     'warning': {'color': 'yellow'},
     'error': {'color': 'red'},
     'critical': {'bold': True, 'color': 'red'}}
    """
def find_hostname(use_chroot: bool = True):
    """
    Find the host name to include in log messages.

    :param use_chroot: Use the name of the chroot when inside a chroot?
                       (boolean, defaults to :data:`True`)
    :returns: A suitable host name (a string).

    Looks for :data:`CHROOT_FILES` that have a nonempty first line (taken to be
    the chroot name). If none are found then :func:`socket.gethostname()` is
    used as a fall back.
    """
def find_program_name():
    """
    Select a suitable program name to embed in log messages.

    :returns: One of the following strings (in decreasing order of preference):

              1. The base name of the currently running Python program or
                 script (based on the value at index zero of :data:`sys.argv`).
              2. The base name of the Python executable (based on
                 :data:`sys.executable`).
              3. The string 'python'.
    """
def find_username():
    """
    Find the username to include in log messages.

    :returns: A suitable username (a string).

    On UNIX systems this uses the :mod:`pwd` module which means ``root`` will
    be reported when :man:`sudo` is used (as it should). If this fails (for
    example on Windows) then :func:`getpass.getuser()` is used as a fall back.
    """
def replace_handler(logger, match_handler, reconfigure):
    """
    Prepare to replace a handler.

    :param logger: Refer to :func:`find_handler()`.
    :param match_handler: Refer to :func:`find_handler()`.
    :param reconfigure: :data:`True` if an existing handler should be replaced,
                        :data:`False` otherwise.
    :returns: A tuple of two values:

              1. The matched :class:`~logging.Handler` object or :data:`None`
                 if no handler was matched.
              2. The :class:`~logging.Logger` to which the matched handler was
                 attached or the logger given to :func:`replace_handler()`.
    """
def find_handler(logger, match_handler):
    """
    Find a (specific type of) handler in the propagation tree of a logger.

    :param logger: The logger to check (a :class:`~logging.Logger` object).
    :param match_handler: A callable that receives a :class:`~logging.Handler`
                          object and returns :data:`True` to match a handler or
                          :data:`False` to skip that handler and continue
                          searching for a match.
    :returns: A tuple of two values:

              1. The matched :class:`~logging.Handler` object or :data:`None`
                 if no handler was matched.
              2. The :class:`~logging.Logger` object to which the handler is
                 attached or :data:`None` if no handler was matched.

    This function finds a logging handler (of the given type) attached to a
    logger or one of its parents (see :func:`walk_propagation_tree()`). It uses
    the undocumented :class:`~logging.Logger.handlers` attribute to find
    handlers attached to a logger, however it won't raise an exception if the
    attribute isn't available. The advantages of this approach are:

    - This works regardless of whether :mod:`coloredlogs` attached the handler
      or other Python code attached the handler.

    - This will correctly recognize the situation where the given logger has no
      handlers but :attr:`~logging.Logger.propagate` is enabled and the logger
      has a parent logger that does have a handler attached.
    """
def match_stream_handler(handler, streams=[]):
    """
    Identify stream handlers writing to the given streams(s).

    :param handler: The :class:`~logging.Handler` class to check.
    :param streams: A sequence of streams to match (defaults to matching
                    :data:`~sys.stdout` and :data:`~sys.stderr`).
    :returns: :data:`True` if the handler is a :class:`~logging.StreamHandler`
              logging to the given stream(s), :data:`False` otherwise.

    This function can be used as a callback for :func:`find_handler()`.
    """
def walk_propagation_tree(logger) -> Generator[Incomplete, None, None]:
    """
    Walk through the propagation hierarchy of the given logger.

    :param logger: The logger whose hierarchy to walk (a
                   :class:`~logging.Logger` object).
    :returns: A generator of :class:`~logging.Logger` objects.

    .. note:: This uses the undocumented :class:`logging.Logger.parent`
              attribute to find higher level loggers, however it won't
              raise an exception if the attribute isn't available.
    """

class BasicFormatter(logging.Formatter):
    """
    Log :class:`~logging.Formatter` that supports ``%f`` for millisecond formatting.

    This class extends :class:`~logging.Formatter` to enable the use of ``%f``
    for millisecond formatting in date/time strings, to allow for the type of
    flexibility requested in issue `#45`_.

    .. _#45: https://github.com/xolox/python-coloredlogs/issues/45
    """
    def formatTime(self, record, datefmt: Incomplete | None = None):
        """
        Format the date/time of a log record.

        :param record: A :class:`~logging.LogRecord` object.
        :param datefmt: A date/time format string (defaults to :data:`DEFAULT_DATE_FORMAT`).
        :returns: The formatted date/time (a string).

        This method overrides :func:`~logging.Formatter.formatTime()` to set
        `datefmt` to :data:`DEFAULT_DATE_FORMAT` when the caller hasn't
        specified a date format.

        When `datefmt` contains the token ``%f`` it will be replaced by the
        value of ``%(msecs)03d`` (refer to issue `#45`_ for use cases).
        """

class ColoredFormatter(BasicFormatter):
    """
    Log :class:`~logging.Formatter` that uses `ANSI escape sequences`_ to create colored logs.

    :class:`ColoredFormatter` inherits from :class:`BasicFormatter` to enable
    the use of ``%f`` for millisecond formatting in date/time strings.

    .. note:: If you want to use :class:`ColoredFormatter` on Windows then you
              need to call :func:`~humanfriendly.terminal.enable_ansi_support()`.
              This is done for you when you call :func:`coloredlogs.install()`.
    """
    nn: Incomplete
    level_styles: Incomplete
    field_styles: Incomplete
    def __init__(self, fmt: Incomplete | None = None, datefmt: Incomplete | None = None, style=..., level_styles: Incomplete | None = None, field_styles: Incomplete | None = None) -> None:
        """
        Initialize a :class:`ColoredFormatter` object.

        :param fmt: A log format string (defaults to :data:`DEFAULT_LOG_FORMAT`).
        :param datefmt: A date/time format string (defaults to :data:`None`,
                        but see the documentation of
                        :func:`BasicFormatter.formatTime()`).
        :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                      :data:`DEFAULT_FORMAT_STYLE`)
        :param level_styles: A dictionary with custom level styles
                             (defaults to :data:`DEFAULT_LEVEL_STYLES`).
        :param field_styles: A dictionary with custom field styles
                             (defaults to :data:`DEFAULT_FIELD_STYLES`).
        :raises: Refer to :func:`check_style()`.

        This initializer uses :func:`colorize_format()` to inject ANSI escape
        sequences in the log format string before it is passed to the
        initializer of the base class.
        """
    def colorize_format(self, fmt, style=...):
        """
        Rewrite a logging format string to inject ANSI escape sequences.

        :param fmt: The log format string.
        :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                      :data:`DEFAULT_FORMAT_STYLE`).
        :returns: The logging format string with ANSI escape sequences.

        This method takes a logging format string like the ones you give to
        :class:`logging.Formatter` and processes it as follows:

        1. First the logging format string is separated into formatting
           directives versus surrounding text (according to the given `style`).

        2. Then formatting directives and surrounding text are grouped
           based on whitespace delimiters (in the surrounding text).

        3. For each group styling is selected as follows:

           1. If the group contains a single formatting directive that has
              a style defined then the whole group is styled accordingly.

           2. If the group contains multiple formatting directives that
              have styles defined then each formatting directive is styled
              individually and surrounding text isn't styled.

        As an example consider the default log format (:data:`DEFAULT_LOG_FORMAT`)::

         %(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s

        The default field styles (:data:`DEFAULT_FIELD_STYLES`) define a style for the
        `name` field but not for the `process` field, however because both fields
        are part of the same whitespace delimited token they'll be highlighted
        together in the style defined for the `name` field.
        """
    def format(self, record):
        """
        Apply level-specific styling to log records.

        :param record: A :class:`~logging.LogRecord` object.
        :returns: The result of :func:`logging.Formatter.format()`.

        This method injects ANSI escape sequences that are specific to the
        level of each log record (because such logic cannot be expressed in the
        syntax of a log format string). It works by making a copy of the log
        record, changing the `msg` field inside the copy and passing the copy
        into the :func:`~logging.Formatter.format()` method of the base
        class.
        """

class Empty:
    """An empty class used to copy :class:`~logging.LogRecord` objects without reinitializing them."""

class HostNameFilter(logging.Filter):
    '''
    Log filter to enable the ``%(hostname)s`` format.

    Python\'s :mod:`logging` module doesn\'t expose the system\'s host name while
    I consider this to be a valuable addition. Fortunately it\'s very easy to
    expose additional fields in format strings: :func:`filter()` simply sets
    the ``hostname`` attribute of each :class:`~logging.LogRecord` object it
    receives and this is enough to enable the use of the ``%(hostname)s``
    expression in format strings.

    You can install this log filter as follows::

     >>> import coloredlogs, logging
     >>> handler = logging.StreamHandler()
     >>> handler.addFilter(coloredlogs.HostNameFilter())
     >>> handler.setFormatter(logging.Formatter(\'[%(hostname)s] %(message)s\'))
     >>> logger = logging.getLogger()
     >>> logger.addHandler(handler)
     >>> logger.setLevel(logging.INFO)
     >>> logger.info("Does it work?")
     [peter-macbook] Does it work?

    Of course :func:`coloredlogs.install()` does all of this for you :-).
    '''
    @classmethod
    def install(cls, handler, fmt: Incomplete | None = None, use_chroot: bool = True, style=...) -> None:
        """
        Install the :class:`HostNameFilter` on a log handler (only if needed).

        :param fmt: The log format string to check for ``%(hostname)``.
        :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                      :data:`DEFAULT_FORMAT_STYLE`).
        :param handler: The logging handler on which to install the filter.
        :param use_chroot: Refer to :func:`find_hostname()`.

        If `fmt` is given the filter will only be installed if `fmt` uses the
        ``hostname`` field. If `fmt` is not given the filter is installed
        unconditionally.
        """
    hostname: Incomplete
    def __init__(self, use_chroot: bool = True) -> None:
        """
        Initialize a :class:`HostNameFilter` object.

        :param use_chroot: Refer to :func:`find_hostname()`.
        """
    def filter(self, record):
        """Set each :class:`~logging.LogRecord`'s `hostname` field."""

class ProgramNameFilter(logging.Filter):
    """
    Log filter to enable the ``%(programname)s`` format.

    Python's :mod:`logging` module doesn't expose the name of the currently
    running program while I consider this to be a useful addition. Fortunately
    it's very easy to expose additional fields in format strings:
    :func:`filter()` simply sets the ``programname`` attribute of each
    :class:`~logging.LogRecord` object it receives and this is enough to enable
    the use of the ``%(programname)s`` expression in format strings.

    Refer to :class:`HostNameFilter` for an example of how to manually install
    these log filters.
    """
    @classmethod
    def install(cls, handler, fmt, programname: Incomplete | None = None, style=...) -> None:
        """
        Install the :class:`ProgramNameFilter` (only if needed).

        :param fmt: The log format string to check for ``%(programname)``.
        :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                      :data:`DEFAULT_FORMAT_STYLE`).
        :param handler: The logging handler on which to install the filter.
        :param programname: Refer to :func:`__init__()`.

        If `fmt` is given the filter will only be installed if `fmt` uses the
        ``programname`` field. If `fmt` is not given the filter is installed
        unconditionally.
        """
    programname: Incomplete
    def __init__(self, programname: Incomplete | None = None) -> None:
        """
        Initialize a :class:`ProgramNameFilter` object.

        :param programname: The program name to use (defaults to the result of
                            :func:`find_program_name()`).
        """
    def filter(self, record):
        """Set each :class:`~logging.LogRecord`'s `programname` field."""

class UserNameFilter(logging.Filter):
    """
    Log filter to enable the ``%(username)s`` format.

    Python's :mod:`logging` module doesn't expose the username of the currently
    logged in user as requested in `#76`_. Given that :class:`HostNameFilter`
    and :class:`ProgramNameFilter` are already provided by `coloredlogs` it
    made sense to provide :class:`UserNameFilter` as well.

    Refer to :class:`HostNameFilter` for an example of how to manually install
    these log filters.

    .. _#76: https://github.com/xolox/python-coloredlogs/issues/76
    """
    @classmethod
    def install(cls, handler, fmt, username: Incomplete | None = None, style=...) -> None:
        """
        Install the :class:`UserNameFilter` (only if needed).

        :param fmt: The log format string to check for ``%(username)``.
        :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                      :data:`DEFAULT_FORMAT_STYLE`).
        :param handler: The logging handler on which to install the filter.
        :param username: Refer to :func:`__init__()`.

        If `fmt` is given the filter will only be installed if `fmt` uses the
        ``username`` field. If `fmt` is not given the filter is installed
        unconditionally.
        """
    username: Incomplete
    def __init__(self, username: Incomplete | None = None) -> None:
        """
        Initialize a :class:`UserNameFilter` object.

        :param username: The username to use (defaults to the
                         result of :func:`find_username()`).
        """
    def filter(self, record):
        """Set each :class:`~logging.LogRecord`'s `username` field."""

class StandardErrorHandler(logging.StreamHandler):
    """
    A :class:`~logging.StreamHandler` that gets the value of :data:`sys.stderr` for each log message.

    The :class:`StandardErrorHandler` class enables `monkey patching of
    sys.stderr <https://github.com/xolox/python-coloredlogs/pull/31>`_. It's
    basically the same as the ``logging._StderrHandler`` class present in
    Python 3 but it will be available regardless of Python version. This
    handler is used by :func:`coloredlogs.install()` to improve compatibility
    with the Python standard library.
    """
    def __init__(self, level=...) -> None:
        """Initialize a :class:`StandardErrorHandler` object."""
    @property
    def stream(self):
        """Get the value of :data:`sys.stderr` (a file-like object)."""

class FormatStringParser:
    """
    Shallow logging format string parser.

    This class enables introspection and manipulation of logging format strings
    in the three styles supported by the :mod:`logging` module starting from
    Python 3.2 (``%``, ``{`` and ``$``).
    """
    style: Incomplete
    capturing_pattern: Incomplete
    raw_pattern: Incomplete
    tokenize_pattern: Incomplete
    name_pattern: Incomplete
    def __init__(self, style=...) -> None:
        """
        Initialize a :class:`FormatStringParser` object.

        :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                      :data:`DEFAULT_FORMAT_STYLE`).
        :raises: Refer to :func:`check_style()`.
        """
    def contains_field(self, format_string, field_name):
        """
        Get the field names referenced by a format string.

        :param format_string: The logging format string.
        :returns: A list of strings with field names.
        """
    def get_field_names(self, format_string):
        """
        Get the field names referenced by a format string.

        :param format_string: The logging format string.
        :returns: A list of strings with field names.
        """
    def get_grouped_pairs(self, format_string):
        """
        Group the results of :func:`get_pairs()` separated by whitespace.

        :param format_string: The logging format string.
        :returns: A list of lists of :class:`FormatStringToken` objects.
        """
    def get_pairs(self, format_string) -> Generator[Incomplete, None, None]:
        """
        Tokenize a logging format string and extract field names from tokens.

        :param format_string: The logging format string.
        :returns: A generator of :class:`FormatStringToken` objects.
        """
    def get_pattern(self, field_name):
        """
        Get a regular expression to match a formatting directive that references the given field name.

        :param field_name: The name of the field to match (a string).
        :returns: A compiled regular expression object.
        """
    def get_tokens(self, format_string):
        """
        Tokenize a logging format string.

        :param format_string: The logging format string.
        :returns: A list of strings with formatting directives separated from surrounding text.
        """

class FormatStringToken(NamedTuple('FormatStringToken', [('text', Incomplete), ('name', Incomplete)])):
    """
    A named tuple for the results of :func:`FormatStringParser.get_pairs()`.

    .. attribute:: name

       The field name referenced in `text` (a string). If `text` doesn't
       contain a formatting directive this will be :data:`None`.

    .. attribute:: text

       The text extracted from the logging format string (a string).
    """

class NameNormalizer:
    """Responsible for normalizing field and level names."""
    aliases: Incomplete
    def __init__(self) -> None:
        """Initialize a :class:`NameNormalizer` object."""
    def normalize_name(self, name):
        """
        Normalize a field or level name.

        :param name: The field or level name (a string).
        :returns: The normalized name (a string).

        Transforms all strings to lowercase and resolves level name aliases
        (refer to :func:`find_level_aliases()`) to their canonical name:

        >>> from coloredlogs import NameNormalizer
        >>> from humanfriendly import format_table
        >>> nn = NameNormalizer()
        >>> sample_names = ['DEBUG', 'INFO', 'WARN', 'WARNING', 'ERROR', 'FATAL', 'CRITICAL']
        >>> print(format_table([(n, nn.normalize_name(n)) for n in sample_names]))
        -----------------------
        | DEBUG    | debug    |
        | INFO     | info     |
        | WARN     | warning  |
        | WARNING  | warning  |
        | ERROR    | error    |
        | FATAL    | critical |
        | CRITICAL | critical |
        -----------------------
        """
    def normalize_keys(self, value):
        """
        Normalize the keys of a dictionary using :func:`normalize_name()`.

        :param value: The dictionary to normalize.
        :returns: A dictionary with normalized keys.
        """
    def get(self, normalized_dict, name):
        """
        Get a value from a dictionary after normalizing the key.

        :param normalized_dict: A dictionary produced by :func:`normalize_keys()`.
        :param name: A key to normalize and get from the dictionary.
        :returns: The value of the normalized key (if any).
        """
