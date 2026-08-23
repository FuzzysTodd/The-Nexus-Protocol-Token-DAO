import socketserver
import typing as t

__all__ = ['forward_tunnel']

class ForwardServer(socketserver.ThreadingTCPServer):
    """A server to use for ssh forwarding."""
    daemon_threads: bool
    allow_reuse_address: bool

class Handler(socketserver.BaseRequestHandler):
    """A handle for server requests."""
    def handle(self) -> None:
        """Handle a request."""

def forward_tunnel(local_port: int, remote_host: str, remote_port: int, transport: t.Any) -> None:
    """Forward an ssh tunnel."""
