import comm.base_comm
import traitlets.config
from _typeshed import Incomplete
from ipykernel.kernelbase import Kernel

__all__ = ['Comm']

class BaseComm(comm.base_comm.BaseComm):
    """The base class for comms."""
    kernel: Kernel | None
    def publish_msg(self, msg_type, data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None, **keys) -> None:
        """Helper for sending a comm message on IOPub"""

class Comm(BaseComm, traitlets.config.LoggingConfigurable):
    """Class for communicating between a Frontend and a Kernel"""
    kernel: Incomplete
    comm_id: Incomplete
    primary: Incomplete
    target_name: Incomplete
    target_module: Incomplete
    topic: Incomplete
    def __init__(self, target_name: str = '', data: Incomplete | None = None, metadata: Incomplete | None = None, buffers: Incomplete | None = None, show_warning: bool = True, **kwargs) -> None:
        """Initialize a comm."""
