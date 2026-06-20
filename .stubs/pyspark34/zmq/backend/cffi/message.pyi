from __pypy__.bufferable import bufferable as maybe_bufferable
from _typeshed import Incomplete

__all__ = ['Frame', 'Message']

maybe_bufferable = object

class Frame(maybe_bufferable):
    tracker: Incomplete
    closed: bool
    more: bool
    tracker_event: Incomplete
    zmq_msg: Incomplete
    def __init__(self, data: Incomplete | None = None, track: bool = False, copy: Incomplete | None = None, copy_threshold: Incomplete | None = None) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    @property
    def buffer(self): ...
    @property
    def bytes(self): ...
    def __len__(self) -> int: ...
    def __eq__(self, other): ...
    @property
    def done(self): ...
    def __buffer__(self, flags): ...
    def __copy__(self):
        """Create a shallow copy of the message.

        This does not copy the contents of the Frame, just the pointer.
        This will increment the 0MQ ref count of the message, but not
        the ref count of the Python object. That is only done once when
        the Python is first turned into a 0MQ message.
        """
    def fast_copy(self):
        """Fast shallow copy of the Frame.

        Does not copy underlying data.
        """
Message = Frame
