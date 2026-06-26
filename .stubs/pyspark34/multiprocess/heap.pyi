from _typeshed import Incomplete

__all__ = ['BufferWrapper']

class Arena:
    """
        A shared memory area backed by a temporary file (POSIX).
        """
    size: Incomplete
    fd: Incomplete
    buffer: Incomplete
    def __init__(self, size, fd: int = -1) -> None: ...

class Heap:
    def __init__(self, size=...) -> None: ...
    def free(self, block) -> None: ...
    def malloc(self, size): ...

class BufferWrapper:
    def __init__(self, size) -> None: ...
    def create_memoryview(self): ...
