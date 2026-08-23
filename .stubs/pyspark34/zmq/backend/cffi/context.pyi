from _typeshed import Incomplete

__all__ = ['Context']

class Context:
    def __init__(self, io_threads: int = 1, shadow: Incomplete | None = None) -> None: ...
    @property
    def underlying(self):
        """The address of the underlying libzmq context"""
    @property
    def closed(self): ...
    def set(self, option, value) -> None:
        """set a context option

        see zmq_ctx_set
        """
    def get(self, option):
        """get context option

        see zmq_ctx_get
        """
    def term(self) -> None: ...
