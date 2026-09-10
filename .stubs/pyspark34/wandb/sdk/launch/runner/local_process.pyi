from .._project_spec import LaunchProject as LaunchProject, get_entry_point_command as get_entry_point_command
from ..builder.build import get_env_vars_dict as get_env_vars_dict
from ..errors import LaunchError as LaunchError
from ..utils import LOG_PREFIX as LOG_PREFIX, MAX_ENV_LENGTHS as MAX_ENV_LENGTHS, PROJECT_SYNCHRONOUS as PROJECT_SYNCHRONOUS, download_wandb_python_deps as download_wandb_python_deps, parse_wandb_uri as parse_wandb_uri, sanitize_wandb_api_key as sanitize_wandb_api_key, validate_wandb_python_deps as validate_wandb_python_deps
from .abstract import AbstractRun as AbstractRun, AbstractRunner as AbstractRunner

class LocalProcessRunner(AbstractRunner):
    """Runner class, uses a project to create a LocallySubmittedRun.

    LocalProcessRunner is very similar to a LocalContainerRunner, except it does not
    run the command inside a docker container. Instead, it runs the
    command specified as a process directly on the bare metal machine.

    """
    def run(self, launch_project: LaunchProject, *args, **kwargs) -> AbstractRun | None: ...
