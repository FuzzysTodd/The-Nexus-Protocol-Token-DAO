from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized
from jupyter_server.base.handlers import JupyterHandler as JupyterHandler

AUTH_RESOURCE: str

class ShutdownHandler(JupyterHandler):
    """A shutdown API handler."""
    auth_resource = AUTH_RESOURCE
    async def post(self) -> None:
        """Shut down the server."""

default_handlers: Incomplete
