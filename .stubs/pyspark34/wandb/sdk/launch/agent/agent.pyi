from .. import loader as loader
from .._project_spec import create_project_from_spec as create_project_from_spec, fetch_and_validate_project as fetch_and_validate_project
from ..builder.build import construct_agent_configs as construct_agent_configs
from ..errors import LaunchDockerError as LaunchDockerError, LaunchError as LaunchError
from ..utils import LAUNCH_DEFAULT_PROJECT as LAUNCH_DEFAULT_PROJECT, LOG_PREFIX as LOG_PREFIX, PROJECT_SYNCHRONOUS as PROJECT_SYNCHRONOUS
from .job_status_tracker import JobAndRunStatusTracker as JobAndRunStatusTracker
from .run_queue_item_file_saver import RunQueueItemFileSaver as RunQueueItemFileSaver
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Dict, List
from wandb.apis.internal import Api as Api
from wandb.errors import CommError as CommError
from wandb.sdk.launch._launch_add import launch_add as launch_add
from wandb.sdk.launch.runner.local_container import LocalSubmittedRun as LocalSubmittedRun
from wandb.sdk.launch.runner.local_process import LocalProcessRunner as LocalProcessRunner
from wandb.sdk.launch.sweeps.scheduler import Scheduler as Scheduler
from wandb.sdk.lib import runid as runid

AGENT_POLLING_INTERVAL: int
RECEIVED_JOB_POLLING_INTERVAL: int
AGENT_POLLING: str
AGENT_RUNNING: str
AGENT_KILLED: str
HIDDEN_AGENT_RUN_TYPE: str
MAX_RESUME_COUNT: int
RUN_INFO_GRACE_PERIOD: int
MAX_WAIT_RUN_STOPPED: int
RUN_START_TIMEOUT: Incomplete

@dataclass
class JobSpecAndQueue:
    job: Dict[str, Any]
    queue: str
    def __init__(self, job, queue) -> None: ...

class LaunchAgent:
    """Launch agent class which polls run given run queues and launches runs for wandb launch."""
    default_config: Incomplete
    version: Incomplete
    gorilla_supports_agents: Incomplete
    def __init__(self, api: Api, config: Dict[str, Any]) -> None:
        """Initialize a launch agent.

        Arguments:
            api: Api object to use for making requests to the backend.
            config: Config dictionary for the agent.
        """
    def fail_run_queue_item(self, run_queue_item_id: str, message: str, phase: str, files: List[str] | None = None) -> None: ...
    @property
    def thread_ids(self) -> List[int]:
        """Returns a list of keys running thread ids for the agent."""
    @property
    def num_running_schedulers(self) -> int:
        """Return just the number of schedulers."""
    @property
    def num_running_jobs(self) -> int:
        """Return the number of jobs not including schedulers."""
    def pop_from_queue(self, queue: str) -> Any:
        """Pops an item off the runqueue to run as a job.

        Arguments:
            queue: Queue to pop from.

        Returns:
            Item popped off the queue.

        Raises:
            Exception: if there is an error popping from the queue.
        """
    def print_status(self) -> None:
        """Prints the current status of the agent."""
    def update_status(self, status: str) -> None:
        """Update the status of the agent.

        Arguments:
            status: Status to update the agent to.
        """
    def finish_thread_id(self, thread_id: int, exception: Exception | LaunchDockerError | None = None) -> None:
        """Removes the job from our list for now."""
    def run_job(self, job: Dict[str, Any], queue: str, file_saver: RunQueueItemFileSaver) -> None:
        """Set up project and run the job.

        Arguments:
            job: Job to run.
        """
    def loop(self) -> None:
        """Loop infinitely to poll for jobs and run them.

        Raises:
            KeyboardInterrupt: if the agent is requested to stop.
        """
    def thread_run_job(self, launch_spec: Dict[str, Any], job: Dict[str, Any], default_config: Dict[str, Any], api: Api, job_tracker: JobAndRunStatusTracker) -> None: ...
    def get_job_and_queue(self) -> JobSpecAndQueue | None: ...
