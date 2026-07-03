from . import Image as Image
from _typeshed import Incomplete

WIDTH: int

def puti16(fp, values) -> None:
    """Write network order (big-endian) 16-bit sequence"""

class FontFile:
    """Base class for raster font file handlers."""
    bitmap: Incomplete
    info: Incomplete
    glyph: Incomplete
    def __init__(self) -> None: ...
    def __getitem__(self, ix): ...
    ysize: Incomplete
    metrics: Incomplete
    def compile(self):
        """Create metrics and bitmap"""
    def save(self, filename) -> None:
        """Save font"""
