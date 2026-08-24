from ..base.handlers import JupyterHandler as JupyterHandler
from ..services.kernelspecs.handlers import kernel_name_regex as kernel_name_regex
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized
from tornado import web

AUTH_RESOURCE: str

class KernelSpecResourceHandler(web.StaticFileHandler, JupyterHandler):
    """A Kernelspec resource handler."""
    SUPPORTED_METHODS: Incomplete
    auth_resource = AUTH_RESOURCE
    def initialize(self) -> None:
        """Initialize a kernelspec resource handler."""
    absolute_path: Incomplete
    root: Incomplete
    async def get(self, kernel_name, path, include_body: bool = True):
        """Get a kernelspec resource."""
    async def head(self, kernel_name, path):
        """Get the head infor for a kernel resource."""

default_handlers: Incomplete
