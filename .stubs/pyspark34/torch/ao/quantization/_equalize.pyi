__all__ = ['set_module_weight', 'set_module_bias', 'get_module_weight', 'get_module_bias', 'max_over_ndim', 'min_over_ndim', 'channel_range', 'cross_layer_equalization', 'equalize', 'converged']

def set_module_weight(module, weight) -> None: ...
def set_module_bias(module, bias) -> None: ...
def get_module_weight(module): ...
def get_module_bias(module): ...
def max_over_ndim(input, axis_list, keepdim: bool = False):
    """ Applies 'torch.max' over the given axises
    """
def min_over_ndim(input, axis_list, keepdim: bool = False):
    """ Applies 'torch.min' over the given axises
    """
def channel_range(input, axis: int = 0):
    """ finds the range of weights associated with a specific channel
    """
def cross_layer_equalization(module1, module2, output_axis: int = 0, input_axis: int = 1) -> None:
    """ Given two adjacent tensors', the weights are scaled such that
    the ranges of the first tensors' output channel are equal to the
    ranges of the second tensors' input channel
    """
def equalize(model, paired_modules_list, threshold: float = 0.0001, inplace: bool = True):
    """ Given a list of adjacent modules within a model, equalization will
    be applied between each pair, this will repeated until convergence is achieved

    Keeps a copy of the changing modules from the previous iteration, if the copies
    are not that different than the current modules (determined by converged_test),
    then the modules have converged enough that further equalizing is not necessary

    Implementation of this referced section 4.1 of this paper https://arxiv.org/pdf/1906.04721.pdf

    Args:
        model: a model (nn.module) that equalization is to be applied on
        paired_modules_list: a list of lists where each sublist is a pair of two
            submodules found in the model, for each pair the two submodules generally
            have to be adjacent in the model to get expected/reasonable results
        threshold: a number used by the converged function to determine what degree
            similarity between models is necessary for them to be called equivalent
        inplace: determines if function is inplace or not
    """
def converged(curr_modules, prev_modules, threshold: float = 0.0001):
    """ Tests for the summed norm of the differences between each set of modules
    being less than the given threshold

    Takes two dictionaries mapping names to modules, the set of names for each dictionary
    should be the same, looping over the set of names, for each name take the differnce
    between the associated modules in each dictionary

    """
