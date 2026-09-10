import importlib.abc
import types
from .importstring import import_item as import_item
from _typeshed import Incomplete

class ShimWarning(Warning):
    """A warning to show when a module has moved, and a shim is in its place."""

class ShimImporter(importlib.abc.MetaPathFinder):
    """Import hook for a shim.

    This ensures that submodule imports return the real target module,
    not a clone that will confuse `is` and `isinstance` checks.
    """
    src: Incomplete
    mirror: Incomplete
    def __init__(self, src, mirror) -> None: ...
    def find_spec(self, fullname, path, target: Incomplete | None = None): ...

class ShimModule(types.ModuleType):
    def __init__(self, *args, **kwargs) -> None: ...
    def __dir__(self): ...
    def __getattr__(self, key): ...
