from _typeshed import Incomplete
from click import ParamType
from databricks_cli.configure.config import debug_option as debug_option, get_profile_from_context as get_profile_from_context, profile_option as profile_option
from databricks_cli.configure.provider import DatabricksConfig as DatabricksConfig, ProfileConfigProvider as ProfileConfigProvider, update_and_persist_config as update_and_persist_config
from databricks_cli.oauth.oauth import get_tokens as get_tokens
from databricks_cli.sdk.version import API_VERSION as API_VERSION, API_VERSIONS as API_VERSIONS
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS

PROMPT_HOST: str
PROMPT_USERNAME: str
PROMPT_PASSWORD: str
PROMPT_TOKEN: str
ENV_AAD_TOKEN: str
DEFAULT_SCOPES: Incomplete

def scope_format(user_input): ...
def configure_cli(token, aad_token, insecure, host, token_file, jobs_api_version, oauth, scope) -> None:
    """
    Configures host, authentication, and jobs-api version for the CLI.
    """

class _DbfsHost(ParamType):
    """
    Used to validate the configured host
    """
    def convert(self, value, param, ctx): ...
