import abc
from abc import abstractmethod
from wandb.proto import wandb_internal_pb2 as pb

class MessageFuture(metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @abstractmethod
    def get(self, timeout: int | None = None) -> pb.Result | None: ...
