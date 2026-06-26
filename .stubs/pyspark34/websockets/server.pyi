from .legacy.server import *
from .datastructures import Headers as Headers, MultipleValuesError as MultipleValuesError
from .exceptions import InvalidHandshake as InvalidHandshake, InvalidHeader as InvalidHeader, InvalidHeaderValue as InvalidHeaderValue, InvalidOrigin as InvalidOrigin, InvalidStatus as InvalidStatus, InvalidUpgrade as InvalidUpgrade, NegotiationError as NegotiationError
from .extensions import Extension as Extension, ServerExtensionFactory as ServerExtensionFactory
from .headers import build_extension as build_extension, parse_connection as parse_connection, parse_extension as parse_extension, parse_subprotocol as parse_subprotocol, parse_upgrade as parse_upgrade
from .http11 import Request as Request, Response as Response
from .protocol import CONNECTING as CONNECTING, OPEN as OPEN, Protocol as Protocol, SERVER as SERVER, State as State
from .typing import ConnectionOption as ConnectionOption, ExtensionHeader as ExtensionHeader, LoggerLike as LoggerLike, Origin as Origin, StatusLike as StatusLike, Subprotocol as Subprotocol, UpgradeProtocol as UpgradeProtocol
from .utils import accept_key as accept_key
from _typeshed import Incomplete
from typing import Any, Callable, Generator, List, Sequence, Tuple

