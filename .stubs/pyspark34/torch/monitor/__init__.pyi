from torch._C._monitor import *
from torch.utils.tensorboard import SummaryWriter as SummaryWriter

STAT_EVENT: str

class TensorboardEventHandler:
    '''
    TensorboardEventHandler is an event handler that will write known events to
    the provided SummaryWriter.

    This currently only supports ``torch.monitor.Stat`` events which are logged
    as scalars.

    Example:
        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_MONITOR)
        >>> # xdoctest: +REQUIRES(module:tensorboard)
        >>> from torch.utils.tensorboard import SummaryWriter
        >>> from torch.monitor import TensorboardEventHandler, register_event_handler
        >>> writer = SummaryWriter("log_dir")
        >>> register_event_handler(TensorboardEventHandler(writer))
    '''
    def __init__(self, writer: SummaryWriter) -> None:
        """
        Constructs the ``TensorboardEventHandler``.
        """
    def __call__(self, event: Event) -> None: ...
