import numpy as np
from ._typing import _T
from .core import c_str as c_str, from_pystr_to_cstr as from_pystr_to_cstr, py_str as py_str
from _typeshed import Incomplete
from enum import IntEnum
from typing import Any, Dict, List

LOGGER: Incomplete

def init(**args: Any) -> None:
    '''Initialize the collective library with arguments.

    Parameters
    ----------
    args: Dict[str, Any]
        Keyword arguments representing the parameters and their values.

        Accepted parameters:
          - xgboost_communicator: The type of the communicator. Can be set as an environment
            variable.
            * rabit: Use Rabit. This is the default if the type is unspecified.
            * federated: Use the gRPC interface for Federated Learning.
        Only applicable to the Rabit communicator (these are case sensitive):
          -- rabit_tracker_uri: Hostname of the tracker.
          -- rabit_tracker_port: Port number of the tracker.
          -- rabit_task_id: ID of the current task, can be used to obtain deterministic rank
             assignment.
          -- rabit_world_size: Total number of workers.
          -- rabit_hadoop_mode: Enable Hadoop support.
          -- rabit_tree_reduce_minsize: Minimal size for tree reduce.
          -- rabit_reduce_ring_mincount: Minimal count to perform ring reduce.
          -- rabit_reduce_buffer: Size of the reduce buffer.
          -- rabit_bootstrap_cache: Size of the bootstrap cache.
          -- rabit_debug: Enable debugging.
          -- rabit_timeout: Enable timeout.
          -- rabit_timeout_sec: Timeout in seconds.
          -- rabit_enable_tcp_no_delay: Enable TCP no delay on Unix platforms.
        Only applicable to the Rabit communicator (these are case-sensitive, and can be set as
        environment variables):
          -- DMLC_TRACKER_URI: Hostname of the tracker.
          -- DMLC_TRACKER_PORT: Port number of the tracker.
          -- DMLC_TASK_ID: ID of the current task, can be used to obtain deterministic rank
             assignment.
          -- DMLC_ROLE: Role of the current task, "worker" or "server".
          -- DMLC_NUM_ATTEMPT: Number of attempts after task failure.
          -- DMLC_WORKER_CONNECT_RETRY: Number of retries to connect to the tracker.
        Only applicable to the Federated communicator (use upper case for environment variables, use
        lower case for runtime configuration):
          -- federated_server_address: Address of the federated server.
          -- federated_world_size: Number of federated workers.
          -- federated_rank: Rank of the current worker.
          -- federated_server_cert: Server certificate file path. Only needed for the SSL mode.
          -- federated_client_key: Client key file path. Only needed for the SSL mode.
          -- federated_client_cert: Client certificate file path. Only needed for the SSL mode.
    '''
def finalize() -> None:
    """Finalize the communicator."""
def get_rank() -> int:
    """Get rank of current process.

    Returns
    -------
    rank : int
        Rank of current process.
    """
def get_world_size() -> int:
    """Get total number workers.

    Returns
    -------
    n : int
        Total number of process.
    """
def is_distributed() -> int:
    """If the collective communicator is distributed."""
def communicator_print(msg: Any) -> None:
    """Print message to the communicator.

    This function can be used to communicate the information of
    the progress to the communicator.

    Parameters
    ----------
    msg : str
        The message to be printed to the communicator.
    """
def get_processor_name() -> str:
    """Get the processor name.

    Returns
    -------
    name : str
        the name of processor(host)
    """
def broadcast(data: _T, root: int) -> _T:
    """Broadcast object from one node to all other nodes.

    Parameters
    ----------
    data : any type that can be pickled
        Input data, if current rank does not equal root, this can be None
    root : int
        Rank of the node to broadcast data from.

    Returns
    -------
    object : int
        the result of broadcast.
    """

DTYPE_ENUM__: Incomplete

class Op(IntEnum):
    """Supported operations for allreduce."""
    MAX: int
    MIN: int
    SUM: int

def allreduce(data: np.ndarray, op: Op) -> np.ndarray:
    """Perform allreduce, return the result.

    Parameters
    ----------
    data :
        Input data.
    op :
        Reduction operator.

    Returns
    -------
    result :
        The result of allreduce, have same shape as data

    Notes
    -----
    This function is not thread-safe.
    """

class CommunicatorContext:
    """A context controlling collective communicator initialization and finalization."""
    args: Incomplete
    def __init__(self, **args: Any) -> None: ...
    def __enter__(self) -> Dict[str, Any]: ...
    def __exit__(self, *args: List) -> None: ...
