import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from databricks_cli.utils import InvalidConfigurationError as InvalidConfigurationError

CONFIG_FILE_ENV_VAR: str
HOST: str
USERNAME: str
PASSWORD: str
TOKEN: str
REFRESH_TOKEN: str
INSECURE: str
JOBS_API_VERSION: str
DEFAULT_SECTION: str

def update_and_persist_config(profile, databricks_config) -> None:
    """
    Takes a DatabricksConfig and adds the in memory contents to the persisted version of the
    config. This will overwrite any other config that was persisted to the file system under the
    same profile.
    :param databricks_config: DatabricksConfig
    """
def get_config():
    """
    Returns a DatabricksConfig containing the hostname and authentication used to talk to
    the Databricks API. By default, we leverage the DefaultConfigProvider to get
    this config, but this behavior may be overridden by calling 'set_config_provider'

    If no DatabricksConfig can be found, an InvalidConfigurationError will be raised.
    """
def get_config_for_profile(profile):
    """
    [Deprecated] Reads from the filesystem and gets a DatabricksConfig for the
    specified profile. If it does not exist, then return a DatabricksConfig with fields set
    to None.

    Internal callers should prefer get_config() to use user-specified overrides, and
    to return appropriate error messages as opposited to invalid configurations.

    If you want to read from a specific profile, please instead use
    'ProfileConfigProvider(profile).get_config()'.

    This method is maintained for backwards-compatibility. It may be removed in future versions.

    :return: DatabricksConfig
    """
def set_config_provider(provider) -> None:
    """
    Sets a DatabricksConfigProvider that will be used for all future calls to get_config(),
    used by the Databricks CLI code to discover the user's credentials.
    """
def get_config_provider():
    """
    Returns the current DatabricksConfigProvider.
    If None, the DefaultConfigProvider will be used.
    """

class DatabricksConfigProvider(metaclass=abc.ABCMeta):
    """
    Responsible for providing hostname and authentication information to make
    API requests against the Databricks REST API.
    This method should generally return None if it cannot provide credentials, in order
    to facilitate chanining of providers.
    """
    __metaclass__ = ABCMeta
    @abstractmethod
    def get_config(self): ...

class DefaultConfigProvider(DatabricksConfigProvider):
    """Look for credentials in a chain of default locations."""
    def __init__(self) -> None: ...
    def get_config(self): ...

class SparkTaskContextConfigProvider(DatabricksConfigProvider):
    """Loads credentials from Spark TaskContext if running in a Spark Executor."""
    @staticmethod
    def set_insecure(x) -> None: ...
    def get_config(self): ...

class EnvironmentVariableConfigProvider(DatabricksConfigProvider):
    """Loads from system environment variables."""
    def get_config(self): ...

class ProfileConfigProvider(DatabricksConfigProvider):
    """Loads from the databrickscfg file."""
    profile: Incomplete
    def __init__(self, profile=...) -> None: ...
    def get_config(self): ...

class DatabricksConfig:
    host: Incomplete
    username: Incomplete
    password: Incomplete
    token: Incomplete
    refresh_token: Incomplete
    insecure: Incomplete
    jobs_api_version: Incomplete
    def __init__(self, host, username, password, token, refresh_token: Incomplete | None = None, insecure: Incomplete | None = None, jobs_api_version: Incomplete | None = None) -> None: ...
    @classmethod
    def from_token(cls, host, token, refresh_token: Incomplete | None = None, insecure: Incomplete | None = None, jobs_api_version: Incomplete | None = None): ...
    @classmethod
    def from_password(cls, host, username, password, insecure: Incomplete | None = None, jobs_api_version: Incomplete | None = None): ...
    @classmethod
    def empty(cls): ...
    @property
    def is_valid_with_token(self): ...
    @property
    def is_valid_with_password(self): ...
    @property
    def is_valid(self): ...
