import torch
from _typeshed import Incomplete
from dataclasses import dataclass
from torch.autograd import Variable as Variable

class _OptimizerHookState:
    """
    Holds state for running optimizer in-line after DDP communication hook.
    Currently contains only optimizer class which must have a method `step_param`.
    """
    functional_optimizer: Incomplete
    def __init__(self, functional_optim, params: Incomplete | None = None) -> None: ...

@dataclass
class _OptimInBackwardHookState:
    optim_stream: torch.cuda.Stream
    wait_for_optim_stream_enqueued: bool
    def __init__(self, optim_stream, wait_for_optim_stream_enqueued) -> None: ...
