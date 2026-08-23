from databricks_cli.click_types import JsonClickType as JsonClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import del_none as del_none, hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base

def create_update_common_options(f): ...
def create_location_cli(api_client, name, url, storage_credential_name, read_only, comment, skip_val, json_file, json):
    """
    Create new external location.

    The public specification for the JSON request is in development.
    """
def list_locations_cli(api_client) -> None:
    """
    List external locations.
    """
def get_location_cli(api_client, name) -> None:
    """
    Get an external location.
    """
def update_location_cli(api_client, name, new_name, url, storage_credential_name, read_only, comment, owner, force, skip_val, json_file, json):
    """
    Update an external location.

    The public specification for the JSON request is in development.
    """
def delete_location_cli(api_client, name, force) -> None:
    """
    Delete an external location.
    """
def validate_location_cli(api_client, name, url, cred_name, cred_aws_iam_role, cred_az_directory_id, cred_az_application_id, cred_az_client_secret, cred_az_mi_access_connector_id, cred_az_mi_id, cred_gcp_sak_email, cred_gcp_sak_private_key_id, cred_gcp_sak_private_key) -> None:
    """
    Validate an external location/credential combination.

    This call will attempt to read/list/write/delete with the given credentials and
    external location.

    One of name/url must be provided. If both are specified, the given credential
    name will be excluded from path overlap checks (used to validate a potential
    update of that credential).

    One of cred-name, or cloud provider specific credential parameters must be
    provided.
    """
def external_locations_group() -> None: ...
def register_ext_loc_commands(cmd_group) -> None: ...
