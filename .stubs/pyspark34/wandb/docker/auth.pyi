from _typeshed import Incomplete
from typing import Any, Dict, Mapping, Tuple

IS_WINDOWS_PLATFORM: Incomplete
DOCKER_CONFIG_FILENAME: Incomplete
LEGACY_DOCKER_CONFIG_FILENAME: str
INDEX_NAME: str
INDEX_URL: Incomplete
TOKEN_USERNAME: str
log: Incomplete

class DockerError(Exception):
    """Base class from which all other exceptions inherit.

    If you want to catch all errors that the Docker SDK might raise,
    catch this base exception.
    """
class InvalidConfigFileError(DockerError): ...
class InvalidRepositoryError(DockerError): ...

def find_config_file(config_path: str | None = None) -> str | None: ...
def config_path_from_environment() -> str | None: ...
def home_dir() -> str:
    """Get the user's home directory.

    Uses the same logic as the Docker Engine client - use %USERPROFILE% on Windows,
    $HOME/getuid on POSIX.
    """
def load_general_config(config_path: str | None = None) -> Dict: ...
def resolve_repository_name(repo_name: str) -> Tuple[str, str]: ...
def resolve_index_name(index_name: str) -> str: ...
def split_repo_name(repo_name: str) -> Tuple[str, str]: ...
def get_credential_store(authconfig: Dict, registry: str) -> str | None: ...

class AuthConfig(dict):
    def __init__(self, dct: Dict, credstore_env: Mapping | None = None) -> None: ...
    @classmethod
    def parse_auth(cls, entries: Dict[str, Dict[str, Any]], raise_on_error: bool = False) -> Dict[str, Dict[str, Any]]:
        """Parse authentication entries.

        Arguments:
          entries:        Dict of authentication entries.
          raise_on_error: If set to true, an invalid format will raise
                          InvalidConfigFileError
        Returns:
          Authentication registry.
        """
    @classmethod
    def load_config(cls, config_path: str | None, config_dict: Dict[str, Any] | None, credstore_env: Mapping | None = None) -> AuthConfig:
        """Load authentication data from a Docker configuration file.

        If the config_path is not passed in it looks for a configuration file in the
        root directory.

        Lookup priority:
            explicit config_path parameter > DOCKER_CONFIG environment
            variable > ~/.docker/config.json > ~/.dockercfg.
        """
    @property
    def auths(self) -> Dict[str, Dict[str, Any]]: ...
    @property
    def creds_store(self) -> str | None: ...
    @property
    def cred_helpers(self) -> Dict: ...
    @property
    def is_empty(self) -> bool: ...
    def resolve_authconfig(self, registry: str | None = None) -> Dict[str, Any] | None:
        """Return the authentication data for a specific registry.

        As with the Docker client, legacy entries in the config with full URLs are
        stripped down to hostnames before checking for a match. Returns None if no match
        was found.
        """
    def get_credential_store(self, registry: str | None) -> str | None: ...
    def get_all_credentials(self) -> Dict[str, Dict[str, Any]]: ...
    def add_auth(self, reg: str, data: Dict[str, Any]) -> None: ...

def resolve_authconfig(authconfig: Dict, registry: str | None = None, credstore_env: Mapping | None = None) -> Dict[str, Any] | None: ...
def convert_to_hostname(url: str) -> str: ...
def decode_auth(auth: str | bytes) -> Tuple[str, str]: ...
def parse_auth(entries: Dict, raise_on_error: bool = False) -> Dict[str, Dict[str, Any]]:
    """Parse authentication entries.

    Arguments:
      entries:        Dict of authentication entries.
      raise_on_error: If set to true, an invalid format will raise
                      InvalidConfigFileError
    Returns:
      Authentication registry.
    """
def load_config(config_path: str | None = None, config_dict: Dict[str, Any] | None = None, credstore_env: Mapping | None = None) -> AuthConfig: ...
