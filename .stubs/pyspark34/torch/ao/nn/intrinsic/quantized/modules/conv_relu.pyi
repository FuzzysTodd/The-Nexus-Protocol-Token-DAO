import torch.ao.nn.quantized as nnq
from _typeshed import Incomplete

__all__ = ['ConvReLU1d', 'ConvReLU2d', 'ConvReLU3d']

class ConvReLU1d(nnq.Conv1d):
    """
    A ConvReLU1d module is a fused module of Conv1d and ReLU

    We adopt the same interface as :class:`torch.ao.nn.quantized.Conv1d`.

    Attributes:
        Same as torch.ao.nn.quantized.Conv1d

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_qconv, output_scale, output_zero_point): ...

class ConvReLU2d(nnq.Conv2d):
    """
    A ConvReLU2d module is a fused module of Conv2d and ReLU

    We adopt the same interface as :class:`torch.ao.nn.quantized.Conv2d`.

    Attributes:
        Same as torch.ao.nn.quantized.Conv2d

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_qconv, output_scale, output_zero_point): ...

class ConvReLU3d(nnq.Conv3d):
    """
    A ConvReLU3d module is a fused module of Conv3d and ReLU

    We adopt the same interface as :class:`torch.ao.nn.quantized.Conv3d`.

    Attributes: Same as torch.ao.nn.quantized.Conv3d

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_qconv, output_scale, output_zero_point): ...
