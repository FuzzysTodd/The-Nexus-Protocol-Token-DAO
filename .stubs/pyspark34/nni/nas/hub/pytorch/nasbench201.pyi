import torch.nn as nn
from _typeshed import Incomplete

__all__ = ['NasBench201']

class ReLUConvBN(nn.Module):
    op: Incomplete
    def __init__(self, C_in, C_out, kernel_size, stride, padding, dilation) -> None: ...
    def forward(self, x): ...

class SepConv(nn.Module):
    op: Incomplete
    def __init__(self, C_in, C_out, kernel_size, stride, padding, dilation) -> None: ...
    def forward(self, x): ...

class Pooling(nn.Module):
    preprocess: Incomplete
    op: Incomplete
    def __init__(self, C_in, C_out, stride, mode) -> None: ...
    def forward(self, x): ...

class Zero(nn.Module):
    C_in: Incomplete
    C_out: Incomplete
    stride: Incomplete
    is_zero: bool
    def __init__(self, C_in, C_out, stride) -> None: ...
    def forward(self, x): ...

class FactorizedReduce(nn.Module):
    stride: Incomplete
    C_in: Incomplete
    C_out: Incomplete
    relu: Incomplete
    convs: Incomplete
    pad: Incomplete
    bn: Incomplete
    def __init__(self, C_in, C_out, stride) -> None: ...
    def forward(self, x): ...

class ResNetBasicblock(nn.Module):
    conv_a: Incomplete
    conv_b: Incomplete
    downsample: Incomplete
    in_dim: Incomplete
    out_dim: Incomplete
    stride: Incomplete
    num_conv: int
    def __init__(self, inplanes, planes, stride) -> None: ...
    def forward(self, inputs): ...

class NasBench201(nn.Module):
    """The full search space proposed by `NAS-Bench-201 <https://arxiv.org/abs/2001.00326>`__.

    It's a stack of :class:`~nni.retiarii.nn.pytorch.NasBench201Cell`.

    Parameters
    ----------
    stem_out_channels
        The output channels of the stem.
    num_modules_per_stack
        The number of modules (cells) in each stack. Each cell is a :class:`~nni.retiarii.nn.pytorch.NasBench201Cell`.
    num_labels
        Number of categories for classification.
    """
    channels: Incomplete
    num_modules: Incomplete
    num_labels: Incomplete
    stem: Incomplete
    cells: Incomplete
    lastact: Incomplete
    global_pooling: Incomplete
    classifier: Incomplete
    def __init__(self, stem_out_channels: int = 16, num_modules_per_stack: int = 5, num_labels: int = 10) -> None: ...
    def forward(self, inputs): ...
