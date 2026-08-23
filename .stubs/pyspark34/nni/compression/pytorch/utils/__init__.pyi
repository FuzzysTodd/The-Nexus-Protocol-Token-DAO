from .utils import *
from .shape_dependency import *
from .counter import count_flops_params as count_flops_params
from .mask_conflict import ChannelMaskConflict as ChannelMaskConflict, GroupMaskConflict as GroupMaskConflict
from .sensitivity_analysis import SensitivityAnalysis as SensitivityAnalysis

def not_safe_to_prune(model, dummy_input):
    """
    Get the layers that are not safe to prune(may bring the shape conflict).
    For example, if the output tensor of a conv layer is directly followed by
    a shape-dependent function(such as reshape/view), then this conv layer
    may be not safe to be pruned. Pruning may change the output shape of
    this conv layer and result in shape problems. This function find all the
    layers that directly followed by the shape-dependent functions(view, reshape, etc).
    If you run the inference after the speedup and run into a shape related error,
    please exclude the layers returned by this function and try again.

    Parameters
    ----------
    model: torch.nn.Module
        The target model to prune.
    dummy_input: torch.Tensor/list of torch.Tensor/tuple of Tensor
    """
