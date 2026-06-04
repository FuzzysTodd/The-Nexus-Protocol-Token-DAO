from _typeshed import Incomplete
from databricks_cli.sdk import ReposService as ReposService, WorkspaceService as WorkspaceService

class ReposApi:
    client: Incomplete
    ws_client: Incomplete
    def __init__(self, api_client) -> None: ...
    def get_repo_id(self, path): ...
    def list(self, path_prefix, next_page_token):
        """
        List repos that the caller has Manage permissions on. Results are
        paginated with each page containing twenty repos.
        """
    def create(self, url, provider, path):
        """
        Creates a repo object and links it to the remote Git repo specified.
        """
    def get(self, repo_id):
        """
        Gets the repo with the given ID.
        """
    def update(self, repo_id, branch, tag):
        """
        Checks out the repo to the given branch or tag. Only one of ``branch``
        or ``tag`` should be provided.
        """
    def delete(self, repo_id):
        """
        Deletes the repo with the given ID.
        """
