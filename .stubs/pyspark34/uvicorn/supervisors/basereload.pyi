from _typeshed import Incomplete
from pathlib import Path
from socket import socket
from types import FrameType
from typing import Callable, Iterator, List
from uvicorn._subprocess import get_subprocess as get_subprocess
from uvicorn.config import Config as Config

HANDLED_SIGNALS: Incomplete
logger: Incomplete

class BaseReload:
    config: Incomplete
    target: Incomplete
    sockets: Incomplete
    should_exit: Incomplete
    pid: Incomplete
    is_restarting: bool
    reloader_name: Incomplete
    def __init__(self, config: Config, target: Callable[[List[socket] | None], None], sockets: List[socket]) -> None: ...
    def signal_handler(self, sig: int, frame: FrameType | None) -> None:
        """
        A signal handler that is registered with the parent process.
        """
    def run(self) -> None: ...
    def pause(self) -> None: ...
    def __iter__(self) -> Iterator[List[Path] | None]: ...
    def __next__(self) -> List[Path] | None: ...
    process: Incomplete
    def startup(self) -> None: ...
    def restart(self) -> None: ...
    def shutdown(self) -> None: ...
    def should_restart(self) -> List[Path] | None: ...
