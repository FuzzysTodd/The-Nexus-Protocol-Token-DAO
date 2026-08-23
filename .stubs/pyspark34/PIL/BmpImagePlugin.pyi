from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8
from _typeshed import Incomplete

BIT2MODE: Incomplete

class BmpImageFile(ImageFile.ImageFile):
    """Image plugin for the Windows Bitmap format (BMP)"""
    format_description: str
    format: str
    COMPRESSIONS: Incomplete

class BmpRleDecoder(ImageFile.PyDecoder):
    def decode(self, buffer): ...

class DibImageFile(BmpImageFile):
    format: str
    format_description: str

SAVE: Incomplete
