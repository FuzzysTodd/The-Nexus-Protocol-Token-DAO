from databricks_cli.click_types import ClusterPolicyIdClickType as ClusterPolicyIdClickType, JsonClickType as JsonClickType, OutputClickType as OutputClickType
from databricks_cli.cluster_policies.api import ClusterPolicyApi as ClusterPolicyApi
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base, pretty_format as pretty_format, truncate_string as truncate_string
from databricks_cli.version import print_version_callback as print_version_callback, version as version

def create_cli(api_client, json_file, json):
    """
    Creates a Databricks cluster Policy.

    The specification for the request json can be found at
    https://docs.databricks.com/dev-tools/api/latest/policies.html#create
    """
def edit_cli(api_client, json_file, json) -> None:
    """
    Edits a Databricks cluster Policy.

    The specification for the request json can be found at
    https://docs.databricks.com/dev-tools/api/latest/policies.html#edit
    """
def delete_cli(api_client, policy_id) -> None:
    """
    Removes a Databricks cluster policy given its ID.

    Use ``databricks cluster_olicies get --policy-id POLICY_ID`` to check termination states.
    """
def get_cli(api_client, policy_id) -> None:
    """
    Retrieves metadata about a cluster policy.
    """
def list_cli(api_client, output) -> None:
    """
    Lists cluster olicies.

    Returns information about all currently cluster olicies.

    By default the output format will be a human readable table with the following fields

      - Policy ID

      - Policy Name

      - Policy Definition
    """
def cluster_policies_group() -> None:
    """
    Utility to interact with Databricks cluster policies.
    """
