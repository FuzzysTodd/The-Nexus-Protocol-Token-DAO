from _typeshed import Incomplete

__all__ = ['Timeout', 'with_timeout']

class _FakeTimer:
    @property
    def pending(self): ...
    active = pending
    @property
    def seconds(self) -> None:
        """Always returns None"""
    timer = seconds
    exception = seconds
    def start(self, *args, **kwargs) -> None: ...
    def stop(self) -> None: ...
    cancel = stop
    stop = cancel
    close = cancel
    def __enter__(self): ...
    def __exit__(self, _t: type[BaseException] | None, _v: BaseException | None, _tb: types.TracebackType | None) -> None: ...

class Timeout(BaseException):
    '''
    Timeout(seconds=None, exception=None, ref=True, priority=-1)

    Raise *exception* in the current greenlet after *seconds*
    have elapsed::

        timeout = Timeout(seconds, exception)
        timeout.start()
        try:
            ...  # exception will be raised here, after *seconds* passed since start() call
        finally:
            timeout.close()

    .. warning::

        You must **always** call `close` on a ``Timeout`` object you have created,
        whether or not the code that the timeout was protecting finishes
        executing before the timeout elapses (whether or not the
        ``Timeout`` exception is raised)  This ``try/finally``
        construct or a ``with`` statement is a good pattern. (If
        the timeout object will be started again, use `cancel` instead
        of `close`; this is rare. You must still `close` it when you are
        done.)

    When *exception* is omitted or ``None``, the ``Timeout`` instance
    itself is raised::

        >>> import gevent
        >>> gevent.Timeout(0.1).start()
        >>> gevent.sleep(0.2)  #doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
         ...
        Timeout: 0.1 seconds

    If the *seconds* argument is not given or is ``None`` (e.g.,
    ``Timeout()``), then the timeout will never expire and never raise
    *exception*. This is convenient for creating functions which take
    an optional timeout parameter of their own. (Note that this is **not**
    the same thing as a *seconds* value of ``0``.)

    ::

       def function(args, timeout=None):
          "A function with an optional timeout."
          timer = Timeout(timeout)
          with timer:
             ...

    .. caution::

        A *seconds* value less than ``0.0`` (e.g., ``-1``) is poorly defined. In the future,
        support for negative values is likely to do the same thing as a value
        of ``None`` or ``0``

    A *seconds* value of ``0`` requests that the event loop spin and poll for I/O;
    it will immediately expire as soon as control returns to the event loop.

    .. rubric:: Use As A Context Manager

    To simplify starting and canceling timeouts, the ``with``
    statement can be used::

        with gevent.Timeout(seconds, exception) as timeout:
            pass  # ... code block ...

    This is equivalent to the try/finally block above with one
    additional feature: if *exception* is the literal ``False``, the
    timeout is still raised, but the context manager suppresses it, so
    the code outside the with-block won\'t see it.

    This is handy for adding a timeout to the functions that don\'t
    support a *timeout* parameter themselves::

        data = None
        with gevent.Timeout(5, False):
            data = mysock.makefile().readline()
        if data is None:
            ...  # 5 seconds passed without reading a line
        else:
            ...  # a line was read within 5 seconds

    .. caution::

        If ``readline()`` above catches and doesn\'t re-raise
        :exc:`BaseException` (for example, with a bare ``except:``), then
        your timeout will fail to function and control won\'t be returned
        to you when you expect.

    .. rubric:: Catching Timeouts

    When catching timeouts, keep in mind that the one you catch may
    not be the one you have set (a calling function may have set its
    own timeout); if you going to silence a timeout, always check that
    it\'s the instance you need::

        timeout = Timeout(1)
        timeout.start()
        try:
            ...
        except Timeout as t:
            if t is not timeout:
                raise # not my timeout
        finally:
            timeout.close()


    .. versionchanged:: 1.1b2

        If *seconds* is not given or is ``None``, no longer allocate a
        native timer object that will never be started.

    .. versionchanged:: 1.1

        Add warning about negative *seconds* values.

    .. versionchanged:: 1.3a1

        Timeout objects now have a :meth:`close`
        method that *must* be called when the timeout will no longer be
        used to properly clean up native resources.
        The ``with`` statement does this automatically.

    '''
    seconds: Incomplete
    exception: Incomplete
    timer: Incomplete
    def __init__(self, seconds: Incomplete | None = None, exception: Incomplete | None = None, ref: bool = True, priority: int = -1, _one_shot: bool = False) -> None: ...
    def start(self) -> None:
        """Schedule the timeout."""
    @classmethod
    def start_new(cls, timeout: Incomplete | None = None, exception: Incomplete | None = None, ref: bool = True, _one_shot: bool = False):
        """Create a started :class:`Timeout`.

        This is a shortcut, the exact action depends on *timeout*'s type:

        * If *timeout* is a :class:`Timeout`, then call its :meth:`start` method
          if it's not already begun.
        * Otherwise, create a new :class:`Timeout` instance, passing (*timeout*, *exception*) as
          arguments, then call its :meth:`start` method.

        Returns the :class:`Timeout` instance.
        """
    @property
    def pending(self):
        """True if the timeout is scheduled to be raised."""
    def cancel(self) -> None:
        """
        If the timeout is pending, cancel it. Otherwise, do nothing.

        The timeout object can be :meth:`started <start>` again. If
        you will not start the timeout again, you should use
        :meth:`close` instead.
        """
    def close(self) -> None:
        """
        Close the timeout and free resources. The timer cannot be started again
        after this method has been used.
        """
    def __enter__(self):
        """
        Start and return the timer. If the timer is already started, just return it.
        """
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None):
        """
        Stop the timer.

        .. versionchanged:: 1.3a1
           The underlying native timer is also stopped. This object cannot be
           used again.
        """

def with_timeout(seconds, function, *args, **kwds):
    """Wrap a call to *function* with a timeout; if the called
    function fails to return before the timeout, cancel it and return a
    flag value, provided by *timeout_value* keyword argument.

    If timeout expires but *timeout_value* is not provided, raise :class:`Timeout`.

    Keyword argument *timeout_value* is not passed to *function*.
    """
