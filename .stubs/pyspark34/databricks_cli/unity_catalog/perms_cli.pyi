from _typeshed import Incomplete
from databricks_cli.click_types import JsonClickType as JsonClickType, OneOfOption as OneOfOption
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base

PERMISSIONS_OBJ_TYPES: Incomplete

def get_permissions_cli(api_client, metastore, catalog, schema, table, storage_credential, external_location, effective) -> None:
    """
    Get permissions on a securable.
    """
def update_permissions_cli(api_client, metastore, catalog, schema, table, storage_credential, external_location, json_file, json):
    """
    Update permissions on a securable.

    The public specification for the JSON request is in development.
    """
def permissions_group() -> None: ...
def register_perms_commands(cmd_group) -> None: ...
