from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8
from _typeshed import Incomplete

xpm_head: Incomplete

class XpmImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def load_read(self, bytes): ...
