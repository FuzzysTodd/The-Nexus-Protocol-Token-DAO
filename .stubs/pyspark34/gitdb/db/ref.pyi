from _typeshed import Incomplete
from gitdb.db.base import CompoundDB

__all__ = ['ReferenceDB']

class ReferenceDB(CompoundDB):
    """A database consisting of database referred to in a file"""
    ObjectDBCls: Incomplete
    def __init__(self, ref_file) -> None: ...
    def update_cache(self, force: bool = False): ...
