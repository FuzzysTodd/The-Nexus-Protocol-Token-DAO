import torch
import torch.nn as nn
from _typeshed import Incomplete
from typing import Tuple

class UnitModule(nn.Module):
    l1: Incomplete
    seq: Incomplete
    l2: Incomplete
    def __init__(self, device: torch.device) -> None: ...
    def forward(self, x): ...

class CompositeModel(nn.Module):
    l1: Incomplete
    u1: Incomplete
    u2: Incomplete
    l2: Incomplete
    def __init__(self, device: torch.device) -> None: ...
    def forward(self, x): ...

class UnitParamModule(nn.Module):
    l: Incomplete
    seq: Incomplete
    p: Incomplete
    def __init__(self, device: torch.device) -> None: ...
    def forward(self, x): ...

class CompositeParamModel(nn.Module):
    l: Incomplete
    u1: Incomplete
    u2: Incomplete
    p: Incomplete
    def __init__(self, device: torch.device) -> None: ...
    def forward(self, x): ...

class FakeSequential(nn.Module):
    def __init__(self, *modules: Tuple[nn.Module, ...]) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class NestedSequentialModel(nn.Module):
    seq1: Incomplete
    lin: Incomplete
    seq2: Incomplete
    def __init__(self, device: torch.device) -> None: ...
