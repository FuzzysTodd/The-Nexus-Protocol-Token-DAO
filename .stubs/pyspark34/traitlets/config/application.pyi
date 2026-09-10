import logging
import typing as t
from ..utils import cast_unicode as cast_unicode
from ..utils.importstring import import_item as import_item
from _typeshed import Incomplete
from traitlets.config.configurable import Configurable as Configurable, SingletonConfigurable as SingletonConfigurable
from traitlets.config.loader import ArgumentError as ArgumentError, Config as Config, ConfigFileNotFound as ConfigFileNotFound, JSONFileConfigLoader as JSONFileConfigLoader, KVArgParseConfigLoader as KVArgParseConfigLoader, PyFileConfigLoader as PyFileConfigLoader
from traitlets.traitlets import Bool as Bool, Dict as Dict, Enum as Enum, Instance as Instance, List as List, TraitError as TraitError, Unicode as Unicode, default as default, observe as observe, observe_compat as observe_compat
from traitlets.utils.bunch import Bunch as Bunch
from traitlets.utils.nested_update import nested_update as nested_update
from traitlets.utils.text import indent as indent, wrap_paragraphs as wrap_paragraphs

option_description: Incomplete
keyvalue_description: Incomplete
subcommand_description: str
TRAITLETS_APPLICATION_RAISE_CONFIG_FILE_ERROR: bool
IS_PYTHONW: Incomplete
T = t.TypeVar('T', bound=t.Callable[..., t.Any])
AnyLogger: Incomplete
StrDict: Incomplete
ArgvType: Incomplete
ClassesType: Incomplete

def catch_config_error(method: T) -> T:
    """Method decorator for catching invalid config (Trait/ArgumentErrors) during init.

    On a TraitError (generally caused by bad config), this will print the trait's
    message, and exit the app.

    For use on init methods, to prevent invoking excepthook on invalid input.
    """

class ApplicationError(Exception): ...

class LevelFormatter(logging.Formatter):
    """Formatter with additional `highlevel` record

    This field is empty if log level is less than highlevel_limit,
    otherwise it is formatted with self.highlevel_format.

    Useful for adding 'WARNING' to warning messages,
    without adding 'INFO' to info, etc.
    """
    highlevel_limit: Incomplete
    highlevel_format: str
    def format(self, record: logging.LogRecord) -> str: ...

