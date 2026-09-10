import asyncio
from .abc import AbstractAccessLogger
from .base_protocol import BaseProtocol
from .web_request import BaseRequest
from .web_response import StreamResponse
from .web_server import Server
from _typeshed import Incomplete
from logging import Logger
from typing import Any, Type

__all__ = ['RequestHandler', 'RequestPayloadError', 'PayloadAccessError']

class RequestPayloadError(Exception):
    """Payload parsing error."""
class PayloadAccessError(Exception):
    """Payload was accessed after response was sent."""

class _ErrInfo:
    status: int
    exc: BaseException
    message: str
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class RequestHandler(BaseProtocol):
    """HTTP protocol implementation.

    RequestHandler handles incoming HTTP request. It reads request line,
    request headers and request payload and calls handle_request() method.
    By default it always returns with 404 response.

    RequestHandler handles errors in incoming request, like bad
    status line, bad headers or incomplete payload. If any error occurs,
    connection gets closed.

    keepalive_timeout -- number of seconds before closing
                         keep-alive connection

    tcp_keepalive -- TCP keep-alive is on, default is on

    debug -- enable debug mode

    logger -- custom logger object

    access_log_class -- custom class for access_logger

    access_log -- custom logging object

    access_log_format -- access log format string

    loop -- Optional event loop

    max_line_size -- Optional maximum header line size

    max_field_size -- Optional maximum header field size

    max_headers -- Optional maximum header size

    """
    KEEPALIVE_RESCHEDULE_DELAY: int
    logger: Incomplete
    debug: Incomplete
    access_log: Incomplete
    access_logger: Incomplete
    def __init__(self, manager: Server, *, loop: asyncio.AbstractEventLoop, keepalive_timeout: float = 75.0, tcp_keepalive: bool = True, logger: Logger = ..., access_log_class: Type[AbstractAccessLogger] = ..., access_log: Logger = ..., access_log_format: str = ..., debug: bool = False, max_line_size: int = 8190, max_headers: int = 32768, max_field_size: int = 8190, lingering_time: float = 10.0, read_bufsize: int = ..., auto_decompress: bool = True) -> None: ...
    @property
    def keepalive_timeout(self) -> float: ...
    transport: Incomplete
    async def shutdown(self, timeout: float | None = 15.0) -> None:
        """Do worker process exit preparations.

        We need to clean up everything and stop accepting requests.
        It is especially important for keep-alive connections.
        """
    def connection_made(self, transport: asyncio.BaseTransport) -> None: ...
    def connection_lost(self, exc: BaseException | None) -> None: ...
    def set_parser(self, parser: Any) -> None: ...
    def eof_received(self) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def keep_alive(self, val: bool) -> None:
        """Set keep-alive connection mode.

        :param bool val: new state.
        """
    def close(self) -> None:
        """Close connection.

        Stop accepting new pipelining messages and close
        connection when handlers done processing messages.
        """
    def force_close(self) -> None:
        """Forcefully close connection."""
    def log_access(self, request: BaseRequest, response: StreamResponse, time: float) -> None: ...
    def log_debug(self, *args: Any, **kw: Any) -> None: ...
    def log_exception(self, *args: Any, **kw: Any) -> None: ...
    async def start(self) -> None:
        """Process incoming request.

        It reads request line, request headers and request payload, then
        calls handle_request() method. Subclass has to override
        handle_request(). start() handles various exceptions in request
        or response handling. Connection is being closed always unless
        keep_alive(True) specified.
        """
    async def finish_response(self, request: BaseRequest, resp: StreamResponse, start_time: float) -> bool:
        """Prepare the response and write_eof, then log access.

        This has to
        be called within the context of any exception so the access logger
        can get exception information. Returns True if the client disconnects
        prematurely.
        """
    def handle_error(self, request: BaseRequest, status: int = 500, exc: BaseException | None = None, message: str | None = None) -> StreamResponse:
        """Handle errors.

        Returns HTTP response with specific status code. Logs additional
        information. It always closes current connection.
        """
