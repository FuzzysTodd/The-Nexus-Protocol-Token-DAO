from ..lib.mailbox import Mailbox as Mailbox
from .interface_queue import InterfaceQueue as InterfaceQueue
from .router_relay import MessageRelayRouter as MessageRelayRouter
from _typeshed import Incomplete
from multiprocessing.process import BaseProcess
from queue import Queue
from wandb.proto import wandb_internal_pb2 as pb

logger: Incomplete

class InterfaceRelay(InterfaceQueue):
    relay_q: Queue[pb.Result] | None
    def __init__(self, mailbox: Mailbox, record_q: Queue[pb.Record] | None = None, result_q: Queue[pb.Result] | None = None, relay_q: Queue[pb.Result] | None = None, process: BaseProcess | None = None, process_check: bool = True) -> None: ...
