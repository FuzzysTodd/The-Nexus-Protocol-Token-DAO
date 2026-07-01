import asyncio
import typing
from _typeshed import Incomplete
from uvicorn._types import ASGISendEvent as ASGISendEvent, WebSocketAcceptEvent as WebSocketAcceptEvent, WebSocketCloseEvent as WebSocketCloseEvent, WebSocketEvent as WebSocketEvent, WebSocketReceiveEvent as WebSocketReceiveEvent, WebSocketScope as WebSocketScope, WebSocketSendEvent as WebSocketSendEvent
from uvicorn.config import Config as Config
from uvicorn.logging import TRACE_LOG_LEVEL as TRACE_LOG_LEVEL
from uvicorn.protocols.utils import get_local_addr as get_local_addr, get_path_with_query_string as get_path_with_query_string, get_remote_addr as get_remote_addr, is_ssl as is_ssl
from uvicorn.server import ServerState as ServerState
from wsproto import events
from wsproto.extensions import Extension as Extension

class WSProtocol(asyncio.Protocol):
    config: Incomplete
    app: Incomplete
    loop: Incomplete
    logger: Incomplete
    root_path: Incomplete
    app_state: Incomplete
    connections: Incomplete
    tasks: Incomplete
    default_headers: Incomplete
    transport: Incomplete
    server: Incomplete
    client: Incomplete
    scheme: Incomplete
    queue: Incomplete
    handshake_complete: bool
    close_sent: bool
    conn: Incomplete
    read_paused: bool
    writable: Incomplete
    bytes: bytes
    text: str
    def __init__(self, config: Config, server_state: ServerState, app_state: typing.Dict[str, typing.Any], _loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    def connection_made(self, transport: asyncio.Transport) -> None: ...
    def connection_lost(self, exc: Exception | None) -> None: ...
    def eof_received(self) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def handle_events(self) -> None: ...
    def pause_writing(self) -> None:
        """
        Called by the transport when the write buffer exceeds the high water mark.
        """
    def resume_writing(self) -> None:
        """
        Called by the transport when the write buffer drops below the low water mark.
        """
    def shutdown(self) -> None: ...
    def on_task_complete(self, task: asyncio.Task) -> None: ...
    scope: Incomplete
    def handle_connect(self, event: events.Request) -> None: ...
    def handle_text(self, event: events.TextMessage) -> None: ...
    def handle_bytes(self, event: events.BytesMessage) -> None: ...
    def handle_close(self, event: events.CloseConnection) -> None: ...
    def handle_ping(self, event: events.Ping) -> None: ...
    def send_500_response(self) -> None: ...
    async def run_asgi(self) -> None: ...
    async def send(self, message: ASGISendEvent) -> None: ...
    async def receive(self) -> WebSocketEvent: ...
