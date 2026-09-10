from ..lib import tracelog as tracelog
from ..lib.mailbox import Mailbox as Mailbox
from .router_queue import MessageQueueRouter as MessageQueueRouter
from queue import Queue
from wandb.proto import wandb_internal_pb2 as pb

class MessageRelayRouter(MessageQueueRouter):
    def __init__(self, request_queue: Queue[pb.Record], response_queue: Queue[pb.Result], relay_queue: Queue[pb.Result], mailbox: Mailbox) -> None: ...
