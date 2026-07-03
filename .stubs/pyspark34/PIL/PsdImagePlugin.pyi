from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import i8 as i8
from _typeshed import Incomplete

MODES: Incomplete

class PsdImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    mode: Incomplete
    tile: Incomplete
    frame: Incomplete
    fp: Incomplete
    def seek(self, layer): ...
    def tell(self): ...
