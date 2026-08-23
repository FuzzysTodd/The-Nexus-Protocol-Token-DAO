from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import List

class _FunctionalAdadelta:
    defaults: Incomplete
    foreach: Incomplete
    maximize: Incomplete
    param_group: Incomplete
    state: Incomplete
    def __init__(self, params: List[Tensor], lr: float = 1.0, rho: float = 0.9, eps: float = 1e-06, weight_decay: float = 0.0, foreach: bool = False, maximize: bool = False, _allow_empty_param_list: bool = False) -> None: ...
    def step(self, gradients: List[Tensor | None]): ...
