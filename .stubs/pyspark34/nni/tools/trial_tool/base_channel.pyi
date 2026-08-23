import abc
from .commands import CommandType as CommandType
from .log_utils import LogType as LogType, nni_log as nni_log
from _typeshed import Incomplete
from abc import ABC

INTERVAL_SECONDS: float

class BaseChannel(ABC, metaclass=abc.ABCMeta):
    is_keep_parsed: Incomplete
    args: Incomplete
    node_id: Incomplete
    def __init__(self, args) -> None: ...
    is_running: bool
    receive_queue: Incomplete
    receive_thread: Incomplete
    send_queue: Incomplete
    send_thread: Incomplete
    def open(self) -> None: ...
    def close(self) -> None: ...
    def send(self, command, data) -> None:
        """Send command to Training Service.
        command: CommandType object.
        data: string payload.
        the message is sent synchronized.
        """
    def sent(self): ...
    def received(self): ...
    def receive(self):
        """Receive a command from Training Service.
        Returns a tuple of command (CommandType) and payload (str)
        """
