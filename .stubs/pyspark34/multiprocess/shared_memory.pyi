from _typeshed import Incomplete

__all__ = ['SharedMemory', 'ShareableList']

class SharedMemory:
    """Creates a new shared memory block or attaches to an existing
    shared memory block.

    Every shared memory block is assigned a unique name.  This enables
    one process to create a shared memory block with a particular name
    so that a different process can attach to that same shared memory
    block using that same name.

    As a resource for sharing data across processes, shared memory blocks
    may outlive the original process that created them.  When one process
    no longer needs access to a shared memory block that might still be
    needed by other processes, the close() method should be called.
    When a shared memory block is no longer needed by any process, the
    unlink() method should be called to ensure proper cleanup."""
    def __init__(self, name: Incomplete | None = None, create: bool = False, size: int = 0) -> None: ...
    def __del__(self) -> None: ...
    def __reduce__(self): ...
    @property
    def buf(self):
        """A memoryview of contents of the shared memory block."""
    @property
    def name(self):
        """Unique name that identifies the shared memory block."""
    @property
    def size(self):
        """Size in bytes."""
    def close(self) -> None:
        """Closes access to the shared memory from this instance but does
        not destroy the shared memory block."""
    def unlink(self) -> None:
        """Requests that the underlying shared memory block be destroyed.

        In order to ensure proper cleanup of resources, unlink should be
        called once (and only once) across all processes which have access
        to the shared memory block."""

class ShareableList:
    """Pattern for a mutable list-like object shareable via a shared
    memory block.  It differs from the built-in list type in that these
    lists can not change their overall length (i.e. no append, insert,
    etc.)

    Because values are packed into a memoryview as bytes, the struct
    packing format for any storable value must require no more than 8
    characters to describe its format."""
    shm: Incomplete
    def __init__(self, sequence: Incomplete | None = None, *, name: Incomplete | None = None) -> None: ...
    def __getitem__(self, position): ...
    def __setitem__(self, position, value) -> None: ...
    def __reduce__(self): ...
    def __len__(self) -> int: ...
    @property
    def format(self):
        """The struct packing format used by all currently stored items."""
    def count(self, value):
        """L.count(value) -> integer -- return number of occurrences of value."""
    def index(self, value):
        """L.index(value) -> integer -- return first index of value.
        Raises ValueError if the value is not present."""
    __class_getitem__: Incomplete
