from _typeshed import Incomplete

__all__ = ['ReentrancyError', 'ReentrancyLock', 'non_reentrant']

class ReentrancyError(RuntimeError): ...

class ReentrancyLock:
    """
    Threading lock that raises an exception for reentrant calls.

    Calls from different threads are serialized, and nested calls from the
    same thread result to an error.

    The object can be used as a context manager or to decorate functions
    via the decorate() method.

    """
    def __init__(self, err_msg) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def decorate(self, func): ...

def non_reentrant(err_msg: Incomplete | None = None):
    """
    Decorate a function with a threading lock and prevent reentrant calls.
    """
