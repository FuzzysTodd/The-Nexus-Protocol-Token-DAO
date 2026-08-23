import abc
from _typeshed import Incomplete
from collections.abc import Generator
from virtualenv.create.via_global_ref.builtin.via_global_self_do import ViaGlobalRefVirtualenvBuiltin

__all__ = ['PyPy']

class PyPy(ViaGlobalRefVirtualenvBuiltin, metaclass=abc.ABCMeta):
    @classmethod
    def can_describe(cls, interpreter): ...
    @classmethod
    def executables(cls, interpreter) -> Generator[Incomplete, Incomplete, None]: ...
    @classmethod
    def exe_names(cls, interpreter): ...
    @classmethod
    def sources(cls, interpreter) -> Generator[Incomplete, Incomplete, Incomplete]: ...
