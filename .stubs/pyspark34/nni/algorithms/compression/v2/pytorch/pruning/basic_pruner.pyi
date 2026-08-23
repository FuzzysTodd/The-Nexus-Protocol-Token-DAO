from ..base import Pruner
from ..utils import Evaluator
from .tools import DataCollector, MetricsCalculator, SparsityAllocator
from _typeshed import Incomplete
from torch import Tensor
from torch.nn import Module
from torch.optim import Optimizer
from typing import Callable, Dict, List, Tuple, overload

__all__ = ['LevelPruner', 'L1NormPruner', 'L2NormPruner', 'FPGMPruner', 'SlimPruner', 'ActivationPruner', 'ActivationAPoZRankPruner', 'ActivationMeanRankPruner', 'TaylorFOWeightPruner', 'ADMMPruner']

class BasicPruner(Pruner):
    data_collector: DataCollector
    metrics_calculator: MetricsCalculator
    sparsity_allocator: SparsityAllocator
    config_list: Incomplete
    def validate_config(self, model: Module, config_list: List[Dict]): ...
    def reset(self, model: Module | None, config_list: List[Dict] | None): ...
    def reset_tools(self) -> None:
        """
        This function is used to reset `self.data_collector`, `self.metrics_calculator` and `self.sparsity_allocator`.
        The subclass needs to implement this function to complete the pruning process.
        See `compress()` to understand how NNI use these three part to generate mask for the bound model.
        """
    def compress(self) -> Tuple[Module, Dict]:
        """
        Used to generate the mask. Pruning process is divided in three stages.
        `self.data_collector` collect the data used to calculate the specify metric.
        `self.metrics_calculator` calculate the metric and `self.sparsity_allocator` generate the mask depend on the metric.

        Returns
        -------
        Tuple[Module, Dict]
            Return the wrapped model and mask.
        """

class EvaluatorBasedPruner(BasicPruner):
    evaluator: Evaluator
    using_evaluator: bool
    trainer: _LEGACY_TRAINER
    traced_optimizer: Optimizer
    criterion: _LEGACY_CRITERION
    def compress(self) -> Tuple[Module, Dict]: ...

class LevelPruner(BasicPruner):
    '''
    This is a basic pruner, and in some papers called it magnitude pruning or fine-grained pruning.
    It will mask the smallest magnitude weights in each specified layer by a saprsity ratio configured in the config list.

    Parameters
    ----------
    model
        Model to be pruned.
    config_list
        Supported keys:
            - sparsity : This is to specify the sparsity for each layer in this config to be compressed.
            - sparsity_per_layer : Equals to sparsity.
            - op_types : Operation types to be pruned.
            - op_names : Operation names to be pruned.
            - op_partial_names: Operation partial names to be pruned, will be autocompleted by NNI.
            - exclude : Set True then the layers setting by op_types and op_names will be excluded from pruning.
    mode
        \'normal\' or \'balance\'.
        If setting \'normal\' mode, target tensor will be pruned in the way of finegrained pruning.
        If setting \'balance\' mode, a specal sparse pattern will chosen by pruner. Take linear
        operation an example, weight tensor will be split into sub block whose shape is aligned to
        balance_gran. Then finegrained pruning will be applied internal of sub block. This sparsity
        pattern have more chance to achieve better trade-off between model performance and hardware
        acceleration. Please refer to releated paper for further information `Balanced Sparsity for
        Efficient DNN Inference on GPU <https://arxiv.org/pdf/1811.00206.pdf>`__.
    balance_gran
        Balance_gran is for special sparse pattern balanced sparsity, Default value is None which means pruning
        without awaring balance, namely normal finegrained pruning.
        If passing list of int, LevelPruner will prune the model in the granularity of multi-dimension block.
        Attention that the length of balance_gran should be smaller than tensor dimension.
        For instance, in Linear operation, length of balance_gran should be equal or smaller than two since
        dimension of pruning weight is two. If setting balbance_gran = [5, 5], sparsity = 0.6, pruner will
        divide pruning parameters into multiple block with tile size (5,5) and each bank has 5 * 5 values
        and 10 values would be kept after pruning. Finegrained pruning is applied in the granularity of block
        so that each block will kept same number of non-zero values after pruning. Such pruning method "balance"
        the non-zero value in tensor which create chance for better hardware acceleration.

        Note: If length of given balance_gran smaller than length of pruning tensor shape, it will be made up
              in right align(such as example 1).

            example 1:
                operation: Linear
                pruning tensor: weight
                pruning tensor shape: [32, 32]
                sparsity: 50%
                balance_gran: [4]

                pruning result: Weight tensor whose shape is [32, 32] will be split into 256 [1, 4] sub blocks.
                                Each sub block will be pruned 2 values.

            example 2:
                operation: Linear
                pruning tensor: weight
                pruning tensor shape: [64, 64]
                sparsity: 25%
                balance_gran: [32, 32]

                pruning result: Weight tensor whose shape is [64, 64] will be split into 4 [32, 32] sub blocks.
                                Each sub block will be pruned 256 values.

    Examples
    --------
        >>> model = ...
        >>> from nni.compression.pytorch.pruning import LevelPruner
        >>> config_list = [{ \'sparsity\': 0.8, \'op_types\': [\'default\'] }]
        >>> pruner = LevelPruner(model, config_list)
        >>> masked_model, masks = pruner.compress()

    For detailed example please refer to
    :githublink:`examples/model_compress/pruning/level_pruning_torch.py <examples/model_compress/pruning/level_pruning_torch.py>`
    '''
    mode: Incomplete
    balance_gran: Incomplete
    def __init__(self, model: Module, config_list: List[Dict], mode: str = 'normal', balance_gran: List | None = None) -> None: ...
    data_collector: Incomplete
    metrics_calculator: Incomplete
    sparsity_allocator: Incomplete
    def reset_tools(self) -> None: ...

