from ..utils import Evaluator as Evaluator
from .tools import TaskGenerator as TaskGenerator
from nni.algorithms.compression.v2.pytorch.base import BasePruningScheduler as BasePruningScheduler, Pruner as Pruner, Task as Task, TaskResult as TaskResult
from nni.compression.pytorch.speedup import ModelSpeedup as ModelSpeedup
from torch import Tensor as Tensor
from torch.nn import Module
from typing import Any, Dict, List, Tuple, overload

class EvaluatorBasedPruningScheduler(BasePruningScheduler):
    evaluator: Evaluator
    using_evaluator: bool
    finetuner: _LEGACY_FINETUNER
    dummy_input: Any

class PruningScheduler(EvaluatorBasedPruningScheduler):
    """
    Parameters
    ----------
    pruner
        The pruner used in pruner scheduler.
        The scheduler will use `Pruner.reset(model, config_list)` to reset it in each iteration.
    task_generator
        Used to generate task for each iteration.
    finetuner
        The finetuner handled all finetune logic, use a pytorch module as input.
        It will be called at the end of each iteration if reset_weight is False,
        will be called at the beginning of each iteration otherwise.
    speedup
        If set True, speedup the model at the end of each iteration to make the pruned model compact.
    dummy_input
        If `speedup` is True, `dummy_input` is required for tracing the model in speedup.
    evaluator
        Evaluate the pruned model and give a score.
        If evaluator is None, the best result refers to the latest result.
    reset_weight
        If set True, the model weight will reset to the origin model weight at the end of each iteration step.
    """
    @overload
    def __init__(self, pruner: Pruner, task_generator: TaskGenerator, evaluator: Evaluator, speedup: bool = False, reset_weight: bool = False) -> None: ...
    @overload
    def __init__(self, pruner: Pruner, task_generator: TaskGenerator, finetuner: _LEGACY_FINETUNER | None = None, speedup: bool = False, dummy_input: Tensor | None = None, evaluator: _LEGACY_EVALUATOR | None = None, reset_weight: bool = False) -> None: ...
    def reset(self, model: Module, config_list: List[Dict], masks: Dict[str, Dict[str, Tensor]] = {}): ...
    def generate_task(self) -> Task | None: ...
    def record_task_result(self, task_result: TaskResult): ...
    def pruning_one_step_normal(self, task: Task) -> TaskResult:
        """
        generate masks -> speedup -> finetune -> evaluate
        """
    def pruning_one_step_reset_weight(self, task: Task) -> TaskResult:
        """
        finetune -> generate masks -> reset weight -> speedup -> evaluate
        """
    def pruning_one_step(self, task: Task) -> TaskResult: ...
    def get_best_result(self) -> Tuple[int | str, Module, Dict[str, Dict[str, Tensor]], float | None, List[Dict]] | None: ...
