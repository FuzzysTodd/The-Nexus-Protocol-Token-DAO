from typing import Type

__all__ = ['WebSocket']

class WebSocket:
    """
    A WebSocket connection.

    Call :meth:`connect` before :meth:`send` and :meth:`receive`.

    All methods are thread safe.

    Parameters
    ----------
    url
        The WebSocket URL.
        For tuner command channel it should be something like ``ws://localhost:8080/tuner``.
    """
    ConnectionClosed: Type[Exception]
    def __init__(self, url: str) -> None: ...
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...
    def send(self, message: str) -> None: ...
    def receive(self) -> str | None:
        """
        Return received message;
        or return ``None`` if the connection has been closed by peer.
        """
