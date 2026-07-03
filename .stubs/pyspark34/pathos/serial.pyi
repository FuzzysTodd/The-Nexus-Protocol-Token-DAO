from _typeshed import Incomplete
from pathos.abstract_launcher import AbstractWorkerPool

__all__ = ['SerialPool']

class SerialPool(AbstractWorkerPool):
    """
Mapper that leverages standard (i.e. serial) python maps.
    """
    def map(self, f, *args, **kwds): ...
    def imap(self, f, *args, **kwds): ...
    def pipe(self, f, *args, **kwds): ...
    def restart(self, force: bool = False) -> None:
        """restart a closed pool"""
    def close(self) -> None:
        """close the pool to any new jobs"""
    def terminate(self) -> None:
        """a more abrupt close"""
    def join(self) -> None:
        """cleanup the closed worker processes"""
    def clear(self) -> None:
        """hard restart"""
    nodes: Incomplete
    __state__: Incomplete
PythonSerial = SerialPool
