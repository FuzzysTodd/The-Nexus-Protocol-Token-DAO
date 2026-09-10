from _typeshed import Incomplete

class Unpickler:
    encoding: Incomplete
    readline: Incomplete
    read: Incomplete
    memo: Incomplete
    def __init__(self, file, *, encoding: str = 'bytes') -> None: ...
    metastack: Incomplete
    stack: Incomplete
    append: Incomplete
    def load(self):
        """Read a pickled object representation from the open file.

        Return the reconstituted object hierarchy specified in the file.
        """
    def pop_mark(self): ...
    def persistent_load(self, pid) -> None: ...

def load(file, *, encoding: str = 'ASCII'): ...
