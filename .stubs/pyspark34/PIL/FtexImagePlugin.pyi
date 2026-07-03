from . import Image as Image, ImageFile as ImageFile
from enum import IntEnum

MAGIC: bytes

class Format(IntEnum):
    DXT1: int
    UNCOMPRESSED: int

class FtexImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    def load_seek(self, pos) -> None: ...
