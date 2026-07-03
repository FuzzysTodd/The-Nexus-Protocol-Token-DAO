import queue
from _typeshed import Incomplete
from threading import Thread

version_info: Incomplete

def items(d): ...
def iteritems(d): ...
def next(x): ...
range = xrange
long = long
basestring = basestring
unicode = unicode
bytearray2 = bytearray
unichr = unichr
bytestr = str
tobytestr = str

def isbytestr(s): ...
def ispython3bytestr(s): ...
def isbytearray(s): ...
def bytetoint(b): ...
def bytetostr(b): ...
def strtobyte(b): ...

Empty: Incomplete
next = next
range = range
long = int
basestring = str
unicode = str
bytearray2 = bytes
unichr = chr
bytestr = bytes
Queue = queue.Queue
Empty = queue.Empty

def hasattr2(obj, attr): ...
hasattr2 = hasattr

class CompatThread(Thread):
    """Compatibility Thread class.

    Allows Python 2 Thread class to accept daemon kwarg in init.
    """
    daemon: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
