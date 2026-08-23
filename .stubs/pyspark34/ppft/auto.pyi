from _typeshed import Incomplete

copyright: Incomplete
__version__: Incomplete
version: Incomplete
BROADCAST_INTERVAL: int

class Discover:
    """Auto-discovery service class"""
    base: Incomplete
    hosts: Incomplete
    isclient: Incomplete
    def __init__(self, base, isclient: bool = False) -> None: ...
    interface_addr: Incomplete
    broadcast_addr: Incomplete
    bsocket: Incomplete
    def run(self, interface_addr, broadcast_addr) -> None:
        """Starts auto-discovery"""
    def broadcast(self) -> None:
        """Sends a broadcast"""
    socket: Incomplete
    def listen(self) -> None:
        """Listens for broadcasts from other clients/servers"""
