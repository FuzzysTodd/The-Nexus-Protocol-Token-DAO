from _typeshed import Incomplete
from jupyter_server.base.handlers import JupyterHandler as JupyterHandler
from jupyter_server.base.websocket import WebSocketMixin as WebSocketMixin
from tornado.websocket import WebSocketHandler

AUTH_RESOURCE: str

class KernelWebsocketHandler(WebSocketMixin, WebSocketHandler, JupyterHandler):
    """The kernels websocket should connect"""
    auth_resource = AUTH_RESOURCE
    @property
    def kernel_websocket_connection_class(self):
        """The kernel websocket connection class."""
    def set_default_headers(self) -> None:
        """Undo the set_default_headers in JupyterHandler

        which doesn't make sense for websockets
        """
    def get_compression_options(self):
        """Get the socket connection options."""
    connection: Incomplete
    async def pre_get(self) -> None:
        """Handle a pre_get."""
    kernel_id: Incomplete
    async def get(self, kernel_id) -> None:
        """Handle a get request for a kernel."""
    async def open(self, kernel_id) -> None:
        """Open a kernel websocket."""
    def on_message(self, ws_message) -> None:
        """Get a kernel message from the websocket and turn it into a ZMQ message."""
    def on_close(self) -> None:
        """Handle a socket closure."""
    def select_subprotocol(self, subprotocols):
        """Select the sub protocol for the socket."""
