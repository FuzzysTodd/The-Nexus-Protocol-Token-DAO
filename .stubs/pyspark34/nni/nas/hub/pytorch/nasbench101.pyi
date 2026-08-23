import torch.nn as nn
from _typeshed import Incomplete

__all__ = ['NasBench101']

class ConvBNReLU(nn.Module):
    in_channels: Incomplete
    out_channels: Incomplete
    conv_bn_relu: Incomplete
    def __init__(self, in_channels, out_channels, kernel_size: int = 1, stride: int = 1, padding: int = 0) -> None: ...
    def reset_parameters(self) -> None: ...
    def forward(self, x): ...

class Conv3x3BNReLU(ConvBNReLU):
    def __init__(self, in_channels, out_channels) -> None: ...

class Conv1x1BNReLU(ConvBNReLU):
    def __init__(self, in_channels, out_channels) -> None: ...
Projection = Conv1x1BNReLU

class NasBench101(nn.Module):
    """The full search space proposed by `NAS-Bench-101 <http://proceedings.mlr.press/v97/ying19a/ying19a.pdf>`__.

    It's simply a stack of :class:`~nni.retiarii.nn.pytorch.NasBench101Cell`. Operations are conv3x3, conv1x1 and maxpool respectively.

    Parameters
    ----------
    stem_out_channels
        Number of output channels of the stem convolution.
    num_stacks
        Number of stacks in the network.
    num_modules_per_stack
        Number of modules in each stack. Each module is a :class:`~nni.retiarii.nn.pytorch.NasBench101Cell`.
    max_num_vertices
        Maximum number of vertices in each cell.
    max_num_edges
        Maximum number of edges in each cell.
    num_labels
        Number of categories for classification.
    bn_eps
        Epsilon for batch normalization.
    bn_momentum
        Momentum for batch normalization.
    """
    stem_conv: Incomplete
    features: Incomplete
    gap: Incomplete
    classifier: Incomplete
    def __init__(self, stem_out_channels: int = 128, num_stacks: int = 3, num_modules_per_stack: int = 3, max_num_vertices: int = 7, max_num_edges: int = 9, num_labels: int = 10, bn_eps: float = 1e-05, bn_momentum: float = 0.003) -> None: ...
    def forward(self, x): ...
