from _typeshed import Incomplete

__all__ = ['BaseManager', 'SyncManager', 'BaseProxy', 'Token', 'SharedMemoryManager']

class Token:
    """
    Type to uniquely identify a shared object
    """
    def __init__(self, typeid, address, id) -> None: ...

class RemoteError(Exception): ...

class Server:
    """
    Server class which runs in a process controlled by a manager object
    """
    public: Incomplete
    registry: Incomplete
    authkey: Incomplete
    listener: Incomplete
    address: Incomplete
    id_to_obj: Incomplete
    id_to_refcount: Incomplete
    id_to_local_proxy_obj: Incomplete
    mutex: Incomplete
    def __init__(self, registry, address, authkey, serializer) -> None: ...
    stop_event: Incomplete
    def serve_forever(self) -> None:
        """
        Run the server forever
        """
    def accepter(self) -> None: ...
    def handle_request(self, conn) -> None:
        """
        Handle a new connection
        """
    def serve_client(self, conn) -> None:
        """
        Handle requests from the proxies in a particular process/thread
        """
    def fallback_getvalue(self, conn, ident, obj): ...
    def fallback_str(self, conn, ident, obj): ...
    def fallback_repr(self, conn, ident, obj): ...
    fallback_mapping: Incomplete
    def dummy(self, c) -> None: ...
    def debug_info(self, c):
        """
        Return some info --- useful to spot problems with refcounting
        """
    def number_of_objects(self, c):
        """
        Number of shared objects
        """
    def shutdown(self, c) -> None:
        """
        Shutdown this process
        """
    def create(self, c, typeid, *args, **kwds):
        """
        Create a new shared object and return its id
        """
    def get_methods(self, c, token):
        """
        Return the methods of the shared object indicated by token
        """
    def accept_connection(self, c, name) -> None:
        """
        Spawn a new thread to serve this connection
        """
    def incref(self, c, ident) -> None: ...
    def decref(self, c, ident) -> None: ...

class State:
    INITIAL: int
    STARTED: int
    SHUTDOWN: int

class BaseManager:
    """
    Base class for managers
    """
    def __init__(self, address: Incomplete | None = None, authkey: Incomplete | None = None, serializer: str = 'pickle', ctx: Incomplete | None = None) -> None: ...
    def get_server(self):
        """
        Return server object with serve_forever() method and address attribute
        """
    def connect(self) -> None:
        """
        Connect manager object to the server process
        """
    shutdown: Incomplete
    def start(self, initializer: Incomplete | None = None, initargs=()) -> None:
        """
        Spawn a server process for this manager object
        """
    def join(self, timeout: Incomplete | None = None) -> None:
        """
        Join the manager process (if it has been spawned)
        """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    @property
    def address(self): ...
    @classmethod
    def register(cls, typeid, callable: Incomplete | None = None, proxytype: Incomplete | None = None, exposed: Incomplete | None = None, method_to_typeid: Incomplete | None = None, create_method: bool = True):
        """
        Register a typeid with the manager type
        """

class ProcessLocalSet(set):
    def __init__(self) -> None: ...
    def __reduce__(self): ...

class BaseProxy:
    """
    A base for proxies of shared objects
    """
    def __init__(self, token, serializer, manager: Incomplete | None = None, authkey: Incomplete | None = None, exposed: Incomplete | None = None, incref: bool = True, manager_owned: bool = False) -> None: ...
    def __reduce__(self): ...
    def __deepcopy__(self, memo): ...

class Namespace:
    def __init__(self, **kwds) -> None: ...

class Value:
    def __init__(self, typecode, value, lock: bool = True) -> None: ...
    def get(self): ...
    def set(self, value) -> None: ...
    value: Incomplete

class IteratorProxy(BaseProxy):
    def __iter__(self): ...
    def __next__(self, *args): ...
    def send(self, *args): ...
    def throw(self, *args): ...
    def close(self, *args): ...

class AcquirerProxy(BaseProxy):
    def acquire(self, blocking: bool = True, timeout: Incomplete | None = None): ...
    def release(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...

class ConditionProxy(AcquirerProxy):
    def wait(self, timeout: Incomplete | None = None): ...
    def notify(self, n: int = 1): ...
    def notify_all(self): ...
    def wait_for(self, predicate, timeout: Incomplete | None = None): ...

class EventProxy(BaseProxy):
    def is_set(self): ...
    def set(self): ...
    def clear(self): ...
    def wait(self, timeout: Incomplete | None = None): ...

class BarrierProxy(BaseProxy):
    def wait(self, timeout: Incomplete | None = None): ...
    def abort(self): ...
    def reset(self): ...
    @property
    def parties(self): ...
    @property
    def n_waiting(self): ...
    @property
    def broken(self): ...

class NamespaceProxy(BaseProxy):
    def __getattr__(self, key): ...
    def __setattr__(self, key, value): ...
    def __delattr__(self, key): ...

class ValueProxy(BaseProxy):
    def get(self): ...
    def set(self, value): ...
    value: Incomplete
    __class_getitem__: Incomplete

class ListProxy(BaseListProxy):
    def __iadd__(self, value): ...
    def __imul__(self, value): ...

class PoolProxy(BasePoolProxy):
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class SyncManager(BaseManager):
    """
    Subclass of `BaseManager` which supports a number of shared object types.

    The types registered are those intended for the synchronization
    of threads, plus `dict`, `list` and `Namespace`.

    The `multiprocess.Manager()` function creates started instances of
    this class.
    """

class _SharedMemoryTracker:
    """Manages one or more shared memory segments."""
    shared_memory_context_name: Incomplete
    segment_names: Incomplete
    def __init__(self, name, segment_names=[]) -> None: ...
    def register_segment(self, segment_name) -> None:
        """Adds the supplied shared memory block name to tracker."""
    def destroy_segment(self, segment_name) -> None:
        """Calls unlink() on the shared memory block with the supplied name
            and removes it from the list of blocks being tracked."""
    def unlink(self) -> None:
        """Calls destroy_segment() on all tracked shared memory blocks."""
    def __del__(self) -> None: ...

class SharedMemoryServer(Server):
    public: Incomplete
    shared_memory_context: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def create(self, c, typeid, *args, **kwargs):
        """Create a new distributed-shared object (not backed by a shared
            memory block) and return its id to be used in a Proxy Object."""
    def shutdown(self, c):
        """Call unlink() on all tracked shared memory, terminate the Server."""
    def track_segment(self, c, segment_name) -> None:
        """Adds the supplied shared memory block name to Server's tracker."""
    def release_segment(self, c, segment_name) -> None:
        """Calls unlink() on the shared memory block with the supplied name
            and removes it from the tracker instance inside the Server."""
    def list_segments(self, c):
        """Returns a list of names of shared memory blocks that the Server
            is currently tracking."""

class SharedMemoryManager(BaseManager):
    """Like SyncManager but uses SharedMemoryServer instead of Server.

        It provides methods for creating and returning SharedMemory instances
        and for creating a list-like object (ShareableList) backed by shared
        memory.  It also provides methods that create and return Proxy Objects
        that support synchronization across processes (i.e. multi-process-safe
        locks and semaphores).
        """
    def __init__(self, *args, **kwargs) -> None: ...
    def __del__(self) -> None: ...
    def get_server(self):
        """Better than monkeypatching for now; merge into Server ultimately"""
    def SharedMemory(self, size):
        """Returns a new SharedMemory instance with the specified size in
            bytes, to be tracked by the manager."""
    def ShareableList(self, sequence):
        """Returns a new ShareableList instance populated with the values
            from the input sequence, to be tracked by the manager."""