class NormPruner(BasicPruner):
    """
    Parameters
    ----------
    model
        Model to be pruned.
    config_list
        Supported keys:
            - sparsity : This is to specify the sparsity for each layer in this config to be compressed.
            - sparsity_per_layer : Equals to sparsity.
            - op_types : Conv2d and Linear are supported in NormPruner.
            - op_names : Operation names to be pruned.
            - op_partial_names: Operation partial names to be pruned, will be autocompleted by NNI.
            - exclude : Set True then the layers setting by op_types and op_names will be excluded from pruning.
    p
        The order of norm.
    mode
        'normal' or 'dependency_aware'.
        If prune the model in a dependency-aware way, this pruner will
        prune the model according to the norm of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if set 'dependency_aware'
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.
    """
    p: Incomplete
    mode: Incomplete
    dummy_input: Incomplete
    def __init__(self, model: Module, config_list: List[Dict], p: int, mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...
    sparsity_allocator: Incomplete
    data_collector: Incomplete
    metrics_calculator: Incomplete
    def reset_tools(self) -> None: ...

class L1NormPruner(NormPruner):
    """
    L1 norm pruner computes the l1 norm of the layer weight on the first dimension,
    then prune the weight blocks on this dimension with smaller l1 norm values.
    i.e., compute the l1 norm of the filters in convolution layer as metric values,
    compute the l1 norm of the weight by rows in linear layer as metric values.

    For more details, please refer to `PRUNING FILTERS FOR EFFICIENT CONVNETS <https://arxiv.org/abs/1608.08710>`__.

    In addition, L1 norm pruner also supports dependency-aware mode.

    Parameters
    ----------
    model
        Model to be pruned.
    config_list
        Supported keys:
            - sparsity : This is to specify the sparsity for each layer in this config to be compressed.
            - sparsity_per_layer : Equals to sparsity.
            - op_types : Conv2d and Linear are supported in L1NormPruner.
            - op_names : Operation names to be pruned.
            - op_partial_names: Operation partial names to be pruned, will be autocompleted by NNI.
            - exclude : Set True then the layers setting by op_types and op_names will be excluded from pruning.
    mode
        'normal' or 'dependency_aware'.
        If prune the model in a dependency-aware way, this pruner will
        prune the model according to the l1-norm of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if set 'dependency_aware'
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.
    """
    def __init__(self, model: Module, config_list: List[Dict], mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...

class L2NormPruner(NormPruner):
    """
    L2 norm pruner is a variant of L1 norm pruner.
    The only different between L2 norm pruner and L1 norm pruner is
    L2 norm pruner prunes the weight with the smallest L2 norm of the weights.

    L2 norm pruner also supports dependency-aware mode.

    Parameters
    ----------
    model
        Model to be pruned.
    config_list
        Supported keys:
            - sparsity : This is to specify the sparsity for each layer in this config to be compressed.
            - sparsity_per_layer : Equals to sparsity.
            - op_types : Conv2d and Linear are supported in L2NormPruner.
            - op_names : Operation names to be pruned.
            - op_partial_names: Operation partial names to be pruned, will be autocompleted by NNI.
            - exclude : Set True then the layers setting by op_types and op_names will be excluded from pruning.
    mode
        'normal' or 'dependency_aware'.
        If prune the model in a dependency-aware way, this pruner will
        prune the model according to the l2-norm of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if set 'dependency_aware'
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.

    Examples
    --------
        >>> model = ...
        >>> from nni.compression.pytorch.pruning import L2NormPruner
        >>> config_list = [{ 'sparsity': 0.8, 'op_types': ['Conv2d'] }]
        >>> pruner = L2NormPruner(model, config_list)
        >>> masked_model, masks = pruner.compress()

    For detailed example please refer to
    :githublink:`examples/model_compress/pruning/norm_pruning_torch.py <examples/model_compress/pruning/norm_pruning_torch.py>`
    """
    def __init__(self, model: Module, config_list: List[Dict], mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...

class FPGMPruner(BasicPruner):
    """
    FPGM pruner prunes the blocks of the weight on the first dimension with the smallest geometric median.
    FPGM chooses the weight blocks with the most replaceable contribution.

    For more details, please refer to
    `Filter Pruning via Geometric Median for Deep Convolutional Neural Networks Acceleration <https://arxiv.org/abs/1811.00250>`__.

    FPGM pruner also supports dependency-aware mode.

    Parameters
    ----------
    model
        Model to be pruned.
    config_list
        Supported keys:
            - sparsity : This is to specify the sparsity for each layer in this config to be compressed.
            - sparsity_per_layer : Equals to sparsity.
            - op_types : Conv2d and Linear are supported in FPGMPruner.
            - op_names : Operation names to be pruned.
            - op_partial_names: Operation partial names to be pruned, will be autocompleted by NNI.
            - exclude : Set True then the layers setting by op_types and op_names will be excluded from pruning.
    mode
        'normal' or 'dependency_aware'.
        If prune the model in a dependency-aware way, this pruner will
        prune the model according to the FPGM of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if set 'dependency_aware'
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.

    Examples
    --------
        >>> model = ...
        >>> from nni.compression.pytorch.pruning import FPGMPruner
        >>> config_list = [{ 'sparsity': 0.8, 'op_types': ['Conv2d'] }]
        >>> pruner = FPGMPruner(model, config_list)
        >>> masked_model, masks = pruner.compress()

    For detailed example please refer to
    :githublink:`examples/model_compress/pruning/fpgm_pruning_torch.py <examples/model_compress/pruning/fpgm_pruning_torch.py>`
    """
    mode: Incomplete
    dummy_input: Incomplete
    def __init__(self, model: Module, config_list: List[Dict], mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...
    sparsity_allocator: Incomplete
    data_collector: Incomplete
    metrics_calculator: Incomplete
    def reset_tools(self) -> None: ...

class SlimPruner(EvaluatorBasedPruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], evaluator: Evaluator, training_epochs: int, scale: float = 0.0001, mode: str = 'global') -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], trainer: _LEGACY_TRAINER, traced_optimizer: Optimizer, criterion: _LEGACY_CRITERION, training_epochs: int, scale: float = 0.0001, mode: str = 'global') -> None: ...
    def criterion_patch(self, criterion: Callable[[Tensor, Tensor], Tensor]) -> Callable[[Tensor, Tensor], Tensor]: ...
    def loss_patch(self, origin_loss: Tensor): ...
    data_collector: Incomplete
    metrics_calculator: Incomplete
    sparsity_allocator: Incomplete
    def reset_tools(self) -> None: ...

class ActivationPruner(EvaluatorBasedPruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], evaluator: Evaluator, training_steps: int, activation: str = 'relu', mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], trainer: _LEGACY_TRAINER, traced_optimizer: Optimizer, criterion: _LEGACY_CRITERION, training_batches: int, activation: str = 'relu', mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...
    sparsity_allocator: Incomplete
    data_collector: Incomplete
    metrics_calculator: Incomplete
    def reset_tools(self) -> None: ...

