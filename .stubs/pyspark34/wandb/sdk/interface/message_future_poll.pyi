from .message_future import MessageFuture as MessageFuture
from typing import Any
from wandb.proto import wandb_internal_pb2 as pb

class MessageFuturePoll(MessageFuture):
    def __init__(self, fn: Any, xid: str) -> None: ...
    def get(self, timeout: int | None = None) -> pb.Result | None: ...
