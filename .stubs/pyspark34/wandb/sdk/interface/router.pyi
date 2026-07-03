import abc
from ..lib import mailbox as mailbox, tracelog as tracelog
from .message_future import MessageFuture as MessageFuture
from _typeshed import Incomplete
from wandb.proto import wandb_internal_pb2 as pb

logger: Incomplete

class MessageRouterClosedError(Exception):
    """Router has been closed."""

class MessageFutureObject(MessageFuture):
    def __init__(self) -> None: ...
    def get(self, timeout: int | None = None) -> pb.Result | None: ...

class MessageRouter(metaclass=abc.ABCMeta):
    def __init__(self, mailbox: mailbox.Mailbox | None = None) -> None: ...
    def message_loop(self) -> None: ...
    def send_and_receive(self, rec: pb.Record, local: bool | None = None) -> MessageFuture: ...
    def join(self) -> None: ...
