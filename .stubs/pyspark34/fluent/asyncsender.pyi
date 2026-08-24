from _typeshed import Incomplete
from fluent import sender
from fluent.sender import EventTime as EventTime

__all__ = ['EventTime', 'FluentSender']

class FluentSender(sender.FluentSender):
    def __init__(self, tag, host: str = 'localhost', port: int = 24224, bufmax=..., timeout: float = 3.0, verbose: bool = False, buffer_overflow_handler: Incomplete | None = None, nanosecond_precision: bool = False, msgpack_kwargs: Incomplete | None = None, queue_maxsize=..., queue_circular=..., queue_overflow_handler: Incomplete | None = None, **kwargs) -> None:
        """
        :param kwargs: This kwargs argument is not used in __init__. This will be removed in the next major version.
        """
    def close(self, flush: bool = True) -> None: ...
    @property
    def queue_maxsize(self): ...
    @property
    def queue_blocking(self): ...
    @property
    def queue_circular(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
