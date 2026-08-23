from _typeshed import Incomplete
from socket import socket
from types import FrameType
from typing import Callable, List
from uvicorn._subprocess import get_subprocess as get_subprocess
from uvicorn.config import Config as Config

HANDLED_SIGNALS: Incomplete
logger: Incomplete

class Multiprocess:
    config: Incomplete
    target: Incomplete
    sockets: Incomplete
    processes: Incomplete
    should_exit: Incomplete
    pid: Incomplete
    def __init__(self, config: Config, target: Callable[[List[socket] | None], None], sockets: List[socket]) -> None: ...
    def signal_handler(self, sig: int, frame: FrameType | None) -> None:
        """
        A signal handler that is registered with the parent process.
        """
    def run(self) -> None: ...
    def startup(self) -> None: ...
    def shutdown(self) -> None: ...
