from .._project_spec import EntryPoint as EntryPoint, LaunchProject as LaunchProject, create_metadata_file as create_metadata_file, get_entry_point_command as get_entry_point_command
from ..errors import LaunchDockerError as LaunchDockerError, LaunchError as LaunchError
from ..registry.local_registry import LocalRegistry as LocalRegistry
from ..utils import LOG_PREFIX as LOG_PREFIX, sanitize_wandb_api_key as sanitize_wandb_api_key, warn_failed_packages_from_build_logs as warn_failed_packages_from_build_logs
from .build import generate_dockerfile as generate_dockerfile, image_tag_from_dockerfile_and_source as image_tag_from_dockerfile_and_source, validate_docker_installation as validate_docker_installation
from _typeshed import Incomplete
from typing import Any, Dict
from wandb.sdk.launch.agent.job_status_tracker import JobAndRunStatusTracker as JobAndRunStatusTracker
from wandb.sdk.launch.builder.abstract import AbstractBuilder as AbstractBuilder
from wandb.sdk.launch.environment.abstract import AbstractEnvironment as AbstractEnvironment
from wandb.sdk.launch.registry.abstract import AbstractRegistry as AbstractRegistry

class DockerBuilder(AbstractBuilder):
    """Builds a docker image for a project.

    Attributes:
        builder_config (Dict[str, Any]): The builder config.

    """
    builder_type: str
    base_image: str
    target_platform: str
    environment: Incomplete
    registry: Incomplete
    config: Incomplete
    def __init__(self, environment: AbstractEnvironment, registry: AbstractRegistry, config: Dict[str, Any], verify: bool = True, login: bool = True) -> None:
        """Initialize a DockerBuilder.

        Arguments:
            environment (AbstractEnvironment): The environment to use.
            registry (AbstractRegistry): The registry to use.
            verify (bool, optional): Whether to verify the functionality of the builder.
            login (bool, optional): Whether to login to the registry.

        Raises:
            LaunchError: If docker is not installed
        """
    @classmethod
    def from_config(cls, config: Dict[str, Any], environment: AbstractEnvironment, registry: AbstractRegistry, verify: bool = True) -> DockerBuilder:
        """Create a DockerBuilder from a config.

        Arguments:
            config (Dict[str, Any]): The config.
            registry (AbstractRegistry): The registry to use.
            verify (bool, optional): Whether to verify the functionality of the builder.
            login (bool, optional): Whether to login to the registry.

        Returns:
            DockerBuilder: The DockerBuilder.
        """
    def verify(self) -> None:
        """Verify the builder."""
    def login(self) -> None:
        """Login to the registry."""
    def build_image(self, launch_project: LaunchProject, entrypoint: EntryPoint, job_tracker: JobAndRunStatusTracker | None = None) -> str:
        """Build the image for the given project.

        Arguments:
            launch_project (LaunchProject): The project to build.
            entrypoint (EntryPoint): The entrypoint to use.
        """
