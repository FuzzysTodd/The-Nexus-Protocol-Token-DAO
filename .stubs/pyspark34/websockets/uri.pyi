import dataclasses
from typing import Tuple

__all__ = ['parse_uri', 'WebSocketURI']

@dataclasses.dataclass
class WebSocketURI:
    """
    WebSocket URI.

    Attributes:
        secure: :obj:`True` for a ``wss`` URI, :obj:`False` for a ``ws`` URI.
        host: Normalized to lower case.
        port: Always set even if it's the default.
        path: May be empty.
        query: May be empty if the URI doesn't include a query component.
        username: Available when the URI contains `User Information`_.
        password: Available when the URI contains `User Information`_.

    .. _User Information: https://www.rfc-editor.org/rfc/rfc3986.html#section-3.2.1

    """
    secure: bool
    host: str
    port: int
    path: str
    query: str
    username: str | None = ...
    password: str | None = ...
    @property
    def resource_name(self) -> str: ...
    @property
    def user_info(self) -> Tuple[str, str] | None: ...
    def __init__(self, secure, host, port, path, query, username, password) -> None: ...

def parse_uri(uri: str) -> WebSocketURI:
    """
    Parse and validate a WebSocket URI.

    Args:
        uri: WebSocket URI.

    Returns:
        WebSocketURI: Parsed WebSocket URI.

    Raises:
        InvalidURI: if ``uri`` isn't a valid WebSocket URI.

    """
