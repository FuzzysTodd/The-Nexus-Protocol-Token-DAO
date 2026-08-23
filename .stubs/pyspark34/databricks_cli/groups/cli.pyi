from _typeshed import Incomplete
from databricks_cli.click_types import OneOfOption as OneOfOption
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.groups.api import GroupsApi as GroupsApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, pretty_format as pretty_format
from databricks_cli.version import print_version_callback as print_version_callback, version as version

MEMBER_OPTIONS: Incomplete

def add_member_cli(api_client, parent_name, user_name, group_name) -> None:
    """Add a user or group to a group."""
def create_cli(api_client, group_name) -> None:
    """Create a new group with the given name."""
def list_members_cli(api_client, group_name) -> None:
    """Return all of the members of a particular group."""
def list_all_cli(api_client) -> None:
    """Return all of the groups in an organization."""
def list_parents_cli(api_client, user_name, group_name) -> None:
    """Retrieve all groups in which a given user or group is a member."""
def remove_member_cli(api_client, parent_name, user_name, group_name) -> None: ...
def delete_cli(api_client, group_name) -> None:
    """Remove a group from this organization."""
def groups_group() -> None:
    """Provide utility to interact with Databricks groups."""
