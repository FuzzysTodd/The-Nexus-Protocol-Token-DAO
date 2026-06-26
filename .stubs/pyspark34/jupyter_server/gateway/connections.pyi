from ..services.kernels.connection.base import BaseKernelWebsocketConnection as BaseKernelWebsocketConnection
from ..utils import url_path_join as url_path_join
from .managers import GatewayClient as GatewayClient
from _typeshed import Incomplete
from typing import Any

class GatewayWebSocketConnection(BaseKernelWebsocketConnection):
    """Web socket connection that proxies to a kernel/enterprise gateway."""
    ws: Incomplete
    ws_future: Incomplete
    disconnected: Incomplete
    retry: Incomplete
    async def connect(self):
        """Connect to the socket."""
    def disconnect(self) -> None:
        """Handle a disconnect."""
    def handle_outgoing_message(self, incoming_msg: str, *args: Any) -> None:
        """Send message to the notebook client."""
    def handle_incoming_message(self, message: str) -> None:
        """Send message to gateway server."""
