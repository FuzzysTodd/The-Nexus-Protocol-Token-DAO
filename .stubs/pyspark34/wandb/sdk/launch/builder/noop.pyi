from .._project_spec import EntryPoint as EntryPoint, LaunchProject as LaunchProject
from ..agent.job_status_tracker import JobAndRunStatusTracker as JobAndRunStatusTracker
from _typeshed import Incomplete
from typing import Any, Dict
from wandb.sdk.launch.builder.abstract import AbstractBuilder as AbstractBuilder
from wandb.sdk.launch.environment.abstract import AbstractEnvironment as AbstractEnvironment
from wandb.sdk.launch.errors import LaunchError as LaunchError
from wandb.sdk.launch.registry.abstract import AbstractRegistry as AbstractRegistry

class NoOpBuilder(AbstractBuilder):
    """NoOp builder."""
    type: str
    environment: Incomplete
    registry: Incomplete
    def __init__(self, builder_config: Dict[str, Any], environment: AbstractEnvironment, registry: AbstractRegistry) -> None:
        """Initialize a NoOpBuilder."""
    @classmethod
    def from_config(cls, config: dict, environment: AbstractEnvironment, registry: AbstractRegistry, verify: bool = True) -> AbstractBuilder:
        """Create a noop builder from a config."""
    def verify(self) -> None:
        """Verify the builder."""
    def build_image(self, launch_project: LaunchProject, entrypoint: EntryPoint, job_tracker: JobAndRunStatusTracker | None = None) -> str:
        """Build the image.

        For this we raise a launch error since it can't build.
        """
