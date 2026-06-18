import typing as t
from .wsgi import ClosingIterator as ClosingIterator
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment
from contextvars import ContextVar

T = t.TypeVar('T')
F = t.TypeVar('F', bound=t.Callable[..., t.Any])

def release_local(local: Local | LocalStack) -> None:
    """Release the data for the current context in a :class:`Local` or
    :class:`LocalStack` without using a :class:`LocalManager`.

    This should not be needed for modern use cases, and may be removed
    in the future.

    .. versionadded:: 0.6.1
    """

class Local:
    """Create a namespace of context-local data. This wraps a
    :class:`ContextVar` containing a :class:`dict` value.

    This may incur a performance penalty compared to using individual
    context vars, as it has to copy data to avoid mutating the dict
    between nested contexts.

    :param context_var: The :class:`~contextvars.ContextVar` to use as
        storage for this local. If not given, one will be created.
        Context vars not created at the global scope may interfere with
        garbage collection.

    .. versionchanged:: 2.0
        Uses ``ContextVar`` instead of a custom storage implementation.
    """
    def __init__(self, context_var: ContextVar[dict[str, t.Any]] | None = None) -> None: ...
    def __iter__(self) -> t.Iterator[tuple[str, t.Any]]: ...
    def __call__(self, name: str, *, unbound_message: str | None = None) -> LocalProxy:
        """Create a :class:`LocalProxy` that access an attribute on this
        local namespace.

        :param name: Proxy this attribute.
        :param unbound_message: The error message that the proxy will
            show if the attribute isn't set.
        """
    def __release_local__(self) -> None: ...
    def __getattr__(self, name: str) -> t.Any: ...
    def __setattr__(self, name: str, value: t.Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

class LocalStack(t.Generic[T]):
    """Create a stack of context-local data. This wraps a
    :class:`ContextVar` containing a :class:`list` value.

    This may incur a performance penalty compared to using individual
    context vars, as it has to copy data to avoid mutating the list
    between nested contexts.

    :param context_var: The :class:`~contextvars.ContextVar` to use as
        storage for this local. If not given, one will be created.
        Context vars not created at the global scope may interfere with
        garbage collection.

    .. versionchanged:: 2.0
        Uses ``ContextVar`` instead of a custom storage implementation.

    .. versionadded:: 0.6.1
    """
    def __init__(self, context_var: ContextVar[list[T]] | None = None) -> None: ...
    def __release_local__(self) -> None: ...
    def push(self, obj: T) -> list[T]:
        """Add a new item to the top of the stack."""
    def pop(self) -> T | None:
        """Remove the top item from the stack and return it. If the
        stack is empty, return ``None``.
        """
    @property
    def top(self) -> T | None:
        """The topmost item on the stack.  If the stack is empty,
        `None` is returned.
        """
    def __call__(self, name: str | None = None, *, unbound_message: str | None = None) -> LocalProxy:
        """Create a :class:`LocalProxy` that accesses the top of this
        local stack.

        :param name: If given, the proxy access this attribute of the
            top item, rather than the item itself.
        :param unbound_message: The error message that the proxy will
            show if the stack is empty.
        """

class LocalManager:
    """Manage releasing the data for the current context in one or more
    :class:`Local` and :class:`LocalStack` objects.

    This should not be needed for modern use cases, and may be removed
    in the future.

    :param locals: A local or list of locals to manage.

    .. versionchanged:: 2.1
        The ``ident_func`` was removed.

    .. versionchanged:: 0.7
        The ``ident_func`` parameter was added.

    .. versionchanged:: 0.6.1
        The :func:`release_local` function can be used instead of a
        manager.
    """
    locals: Incomplete
    def __init__(self, locals: None | Local | LocalStack | t.Iterable[Local | LocalStack] = None) -> None: ...
    def cleanup(self) -> None:
        """Release the data in the locals for this context. Call this at
        the end of each request or use :meth:`make_middleware`.
        """
    def make_middleware(self, app: WSGIApplication) -> WSGIApplication:
        """Wrap a WSGI application so that local data is released
        automatically after the response has been sent for a request.
        """
    def middleware(self, func: WSGIApplication) -> WSGIApplication:
        """Like :meth:`make_middleware` but used as a decorator on the
        WSGI application function.

        .. code-block:: python

            @manager.middleware
            def application(environ, start_response):
                ...
        """

class _ProxyLookup:
    """Descriptor that handles proxied attribute lookup for
    :class:`LocalProxy`.

    :param f: The built-in function this attribute is accessed through.
        Instead of looking up the special method, the function call
        is redone on the object.
    :param fallback: Return this function if the proxy is unbound
        instead of raising a :exc:`RuntimeError`.
    :param is_attr: This proxied name is an attribute, not a function.
        Call the fallback immediately to get the value.
    :param class_value: Value to return when accessed from the
        ``LocalProxy`` class directly. Used for ``__doc__`` so building
        docs still works.
    """
    bind_f: Incomplete
    fallback: Incomplete
    class_value: Incomplete
    is_attr: Incomplete
    def __init__(self, f: t.Callable | None = None, fallback: t.Callable | None = None, class_value: t.Any | None = None, is_attr: bool = False) -> None: ...
    name: Incomplete
    def __set_name__(self, owner: LocalProxy, name: str) -> None: ...
    def __get__(self, instance: LocalProxy, owner: type | None = None) -> t.Any: ...
    def __call__(self, instance: LocalProxy, *args: t.Any, **kwargs: t.Any) -> t.Any:
        """Support calling unbound methods from the class. For example,
        this happens with ``copy.copy``, which does
        ``type(x).__copy__(x)``. ``type(x)`` can't be proxied, so it
        returns the proxy type and descriptor.
        """

class _ProxyIOp(_ProxyLookup):
    """Look up an augmented assignment method on a proxied object. The
    method is wrapped to return the proxy instead of the object.
    """
    bind_f: Incomplete
    def __init__(self, f: t.Callable | None = None, fallback: t.Callable | None = None) -> None: ...

class LocalProxy(t.Generic[T]):
    '''A proxy to the object bound to a context-local object. All
    operations on the proxy are forwarded to the bound object. If no
    object is bound, a ``RuntimeError`` is raised.

    :param local: The context-local object that provides the proxied
        object.
    :param name: Proxy this attribute from the proxied object.
    :param unbound_message: The error message to show if the
        context-local object is unbound.

    Proxy a :class:`~contextvars.ContextVar` to make it easier to
    access. Pass a name to proxy that attribute.

    .. code-block:: python

        _request_var = ContextVar("request")
        request = LocalProxy(_request_var)
        session = LocalProxy(_request_var, "session")

    Proxy an attribute on a :class:`Local` namespace by calling the
    local with the attribute name:

    .. code-block:: python

        data = Local()
        user = data("user")

    Proxy the top item on a :class:`LocalStack` by calling the local.
    Pass a name to proxy that attribute.

    .. code-block::

        app_stack = LocalStack()
        current_app = app_stack()
        g = app_stack("g")

    Pass a function to proxy the return value from that function. This
    was previously used to access attributes of local objects before
    that was supported directly.

    .. code-block:: python

        session = LocalProxy(lambda: request.session)

    ``__repr__`` and ``__class__`` are proxied, so ``repr(x)`` and
    ``isinstance(x, cls)`` will look like the proxied object. Use
    ``issubclass(type(x), LocalProxy)`` to check if an object is a
    proxy.

    .. code-block:: python

        repr(user)  # <User admin>
        isinstance(user, User)  # True
        issubclass(type(user), LocalProxy)  # True

    .. versionchanged:: 2.2.2
        ``__wrapped__`` is set when wrapping an object, not only when
        wrapping a function, to prevent doctest from failing.

    .. versionchanged:: 2.2
        Can proxy a ``ContextVar`` or ``LocalStack`` directly.

    .. versionchanged:: 2.2
        The ``name`` parameter can be used with any proxied object, not
        only ``Local``.

    .. versionchanged:: 2.2
        Added the ``unbound_message`` parameter.

    .. versionchanged:: 2.0
        Updated proxied attributes and methods to reflect the current
        data model.

    .. versionchanged:: 0.6.1
        The class can be instantiated with a callable.
    '''
    def __init__(self, local: ContextVar[T] | Local | LocalStack[T] | t.Callable[[], T], name: str | None = None, *, unbound_message: str | None = None) -> None: ...
    __doc__: Incomplete
    __wrapped__: Incomplete
    __bytes__: Incomplete
    __format__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    __eq__: Incomplete
    __ne__: Incomplete
    __gt__: Incomplete
    __ge__: Incomplete
    __hash__: Incomplete
    __bool__: Incomplete
    __getattr__: Incomplete
    __setattr__: Incomplete
    __delattr__: Incomplete
    __dir__: Incomplete
    __class__: Incomplete
    __instancecheck__: Incomplete
    __subclasscheck__: Incomplete
    __call__: Incomplete
    __len__: Incomplete
    __length_hint__: Incomplete
    __getitem__: Incomplete
    __setitem__: Incomplete
    __delitem__: Incomplete
    __iter__: Incomplete
    __next__: Incomplete
    __reversed__: Incomplete
    __contains__: Incomplete
    __add__: Incomplete
    __sub__: Incomplete
    __mul__: Incomplete
    __matmul__: Incomplete
    __truediv__: Incomplete
    __floordiv__: Incomplete
    __mod__: Incomplete
    __divmod__: Incomplete
    __pow__: Incomplete
    __lshift__: Incomplete
    __rshift__: Incomplete
    __and__: Incomplete
    __xor__: Incomplete
    __or__: Incomplete
    __radd__: Incomplete
    __rsub__: Incomplete
    __rmul__: Incomplete
    __rmatmul__: Incomplete
    __rtruediv__: Incomplete
    __rfloordiv__: Incomplete
    __rmod__: Incomplete
    __rdivmod__: Incomplete
    __rpow__: Incomplete
    __rlshift__: Incomplete
    __rrshift__: Incomplete
    __rand__: Incomplete
    __rxor__: Incomplete
    __ror__: Incomplete
    __iadd__: Incomplete
    __isub__: Incomplete
    __imul__: Incomplete
    __imatmul__: Incomplete
    __itruediv__: Incomplete
    __ifloordiv__: Incomplete
    __imod__: Incomplete
    __ipow__: Incomplete
    __ilshift__: Incomplete
    __irshift__: Incomplete
    __iand__: Incomplete
    __ixor__: Incomplete
    __ior__: Incomplete
    __neg__: Incomplete
    __pos__: Incomplete
    __abs__: Incomplete
    __invert__: Incomplete
    __complex__: Incomplete
    __int__: Incomplete
    __float__: Incomplete
    __index__: Incomplete
    __round__: Incomplete
    __trunc__: Incomplete
    __floor__: Incomplete
    __ceil__: Incomplete
    __enter__: Incomplete
    __exit__: Incomplete
    __await__: Incomplete
    __aiter__: Incomplete
    __anext__: Incomplete
    __aenter__: Incomplete
    __aexit__: Incomplete
    __copy__: Incomplete
    __deepcopy__: Incomplete
