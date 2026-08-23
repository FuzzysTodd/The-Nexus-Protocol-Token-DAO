import argparse
import typing as t
from ..utils import cast_unicode as cast_unicode, filefind as filefind, warnings as warnings
from _typeshed import Incomplete
from traitlets.traitlets import Any as Any, Container as Container, Dict as Dict, HasTraits as HasTraits, List as List, Undefined as Undefined

class ConfigError(Exception): ...
class ConfigLoaderError(ConfigError): ...
class ConfigFileNotFound(ConfigError): ...
class ArgumentError(ConfigLoaderError): ...
class _Sentinel: ...

class ArgumentParser(argparse.ArgumentParser):
    """Simple argparse subclass that prints help to stdout by default."""
    def print_help(self, file: Incomplete | None = None): ...

def execfile(fname, glob) -> None: ...

class LazyConfigValue(HasTraits):
    """Proxy object for exposing methods on configurable containers

    These methods allow appending/extending/updating
    to add to non-empty defaults instead of clobbering them.

    Exposes:

    - append, extend, insert on lists
    - update on dicts
    - update, add on sets
    """
    def append(self, obj) -> None:
        """Append an item to a List"""
    def extend(self, other) -> None:
        """Extend a list"""
    def prepend(self, other) -> None:
        """like list.extend, but for the front"""
    def merge_into(self, other):
        """
        Merge with another earlier LazyConfigValue or an earlier container.
        This is useful when having global system-wide configuration files.

        Self is expected to have higher precedence.

        Parameters
        ----------
        other : LazyConfigValue or container

        Returns
        -------
        LazyConfigValue
            if ``other`` is also lazy, a reified container otherwise.
        """
    def insert(self, index, other) -> None: ...
    def update(self, other) -> None:
        """Update either a set or dict"""
    def add(self, obj) -> None:
        """Add an item to a set"""
    def get_value(self, initial):
        """construct the value from the initial one

        after applying any insert / extend / update changes
        """
    def to_dict(self):
        """return JSONable dict form of my data

        Currently update as dict or set, extend, prepend as lists, and inserts as list of tuples.
        """

class Config(dict):
    '''An attribute-based dict that can do smart merges.

    Accessing a field on a config object for the first time populates the key
    with either a nested Config object for keys starting with capitals
    or :class:`.LazyConfigValue` for lowercase keys,
    allowing quick assignments such as::

        c = Config()
        c.Class.int_trait = 5
        c.Class.list_trait.append("x")

    '''
    def __init__(self, *args: t.Any, **kwds: t.Any) -> None: ...
    def merge(self, other) -> None:
        """merge another config object into this one"""
    def collisions(self, other: Config) -> dict[str, t.Any]:
        '''Check for collisions between two config objects.

        Returns a dict of the form {"Class": {"trait": "collision message"}}`,
        indicating which values have been ignored.

        An empty dict indicates no collisions.
        '''
    def __contains__(self, key: t.Any) -> bool: ...
    has_key = __contains__
    def copy(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key: str, value: t.Any) -> None: ...
    def __getattr__(self, key): ...
    def __setattr__(self, key: str, value: t.Any) -> None: ...
    def __delattr__(self, key: str) -> None: ...

class DeferredConfig:
    """Class for deferred-evaluation of config from CLI"""
    def get_value(self, trait) -> None: ...

class DeferredConfigString(str, DeferredConfig):
    """Config value for loading config from a string

    Interpretation is deferred until it is loaded into the trait.

    Subclass of str for backward compatibility.

    This class is only used for values that are not listed
    in the configurable classes.

    When config is loaded, `trait.from_string` will be used.

    If an error is raised in `.from_string`,
    the original string is returned.

    .. versionadded:: 5.0
    """
    def get_value(self, trait):
        """Get the value stored in this string"""

class DeferredConfigList(list, DeferredConfig):
    """Config value for loading config from a list of strings

    Interpretation is deferred until it is loaded into the trait.

    This class is only used for values that are not listed
    in the configurable classes.

    When config is loaded, `trait.from_string_list` will be used.

    If an error is raised in `.from_string_list`,
    the original string list is returned.

    .. versionadded:: 5.0
    """
    def get_value(self, trait):
        """Get the value stored in this string"""

class ConfigLoader:
    """A object for loading configurations from just about anywhere.

    The resulting configuration is packaged as a :class:`Config`.

    Notes
    -----
    A :class:`ConfigLoader` does one thing: load a config from a source
    (file, command line arguments) and returns the data as a :class:`Config` object.
    There are lots of things that :class:`ConfigLoader` does not do.  It does
    not implement complex logic for finding config files.  It does not handle
    default values or merge multiple configs.  These things need to be
    handled elsewhere.
    """
    log: Incomplete
    def __init__(self, log: t.Any = None) -> None:
        """A base class for config loaders.

        log : instance of :class:`logging.Logger` to use.
              By default logger of :meth:`traitlets.config.application.Application.instance()`
              will be used

        Examples
        --------
        >>> cl = ConfigLoader()
        >>> config = cl.load_config()
        >>> config
        {}
        """
    config: Incomplete
    def clear(self) -> None: ...
    def load_config(self):
        """Load a config from somewhere, return a :class:`Config` instance.

        Usually, this will cause self.config to be set and then returned.
        However, in most cases, :meth:`ConfigLoader.clear` should be called
        to erase any previous state.
        """

