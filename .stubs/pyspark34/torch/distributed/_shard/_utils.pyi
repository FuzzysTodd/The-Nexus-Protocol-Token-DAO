import torch
from torch.distributed._shard.metadata import ShardMetadata as ShardMetadata
from typing import Sequence

def narrow_tensor_by_index(tensor: torch.Tensor, offsets: Sequence[int], sizes: Sequence[int]) -> torch.Tensor:
    """
    Narrow the tensor according to ``offsets`` and ``sizes``.
    """
def narrow_tensor(tensor: torch.Tensor, metadata: ShardMetadata) -> torch.Tensor:
    """
    Narrow the tensor according to the metadata
    """
