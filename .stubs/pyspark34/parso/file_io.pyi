import os
from _typeshed import Incomplete

class FileIO:
    path: Incomplete
    def __init__(self, path: os.PathLike | str) -> None: ...
    def read(self): ...
    def get_last_modified(self):
        """
        Returns float - timestamp or None, if path doesn't exist.
        """

class KnownContentFileIO(FileIO):
    def __init__(self, path, content) -> None: ...
    def read(self): ...
