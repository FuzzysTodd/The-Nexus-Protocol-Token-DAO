import socketserver

__all__ = ['forward_tunnel']

class ForwardServer(socketserver.ThreadingTCPServer):
    daemon_threads: bool
    allow_reuse_address: bool

class Handler(socketserver.BaseRequestHandler):
    def handle(self) -> None: ...

def forward_tunnel(local_port, remote_host, remote_port, transport) -> None: ...
