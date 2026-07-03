from ..datastructures import Headers
from .server import HTTPResponse, WebSocketServerProtocol
from typing import Any, Awaitable, Callable, Iterable, Tuple

__all__ = ['BasicAuthWebSocketServerProtocol', 'basic_auth_protocol_factory']

Credentials = Tuple[str, str]

class BasicAuthWebSocketServerProtocol(WebSocketServerProtocol):
    """
    WebSocket server protocol that enforces HTTP Basic Auth.

    """
    realm: str
    username: str | None
    def __init__(self, *args: Any, realm: str | None = None, check_credentials: Callable[[str, str], Awaitable[bool]] | None = None, **kwargs: Any) -> None: ...
    async def check_credentials(self, username: str, password: str) -> bool:
        """
        Check whether credentials are authorized.

        This coroutine may be overridden in a subclass, for example to
        authenticate against a database or an external service.

        Args:
            username: HTTP Basic Auth username.
            password: HTTP Basic Auth password.

        Returns:
            bool: :obj:`True` if the handshake should continue;
            :obj:`False` if it should fail with an HTTP 401 error.

        """
    async def process_request(self, path: str, request_headers: Headers) -> HTTPResponse | None:
        """
        Check HTTP Basic Auth and return an HTTP 401 response if needed.

        """

def basic_auth_protocol_factory(realm: str | None = None, credentials: Credentials | Iterable[Credentials] | None = None, check_credentials: Callable[[str, str], Awaitable[bool]] | None = None, create_protocol: Callable[..., BasicAuthWebSocketServerProtocol] | None = None) -> Callable[..., BasicAuthWebSocketServerProtocol]:
    '''
    Protocol factory that enforces HTTP Basic Auth.

    :func:`basic_auth_protocol_factory` is designed to integrate with
    :func:`~websockets.server.serve` like this::

        websockets.serve(
            ...,
            create_protocol=websockets.basic_auth_protocol_factory(
                realm="my dev server",
                credentials=("hello", "iloveyou"),
            )
        )

    Args:
        realm: Scope of protection. It should contain only ASCII characters
            because the encoding of non-ASCII characters is undefined.
            Refer to section 2.2 of :rfc:`7235` for details.
        credentials: Hard coded authorized credentials. It can be a
            ``(username, password)`` pair or a list of such pairs.
        check_credentials: Coroutine that verifies credentials.
            It receives ``username`` and ``password`` arguments
            and returns a :class:`bool`. One of ``credentials`` or
            ``check_credentials`` must be provided but not both.
        create_protocol: Factory that creates the protocol. By default, this
            is :class:`BasicAuthWebSocketServerProtocol`. It can be replaced
            by a subclass.
    Raises:
        TypeError: If the ``credentials`` or ``check_credentials`` argument is
            wrong.

    '''
