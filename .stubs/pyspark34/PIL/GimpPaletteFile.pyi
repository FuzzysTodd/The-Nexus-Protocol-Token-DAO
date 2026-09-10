from ._binary import o8 as o8
from _typeshed import Incomplete

class GimpPaletteFile:
    """File handler for GIMP's palette format."""
    rawmode: str
    palette: Incomplete
    def __init__(self, fp) -> None: ...
    def getpalette(self): ...
