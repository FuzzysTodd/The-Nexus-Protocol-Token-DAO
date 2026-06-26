import io
from _typeshed import Incomplete

long = int
file = io.IOBase

def str_(byte): ...
def b_(string): ...

copyright: str
parent: Incomplete
__version__: Incomplete

def start_thread(name, target, args=(), kwargs={}, daemon: bool = True):
    """Starts a thread"""
def get_class_hierarchy(clazz): ...
def is_not_imported(arg, modules): ...

class portnumber:
    """port selector

Usage:
    >>> pick = portnumber(min=1024,max=65535)
    >>> print( pick() )
    """
    min: Incomplete
    max: Incomplete
    first: int
    current: int
    def __init__(self, min: int = 0, max=...) -> None:
        """select a port number from a given range.

The first call will return a random number from the available range,
and each subsequent call will return the next number in the range.

Inputs:
    min -- minimum port number  [default = 0]
    max -- maximum port number  [default = 65536]
        """
    def __call__(self): ...

def randomport(min: int = 1024, max: int = 65536):
    """select a random port number

Inputs:
    min -- minimum port number  [default = 1024]
    max -- maximum port number  [default = 65536]
    """
