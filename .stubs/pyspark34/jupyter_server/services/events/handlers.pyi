from ...base.handlers import APIHandler as APIHandler
from _typeshed import Incomplete
from datetime import datetime
from jupyter_events import EventLogger as EventLogger
from jupyter_server.auth import authorized as authorized
from jupyter_server.base.handlers import JupyterHandler as JupyterHandler
from tornado import websocket
from typing import Any, Dict

AUTH_RESOURCE: str

class SubscribeWebsocket(JupyterHandler, websocket.WebSocketHandler):
    """Websocket handler for subscribing to events"""
    auth_resource = AUTH_RESOURCE
    def pre_get(self) -> None:
        """Handles authentication/authorization when
        attempting to subscribe to events emitted by
        Jupyter Server's eventbus.
        """
    async def get(self, *args, **kwargs) -> None:
        """Get an event socket."""
    async def event_listener(self, logger: EventLogger, schema_id: str, data: dict) -> None:
        """Write an event message."""
    def open(self) -> None:
        """Routes events that are emitted by Jupyter Server's
        EventBus to a WebSocket client in the browser.
        """
    def on_close(self) -> None:
        """Handle a socket close."""

def validate_model(data: Dict[str, Any]) -> None:
    """Validates for required fields in the JSON request body"""
def get_timestamp(data: Dict[str, Any]) -> datetime | None:
    """Parses timestamp from the JSON request body"""

class EventHandler(APIHandler):
    """REST api handler for events"""
    auth_resource = AUTH_RESOURCE
    async def post(self) -> None:
        """Emit an event."""

default_handlers: Incomplete
