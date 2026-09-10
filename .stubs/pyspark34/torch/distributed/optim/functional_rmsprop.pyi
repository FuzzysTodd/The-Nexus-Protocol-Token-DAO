from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import List

class _FunctionalRMSprop:
    defaults: Incomplete
    centered: Incomplete
    foreach: Incomplete
    maximize: Incomplete
    param_group: Incomplete
    state: Incomplete
    def __init__(self, params: List[Tensor], lr: float = 0.01, alpha: float = 0.99, eps: float = 1e-08, weight_decay: float = 0.0, momentum: float = 0.0, centered: bool = False, foreach: bool = False, maximize: bool = False, _allow_empty_param_list: bool = False) -> None: ...
    def step(self, gradients: List[Tensor | None]): ...
