import abc
import wandb.apis.public as public
from _typeshed import Incomplete
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List
from wandb.apis.internal import Api as Api
from wandb.apis.public import QueuedRun as QueuedRun, Run as Run
from wandb.errors import CommError as CommError
from wandb.sdk.launch._launch_add import launch_add as launch_add
from wandb.sdk.launch.errors import LaunchError as LaunchError
from wandb.sdk.launch.sweeps import SchedulerError as SchedulerError
from wandb.sdk.launch.sweeps.utils import create_sweep_command_args as create_sweep_command_args, make_launch_sweep_entrypoint as make_launch_sweep_entrypoint
from wandb.sdk.lib.runid import generate_id as generate_id

LOG_PREFIX: Incomplete
DEFAULT_POLLING_SLEEP: float

class SchedulerState(Enum):
    PENDING: int
    STARTING: int
    RUNNING: int
    FLUSH_RUNS: int
    COMPLETED: int
    FAILED: int
    STOPPED: int
    CANCELLED: int

class RunState(Enum):
    RUNNING: Incomplete
    PENDING: Incomplete
    PREEMPTING: Incomplete
    CRASHED: Incomplete
    FAILED: Incomplete
    KILLED: Incomplete
    FINISHED: Incomplete
    PREEMPTED: Incomplete
    UNKNOWN: Incomplete
    def __new__(cls, *args: List, **kwds: Any) -> RunState: ...
    def __init__(self, _: str, life: str = 'unknown') -> None: ...
    @property
    def is_alive(self) -> bool: ...

@dataclass
class _Worker:
    agent_config: Dict[str, Any]
    agent_id: str
    def __init__(self, agent_config, agent_id) -> None: ...

@dataclass
class SweepRun:
    id: str
    worker_id: int
    state: RunState = ...
    queued_run: public.QueuedRun | None = ...
    args: Dict[str, Any] | None = ...
    logs: List[str] | None = ...
    def __init__(self, id, worker_id, state, queued_run, args, logs) -> None: ...

class Scheduler(ABC, metaclass=abc.ABCMeta):
    """A controller/agent that populates a Launch RunQueue from a hyperparameter sweep."""
    PLACEHOLDER_URI: str
    SWEEP_JOB_TYPE: str
    ENTRYPOINT: Incomplete
    def __init__(self, api: Api, *args: Any | None, polling_sleep: float | None = None, sweep_id: str | None = None, entity: str | None = None, project: str | None = None, project_queue: str | None = None, num_workers: int | str | None = None, **kwargs: Any | None) -> None: ...
    @property
    def state(self) -> SchedulerState: ...
    @state.setter
    def state(self, value: SchedulerState) -> None: ...
    @property
    def is_alive(self) -> bool: ...
    @property
    def at_runcap(self) -> bool:
        """False if under user-specified cap on # of runs."""
    @property
    def num_active_runs(self) -> int: ...
    @property
    def busy_workers(self) -> Dict[int, _Worker]:
        """Returns dict of id:worker already assigned to a launch run.

        runs should always have a worker_id, but are created before
        workers are assigned to the run
        """
    @property
    def available_workers(self) -> Dict[int, _Worker]:
        """Returns dict of id:worker ready to launch another run."""
    def stop_sweep(self) -> None:
        """Stop the sweep."""
    def fail_sweep(self, err: str | None) -> None:
        """Fail the sweep w/ optional exception."""
    def start(self) -> None:
        """Start a scheduler, confirms prerequisites, begins execution loop."""
    def run(self) -> None:
        """Main run function."""
    def exit(self) -> None: ...
