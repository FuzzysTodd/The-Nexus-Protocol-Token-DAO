import socket
from _typeshed import Incomplete
from torch.distributed.elastic.utils.logging import get_logger as get_logger

log: Incomplete

def create_c10d_store(is_server: bool, server_addr: str, server_port: int = -1, world_size: int = 1, timeout: float = ..., wait_for_workers: bool = True, retries: int = 3): ...
def get_free_port(): ...
def get_socket_with_port() -> socket.socket:
    '''
    Returns a free port on localhost that is "reserved" by binding a temporary
    socket on it. Close the socket before passing the port to the entity
    that requires it. Usage example

    ::

    sock = _get_socket_with_port()
    with closing(sock):
        port = sock.getsockname()[1]
        sock.close()
        # there is still a race-condition that some other process
        # may grab this port before func() runs
        func(port)
    '''
