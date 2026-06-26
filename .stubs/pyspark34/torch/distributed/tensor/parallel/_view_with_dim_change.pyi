import torch
from torch.distributed._tensor import DTensor as DT
from torch.distributed._tensor.ops.utils import prod as prod
from torch.distributed._tensor.placement_types import Shard as Shard
from typing import Tuple

class _ViewAndRedistribute(torch.autograd.Function):
    @staticmethod
    def forward(ctx, self: DT, sharding_dim: int, shape: Tuple[int, ...]) -> DT: ...
    @staticmethod
    def backward(ctx, grad_output: DT) -> Tuple[DT, None, None]: ...
