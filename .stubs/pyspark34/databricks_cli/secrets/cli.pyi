from _typeshed import Incomplete
from databricks_cli.click_types import OutputClickType as OutputClickType, SecretKeyClickType as SecretKeyClickType, SecretPrincipalClickType as SecretPrincipalClickType, SecretScopeClickType as SecretScopeClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.secrets.api import SecretApi as SecretApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, error_and_quit as error_and_quit, pretty_format as pretty_format, truncate_string as truncate_string
from databricks_cli.version import print_version_callback as print_version_callback, version as version

SCOPE_HEADER: Incomplete
SECRET_HEADER: Incomplete
ACL_HEADER: Incomplete
DASH_MARKER: Incomplete

def create_scope(api_client, scope, initial_manage_principal, scope_backend_type, resource_id, dns_name) -> None:
    """
    Creates a new secret scope with given name.
    """
def list_scopes(api_client, output) -> None:
    """
    Lists all secret scopes.
    """
def delete_scope(api_client, scope) -> None:
    """
    Deletes a secret scope.
    """
def put_secret(api_client, scope, key, string_value, binary_file) -> None:
    '''
    Puts a secret in the provided scope with the given name.
    Overwrites any existing value if the name exists.

    You should specify at most one option in "string-value" and "binary-file".

    If "string-value", the argument will be stored in UTF-8 (MB4) form.

    If "binary-file", the argument should be a path to file. File content will be read as secret
    value and stored as bytes.

    If none of "string-value" and "binary-file" specified, an editor will be opened for
    inputting secret value. The value will be stored in UTF-8 (MB4) form.

    "databricks secrets write" is an alias for "databricks secrets put", and will be
    deprecated in a future release.
    '''
def delete_secret(api_client, scope, key) -> None:
    """
    Deletes the secret stored in this scope.
    """
def list_secrets(api_client, scope, output) -> None:
    """
    Lists the secret keys that are stored at this scope. Also lists the last updated timestamp
    (UNIX time in milliseconds) if available.
    """
def put_acl(api_client, scope, principal, permission) -> None:
    '''
    Creates or overwrites the ACL associated with the given principal (user or group) on the
    specified secret scope.

    "databricks secrets write-acl" is an alias for "databricks secrets put-acl",
    and will be deprecated in a future release.
    '''
def delete_acl(api_client, scope, principal) -> None:
    """
    Deletes the given ACL on the given secret scope.
    """
def list_acls(api_client, scope, output) -> None:
    """
    Lists the ACLs set on the given secret scope.
    """
def get_acl(api_client, scope, principal, output) -> None:
    """
    Describes the details about the given ACL for the principal and secret scope.
    """
def secrets_group() -> None:
    """
    Utility to interact with secret API.
    """
