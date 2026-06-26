from .._project_spec import EntryPoint as EntryPoint, EntrypointDefaults as EntrypointDefaults, LaunchProject as LaunchProject, fetch_and_validate_project as fetch_and_validate_project
from ..errors import ExecutionError as ExecutionError, LaunchError as LaunchError
from ..utils import LAUNCH_CONFIG_FILE as LAUNCH_CONFIG_FILE, LOG_PREFIX as LOG_PREFIX, resolve_build_and_registry_config as resolve_build_and_registry_config
from .abstract import AbstractBuilder as AbstractBuilder
from typing import Any, Dict, List, Tuple
from wandb.apis.internal import Api as Api
from wandb.sdk.launch.loader import builder_from_config as builder_from_config, environment_from_config as environment_from_config, registry_from_config as registry_from_config

def validate_docker_installation() -> None:
    """Verify if Docker is installed on host machine."""
def get_docker_user(launch_project: LaunchProject, runner_type: str) -> Tuple[str, int]: ...

DOCKERFILE_TEMPLATE: str
PYTHON_SETUP_TEMPLATE: str
ACCELERATOR_SETUP_TEMPLATE: str
PIP_TEMPLATE: str
CONDA_TEMPLATE: str
USER_CREATE_TEMPLATE: str
ENTRYPOINT_TEMPLATE: str

def get_current_python_version() -> Tuple[str, str]: ...
def get_base_setup(launch_project: LaunchProject, py_version: str, py_major: str) -> str:
    """Fill in the Dockerfile templates for stage 2 of build.

    CPU version is built on python, Accelerator version is built on user provided.
    """
def get_env_vars_dict(launch_project: LaunchProject, api: Api, max_env_length: int) -> Dict[str, str]:
    """Generate environment variables for the project.

    Arguments:
    launch_project: LaunchProject to generate environment variables for.

    Returns:
        Dictionary of environment variables.
    """
def get_requirements_section(launch_project: LaunchProject, builder_type: str) -> str: ...
def get_user_setup(username: str, userid: int, runner_type: str) -> str: ...
def get_entrypoint_setup(entry_point: EntryPoint) -> str: ...
def generate_dockerfile(launch_project: LaunchProject, entry_point: EntryPoint, runner_type: str, builder_type: str, dockerfile: str | None = None) -> str: ...
def construct_gcp_registry_uri(gcp_repo: str, gcp_project: str, gcp_registry: str) -> str: ...
def join(split_command: List[str]) -> str:
    '''Return a shell-escaped string from *split_command*.

    Also remove quotes from double quoted strings. Ex:
    "\'local container queue\'" --> "local container queue"
    '''
def construct_agent_configs(launch_config: Dict | None = None, build_config: Dict | None = None) -> Tuple[Dict[str, Any] | None, Dict[str, Any], Dict[str, Any]]: ...
def build_image_with_builder(builder: AbstractBuilder, launch_project: LaunchProject, entry_point: EntryPoint) -> str | None:
    """Build image with testing and logging."""
def build_image_from_project(launch_project: LaunchProject, api: Api, launch_config: Dict[str, Any]) -> str:
    """Construct a docker image from a project and returns the URI of the image.

    Arguments:
        launch_project: The project to build an image from.
        api: The API object to use for fetching the project.
        launch_config: The launch config to use for building the image.

    Returns:
        The URI of the built image.
    """
def image_tag_from_dockerfile_and_source(launch_project: LaunchProject, dockerfile_contents: str) -> str:
    """Hashes the source and dockerfile contents into a unique tag."""
