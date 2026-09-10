from . import Image as Image, ImageFile as ImageFile
from _typeshed import Incomplete

MODES: Incomplete

class FpxImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    fp: Incomplete
    def load(self): ...
    def close(self) -> None: ...
    def __exit__(self, *args) -> None: ...
