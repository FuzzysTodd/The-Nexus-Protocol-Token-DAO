from ..utils import Evaluator
from .basic_scheduler import PruningScheduler, _LEGACY_EVALUATOR, _LEGACY_FINETUNER
from _typeshed import Incomplete
from pathlib import Path
from torch import Tensor
from torch.nn import Module
from typing import Any, Dict, List, overload

__all__ = ['LinearPruner', 'AGPPruner', 'LotteryTicketPruner', 'SimulatedAnnealingPruner']

class IterativePruner(PruningScheduler):
    def export_model(self, *args, **kwargs) -> None:
        """
        Deprecated function.
        """

class LinearPruner(IterativePruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], pruning_algorithm: str, total_iteration: int, log_dir: str = '.', keep_intermediate_result: bool = False, evaluator: Evaluator | None = None, speedup: bool = False, pruning_params: Dict = {}) -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], pruning_algorithm: str, total_iteration: int, log_dir: str = '.', keep_intermediate_result: bool = False, finetuner: _LEGACY_FINETUNER | None = None, speedup: bool = False, dummy_input: Any | None = None, evaluator: _LEGACY_EVALUATOR | None = None, pruning_params: Dict = {}) -> None: ...

class AGPPruner(IterativePruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], pruning_algorithm: str, total_iteration: int, log_dir: str = '.', keep_intermediate_result: bool = False, evaluator: Evaluator | None = None, speedup: bool = False, pruning_params: Dict = {}) -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], pruning_algorithm: str, total_iteration: int, log_dir: str = '.', keep_intermediate_result: bool = False, finetuner: _LEGACY_FINETUNER | None = None, speedup: bool = False, dummy_input: Any | None = None, evaluator: _LEGACY_EVALUATOR | None = None, pruning_params: Dict = {}) -> None: ...

class LotteryTicketPruner(IterativePruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], pruning_algorithm: str, total_iteration: int, log_dir: str = '.', keep_intermediate_result: bool = False, evaluator: Evaluator | None = None, speedup: bool = False, reset_weight: bool = True, pruning_params: Dict = {}) -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], pruning_algorithm: str, total_iteration: int, log_dir: str = '.', keep_intermediate_result: bool = False, finetuner: _LEGACY_FINETUNER | None = None, speedup: bool = False, dummy_input: Tensor | None = None, evaluator: _LEGACY_EVALUATOR | None = None, reset_weight: bool = True, pruning_params: Dict = {}) -> None: ...

class SimulatedAnnealingPruner(IterativePruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], evaluator: Evaluator, start_temperature: float = 100, stop_temperature: float = 20, cool_down_rate: float = 0.9, perturbation_magnitude: float = 0.35, pruning_algorithm: str = 'level', pruning_params: Dict = {}, log_dir: str | Path = '.', keep_intermediate_result: bool = False, speedup: bool = False) -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], evaluator: _LEGACY_EVALUATOR, start_temperature: float = 100, stop_temperature: float = 20, cool_down_rate: float = 0.9, perturbation_magnitude: float = 0.35, pruning_algorithm: str = 'level', pruning_params: Dict = {}, log_dir: str | Path = '.', keep_intermediate_result: bool = False, finetuner: _LEGACY_FINETUNER | None = None, speedup: bool = False, dummy_input: Tensor | None = None) -> None: ...
