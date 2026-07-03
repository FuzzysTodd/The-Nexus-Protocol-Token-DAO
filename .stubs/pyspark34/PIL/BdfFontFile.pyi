from . import FontFile as FontFile, Image as Image
from _typeshed import Incomplete

bdf_slant: Incomplete
bdf_spacing: Incomplete

def bdf_char(f): ...

class BdfFontFile(FontFile.FontFile):
    """Font file plugin for the X11 BDF format."""
    def __init__(self, fp) -> None: ...
