import torch
from torch.distributed import ProcessGroup
from typing import Dict, Iterable, Iterator

__all__ = ['average_parameters', 'get_params_to_average', 'average_parameters_or_parameter_groups']

def average_parameters(params: Iterator[torch.nn.Parameter], process_group: ProcessGroup):
    """
    Averages all the given parameters.
    For allreduce efficiency, all the parameters are flattened into a contiguous buffer.
    Thus, it requires extra memory of the same size as the given parameters.
    """
def get_params_to_average(params: Iterable[torch.nn.Parameter] | Iterable[Dict[str, torch.nn.Parameter]]):
    """
    Returns a list of parameters that need to average, which filters out the parameters that do not contain any gradients.
    Args:
        params: The parameters of a model or parameter groups of an optimizer.
    """
def average_parameters_or_parameter_groups(params: Iterable[torch.nn.Parameter] | Iterable[Dict[str, torch.nn.Parameter]], process_group: ProcessGroup):
    """
    Averages parameters of a model or parameter groups of an optimizer.
    """
