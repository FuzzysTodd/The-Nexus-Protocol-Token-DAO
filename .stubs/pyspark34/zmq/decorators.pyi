from _typeshed import Incomplete

__all__ = ['context', 'socket']

class _Decorator:
    """The mini decorator factory"""
    def __init__(self, target: Incomplete | None = None) -> None: ...
    def __call__(self, *dec_args, **dec_kwargs):
        """
        The main logic of decorator

        Here is how those arguments works::

            @out_decorator(*dec_args, *dec_kwargs)
            def func(*wrap_args, **wrap_kwargs):
                ...

        And in the ``wrapper``, we simply create ``self.target`` instance via
        ``with``::

            target = self.get_target(*args, **kwargs)
            with target(*dec_args, **dec_kwargs) as obj:
                ...

        """
    def get_target(self, *args, **kwargs):
        """Return the target function

        Allows modifying args/kwargs to be passed.
        """
    def process_decorator_args(self, *args, **kwargs):
        """Process args passed to the decorator.

        args not consumed by the decorator will be passed to the target factory
        (Context/Socket constructor).
        """

class _ContextDecorator(_Decorator):
    """Decorator subclass for Contexts"""
    def __init__(self) -> None: ...

class _SocketDecorator(_Decorator):
    """Decorator subclass for sockets

    Gets the context from other args.
    """
    context_name: Incomplete
    def process_decorator_args(self, *args, **kwargs):
        """Also grab context_name out of kwargs"""
    def get_target(self, *args, **kwargs):
        """Get context, based on call-time args"""

def context(*args, **kwargs):
    """Decorator for adding a Context to a function.

    Usage::

        @context()
        def foo(ctx):
            ...

    .. versionadded:: 15.3

    :param str name: the keyword argument passed to decorated function
    """
def socket(*args, **kwargs):
    """Decorator for adding a socket to a function.

    Usage::

        @socket(zmq.PUSH)
        def foo(push):
            ...

    .. versionadded:: 15.3

    :param str name: the keyword argument passed to decorated function
    :param str context_name: the keyword only argument to identify context
                             object
    """
