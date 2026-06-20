from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8

class FliImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def seek(self, frame) -> None: ...
    def tell(self): ...
