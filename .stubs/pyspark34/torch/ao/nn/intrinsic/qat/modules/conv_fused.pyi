import torch.ao.nn.intrinsic as nni
import torch.ao.nn.qat as nnqat
import torch.nn as nn
from _typeshed import Incomplete
from typing import TypeVar

__all__ = ['ConvBn1d', 'ConvBnReLU1d', 'ConvReLU1d', 'ConvBn2d', 'ConvBnReLU2d', 'ConvReLU2d', 'ConvBn3d', 'ConvBnReLU3d', 'ConvReLU3d', 'update_bn_stats', 'freeze_bn_stats']

MOD = TypeVar('MOD', bound=nn.modules.conv._ConvNd)

class _ConvBnNd(nn.modules.conv._ConvNd, nni._FusedModule):
    qconfig: Incomplete
    freeze_bn: Incomplete
    bn: Incomplete
    weight_fake_quant: Incomplete
    bias: Incomplete
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, dilation, transposed, output_padding, groups, bias, padding_mode, eps: float = 1e-05, momentum: float = 0.1, freeze_bn: bool = False, qconfig: Incomplete | None = None, dim: int = 2) -> None: ...
    def reset_running_stats(self) -> None: ...
    def reset_bn_parameters(self) -> None: ...
    def reset_parameters(self) -> None: ...
    def update_bn_stats(self): ...
    def freeze_bn_stats(self): ...
    def extra_repr(self): ...
    def forward(self, input): ...
    training: Incomplete
    def train(self, mode: bool = True):
        """
        Batchnorm's training behavior is using the self.training flag. Prevent
        changing it if BN is frozen. This makes sure that calling `model.train()`
        on a model with a frozen BN will behave properly.
        """
    @classmethod
    def from_float(cls, mod):
        """Create a qat module from a float module or qparams_dict

            Args: `mod` a float module, either produced by torch.ao.quantization utilities
            or directly from user
        """
    def to_float(self): ...

class ConvBn1d(_ConvBnNd, nn.Conv1d):
    """
    A ConvBn1d module is a module fused from Conv1d and BatchNorm1d,
    attached with FakeQuantize modules for weight,
    used in quantization aware training.

    We combined the interface of :class:`torch.nn.Conv1d` and
    :class:`torch.nn.BatchNorm1d`.

    Similar to :class:`torch.nn.Conv1d`, with FakeQuantize modules initialized
    to default.

    Attributes:
        freeze_bn:
        weight_fake_quant: fake quant module for weight

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: Incomplete | None = None, padding_mode: str = 'zeros', eps: float = 1e-05, momentum: float = 0.1, freeze_bn: bool = False, qconfig: Incomplete | None = None) -> None: ...

class ConvBnReLU1d(ConvBn1d):
    """
    A ConvBnReLU1d module is a module fused from Conv1d, BatchNorm1d and ReLU,
    attached with FakeQuantize modules for weight,
    used in quantization aware training.

    We combined the interface of :class:`torch.nn.Conv1d` and
    :class:`torch.nn.BatchNorm1d` and :class:`torch.nn.ReLU`.

    Similar to `torch.nn.Conv1d`, with FakeQuantize modules initialized to
    default.

    Attributes:
        weight_fake_quant: fake quant module for weight

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: Incomplete | None = None, padding_mode: str = 'zeros', eps: float = 1e-05, momentum: float = 0.1, freeze_bn: bool = False, qconfig: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...

class ConvReLU1d(nnqat.Conv1d, nni._FusedModule):
    """A ConvReLU1d module is a fused module of Conv1d and ReLU, attached with
    FakeQuantize modules for weight for
    quantization aware training.

    We combined the interface of :class:`~torch.nn.Conv1d` and
    :class:`~torch.nn.BatchNorm1d`.

    Attributes:
        weight_fake_quant: fake quant module for weight

    """
    qconfig: Incomplete
    weight_fake_quant: Incomplete
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', qconfig: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...

