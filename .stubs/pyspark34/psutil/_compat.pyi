from _typeshed import Incomplete
from contextlib import redirect_stderr as redirect_stderr
from functools import lru_cache as lru_cache
from shutil import get_terminal_size as get_terminal_size, which as which
from typing import NamedTuple

__all__ = ['PY3', 'long', 'range', 'super', 'unicode', 'basestring', 'u', 'b', 'lru_cache', 'which', 'get_terminal_size', 'redirect_stderr', 'FileNotFoundError', 'PermissionError', 'ProcessLookupError', 'InterruptedError', 'ChildProcessError', 'FileExistsError']

PY3: Incomplete
long = int
xrange = range
unicode = str
basestring = str
range = range

def u(s): ...
def b(s): ...
super = super
FileNotFoundError = FileNotFoundError
PermissionError = PermissionError
ProcessLookupError = ProcessLookupError
InterruptedError = InterruptedError
ChildProcessError = ChildProcessError
FileExistsError = FileExistsError

class _CacheInfo(NamedTuple):
    hits: Incomplete
    misses: Incomplete
    maxsize: Incomplete
    currsize: Incomplete

class _HashedSeq(list):
    hashvalue: Incomplete
    def __init__(self, tup, hash=...) -> None: ...
    def __hash__(self): ...

class SubprocessTimeoutExpired(Exception): ...
