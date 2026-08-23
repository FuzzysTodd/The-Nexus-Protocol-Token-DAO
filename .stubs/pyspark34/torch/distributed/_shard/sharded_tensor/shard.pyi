import torch
from dataclasses import dataclass
from torch.distributed._shard.metadata import ShardMetadata as ShardMetadata
from typing import List

@dataclass
class Shard:
    """
    Container which holds the data for a shard as a Tensor and also
    the associated metadata for that shard.

    Args:
        tensor(torch.Tensor): Local tensor for the shard.
        metadata(:class `torch.distributed._shard.sharded_tensor.ShardMetadata`):
            The metadata for the shard, including offsets, lengths and device placement.
    """
    tensor: torch.Tensor
    metadata: ShardMetadata
    def __post_init__(self) -> None: ...
    @classmethod
    def from_tensor_and_offsets(cls, tensor: torch.Tensor, shard_offsets: List[int], rank: int):
        """
        Creates a Shard of a ShardedTensor from a local torch.Tensor, shard_offsets and rank.

        Args:
            tensor(torch.Tensor): Local tensor for the shard.
            shard_offsets(List[int]): List of integers specify the offset
                of the shard on each dimension.
            rank(int): Specify the rank for the shard.
        """
    def __init__(self, tensor, metadata) -> None: ...
