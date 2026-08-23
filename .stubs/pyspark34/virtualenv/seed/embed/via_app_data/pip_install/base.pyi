from _typeshed import Incomplete
from abc import ABCMeta
from distlib.scripts import ScriptMaker

__all__ = ['PipInstall']

class PipInstall(metaclass=ABCMeta):
    def __init__(self, wheel, creator, image_folder) -> None: ...
    def install(self, version_info) -> None: ...
    def build_image(self) -> None: ...
    def clear(self) -> None: ...
    def has_image(self): ...

class ScriptMakerCustom(ScriptMaker):
    clobber: bool
    set_mode: bool
    executable: Incomplete
    version_info: Incomplete
    variants: Incomplete
    def __init__(self, target_dir, version_info, executable, name) -> None: ...
