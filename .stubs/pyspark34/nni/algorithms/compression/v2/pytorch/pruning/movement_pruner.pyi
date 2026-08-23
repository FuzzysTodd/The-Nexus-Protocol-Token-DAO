from ..utils import Evaluator as Evaluator, Scaling as Scaling
from ..utils.external.huggingface import parser_factory as parser_factory
from .tools import NormalSparsityAllocator as NormalSparsityAllocator, StraightMetricsCalculator as StraightMetricsCalculator, ThresholdSparsityAllocator as ThresholdSparsityAllocator
from .tools.base import EvaluatorBasedDataCollector as EvaluatorBasedDataCollector, TrainerBasedDataCollector as TrainerBasedDataCollector
from _typeshed import Incomplete
from nni.algorithms.compression.v2.pytorch.base import LayerInfo as LayerInfo, PrunerModuleWrapper as PrunerModuleWrapper
from nni.algorithms.compression.v2.pytorch.pruning.basic_pruner import EXCLUDE_SCHEMA as EXCLUDE_SCHEMA, EvaluatorBasedPruner as EvaluatorBasedPruner, INTERNAL_SCHEMA as INTERNAL_SCHEMA, NORMAL_SCHEMA as NORMAL_SCHEMA
from nni.algorithms.compression.v2.pytorch.utils import CompressorSchema as CompressorSchema
from torch import Tensor as Tensor, autograd
from torch.nn import Module as Module
from torch.optim import Optimizer
from typing import Callable, Dict, List, Tuple, overload
from typing_extensions import Literal

class PrunerScoredModuleWrapper(PrunerModuleWrapper):
    """
    Wrap a module to enable data parallel, forward method customization and buffer registeration.
    Different from `PrunerModuleWrapper`, `PrunerScoredModuleWrapper` will record the gradient.

    Parameters
    ----------
    module
        The module user wants to compress.
    config
        The configurations that users specify for compression.
    module_name
        The name of the module to compress, wrapper module shares same name.
    """
    weight_score: Incomplete
    def __init__(self, module: Module, module_name: str, config: Dict, score_size: List[int] | None = None) -> None: ...
    def forward(self, *inputs): ...

class _StraightThrough(autograd.Function):
    """
    Straight through the gradient to the score, then the score = initial_score + sum(-lr * grad(weight) * weight).
    """
    @staticmethod
    def forward(ctx, score, masks): ...
    @staticmethod
    def backward(ctx, gradOutput): ...

class WeightScoreTrainerBasedDataCollector(TrainerBasedDataCollector):
    """
    Collect all weight_score in wrappers as data used to calculate metrics.
    """
    def collect(self) -> Dict[str, Tensor]: ...

class EvaluatorBasedScoreDataCollector(EvaluatorBasedDataCollector):
    """
    Collect all weight_score in wrappers as data used to calculate metrics.
    """
    def collect(self) -> Dict[str, Tensor]: ...

class MovementPruner(EvaluatorBasedPruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], evaluator: Evaluator, warm_up_step: int, cool_down_beginning_step: int, training_epochs: int | None = None, training_steps: int | None = None, regular_scale: float | None = None, movement_mode: Literal['hard', 'soft'] = 'hard', sparse_granularity: Literal['auto', 'finegrained'] = 'finegrained') -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], trainer: Callable[[Module, Optimizer, Callable], None], traced_optimizer: Optimizer, criterion: Callable[[Tensor, Tensor], Tensor], training_epochs: int, warm_up_step: int, cool_down_beginning_step: int) -> None: ...
    def cubic_schedule(self, current_step: int): ...
    metrics_calculator: Incomplete
    sparsity_allocator: Incomplete
    step_counter: int
    data_collector: Incomplete
    def reset_tools(self): ...
    def compress(self) -> Tuple[Module, Dict]: ...
