import comm.base_comm
import traitlets.config
from .comm import Comm as Comm
from _typeshed import Incomplete

logger: Incomplete

class CommManager(comm.base_comm.CommManager, traitlets.config.LoggingConfigurable):
    """A comm manager."""
    kernel: Incomplete
    comms: Incomplete
    targets: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize the manager."""
    def comm_open(self, stream, ident, msg) -> None:
        """Handler for comm_open messages"""
