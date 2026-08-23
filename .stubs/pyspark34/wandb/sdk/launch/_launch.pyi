from . import loader as loader
from ._project_spec import create_project_from_spec as create_project_from_spec, fetch_and_validate_project as fetch_and_validate_project
from .agent import LaunchAgent as LaunchAgent
from .builder.build import construct_agent_configs as construct_agent_configs
from .errors import ExecutionError as ExecutionError, LaunchError as LaunchError
from .runner.abstract import AbstractRun as AbstractRun
from .utils import LAUNCH_CONFIG_FILE as LAUNCH_CONFIG_FILE, LAUNCH_DEFAULT_PROJECT as LAUNCH_DEFAULT_PROJECT, PROJECT_SYNCHRONOUS as PROJECT_SYNCHRONOUS, construct_launch_spec as construct_launch_spec, validate_launch_spec_source as validate_launch_spec_source
from typing import Any, Dict, List, Tuple
from wandb.apis.internal import Api as Api

def resolve_agent_config(entity: str | None, project: str | None, max_jobs: int | None, queues: Tuple[str] | None, config: str | None) -> Tuple[Dict[str, Any], Api]:
    """Resolve the agent config.

    Arguments:
        api (Api): The api.
        entity (str): The entity.
        project (str): The project.
        max_jobs (int): The max number of jobs.
        queues (Tuple[str]): The queues.
        config (str): The config.

    Returns:
        Tuple[Dict[str, Any], Api]: The resolved config and api.
    """
def create_and_run_agent(api: Api, config: Dict[str, Any]) -> None: ...
def launch(api: Api, job: str | None = None, entry_point: List[str] | None = None, version: str | None = None, name: str | None = None, resource: str | None = None, resource_args: Dict[str, Any] | None = None, project: str | None = None, entity: str | None = None, docker_image: str | None = None, config: Dict[str, Any] | None = None, synchronous: bool | None = True, run_id: str | None = None, repository: str | None = None) -> AbstractRun:
    '''Launch a W&B launch experiment.

    Arguments:
        job: string reference to a wandb.Job eg: wandb/test/my-job:latest
        api: An instance of a wandb Api from wandb.apis.internal.
        entry_point: Entry point to run within the project. Defaults to using the entry point used
            in the original run for wandb URIs, or main.py for git repository URIs.
        version: For Git-based projects, either a commit hash or a branch name.
        name: Name run under which to launch the run.
        resource: Execution backend for the run.
        resource_args: Resource related arguments for launching runs onto a remote backend.
            Will be stored on the constructed launch config under ``resource_args``.
        project: Target project to send launched run to
        entity: Target entity to send launched run to
        config: A dictionary containing the configuration for the run. May also contain
        resource specific arguments under the key "resource_args".
        synchronous: Whether to block while waiting for a run to complete. Defaults to True.
            Note that if ``synchronous`` is False and ``backend`` is "local-container", this
            method will return, but the current process will block when exiting until
            the local run completes. If the current process is interrupted, any
            asynchronous runs launched via this method will be terminated. If
            ``synchronous`` is True and the run fails, the current process will
            error out as well.
        run_id: ID for the run (To ultimately replace the :name: field)
        repository: string name of repository path for remote registry

    Example:
        ```python
        from wandb.sdk.launch import launch

        job = "wandb/jobs/Hello World:latest"
        params = {"epochs": 5}
        # Run W&B project and create a reproducible docker environment
        # on a local host
        api = wandb.apis.internal.Api()
        launch(api, job, parameters=params)
        ```


    Returns:
        an instance of`wandb.launch.SubmittedRun` exposing information (e.g. run ID)
        about the launched run.

    Raises:
        `wandb.exceptions.ExecutionError` If a run launched in blocking mode
        is unsuccessful.
    '''
