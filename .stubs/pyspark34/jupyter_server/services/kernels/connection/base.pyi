from .abc import KernelWebsocketConnectionABC as KernelWebsocketConnectionABC
from _typeshed import Incomplete
from traitlets.config import LoggingConfigurable

def serialize_binary_message(msg):
    """serialize a message as a binary blob

    Header:

    4 bytes: number of msg parts (nbufs) as 32b int
    4 * nbufs bytes: offset for each buffer as integer as 32b int

    Offsets are from the start of the buffer, including the header.

    Returns
    -------
    The message serialized to bytes.

    """
def deserialize_binary_message(bmsg):
    """deserialize a message from a binary blog

    Header:

    4 bytes: number of msg parts (nbufs) as 32b int
    4 * nbufs bytes: offset for each buffer as integer as 32b int

    Offsets are from the start of the buffer, including the header.

    Returns
    -------
    message dictionary
    """
def serialize_msg_to_ws_v1(msg_or_list, channel, pack: Incomplete | None = None):
    """Serialize a message using the v1 protocol."""
def deserialize_msg_from_ws_v1(ws_msg):
    """Deserialize a message using the v1 protocol."""

class BaseKernelWebsocketConnection(LoggingConfigurable):
    """A configurable base class for connecting Kernel WebSockets to ZMQ sockets."""
    kernel_ws_protocol: Incomplete
    @property
    def kernel_manager(self):
        """The kernel manager."""
    @property
    def multi_kernel_manager(self):
        """The multi kernel manager."""
    @property
    def kernel_id(self):
        """The kernel id."""
    @property
    def session_id(self):
        """The session id."""
    kernel_info_timeout: Incomplete
    session: Incomplete
    websocket_handler: Incomplete
    async def connect(self) -> None:
        """Handle a connect."""
    async def disconnect(self) -> None:
        """Handle a disconnect."""
    def handle_incoming_message(self, incoming_msg: str) -> None:
        """Handle an incoming message."""
    def handle_outgoing_message(self, stream: str, outgoing_msg: list) -> None:
        """Handle an outgoing message."""
