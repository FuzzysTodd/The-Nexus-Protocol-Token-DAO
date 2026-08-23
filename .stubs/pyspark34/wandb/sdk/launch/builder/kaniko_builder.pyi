from .._project_spec import EntryPoint as EntryPoint, LaunchProject as LaunchProject, create_metadata_file as create_metadata_file, get_entry_point_command as get_entry_point_command
from ..errors import LaunchError as LaunchError
from ..utils import LOG_PREFIX as LOG_PREFIX, get_kube_context_and_api_client as get_kube_context_and_api_client, sanitize_wandb_api_key as sanitize_wandb_api_key, warn_failed_packages_from_build_logs as warn_failed_packages_from_build_logs
from .build import generate_dockerfile as generate_dockerfile, image_tag_from_dockerfile_and_source as image_tag_from_dockerfile_and_source
from _typeshed import Incomplete
from wandb.sdk.launch.agent.job_status_tracker import JobAndRunStatusTracker as JobAndRunStatusTracker
from wandb.sdk.launch.builder.abstract import AbstractBuilder as AbstractBuilder
from wandb.sdk.launch.environment.abstract import AbstractEnvironment as AbstractEnvironment
from wandb.sdk.launch.environment.azure_environment import AzureEnvironment as AzureEnvironment
from wandb.sdk.launch.registry.abstract import AbstractRegistry as AbstractRegistry
from wandb.sdk.launch.registry.azure_container_registry import AzureContainerRegistry as AzureContainerRegistry
from wandb.sdk.launch.registry.elastic_container_registry import ElasticContainerRegistry as ElasticContainerRegistry
from wandb.sdk.launch.registry.google_artifact_registry import GoogleArtifactRegistry as GoogleArtifactRegistry
from wandb.util import get_module as get_module

SERVICE_ACCOUNT_NAME: Incomplete
NAMESPACE: Incomplete

class KanikoBuilder(AbstractBuilder):
    """Builds a docker image for a project using Kaniko."""
    type: str
    build_job_name: str
    build_context_store: str
    secret_name: str | None
    secret_key: str | None
    image: str
    environment: Incomplete
    registry: Incomplete
    def __init__(self, environment: AbstractEnvironment, registry: AbstractRegistry, build_job_name: str = 'wandb-launch-container-build', build_context_store: str = '', secret_name: str = '', secret_key: str = '', image: str = 'gcr.io/kaniko-project/executor:v1.11.0', verify: bool = True) -> None:
        """Initialize a KanikoBuilder.

        Arguments:
            environment (AbstractEnvironment): The environment to use.
            registry (AbstractRegistry): The registry to use.
            build_job_name (str, optional): The name of the build job.
            build_context_store (str, optional): The name of the build context store.
            secret_name (str, optional): The name of the secret to use for the registry.
            secret_key (str, optional): The key of the secret to use for the registry.
            verify (bool, optional): Whether to verify the functionality of the builder.
                Defaults to True.
        """
    @classmethod
    def from_config(cls, config: dict, environment: AbstractEnvironment, registry: AbstractRegistry, verify: bool = True, login: bool = True) -> AbstractBuilder:
        '''Create a KanikoBuilder from a config dict.

        Arguments:
            config: A dict containing the builder config. Must contain a "type" key
                with value "kaniko".
            environment: The environment to use for the build.
            registry: The registry to use for the build.
            verify: Whether to verify the builder config.

        Returns:
            A KanikoBuilder instance.
        '''
    def verify(self) -> None:
        """Verify that the builder config is valid.

        Raises:
            LaunchError: If the builder config is invalid.
        """
    def login(self) -> None:
        """Login to the registry."""
    def build_image(self, launch_project: LaunchProject, entrypoint: EntryPoint, job_tracker: JobAndRunStatusTracker | None = None) -> str: ...
