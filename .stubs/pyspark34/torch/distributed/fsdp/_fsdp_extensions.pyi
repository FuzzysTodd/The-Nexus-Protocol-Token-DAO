import abc
import torch
import torch.distributed as dist
from abc import ABC, abstractmethod
from torch.distributed._shard.sharded_tensor.api import ShardedTensor as ShardedTensor
from torch.distributed._shard.sharded_tensor.shard import Shard as Shard
from typing import Any, List, Tuple

class FSDPExtensions(ABC, metaclass=abc.ABCMeta):
    """
    This enables some customizable hooks to enable composability with tensor
    parallelism. To activate these hooks, use :func:`_set_fsdp_extensions` to
    set a custom :class:`FSDPExtensions` that implements the hooks.
    """
    @abstractmethod
    def pre_flatten_transform(self, tensor: torch.Tensor) -> Tuple[torch.Tensor, Any | None]:
        """E.g. converting ``DistributedTensor`` to local tensor."""
    @abstractmethod
    def post_unflatten_transform(self, tensor: torch.Tensor, param_extension: Any) -> torch.Tensor:
        """E.g. converting local tensor to ``DistributedTensor``."""
    @abstractmethod
    def chunk_tensor(self, tensor: torch.Tensor, rank: int, world_size: int, num_devices_per_node: int, pg: dist.ProcessGroup) -> torch.Tensor:
        """Shards a tensor to chunks and returns the local chunk."""
    @abstractmethod
    def pre_load_state_dict_transform(self, tensor: torch.Tensor) -> Tuple[torch.Tensor, List[Shard]]:
        """
        This is to be called before loading a *sharded* model state dict and
        should return the tensor and list of shards from which to load data.
        """