class ActivationAPoZRankPruner(ActivationPruner):
    __doc__: Incomplete

class ActivationMeanRankPruner(ActivationPruner):
    __doc__: Incomplete

class TaylorFOWeightPruner(EvaluatorBasedPruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], evaluator: Evaluator, training_steps: int, mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], trainer: _LEGACY_TRAINER, traced_optimizer: Optimizer, criterion: _LEGACY_CRITERION, training_batches: int, mode: str = 'normal', dummy_input: Tensor | None = None) -> None: ...
    sparsity_allocator: Incomplete
    data_collector: Incomplete
    metrics_calculator: Incomplete
    def reset_tools(self) -> None: ...

class ADMMPruner(EvaluatorBasedPruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], evaluator: Evaluator, iterations: int, training_epochs: int, granularity: str = 'fine-grained') -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], trainer: _LEGACY_TRAINER, traced_optimizer: Optimizer, criterion: _LEGACY_CRITERION, iterations: int, training_epochs: int, granularity: str = 'fine-grained') -> None: ...
    U: Incomplete
    def reset(self, model: Module, config_list: List[Dict]): ...
    def criterion_patch(self, origin_criterion: Callable[[Tensor, Tensor], Tensor]): ...
    def loss_patch(self, origin_loss: Tensor): ...
    data_collector: Incomplete
    metrics_calculator: Incomplete
    sparsity_allocator: Incomplete
    def reset_tools(self) -> None: ...
    def compress(self) -> Tuple[Module, Dict]: ...
