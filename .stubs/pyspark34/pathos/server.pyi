from _typeshed import Incomplete

__all__ = ['Server']

class Server:
    """
Server base class for pathos servers for parallel and distributed computing.
    """
    def selector(self):
        """get the selector"""
    def deactivate(self) -> None:
        """turn off the selector"""
    def activate(self, onTimeout: Incomplete | None = None, selector: Incomplete | None = None) -> None:
        """configure the selector and install the timeout callback"""
    def serve(self, timeout) -> None:
        """begin serving, and set the timeout"""
    def __init__(self) -> None:
        """
Takes no initial input.
        """
