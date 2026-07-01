import abc
import torch.distributed.elastic.rendezvous as rdzv
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum
from torch.distributed.elastic.events import Event
from torch.distributed.elastic.multiprocessing import ProcessFailure, Std
from typing import Any, Callable, Dict, List, Tuple

__all__ = ['WorkerSpec', 'Worker', 'WorkerState', 'WorkerGroup', 'RunResult', 'ElasticAgent', 'SimpleElasticAgent']

@dataclass
class WorkerSpec:
    """
    Contains blueprint information about a particular type of worker.
    For a given role, there must only exist a single worker spec.
    Worker spec is expected to be homogenous across all nodes (machine),
    that is each node runs the same number of workers for a particular spec.

    Args:
        role: user-defined role for the workers with this spec
        local_world_size: number local workers to run
        fn: (deprecated use entrypoint instead)
        entrypoint: worker function or command
        args: arguments to pass to ``entrypoint``
        rdzv_handler: handles rdzv for this set of workers
        max_restarts: number of max retries for the workers
        monitor_interval: monitor status of workers every ``n`` seconds
        master_port: fixed port to run the c10d store on rank 0
                     if not specified then will chose a random free port
        master_addr: fixed master_addr to run the c10d store on rank 0
                     if not specified then will chose hostname on agent rank 0
        redirects: redirect std streams to a file,
                   selectively redirect for a particular
                   local rank by passing a map
        tee: tees the specified std stream(s) to console + file,
             selectively tee for a particular local rank by passing a map,
             takes precedence over ``redirects`` settings.

    """
    role: str
    local_world_size: int
    rdzv_handler: rdzv.RendezvousHandler
    fn: Callable | None = ...
    entrypoint: Callable | str | None = ...
    args: Tuple = ...
    max_restarts: int = ...
    monitor_interval: float = ...
    master_port: int | None = ...
    master_addr: str | None = ...
    local_addr: str | None = ...
    redirects: Std | Dict[int, Std] = ...
    tee: Std | Dict[int, Std] = ...
    def __post_init__(self) -> None: ...
    def get_entrypoint_name(self):
        """
        If the entrypoint is a function (e.g. ``Callable``) returns its ``__qualname__``,
        else if the entrypoint is a binary (e.g. ``str``), returns the binary name.
        """
    def __init__(self, role, local_world_size, rdzv_handler, fn, entrypoint, args, max_restarts, monitor_interval, master_port, master_addr, local_addr, redirects, tee) -> None: ...

class Worker:
    """
    Represents a worker instance. Contrast this with ``WorkerSpec`` that
    represents the specifications of a worker. A ``Worker`` is created from
    a ``WorkerSpec``. A ``Worker`` is to a ``WorkerSpec`` as an object is to
    a class.

    The ``id`` of the worker is interpreted
    by the specific implementation of ``ElasticAgent``. For a local
    agent, it could be the ``pid (int)`` of the worker, for a remote
    agent it could be encoded as ``host:port (string)``.

    Args:
        id (Any): uniquely identifies a worker (interpreted by the agent)
        local_rank (int): local rank of the worker
        global_rank (int): global rank of the worker
        role_rank (int): rank of the worker across all workers that have the same role
        world_size (int): number of workers (globally)
        role_world_size (int): number of workers that have the same role
    """
    id: Incomplete
    local_rank: Incomplete
    global_rank: Incomplete
    role_rank: Incomplete
    world_size: Incomplete
    role_world_size: Incomplete
    def __init__(self, local_rank: int, global_rank: int = -1, role_rank: int = -1, world_size: int = -1, role_world_size: int = -1) -> None: ...

class WorkerState(str, Enum):
    """
    State of the ``WorkerGroup``. Workers in a worker group change state as a unit.
    If a single worker in a worker group fails the entire set is considered
    failed::

      UNKNOWN - agent lost track of worker group state, unrecoverable
      INIT - worker group object created not yet started
      HEALTHY - workers running and healthy
      UNHEALTHY - workers running and unhealthy
      STOPPED - workers stopped (interrupted) by the agent
      SUCCEEDED - workers finished running (exit 0)
      FAILED - workers failed to successfully finish (exit !0)


    A worker group starts from an initial ``INIT`` state,
    then progresses to ``HEALTHY`` or ``UNHEALTHY`` states,
    and finally reaches a terminal ``SUCCEEDED`` or ``FAILED`` state.

    Worker groups can be interrupted and temporarily put into ``STOPPED`` state
    by the agent. Workers in ``STOPPED`` state are scheduled to be restarted
    in the near future by the agent. Some examples of workers being put into
    ``STOPPED`` state are:

    1. Worker group failure|unhealthy observed
    2. Membership change detected

    When actions (start, stop, rdzv, retry, etc) on worker group fails
    and results in the action being partially applied to the worker group
    the state will be ``UNKNOWN``. Typically this happens on uncaught/unhandled
    exceptions during state change events on the agent. The agent is not
    expected to recover worker groups in ``UNKNOWN`` state and is better off
    self terminating and allowing the job manager to retry the node.
    """
    UNKNOWN: str
    INIT: str
    HEALTHY: str
    UNHEALTHY: str
    STOPPED: str
    SUCCEEDED: str
    FAILED: str
    @staticmethod
    def is_running(state: WorkerState) -> bool:
        """
        Returns:
             True if the worker state represents workers still running
             (e.g. that the process exists but not necessarily healthy).
        """

