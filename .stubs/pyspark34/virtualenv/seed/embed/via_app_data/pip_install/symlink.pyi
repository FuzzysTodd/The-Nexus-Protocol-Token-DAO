from .base import PipInstall

__all__ = ['SymlinkPipInstall']

class SymlinkPipInstall(PipInstall):
    def build_image(self) -> None: ...
    def clear(self) -> None: ...
