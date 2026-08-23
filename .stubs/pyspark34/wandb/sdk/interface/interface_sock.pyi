from ..lib.mailbox import Mailbox as Mailbox
from ..lib.sock_client import SockClient as SockClient
from ..wandb_run import Run as Run
from .interface_shared import InterfaceShared as InterfaceShared
from .message_future import MessageFuture as MessageFuture
from .router_sock import MessageSockRouter as MessageSockRouter
from _typeshed import Incomplete

logger: Incomplete

class InterfaceSock(InterfaceShared):
    def __init__(self, sock_client: SockClient, mailbox: Mailbox) -> None: ...
