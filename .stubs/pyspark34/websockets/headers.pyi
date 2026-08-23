from .typing import ConnectionOption, ExtensionHeader, Subprotocol, UpgradeProtocol
from typing import List, Sequence, Tuple, TypeVar

__all__ = ['build_host', 'parse_connection', 'parse_upgrade', 'parse_extension', 'build_extension', 'parse_subprotocol', 'build_subprotocol', 'validate_subprotocols', 'build_www_authenticate_basic', 'parse_authorization_basic', 'build_authorization_basic']

T = TypeVar('T')

def build_host(host: str, port: int, secure: bool) -> str:
    """
    Build a ``Host`` header.

    """
def parse_connection(header: str) -> List[ConnectionOption]:
    """
    Parse a ``Connection`` header.

    Return a list of HTTP connection options.

    Args
        header: value of the ``Connection`` header.

    Raises:
        InvalidHeaderFormat: on invalid inputs.

    """
def parse_upgrade(header: str) -> List[UpgradeProtocol]:
    """
    Parse an ``Upgrade`` header.

    Return a list of HTTP protocols.

    Args:
        header: value of the ``Upgrade`` header.

    Raises:
        InvalidHeaderFormat: on invalid inputs.

    """
def parse_extension(header: str) -> List[ExtensionHeader]:
    """
    Parse a ``Sec-WebSocket-Extensions`` header.

    Return a list of WebSocket extensions and their parameters in this format::

        [
            (
                'extension name',
                [
                    ('parameter name', 'parameter value'),
                    ....
                ]
            ),
            ...
        ]

    Parameter values are :obj:`None` when no value is provided.

    Raises:
        InvalidHeaderFormat: on invalid inputs.

    """
parse_extension_list = parse_extension

def build_extension(extensions: Sequence[ExtensionHeader]) -> str:
    """
    Build a ``Sec-WebSocket-Extensions`` header.

    This is the reverse of :func:`parse_extension`.

    """
build_extension_list = build_extension

def parse_subprotocol(header: str) -> List[Subprotocol]:
    """
    Parse a ``Sec-WebSocket-Protocol`` header.

    Return a list of WebSocket subprotocols.

    Raises:
        InvalidHeaderFormat: on invalid inputs.

    """
parse_subprotocol_list = parse_subprotocol

def build_subprotocol(subprotocols: Sequence[Subprotocol]) -> str:
    """
    Build a ``Sec-WebSocket-Protocol`` header.

    This is the reverse of :func:`parse_subprotocol`.

    """
build_subprotocol_list = build_subprotocol

def validate_subprotocols(subprotocols: Sequence[Subprotocol]) -> None:
    """
    Validate that ``subprotocols`` is suitable for :func:`build_subprotocol`.

    """
def build_www_authenticate_basic(realm: str) -> str:
    """
    Build a ``WWW-Authenticate`` header for HTTP Basic Auth.

    Args:
        realm: identifier of the protection space.

    """
def parse_authorization_basic(header: str) -> Tuple[str, str]:
    """
    Parse an ``Authorization`` header for HTTP Basic Auth.

    Return a ``(username, password)`` tuple.

    Args:
        header: value of the ``Authorization`` header.

    Raises:
        InvalidHeaderFormat: on invalid inputs.
        InvalidHeaderValue: on unsupported inputs.

    """
def build_authorization_basic(username: str, password: str) -> str:
    """
    Build an ``Authorization`` header for HTTP Basic Auth.

    This is the reverse of :func:`parse_authorization_basic`.

    """
