import enum
from .errors import LaunchError as LaunchError
from .utils import LOG_PREFIX as LOG_PREFIX, recursive_macro_sub as recursive_macro_sub
from _typeshed import Incomplete
from typing import Any, Dict, List
from wandb.apis.internal import Api as Api
from wandb.errors import CommError as CommError
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.launch import utils as utils
from wandb.sdk.lib.runid import generate_id as generate_id

DEFAULT_LAUNCH_METADATA_PATH: str
RESOURCE_UID_MAP: Incomplete
IMAGE_TAG_MAX_LENGTH: int

class LaunchSource(enum.IntEnum):
    WANDB: int
    GIT: int
    LOCAL: int
    DOCKER: int
    JOB: int

class EntrypointDefaults(List[str]):
    PYTHON: Incomplete

class LaunchProject:
    """A launch project specification."""
    uri: Incomplete
    job: Incomplete
    api: Incomplete
    launch_spec: Incomplete
    target_entity: Incomplete
    target_project: Incomplete
    name: Incomplete
    resource: Incomplete
    resource_args: Incomplete
    sweep_id: Incomplete
    python_version: Incomplete
    accelerator_base_image: Incomplete
    docker_user_id: Incomplete
    git_version: Incomplete
    git_repo: Incomplete
    overrides: Incomplete
    override_args: Incomplete
    override_config: Incomplete
    override_artifacts: Incomplete
    override_entrypoint: Incomplete
    override_dockerfile: Incomplete
    deps_type: Incomplete
    run_id: Incomplete
    source: Incomplete
    project_dir: Incomplete
    aux_dir: Incomplete
    def __init__(self, uri: str | None, job: str | None, api: Api, launch_spec: Dict[str, Any], target_entity: str, target_project: str, name: str | None, docker_config: Dict[str, Any], git_info: Dict[str, str], overrides: Dict[str, Any], resource: str, resource_args: Dict[str, Any], run_id: str | None, sweep_id: str | None = None) -> None: ...
    @property
    def base_image(self) -> str:
        """Returns {PROJECT}_base:{PYTHON_VERSION}."""
    @property
    def image_name(self) -> str: ...
    def fill_macros(self, image: str) -> Dict[str, Any]:
        """Substitute values for macros in resource arguments.

        Certain macros can be used in resource args. These macros allow the
        user to set resource args dynamically in the context of the
        run being launched. The macros are given in the ${macro} format. The
        following macros are currently supported:

        ${project_name} - the name of the project the run is being launched to.
        ${entity_name} - the owner of the project the run being launched to.
        ${run_id} - the id of the run being launched.
        ${run_name} - the name of the run that is launching.
        ${image_uri} - the URI of the container image for this run.

        Additionally, you may use ${<ENV-VAR-NAME>} to refer to the value of any
        environment variables that you plan to set in the environment of any
        agents that will receive these resource args.

        Calling this method will overwrite the contents of self.resource_args
        with the substituted values.

        Args:
            image (str): The image name to fill in for ${wandb-image}.

        Returns:
            None
        """
    def build_required(self) -> bool:
        """Checks the source to see if a build is required."""
    @property
    def docker_image(self) -> str | None: ...
    @docker_image.setter
    def docker_image(self, value: str) -> None: ...
    def get_single_entry_point(self) -> EntryPoint | None:
        """Returns the first entrypoint for the project, or None if no entry point was provided because a docker image was provided."""
    def set_entry_point(self, command: List[str]) -> EntryPoint:
        """Add an entry point to the project."""
    def get_image_source_string(self) -> str:
        """Returns a unique string identifying the source of an image."""

class EntryPoint:
    """An entry point into a wandb launch specification."""
    name: Incomplete
    command: Incomplete
    def __init__(self, name: str | None, command: List[str]) -> None: ...
    def compute_command(self, user_parameters: List[str] | None) -> List[str]:
        """Converts user parameter dictionary to a string."""

def get_entry_point_command(entry_point: EntryPoint | None, parameters: List[str]) -> List[str]:
    """Returns the shell command to execute in order to run the specified entry point.

    Arguments:
    entry_point: Entry point to run
    parameters: Parameters (dictionary) for the entry point command

    Returns:
        List of strings representing the shell command to be executed
    """
def create_project_from_spec(launch_spec: Dict[str, Any], api: Api) -> LaunchProject:
    """Constructs a LaunchProject instance using a launch spec.

    Arguments:
    launch_spec: Dictionary representation of launch spec
    api: Instance of wandb.apis.internal Api

    Returns:
        An initialized `LaunchProject` object
    """
def fetch_and_validate_project(launch_project: LaunchProject, api: Api) -> LaunchProject:
    """Fetches a project into a local directory, adds the config values to the directory, and validates the first entrypoint for the project.

    Arguments:
    launch_project: LaunchProject to fetch and validate.
    api: Instance of wandb.apis.internal Api

    Returns:
        A validated `LaunchProject` object.

    """
def create_metadata_file(launch_project: LaunchProject, image_uri: str, sanitized_entrypoint_str: str, sanitized_dockerfile_contents: str) -> None: ...
