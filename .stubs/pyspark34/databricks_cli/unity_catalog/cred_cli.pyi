from databricks_cli.click_types import JsonClickType as JsonClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base

def fill_credential(data, aws_iam_role_arn, az_sp_directory_id, az_sp_application_id, az_sp_client_secret, az_mi_access_connector_id, az_mi_id, gcp_sak_email, gcp_sak_private_key_id, gcp_sak_private_key) -> None: ...
def create_update_common_options(f): ...
def create_credential_cli(api_client, name, aws_iam_role_arn, az_sp_directory_id, az_sp_application_id, az_sp_client_secret, az_mi_access_connector_id, az_mi_id, gcp_sak_email, gcp_sak_private_key_id, gcp_sak_private_key, comment, skip_val, json_file, json):
    """
    Create new storage credential.

    The public specification for the JSON request is in development.
    """
def list_credentials_cli(api_client, name_pattern) -> None:
    """
    List storage credentials.
    """
def get_credential_cli(api_client, name) -> None:
    """
    Get a storage credential.
    """
def update_credential_cli(api_client, name, new_name, aws_iam_role_arn, az_sp_directory_id, az_sp_application_id, az_sp_client_secret, az_mi_access_connector_id, az_mi_id, gcp_sak_email, gcp_sak_private_key_id, gcp_sak_private_key, comment, owner, skip_val, json_file, json):
    """
    Update a storage credential.

    The public specification for the JSON request is in development.
    """
def delete_credential_cli(api_client, name, force) -> None:
    """
    Delete a storage credential.
    """
def storage_credentials_group() -> None: ...
def register_cred_commands(cmd_group) -> None: ...
