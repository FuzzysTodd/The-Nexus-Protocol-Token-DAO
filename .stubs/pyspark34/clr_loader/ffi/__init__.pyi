from _typeshed import Incomplete
from pathlib import Path

__all__ = ['ffi', 'load_hostfxr', 'load_mono', 'load_netfx']

ffi: Incomplete

def load_hostfxr(dotnet_root: Path): ...
def load_mono(path: Path | None = None): ...
def load_netfx(): ...
