import abc
from .common import PyPy
from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.create.describe import PosixSupports, Python3Supports, WindowsSupports

__all__ = ['PyPy3', 'PyPy3Posix', 'Pypy3Windows']

class PyPy3(PyPy, Python3Supports, metaclass=abc.ABCMeta):
    @classmethod
    def exe_stem(cls): ...
    @classmethod
    def exe_names(cls, interpreter): ...

class PyPy3Posix(PyPy3, PosixSupports):
    """PyPy 3 on POSIX."""
    def to_lib(self, src): ...
    @classmethod
    def sources(cls, interpreter) -> Generator[Incomplete, Incomplete, None]: ...

class Pypy3Windows(PyPy3, WindowsSupports):
    """PyPy 3 on Windows."""
    @property
    def less_v37(self): ...
