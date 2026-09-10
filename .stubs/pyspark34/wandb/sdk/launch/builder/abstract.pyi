import abc
from .._project_spec import EntryPoint as EntryPoint, LaunchProject as LaunchProject
from abc import ABC, abstractmethod
from typing import Any, Dict
from wandb.sdk.launch.agent.job_status_tracker import JobAndRunStatusTracker as JobAndRunStatusTracker
from wandb.sdk.launch.environment.abstract import AbstractEnvironment as AbstractEnvironment
from wandb.sdk.launch.registry.abstract import AbstractRegistry as AbstractRegistry

class AbstractBuilder(ABC, metaclass=abc.ABCMeta):
    """Abstract plugin class defining the interface needed to build container images for W&B Launch."""
    builder_type: str
    environment: AbstractEnvironment
    registry: AbstractRegistry
    builder_config: Dict[str, Any]
    @abstractmethod
    def __init__(self, environment: AbstractEnvironment, registry: AbstractRegistry, verify: bool = True):
        """Initialize a builder.

        Arguments:
            builder_config: The builder config.
            registry: The registry to use.
            verify: Whether to verify the functionality of the builder.

        Raises:
            LaunchError: If the builder cannot be intialized or verified.
        """
    @classmethod
    @abstractmethod
    def from_config(cls, config: dict, environment: AbstractEnvironment, registry: AbstractRegistry, verify: bool = True) -> AbstractBuilder:
        """Create a builder from a config dictionary.

        Arguments:
            config: The config dictionary.
            environment: The environment to use.
            registry: The registry to use.
            verify: Whether to verify the functionality of the builder.
            login: Whether to login to the registry immediately.

        Returns:
            The builder.
        """
    @abstractmethod
    def build_image(self, launch_project: LaunchProject, entrypoint: EntryPoint, job_tracker: JobAndRunStatusTracker | None = None) -> str:
        """Build the image for the given project.

        Arguments:
            launch_project: The project to build.
            build_ctx_path: The path to the build context.

        Returns:
            The image name.
        """
    @abstractmethod
    def verify(self) -> None:
        """Verify that the builder can be used to build images.

        Raises:
            LaunchError: If the builder cannot be used to build images.
        """