class WorkerGroup:
    """
    Represents the set of ``Worker`` instances for the given ``WorkerSpec``
    managed by ``ElasticAgent``. Whether the worker group contains cross
    instance workers or not depends on the implementation of the agent.
    """
    spec: Incomplete
    workers: Incomplete
    store: Incomplete
    group_rank: Incomplete
    group_world_size: Incomplete
    state: Incomplete
    def __init__(self, spec: WorkerSpec) -> None: ...

class _RoleInstanceInfo:
    """
    The class is used by the agent to exchange the information with other agents.
    The information is used to determine the rank of the workers that agent
    manages in heterogeneous environments, where different agents can have
    different number of workers.
    """
    role: Incomplete
    rank: Incomplete
    local_world_size: Incomplete
    def __init__(self, role: str, rank: int, local_world_size: int) -> None:
        """

        Args:
            role (str): user-defined role for the workers with this spec
            rank (int): the rank of the agent
            local_world_size (int): number of local workers to run
        """
    def serialize(self) -> bytes: ...
    @staticmethod
    def deserialize(data: bytes): ...
    @staticmethod
    def compare(obj1, obj2) -> int: ...
    @staticmethod
    def find_role_boundaries(roles_infos: List, role: str) -> Tuple[int, int]: ...

@dataclass
class RunResult:
    '''
    Results returned by the worker executions. Run results follow an "all-or-nothing" policy
    where the run is successful if and only if ALL local workers managed by this agent
    complete successfully.

    If the result is successful (e.g. ``is_failed() = False``) then the ``return_values``
    field contains the outputs (return values) of the workers managed by THIS agent mapped
    by their GLOBAL ranks. That is ``result.return_values[0]`` is the return value of
    global rank 0.

    .. note:: ``return_values`` are only meaningful for when the worker entrypoint
              is a function. Workers specified as a binary entrypoint do not canonically
              have a return value and the ``return_values`` field is meaningless and
              may be empty.

    If ``is_failed()`` returns ``True`` then the ``failures`` field contains the
    failure information, again, mapped by the GLOBAL rank of the worker that failed.

    The keys in ``return_values`` and ``failures`` are mutually exclusive, that is,
    a worker\'s final state can only be one of: succeeded, failed. Workers intentionally
    terminated by the agent according to the agent\'s restart policy, are not represented
    in either ``return_values`` nor ``failures``.
    '''
    state: WorkerState
    return_values: Dict[int, Any] = ...
    failures: Dict[int, ProcessFailure] = ...
    def is_failed(self) -> bool: ...
    def __init__(self, state, return_values, failures) -> None: ...

class ElasticAgent(abc.ABC, metaclass=abc.ABCMeta):
    '''
    Agent process responsible for managing one or more worker processes.
    The worker processes are assumed to be regular distributed PyTorch scripts.
    When the worker process is created by the agent, the agent provides the
    necessary information for the worker processes to properly initialize
    a torch process group.

    The exact deployment topology and ratio of agent-to-worker is dependent
    on the specific implementation of the agent and the user\'s job placement
    preferences. For instance, to run a distributed training job on GPU with
    8 trainers (one per GPU) one can:

    1. Use 8 x single GPU instances, place an agent per instance, managing
       1 worker per agent.
    2. Use 4 x double GPU instances, place an agent per instance, managing
       2 workers per agent.
    3. Use 2 x quad GPU instances, place an agent per instance, managing
       4 workers per agent.
    4. Use 1 x 8 GPU instance, place an agent per instance, managing
       8 workers per agent.

    Usage
    ::

     group_result = agent.run()
      if group_result.is_failed():
        # workers failed
        failure = group_result.failures[0]
        log.exception(f"worker 0 failed with exit code : {failure.exit_code}")
      else:
        return group_result.return_values[0] # return rank 0\'s results

    '''
    @abc.abstractmethod
    def run(self, role: str = ...) -> RunResult:
        """
        Runs the agent, retrying the worker group on failures up to
        ``max_restarts``.

        Returns:
            The result of the execution, containing the return values or
            failure details for each worker mapped by the worker's global rank.

        Raises:
            Exception - any other failures NOT related to worker process
        """
    @abc.abstractmethod
    def get_worker_group(self, role: str = ...) -> WorkerGroup:
        """
        Returns:
            The ``WorkerGroup`` for the given ``role``.
            Note that the worker group is a mutable object and hence in a
            multi-threaded/process environment it may change state.
            Implementors are encouraged (but not required) to return
            a defensive read-only copy.
        """

class SimpleElasticAgent(ElasticAgent, metaclass=abc.ABCMeta):
    """
    An ``ElasticAgent`` that manages workers (``WorkerGroup``)
    for a single ``WorkerSpec`` (e.g. one particular type of worker role).
    """
    def __init__(self, spec: WorkerSpec, exit_barrier_timeout: float = 300) -> None: ...
    def get_worker_group(self, role: str = ...) -> WorkerGroup: ...
    def run(self, role: str = ...) -> RunResult: ...
    def get_event_failed(self) -> Event: ...
    def get_event_succeeded(self) -> Event: ...
