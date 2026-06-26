import torch
from _typeshed import Incomplete
from torch.distributed import distributed_c10d as distributed_c10d
from torch.distributed._shard.sharded_tensor.api import ShardedTensor as ShardedTensor
from torch.overrides import get_default_nowrap_functions as get_default_nowrap_functions

class ReplicatedTensor(torch.Tensor):
    """
    ReplicatedTensor represents a tensor which is replicated across the `world_size` and
    has the same value on each rank.

    ReplicatedTensor is a :class:`~torch.Tensor` subclass, and it could be used together
    with ShardedTensor/Tensor together to express different types of computation. The
    inter-op rules defined as (using torch.add as an example op):
        ReplicatedTensor + ReplicatedTensor = ReplicatedTensor
        ReplicatedTensor + torch.Tensor = torch.Tensor
        ReplicatedTensor + ShardedTensor = ShardedTensor
        ReplicatedTensor + other type (i.e. Scalar) = other type

    NOTE: We do not gurantee equal content of ReplicatedTensor across nodes after its
    construction. Although we defined proper inter-op rules to make sure ReplicatedTensor
    stays the same, there's no enforcement on it (i.e. if you manually modify content on
    some ranks, the modified value will not automatically get synced to other nodes). If
    you wish to manually validate tensors are the same across ranks, use `validate()`.

    """
    def __new__(cls, data: Incomplete | None = None, process_group: Incomplete | None = None): ...
    def __deepcopy__(self, memo): ...
    @classmethod
    def __torch_function__(cls, func, types, args=(), kwargs: Incomplete | None = None): ...
    def validate(self) -> bool:
        """
        Validate the ReplicatedTensor is legit by all gathering tensors on all ranks
        and check to make sure they are the same.

        If there's some ranks with different values, a ValueError will be raised.

        Keyword args:
            process_group (ProcessGroup, optional): The process group to work on. If None,
                the default process group will be used.

        Returns:
            True if validation succeed.
        """
