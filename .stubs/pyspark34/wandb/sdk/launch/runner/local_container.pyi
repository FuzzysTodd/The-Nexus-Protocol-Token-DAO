import subprocess
import threading
from .._project_spec import LaunchProject as LaunchProject
from ..builder.build import get_env_vars_dict as get_env_vars_dict
from ..errors import LaunchError as LaunchError
from ..utils import LOG_PREFIX as LOG_PREFIX, MAX_ENV_LENGTHS as MAX_ENV_LENGTHS, PROJECT_SYNCHRONOUS as PROJECT_SYNCHRONOUS, docker_image_exists as docker_image_exists, pull_docker_image as pull_docker_image, sanitize_wandb_api_key as sanitize_wandb_api_key
from .abstract import AbstractRun as AbstractRun, AbstractRunner as AbstractRunner, Status as Status
from _typeshed import Incomplete
from typing import Any, Dict, List
from wandb.apis.internal import Api as Api
from wandb.sdk.launch.environment.abstract import AbstractEnvironment as AbstractEnvironment
from wandb.sdk.launch.registry.abstract import AbstractRegistry as AbstractRegistry

class LocalSubmittedRun(AbstractRun):
    """Instance of ``AbstractRun`` corresponding to a subprocess launched to run an entry point command locally."""
    def __init__(self) -> None: ...
    def set_command_proc(self, command_proc: subprocess.Popen) -> None: ...
    def set_thread(self, thread: threading.Thread) -> None: ...
    @property
    def id(self) -> str | None: ...
    def wait(self) -> bool: ...
    def get_logs(self) -> str | None: ...
    def cancel(self) -> None: ...
    def get_status(self) -> Status: ...

class LocalContainerRunner(AbstractRunner):
    """Runner class, uses a project to create a LocallySubmittedRun."""
    environment: Incomplete
    registry: Incomplete
    def __init__(self, api: Api, backend_config: Dict[str, Any], environment: AbstractEnvironment, registry: AbstractRegistry) -> None: ...
    def run(self, launch_project: LaunchProject, image_uri: str) -> AbstractRun | None: ...

def get_docker_command(image: str, env_vars: Dict[str, str], entry_cmd: List[str] | None = None, docker_args: Dict[str, Any] | None = None, additional_args: List[str] | None = None) -> List[str]:
    """Construct the docker command using the image and docker args.

    Arguments:
    image: a Docker image to be run
    env_vars: a dictionary of environment variables for the command
    entry_cmd: the entry point command to run
    docker_args: a dictionary of additional docker args for the command
    """
def join(split_command: List[str]) -> str:
    """Return a shell-escaped string from *split_command*."""
