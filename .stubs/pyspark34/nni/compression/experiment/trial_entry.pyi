from .config.utils import parse_basic_pruner as parse_basic_pruner, parse_params as parse_params
from nni.algorithms.compression.v2.pytorch.pruning import PruningScheduler as PruningScheduler
from nni.algorithms.compression.v2.pytorch.pruning.tools import AGPTaskGenerator as AGPTaskGenerator
from nni.compression.pytorch.utils import count_flops_params as count_flops_params

def sigmoid(x: float, theta0: float = -0.5, theta1: float = 10) -> float: ...
