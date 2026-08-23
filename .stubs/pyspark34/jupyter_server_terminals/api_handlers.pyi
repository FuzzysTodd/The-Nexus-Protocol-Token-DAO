from .base import TerminalsMixin as TerminalsMixin
from _typeshed import Incomplete
from jupyter_server.base.handlers import APIHandler

AUTH_RESOURCE: str

class TerminalAPIHandler(APIHandler):
    """The base terminal handler."""
    auth_resource = AUTH_RESOURCE

class TerminalRootHandler(TerminalsMixin, TerminalAPIHandler):
    """The root termanal API handler."""
    def get(self) -> None:
        """Get the list of terminals."""
    def post(self) -> None:
        """POST /terminals creates a new terminal and redirects to it"""

class TerminalHandler(TerminalsMixin, TerminalAPIHandler):
    """A handler for a specific terminal."""
    SUPPORTED_METHODS: Incomplete
    def get(self, name) -> None:
        """Get a terminal by name."""
    async def delete(self, name) -> None:
        """Remove a terminal by name."""

default_handlers: Incomplete
