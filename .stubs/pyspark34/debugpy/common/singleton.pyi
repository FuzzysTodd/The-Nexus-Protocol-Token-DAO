from _typeshed import Incomplete

class Singleton:
    """A base class for a class of a singleton object.

    For any derived class T, the first invocation of T() will create the instance,
    and any future invocations of T() will return that instance.

    Concurrent invocations of T() from different threads are safe.
    """
    def __new__(cls, *args, **kwargs): ...
    def __init__(self, *args, **kwargs) -> None:
        """Initializes the singleton instance. Guaranteed to only be invoked once for
        any given type derived from Singleton.

        If shared=False, the caller is requesting a singleton instance for their own
        exclusive use. This is only allowed if the singleton has not been created yet;
        if so, it is created and marked as being in exclusive use. While it is marked
        as such, all attempts to obtain an existing instance of it immediately raise
        an exception. The singleton can eventually be promoted to shared use by calling
        share() on it.
        """
    def __enter__(self):
        """Lock this singleton to prevent concurrent access."""
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None:
        """Unlock this singleton to allow concurrent access."""
    def share(self) -> None:
        """Share this singleton, if it was originally created with shared=False."""

class ThreadSafeSingleton(Singleton):
    """A singleton that incorporates a lock for thread-safe access to its members.

    The lock can be acquired using the context manager protocol, and thus idiomatic
    use is in conjunction with a with-statement. For example, given derived class T::

        with T() as t:
            t.x = t.frob(t.y)

    All access to the singleton from the outside should follow this pattern for both
    attributes and method calls. Singleton members can assume that self is locked by
    the caller while they're executing, but recursive locking of the same singleton
    on the same thread is also permitted.
    """
    threadsafe_attrs: Incomplete
    readonly_attrs: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def assert_locked(self) -> None: ...
    def __getattribute__(self, name): ...
    def __setattr__(self, name, value): ...

def threadsafe_method(func):
    """Marks a method of a ThreadSafeSingleton-derived class as inherently thread-safe.

    A method so marked must either not use any singleton state, or lock it appropriately.
    """
def autolocked_method(func):
    """Automatically synchronizes all calls of a method of a ThreadSafeSingleton-derived
    class by locking the singleton for the duration of each call.
    """
