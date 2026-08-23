from ._binary import o8 as o8
from _typeshed import Incomplete

class PaletteFile:
    """File handler for Teragon-style palette files."""
    rawmode: str
    palette: Incomplete
    def __init__(self, fp) -> None: ...
    def getpalette(self): ...
