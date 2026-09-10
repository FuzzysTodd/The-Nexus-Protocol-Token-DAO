from ...base.handlers import APIHandler as APIHandler
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized
from jupyter_server.utils import url_path_join as url_path_join

AUTH_RESOURCE: str

class SessionsAPIHandler(APIHandler):
    """A Sessions API handler."""
    auth_resource = AUTH_RESOURCE

class SessionRootHandler(SessionsAPIHandler):
    """A Session Root API handler."""
    async def get(self) -> None:
        """Get a list of running sessions."""
    async def post(self) -> None:
        """Create a new session."""

class SessionHandler(SessionsAPIHandler):
    """A handler for a single session."""
    async def get(self, session_id) -> None:
        """Get the JSON model for a single session."""
    async def patch(self, session_id) -> None:
        """Patch updates sessions:

        - path updates session to track renamed paths
        - kernel.name starts a new kernel with a given kernelspec
        """
    async def delete(self, session_id) -> None:
        """Delete the session with given session_id."""

default_handlers: Incomplete
