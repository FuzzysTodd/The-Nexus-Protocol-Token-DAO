from _typeshed import Incomplete
from torch.distributed import PrefixStore as PrefixStore, Store as Store, TCPStore as TCPStore
from torch.distributed.elastic.rendezvous import RendezvousHandler as RendezvousHandler, RendezvousParameters as RendezvousParameters
from torch.distributed.elastic.rendezvous.utils import parse_rendezvous_endpoint as parse_rendezvous_endpoint
from typing import Tuple

log: Incomplete

class StaticTCPRendezvous(RendezvousHandler):
    """
    Static rendezvous that is a wrapper around the TCPStore.
    Creates TCPStore based on the input parameters with the
    listener on the agent with group_rank=0
    """
    master_addr: Incomplete
    master_port: Incomplete
    rank: Incomplete
    world_size: Incomplete
    run_id: Incomplete
    timeout: Incomplete
    def __init__(self, master_addr: str, master_port: int, rank: int, world_size: int, run_id: str, timeout: int) -> None: ...
    def get_backend(self) -> str: ...
    def next_rendezvous(self) -> Tuple[Store, int, int]: ...
    def is_closed(self): ...
    def set_closed(self) -> None: ...
    def num_nodes_waiting(self): ...
    def get_run_id(self) -> str: ...
    def shutdown(self) -> bool: ...

def create_rdzv_handler(params: RendezvousParameters) -> RendezvousHandler: ...
