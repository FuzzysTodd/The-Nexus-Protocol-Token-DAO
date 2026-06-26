from . import Image as Image, ImageFile as ImageFile, ImagePalette as ImagePalette
from _typeshed import Incomplete

COMMENT: str
DATE: str
EQUIPMENT: str
FRAMES: str
LUT: str
NAME: str
SCALE: str
SIZE: str
MODE: str
TAGS: Incomplete
OPEN: Incomplete
split: Incomplete

def number(s): ...

class ImImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    @property
    def n_frames(self): ...
    @property
    def is_animated(self): ...
    frame: Incomplete
    fp: Incomplete
    tile: Incomplete
    def seek(self, frame) -> None: ...
    def tell(self): ...

SAVE: Incomplete
