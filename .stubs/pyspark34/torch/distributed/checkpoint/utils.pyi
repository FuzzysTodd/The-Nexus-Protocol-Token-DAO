import torch
import torch.distributed as dist
from .metadata import MetadataIndex, STATE_DICT_TYPE
from _typeshed import Incomplete
from typing import Any, Callable, List, TypeVar

__all__ = ['find_tensor_shard', 'find_state_dict_object']

T = TypeVar('T')
R = TypeVar('R')

class _DistWrapper:
    """
    This is a wrapper around PG that provides a series of features around object collectives.

    It works without distributed initialized, where most collectives turns into nops.

    All variants that take functions are exception robust, meaning that if one or more
    ranks raise errors, all ranks will observe those.
    """
    group: Incomplete
    use_dist: Incomplete
    coordinator_rank: Incomplete
    rank: Incomplete
    is_coordinator: Incomplete
    def __init__(self, group: dist.ProcessGroup | None, use_dist: bool, coordinator_rank: int) -> None: ...
    def get_rank(self) -> int: ...
    def get_world_size(self) -> int: ...
    def broadcast_object(self, object: T | None) -> T:
        """
        Same as c10d::broadcast_object_list but works without distributed enabled.
        """
    def gather_object(self, object: T) -> List[T] | None:
        """
        Same as c10d::gather_object but works without distributed enabled.
        """
    def all_gather_object(self, object: T) -> List[T]:
        """
        Same as c10d::all_gather_object but works without distributed enabled.
        """
    def scatter_object(self, object_list: List[T] | None) -> T:
        """
        Same as c10d::scatter_object but works without distributed enabled.
        """
    def reduce_scatter(self, step: str, map_fun: Callable[[], T], reduce_fun: Callable[[List[T]], List[R]]) -> R:
        """
        Compute a value on each rank, then do centralized reduce on a single rank, followed by a scatter.

        This method operates in the following way:
            Run ``map_fun`` on all ranks
            Gather results on rank 0
            Call ``reduce_fun`` on all those values
            Scatter to each rank part of the result.
        """
    def all_reduce(self, step: str, map_fun: Callable[[], T], reduce_fun: Callable[[List[T]], R]) -> R:
        """
        Compute a value on each rank, then do centralized reduce on a single rank, followed by a broadcast.

        This method operates in the following way:
            Run ``map_fun`` on all ranks
            Gather results on rank 0
            Call ``reduce_fun`` on all those values
            Broadcast the reduced value to all ranks.
        """
    def all_gather(self, step: str, map_fun: Callable[[], T]) -> List[T]:
        """
        Compute a value on each rank, then all_gather them.

        This method operates in the following way:
            Run ``map_cp`` on all ranks
            all_gather the values to all ranks
        """
    def broadcast(self, step: str, map_fun: Callable[[], T]) -> T:
        """
        Compute a value on rank 0 and broadcast it.

        This method operates in the following way:
            Run ``map_cp`` on rank 0
            broadcast the value
        """

def find_tensor_shard(tensor: torch.Tensor, index: MetadataIndex) -> torch.Tensor: ...
def find_state_dict_object(state_dict: STATE_DICT_TYPE, index: MetadataIndex) -> Any: ...
