from _typeshed import Incomplete

__all__ = ['Tunnel', 'TunnelException']

class TunnelException(Exception):
    """Exception for failure to establish ssh tunnel"""

class Tunnel:
    """a ssh-tunnel launcher for parallel and distributed computing."""
    MINPORT: int
    MAXPORT: int
    verbose: bool
    connected: bool
    def connect(self, host, port: Incomplete | None = None, through: Incomplete | None = None):
        """establish a secure shell tunnel between local and remote host

Input:
    host     -- remote hostname  [user@host:path is also valid]
    port     -- remote port number

Additional Input:
    through  -- 'tunnel-through' hostname  [default = None]
        """
    def disconnect(self) -> None:
        """destroy the ssh tunnel"""
    name: Incomplete
    def __init__(self, name: Incomplete | None = None, **kwds) -> None:
        """create a ssh tunnel launcher

Inputs:
    name        -- a unique identifier (string) for the launcher
        """
