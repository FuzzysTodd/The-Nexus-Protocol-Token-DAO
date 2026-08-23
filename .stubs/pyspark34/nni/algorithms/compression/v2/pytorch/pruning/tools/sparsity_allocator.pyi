from ...base import Pruner as Pruner
from ...utils import Scaling as Scaling
from .base import SparsityAllocator as SparsityAllocator
from _typeshed import Incomplete
from nni.common.graph_utils import TorchModuleGraph as TorchModuleGraph
from nni.compression.pytorch.utils.shape_dependency import ChannelDependency as ChannelDependency, GroupDependency as GroupDependency
from torch import Tensor as Tensor
from typing import Any, Dict

class NormalSparsityAllocator(SparsityAllocator):
    """
    This allocator directly masks the locations of each pruning target with lower metric values.
    """
    def common_target_masks_generation(self, metrics: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...

class ThresholdSparsityAllocator(SparsityAllocator):
    """
    Note: This allocator is an experimental allocator.
    It takes 'total_sparsity' as threshold to mask the pruning target where metric is lower then threshold.
    """
    def common_target_masks_generation(self, metrics: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...

class BankSparsityAllocator(SparsityAllocator):
    """
    In bank pruner, all values in weight are divided into different sub blocks each shape
    aligned with balance_gran. Each sub block has the same sparsity which equal to the overall sparsity.
    This allocator pruned the weight in the granularity of block.
    """
    balance_gran: Incomplete
    def __init__(self, pruner: Pruner, balance_gran: list) -> None: ...
    def common_target_masks_generation(self, metrics: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...

class GlobalSparsityAllocator(SparsityAllocator):
    """
    This allocator sorts all metrics as a whole, mask the locations of pruning target with lower metric value.
    By default, this allocator will prevent each module from being over-pruned with upper sparsity 0.99.
    """
    def common_target_masks_generation(self, metrics: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...

class DependencyAwareAllocator(SparsityAllocator):
    """
    An specific allocator for Conv2d & Linear module with dependency-aware.
    It will generate a public mask for the modules that have dependencies,
    then generate the part of the non-public mask for each module.
    For other module types, the way to generate the mask is the same as `NormalSparsityAllocator`.
    """
    def __init__(self, pruner: Pruner, dummy_input: Any, scalers: Dict[str, Dict[str, Scaling]] | Scaling | None = None) -> None: ...
    def common_target_masks_generation(self, metrics: Dict[str, Dict[str, Tensor]]) -> Dict[str, Dict[str, Tensor]]: ...
