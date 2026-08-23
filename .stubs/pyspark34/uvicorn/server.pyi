import socket
from _typeshed import Incomplete
from types import FrameType
from typing import List
from uvicorn.config import Config as Config
from uvicorn.protocols.http.h11_impl import H11Protocol as H11Protocol
from uvicorn.protocols.http.httptools_impl import HttpToolsProtocol as HttpToolsProtocol
from uvicorn.protocols.websockets.websockets_impl import WebSocketProtocol as WebSocketProtocol
from uvicorn.protocols.websockets.wsproto_impl import WSProtocol as WSProtocol

Protocols = H11Protocol | HttpToolsProtocol | WSProtocol | WebSocketProtocol
HANDLED_SIGNALS: Incomplete
logger: Incomplete

class ServerState:
    """
    Shared servers state that is available between all protocol instances.
    """
    total_requests: int
    connections: Incomplete
    tasks: Incomplete
    default_headers: Incomplete
    def __init__(self) -> None: ...

class Server:
    config: Incomplete
    server_state: Incomplete
    started: bool
    should_exit: bool
    force_exit: bool
    last_notified: float
    def __init__(self, config: Config) -> None: ...
    def run(self, sockets: List[socket.socket] | None = None) -> None: ...
    lifespan: Incomplete
    async def serve(self, sockets: List[socket.socket] | None = None) -> None: ...
    servers: Incomplete
    async def startup(self, sockets: List[socket.socket] | None = None) -> None: ...
    async def main_loop(self) -> None: ...
    async def on_tick(self, counter: int) -> bool: ...
    async def shutdown(self, sockets: List[socket.socket] | None = None) -> None: ...
    def install_signal_handlers(self) -> None: ...
    def handle_exit(self, sig: int, frame: FrameType | None) -> None: ...
