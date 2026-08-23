from _typeshed import Incomplete
from pathos.abstract_launcher import AbstractWorkerPool
from pathos.helpers import ProcessPool as Pool

__all__ = ['ProcessPool', '_ProcessPool']

_ProcessPool = Pool

class ProcessPool(AbstractWorkerPool):
    """
Mapper that leverages python's multiprocessing.
    """
    def __init__(self, *args, **kwds) -> None:
        """
NOTE: if number of nodes is not given, will autodetect processors.

NOTE: additional keyword input is optional, with:
    id          - identifier for the pool
    initializer - function that takes no input, called when node is spawned
    initargs    - tuple of args for initializers that have args
    maxtasksperchild - int that limits the max number of tasks per node
        """
    clear: Incomplete
    def map(self, f, *args, **kwds): ...
    def imap(self, f, *args, **kwds): ...
    def uimap(self, f, *args, **kwds): ...
    def amap(self, f, *args, **kwds): ...
    def pipe(self, f, *args, **kwds): ...
    def apipe(self, f, *args, **kwds): ...
    def restart(self, force: bool = False):
        """restart a closed pool"""
    def close(self) -> None:
        """close the pool to any new jobs"""
    def terminate(self) -> None:
        """a more abrupt close"""
    def join(self) -> None:
        """cleanup the closed worker processes"""
    ncpus: Incomplete
    nodes: Incomplete
    __state__: Incomplete
ProcessingPool = ProcessPool
