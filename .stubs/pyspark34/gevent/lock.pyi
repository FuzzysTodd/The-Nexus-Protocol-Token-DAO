from _typeshed import Incomplete
from gevent._semaphore import BoundedSemaphore as BoundedSemaphore, Semaphore as Semaphore

__all__ = ['Semaphore', 'BoundedSemaphore', 'DummySemaphore', 'RLock']

class _GILLock:
    def __init__(self) -> None: ...
    def acquire(self): ...
    def release(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def locked(self): ...

class _AtomicSemaphoreMixin:
    def __init__(self, *args, **kwargs) -> None: ...
    def release(self): ...
    def acquire(self, blocking: bool = True, timeout: Incomplete | None = None): ...
    def wait(self, timeout: Incomplete | None = None): ...

class _AtomicSemaphore(_AtomicSemaphoreMixin, Semaphore):
    __doc__: Incomplete

class _AtomicBoundedSemaphore(_AtomicSemaphoreMixin, BoundedSemaphore):
    __doc__: Incomplete
    def release(self): ...

class DummySemaphore:
    '''
    DummySemaphore(value=None) -> DummySemaphore

    An object with the same API as :class:`Semaphore`,
    initialized with "infinite" initial value. None of its
    methods ever block.

    This can be used to parameterize on whether or not to actually
    guard access to a potentially limited resource. If the resource is
    actually limited, such as a fixed-size thread pool, use a real
    :class:`Semaphore`, but if the resource is unbounded, use an
    instance of this class. In that way none of the supporting code
    needs to change.

    Similarly, it can be used to parameterize on whether or not to
    enforce mutual exclusion to some underlying object. If the
    underlying object is known to be thread-safe itself mutual
    exclusion is not needed and a ``DummySemaphore`` can be used, but
    if that\'s not true, use a real ``Semaphore``.
    '''
    def __init__(self, value: Incomplete | None = None) -> None:
        """
        .. versionchanged:: 1.1rc3
            Accept and ignore a *value* argument for compatibility with Semaphore.
        """
    def locked(self):
        """A DummySemaphore is never locked so this always returns False."""
    def ready(self):
        """A DummySemaphore is never locked so this always returns True."""
    def release(self) -> None:
        """Releasing a dummy semaphore does nothing."""
    def rawlink(self, callback) -> None: ...
    def unlink(self, callback) -> None: ...
    def wait(self, timeout: Incomplete | None = None):
        """Waiting for a DummySemaphore returns immediately."""
    def acquire(self, blocking: bool = True, timeout: Incomplete | None = None):
        """
        A DummySemaphore can always be acquired immediately so this always
        returns True and ignores its arguments.

        .. versionchanged:: 1.1a1
           Always return *true*.
        """
    def __enter__(self) -> None: ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: types.TracebackType | None) -> None: ...

class RLock:
    """
    A mutex that can be acquired more than once by the same greenlet.

    A mutex can only be locked by one greenlet at a time. A single greenlet
    can `acquire` the mutex as many times as desired, though. Each call to
    `acquire` must be paired with a matching call to `release`.

    It is an error for a greenlet that has not acquired the mutex
    to release it.

    Instances are context managers.
    """
    def __init__(self, hub: Incomplete | None = None) -> None:
        """
        .. versionchanged:: 20.5.1
           Add the ``hub`` argument.
        """
    def acquire(self, blocking: bool = True, timeout: Incomplete | None = None):
        """
        Acquire the mutex, blocking if *blocking* is true, for up to
        *timeout* seconds.

        .. versionchanged:: 1.5a4
           Added the *timeout* parameter.

        :return: A boolean indicating whether the mutex was acquired.
        """
    def __enter__(self): ...
    def release(self) -> None:
        """
        Release the mutex.

        Only the greenlet that originally acquired the mutex can
        release it.
        """
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
