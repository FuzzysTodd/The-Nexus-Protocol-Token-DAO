import torch
from _typeshed import Incomplete

__all__ = ['Linear']

class Linear(torch.nn.Module):
    """
    A dynamically quantized sparse linear module with float tensor as inputs and outputs.
    """
    in_features: Incomplete
    out_features: Incomplete
    def __init__(self, in_features, out_features, row_block_size, col_block_size, bias: bool = True, dtype=...) -> None: ...
    def extra_repr(self): ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
    def weight(self): ...
    def bias(self): ...
    def set_weight_bias(self, w: torch.Tensor, b: torch.Tensor | None, row_block_size: int | None, col_block_size: int | None) -> None: ...
    @classmethod
    def from_float(cls, mod):
        """Create a quantized sparse dynamic module from a float module.

        We only care about the convert at this stage, no need for observers just yet.
        """
