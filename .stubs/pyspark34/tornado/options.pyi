from _typeshed import Incomplete
from tornado.escape import native_str as native_str
from tornado.log import define_logging_options as define_logging_options
from tornado.util import basestring_type as basestring_type, exec_in as exec_in
from typing import Any, Callable, Dict, Iterable, Iterator, List, Set, TextIO, Tuple

class Error(Exception):
    """Exception raised by errors in the options module."""

class OptionParser:
    """A collection of options, a dictionary with object-like access.

    Normally accessed via static functions in the `tornado.options` module,
    which reference a global instance.
    """
    def __init__(self) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __contains__(self, name: str) -> bool: ...
    def __getitem__(self, name: str) -> Any: ...
    def __setitem__(self, name: str, value: Any) -> None: ...
    def items(self) -> Iterable[Tuple[str, Any]]:
        """An iterable of (name, value) pairs.

        .. versionadded:: 3.1
        """
    def groups(self) -> Set[str]:
        """The set of option-groups created by ``define``.

        .. versionadded:: 3.1
        """
    def group_dict(self, group: str) -> Dict[str, Any]:
        """The names and values of options in a group.

        Useful for copying options into Application settings::

            from tornado.options import define, parse_command_line, options

            define('template_path', group='application')
            define('static_path', group='application')

            parse_command_line()

            application = Application(
                handlers, **options.group_dict('application'))

        .. versionadded:: 3.1
        """
    def as_dict(self) -> Dict[str, Any]:
        """The names and values of all options.

        .. versionadded:: 3.1
        """
    def define(self, name: str, default: Any = None, type: type | None = None, help: str | None = None, metavar: str | None = None, multiple: bool = False, group: str | None = None, callback: Callable[[Any], None] | None = None) -> None:
        '''Defines a new command line option.

        ``type`` can be any of `str`, `int`, `float`, `bool`,
        `~datetime.datetime`, or `~datetime.timedelta`. If no ``type``
        is given but a ``default`` is, ``type`` is the type of
        ``default``. Otherwise, ``type`` defaults to `str`.

        If ``multiple`` is True, the option value is a list of ``type``
        instead of an instance of ``type``.

        ``help`` and ``metavar`` are used to construct the
        automatically generated command line help string. The help
        message is formatted like::

           --name=METAVAR      help string

        ``group`` is used to group the defined options in logical
        groups. By default, command line options are grouped by the
        file in which they are defined.

        Command line option names must be unique globally.

        If a ``callback`` is given, it will be run with the new value whenever
        the option is changed.  This can be used to combine command-line
        and file-based options::

            define("config", type=str, help="path to config file",
                   callback=lambda path: parse_config_file(path, final=False))

        With this definition, options in the file specified by ``--config`` will
        override options set earlier on the command line, but can be overridden
        by later flags.

        '''
    def parse_command_line(self, args: List[str] | None = None, final: bool = True) -> List[str]:
        """Parses all options given on the command line (defaults to
        `sys.argv`).

        Options look like ``--option=value`` and are parsed according
        to their ``type``. For boolean options, ``--option`` is
        equivalent to ``--option=true``

        If the option has ``multiple=True``, comma-separated values
        are accepted. For multi-value integer options, the syntax
        ``x:y`` is also accepted and equivalent to ``range(x, y)``.

        Note that ``args[0]`` is ignored since it is the program name
        in `sys.argv`.

        We return a list of all arguments that are not parsed as options.

        If ``final`` is ``False``, parse callbacks will not be run.
        This is useful for applications that wish to combine configurations
        from multiple sources.

        """
    def parse_config_file(self, path: str, final: bool = True) -> None:
        """Parses and loads the config file at the given path.

        The config file contains Python code that will be executed (so
        it is **not safe** to use untrusted config files). Anything in
        the global namespace that matches a defined option will be
        used to set that option's value.

        Options may either be the specified type for the option or
        strings (in which case they will be parsed the same way as in
        `.parse_command_line`)

        Example (using the options defined in the top-level docs of
        this module)::

            port = 80
            mysql_host = 'mydb.example.com:3306'
            # Both lists and comma-separated strings are allowed for
            # multiple=True.
            memcache_hosts = ['cache1.example.com:11011',
                              'cache2.example.com:11011']
            memcache_hosts = 'cache1.example.com:11011,cache2.example.com:11011'

        If ``final`` is ``False``, parse callbacks will not be run.
        This is useful for applications that wish to combine configurations
        from multiple sources.

        .. note::

            `tornado.options` is primarily a command-line library.
            Config file support is provided for applications that wish
            to use it, but applications that prefer config files may
            wish to look at other libraries instead.

        .. versionchanged:: 4.1
           Config files are now always interpreted as utf-8 instead of
           the system default encoding.

        .. versionchanged:: 4.4
           The special variable ``__file__`` is available inside config
           files, specifying the absolute path to the config file itself.

        .. versionchanged:: 5.1
           Added the ability to set options via strings in config files.

        """
    def print_help(self, file: TextIO | None = None) -> None:
        """Prints all the command line options to stderr (or another file)."""
    def add_parse_callback(self, callback: Callable[[], None]) -> None:
        """Adds a parse callback, to be invoked when option parsing is done."""
    def run_parse_callbacks(self) -> None: ...
    def mockable(self) -> _Mockable:
        """Returns a wrapper around self that is compatible with
        `mock.patch <unittest.mock.patch>`.

        The `mock.patch <unittest.mock.patch>` function (included in
        the standard library `unittest.mock` package since Python 3.3,
        or in the third-party ``mock`` package for older versions of
        Python) is incompatible with objects like ``options`` that
        override ``__getattr__`` and ``__setattr__``.  This function
        returns an object that can be used with `mock.patch.object
        <unittest.mock.patch.object>` to modify option values::

            with mock.patch.object(options.mockable(), 'name', value):
                assert options.name == value
        """

