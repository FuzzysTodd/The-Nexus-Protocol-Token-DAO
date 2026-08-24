from databricks_cli.click_types import ContextObject as ContextObject
from databricks_cli.configure.provider import ProfileConfigProvider as ProfileConfigProvider, get_config as get_config, update_and_persist_config as update_and_persist_config
from databricks_cli.oauth.oauth import check_and_refresh_access_token as check_and_refresh_access_token
from databricks_cli.sdk import ApiClient as ApiClient
from databricks_cli.sdk.version import API_VERSIONS as API_VERSIONS
from databricks_cli.utils import InvalidConfigurationError as InvalidConfigurationError

def provide_api_client(function):
    """
    Injects the api_client keyword argument to the wrapped function.
    All callbacks wrapped by provide_api_client expect the argument ``profile`` to be passed in.
    """
def get_profile_from_context(): ...
def debug_option(f): ...
def profile_option(f): ...
def api_version_option(f): ...
