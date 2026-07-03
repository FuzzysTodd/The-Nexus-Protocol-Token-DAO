from _typeshed import Incomplete
from gitdb.db.base import CompoundDB, FileDBBase, ObjectDBW
from gitdb.db.loose import LooseObjectDB
from gitdb.db.pack import PackedDB
from gitdb.db.ref import ReferenceDB

__all__ = ['GitDB']

class GitDB(FileDBBase, ObjectDBW, CompoundDB):
    """A git-style object database, which contains all objects in the 'objects'
    subdirectory

    ``IMPORTANT``: The usage of this implementation is highly discouraged as it fails to release file-handles.
    This can be a problem with long-running processes and/or big repositories.
    """
    PackDBCls = PackedDB
    LooseDBCls = LooseObjectDB
    ReferenceDBCls = ReferenceDB
    packs_dir: str
    loose_dir: str
    alternates_dir: Incomplete
    def __init__(self, root_path) -> None:
        """Initialize ourselves on a git objects directory"""
    def store(self, istream): ...
    def ostream(self): ...
    def set_ostream(self, ostream): ...
