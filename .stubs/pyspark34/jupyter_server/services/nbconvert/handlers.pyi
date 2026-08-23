from ...base.handlers import APIHandler as APIHandler
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized

AUTH_RESOURCE: str

class NbconvertRootHandler(APIHandler):
    """The nbconvert root API handler."""
    auth_resource = AUTH_RESOURCE
    def initialize(self, **kwargs) -> None:
        """Initialize an nbconvert root handler."""
    async def get(self) -> None:
        """Get the list of nbconvert exporters."""

default_handlers: Incomplete
