from _typeshed import Incomplete
from threading import Thread
from typing import NamedTuple

class gcref(NamedTuple):
    obj: Incomplete
    event: Incomplete

class GarbageCollectorThread(Thread):
    """Thread in which garbage collection actually happens."""
    gc: Incomplete
    daemon: bool
    pid: Incomplete
    ready: Incomplete
    def __init__(self, gc) -> None: ...
    def run(self) -> None: ...

class GarbageCollector:
    """PyZMQ Garbage Collector

    Used for representing the reference held by libzmq during zero-copy sends.
    This object holds a dictionary, keyed by Python id,
    of the Python objects whose memory are currently in use by zeromq.

    When zeromq is done with the memory, it sends a message on an inproc PUSH socket
    containing the packed size_t (32 or 64-bit unsigned int),
    which is the key in the dict.
    When the PULL socket in the gc thread receives that message,
    the reference is popped from the dict,
    and any tracker events that should be signaled fire.
    """
    refs: Incomplete
    url: str
    pid: Incomplete
    thread: Incomplete
    def __init__(self, context: Incomplete | None = None) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, ctx) -> None: ...
    def stop(self) -> None:
        """stop the garbage-collection thread"""
    def start(self) -> None:
        """Start a new garbage collection thread.

        Creates a new zmq Context used for garbage collection.
        Under most circumstances, this will only be called once per process.
        """
    def is_alive(self):
        """Is the garbage collection thread currently running?

        Includes checks for process shutdown or fork.
        """
    def store(self, obj, event: Incomplete | None = None):
        """store an object and (optionally) event for zero-copy"""
    def __del__(self) -> None: ...

gc: Incomplete
