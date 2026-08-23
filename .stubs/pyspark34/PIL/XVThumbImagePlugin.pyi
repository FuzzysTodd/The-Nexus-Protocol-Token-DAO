from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8

PALETTE: bytes

class XVThumbImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
