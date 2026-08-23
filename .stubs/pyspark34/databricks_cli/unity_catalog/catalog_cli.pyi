from databricks_cli.click_types import JsonClickType as JsonClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base

def create_catalog_cli(api_client, name, comment, provider, share) -> None:
    """
    Create a new catalog.
    """
def list_catalogs_cli(api_client) -> None:
    """
    List catalogs.
    """
def get_catalog_cli(api_client, name) -> None:
    """
    Get a catalog.
    """
def update_catalog_cli(api_client, name, json_file, json):
    """
    Update a catalog.

    The public specification for the JSON request is in development.
    """
def delete_catalog_cli(api_client, name, purge):
    """
    Delete a catalog.
    """
def get_catalog_bindings_cli(api_client, name) -> None:
    """
    Get workspace bindings of a catalog.
    """
def update_catalog_bindings_cli(api_client, name, json_file, json):
    """
    Update workspace bindings of a catalog.

    The public specification for the JSON request is in development.
    """
def catalogs_group() -> None: ...
def register_catalog_commands(cmd_group) -> None: ...
