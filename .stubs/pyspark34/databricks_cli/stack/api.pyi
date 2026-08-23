from _typeshed import Incomplete
from databricks_cli.dbfs.api import DbfsApi as DbfsApi
from databricks_cli.jobs.api import JobsApi as JobsApi
from databricks_cli.stack.exceptions import StackError as StackError
from databricks_cli.workspace.api import DIRECTORY as DIRECTORY, NOTEBOOK as NOTEBOOK, WorkspaceApi as WorkspaceApi
from databricks_cli.workspace.types import WorkspaceLanguage as WorkspaceLanguage

MS_SEC: int
JOBS_SERVICE: str
WORKSPACE_SERVICE: str
DBFS_SERVICE: str
STACK_NAME: str
STACK_RESOURCES: str
STACK_DEPLOYED: str
RESOURCE_ID: str
RESOURCE_SERVICE: str
RESOURCE_WRITE_STATUS: str
RESOURCE_PROPERTIES: str
RESOURCE_DATABRICKS_ID: str
CLI_VERSION_KEY: str
JOBS_RESOURCE_NAME: str
JOBS_RESOURCE_JOB_ID: str
WORKSPACE_RESOURCE_SOURCE_PATH: str
WORKSPACE_RESOURCE_PATH: str
WORKSPACE_RESOURCE_OBJECT_TYPE: str
DBFS_RESOURCE_SOURCE_PATH: str
DBFS_RESOURCE_PATH: str
DBFS_RESOURCE_IS_DIR: str

class StackApi:
    jobs_client: Incomplete
    workspace_client: Incomplete
    dbfs_client: Incomplete
    def __init__(self, api_client) -> None: ...
    def deploy(self, stack_config, stack_status: Incomplete | None = None, headers: Incomplete | None = None, **kwargs):
        """
        Deploys a stack given stack JSON configuration template at path config_path.

        After going through each of the resources and deploying them, stores status JSON
        of deployment with deploy status of each resource deployment.
        For each resource deployment, stack_status is used to get the associated resource status
        of a resource from the last deployment.

        :param stack_config: Must have the fields of
        'name', the name of the stack and 'resources', a list of stack resources.
        :param stack_status: Must have the fields of 'name', the name of the stack, 'resources',
        a list of stack resources, and 'deployed', a list of resource statuses from a previous
        deployment.
        :return: new_stack_status: The new stack status generated from the deployment of
        the given stack_config.
        """
    def download(self, stack_config, headers: Incomplete | None = None, **kwargs) -> None:
        """
        Downloads a stack given a dict of the stack configuration.
        :param stack_config: dict of stack configuration. Must contain 'name' and 'resources' field.
        :return: None.
        """
