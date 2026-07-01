from _typeshed import Incomplete
from databricks_cli.sdk import GroupsService as GroupsService

class GroupsApi:
    """Implement the databricks '2.0/groups' API Interface."""
    client: Incomplete
    def __init__(self, api_client) -> None: ...
    def add_member(self, parent_name, user_name, group_name):
        """
        Only one of ``user_name`` or ``group_name`` should be provided.
        """
    def create(self, group_name):
        """Create a new group with the given name."""
    def list_members(self, group_name):
        """Return all of the members of a particular group."""
    def list_all(self):
        """Return all of the groups in an organization."""
    def list_parents(self, user_name, group_name):
        """
        Only one of ``user_name`` or ``group_name`` should be provided.

        Retrieve all groups in which a given user or group is a member.

        Note: this method is non-recursive - it will return all groups in
        which the given user or group is a member but not the groups in which
        those groups are members).
        """
    def remove_member(self, parent_name, user_name, group_name):
        """
        Only one of ``user_name`` or ``group_name`` should be provided.
        """
    def delete(self, group_name):
        """Remove a group from this organization."""
