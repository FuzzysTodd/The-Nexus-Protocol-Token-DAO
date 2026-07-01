from .base import TerminalsMixin as TerminalsMixin
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.base.websocket import WebSocketMixin
from terminado.websocket import TermSocket as BaseTermSocket

AUTH_RESOURCE: str

class TermSocket(TerminalsMixin, WebSocketMixin, JupyterHandler, BaseTermSocket):
    """A terminal websocket."""
    auth_resource = AUTH_RESOURCE
    def initialize(self, name, term_manager, **kwargs) -> None:
        """Initialize the socket."""
    def origin_check(self):
        """Terminado adds redundant origin_check
        Tornado already calls check_origin, so don't do anything here.
        """
    def get(self, *args, **kwargs):
        """Get the terminal socket."""
    def on_message(self, message) -> None:
        """Handle a socket mesage."""
    def write_message(self, message, binary: bool = False) -> None:
        """Write a message to the socket."""
