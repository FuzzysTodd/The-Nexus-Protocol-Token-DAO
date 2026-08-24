from ..websocket import KernelWebsocketHandler as KernelWebsocketHandler
from .abc import KernelWebsocketConnectionABC as KernelWebsocketConnectionABC
from .base import BaseKernelWebsocketConnection as BaseKernelWebsocketConnection, deserialize_binary_message as deserialize_binary_message, deserialize_msg_from_ws_v1 as deserialize_msg_from_ws_v1, serialize_binary_message as serialize_binary_message, serialize_msg_to_ws_v1 as serialize_msg_to_ws_v1
from _typeshed import Incomplete

class ZMQChannelsWebsocketConnection(BaseKernelWebsocketConnection):
    """A Jupyter Server Websocket Connection"""
    limit_rate: Incomplete
    iopub_msg_rate_limit: Incomplete
    iopub_data_rate_limit: Incomplete
    rate_limit_window: Incomplete
    @property
    def write_message(self):
        """Alias to the websocket handler's write_message method."""
    channels: Incomplete
    kernel_info_channel: Incomplete
    session_key: Incomplete
    @classmethod
    async def close_all(cls) -> None:
        """Tornado does not provide a way to close open sockets, so add one."""
    @property
    def subprotocol(self):
        """The sub protocol."""
    def create_stream(self) -> None:
        """Create a stream."""
    def nudge(self):
        """Nudge the zmq connections with kernel_info_requests
        Returns a Future that will resolve when we have received
        a shell or control reply and at least one iopub message,
        ensuring that zmq subscriptions are established,
        sockets are fully connected, and kernel is responsive.
        Keeps retrying kernel_info_request until these are both received.
        """
    async def prepare(self) -> None:
        """Prepare a kernel connection."""
    def connect(self):
        """Handle a connection."""
    def close(self):
        """Close the connection."""
    def disconnect(self) -> None:
        """Handle a disconnect."""
    def handle_incoming_message(self, incoming_msg: str) -> None:
        """Handle incoming messages from Websocket to ZMQ Sockets."""
    def handle_outgoing_message(self, stream: str, outgoing_msg: list) -> None:
        """Handle the outgoing messages from ZMQ sockets to Websocket."""
    def get_part(self, field, value, msg_list):
        """Get a part of a message."""
    def request_kernel_info(self):
        """send a request for kernel_info"""
    def write_stderr(self, error_message, parent_header) -> None:
        """Write a message to stderr."""
    def on_kernel_restarted(self) -> None:
        """Handle a kernel restart."""
    def on_restart_failed(self) -> None:
        """Handle a kernel restart failure."""
