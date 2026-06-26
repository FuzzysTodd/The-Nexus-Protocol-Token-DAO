from .legacy.client import *
from .datastructures import Headers as Headers, MultipleValuesError as MultipleValuesError
from .exceptions import InvalidHandshake as InvalidHandshake, InvalidHeader as InvalidHeader, InvalidHeaderValue as InvalidHeaderValue, InvalidStatus as InvalidStatus, InvalidUpgrade as InvalidUpgrade, NegotiationError as NegotiationError
from .extensions import ClientExtensionFactory as ClientExtensionFactory, Extension as Extension
from .headers import build_authorization_basic as build_authorization_basic, build_extension as build_extension, build_host as build_host, build_subprotocol as build_subprotocol, parse_connection as parse_connection, parse_extension as parse_extension, parse_subprotocol as parse_subprotocol, parse_upgrade as parse_upgrade
from .http11 import Request as Request, Response as Response
from .protocol import CLIENT as CLIENT, CONNECTING as CONNECTING, OPEN as OPEN, Protocol as Protocol, State as State
from .typing import ConnectionOption as ConnectionOption, ExtensionHeader as ExtensionHeader, LoggerLike as LoggerLike, Origin as Origin, Subprotocol as Subprotocol, UpgradeProtocol as UpgradeProtocol
from .uri import WebSocketURI as WebSocketURI
from .utils import accept_key as accept_key, generate_key as generate_key
from _typeshed import Incomplete
from typing import Any, Generator, List, Sequence

class ClientProtocol(Protocol):
    '''
    Sans-I/O implementation of a WebSocket client connection.

    Args:
        wsuri: URI of the WebSocket server, parsed
            with :func:`~websockets.uri.parse_uri`.
        origin: value of the ``Origin`` header. This is useful when connecting
            to a server that validates the ``Origin`` header to defend against
            Cross-Site WebSocket Hijacking attacks.
        extensions: list of supported extensions, in order in which they
            should be tried.
        subprotocols: list of supported subprotocols, in order of decreasing
            preference.
        state: initial state of the WebSocket connection.
        max_size: maximum size of incoming messages in bytes;
            :obj:`None` disables the limit.
        logger: logger for this connection;
            defaults to ``logging.getLogger("websockets.client")``;
            see the :doc:`logging guide <../../topics/logging>` for details.

    '''
    wsuri: Incomplete
    origin: Incomplete
    available_extensions: Incomplete
    available_subprotocols: Incomplete
    key: Incomplete
    def __init__(self, wsuri: WebSocketURI, *, origin: Origin | None = None, extensions: Sequence[ClientExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, state: State = ..., max_size: int | None = ..., logger: LoggerLike | None = None) -> None: ...
    def connect(self) -> Request:
        """
        Create a handshake request to open a connection.

        You must send the handshake request with :meth:`send_request`.

        You can modify it before sending it, for example to add HTTP headers.

        Returns:
            Request: WebSocket handshake request event to send to the server.

        """
    extensions: Incomplete
    subprotocol: Incomplete
    def process_response(self, response: Response) -> None:
        """
        Check a handshake response.

        Args:
            request: WebSocket handshake response received from the server.

        Raises:
            InvalidHandshake: if the handshake response is invalid.

        """
    def process_extensions(self, headers: Headers) -> List[Extension]:
        """
        Handle the Sec-WebSocket-Extensions HTTP response header.

        Check that each extension is supported, as well as its parameters.

        :rfc:`6455` leaves the rules up to the specification of each
        extension.

        To provide this level of flexibility, for each extension accepted by
        the server, we check for a match with each extension available in the
        client configuration. If no match is found, an exception is raised.

        If several variants of the same extension are accepted by the server,
        it may be configured several times, which won't make sense in general.
        Extensions must implement their own requirements. For this purpose,
        the list of previously accepted extensions is provided.

        Other requirements, for example related to mandatory extensions or the
        order of extensions, may be implemented by overriding this method.

        Args:
            headers: WebSocket handshake response headers.

        Returns:
            List[Extension]: List of accepted extensions.

        Raises:
            InvalidHandshake: to abort the handshake.

        """
    def process_subprotocol(self, headers: Headers) -> Subprotocol | None:
        """
        Handle the Sec-WebSocket-Protocol HTTP response header.

        If provided, check that it contains exactly one supported subprotocol.

        Args:
            headers: WebSocket handshake response headers.

        Returns:
           Optional[Subprotocol]: Subprotocol, if one was selected.

        """
    def send_request(self, request: Request) -> None:
        """
        Send a handshake request to the server.

        Args:
            request: WebSocket handshake request event.

        """
    handshake_exc: Incomplete
    parser: Incomplete
    state: Incomplete
    def parse(self) -> Generator[None, None, None]: ...

class ClientConnection(ClientProtocol):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
