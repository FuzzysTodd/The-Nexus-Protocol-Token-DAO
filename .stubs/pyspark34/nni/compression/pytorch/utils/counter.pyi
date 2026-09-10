from _typeshed import Incomplete

__all__ = ['count_flops_params']

class ModelProfiler:
    ops: Incomplete
    mode: Incomplete
    results: Incomplete
    def __init__(self, custom_ops: Incomplete | None = None, mode: str = 'default') -> None:
        """
        ModelProfiler is used to share state to hooks.

        Parameters
        ----------
        custom_ops: dict
            a mapping of (module -> torch.nn.Module : custom operation)
            the custom operation is a callback funtion to calculate
            the module flops, parameters and the weight shape, it will overwrite the default operation.
            for reference, please see ``self.ops``.
        mode:
            the mode of how to collect information. If the mode is set to `default`,
            only the information of convolution, linear and rnn modules will be collected.
            If the mode is set to `full`, other operations will also be collected.
        """
    def count_module(self, m, x, y, name) -> None: ...
    def sum_flops(self): ...
    def sum_params(self): ...
    def format_results(self): ...

def count_flops_params(model, x, custom_ops: Incomplete | None = None, verbose: bool = True, mode: str = 'default'):
    '''
    Count FLOPs and Params of the given model. This function would
    identify the mask on the module and take the pruned shape into consideration.
    Note that, for sturctured pruning, we only identify the remained filters
    according to its mask, and do not take the pruned input channels into consideration,
    so the calculated FLOPs will be larger than real number.

    The FLOPs is counted "per sample", which means that input has a batch size larger than 1,
    the calculated FLOPs should not differ from batch size of 1.

    Parameters
    ---------
    model : nn.Module
        Target model.
    x : tuple or tensor
        The input shape of data (a tuple), a tensor or a tuple of tensor as input data.
    custom_ops : dict
        A mapping of (module -> torch.nn.Module : custom operation)
        the custom operation is a callback funtion to calculate
        the module flops and parameters, it will overwrite the default operation.
        for reference, please see ``ops`` in ``ModelProfiler``.
    verbose : bool
        If False, mute detail information about modules. Default is True.
    mode : str
        the mode of how to collect information. If the mode is set to ``default``,
        only the information of convolution and linear will be collected.
        If the mode is set to ``full``, other operations will also be collected.

    Returns
    -------
    tuple of int, int and dict
        Representing total FLOPs, total parameters, and a detailed list of results respectively.
        The list of results are a list of dict, each of which contains (name, module_type, weight_shape,
        flops, params, input_size, output_size) as its keys.
    '''
