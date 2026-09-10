from mypy.ipc import IPCBase as IPCBase
from typing import Any
from typing_extensions import Final

DEFAULT_STATUS_FILE: Final[str]

def receive(connection: IPCBase) -> Any:
    """Receive JSON data from a connection until EOF.

    Raise OSError if the data received is not valid JSON or if it is
    not a dict.
    """
