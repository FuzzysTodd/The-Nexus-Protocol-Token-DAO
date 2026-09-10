from ..base.handlers import APIHandler as APIHandler, JupyterHandler as JupyterHandler
from ..services.kernelspecs.handlers import kernel_name_regex as kernel_name_regex
from ..utils import url_path_join as url_path_join
from .managers import GatewayClient as GatewayClient
from _typeshed import Incomplete
from tornado.websocket import WebSocketHandler
from traitlets.config.configurable import LoggingConfigurable

GATEWAY_WS_PING_INTERVAL_SECS: Incomplete

class WebSocketChannelsHandler(WebSocketHandler, JupyterHandler):
    """Gateway web socket channels handler."""
    session: Incomplete
    gateway: Incomplete
    kernel_id: Incomplete
    ping_callback: Incomplete
    def check_origin(self, origin: Incomplete | None = None):
        """Check origin for the socket."""
    def set_default_headers(self) -> None:
        """Undo the set_default_headers in JupyterHandler which doesn't make sense for websockets"""
    def get_compression_options(self):
        """Get the compression options for the socket."""
    def authenticate(self) -> None:
        """Run before finishing the GET request

        Extend this method to add logic that should fire before
        the websocket finishes completing.
        """
    def initialize(self) -> None:
        """Intialize the socket."""
    async def get(self, kernel_id, *args, **kwargs) -> None:
        """Get the socket."""
    def send_ping(self) -> None:
        """Send a ping to the socket."""
    def open(self, kernel_id, *args, **kwargs) -> None:
        """Handle web socket connection open to notebook server and delegate to gateway web socket handler"""
    def on_message(self, message) -> None:
        """Forward message to gateway web socket handler."""
    def write_message(self, message, binary: bool = False) -> None:
        """Send message back to notebook client.  This is called via callback from self.gateway._read_messages."""
    def on_close(self) -> None:
        """Handle a closing socket."""

class GatewayWebSocketClient(LoggingConfigurable):
    """Proxy web socket connection to a kernel/enterprise gateway."""
    kernel_id: Incomplete
    ws: Incomplete
    ws_future: Incomplete
    disconnected: bool
    retry: int
    def __init__(self, **kwargs) -> None:
        """Initialize the gateway web socket client."""
    def on_open(self, kernel_id, message_callback, **kwargs) -> None:
        """Web socket connection open against gateway server."""
    def on_message(self, message):
        """Send message to gateway server."""
    def on_close(self) -> None:
        """Web socket closed event."""

class GatewayResourceHandler(APIHandler):
    """Retrieves resources for specific kernelspec definitions from kernel/enterprise gateway."""
    async def get(self, kernel_name, path, include_body: bool = True) -> None:
        """Get a gateway resource by name and path."""

default_handlers: Incomplete
