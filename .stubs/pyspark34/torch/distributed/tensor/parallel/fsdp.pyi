import torch
import torch.distributed._shard.sharding_spec as shard_spec
import torch.distributed.distributed_c10d as c10d
from torch.distributed._tensor import DeviceMesh
from torch.distributed._tensor.placement_types import Placement
from typing import List, NamedTuple

__all__ = ['enable_2d_with_fsdp']

def enable_2d_with_fsdp() -> bool:
    """
    The API registers the extension which is needed for Tensor Parallelism (TP)
    to work with FullyShardedDataParallel (FSDP). We first parallelize parameters
    within one module or sub_modules based on a parallelize_plan and will let FSDP
    reshard the local tensor of distributed parameter which is essentially a DTensor.

    Return:
        A `bool` indicated whether extension registration succeeds or not.
    """

class _STShardingInfo(NamedTuple):
    """:class:`ShardedTensor` sharding information."""
    sharding_spec: shard_spec.ShardingSpec | None
    global_size: torch.Size | None
    process_group: c10d.ProcessGroup | None
    device_mesh: DeviceMesh | None
    placements: List[Placement] | None
