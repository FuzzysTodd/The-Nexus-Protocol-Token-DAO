import torch
from enum import Enum
from torch._C import _MobileOptimizerType as MobileOptimizerType
from typing import AnyStr, List, Set

class LintCode(Enum):
    BUNDLED_INPUT: int
    REQUIRES_GRAD: int
    DROPOUT: int
    BATCHNORM: int

def optimize_for_mobile(script_module: torch.jit.ScriptModule, optimization_blocklist: Set[MobileOptimizerType] | None = None, preserved_methods: List[AnyStr] | None = None, backend: str = 'CPU') -> torch.jit.RecursiveScriptModule:
    """
    Args:
        script_module: An instance of torch script module with type of ScriptModule.
        optimization_blocklist: A set with type of MobileOptimizerType. When set is not passed,
            optimization method will run all the optimizer pass; otherwise, optimizer
            method will run the optimization pass that is not included inside optimization_blocklist.
        preserved_methods: A list of methods that needed to be preserved when freeze_module pass is invoked
        backend: Device type to use for running the result model ('CPU'(default), 'Vulkan' or 'Metal').
    Returns:
        A new optimized torch script module
    """
def generate_mobile_module_lints(script_module: torch.jit.ScriptModule):
    """
    Args:
        script_module: An instance of torch script module with type of ScriptModule

    Returns:
        lint_map: A list of dictionary that contains modules lints
    """
