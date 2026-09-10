from ..base.handlers import JupyterHandler as JupyterHandler, path_regex as path_regex
from ..utils import url_escape as url_escape, url_path_join as url_path_join
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized

AUTH_RESOURCE: str

class ViewHandler(JupyterHandler):
    """Render HTML files within an iframe."""
    auth_resource = AUTH_RESOURCE
    async def get(self, path) -> None:
        """Get a view on a given path."""

default_handlers: Incomplete
