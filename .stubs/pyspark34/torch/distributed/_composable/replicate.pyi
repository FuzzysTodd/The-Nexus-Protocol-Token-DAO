import torch
import torch.nn as nn
from .contract import contract as contract
from _typeshed import Incomplete
from typing import Tuple

def replicate(module: nn.Module, **kwargs) -> nn.Module:
    """Replicates a module

    Args:
        module (torch.nn.Module): module to replicate

    Example::
        >>> # xdoctest: +REQUIRES(module:torch._C._distributed_c10d)
        >>> module = nn.Linear(3, 3)
        >>> replicate(module)
    """

class _ReplicateState:
    modules: Incomplete
    has_initialized: bool
    kwargs: Incomplete
    def __init__(self) -> None: ...
    def mark_modules(self, *modules: nn.Module, **kwargs) -> None: ...
    def init_helper(self) -> None: ...
    def forward_pre_hook(self, module: nn.Module, input: Tuple[torch.Tensor, ...]) -> None: ...
    def forward_post_hook(self, module: nn.Module, input: Tuple[torch.Tensor], output: torch.Tensor) -> torch.Tensor: ...
