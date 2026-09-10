from .params import DEFAULT_BIND_ADDR_TUPLE as DEFAULT_BIND_ADDR_TUPLE

def bind_and_listen(sock, address=..., backlog: int = 50, reuse_addr: bool = True) -> None: ...
def tcp_listener(address=..., backlog: int = 50, reuse_addr: bool = True):
    """A shortcut to create a TCP socket, bind it and put it into listening state."""
def udp_listener(address=..., reuse_addr: bool = True):
    """A shortcut to create a UDF socket, bind it and put it into listening state."""
