from databricks_cli.click_types import JsonClickType as JsonClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base

def create_schema_cli(api_client, catalog_name, name, comment) -> None:
    """
    Create a new schema in the specified catalog.
    """
def list_schemas_cli(api_client, catalog_name, name_pattern) -> None:
    """
    List schemas.
    """
def get_schema_cli(api_client, full_name) -> None:
    """
    Get a schema.
    """
def update_schema_cli(api_client, full_name, json_file, json):
    """
    Update a schema.

    The public specification for the JSON request is in development.
    """
def delete_schema_cli(api_client, full_name, purge) -> None:
    """
    Delete a schema.
    """
def schemas_group() -> None: ...
def register_schema_commands(cmd_group) -> None: ...