class _Mockable:
    """`mock.patch` compatible wrapper for `OptionParser`.

    As of ``mock`` version 1.0.1, when an object uses ``__getattr__``
    hooks instead of ``__dict__``, ``patch.__exit__`` tries to delete
    the attribute it set instead of setting a new one (assuming that
    the object does not capture ``__setattr__``, so the patch
    created a new attribute in ``__dict__``).

    _Mockable's getattr and setattr pass through to the underlying
    OptionParser, and delattr undoes the effect of a previous setattr.
    """
    def __init__(self, options: OptionParser) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

class _Option:
    UNSET: Incomplete
    name: Incomplete
    type: Incomplete
    help: Incomplete
    metavar: Incomplete
    multiple: Incomplete
    file_name: Incomplete
    group_name: Incomplete
    callback: Incomplete
    default: Incomplete
    def __init__(self, name: str, default: Any = None, type: type | None = None, help: str | None = None, metavar: str | None = None, multiple: bool = False, file_name: str | None = None, group_name: str | None = None, callback: Callable[[Any], None] | None = None) -> None: ...
    def value(self) -> Any: ...
    def parse(self, value: str) -> Any: ...
    def set(self, value: Any) -> None: ...

options: Incomplete

def define(name: str, default: Any = None, type: type | None = None, help: str | None = None, metavar: str | None = None, multiple: bool = False, group: str | None = None, callback: Callable[[Any], None] | None = None) -> None:
    """Defines an option in the global namespace.

    See `OptionParser.define`.
    """
def parse_command_line(args: List[str] | None = None, final: bool = True) -> List[str]:
    """Parses global options from the command line.

    See `OptionParser.parse_command_line`.
    """
def parse_config_file(path: str, final: bool = True) -> None:
    """Parses global options from a config file.

    See `OptionParser.parse_config_file`.
    """
def print_help(file: TextIO | None = None) -> None:
    """Prints all the command line options to stderr (or another file).

    See `OptionParser.print_help`.
    """
def add_parse_callback(callback: Callable[[], None]) -> None:
    """Adds a parse callback, to be invoked when option parsing is done.

    See `OptionParser.add_parse_callback`
    """