class ConvBn2d(_ConvBnNd, nn.Conv2d):
    """
    A ConvBn2d module is a module fused from Conv2d and BatchNorm2d,
    attached with FakeQuantize modules for weight,
    used in quantization aware training.

    We combined the interface of :class:`torch.nn.Conv2d` and
    :class:`torch.nn.BatchNorm2d`.

    Similar to :class:`torch.nn.Conv2d`, with FakeQuantize modules initialized
    to default.

    Attributes:
        freeze_bn:
        weight_fake_quant: fake quant module for weight

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: Incomplete | None = None, padding_mode: str = 'zeros', eps: float = 1e-05, momentum: float = 0.1, freeze_bn: bool = False, qconfig: Incomplete | None = None) -> None: ...

class ConvBnReLU2d(ConvBn2d):
    """
    A ConvBnReLU2d module is a module fused from Conv2d, BatchNorm2d and ReLU,
    attached with FakeQuantize modules for weight,
    used in quantization aware training.

    We combined the interface of :class:`torch.nn.Conv2d` and
    :class:`torch.nn.BatchNorm2d` and :class:`torch.nn.ReLU`.

    Similar to `torch.nn.Conv2d`, with FakeQuantize modules initialized to
    default.

    Attributes:
        weight_fake_quant: fake quant module for weight

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: Incomplete | None = None, padding_mode: str = 'zeros', eps: float = 1e-05, momentum: float = 0.1, freeze_bn: bool = False, qconfig: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...

class ConvReLU2d(nnqat.Conv2d, nni._FusedModule):
    """A ConvReLU2d module is a fused module of Conv2d and ReLU, attached with
    FakeQuantize modules for weight for
    quantization aware training.

    We combined the interface of :class:`~torch.nn.Conv2d` and
    :class:`~torch.nn.BatchNorm2d`.

    Attributes:
        weight_fake_quant: fake quant module for weight

    """
    qconfig: Incomplete
    weight_fake_quant: Incomplete
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', qconfig: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...

class ConvBn3d(_ConvBnNd, nn.Conv3d):
    """
    A ConvBn3d module is a module fused from Conv3d and BatchNorm3d,
    attached with FakeQuantize modules for weight,
    used in quantization aware training.

    We combined the interface of :class:`torch.nn.Conv3d` and
    :class:`torch.nn.BatchNorm3d`.

    Similar to :class:`torch.nn.Conv3d`, with FakeQuantize modules initialized
    to default.

    Attributes:
        freeze_bn:
        weight_fake_quant: fake quant module for weight

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: Incomplete | None = None, padding_mode: str = 'zeros', eps: float = 1e-05, momentum: float = 0.1, freeze_bn: bool = False, qconfig: Incomplete | None = None) -> None: ...

class ConvBnReLU3d(ConvBn3d):
    """
    A ConvBnReLU3d module is a module fused from Conv3d, BatchNorm3d and ReLU,
    attached with FakeQuantize modules for weight,
    used in quantization aware training.

    We combined the interface of :class:`torch.nn.Conv3d` and
    :class:`torch.nn.BatchNorm3d` and :class:`torch.nn.ReLU`.

    Similar to `torch.nn.Conv3d`, with FakeQuantize modules initialized to
    default.

    Attributes:
        weight_fake_quant: fake quant module for weight

    """
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: Incomplete | None = None, padding_mode: str = 'zeros', eps: float = 1e-05, momentum: float = 0.1, freeze_bn: bool = False, qconfig: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...

class ConvReLU3d(nnqat.Conv3d, nni._FusedModule):
    """A ConvReLU3d module is a fused module of Conv3d and ReLU, attached with
    FakeQuantize modules for weight for
    quantization aware training.

    We combined the interface of :class:`~torch.nn.Conv3d` and
    :class:`~torch.nn.BatchNorm3d`.

    Attributes:
        weight_fake_quant: fake quant module for weight

    """
    qconfig: Incomplete
    weight_fake_quant: Incomplete
    def __init__(self, in_channels, out_channels, kernel_size, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, bias: bool = True, padding_mode: str = 'zeros', qconfig: Incomplete | None = None) -> None: ...
    def forward(self, input): ...
    @classmethod
    def from_float(cls, mod): ...

def update_bn_stats(mod) -> None: ...
def freeze_bn_stats(mod) -> None: ...
