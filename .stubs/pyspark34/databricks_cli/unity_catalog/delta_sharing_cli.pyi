from _typeshed import Incomplete
from databricks_cli.click_types import JsonClickType as JsonClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.unity_catalog.api import UnityCatalogApi as UnityCatalogApi
from databricks_cli.unity_catalog.utils import hide as hide, json_file_help as json_file_help, json_string_help as json_string_help, mc_pretty_format as mc_pretty_format
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base, merge_dicts_shallow as merge_dicts_shallow

def create_share_cli(api_client, name) -> None:
    """
    Create a new share.
    """
def list_shares_cli(api_client) -> None:
    """
    List shares.
    """
def get_share_cli(api_client, name, include_shared_data) -> None:
    """
    Get a share.
    """
def list_share_permissions_cli(api_client, name) -> None:
    """
    List permissions on a share.
    """
def update_share_permissions_cli(api_client, name, json_file, json):
    """
    Update permissions on a share.

    The public specification for the JSON request is in development.
    """
def update_share_cli(api_client, name, new_name, comment, owner, add_table, remove_table, json_file, json):
    """
    Update a share.

    The public specification for the JSON request is in development.
    """
def shared_schema_object(name: Incomplete | None = None, comment: Incomplete | None = None): ...
def create_common_shared_schema_options(f): ...
def add_share_schema_cli(api_client, share, schema, comment, json_file, json) -> None:
    """
    Adds a shared schema.

    The public specification for the JSON request is in development.
    """
def update_share_schema_cli(api_client, share, schema, comment, json_file, json) -> None:
    """
    Updates a shared schema.

    The public specification for the JSON request is in development.
    """
def remove_share_schema_cli(api_client, share, schema, json_file, json) -> None:
    """
    Removes a shared schema by full schema name.

    The public specification for the JSON request is in development.
    """
def shared_table_object(name: Incomplete | None = None, comment: Incomplete | None = None, shared_as: Incomplete | None = None, cdf_enabled: Incomplete | None = None, partitions: Incomplete | None = None, start_version: Incomplete | None = None): ...
def create_common_shared_table_options(f): ...
def add_share_table_cli(api_client, share, table, shared_as, comment, partitions, cdf, start_version, json_file, json) -> None:
    """
    Adds a shared table.

    The public specification for the JSON request is in development.
    """
def update_share_table_cli(api_client, share, table, shared_as, comment, partitions, cdf, start_version, json_file, json) -> None:
    """
    Updates a shared table.

    The public specification for the JSON request is in development.
    """
def remove_share_table_cli(api_client, share, table, shared_as, json_file, json) -> None:
    """
    Removes a shared table either by table name or the shared-as table name.

    The public specification for the JSON request is in development.
    """
def delete_share_cli(api_client, name) -> None:
    """
    Delete a share.
    """
def parse_recipient_custom_properties(custom_property_list): ...
def create_recipient_cli(api_client, name, comment, sharing_id, allowed_ip_address, custom_property) -> None:
    """
    Create a new recipient.
    """
def list_recipients_cli(api_client) -> None:
    """
    List recipients.
    """
def get_recipient_cli(api_client, name) -> None:
    """
    Get a recipient.
    """
def update_recipient_cli(api_client, name, new_name, comment, owner, allowed_ip_address, custom_property, json_file, json):
    """
    Update a recipient.

    The public specification for the JSON request is in development.
    """
def rotate_recipient_token_cli(api_client, name, existing_token_expire_in_seconds) -> None:
    """
    Rotate recipient token.
    """
def list_recipient_permissions_cli(api_client, name) -> None:
    """
    List a recipient's share permissions.
    """
def delete_recipient_cli(api_client, name) -> None:
    """
    Delete a recipient.
    """
def create_provider_cli(api_client, name, comment, recipient_profile_json_file, recipient_profile_json):
    """
    Create a provider.

    The public specification for the JSON request is in development.
    """
def list_providers_cli(api_client) -> None:
    """
    List providers.
    """
def get_provider_cli(api_client, name) -> None:
    """
    Get a provider.
    """
def update_provider_cli(api_client, name, new_name, comment, owner, recipient_profile_json_file, recipient_profile_json, json_file, json):
    """
    Update a provider.

    The public specification for the JSON request is in development.
    """
def list_provider_shares_cli(api_client, name) -> None:
    """
    List a provider's shares.
    """
def delete_provider_cli(api_client, name) -> None:
    """
    Delete a provider.
    """
def shares_group() -> None: ...
def register_shares_commands(cmd_group) -> None: ...
def recipients_group() -> None: ...
def register_recipients_commands(cmd_group) -> None: ...
def providers_group() -> None: ...
def register_providers_commands(cmd_group) -> None: ...
def register_delta_sharing_commands(cmd_group) -> None: ...
