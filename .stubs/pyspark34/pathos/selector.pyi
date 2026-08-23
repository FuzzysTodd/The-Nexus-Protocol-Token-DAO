from _typeshed import Incomplete
from pathos import logger as logger

class Selector:
    """
Selector object for watching and event notification.
    """
    def watch(self, timeout: Incomplete | None = None) -> None:
        """dispatch events to the registered hanlders"""
    def notifyOnReadReady(self, fd, handler) -> None:
        """add <handler> to the list of routines to call when <fd> is read ready"""
    def notifyOnWriteReady(self, fd, handler) -> None:
        """add <handler> to the list of routines to call when <fd> is write ready"""
    def notifyOnException(self, fd, handler) -> None:
        """add <handler> to the list of routines to call when <fd> raises an exception"""
    def notifyOnInterrupt(self, handler) -> None:
        """add <handler> to the list of routines to call when a signal arrives"""
    def notifyWhenIdle(self, handler) -> None:
        """add <handler> to the list of routines to call when a timeout occurs"""
    state: bool
    def __init__(self) -> None:
        """
Takes no initial input.
        """
