from dataclasses import dataclass
from typing import Any, Callable, ClassVar, Dict, Iterable, Mapping, MutableMapping

__all__ = ['AbstractConfig', 'ConfigAlreadyRegisteredError', 'ConfigError', 'ConfigUnknownOptionError', 'ConfigValueParsingError', 'ConfigValueValidationError', 'Option', 'Options']

class ConfigError(Exception):
    """Base exception for the config module."""

class ConfigAlreadyRegisteredError(ConfigError):
    """Raised when a module tries to register a configuration option that
    already exists.

    Should not be raised too much really, only when developing new fontTools
    modules.
    """
    def __init__(self, name) -> None: ...

class ConfigValueParsingError(ConfigError):
    """Raised when a configuration value cannot be parsed."""
    def __init__(self, name, value) -> None: ...

class ConfigValueValidationError(ConfigError):
    """Raised when a configuration value cannot be validated."""
    def __init__(self, name, value) -> None: ...

class ConfigUnknownOptionError(ConfigError):
    """Raised when a configuration option is unknown."""
    def __init__(self, option_or_name) -> None: ...

@dataclass(frozen=True, eq=False)
class Option:
    name: str
    help: str
    default: Any
    parse: Callable[[str], Any]
    validate: Callable[[Any], bool] | None = ...
    @staticmethod
    def parse_optional_bool(v: str) -> bool | None: ...
    @staticmethod
    def validate_optional_bool(v: Any) -> bool: ...
    def __init__(self, name, help, default, parse, validate) -> None: ...

class Options(Mapping):
    """Registry of available options for a given config system.

    Define new options using the :meth:`register()` method.

    Access existing options using the Mapping interface.
    """
    def __init__(self, other: Options = None) -> None: ...
    def register(self, name: str, help: str, default: Any, parse: Callable[[str], Any], validate: Callable[[Any], bool] | None = None) -> Option:
        """Create and register a new option."""
    def register_option(self, option: Option) -> Option:
        """Register a new option."""
    def is_registered(self, option: Option) -> bool:
        """Return True if the same option object is already registered."""
    def __getitem__(self, key: str) -> Option: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...

class AbstractConfig(MutableMapping):
    '''
    Create a set of config values, optionally pre-filled with values from
    the given dictionary or pre-existing config object.

    The class implements the MutableMapping protocol keyed by option name (`str`).
    For convenience its methods accept either Option or str as the key parameter.

    .. seealso:: :meth:`set()`

    This config class is abstract because it needs its ``options`` class
    var to be set to an instance of :class:`Options` before it can be
    instanciated and used.

    .. code:: python

        class MyConfig(AbstractConfig):
            options = Options()

        MyConfig.register_option( "test:option_name", "This is an option", 0, int, lambda v: isinstance(v, int))

        cfg = MyConfig({"test:option_name": 10})

    '''
    options: ClassVar[Options]
    @classmethod
    def register_option(cls, name: str, help: str, default: Any, parse: Callable[[str], Any], validate: Callable[[Any], bool] | None = None) -> Option:
        """Register an available option in this config system."""
    def __init__(self, values: AbstractConfig | Dict[Option | str, Any] = {}, parse_values: bool = False, skip_unknown: bool = False) -> None: ...
    def set(self, option_or_name: Option | str, value: Any, parse_values: bool = False, skip_unknown: bool = False):
        """Set the value of an option.

        Args:
            * `option_or_name`: an `Option` object or its name (`str`).
            * `value`: the value to be assigned to given option.
            * `parse_values`: parse the configuration value from a string into
                its proper type, as per its `Option` object. The default
                behavior is to raise `ConfigValueValidationError` when the value
                is not of the right type. Useful when reading options from a
                file type that doesn't support as many types as Python.
            * `skip_unknown`: skip unknown configuration options. The default
                behaviour is to raise `ConfigUnknownOptionError`. Useful when
                reading options from a configuration file that has extra entries
                (e.g. for a later version of fontTools)
        """
    def get(self, option_or_name: Option | str, default: Any = ...) -> Any:
        '''
        Get the value of an option. The value which is returned is the first
        provided among:

        1. a user-provided value in the options\'s ``self._values`` dict
        2. a caller-provided default value to this method call
        3. the global default for the option provided in ``fontTools.config``

        This is to provide the ability to migrate progressively from config
        options passed as arguments to fontTools APIs to config options read
        from the current TTFont, e.g.

        .. code:: python

            def fontToolsAPI(font, some_option):
                value = font.cfg.get("someLib.module:SOME_OPTION", some_option)
                # use value

        That way, the function will work the same for users of the API that
        still pass the option to the function call, but will favour the new
        config mechanism if the given font specifies a value for that option.
        '''
    def copy(self): ...
    def __getitem__(self, option_or_name: Option | str) -> Any: ...
    def __setitem__(self, option_or_name: Option | str, value: Any) -> None: ...
    def __delitem__(self, option_or_name: Option | str) -> None: ...
    def __iter__(self) -> Iterable[str]: ...
    def __len__(self) -> int: ...
