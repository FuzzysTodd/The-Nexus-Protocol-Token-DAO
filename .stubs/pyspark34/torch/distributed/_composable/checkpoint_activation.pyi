import torch
import torch.nn as nn
from .contract import contract as contract
from torch.utils.checkpoint import detach_variable as detach_variable, get_device_states as get_device_states, set_device_states as set_device_states
from typing import Any, Tuple

class _ModuleHookCheckpointFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, module: nn.Module, output: Any, *inputs: Any) -> Any: ...
    @staticmethod
    def backward(ctx, output_grads: Tuple[torch.Tensor | None]) -> Any: ...

class _Holder: ...

def checkpoint(module: nn.Module, *, use_reentrant: bool = True) -> nn.Module:
    """
    This is a composable activation checkpointing API. Unlike functional
    activation checkpointing APIs, this one does not require changing model
    source code. Unlike ``nn.Module`` wrapper activation checkpointing APIs,
    this one does not modify model structure or fully-qualified names either.
    Under the hood, it registers activation checkpointing logic as pre- and
    post-forward hooks. Hence, this API can be easily applied to any model or
    sub-modules in the model.

    Args:
        module (nn.Module): the target model or sub-module to apply activation
            checkpointing.
        use_reentrant (bool): Apply activation checkpointing using reentrant
            autograd.

    Example::
        >>> # xdoctest: +SKIP
        >>> import torch.nn as nn
        >>>
        >>> class MyModel(nn.Module):
        >>>     def __init__(self):
        >>>         super().__init__()
        >>>         self.l1 = nn.Linear(10, 10)
        >>>         self.l2 = nn.Linear(10, 10)
        >>>
        >>>     def forward(self, x):
        >>>         return self.l2(self.l1(x))
        >>>
        >>> model = MyModel()
        >>> checkpoint(model.l1)  # apply activation checkpointing only to l1
        >>> model(torch.zeros(2, 10)).sum().backward()

    """
