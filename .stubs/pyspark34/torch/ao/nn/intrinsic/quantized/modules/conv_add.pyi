import torch.ao.nn.quantized as nnq
from _typeshed import Incomplete

class ConvAdd2d(nnq.Conv2d):
    """
    A ConvAdd2d module is a fused module of Conv2d and Add

    We adopt the same interface as :class:`torch.ao.nn.quantized.Conv2d`.

    Attributes:
        Same as torch.ao.nn.quantized.Conv2d

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input, extra_input): ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_qconv, output_scale, output_zero_point): ...

class ConvAddReLU2d(nnq.Conv2d):
    """
    A ConvAddReLU2d module is a fused module of Conv2d, Add and Relu

    We adopt the same interface as :class:`torch.ao.nn.quantized.Conv2d`.

    Attributes:
        Same as torch.ao.nn.quantized.Conv2d

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', device: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def forward(self, input, extra_input): ...
    @classmethod
    def from_float(cls, mod): ...
    @classmethod
    def from_reference(cls, ref_qconv, output_scale, output_zero_point): ...
