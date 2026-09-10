from ..utils import Evaluator as Evaluator, OptimizerConstructHelper as OptimizerConstructHelper
from .basic_pruner import ADMMPruner as ADMMPruner
from .iterative_pruner import IterativePruner as IterativePruner, SimulatedAnnealingPruner as SimulatedAnnealingPruner
from .tools import LotteryTicketTaskGenerator as LotteryTicketTaskGenerator
from _typeshed import Incomplete
from torch import Tensor as Tensor
from torch.nn import Module as Module
from typing import Callable, Dict, List, overload

class AutoCompressTaskGenerator(LotteryTicketTaskGenerator):
    def __init__(self, total_iteration: int, origin_model: Module, origin_config_list: List[Dict], origin_masks: Dict[str, Dict[str, Tensor]] = {}, sa_params: Dict = {}, log_dir: str = '.', keep_intermediate_result: bool = False) -> None: ...
    def reset(self, model: Module, config_list: List[Dict] = [], masks: Dict[str, Dict[str, Tensor]] = {}): ...
    def allocate_sparsity(self, new_config_list: List[Dict], model: Module, masks: Dict[str, Dict[str, Tensor]]): ...

class AutoCompressPruner(IterativePruner):
    __doc__: Incomplete
    @overload
    def __init__(self, model: Module, config_list: List[Dict], total_iteration: int, admm_params: Dict, sa_params: Dict, log_dir: str = '.', keep_intermediate_result: bool = False, evaluator: Evaluator | None = None, speedup: bool = False) -> None: ...
    @overload
    def __init__(self, model: Module, config_list: List[Dict], total_iteration: int, admm_params: Dict, sa_params: Dict, log_dir: str = '.', keep_intermediate_result: bool = False, finetuner: Callable[[Module], None] | None = None, speedup: bool = False, dummy_input: Tensor | None = None, evaluator: Callable[[Module], float] | None = None) -> None: ...
