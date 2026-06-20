import torch
import torch.nn as nn
from .differentiable import DifferentiableMixedInput, DifferentiableMixedLayer
from _typeshed import Incomplete
from typing import Any, Tuple

__all__ = ['ProxylessMixedLayer', 'ProxylessMixedInput']

class ProxylessContext:
    arch_alpha: Incomplete
    softmax: Incomplete
    layer_input: Incomplete
    layer_output: Incomplete
    layer_sample_idx: Incomplete
    def __init__(self, arch_alpha: torch.Tensor, softmax: nn.Module) -> None: ...
    def clear_context(self) -> None: ...
    def save_forward_context(self, layer_input: Any, layer_output: Any, layer_sample_idx: int): ...
    def backward_hook(self, module: nn.Module, grad_input: Tuple[torch.Tensor, ...] | torch.Tensor, grad_output: Tuple[torch.Tensor, ...] | torch.Tensor) -> None: ...

class ProxylessMixedLayer(DifferentiableMixedLayer):
    """Proxyless version of differentiable mixed layer.
    It resamples a single-path every time, rather than go through the softmax.
    """
    ctx: Incomplete
    def __init__(self, paths: list[tuple[str, nn.Module]], alpha: torch.Tensor, softmax: nn.Module, label: str) -> None: ...
    def forward(self, *args, **kwargs):
        """Forward pass of one single path."""
    def forward_path(self, index, *args, **kwargs): ...
    def resample(self, memo):
        """Sample one path based on alpha if label is not found in memo."""

class ProxylessMixedInput(DifferentiableMixedInput):
    """Proxyless version of differentiable input choice.
    See :class:`ProxylessMixedLayer` for implementation details.
    """
    ctx: Incomplete
    def __init__(self, n_candidates: int, n_chosen: int | None, alpha: torch.Tensor, softmax: nn.Module, label: str) -> None: ...
    def forward(self, inputs):
        """Choose one single input."""
    def forward_path(self, index, inputs): ...
    def resample(self, memo):
        """Sample one path based on alpha if label is not found in memo."""
