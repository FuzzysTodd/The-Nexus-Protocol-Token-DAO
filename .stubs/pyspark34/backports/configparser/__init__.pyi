from _typeshed import Incomplete
from collections.abc import MutableMapping

__all__ = ['NoSectionError', 'DuplicateOptionError', 'DuplicateSectionError', 'NoOptionError', 'InterpolationError', 'InterpolationDepthError', 'InterpolationMissingOptionError', 'InterpolationSyntaxError', 'ParsingError', 'MissingSectionHeaderError', 'ConfigParser', 'SafeConfigParser', 'RawConfigParser', 'Interpolation', 'BasicInterpolation', 'ExtendedInterpolation', 'LegacyInterpolation', 'SectionProxy', 'ConverterMapping', 'DEFAULTSECT', 'MAX_INTERPOLATION_DEPTH']

DEFAULTSECT: str
MAX_INTERPOLATION_DEPTH: int

class Error(Exception):
    """Base class for ConfigParser exceptions."""
    message: Incomplete
    def __init__(self, msg: str = '') -> None: ...

class NoSectionError(Error):
    """Raised when no section matches a requested option."""
    section: Incomplete
    args: Incomplete
    def __init__(self, section) -> None: ...

class DuplicateSectionError(Error):
    """Raised when a section is repeated in an input source.

    Possible repetitions that raise this exception are: multiple creation
    using the API or in strict parsers when a section is found more than once
    in a single input file, string or dictionary.
    """
    section: Incomplete
    source: Incomplete
    lineno: Incomplete
    args: Incomplete
    def __init__(self, section, source: Incomplete | None = None, lineno: Incomplete | None = None) -> None: ...

class DuplicateOptionError(Error):
    """Raised by strict parsers when an option is repeated in an input source.

    Current implementation raises this exception only when an option is found
    more than once in a single file, string or dictionary.
    """
    section: Incomplete
    option: Incomplete
    source: Incomplete
    lineno: Incomplete
    args: Incomplete
    def __init__(self, section, option, source: Incomplete | None = None, lineno: Incomplete | None = None) -> None: ...

class NoOptionError(Error):
    """A requested option was not found."""
    option: Incomplete
    section: Incomplete
    args: Incomplete
    def __init__(self, option, section) -> None: ...

class InterpolationError(Error):
    """Base class for interpolation-related exceptions."""
    option: Incomplete
    section: Incomplete
    args: Incomplete
    def __init__(self, option, section, msg) -> None: ...

class InterpolationMissingOptionError(InterpolationError):
    """A string substitution required a setting which was not available."""
    reference: Incomplete
    args: Incomplete
    def __init__(self, option, section, rawval, reference) -> None: ...

class InterpolationSyntaxError(InterpolationError):
    """Raised when the source text contains invalid syntax.

    Current implementation raises this exception when the source text into
    which substitutions are made does not conform to the required syntax.
    """

class InterpolationDepthError(InterpolationError):
    """Raised when substitutions are nested too deeply."""
    args: Incomplete
    def __init__(self, option, section, rawval) -> None: ...

class ParsingError(Error):
    """Raised when a configuration file does not follow legal syntax."""
    source: Incomplete
    errors: Incomplete
    args: Incomplete
    def __init__(self, source: Incomplete | None = None, filename: Incomplete | None = None) -> None: ...
    @property
    def filename(self):
        """Deprecated, use `source'."""
    @filename.setter
    def filename(self, value) -> None:
        """Deprecated, user `source'."""
    def append(self, lineno, line) -> None: ...

class MissingSectionHeaderError(ParsingError):
    """Raised when a key-value pair is found before any section header."""
    source: Incomplete
    lineno: Incomplete
    line: Incomplete
    args: Incomplete
    def __init__(self, filename, lineno, line) -> None: ...

class Interpolation:
    """Dummy interpolation that passes the value through with no changes."""
    def before_get(self, parser, section, option, value, defaults): ...
    def before_set(self, parser, section, option, value): ...
    def before_read(self, parser, section, option, value): ...
    def before_write(self, parser, section, option, value): ...

class BasicInterpolation(Interpolation):
    '''Interpolation as implemented in the classic ConfigParser.

    The option values can contain format strings which refer to other values in
    the same section, or values in the special default section.

    For example:

        something: %(dir)s/whatever

    would resolve the "%(dir)s" to the value of dir.  All reference
    expansions are done late, on demand. If a user needs to use a bare % in
    a configuration file, she can escape it by writing %%. Other % usage
    is considered a user error and raises `InterpolationSyntaxError\'.'''
    def before_get(self, parser, section, option, value, defaults): ...
    def before_set(self, parser, section, option, value): ...

class ExtendedInterpolation(Interpolation):
    """Advanced variant of interpolation, supports the syntax used by
    `zc.buildout'. Enables interpolation between sections."""
    def before_get(self, parser, section, option, value, defaults): ...
    def before_set(self, parser, section, option, value): ...

class LegacyInterpolation(Interpolation):
    """Deprecated interpolation used in old versions of ConfigParser.
    Use BasicInterpolation or ExtendedInterpolation instead."""
    def __init__(self, *args, **kwargs) -> None: ...
    def before_get(self, parser, section, option, value, vars): ...
    def before_set(self, parser, section, option, value): ...

