from databricks_cli.click_types import ClusterIdClickType as ClusterIdClickType, JsonClickType as JsonClickType, OneOfOption as OneOfOption, OutputClickType as OutputClickType
from databricks_cli.clusters.api import ClusterApi as ClusterApi
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.utils import CLUSTER_OPTIONS as CLUSTER_OPTIONS, CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base, pretty_format as pretty_format, truncate_string as truncate_string
from databricks_cli.version import print_version_callback as print_version_callback, version as version

def create_cli(api_client, json_file, json):
    """
    Creates a Databricks cluster.

    The specification for the request json can be found at
    https://docs.databricks.com/api/latest/clusters.html#create
    """
def edit_cli(api_client, json_file, json) -> None:
    """
    Edits a Databricks cluster.

    The specification for the request json can be found at
    https://docs.databricks.com/api/latest/clusters.html#edit
    """
def start_cli(api_client, cluster_id) -> None:
    """
    Starts a terminated Databricks cluster given its ID.

    If the cluster is not currently in a TERMINATED state, nothing will happen.

    """
def restart_cli(api_client, cluster_id) -> None:
    """
    Restarts a Databricks cluster given its ID.

    If the cluster is not currently in a RUNNING state, nothing will happen
    """
def resize_cli(api_client, cluster_id, num_workers) -> None:
    """Resizes a Databricks cluster given its ID.

    Provide a `--num-workers` parameter to indicate the new cluster size.

    If the cluster is not currently in a RUNNING state, this will cause an
    error to occur.
    """
def delete_cli(api_client, cluster_id) -> None:
    """
    Removes a Databricks cluster given its ID.

    The cluster is removed asynchronously. Once the deletion has completed,
    the cluster will be in a TERMINATED state. If the cluster is already in
    a TERMINATING or TERMINATED state, nothing will happen.

    Use ``databricks clusters get --cluster-id CLUSTER_ID`` to check termination states.
    """
def get_cli(api_client, cluster_id, cluster_name) -> None:
    """
    Retrieves metadata about a cluster.
    """
def list_cli(api_client, output) -> None:
    """
    Lists active and recently terminated clusters.

    Returns information about all currently active clusters, and up
    to 100 most recently terminated clusters in the past 7 days.

    By default the output format will be a human readable table with the following fields

      - Cluster ID

      - Cluster name

      - Cluster state
    """
def list_zones_cli(api_client) -> None:
    """
    Lists zones where clusters can be created.

    The output format is specified in
    https://docs.databricks.com/api/latest/clusters.html#list-zones
    """
def list_node_types_cli(api_client) -> None:
    """
    Lists possible node types for a cluster.

    The output format is specified in
    https://docs.databricks.com/api/latest/clusters.html#list-node-types
    """
def spark_versions_cli(api_client) -> None:
    """
    Lists possible Databricks Runtime versions for a cluster.

    The output format is specified in
    https://docs.databricks.com/api/latest/clusters.html#spark-versions
    """
def permanent_delete_cli(api_client, cluster_id) -> None:
    """
    Permanently deletes a Spark cluster.

    If the cluster is running, it is terminated and its resources are asynchronously removed.
    If the cluster is terminated, then it is immediately removed.
    """
def cluster_events_cli(api_client, cluster_id, start_time, end_time, order, event_type, offset, limit, output) -> None:
    """
    Gets events for a Spark cluster.
    """
def clusters_group() -> None:
    """
    Utility to interact with Databricks clusters.
    """
