from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from ._binary import o8 as o8
from _typeshed import Incomplete

MODES: Incomplete

class TgaImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    im: Incomplete
    def load_end(self) -> None: ...

SAVE: Incomplete