class RawConfigParser(MutableMapping):
    """ConfigParser that does not do interpolation."""
    SECTCRE: Incomplete
    OPTCRE: Incomplete
    OPTCRE_NV: Incomplete
    NONSPACECRE: Incomplete
    BOOLEAN_STATES: Incomplete
    default_section: Incomplete
    def __init__(self, defaults: Incomplete | None = None, dict_type=..., allow_no_value: bool = False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes: Incomplete | None = None, strict: bool = True, empty_lines_in_values: bool = True, default_section=..., interpolation=..., converters=...) -> None: ...
    def defaults(self): ...
    def sections(self):
        """Return a list of section names, excluding [DEFAULT]"""
    def add_section(self, section) -> None:
        """Create a new section in the configuration.

        Raise DuplicateSectionError if a section by the specified name
        already exists. Raise ValueError if name is DEFAULT.
        """
    def has_section(self, section):
        """Indicate whether the named section is present in the configuration.

        The DEFAULT section is not acknowledged.
        """
    def options(self, section):
        """Return a list of option names for the given section name."""
    def read(self, filenames, encoding: Incomplete | None = None):
        """Read and parse a filename or an iterable of filenames.

        Files that cannot be opened are silently ignored; this is
        designed so that you can specify an iterable of potential
        configuration file locations (e.g. current directory, user's
        home directory, systemwide directory), and all existing
        configuration files in the iterable will be read.  A single
        filename may also be given.

        Return list of successfully read files.
        """
    def read_file(self, f, source: Incomplete | None = None) -> None:
        """Like read() but the argument must be a file-like object.

        The `f' argument must be iterable, returning one line at a time.
        Optional second argument is the `source' specifying the name of the
        file being read. If not given, it is taken from f.name. If `f' has no
        `name' attribute, `<???>' is used.
        """
    def read_string(self, string, source: str = '<string>') -> None:
        """Read configuration from a given string."""
    def read_dict(self, dictionary, source: str = '<dict>') -> None:
        """Read configuration from a dictionary.

        Keys are section names, values are dictionaries with keys and values
        that should be present in the section. If the used dictionary type
        preserves order, sections and their keys will be added in order.

        All types held in the dictionary are converted to strings during
        reading, including section names, option names and keys.

        Optional second argument is the `source' specifying the name of the
        dictionary being read.
        """
    def readfp(self, fp, filename: Incomplete | None = None) -> None:
        """Deprecated, use read_file instead."""
    def get(self, section, option, *, raw: bool = False, vars: Incomplete | None = None, fallback=...):
        """Get an option value for a given section.

        If `vars' is provided, it must be a dictionary. The option is looked up
        in `vars' (if provided), `section', and in `DEFAULTSECT' in that order.
        If the key is not found and `fallback' is provided, it is used as
        a fallback value. `None' can be provided as a `fallback' value.

        If interpolation is enabled and the optional argument `raw' is False,
        all interpolations are expanded in the return values.

        Arguments `raw', `vars', and `fallback' are keyword only.

        The section DEFAULT is special.
        """
    def getint(self, section, option, *, raw: bool = False, vars: Incomplete | None = None, fallback=..., **kwargs): ...
    def getfloat(self, section, option, *, raw: bool = False, vars: Incomplete | None = None, fallback=..., **kwargs): ...
    def getboolean(self, section, option, *, raw: bool = False, vars: Incomplete | None = None, fallback=..., **kwargs): ...
    def items(self, section=..., raw: bool = False, vars: Incomplete | None = None):
        """Return a list of (name, value) tuples for each option in a section.

        All % interpolations are expanded in the return values, based on the
        defaults passed into the constructor, unless the optional argument
        `raw' is true.  Additional substitutions may be provided using the
        `vars' argument, which must be a dictionary whose contents overrides
        any pre-existing defaults.

        The section DEFAULT is special.
        """
    def popitem(self):
        """Remove a section from the parser and return it as
        a (section_name, section_proxy) tuple. If no section is present, raise
        KeyError.

        The section DEFAULT is never returned because it cannot be removed.
        """
    def optionxform(self, optionstr): ...
    def has_option(self, section, option):
        """Check for the existence of a given option in a given section.
        If the specified `section' is None or an empty string, DEFAULT is
        assumed. If the specified `section' does not exist, returns False."""
    def set(self, section, option, value: Incomplete | None = None) -> None:
        """Set an option."""
    def write(self, fp, space_around_delimiters: bool = True) -> None:
        """Write an .ini-format representation of the configuration state.

        If `space_around_delimiters' is True (the default), delimiters
        between keys and values are surrounded by spaces.

        Please note that comments in the original configuration file are not
        preserved when writing the configuration back.
        """
    def remove_option(self, section, option):
        """Remove an option."""
    def remove_section(self, section):
        """Remove a file section."""
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def converters(self): ...

class ConfigParser(RawConfigParser):
    """ConfigParser implementing interpolation."""
    def set(self, section, option, value: Incomplete | None = None) -> None:
        """Set an option.  Extends RawConfigParser.set by validating type and
        interpolation syntax on the value."""
    def add_section(self, section) -> None:
        """Create a new section in the configuration.  Extends
        RawConfigParser.add_section by validating if the section name is
        a string."""

class SafeConfigParser(ConfigParser):
    """ConfigParser alias for backwards compatibility purposes."""
    def __init__(self, *args, **kwargs) -> None: ...

class SectionProxy(MutableMapping):
    """A proxy for a single section from a parser."""
    def __init__(self, parser, name) -> None:
        """Creates a view on a section of the specified `name` in `parser`."""
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def parser(self): ...
    @property
    def name(self): ...
    def get(self, option, fallback: Incomplete | None = None, *, raw: bool = False, vars: Incomplete | None = None, _impl: Incomplete | None = None, **kwargs):
        """Get an option value.

        Unless `fallback` is provided, `None` will be returned if the option
        is not found.

        """

class ConverterMapping(MutableMapping):
    """Enables reuse of get*() methods between the parser and section proxies.

    If a parser class implements a getter directly, the value for the given
    key will be ``None``. The presence of the converter name here enables
    section proxies to find and use the implementation on the parser class.
    """
    GETTERCRE: Incomplete
    def __init__(self, parser) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
