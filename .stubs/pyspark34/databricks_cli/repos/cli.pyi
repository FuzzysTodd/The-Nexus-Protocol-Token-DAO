from _typeshed import Incomplete
from databricks_cli.click_types import OneOfOption as OneOfOption
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.repos.api import ReposApi as ReposApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, pretty_format as pretty_format
from databricks_cli.version import print_version_callback as print_version_callback, version as version

UPDATE_OPTIONS: Incomplete
ID_OPTIONS: Incomplete

def list_repos_cli(api_client, path_prefix, next_page_token) -> None:
    """
    List repos that the user has Manage permissions on.
    """
def create_repo_cli(api_client, url, provider, path) -> None:
    """
    Creates a repo object and links it to the remote Git repo specified.
    """
def get_repo_cli(api_client, repo_id, path) -> None:
    """
    Gets the repo.
    """
def update_repo_cli(api_client, repo_id, branch, tag, path) -> None:
    """
    Checks out the repo to the given branch or tag. This call returns an error if the branch 
    or tag doesn't exist.
    """
def delete_repo_cli(api_client, repo_id, path) -> None:
    """
    Deletes the repo.
    """
def repos_group() -> None:
    """Utility to interact with Repos."""
