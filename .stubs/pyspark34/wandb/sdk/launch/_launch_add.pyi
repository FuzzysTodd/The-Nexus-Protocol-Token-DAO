import wandb.apis.public as public
from typing import Any, Dict, List
from wandb.apis.internal import Api as Api
from wandb.sdk.launch._project_spec import create_project_from_spec as create_project_from_spec
from wandb.sdk.launch.builder.build import build_image_from_project as build_image_from_project
from wandb.sdk.launch.errors import LaunchError as LaunchError
from wandb.sdk.launch.utils import LAUNCH_DEFAULT_PROJECT as LAUNCH_DEFAULT_PROJECT, LOG_PREFIX as LOG_PREFIX, construct_launch_spec as construct_launch_spec, validate_launch_spec_source as validate_launch_spec_source

def push_to_queue(api: Api, queue_name: str, launch_spec: Dict[str, Any], project_queue: str) -> Any: ...
def launch_add(uri: str | None = None, job: str | None = None, config: Dict[str, Any] | None = None, project: str | None = None, entity: str | None = None, queue_name: str | None = None, resource: str | None = None, entry_point: List[str] | None = None, name: str | None = None, version: str | None = None, docker_image: str | None = None, project_queue: str | None = None, resource_args: Dict[str, Any] | None = None, run_id: str | None = None, build: bool | None = False, repository: str | None = None, sweep_id: str | None = None, author: str | None = None) -> public.QueuedRun:
    '''Enqueue a W&B launch experiment. With either a source uri, job or docker_image.

    Arguments:
        uri: URI of experiment to run. A wandb run uri or a Git repository URI.
        job: string reference to a wandb.Job eg: wandb/test/my-job:latest
        config: A dictionary containing the configuration for the run. May also contain
            resource specific arguments under the key "resource_args"
        project: Target project to send launched run to
        entity: Target entity to send launched run to
        queue: the name of the queue to enqueue the run to
        resource: Execution backend for the run: W&B provides built-in support for "local-container" backend
        entry_point: Entry point to run within the project. Defaults to using the entry point used
            in the original run for wandb URIs, or main.py for git repository URIs.
        name: Name run under which to launch the run.
        version: For Git-based projects, either a commit hash or a branch name.
        docker_image: The name of the docker image to use for the run.
        resource_args: Resource related arguments for launching runs onto a remote backend.
            Will be stored on the constructed launch config under ``resource_args``.
        run_id: optional string indicating the id of the launched run
        build: optional flag defaulting to false, requires queue to be set
            if build, an image is created, creates a job artifact, pushes a reference
                to that job artifact to queue
        repository: optional string to control the name of the remote repository, used when
            pushing images to a registry
        project_queue: optional string to control the name of the project for the queue. Primarily used
            for back compatibility with project scoped queues


    Example:
    ```python
    from wandb.sdk.launch import launch_add

    project_uri = "https://github.com/wandb/examples"
    params = {"alpha": 0.5, "l1_ratio": 0.01}
    # Run W&B project and create a reproducible docker environment
    # on a local host
    api = wandb.apis.internal.Api()
    launch_add(uri=project_uri, parameters=params)
    ```


    Returns:
        an instance of`wandb.api.public.QueuedRun` which gives information about the
        queued run, or if `wait_until_started` or `wait_until_finished` are called, gives access
        to the underlying Run information.

    Raises:
        `wandb.exceptions.LaunchError` if unsuccessful
    '''
