from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import List, Tuple

class _FunctionalAdamax:
    defaults: Incomplete
    foreach: Incomplete
    maximize: Incomplete
    state: Incomplete
    param_group: Incomplete
    def __init__(self, params: List[Tensor], lr: float = 0.001, betas: Tuple[float, float] = (0.9, 0.999), eps: float = 1e-08, weight_decay: float = 0.0, foreach: bool = False, maximize: bool = False, _allow_empty_param_list: bool = False) -> None: ...
    def step(self, gradients: List[Tensor | None]): ...
