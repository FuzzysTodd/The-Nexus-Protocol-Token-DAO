import configparser
from _typeshed import Incomplete
from pip._internal.exceptions import ConfigurationError as ConfigurationError, ConfigurationFileCouldNotBeLoaded as ConfigurationFileCouldNotBeLoaded
from pip._internal.utils import appdirs as appdirs
from pip._internal.utils.compat import WINDOWS as WINDOWS
from pip._internal.utils.logging import getLogger as getLogger
from pip._internal.utils.misc import ensure_dir as ensure_dir, enum as enum
from typing import Any, Dict, Iterable, List, Tuple

RawConfigParser = configparser.RawConfigParser
Kind: Incomplete
CONFIG_BASENAME: Incomplete
ENV_NAMES_IGNORED: Incomplete
kinds: Incomplete
OVERRIDE_ORDER: Incomplete
VALID_LOAD_ONLY: Incomplete
logger: Incomplete

def get_configuration_files() -> Dict[Kind, List[str]]: ...

class Configuration:
    '''Handles management of configuration.

    Provides an interface to accessing and managing configuration files.

    This class converts provides an API that takes "section.key-name" style
    keys and stores the value associated with it as "key-name" under the
    section "section".

    This allows for a clean interface wherein the both the section and the
    key-name are preserved in an easy to manage form in the configuration files
    and the data stored is also nice.
    '''
    isolated: Incomplete
    load_only: Incomplete
    def __init__(self, isolated: bool, load_only: Kind | None = None) -> None: ...
    def load(self) -> None:
        """Loads configuration from configuration files and environment"""
    def get_file_to_edit(self) -> str | None:
        """Returns the file with highest priority in configuration"""
    def items(self) -> Iterable[Tuple[str, Any]]:
        """Returns key-value pairs like dict.items() representing the loaded
        configuration
        """
    def get_value(self, key: str) -> Any:
        """Get a value from the configuration."""
    def set_value(self, key: str, value: Any) -> None:
        """Modify a value in the configuration."""
    def unset_value(self, key: str) -> None:
        """Unset a value in the configuration."""
    def save(self) -> None:
        """Save the current in-memory state."""
    def get_environ_vars(self) -> Iterable[Tuple[str, str]]:
        """Returns a generator with all environmental vars with prefix PIP_"""
    def iter_config_files(self) -> Iterable[Tuple[Kind, List[str]]]:
        """Yields variant and configuration files associated with it.

        This should be treated like items of a dictionary.
        """
    def get_values_in_config(self, variant: Kind) -> Dict[str, Any]:
        """Get values present in a config file"""
