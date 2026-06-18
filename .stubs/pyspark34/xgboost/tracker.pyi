import argparse
import socket
from _typeshed import Incomplete
from typing import Dict, List, Tuple

class ExSocket:
    """
    Extension of socket to handle recv and send of special data
    """
    sock: Incomplete
    def __init__(self, sock: socket.socket) -> None: ...
    def recvall(self, nbytes: int) -> bytes:
        """Receive number of bytes."""
    def recvint(self) -> int:
        """Receive an integer of 32 bytes"""
    def sendint(self, value: int) -> None:
        """Send an integer of 32 bytes"""
    def sendstr(self, value: str) -> None:
        """Send a Python string"""
    def recvstr(self) -> str:
        """Receive a Python string"""

MAGIC_NUM: int

def get_some_ip(host: str) -> str:
    """Get ip from host"""
def get_family(addr: str) -> int:
    """Get network family from address."""

class WorkerEntry:
    """Hanlder to each worker."""
    sock: Incomplete
    host: Incomplete
    rank: Incomplete
    world_size: Incomplete
    task_id: Incomplete
    cmd: Incomplete
    wait_accept: int
    port: Incomplete
    def __init__(self, sock: socket.socket, s_addr: Tuple[str, int]) -> None: ...
    def print(self, use_logger: bool) -> None:
        """Execute the print command from worker."""
    def decide_rank(self, job_map: Dict[str, int]) -> int:
        """Get the rank of current entry."""
    def assign_rank(self, rank: int, wait_conn: Dict[int, 'WorkerEntry'], tree_map: _TreeMap, parent_map: Dict[int, int], ring_map: _RingMap) -> List[int]:
        """Assign the rank for current entry."""

class RabitTracker:
    """
    tracker for rabit
    """
    port: Incomplete
    sock: Incomplete
    host_ip: Incomplete
    thread: Incomplete
    n_workers: Incomplete
    def __init__(self, host_ip: str, n_workers: int, port: int = 0, use_logger: bool = False, sortby: str = 'host') -> None:
        """A Python implementation of RABIT tracker.

        Parameters
        ..........
        use_logger:
            Use logging.info for tracker print command.  When set to False, Python print
            function is used instead.

        sortby:
            How to sort the workers for rank assignment. The default is host, but users
            can set the `DMLC_TASK_ID` via RABIT initialization arguments and obtain
            deterministic rank assignment. Available options are:
              - host
              - task

        """
    def __del__(self) -> None: ...
    def worker_envs(self) -> Dict[str, str | int]:
        """
        get environment variables for workers
        can be passed in as args or envs
        """
    def find_share_ring(self, tree_map: _TreeMap, parent_map: Dict[int, int], rank: int) -> List[int]:
        """
        get a ring structure that tends to share nodes with the tree
        return a list starting from rank
        """
    def get_ring(self, tree_map: _TreeMap, parent_map: Dict[int, int]) -> _RingMap:
        """
        get a ring connection used to recover local data
        """
    def get_link_map(self, n_workers: int) -> Tuple[_TreeMap, Dict[int, int], _RingMap]:
        """
        get the link map, this is a bit hacky, call for better algorithm
        to place similar nodes together
        """
    def accept_workers(self, n_workers: int) -> None:
        """Wait for all workers to connect to the tracker."""
    def start(self, n_workers: int) -> None:
        """Strat the tracker, it will wait for `n_workers` to connect."""
    def join(self) -> None:
        """Wait for the tracker to finish."""
    def alive(self) -> bool:
        """Wether the tracker thread is alive"""

def get_host_ip(host_ip: str | None = None) -> str:
    """Get the IP address of current host.  If `host_ip` is not none then it will be
    returned as it's

    """
def start_rabit_tracker(args: argparse.Namespace) -> None:
    """Standalone function to start rabit tracker.

    Parameters
    ----------
    args: arguments to start the rabit tracker.
    """
def main() -> None:
    """Main function if tracker is executed in standalone mode."""
