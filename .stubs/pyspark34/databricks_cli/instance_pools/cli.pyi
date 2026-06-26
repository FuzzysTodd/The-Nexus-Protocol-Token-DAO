from databricks_cli.click_types import InstancePoolIdClickType as InstancePoolIdClickType, JsonClickType as JsonClickType, OutputClickType as OutputClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.instance_pools.api import InstancePoolsApi as InstancePoolsApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base, pretty_format as pretty_format, truncate_string as truncate_string
from databricks_cli.version import print_version_callback as print_version_callback, version as version

def create_cli(api_client, json_file, json):
    """
    Creates a Databricks instance pool.

    The specification for the request json can be found at
    https://docs.databricks.com/api/latest/instance-pools.html#create
    """
def edit_cli(api_client, json_file, json):
    """
    Edits a Databricks instance pool.

    The specification for the request json can be found at
    https://docs.databricks.com/api/latest/instance-pools.html#edit
    """
def delete_cli(api_client, instance_pool_id) -> None:
    """
    Deletes a Databricks instance pool given its ID.

    This permanently deletes the instance pool. The idle instances in the pool are terminated
    asynchronously. New clusters cannot attach to the pool. Running clusters attached to the pool
    continue to run but cannot auto-scale up. Terminated clusters attached to the pool will fail to
    start until they are edited to no longer use the pool.
    """
def get_cli(api_client, instance_pool_id) -> None:
    """
    Retrieves metadata about an instance pool.
    """
def list_cli(api_client, output) -> None:
    """
    Lists active instance pools with the stats of the pools.
    """
def instance_pools_group() -> None:
    """
    Utility to interact with Databricks instance pools.
    """
