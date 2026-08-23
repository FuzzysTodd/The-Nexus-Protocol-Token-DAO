from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import List

class _FunctionalAdagrad:
    defaults: Incomplete
    coalesce_grad: Incomplete
    foreach: Incomplete
    maximize: Incomplete
    state: Incomplete
    param_group: Incomplete
    def __init__(self, params: List[Tensor], lr: float = 0.01, lr_decay: float = 0.0, weight_decay: float = 0.0, initial_accumulator_value: float = 0.0, warmup_lr_multiplier: float = 1.0, warmup_num_iters: float = 0.0, eps: float = 1e-10, coalesce_grad: bool = True, foreach: bool = False, maximize: bool = False, _allow_empty_param_list: bool = False) -> None: ...
    def step(self, gradients: List[Tensor | None]): ...