class Application(SingletonConfigurable):
    """A singleton application with full configuration support."""
    name: str | Unicode[str, str | bytes]
    description: str | Unicode[str, str | bytes]
    option_description: str | Unicode[str, str | bytes]
    keyvalue_description: str | Unicode[str, str | bytes]
    subcommand_description: str | Unicode[str, str | bytes]
    python_config_loader_class = PyFileConfigLoader
    json_config_loader_class = JSONFileConfigLoader
    examples: str | Unicode[str, str | bytes]
    classes: ClassesType
    version: str | Unicode[str, str | bytes]
    argv: Incomplete
    raise_config_file_errors: Incomplete
    log_level: Incomplete
    log_datefmt: Incomplete
    log_format: Incomplete
    def get_default_logging_config(self) -> StrDict:
        """Return the base logging configuration.

        The default is to log to stderr using a StreamHandler, if no default
        handler already exists.

        The log handler level starts at logging.WARN, but this can be adjusted
        by setting the ``log_level`` attribute.

        The ``logging_config`` trait is merged into this allowing for finer
        control of logging.

        """
    logging_config: Incomplete
    aliases: StrDict
    flags: StrDict
    subcommands: dict[str, t.Any] | Dict
    subapp: Incomplete
    extra_args: Incomplete
    cli_config: Incomplete
    show_config: Incomplete
    show_config_json: Incomplete
    def __init__(self, **kwargs: t.Any) -> None: ...
    def initialize(self, argv: ArgvType = None) -> None:
        """Do the basic steps to configure me.

        Override in subclasses.
        """
    def start(self) -> None:
        """Start the app mainloop.

        Override in subclasses.
        """
    def start_show_config(self) -> None:
        """start function used when show_config is True"""
    def print_alias_help(self) -> None:
        """Print the alias parts of the help."""
    def emit_alias_help(self) -> t.Generator[str, None, None]:
        """Yield the lines for alias part of the help."""
    def print_flag_help(self) -> None:
        """Print the flag part of the help."""
    def emit_flag_help(self) -> t.Generator[str, None, None]:
        """Yield the lines for the flag part of the help."""
    def print_options(self) -> None:
        """Print the options part of the help."""
    def emit_options_help(self) -> t.Generator[str, None, None]:
        """Yield the lines for the options part of the help."""
    def print_subcommands(self) -> None:
        """Print the subcommand part of the help."""
    def emit_subcommands_help(self) -> t.Generator[str, None, None]:
        """Yield the lines for the subcommand part of the help."""
    def emit_help_epilogue(self, classes: bool) -> t.Generator[str, None, None]:
        """Yield the very bottom lines of the help message.

        If classes=False (the default), print `--help-all` msg.
        """
    def print_help(self, classes: bool = False) -> None:
        """Print the help for each Configurable class in self.classes.

        If classes=False (the default), only flags and aliases are printed.
        """
    def emit_help(self, classes: bool = False) -> t.Generator[str, None, None]:
        """Yield the help-lines for each Configurable class in self.classes.

        If classes=False (the default), only flags and aliases are printed.
        """
    def document_config_options(self) -> str:
        """Generate rST format documentation for the config options this application

        Returns a multiline string.
        """
    def print_description(self) -> None:
        """Print the application description."""
    def emit_description(self) -> t.Generator[str, None, None]:
        """Yield lines with the application description."""
    def print_examples(self) -> None:
        """Print usage and examples (see `emit_examples()`)."""
    def emit_examples(self) -> t.Generator[str, None, None]:
        """Yield lines with the usage and examples.

        This usage string goes at the end of the command line help string
        and should contain examples of the application's usage.
        """
    def print_version(self) -> None:
        """Print the version string."""
    def initialize_subcommand(self, subc: str, argv: ArgvType = None) -> None:
        """Initialize a subcommand with argv."""
    def flatten_flags(self) -> tuple[dict[str, t.Any], dict[str, t.Any]]:
        """Flatten flags and aliases for loaders, so cl-args override as expected.

        This prevents issues such as an alias pointing to InteractiveShell,
        but a config file setting the same trait in TerminalInteraciveShell
        getting inappropriate priority over the command-line arg.
        Also, loaders expect ``(key: longname)`` and not ``key: (longname, help)`` items.

        Only aliases with exactly one descendent in the class list
        will be promoted.

        """
    def parse_command_line(self, argv: ArgvType = None) -> None:
        """Parse the command line arguments."""
    @property
    def loaded_config_files(self) -> list[str]:
        """Currently loaded configuration files"""
    def load_config_file(self, filename: str, path: str | t.Sequence[str | None] | None = None) -> None:
        """Load config files by filename and path."""
    def generate_config_file(self, classes: ClassesType | None = None) -> str:
        """generate default config file from Configurables"""
    def close_handlers(self) -> None: ...
    def exit(self, exit_status: int | str | None = 0) -> None: ...
    def __del__(self) -> None: ...
    @classmethod
    def launch_instance(cls, argv: ArgvType = None, **kwargs: t.Any) -> None:
        """Launch a global instance of this Application

        If a global instance already exists, this reinitializes and starts it
        """

default_aliases: Incomplete
default_flags: Incomplete

def boolean_flag(name: str, configurable: str, set_help: str = '', unset_help: str = '') -> StrDict:
    """Helper for building basic --trait, --no-trait flags.

    Parameters
    ----------
    name : str
        The name of the flag.
    configurable : str
        The 'Class.trait' string of the trait to be set/unset with the flag
    set_help : unicode
        help string for --name flag
    unset_help : unicode
        help string for --no-name flag

    Returns
    -------
    cfg : dict
        A dict with two keys: 'name', and 'no-name', for setting and unsetting
        the trait, respectively.
    """
def get_config() -> Config:
    """Get the config object for the global Application instance, if there is one

    otherwise return an empty config object
    """