class FileConfigLoader(ConfigLoader):
    """A base class for file based configurations.

    As we add more file based config loaders, the common logic should go
    here.
    """
    filename: Incomplete
    path: Incomplete
    full_filename: str
    def __init__(self, filename: str, path: str | None = None, **kw: t.Any) -> None:
        """Build a config loader for a filename and path.

        Parameters
        ----------
        filename : str
            The file name of the config file.
        path : str, list, tuple
            The path to search for the config file on, or a sequence of
            paths to try in order.
        """

class JSONFileConfigLoader(FileConfigLoader):
    """A JSON file loader for config

    Can also act as a context manager that rewrite the configuration file to disk on exit.

    Example::

        with JSONFileConfigLoader('myapp.json','/home/jupyter/configurations/') as c:
            c.MyNewConfigurable.new_value = 'Updated'

    """
    config: Incomplete
    def load_config(self):
        """Load the config from a file and return it as a Config object."""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None:
        """
        Exit the context manager but do not handle any errors.

        In case of any error, we do not want to write the potentially broken
        configuration to disk.
        """

class PyFileConfigLoader(FileConfigLoader):
    """A config loader for pure python files.

    This is responsible for locating a Python config file by filename and
    path, then executing it to construct a Config object.
    """
    def load_config(self):
        """Load the config from a file and return it as a Config object."""
    def load_subconfig(self, fname, path: Incomplete | None = None) -> None:
        """Injected into config file namespace as load_subconfig"""

class CommandLineConfigLoader(ConfigLoader):
    """A config loader for command line arguments.

    As we add more command line based loaders, the common logic should go
    here.
    """

class_trait_opt_pattern: Incomplete

class _KVAction(argparse.Action):
    """Custom argparse action for handling --Class.trait=x

    Always
    """
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None: ...

class _DefaultOptionDict(dict):
    """Like the default options dict

    but acts as if all --Class.trait options are predefined
    """
    def __contains__(self, key: t.Any) -> bool: ...
    def __getitem__(self, key): ...
    def get(self, key, default: Incomplete | None = None): ...

class _KVArgParser(argparse.ArgumentParser):
    """subclass of ArgumentParser where any --Class.trait option is implicitly defined"""
    def parse_known_args(self, args: Incomplete | None = None, namespace: Incomplete | None = None): ...

SubcommandsDict: Incomplete

class ArgParseConfigLoader(CommandLineConfigLoader):
    """A loader that uses the argparse module to load from the command line."""
    parser_class = ArgumentParser
    argv: Incomplete
    aliases: Incomplete
    flags: Incomplete
    classes: Incomplete
    subcommands: Incomplete
    parser_args: Incomplete
    version: Incomplete
    parser_kw: Incomplete
    def __init__(self, argv: list[str] | None = None, aliases: dict[str, str] | None = None, flags: dict[str, str] | None = None, log: t.Any = None, classes: list[type[t.Any]] | None = None, subcommands: SubcommandsDict | None = None, *parser_args: t.Any, **parser_kw: t.Any) -> None:
        '''Create a config loader for use with argparse.

        Parameters
        ----------
        classes : optional, list
            The classes to scan for *container* config-traits and decide
            for their "multiplicity" when adding them as *argparse* arguments.
        argv : optional, list
            If given, used to read command-line arguments from, otherwise
            sys.argv[1:] is used.
        *parser_args : tuple
            A tuple of positional arguments that will be passed to the
            constructor of :class:`argparse.ArgumentParser`.
        **parser_kw : dict
            A tuple of keyword arguments that will be passed to the
            constructor of :class:`argparse.ArgumentParser`.
        aliases : dict of str to str
            Dict of aliases to full traitlets names for CLI parsing
        flags : dict of str to str
            Dict of flags to full traitlets names for CLI parsing
        log
            Passed to `ConfigLoader`

        Returns
        -------
        config : Config
            The resulting Config object.
        '''
    def load_config(self, argv: Incomplete | None = None, aliases: Incomplete | None = None, flags=..., classes: Incomplete | None = None):
        """Parse command line arguments and return as a Config object.

        Parameters
        ----------
        argv : optional, list
            If given, a list with the structure of sys.argv[1:] to parse
            arguments from. If not given, the instance's self.argv attribute
            (given at construction time) is used.
        flags
            Deprecated in traitlets 5.0, instantiate the config loader with the flags.

        """
    def get_extra_args(self): ...

class _FlagAction(argparse.Action):
    """ArgParse action to handle a flag"""
    flag: Incomplete
    alias: Incomplete
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None: ...

class KVArgParseConfigLoader(ArgParseConfigLoader):
    """A config loader that loads aliases and flags with argparse,

    as well as arbitrary --Class.trait value
    """
    parser_class: Incomplete

class KeyValueConfigLoader(KVArgParseConfigLoader):
    """Deprecated in traitlets 5.0

    Use KVArgParseConfigLoader
    """
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...

def load_pyconfig_files(config_files, path):
    """Load multiple Python config files, merging each of them in turn.

    Parameters
    ----------
    config_files : list of str
        List of config files names to load and merge into the config.
    path : unicode
        The full path to the location of the config files.
    """
