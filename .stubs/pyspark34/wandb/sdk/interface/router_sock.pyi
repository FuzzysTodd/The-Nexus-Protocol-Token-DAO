from ..lib.mailbox import Mailbox as Mailbox
from ..lib.sock_client import SockClient as SockClient, SockClientClosedError as SockClientClosedError
from .router import MessageRouter as MessageRouter, MessageRouterClosedError as MessageRouterClosedError

class MessageSockRouter(MessageRouter):
    def __init__(self, sock_client: SockClient, mailbox: Mailbox) -> None: ...
