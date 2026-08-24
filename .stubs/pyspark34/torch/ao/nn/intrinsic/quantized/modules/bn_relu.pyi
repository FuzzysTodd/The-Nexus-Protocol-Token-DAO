import torch.ao.nn.quantized as nnq
from _typeshed import Incomplete

__all__ = ['BNReLU2d', 'BNReLU3d']

class BNReLU2d(nnq.BatchNorm2d):
    """
    A BNReLU2d module is a fused module of BatchNorm2d and ReLU

    We adopt the same interface as :class:`torch.ao.nn.quantized.BatchNorm2d`.

    Attributes:
        Same as torch.ao.nn.quantized.BatchNorm2d

    """
    def __init__(self, num_features, eps: float = 1e-05, momentum: float = 0.1, device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, bn_relu, output_scale, output_zero_point): ...

class BNReLU3d(nnq.BatchNorm3d):
    """
    A BNReLU3d module is a fused module of BatchNorm3d and ReLU

    We adopt the same interface as :class:`torch.ao.nn.quantized.BatchNorm3d`.

    Attributes:
        Same as torch.ao.nn.quantized.BatchNorm3d

    """
    def __init__(self, num_features, eps: float = 1e-05, momentum: float = 0.1, device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, bn_relu, output_scale, output_zero_point): ...
