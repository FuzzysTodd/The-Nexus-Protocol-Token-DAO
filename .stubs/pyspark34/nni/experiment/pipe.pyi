from . import management as management
from _typeshed import Incomplete

class UnixPipe:
    path: Incomplete
    file: Incomplete
    def __init__(self, experiment_id: str) -> None: ...
    def connect(self): ...
    def close(self) -> None: ...
Pipe = UnixPipe
