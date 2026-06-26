from .api import RendezvousConnectionError as RendezvousConnectionError, RendezvousError as RendezvousError, RendezvousParameters as RendezvousParameters, RendezvousStateError as RendezvousStateError
from .dynamic_rendezvous import RendezvousBackend as RendezvousBackend, Token as Token
from .utils import parse_rendezvous_endpoint as parse_rendezvous_endpoint
from _typeshed import Incomplete
from torch.distributed import FileStore as FileStore, Store as Store, TCPStore as TCPStore
from torch.distributed.elastic.events import NodeState as NodeState, construct_and_record_rdzv_event as construct_and_record_rdzv_event
from typing import Tuple

log: Incomplete

class C10dRendezvousBackend(RendezvousBackend):
    """Represents a C10d-backed rendezvous backend.

    Args:
        store:
            The :py:class:`torch.distributed.Store` instance to use to
            communicate with the C10d store.
        run_id:
            The run id of the rendezvous.
    """
    def __init__(self, store: Store, run_id: str) -> None: ...
    @property
    def name(self) -> str:
        """See base class."""
    def get_state(self) -> Tuple[bytes, Token] | None:
        """See base class."""
    def set_state(self, state: bytes, token: Token | None = None) -> Tuple[bytes, Token, bool] | None:
        """See base class."""

def create_backend(params: RendezvousParameters) -> Tuple[C10dRendezvousBackend, Store]:
    '''Creates a new :py:class:`C10dRendezvousBackend` from the specified
    parameters.

    +--------------+-----------------------------------------------------------+
    | Parameter    | Description                                               |
    +==============+===========================================================+
    | store_type   | The type of the C10d store. The currently supported types |
    |              | are "tcp" and "file" which correspond to                  |
    |              | :py:class:`torch.distributed.TCPStore` and                |
    |              | :py:class:`torch.distributed.FileStore`, respectively.    |
    |              | Defaults to "tcp".                                        |
    +--------------+-----------------------------------------------------------+
    | read_timeout | The read timeout, in seconds, for store operations.       |
    |              | Defaults to 60 seconds.                                   |
    |              |                                                           |
    |              | Note this only applies to                                 |
    |              | :py:class:`torch.distributed.TCPStore`. It is not relevant|
    |              | to :py:class:`torch.distributed.FileStore` which does not |
    |              | take in timeout as a parameter.                           |
    +--------------+-----------------------------------------------------------+
    | is_host      | A boolean value indicating whether this backend instance  |
    |              | will host the C10d store. If not specified it will be     |
    |              | inferred heuristically by matching the hostname or the IP |
    |              | address of this machine against the specified rendezvous  |
    |              | endpoint. Defaults to ``None``.                           |
    |              |                                                           |
    |              | Note that this configuration option only applies to       |
    |              | :py:class:`torch.distributed.TCPStore`. In normal         |
    |              | circumstances you can safely skip it; the only time when  |
    |              | it is needed is if its value cannot be correctly          |
    |              | determined (e.g. the rendezvous endpoint has a CNAME as   |
    |              | the hostname or does not match the FQDN of the machine).  |
    +--------------+-----------------------------------------------------------+
    '''
