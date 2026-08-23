from _typeshed import Incomplete
from tornado.iostream import IOStream as IOStream

WS_PING_INTERVAL: int

class WebSocketMixin:
    """Mixin for common websocket options"""
    ping_callback: Incomplete
    last_ping: float
    last_pong: float
    stream: IOStream | None
    @property
    def ping_interval(self):
        """The interval for websocket keep-alive pings.

        Set ws_ping_interval = 0 to disable pings.
        """
    @property
    def ping_timeout(self):
        """If no ping is received in this many milliseconds,
        close the websocket connection (VPNs, etc. can fail to cleanly close ws connections).
        Default is max of 3 pings or 30 seconds.
        """
    def check_origin(self, origin: Incomplete | None = None):
        """Check Origin == Host or Access-Control-Allow-Origin.

        Tornado >= 4 calls this method automatically, raising 403 if it returns False.
        """
    def clear_cookie(self, *args, **kwargs) -> None:
        """meaningless for websockets"""
    def open(self, *args, **kwargs):
        """Open the websocket."""
    def send_ping(self) -> None:
        """send a ping to keep the websocket alive"""
    def on_pong(self, data) -> None:
        """Handle a pong message."""
