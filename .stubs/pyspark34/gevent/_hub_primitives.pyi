from _typeshed import Incomplete

__all__ = ['WaitOperationsGreenlet', 'iwait_on_objects', 'wait_on_objects', 'wait_read', 'wait_write', 'wait_readwrite']

class WaitOperationsGreenlet(SwitchOutGreenletWithLoop):
    def wait(self, watcher) -> None:
        """
        Wait until the *watcher* (which must not be started) is ready.

        The current greenlet will be unscheduled during this time.
        """
    def cancel_waits_close_and_then(self, watchers, exc_kind, then, *then_args) -> None: ...
    def cancel_wait(self, watcher, error, close_watcher: bool = False) -> None:
        """
        Cancel an in-progress call to :meth:`wait` by throwing the given *error*
        in the waiting greenlet.

        .. versionchanged:: 1.3a1
           Added the *close_watcher* parameter. If true, the watcher
           will be closed after the exception is thrown. The watcher should then
           be discarded. Closing the watcher is important to release native resources.
        .. versionchanged:: 1.3a2
           Allow the *watcher* to be ``None``. No action is taken in that case.

        """

class _WaitIterator:
    def __init__(self, objects, hub, timeout, count) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__
    def __enter__(self): ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...

def iwait_on_objects(objects, timeout: Incomplete | None = None, count: Incomplete | None = None):
    """
    Iteratively yield *objects* as they are ready, until all (or *count*) are ready
    or *timeout* expired.

    If you will only be consuming a portion of the *objects*, you should
    do so inside a ``with`` block on this object to avoid leaking resources::

        with gevent.iwait((a, b, c)) as it:
            for i in it:
                if i is a:
                    break

    :param objects: A sequence (supporting :func:`len`) containing objects
        implementing the wait protocol (rawlink() and unlink()).
    :keyword int count: If not `None`, then a number specifying the maximum number
        of objects to wait for. If ``None`` (the default), all objects
        are waited for.
    :keyword float timeout: If given, specifies a maximum number of seconds
        to wait. If the timeout expires before the desired waited-for objects
        are available, then this method returns immediately.

    .. seealso:: :func:`wait`

    .. versionchanged:: 1.1a1
       Add the *count* parameter.
    .. versionchanged:: 1.1a2
       No longer raise :exc:`LoopExit` if our caller switches greenlets
       in between items yielded by this function.
    .. versionchanged:: 1.4
       Add support to use the returned object as a context manager.
    """
def wait_on_objects(objects: Incomplete | None = None, timeout: Incomplete | None = None, count: Incomplete | None = None):
    """
    Wait for *objects* to become ready or for event loop to finish.

    If *objects* is provided, it must be a list containing objects
    implementing the wait protocol (rawlink() and unlink() methods):

    - :class:`gevent.Greenlet` instance
    - :class:`gevent.event.Event` instance
    - :class:`gevent.lock.Semaphore` instance
    - :class:`gevent.subprocess.Popen` instance

    If *objects* is ``None`` (the default), ``wait()`` blocks until
    the current event loop has nothing to do (or until *timeout* passes):

    - all greenlets have finished
    - all servers were stopped
    - all event loop watchers were stopped.

    If *count* is ``None`` (the default), wait for all *objects*
    to become ready.

    If *count* is a number, wait for (up to) *count* objects to become
    ready. (For example, if count is ``1`` then the function exits
    when any object in the list is ready).

    If *timeout* is provided, it specifies the maximum number of
    seconds ``wait()`` will block.

    Returns the list of ready objects, in the order in which they were
    ready.

    .. seealso:: :func:`iwait`
    """
def wait_read(fileno, timeout: Incomplete | None = None, timeout_exc=...):
    """
    wait_read(fileno, timeout=None, [timeout_exc=None]) -> None

    Block the current greenlet until *fileno* is ready to read.

    For the meaning of the other parameters and possible exceptions,
    see :func:`wait`.

    .. seealso:: :func:`cancel_wait`
    """
def wait_write(fileno, timeout: Incomplete | None = None, timeout_exc=..., event=...):
    """
    wait_write(fileno, timeout=None, [timeout_exc=None]) -> None

    Block the current greenlet until *fileno* is ready to write.

    For the meaning of the other parameters and possible exceptions,
    see :func:`wait`.

    .. deprecated:: 1.1
       The keyword argument *event* is ignored. Applications should not pass this parameter.
       In the future, doing so will become an error.

    .. seealso:: :func:`cancel_wait`
    """
def wait_readwrite(fileno, timeout: Incomplete | None = None, timeout_exc=..., event=...):
    """
    wait_readwrite(fileno, timeout=None, [timeout_exc=None]) -> None

    Block the current greenlet until *fileno* is ready to read or
    write.

    For the meaning of the other parameters and possible exceptions,
    see :func:`wait`.

    .. deprecated:: 1.1
       The keyword argument *event* is ignored. Applications should not pass this parameter.
       In the future, doing so will become an error.

    .. seealso:: :func:`cancel_wait`
    """
