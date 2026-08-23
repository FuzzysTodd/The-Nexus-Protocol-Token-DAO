import asyncio
from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence, Tuple
from uvicorn._types import ASGISendEvent as ASGISendEvent, WebSocketAcceptEvent as WebSocketAcceptEvent, WebSocketCloseEvent as WebSocketCloseEvent, WebSocketConnectEvent as WebSocketConnectEvent, WebSocketDisconnectEvent as WebSocketDisconnectEvent, WebSocketReceiveEvent as WebSocketReceiveEvent, WebSocketScope as WebSocketScope, WebSocketSendEvent as WebSocketSendEvent
from uvicorn.config import Config as Config
from uvicorn.logging import TRACE_LOG_LEVEL as TRACE_LOG_LEVEL
from uvicorn.protocols.utils import get_local_addr as get_local_addr, get_path_with_query_string as get_path_with_query_string, get_remote_addr as get_remote_addr, is_ssl as is_ssl
from uvicorn.server import ServerState as ServerState
from websockets.datastructures import Headers as Headers
from websockets.legacy.server import HTTPResponse as HTTPResponse
from websockets.server import WebSocketServerProtocol
from websockets.typing import Subprotocol

class Server:
    closing: bool
    def register(self, ws: WebSocketServerProtocol) -> None: ...
    def unregister(self, ws: WebSocketServerProtocol) -> None: ...
    def is_serving(self) -> bool: ...

class WebSocketProtocol(WebSocketServerProtocol):
    extra_headers: List[Tuple[str, str]]
    config: Incomplete
    app: Incomplete
    loop: Incomplete
    root_path: Incomplete
    app_state: Incomplete
    connections: Incomplete
    tasks: Incomplete
    transport: Incomplete
    server: Incomplete
    client: Incomplete
    scheme: Incomplete
    scope: Incomplete
    handshake_started_event: Incomplete
    handshake_completed_event: Incomplete
    closed_event: Incomplete
    initial_response: Incomplete
    connect_sent: bool
    lost_connection_before_handshake: bool
    accepted_subprotocol: Incomplete
    ws_server: Incomplete
    server_header: Incomplete
    def __init__(self, config: Config, server_state: ServerState, app_state: Dict[str, Any], _loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    def connection_made(self, transport: asyncio.Transport) -> None: ...
    def connection_lost(self, exc: Exception | None) -> None: ...
    def shutdown(self) -> None: ...
    def on_task_complete(self, task: asyncio.Task) -> None: ...
    async def process_request(self, path: str, headers: Headers) -> HTTPResponse | None:
        """
        This hook is called to determine if the websocket should return
        an HTTP response and close.

        Our behavior here is to start the ASGI application, and then wait
        for either `accept` or `close` in order to determine if we should
        close the connection.
        """
    def process_subprotocol(self, headers: Headers, available_subprotocols: Sequence[Subprotocol] | None) -> Subprotocol | None:
        """
        We override the standard 'process_subprotocol' behavior here so that
        we return whatever subprotocol is sent in the 'accept' message.
        """
    def send_500_response(self) -> None: ...
    async def ws_handler(self, protocol: WebSocketServerProtocol, path: str) -> Any:
        """
        This is the main handler function for the 'websockets' implementation
        to call into. We just wait for close then return, and instead allow
        'send' and 'receive' events to drive the flow.
        """
    async def run_asgi(self) -> None:
        """
        Wrapper around the ASGI callable, handling exceptions and unexpected
        termination states.
        """
    async def asgi_send(self, message: ASGISendEvent) -> None: ...
    async def asgi_receive(self) -> WebSocketDisconnectEvent | WebSocketConnectEvent | WebSocketReceiveEvent: ...
