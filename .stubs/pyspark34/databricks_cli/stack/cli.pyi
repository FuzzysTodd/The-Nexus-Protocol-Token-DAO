from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.stack.api import StackApi as StackApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions
from databricks_cli.version import print_version_callback as print_version_callback, version as version

DEBUG_MODE: bool

def deploy(api_client, config_path, **kwargs) -> None:
    """
    Deploy a stack to the databricks workspace given a JSON stack configuration template.

    After deployment, a stack status will be saves at <config_file_name>.deployed.json. Please
    do not edit or move the file as it is generated through the CLI and is used for future
    deployments of the stack. If you run into errors with the stack status at deployment,
    please delete the stack status file and try the deployment again. If the problem persists,
    please raise a Github issue on the Databricks CLI repository at
    https://www.github.com/databricks/databricks-cli/issues
    """
def download(api_client, config_path, **kwargs) -> None:
    """
    Download workspace notebooks of a stack to the local filesystem given a JSON stack
    configuration template.
    """
def stack_group() -> None:
    """
    [Beta] Utility to deploy and download Databricks resource stacks.
    """
