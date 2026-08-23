from ...base.handlers import APIHandler as APIHandler
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized

AUTH_RESOURCE: str

class ConfigHandler(APIHandler):
    """A config API handler."""
    auth_resource = AUTH_RESOURCE
    def get(self, section_name) -> None:
        """Get config by section name."""
    def put(self, section_name) -> None:
        """Set a config section by name."""
    def patch(self, section_name) -> None:
        """Update a config section by name."""

section_name_regex: str
default_handlers: Incomplete
