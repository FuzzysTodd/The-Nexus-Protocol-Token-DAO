import boto3
from .._project_spec import EntryPoint as EntryPoint, LaunchProject as LaunchProject, get_entry_point_command as get_entry_point_command
from ..builder.build import get_env_vars_dict as get_env_vars_dict
from ..registry.abstract import AbstractRegistry as AbstractRegistry
from ..utils import LOG_PREFIX as LOG_PREFIX, MAX_ENV_LENGTHS as MAX_ENV_LENGTHS, PROJECT_SYNCHRONOUS as PROJECT_SYNCHRONOUS, to_camel_case as to_camel_case
from .abstract import AbstractRun as AbstractRun, AbstractRunner as AbstractRunner, Status as Status
from _typeshed import Incomplete
from typing import Any, Dict, List
from wandb.apis.internal import Api as Api
from wandb.sdk.launch.environment.aws_environment import AwsEnvironment as AwsEnvironment
from wandb.sdk.launch.errors import LaunchError as LaunchError

class SagemakerSubmittedRun(AbstractRun):
    """Instance of ``AbstractRun`` corresponding to a subprocess launched to run an entry point command on aws sagemaker."""
    client: Incomplete
    log_client: Incomplete
    training_job_name: Incomplete
    def __init__(self, training_job_name: str, client: boto3.Client, log_client: boto3.Client | None = None) -> None: ...
    @property
    def id(self) -> str: ...
    def get_logs(self) -> str | None: ...
    def wait(self) -> bool: ...
    def cancel(self) -> None: ...
    def get_status(self) -> Status: ...

class SageMakerRunner(AbstractRunner):
    """Runner class, uses a project to create a SagemakerSubmittedRun."""
    environment: Incomplete
    registry: Incomplete
    def __init__(self, api: Api, backend_config: Dict[str, Any], environment: AwsEnvironment, registry: AbstractRegistry) -> None:
        """Initialize the SagemakerRunner.

        Arguments:
            api (Api): The API instance.
            backend_config (Dict[str, Any]): The backend configuration.
            environment (AwsEnvironment): The AWS environment.

        Raises:
            LaunchError: If the runner cannot be initialized.
        """
    def run(self, launch_project: LaunchProject, image_uri: str) -> AbstractRun | None:
        """Run a project on Amazon Sagemaker.

        Arguments:
            launch_project (LaunchProject): The project to run.

        Returns:
            Optional[AbstractRun]: The run instance.

        Raises:
            LaunchError: If the launch is unsuccessful.
        """

def merge_image_uri_with_algorithm_specification(algorithm_specification: Dict[str, Any] | None, image_uri: str | None, entrypoint_command: List[str], args: List[str] | None) -> Dict[str, Any]:
    """Create an AWS AlgorithmSpecification.

    AWS Sagemaker algorithms require a training image and an input mode. If the user
    does not specify the specification themselves, define the spec minimally using these
    two fields. Otherwise, if they specify the AlgorithmSpecification set the training
    image if it is not set.
    """
def build_sagemaker_args(launch_project: LaunchProject, api: Api, role_arn: str, entry_point: EntryPoint | None, args: List[str] | None, max_env_length: int, image_uri: str | None = None, default_output_path: str | None = None) -> Dict[str, Any]: ...
def launch_sagemaker_job(launch_project: LaunchProject, sagemaker_args: Dict[str, Any], sagemaker_client: boto3.Client, log_client: boto3.Client | None = None) -> SagemakerSubmittedRun: ...
def get_role_arn(sagemaker_args: Dict[str, Any], backend_config: Dict[str, Any], account_id: str) -> str:
    """Get the role arn from the sagemaker args or the backend config."""
