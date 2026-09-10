from _typeshed import Incomplete
from abc import ABCMeta

__all__ = ['Describe', 'Python3Supports', 'PosixSupports', 'WindowsSupports']

class Describe(metaclass=ABCMeta):
    """Given a host interpreter tell us information about what the created interpreter might look like."""
    suffix: Incomplete
    interpreter: Incomplete
    dest: Incomplete
    def __init__(self, dest, interpreter) -> None: ...
    @property
    def bin_dir(self): ...
    @property
    def script_dir(self): ...
    @property
    def purelib(self): ...
    @property
    def platlib(self): ...
    @property
    def libs(self): ...
    @property
    def stdlib(self): ...
    @property
    def stdlib_platform(self): ...
    @classmethod
    def can_describe(cls, interpreter):
        """Knows means it knows how the output will look."""
    @property
    def env_name(self): ...
    @property
    def exe(self): ...
    @classmethod
    def exe_stem(cls) -> None:
        """Executable name without suffix - there seems to be no standard way to get this without creating it."""
    def script(self, name): ...

class Python3Supports(Describe, metaclass=ABCMeta):
    @classmethod
    def can_describe(cls, interpreter): ...

class PosixSupports(Describe, metaclass=ABCMeta):
    @classmethod
    def can_describe(cls, interpreter): ...

class WindowsSupports(Describe, metaclass=ABCMeta):
    @classmethod
    def can_describe(cls, interpreter): ...
