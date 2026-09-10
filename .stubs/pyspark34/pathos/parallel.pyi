from _typeshed import Incomplete
from pathos.abstract_launcher import AbstractWorkerPool

__all__ = ['ParallelPool', 'stats']

def stats(pool: Incomplete | None = None):
    """return a string containing stats response from the pp.Server"""

class ParallelPool(AbstractWorkerPool):
    """
Mapper that leverages parallelpython (i.e. pp) maps.
    """
    def __init__(self, *args, **kwds) -> None:
        """
NOTE: if number of nodes is not given, will autodetect processors.

NOTE: if a tuple of servers is not provided, defaults to localhost only.

NOTE: additional keyword input is optional, with:
    id          - identifier for the pool
    servers     - tuple of pp.Servers
        """
    clear: Incomplete
    def map(self, f, *args, **kwds): ...
    def imap(self, f, *args, **kwds): ...
    def uimap(self, f, *args, **kwds): ...
    def amap(self, f, *args, **kwds): ...
    def pipe(self, f, *args, **kwds): ...
    def apipe(self, f, *args, **kwds): ...
    def restart(self, force: bool = False) -> None:
        """restart a closed pool"""
    def close(self) -> None:
        """close the pool to any new jobs"""
    def terminate(self) -> None:
        """a more abrupt close"""
    def join(self) -> None:
        """cleanup the closed worker processes"""
    ncpus: Incomplete
    nodes: Incomplete
    servers: Incomplete
    __state__: Incomplete
ParallelPythonPool = ParallelPool
