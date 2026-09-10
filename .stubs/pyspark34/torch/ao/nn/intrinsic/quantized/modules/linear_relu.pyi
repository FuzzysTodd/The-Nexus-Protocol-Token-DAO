import torch
import torch.ao.nn.quantized as nnq
from _typeshed import Incomplete

__all__ = ['LinearReLU', 'LinearLeakyReLU', 'LinearTanh']

class LinearReLU(nnq.Linear):
    """
    A LinearReLU module fused from Linear and ReLU modules

    We adopt the same interface as :class:`torch.ao.nn.quantized.Linear`.

    Attributes:
        Same as torch.ao.nn.quantized.Linear

    Examples::

        >>> # xdoctest: +SKIP
        >>> m = nn.intrinsic.LinearReLU(20, 30)
        >>> input = torch.randn(128, 20)
        >>> output = m(input)
        >>> print(output.size())
        torch.Size([128, 30])
    """
    def __init__(self, in_features, out_features, bias: bool = True, dtype=...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_linear_relu, output_scale, output_zero_point): ...

class LinearLeakyReLU(nnq.Linear):
    """
    For onednn backend only
    A LinearLeakyReLU module fused from Linear and LeakyReLU modules
    We adopt the same interface as :class:`torch.ao.nn.quantized.Linear`.
    Attributes:
        Same as torch.ao.nn.quantized.Linear
        + negative_slope
    Examples::
        >>> # xdoctest: +SKIP
        >>> m = nn.intrinsic.LinearLeakyReLU(20, 30, 0.01)
        >>> input = torch.randn(128, 20)
        >>> output = m(input)
        >>> print(output.size())
        torch.Size([128, 30])
    """
    negative_slope: Incomplete
    def __init__(self, in_features, out_features, negative_slope, bias: bool = True, dtype=...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_mod, output_scale, output_zero_point): ...

class LinearTanh(nnq.Linear):
    """
    A LinearTanh module fused from Linear and Tanh modules

    We adopt the same interface as :class:`torch.ao.nn.quantized.Linear`.

    Attributes:
        Same as torch.ao.nn.quantized.Linear

    Examples::

        >>> # xdoctest: +SKIP
        >>> m = nn.intrinsic.LinearTanh(20, 30)
        >>> input = torch.randn(128, 20)
        >>> output = m(input)
        >>> print(output.size())
        torch.Size([128, 30])
    """
    def __init__(self, in_features, out_features, bias: bool = True, dtype=...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_mod, output_scale, output_zero_point): ...
