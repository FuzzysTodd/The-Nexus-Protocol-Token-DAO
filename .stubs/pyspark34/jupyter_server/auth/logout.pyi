from ..base.handlers import JupyterHandler as JupyterHandler
from _typeshed import Incomplete

class LogoutHandler(JupyterHandler):
    """An auth logout handler."""
    def get(self) -> None:
        """Handle a logout."""

default_handlers: Incomplete
