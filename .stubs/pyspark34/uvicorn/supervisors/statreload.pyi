from _typeshed import Incomplete
from pathlib import Path
from socket import socket
from typing import Callable, Iterator, List
from uvicorn.config import Config as Config
from uvicorn.supervisors.basereload import BaseReload as BaseReload

logger: Incomplete

class StatReload(BaseReload):
    reloader_name: str
    mtimes: Incomplete
    def __init__(self, config: Config, target: Callable[[List[socket] | None], None], sockets: List[socket]) -> None: ...
    def should_restart(self) -> List[Path] | None: ...
    def restart(self) -> None: ...
    def iter_py_files(self) -> Iterator[Path]: ...
