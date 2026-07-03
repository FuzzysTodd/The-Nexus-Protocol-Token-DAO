from . import Image as Image, ImageFile as ImageFile
from ._deprecate import deprecate as deprecate
from _typeshed import Incomplete

split: Incomplete
field: Incomplete
gs_windows_binary: Incomplete

def has_ghostscript(): ...
def Ghostscript(tile, size, fp, scale: int = 1, transparency: bool = False):
    """Render an image using Ghostscript"""

class PSFile:
    """
    Wrapper for bytesio object that treats either CR or LF as end of line.
    This class is no longer used internally, but kept for backwards compatibility.
    """
    fp: Incomplete
    char: Incomplete
    def __init__(self, fp) -> None: ...
    def seek(self, offset, whence=...) -> None: ...
    def readline(self): ...

class EpsImageFile(ImageFile.ImageFile):
    """EPS File Parser for the Python Imaging Library"""
    format: str
    format_description: str
    mode_map: Incomplete
    im: Incomplete
    mode: Incomplete
    tile: Incomplete
    def load(self, scale: int = 1, transparency: bool = False): ...
    def load_seek(self, *args, **kwargs) -> None: ...
