from _typeshed import Incomplete
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.tokens.api import TokensApi as TokensApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, pretty_format as pretty_format
from databricks_cli.version import print_version_callback as print_version_callback, version as version

TOKEN_LIFETIME_SEC: Incomplete

def create_token_cli(api_client, lifetime_seconds, comment) -> None:
    """
    Create and return a token.
    This call returns the error QUOTA_EXCEEDED if the caller exceeds the token quota, which is 600.
    """
def list_cli(api_client) -> None:
    """
    List all the valid tokens for a user-workspace pair.
    """
def revoke_cli(api_client, token_id) -> None:
    """
    Revoke an access token.

    This call returns the error RESOURCE_DOES_NOT_EXIST
    if a token with the specified ID is not valid.
    """
def tokens_group() -> None:
    """Utility to interact with Databricks tokens."""
