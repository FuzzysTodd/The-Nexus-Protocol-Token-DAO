from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8
from _typeshed import Incomplete

logger: Incomplete

class PcxImageFile(ImageFile.ImageFile):
    format: str
    format_description: str

SAVE: Incomplete
