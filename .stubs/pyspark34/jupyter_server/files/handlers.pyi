from jupyter_server.auth import authorized as authorized
from jupyter_server.base.handlers import JupyterHandler as JupyterHandler
from tornado import web
from typing import List

AUTH_RESOURCE: str

class FilesHandler(JupyterHandler, web.StaticFileHandler):
    """serve files via ContentsManager

    Normally used when ContentsManager is not a FileContentsManager.

    FileContentsManager subclasses use AuthenticatedFilesHandler by default,
    a subclass of StaticFileHandler.
    """
    auth_resource = AUTH_RESOURCE
    @property
    def content_security_policy(self):
        """The content security policy."""
    def head(self, path):
        """The head response."""
    async def get(self, path, include_body: bool = True) -> None:
        """Get a file by path."""

default_handlers: List[JupyterHandler]
