from databricks_cli.click_types import JsonClickType as JsonClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base

def create_table_cli(api_client, json_file, json):
    """
    Create new table specified by the JSON input.

    WARNING: Creating table metadata via the UC API may create a table
    that is unusable in DBR. Instead, use SQL commands (CREATE TABLE) in DBR.

    The public specification for the JSON request is in development.
    """
def list_tables_cli(api_client, catalog_name, schema_name, name_pattern) -> None:
    """
    List tables.
    """
def list_table_summaries_cli(api_client, catalog_name) -> None:
    """
    List table summaries (in bulk).
    """
def get_table_cli(api_client, full_name) -> None:
    """
    Get a table.
    """
def update_table_cli(api_client, full_name, json_file, json):
    """
    Update a table.

    WARNING: Altering table metadata via the UC API may cause the table
    to be unusable in DBR. Instead, use SQL commands (ALTER TABLE) in DBR.

    The public specification for the JSON request is in development.
    """
def delete_table_cli(api_client, full_name) -> None:
    """
    Delete a table.
    """
def tables_group() -> None: ...
def register_table_commands(cmd_group) -> None: ...
