from _typeshed import Incomplete
from abc import ABC
from torch.distributed.algorithms.ddp_comm_hooks.default_hooks import allreduce_hook as allreduce_hook
from torch.distributed.fsdp import FullyShardedDataParallel as FullyShardedDataParallel
from torch.distributed.optim import as_functional_optim as as_functional_optim
from torch.nn.parallel import DistributedDataParallel as DistributedDataParallel
from torch.optim import Optimizer as Optimizer
from typing import Type

def register_overlapped(optim_cls): ...

class OverlappedOptimizer(ABC):
    optim_cls: Incomplete
    def __init__(self, optim_cls: Type) -> None:
        """
        OverlappedOptimizer is a base class that child classes can implement to
        specify how different optimizers will register themselves with DDP.
        """
    def register_ddp(self, ddp: DistributedDataParallel) -> None:
        """Registers the overlapped optimizer with DDP."""
    def register_fsdp(self, fsdp: FullyShardedDataParallel) -> None:
        """Registers the overlapped optimizer with FSDP."""

class _OverlappedStandardOptimizer(OverlappedOptimizer):
    """Overlaps a regular ``Optimizer``."""
    def __init__(self, optim_cls: Type, params, *optim_args, **optim_kwargs) -> None: ...
    def register_ddp(self, ddp_inst: DistributedDataParallel): ...
