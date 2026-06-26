from ..utils import Evaluator as Evaluator, compute_sparsity as compute_sparsity, config_list_canonical as config_list_canonical
from .iterative_pruner import IterativePruner as IterativePruner, PRUNER_DICT as PRUNER_DICT
from .tools import TaskGenerator as TaskGenerator
from .tools.rl_env import AMCEnv as AMCEnv, DDPG as DDPG
from _typeshed import Incomplete
from nni.algorithms.compression.v2.pytorch.base import Task as Task, TaskResult as TaskResult
from nni.compression.pytorch.utils import count_flops_params as count_flops_params
from torch import Tensor as Tensor
from torch.nn import Module as Module
from typing import Callable, Dict, List, overload

class AMCTaskGenerator(TaskGenerator):
    """
    Parameters
    ----------
    total_episode
        The total episode number.
    dummy_input
        Use to inference and count the flops.
    origin_model
        The origin unwrapped pytorch model to be pruned.
    origin_config_list
        The origin config list provided by the user. Note that this config_list is directly config the origin model.
        This means the sparsity provided by the origin_masks should also be recorded in the origin_config_list.
    origin_masks
        The pre masks on the origin model. This mask maybe user-defined or maybe generate by previous pruning.
    log_dir
        The log directory use to saving the task generator log.
    keep_intermediate_result
        If keeping the intermediate result, including intermediate model and masks during each iteration.
    ddpg_params
        The ddpg agent parameters.
    target : str
        'flops' or 'params'. Note that the sparsity in other pruners always means the parameters sparse,
        but in AMC, you can choose flops sparse. This parameter is used to explain what the sparsity setting in config_list refers to.
    """
    total_episode: Incomplete
    current_episode: int
    dummy_input: Incomplete
    ddpg_params: Incomplete
    target: Incomplete
    config_list_copy: Incomplete
    def __init__(self, total_episode: int, dummy_input: Tensor, origin_model: Module, origin_config_list: List[Dict], origin_masks: Dict[str, Dict[str, Tensor]] = {}, log_dir: str = '.', keep_intermediate_result: bool = False, ddpg_params: Dict = {}, target: str = 'flops') -> None: ...
    T: Incomplete
    action: Incomplete
    observation: Incomplete
    warmup_episode: Incomplete
    env: Incomplete
    agent: Incomplete
    def init_pending_tasks(self) -> List[Task]: ...
    temp_config_list: Incomplete
    def generate_tasks(self, task_result: TaskResult) -> List[Task]: ...

class AMCPruner(IterativePruner):
    __doc__: Incomplete
    @overload
    def __init__(self, total_episode: int, model: Module, config_list: List[Dict], evaluator: Evaluator, pruning_algorithm: str = 'l1', log_dir: str = '.', keep_intermediate_result: bool = False, ddpg_params: dict = {}, pruning_params: dict = {}, target: str = 'flops') -> None: ...
    @overload
    def __init__(self, total_episode: int, model: Module, config_list: List[Dict], dummy_input: Tensor, evaluator: Callable[[Module], float], pruning_algorithm: str = 'l1', log_dir: str = '.', keep_intermediate_result: bool = False, finetuner: Callable[[Module], None] | None = None, ddpg_params: dict = {}, pruning_params: dict = {}, target: str = 'flops') -> None: ...
