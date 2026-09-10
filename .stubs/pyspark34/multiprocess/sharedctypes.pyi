from _typeshed import Incomplete

__all__ = ['RawValue', 'RawArray', 'Value', 'Array', 'copy', 'synchronized']

def RawValue(typecode_or_type, *args):
    """
    Returns a ctypes object allocated from shared memory
    """
def RawArray(typecode_or_type, size_or_initializer):
    """
    Returns a ctypes array allocated from shared memory
    """
def Value(typecode_or_type, *args, lock: bool = True, ctx: Incomplete | None = None):
    """
    Return a synchronization wrapper for a Value
    """
def Array(typecode_or_type, size_or_initializer, *, lock: bool = True, ctx: Incomplete | None = None):
    """
    Return a synchronization wrapper for a RawArray
    """
def copy(obj): ...
def synchronized(obj, lock: Incomplete | None = None, ctx: Incomplete | None = None): ...

class SynchronizedBase:
    acquire: Incomplete
    release: Incomplete
    def __init__(self, obj, lock: Incomplete | None = None, ctx: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def __reduce__(self): ...
    def get_obj(self): ...
    def get_lock(self): ...

class Synchronized(SynchronizedBase):
    value: Incomplete

class SynchronizedArray(SynchronizedBase):
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __setitem__(self, i, value) -> None: ...
    def __getslice__(self, start, stop): ...
    def __setslice__(self, start, stop, values) -> None: ...

class SynchronizedString(SynchronizedArray):
    value: Incomplete
    raw: Incomplete
