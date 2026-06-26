from _typeshed import Incomplete
from torch import nn as nn

def rows_are_subset(subset_tensor, superset_tensor) -> bool:
    """
    Checks to see if all rows in subset tensor are present in the superset tensor
    """

class SimpleLinear(nn.Module):
    """Model with only Linear layers without biases, some wrapped in a Sequential,
    some following the Sequential. Used to test basic pruned Linear-Linear fusion."""
    seq: Incomplete
    linear1: Incomplete
    linear2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class LinearBias(nn.Module):
    """Model with only Linear layers, alternating layers with biases,
    wrapped in a Sequential. Used to test pruned Linear-Bias-Linear fusion."""
    seq: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class LinearActivation(nn.Module):
    """Model with only Linear layers, some with bias, some in a Sequential and some following.
    Activation functions modules in between each Linear in the Sequential, and each outside layer.
    Used to test pruned Linear(Bias)-Activation-Linear fusion."""
    seq: Incomplete
    linear1: Incomplete
    act1: Incomplete
    linear2: Incomplete
    act2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class LinearActivationFunctional(nn.Module):
    """Model with only Linear layers, some with bias, some in a Sequential and some following.
    Activation functions modules in between each Linear in the Sequential, and functional
    activationals are called in between each outside layer.
    Used to test pruned Linear(Bias)-Activation-Linear fusion."""
    seq: Incomplete
    linear1: Incomplete
    linear2: Incomplete
    linear3: Incomplete
    act1: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class SimpleConv2d(nn.Module):
    """Model with only Conv2d layers, all without bias, some in a Sequential and some following.
    Used to test pruned Conv2d-Conv2d fusion."""
    seq: Incomplete
    conv2d1: Incomplete
    conv2d2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class Conv2dBias(nn.Module):
    """Model with only Conv2d layers, some with bias, some in a Sequential and some outside.
    Used to test pruned Conv2d-Bias-Conv2d fusion."""
    seq: Incomplete
    conv2d1: Incomplete
    conv2d2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class Conv2dActivation(nn.Module):
    """Model with only Conv2d layers, some with bias, some in a Sequential and some following.
    Activation function modules in between each Sequential layer, functional activations called
    in-between each outside layer.
    Used to test pruned Conv2d-Bias-Activation-Conv2d fusion."""
    seq: Incomplete
    conv2d1: Incomplete
    conv2d2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class Conv2dPadBias(nn.Module):
    """Model with only Conv2d layers, all with bias and some with padding > 0,
    some in a Sequential and some following. Activation function modules in between each layer.
    Used to test that bias is propagated correctly in the special case of
    pruned Conv2d-Bias-(Activation)Conv2d fusion, when the second Conv2d layer has padding > 0."""
    seq: Incomplete
    conv2d1: Incomplete
    act1: Incomplete
    conv2d2: Incomplete
    act2: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class Conv2dPool(nn.Module):
    """Model with only Conv2d layers, all with bias, some in a Sequential and some following.
    Activation function modules in between each layer, Pool2d modules in between each layer.
    Used to test pruned Conv2d-Pool2d-Conv2d fusion."""
    seq: Incomplete
    conv2d1: Incomplete
    maxpool: Incomplete
    af1: Incomplete
    conv2d2: Incomplete
    conv2d3: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class Conv2dPoolFlattenFunctional(nn.Module):
    """Model with Conv2d layers, all with bias, some in a Sequential and some following, and then a Pool2d
    and a functional Flatten followed by a Linear layer.
    Activation functions and Pool2ds in between each layer also.
    Used to test pruned Conv2d-Pool2d-Flatten-Linear fusion."""
    seq: Incomplete
    conv2d1: Incomplete
    af1: Incomplete
    conv2d2: Incomplete
    avg_pool: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class Conv2dPoolFlatten(nn.Module):
    """Model with Conv2d layers, all with bias, some in a Sequential and some following, and then a Pool2d
    and a Flatten module followed by a Linear layer.
    Activation functions and Pool2ds in between each layer also.
    Used to test pruned Conv2d-Pool2d-Flatten-Linear fusion."""
    seq: Incomplete
    conv2d1: Incomplete
    af1: Incomplete
    conv2d2: Incomplete
    avg_pool: Incomplete
    flatten: Incomplete
    fc: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class LSTMLinearModel(nn.Module):
    """Container module with an encoder, a recurrent module, and a linear."""
    lstm: Incomplete
    linear: Incomplete
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_layers: int) -> None: ...
    def forward(self, input): ...

class LSTMLayerNormLinearModel(nn.Module):
    """Container module with an LSTM, a LayerNorm, and a linear."""
    lstm: Incomplete
    norm: Incomplete
    linear: Incomplete
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_layers: int) -> None: ...
    def forward(self, x): ...
