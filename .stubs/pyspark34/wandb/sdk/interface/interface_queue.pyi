from ..lib import tracelog as tracelog
from ..lib.mailbox import Mailbox as Mailbox
from .interface_shared import InterfaceShared as InterfaceShared
from .router_queue import MessageQueueRouter as MessageQueueRouter
from _typeshed import Incomplete
from multiprocessing.process import BaseProcess
from queue import Queue
from wandb.proto import wandb_internal_pb2 as pb

logger: Incomplete

class InterfaceQueue(InterfaceShared):
    record_q: Queue[pb.Record] | None
    result_q: Queue[pb.Result] | None
    def __init__(self, record_q: Queue[pb.Record] | None = None, result_q: Queue[pb.Result] | None = None, process: BaseProcess | None = None, process_check: bool = True, mailbox: Mailbox | None = None) -> None: ...
