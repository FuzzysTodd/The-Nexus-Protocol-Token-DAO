import torch
from _typeshed import Incomplete
from torch.distributed._shard import sharded_tensor as sharded_tensor
from torch.distributed._shard.sharding_spec import ChunkShardingSpec as ChunkShardingSpec

PLACEMENTS: Incomplete
DEFAULT_GPU_NUM: int

class MyShardedModel2(torch.nn.Module):
    sharded_tensor2: Incomplete
    random_tensor2: Incomplete
    def __init__(self, spec: Incomplete | None = None, group: Incomplete | None = None, init_rrefs: bool = True) -> None: ...

class MyShardedModel1(torch.nn.Module):
    sharded_tensor1: Incomplete
    random_tensor1: Incomplete
    submodule: Incomplete
    def __init__(self, spec: Incomplete | None = None, group: Incomplete | None = None, init_rrefs: bool = True) -> None: ...
