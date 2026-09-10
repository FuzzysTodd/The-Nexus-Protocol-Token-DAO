from _typeshed import Incomplete
from torch import optim as optim
from typing import Type

functional_optim_map: Incomplete

def register_functional_optim(key, optim) -> None:
    '''
    Interface to insert a new functional optimizer to functional_optim_map
    ``fn_optim_key`` and ``fn_optimizer`` are user defined. The optimizer and key
    need not be of :class:`torch.optim.Optimizer` (e.g. for custom optimizers)
    Example::
        >>> # import the new functional optimizer
        >>> # xdoctest: +SKIP
        >>> from xyz import fn_optimizer
        >>> from torch.distributed.optim.utils import register_functional_optim
        >>> fn_optim_key = "XYZ_optim"
        >>> register_functional_optim(fn_optim_key, fn_optimizer)
    '''
def as_functional_optim(optim_cls: Type, *args, **kwargs): ...
