import tornado.websocket
from _typeshed import Incomplete
from collections.abc import Generator

class TermSocket(tornado.websocket.WebSocketHandler):
    """Handler for a terminal websocket"""
    term_manager: Incomplete
    term_name: str
    size: Incomplete
    terminal: Incomplete
    def initialize(self, term_manager) -> None: ...
    def origin_check(self, origin: Incomplete | None = None):
        """Deprecated: backward-compat for terminado <= 0.5."""
    def open(self, url_component: Incomplete | None = None) -> None:
        """Websocket connection opened.

        Call our terminal manager to get a terminal, and connect to it as a
        client.
        """
    def on_pty_read(self, text) -> None:
        """Data read from pty; send to frontend"""
    def send_json_message(self, content) -> None: ...
    def on_message(self, message) -> Generator[Incomplete, None, None]:
        """Handle incoming websocket message

        We send JSON arrays, where the first element is a string indicating
        what kind of message this is. Data associated with the message follows.
        """
    def on_close(self) -> None:
        """Handle websocket closing.

        Disconnect from our terminal, and tell the terminal manager we're
        disconnecting.
        """
    def on_pty_died(self) -> None:
        """Terminal closed: tell the frontend, and close the socket."""
    def log_terminal_output(self, log: str = '') -> None:
        """
        Logs the terminal input/output
        :param log: log line to write
        :return:
        """
    def stdin_to_ptyproc(self, text) -> None:
        """Handles stdin messages sent on the websocket.

        This is a blocking call that should NOT be performed inside the
        server primary event loop thread. Messages must be handled
        asynchronously to prevent blocking on the PTY buffer.
        """
