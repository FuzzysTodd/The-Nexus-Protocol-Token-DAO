import abc
from .common import CPython, CPythonPosix, CPythonWindows
from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.create.describe import Python3Supports

__all__ = ['CPython3', 'CPython3Posix', 'CPython3Windows']

class CPython3(CPython, Python3Supports, metaclass=abc.ABCMeta):
    """CPython 3 or later."""

class CPython3Posix(CPythonPosix, CPython3):
    @classmethod
    def can_describe(cls, interpreter): ...
    def env_patch_text(self): ...
    @classmethod
    def pyvenv_launch_patch_active(cls, interpreter): ...

class CPython3Windows(CPythonWindows, CPython3):
    """CPython 3 on Windows."""
    @classmethod
    def setup_meta(cls, interpreter): ...
    @classmethod
    def sources(cls, interpreter) -> Generator[Incomplete, Incomplete, None]: ...
    @classmethod
    def executables(cls, interpreter): ...
    @classmethod
    def has_shim(cls, interpreter): ...
    @classmethod
    def shim(cls, interpreter): ...
    @classmethod
    def host_python(cls, interpreter): ...
    @classmethod
    def dll_and_pyd(cls, interpreter) -> Generator[Incomplete, None, None]: ...
    @classmethod
    def python_zip(cls, interpreter) -> Generator[Incomplete, None, None]:
        '''
        "python{VERSION}.zip" contains compiled *.pyc std lib packages, where
        "VERSION" is `py_version_nodot` var from the `sysconfig` module.
        :see: https://docs.python.org/3/using/windows.html#the-embeddable-package
        :see: `discovery.py_info.PythonInfo` class (interpreter).
        :see: `python -m sysconfig` output.

        :note: The embeddable Python distribution for Windows includes
        "python{VERSION}.zip" and "python{VERSION}._pth" files. User can
        move/rename *zip* file and edit `sys.path` by editing *_pth* file.
        Here the `pattern` is used only for the default *zip* file name!
        '''
