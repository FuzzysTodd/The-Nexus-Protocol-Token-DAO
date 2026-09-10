from databricks_cli.click_types import JsonClickType as JsonClickType, MetastoreIdClickType as MetastoreIdClickType, WorkspaceIdClickType as WorkspaceIdClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base

def create_metastore_cli(api_client, name, storage_root, region) -> None:
    """
    Create new metastore.
    """
def list_metastores_cli(api_client) -> None:
    """
    List metastores.
    """
def get_metastore_cli(api_client, metastore_id) -> None:
    """
    Get a metastore.
    """
def update_metastore_cli(api_client, metastore_id, new_name, storage_root_credential_id, delta_sharing_scope, delta_sharing_recipient_token_lifetime_in_seconds, delta_sharing_organization_name, owner, json_file, json):
    """
    Update a metastore.

    The public specification for the JSON request is in development.
    """
def delete_metastore_cli(api_client, metastore_id, force) -> None:
    """
    Delete a metastore.
    """
def metastore_summary_cli(api_client) -> None:
    """
    Get metastore summary.
    """
def get_metastore_assignment_cli(api_client) -> None:
    """
    Get current metastore assignment for workspace.
    """
def assign_metastore_cli(api_client, workspace_id, metastore_id, default_catalog_name) -> None:
    """
    Assign a metastore to a specified workspace.

    If the workspace already has a metastore assigned, it is updated.
    """
def unassign_metastore_cli(api_client, workspace_id, metastore_id) -> None:
    """
    Unassign a metastore from a workspace.
    """
def metastores_group() -> None: ...
def register_metastore_commands(cmd_group) -> None: ...
