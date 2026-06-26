from ...base.handlers import APIHandler as APIHandler
from .websocket import KernelWebsocketHandler as KernelWebsocketHandler
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized
from jupyter_server.utils import url_escape as url_escape, url_path_join as url_path_join

AUTH_RESOURCE: str

class KernelsAPIHandler(APIHandler):
    """A kernels API handler."""
    auth_resource = AUTH_RESOURCE

class MainKernelHandler(KernelsAPIHandler):
    """The root kernel handler."""
    async def get(self) -> None:
        """Get the list of running kernels."""
    async def post(self) -> None:
        """Start a kernel."""

class KernelHandler(KernelsAPIHandler):
    """A kernel API handler."""
    async def get(self, kernel_id) -> None:
        """Get a kernel model."""
    async def delete(self, kernel_id) -> None:
        """Remove a kernel."""

class KernelActionHandler(KernelsAPIHandler):
    """A kernel action API handler."""
    async def post(self, kernel_id, action) -> None:
        """Interrupt or restart a kernel."""

default_handlers: Incomplete
