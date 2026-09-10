import logging
from _typeshed import Incomplete

__version__: str

class DistlibException(Exception): ...

class NullHandler(logging.Handler):
    def handle(self, record) -> None: ...
    def emit(self, record) -> None: ...
    lock: Incomplete
    def createLock(self) -> None: ...

logger: Incomplete
