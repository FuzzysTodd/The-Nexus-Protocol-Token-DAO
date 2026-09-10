from .base import TaskGenerator as TaskGenerator
from _typeshed import Incomplete
from nni.algorithms.compression.v2.pytorch.base import Task as Task, TaskResult as TaskResult
from nni.algorithms.compression.v2.pytorch.utils import compute_sparsity as compute_sparsity, config_list_canonical as config_list_canonical, get_model_weights_numel as get_model_weights_numel
from pathlib import Path
from torch import Tensor as Tensor
from torch.nn import Module as Module
from typing import Dict, List

class FunctionBasedTaskGenerator(TaskGenerator):
    total_iteration: Incomplete
    skip_first_iteration: Incomplete
    def __init__(self, total_iteration: int, origin_model: Module, origin_config_list: List[Dict], origin_masks: Dict[str, Dict[str, Tensor]] = {}, log_dir: str = '.', keep_intermediate_result: bool = False, skip_first_iteration: bool = False) -> None:
        """
        Parameters
        ----------
        total_iteration
            The total iteration number.
        origin_model
            The origin unwrapped pytorch model to be pruned.
        origin_config_list
            The origin config list provided by the user. Note that this config_list is directly config the origin model.
            This means the sparsity provided by the origin_masks should also be recorded in the origin_config_list.
        origin_masks
            The pre masks on the origin model. This mask maybe user-defined or maybe generate by previous pruning.
        log_dir
            The log directory used to save the task generator log.
        keep_intermediate_result
            If keeping the intermediate result, including intermediate model and masks during each iteration.
        skip_first_iteration
            If skipping the first iteration, the iteration counter will start at 1.
            In these function-based iterative pruning algorithms, iteration `0` means a warm up stage with `sparsity = 0`.
            If the `original_model` is a pre-trained model, the first iteration is usually can be skipped.
        """
    current_iteration: Incomplete
    target_sparsity: Incomplete
    def reset(self, model: Module, config_list: List[Dict] = [], masks: Dict[str, Dict[str, Tensor]] = {}): ...
    def init_pending_tasks(self) -> List[Task]: ...
    def generate_tasks(self, task_result: TaskResult) -> List[Task]: ...
    def generate_config_list(self, target_sparsity: List[Dict], iteration: int, compact2origin_sparsity: List[Dict]) -> List[Dict]: ...
    def allocate_sparsity(self, new_config_list: List[Dict], model: Module, masks: Dict[str, Dict[str, Tensor]]): ...

class AGPTaskGenerator(FunctionBasedTaskGenerator):
    def generate_config_list(self, target_sparsity: List[Dict], iteration: int, compact2origin_sparsity: List[Dict]) -> List[Dict]: ...

class LinearTaskGenerator(FunctionBasedTaskGenerator):
    def generate_config_list(self, target_sparsity: List[Dict], iteration: int, compact2origin_sparsity: List[Dict]) -> List[Dict]: ...

class LotteryTicketTaskGenerator(FunctionBasedTaskGenerator):
    current_iteration: int
    target_sparsity: Incomplete
    def reset(self, model: Module, config_list: List[Dict] = [], masks: Dict[str, Dict[str, Tensor]] = {}): ...
    def generate_config_list(self, target_sparsity: List[Dict], iteration: int, compact2origin_sparsity: List[Dict]) -> List[Dict]: ...

class SimulatedAnnealingTaskGenerator(TaskGenerator):
    start_temperature: Incomplete
    stop_temperature: Incomplete
    cool_down_rate: Incomplete
    perturbation_magnitude: Incomplete
    def __init__(self, origin_model: Module | None, origin_config_list: List[Dict] | None, origin_masks: Dict[str, Dict[str, Tensor]] = {}, start_temperature: float = 100, stop_temperature: float = 20, cool_down_rate: float = 0.9, perturbation_magnitude: float = 0.35, log_dir: str | Path = '.', keep_intermediate_result: bool = False) -> None:
        """
        Parameters
        ----------
        origin_model
            The origin unwrapped pytorch model to be pruned.
        origin_config_list
            The origin config list provided by the user. Note that this config_list is directly config the origin model.
            This means the sparsity provided by the origin_masks should also be recorded in the origin_config_list.
        origin_masks
            The pre masks on the origin model. This mask maybe user-defined or maybe generate by previous pruning.
        start_temperature
            Start temperature of the simulated annealing process.
        stop_temperature
            Stop temperature of the simulated annealing process.
        cool_down_rate
            Cool down rate of the temperature.
        perturbation_magnitude
            Initial perturbation magnitude to the sparsities. The magnitude decreases with current temperature.
        log_dir
            The log directory use to saving the task generator log.
        keep_intermediate_result
            If keeping the intermediate result, including intermediate model and masks during each iteration.
        """
    current_temperature: Incomplete
    target_sparsity_list: Incomplete
    def reset(self, model: Module, config_list: List[Dict] = [], masks: Dict[str, Dict[str, Tensor]] = {}): ...
    temp_model_path: Incomplete
    temp_masks_path: Incomplete
    def init_pending_tasks(self) -> List[Task]: ...
    def generate_tasks(self, task_result: TaskResult) -> List[Task]: ...
