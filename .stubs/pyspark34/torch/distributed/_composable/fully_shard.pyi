import torch
import torch.distributed as dist
import torch.nn as nn
from torch.distributed._composable.contract import contract as contract
from torch.distributed.fsdp.api import BackwardPrefetch as BackwardPrefetch, CPUOffload as CPUOffload, MixedPrecision as MixedPrecision, ShardingStrategy as ShardingStrategy
from torch.distributed.fsdp.wrap import _FSDPPolicy
from typing import Callable, Iterable

def fully_shard(module: nn.Module, *, process_group: dist.ProcessGroup | None = None, policy: _FSDPPolicy | None = None, strategy: ShardingStrategy | None = None, mixed_precision: MixedPrecision | None = None, cpu_offload: CPUOffload | None = None, ignored_modules: Iterable[torch.nn.Module] | None = None, device_id: int | torch.device | None = None, param_init_fn: Callable[[nn.Module], None] | None = None, sync_module_states: bool = False) -> nn.Module:
    """
    Applies ``FullyShardedDataParallel` (FSDP) semantics to ``module``.
    """
