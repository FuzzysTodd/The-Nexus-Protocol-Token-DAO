from _typeshed import Incomplete
from multiprocessing.context import SpawnProcess
from socket import socket
from typing import Callable, List
from uvicorn.config import Config as Config

spawn: Incomplete

def get_subprocess(config: Config, target: Callable[..., None], sockets: List[socket]) -> SpawnProcess:
    """
    Called in the parent process, to instantiate a new child process instance.
    The child is not yet started at this point.

    * config - The Uvicorn configuration instance.
    * target - A callable that accepts a list of sockets. In practice this will
               be the `Server.run()` method.
    * sockets - A list of sockets to pass to the server. Sockets are bound once
                by the parent process, and then passed to the child processes.
    """
def subprocess_started(config: Config, target: Callable[..., None], sockets: List[socket], stdin_fileno: int | None) -> None:
    """
    Called when the child process starts.

    * config - The Uvicorn configuration instance.
    * target - A callable that accepts a list of sockets. In practice this will
               be the `Server.run()` method.
    * sockets - A list of sockets to pass to the server. Sockets are bound once
                by the parent process, and then passed to the child processes.
    * stdin_fileno - The file number of sys.stdin, so that it can be reattached
                     to the child process.
    """
