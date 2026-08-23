import typing as t
import typing_extensions as te
from _typeshed import Incomplete
from blinker._utilities import IdentityType as IdentityType, WeakTypes as WeakTypes, annotatable_weakref as annotatable_weakref, hashable_identity as hashable_identity, is_coroutine_function as is_coroutine_function, lazy_property as lazy_property, reference as reference, symbol as symbol
from weakref import WeakValueDictionary

T_callable = t.TypeVar('T_callable', bound=t.Callable[..., t.Any])
T = t.TypeVar('T')
P = te.ParamSpec('P')
AsyncWrapperType: Incomplete
SyncWrapperType: Incomplete
ANY: Incomplete
ANY_ID: int

class Signal:
    """A notification emitter."""
    ANY = ANY
    def receiver_connected(self) -> Signal:
        """Emitted after each :meth:`connect`.

        The signal sender is the signal instance, and the :meth:`connect`
        arguments are passed through: *receiver*, *sender*, and *weak*.

        .. versionadded:: 1.2

        """
    def receiver_disconnected(self) -> Signal:
        """Emitted after :meth:`disconnect`.

        The sender is the signal instance, and the :meth:`disconnect` arguments
        are passed through: *receiver* and *sender*.

        Note, this signal is emitted **only** when :meth:`disconnect` is
        called explicitly.

        The disconnect signal can not be emitted by an automatic disconnect
        (due to a weakly referenced receiver or sender going out of scope),
        as the receiver and/or sender instances are no longer available for
        use at the time this signal would be emitted.

        An alternative approach is available by subscribing to
        :attr:`receiver_connected` and setting up a custom weakref cleanup
        callback on weak receivers and senders.

        .. versionadded:: 1.2

        """
    __doc__: Incomplete
    receivers: Incomplete
    is_muted: bool
    def __init__(self, doc: str | None = None) -> None:
        """
        :param doc: optional.  If provided, will be assigned to the signal's
          __doc__ attribute.

        """
    def connect(self, receiver: T_callable, sender: t.Any = ..., weak: bool = True) -> T_callable:
        """Connect *receiver* to signal events sent by *sender*.

        :param receiver: A callable.  Will be invoked by :meth:`send` with
          `sender=` as a single positional argument and any ``kwargs`` that
          were provided to a call to :meth:`send`.

        :param sender: Any object or :obj:`ANY`, defaults to ``ANY``.
          Restricts notifications delivered to *receiver* to only those
          :meth:`send` emissions sent by *sender*.  If ``ANY``, the receiver
          will always be notified.  A *receiver* may be connected to
          multiple *sender* values on the same Signal through multiple calls
          to :meth:`connect`.

        :param weak: If true, the Signal will hold a weakref to *receiver*
          and automatically disconnect when *receiver* goes out of scope or
          is garbage collected.  Defaults to True.

        """
    def connect_via(self, sender: t.Any, weak: bool = False) -> t.Callable[[T_callable], T_callable]:
        """Connect the decorated function as a receiver for *sender*.

        :param sender: Any object or :obj:`ANY`.  The decorated function
          will only receive :meth:`send` emissions sent by *sender*.  If
          ``ANY``, the receiver will always be notified.  A function may be
          decorated multiple times with differing *sender* values.

        :param weak: If true, the Signal will hold a weakref to the
          decorated function and automatically disconnect when *receiver*
          goes out of scope or is garbage collected.  Unlike
          :meth:`connect`, this defaults to False.

        The decorated function will be invoked by :meth:`send` with
          `sender=` as a single positional argument and any ``kwargs`` that
          were provided to the call to :meth:`send`.


        .. versionadded:: 1.1

        """
    def connected_to(self, receiver: t.Callable, sender: t.Any = ...) -> t.Generator[None, None, None]:
        """Execute a block with the signal temporarily connected to *receiver*.

        :param receiver: a receiver callable
        :param sender: optional, a sender to filter on

        This is a context manager for use in the ``with`` statement.  It can
        be useful in unit tests.  *receiver* is connected to the signal for
        the duration of the ``with`` block, and will be disconnected
        automatically when exiting the block:

        .. code-block:: python

          with on_ready.connected_to(receiver):
             # do stuff
             on_ready.send(123)

        .. versionadded:: 1.1

        """
    def muted(self) -> t.Generator[None, None, None]:
        """Context manager for temporarily disabling signal.
        Useful for test purposes.
        """
    def temporarily_connected_to(self, receiver: t.Callable, sender: t.Any = ...) -> t.ContextManager[None]:
        """An alias for :meth:`connected_to`.

        :param receiver: a receiver callable
        :param sender: optional, a sender to filter on

        .. versionadded:: 0.9

        .. versionchanged:: 1.1
          Renamed to :meth:`connected_to`.  ``temporarily_connected_to`` was
          deprecated in 1.2 and will be removed in a subsequent version.

        """
    def send(self, *sender: t.Any, _async_wrapper: AsyncWrapperType | None = None, **kwargs: t.Any) -> list[tuple[t.Callable, t.Any]]:
        """Emit this signal on behalf of *sender*, passing on ``kwargs``.

        Returns a list of 2-tuples, pairing receivers with their return
        value. The ordering of receiver notification is undefined.

        :param sender: Any object or ``None``.  If omitted, synonymous
          with ``None``.  Only accepts one positional argument.
        :param _async_wrapper: A callable that should wrap a coroutine
          receiver and run it when called synchronously.

        :param kwargs: Data to be sent to receivers.
        """
    async def send_async(self, *sender: t.Any, _sync_wrapper: SyncWrapperType | None = None, **kwargs: t.Any) -> list[tuple[t.Callable, t.Any]]:
        """Emit this signal on behalf of *sender*, passing on ``kwargs``.

        Returns a list of 2-tuples, pairing receivers with their return
        value. The ordering of receiver notification is undefined.

        :param sender: Any object or ``None``.  If omitted, synonymous
          with ``None``. Only accepts one positional argument.
        :param _sync_wrapper: A callable that should wrap a synchronous
          receiver and run it when awaited.

        :param kwargs: Data to be sent to receivers.
        """
    def has_receivers_for(self, sender: t.Any) -> bool:
        """True if there is probably a receiver for *sender*.

        Performs an optimistic check only.  Does not guarantee that all
        weakly referenced receivers are still alive.  See
        :meth:`receivers_for` for a stronger search.

        """
    def receivers_for(self, sender: t.Any) -> t.Generator[t.Callable[[t.Any], t.Any], None, None]:
        """Iterate all live receivers listening for *sender*."""
    def disconnect(self, receiver: t.Callable, sender: t.Any = ...) -> None:
        """Disconnect *receiver* from this signal's events.

        :param receiver: a previously :meth:`connected<connect>` callable

        :param sender: a specific sender to disconnect from, or :obj:`ANY`
          to disconnect from all senders.  Defaults to ``ANY``.

        """

receiver_connected: Incomplete

class NamedSignal(Signal):
    """A named generic notification emitter."""
    name: Incomplete
    def __init__(self, name: str, doc: str | None = None) -> None: ...

class Namespace(dict):
    """A mapping of signal names to signals."""
    def signal(self, name: str, doc: str | None = None) -> NamedSignal:
        """Return the :class:`NamedSignal` *name*, creating it if required.

        Repeated calls to this function will return the same signal object.

        """

class WeakNamespace(WeakValueDictionary):
    """A weak mapping of signal names to signals.

    Automatically cleans up unused Signals when the last reference goes out
    of scope.  This namespace implementation exists for a measure of legacy
    compatibility with Blinker <= 1.2, and may be dropped in the future.

    .. versionadded:: 1.3

    """
    def signal(self, name: str, doc: str | None = None) -> NamedSignal:
        """Return the :class:`NamedSignal` *name*, creating it if required.

        Repeated calls to this function will return the same signal object.

        """

signal: Incomplete
