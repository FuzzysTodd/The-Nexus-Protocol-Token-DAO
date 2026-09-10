from ...base.handlers import APIHandler as APIHandler, JupyterHandler as JupyterHandler
from _typeshed import Incomplete
from jupyter_server._tz import isoformat as isoformat, utcfromtimestamp as utcfromtimestamp
from jupyter_server.auth import authorized as authorized
from tornado import web

AUTH_RESOURCE: str

class APISpecHandler(web.StaticFileHandler, JupyterHandler):
    """A spec handler for the REST API."""
    auth_resource = AUTH_RESOURCE
    def initialize(self) -> None:
        """Initialize the API spec handler."""
    def get(self):
        """Get the API spec."""
    def get_content_type(self):
        """Get the content type."""

class APIStatusHandler(APIHandler):
    """An API status handler."""
    auth_resource = AUTH_RESOURCE
    async def get(self) -> None:
        """Get the API status."""

class IdentityHandler(APIHandler):
    """Get the current user's identity model"""
    def get(self) -> None:
        """Get the identity model."""

default_handlers: Incomplete
