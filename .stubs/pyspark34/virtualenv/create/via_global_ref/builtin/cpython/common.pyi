from abc import ABCMeta
from virtualenv.create.describe import PosixSupports, WindowsSupports
from virtualenv.create.via_global_ref.builtin.via_global_self_do import ViaGlobalRefVirtualenvBuiltin

__all__ = ['CPython', 'CPythonPosix', 'CPythonWindows', 'is_mac_os_framework']

class CPython(ViaGlobalRefVirtualenvBuiltin, metaclass=ABCMeta):
    @classmethod
    def can_describe(cls, interpreter): ...
    @classmethod
    def exe_stem(cls): ...

class CPythonPosix(CPython, PosixSupports, metaclass=ABCMeta):
    """Create a CPython virtual environment on POSIX platforms."""

class CPythonWindows(CPython, WindowsSupports, metaclass=ABCMeta):
    @classmethod
    def host_python(cls, interpreter): ...

def is_mac_os_framework(interpreter): ...
