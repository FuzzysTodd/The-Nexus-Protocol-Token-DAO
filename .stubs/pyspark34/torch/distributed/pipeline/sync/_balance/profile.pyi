import torch
import torch.nn as nn
from ..microbatch import Batch as Batch
from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import Any, Generator, List, Sequence

Device: Incomplete
Tensors = Sequence[Tensor]
TensorOrTensors = Tensor | Tensors

def layerwise_sandbox(module: nn.Sequential, device: torch.device) -> Generator[nn.Module, None, None]:
    """Copies layers for ease to profile. It doesn't modify the given
    module.
    """
def detach(batch: Batch) -> None:
    """Detaches from autograd graph."""
def profile_times(module: nn.Sequential, sample: List[Any] | Tensor, timeout: float, device: torch.device) -> List[int]:
    """Profiles elapsed times per layer."""
def profile_sizes(module: nn.Sequential, input: List[Any] | Tensor, chunks: int, param_scale: float, device: torch.device) -> List[int]:
    """Profiles CUDA memory usage per layer."""
