from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import List, Tuple

class _FunctionalRprop:
    defaults: Incomplete
    etas: Incomplete
    step_sizes: Incomplete
    foreach: Incomplete
    maximize: Incomplete
    param_group: Incomplete
    state: Incomplete
    def __init__(self, params: List[Tensor], lr: float = 0.01, etas: Tuple[float, float] = (0.5, 1.2), step_sizes: Tuple[float, float] = (1e-06, 50), foreach: bool = False, maximize: bool = False, _allow_empty_param_list: bool = False) -> None: ...
    def step(self, gradients: List[Tensor | None]): ...
