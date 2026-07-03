from _typeshed import Incomplete
from nni.algorithms.compression.v2.pytorch.utils import config_list_canonical as config_list_canonical
from nni.compression.pytorch.utils import count_flops_params as count_flops_params
from torch import Tensor as Tensor
from torch.nn import Module as Module
from typing import Dict, List

class AMCEnv:
    pruning_ops: Incomplete
    pruning_types: Incomplete
    pruning_op_names: Incomplete
    dummy_input: Incomplete
    total_sparsity: Incomplete
    max_sparsity_per_layer: Incomplete
    target: Incomplete
    origin_statistics: Incomplete
    under_pruning_target: Incomplete
    excepted_pruning_target: Incomplete
    def __init__(self, model: Module, config_list: List[Dict], dummy_input: Tensor, total_sparsity: float, max_sparsity_per_layer: Dict[str, float], target: str = 'flops') -> None: ...
    ops_iter: Incomplete
    def reset(self): ...
    current_op_name: Incomplete
    current_op_target: Incomplete
    def correct_action(self, action: float, model: Module): ...
    def step(self, action: float, model: Module): ...
    def is_first_layer(self): ...
    def is_final_layer(self): ...
    @property
    def state_feature(self): ...