class ServerProtocol(Protocol):
    '''
    Sans-I/O implementation of a WebSocket server connection.

    Args:
        origins: acceptable values of the ``Origin`` header; include
            :obj:`None` in the list if the lack of an origin is acceptable.
            This is useful for defending against Cross-Site WebSocket
            Hijacking attacks.
        extensions: list of supported extensions, in order in which they
            should be tried.
        subprotocols: list of supported subprotocols, in order of decreasing
            preference.
        select_subprotocol: Callback for selecting a subprotocol among
            those supported by the client and the server. It has the same
            signature as the :meth:`select_subprotocol` method, including a
            :class:`ServerProtocol` instance as first argument.
        state: initial state of the WebSocket connection.
        max_size: maximum size of incoming messages in bytes;
            :obj:`None` disables the limit.
        logger: logger for this connection;
            defaults to ``logging.getLogger("websockets.client")``;
            see the :doc:`logging guide <../../topics/logging>` for details.

    '''
    origins: Incomplete
    available_extensions: Incomplete
    available_subprotocols: Incomplete
    def __init__(self, *, origins: Sequence[Origin | None] | None = None, extensions: Sequence[ServerExtensionFactory] | None = None, subprotocols: Sequence[Subprotocol] | None = None, select_subprotocol: Callable[[ServerProtocol, Sequence[Subprotocol]], Subprotocol | None] | None = None, state: State = ..., max_size: int | None = ..., logger: LoggerLike | None = None) -> None: ...
    handshake_exc: Incomplete
    def accept(self, request: Request) -> Response:
        """
        Create a handshake response to accept the connection.

        If the connection cannot be established, the handshake response
        actually rejects the handshake.

        You must send the handshake response with :meth:`send_response`.

        You may modify it before sending it, for example to add HTTP headers.

        Args:
            request: WebSocket handshake request event received from the client.

        Returns:
            WebSocket handshake response event to send to the client.

        """
    origin: Incomplete
    def process_request(self, request: Request) -> Tuple[str, str | None, str | None]:
        """
        Check a handshake request and negotiate extensions and subprotocol.

        This function doesn't verify that the request is an HTTP/1.1 or higher
        GET request and doesn't check the ``Host`` header. These controls are
        usually performed earlier in the HTTP request handling code. They're
        the responsibility of the caller.

        Args:
            request: WebSocket handshake request received from the client.

        Returns:
            Tuple[str, Optional[str], Optional[str]]:
            ``Sec-WebSocket-Accept``, ``Sec-WebSocket-Extensions``, and
            ``Sec-WebSocket-Protocol`` headers for the handshake response.

        Raises:
            InvalidHandshake: if the handshake request is invalid;
                then the server must return 400 Bad Request error.

        """
    def process_origin(self, headers: Headers) -> Origin | None:
        """
        Handle the Origin HTTP request header.

        Args:
            headers: WebSocket handshake request headers.

        Returns:
           Optional[Origin]: origin, if it is acceptable.

        Raises:
            InvalidHandshake: if the Origin header is invalid.
            InvalidOrigin: if the origin isn't acceptable.

        """
    def process_extensions(self, headers: Headers) -> Tuple[str | None, List[Extension]]:
        """
        Handle the Sec-WebSocket-Extensions HTTP request header.

        Accept or reject each extension proposed in the client request.
        Negotiate parameters for accepted extensions.

        Per :rfc:`6455`, negotiation rules are defined by the specification of
        each extension.

        To provide this level of flexibility, for each extension proposed by
        the client, we check for a match with each extension available in the
        server configuration. If no match is found, the extension is ignored.

        If several variants of the same extension are proposed by the client,
        it may be accepted several times, which won't make sense in general.
        Extensions must implement their own requirements. For this purpose,
        the list of previously accepted extensions is provided.

        This process doesn't allow the server to reorder extensions. It can
        only select a subset of the extensions proposed by the client.

        Other requirements, for example related to mandatory extensions or the
        order of extensions, may be implemented by overriding this method.

        Args:
            headers: WebSocket handshake request headers.

        Returns:
            Tuple[Optional[str], List[Extension]]: ``Sec-WebSocket-Extensions``
            HTTP response header and list of accepted extensions.

        Raises:
            InvalidHandshake: if the Sec-WebSocket-Extensions header is invalid.

        """
    def process_subprotocol(self, headers: Headers) -> Subprotocol | None:
        """
        Handle the Sec-WebSocket-Protocol HTTP request header.

        Args:
            headers: WebSocket handshake request headers.

        Returns:
           Optional[Subprotocol]: Subprotocol, if one was selected; this is
           also the value of the ``Sec-WebSocket-Protocol`` response header.

        Raises:
            InvalidHandshake: if the Sec-WebSocket-Subprotocol header is invalid.

        """
    def select_subprotocol(self, subprotocols: Sequence[Subprotocol]) -> Subprotocol | None:
        '''
        Pick a subprotocol among those offered by the client.

        If several subprotocols are supported by both the client and the server,
        pick the first one in the list declared the server.

        If the server doesn\'t support any subprotocols, continue without a
        subprotocol, regardless of what the client offers.

        If the server supports at least one subprotocol and the client doesn\'t
        offer any, abort the handshake with an HTTP 400 error.

        You provide a ``select_subprotocol`` argument to :class:`ServerProtocol`
        to override this logic. For example, you could accept the connection
        even if client doesn\'t offer a subprotocol, rather than reject it.

        Here\'s how to negotiate the ``chat`` subprotocol if the client supports
        it and continue without a subprotocol otherwise::

            def select_subprotocol(protocol, subprotocols):
                if "chat" in subprotocols:
                    return "chat"

        Args:
            subprotocols: list of subprotocols offered by the client.

        Returns:
            Optional[Subprotocol]: Selected subprotocol, if a common subprotocol
            was found.

            :obj:`None` to continue without a subprotocol.

        Raises:
            NegotiationError: custom implementations may raise this exception
                to abort the handshake with an HTTP 400 error.

        '''
    def reject(self, status: StatusLike, text: str) -> Response:
        """
        Create a handshake response to reject the connection.

        A short plain text response is the best fallback when failing to
        establish a WebSocket connection.

        You must send the handshake response with :meth:`send_response`.

        You can modify it before sending it, for example to alter HTTP headers.

        Args:
            status: HTTP status code.
            text: HTTP response body; will be encoded to UTF-8.

        Returns:
            Response: WebSocket handshake response event to send to the client.

        """
    state: Incomplete
    parser: Incomplete
    def send_response(self, response: Response) -> None:
        """
        Send a handshake response to the client.

        Args:
            response: WebSocket handshake response event to send.

        """
    def parse(self) -> Generator[None, None, None]: ...

class ServerConnection(ServerProtocol):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
