import torch.nn as nn
from _typeshed import Incomplete

class LinearReluFunctionalChild(nn.Module):
    w1: Incomplete
    b1: Incomplete
    def __init__(self, N) -> None: ...
    def forward(self, x): ...

class LinearReluFunctional(nn.Module):
    child: Incomplete
    w1: Incomplete
    b1: Incomplete
    def __init__(self, N) -> None: ...
    def forward(self, x): ...
