from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Pruner

__all__ = ['DependencyAwarePruner']

class DependencyAwarePruner(Pruner):
    """
    DependencyAwarePruner has two ways to calculate the masks
    for conv layers. In the normal way, the DependencyAwarePruner
    will calculate the mask of each layer separately. For example, each
    conv layer determine which filters should be pruned according to its L1
    norm. In constrast, in the dependency-aware way, the layers that in a
    dependency group will be pruned jointly and these layers will be forced
    to prune the same channels.
    """
    dependency_aware: Incomplete
    dummy_input: Incomplete
    graph: Incomplete
    channel_depen: Incomplete
    group_depen: Incomplete
    masker: Incomplete
    def __init__(self, model, config_list, optimizer: Incomplete | None = None, pruning_algorithm: str = 'level', dependency_aware: bool = False, dummy_input: Incomplete | None = None, **algo_kwargs) -> None: ...
    def calc_mask(self, wrapper, wrapper_idx: Incomplete | None = None): ...
    def update_mask(self) -> None: ...
    def validate_config(self, model, config_list): ...
