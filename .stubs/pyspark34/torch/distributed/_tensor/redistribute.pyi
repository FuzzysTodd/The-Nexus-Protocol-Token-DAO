import torch
import torch.distributed._tensor.api as dtensor
from torch.distributed._tensor.device_mesh import DeviceMesh as DeviceMesh
from torch.distributed._tensor.placement_types import Placement as Placement, Replicate as Replicate, Shard as Shard
from typing import List, Sequence

def redistribute_dtensor(input: dtensor.DTensor, device_mesh: DeviceMesh, placements: Sequence[Placement]) -> dtensor.DTensor: ...

class Redistribute(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input: dtensor.DTensor, device_mesh: DeviceMesh, placements: List[Placement]): ...
    @staticmethod
    def backward(ctx, grad_output: dtensor.DTensor): ...
