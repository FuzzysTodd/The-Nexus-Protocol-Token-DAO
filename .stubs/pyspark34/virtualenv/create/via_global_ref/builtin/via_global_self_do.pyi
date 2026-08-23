from .builtin_way import VirtualenvBuiltin
from _typeshed import Incomplete
from abc import ABCMeta
from collections.abc import Generator
from virtualenv.create.via_global_ref.api import ViaGlobalRefApi, ViaGlobalRefMeta

__all__ = ['BuiltinViaGlobalRefMeta', 'ViaGlobalRefVirtualenvBuiltin']

class BuiltinViaGlobalRefMeta(ViaGlobalRefMeta):
    sources: Incomplete
    def __init__(self) -> None: ...

class ViaGlobalRefVirtualenvBuiltin(ViaGlobalRefApi, VirtualenvBuiltin, metaclass=ABCMeta):
    def __init__(self, options, interpreter) -> None: ...
    @classmethod
    def can_create(cls, interpreter):
        """By default, all built-in methods assume that if we can describe it we can create it."""
    @classmethod
    def setup_meta(cls, interpreter): ...
    @classmethod
    def sources(cls, interpreter) -> Generator[Incomplete, None, None]: ...
    def to_bin(self, src): ...
    enable_system_site_package: bool
    def create(self) -> None: ...
    def ensure_directories(self): ...
    def set_pyenv_cfg(self) -> None:
        """
        We directly inject the base prefix and base exec prefix to avoid site.py needing to discover these
        from home (which usually is done within the interpreter itself).
        """
