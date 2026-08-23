from . import port_file as port_file
from ..lib import tracelog as tracelog
from .server_sock import SocketServer as SocketServer
from .streams import StreamMux as StreamMux

class WandbServer:
    def __init__(self, sock_port: int | None = None, port_fname: str | None = None, address: str | None = None, pid: int | None = None, debug: bool = True, serve_sock: bool = False) -> None: ...
    def serve(self) -> None: ...
