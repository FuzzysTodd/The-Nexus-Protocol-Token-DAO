from .. import exc as exc, util as util
from ..util._has_cy import HAS_CYEXTENSION as HAS_CYEXTENSION
from ..util.typing import Protocol as Protocol
from typing import Any, Callable

def connection_memoize(key: str) -> Callable[[_C], _C]:
    """Decorator, memoize a function in a connection.info stash.

    Only applicable to functions which take no arguments other than a
    connection.  The memo will be stored in ``connection.info[key]``.
    """

class _TConsSubject(Protocol): ...

class TransactionalContext:
    """Apply Python context manager behavior to transaction objects.

    Performs validation to ensure the subject of the transaction is not
    used if the transaction were ended prematurely.

    """
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> TransactionalContext: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
