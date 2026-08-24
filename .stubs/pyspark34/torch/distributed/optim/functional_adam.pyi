from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import List, Tuple

class _FunctionalAdam:
    defaults: Incomplete
    amsgrad: Incomplete
    maximize: Incomplete
    foreach: Incomplete
    fused: Incomplete
    state: Incomplete
    param_group: Incomplete
    def __init__(self, params: List[Tensor], lr: float = 0.001, betas: Tuple[float, float] = (0.9, 0.999), eps: float = 1e-08, weight_decay: float = 0.0, amsgrad: bool = False, maximize: bool = False, foreach: bool = False, fused: bool = False, _allow_empty_param_list: bool = False) -> None: ...
    def step_param(self, param: Tensor, grad: Tensor | None):
        """
        Similar to step, but operates on a single parameter and optionally a
        gradient tensor.
        """
    def step(self, gradients: List[Tensor | None]): ...
