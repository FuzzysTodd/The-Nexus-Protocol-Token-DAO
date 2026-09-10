from .attrsettr import AttributeSetter, OptValT
from typing import Any, Callable, Dict, Generic, List, TypeVar, overload
from zmq.backend import Context as ContextBase

__all__ = ['Context']

T = TypeVar('T', bound='Context')
ST = TypeVar('ST', bound='Socket', covariant=True)

class Context(ContextBase, AttributeSetter, Generic[ST]):
    """Create a zmq Context

    A zmq Context creates sockets via its ``ctx.socket`` method.

    .. versionchanged:: 24

        When using a Context as a context manager (``with zmq.Context()``),
        or deleting a context without closing it first,
        ``ctx.destroy()`` is called,
        closing any leftover sockets,
        instead of `ctx.term()` which requires sockets to be closed first.

        This prevents hangs caused by `ctx.term()` if sockets are left open,
        but means that unclean destruction of contexts
        (with sockets left open) is not safe
        if sockets are managed in other threads.

    .. versionadded:: 25

        Contexts can now be shadowed by passing another Context.
        This helps in creating an async copy of a sync context or vice versa::

            ctx = zmq.Context(async_ctx)

        Which previously had to be::

            ctx = zmq.Context.shadow(async_ctx.underlying)
    """
    sockopts: Dict[int, Any]
    @overload
    def __init__(self, io_threads: int = 1) -> None: ...
    @overload
    def __init__(self, io_threads: Context) -> None: ...
    @overload
    def __init__(self, *, shadow: Context | int) -> None: ...
    def __del__(self) -> None:
        """Deleting a Context without closing it destroys it and all sockets.

        .. versionchanged:: 24
            Switch from threadsafe `term()` which hangs in the event of open sockets
            to less safe `destroy()` which
            warns about any leftover sockets and closes them.
        """
    def __enter__(self) -> T: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def __copy__(self, memo: Any = None) -> T:
        """Copying a Context creates a shadow copy"""
    __deepcopy__ = __copy__
    @classmethod
    def shadow(cls, address: int | Context) -> T:
        """Shadow an existing libzmq context

        address is a zmq.Context or an integer (or FFI pointer)
        representing the address of the libzmq context.

        .. versionadded:: 14.1

        .. versionadded:: 25
            Support for shadowing `zmq.Context` objects,
            instead of just integer addresses.
        """
    @classmethod
    def shadow_pyczmq(cls, ctx: Any) -> T:
        """Shadow an existing pyczmq context

        ctx is the FFI `zctx_t *` pointer

        .. versionadded:: 14.1
        """
    @classmethod
    def instance(cls, io_threads: int = 1) -> T:
        """Returns a global Context instance.

        Most single-threaded applications have a single, global Context.
        Use this method instead of passing around Context instances
        throughout your code.

        A common pattern for classes that depend on Contexts is to use
        a default argument to enable programs with multiple Contexts
        but not require the argument for simpler applications::

            class MyClass(object):
                def __init__(self, context=None):
                    self.context = context or Context.instance()

        .. versionchanged:: 18.1

            When called in a subprocess after forking,
            a new global instance is created instead of inheriting
            a Context that won't work from the parent process.
        """
    def term(self) -> None:
        """Close or terminate the context.

        Context termination is performed in the following steps:

        - Any blocking operations currently in progress on sockets open within context shall
          raise :class:`zmq.ContextTerminated`.
          With the exception of socket.close(), any further operations on sockets open within this context
          shall raise :class:`zmq.ContextTerminated`.
        - After interrupting all blocking calls, term shall block until the following conditions are satisfied:
            - All sockets open within context have been closed.
            - For each socket within context, all messages sent on the socket have either been
              physically transferred to a network peer,
              or the socket's linger period set with the zmq.LINGER socket option has expired.

        For further details regarding socket linger behaviour refer to libzmq documentation for ZMQ_LINGER.

        This can be called to close the context by hand. If this is not called,
        the context will automatically be closed when it is garbage collected,
        in which case you may see a ResourceWarning about the unclosed context.
        """
    def __dir__(self) -> List[str]: ...
    def destroy(self, linger: int | None = None) -> None:
        """Close all sockets associated with this context and then terminate
        the context.

        .. warning::

            destroy involves calling ``zmq_close()``, which is **NOT** threadsafe.
            If there are active sockets in other threads, this must not be called.

        Parameters
        ----------

        linger : int, optional
            If specified, set LINGER on sockets prior to closing them.
        """
    def socket(self, socket_type: int, socket_class: Callable[[T, int], ST] | None = None, **kwargs: Any) -> ST:
        """Create a Socket associated with this Context.

        Parameters
        ----------
        socket_type : int
            The socket type, which can be any of the 0MQ socket types:
            REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, etc.

        socket_class: zmq.Socket or a subclass
            The socket class to instantiate, if different from the default for this Context.
            e.g. for creating an asyncio socket attached to a default Context or vice versa.

            .. versionadded:: 25

        kwargs:
            will be passed to the __init__ method of the socket class.
        """
    def setsockopt(self, opt: int, value: Any) -> None:
        """set default socket options for new sockets created by this Context

        .. versionadded:: 13.0
        """
    def getsockopt(self, opt: int) -> OptValT:
        """get default socket options for new sockets created by this Context

        .. versionadded:: 13.0
        """
    def __delattr__(self, key: str) -> None:
        """delete default sockopts as attributes"""
