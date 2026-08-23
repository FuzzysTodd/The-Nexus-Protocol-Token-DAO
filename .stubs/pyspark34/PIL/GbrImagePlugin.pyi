from . import Image as Image, ImageFile as ImageFile
from _typeshed import Incomplete

class GbrImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    im: Incomplete
    def load(self): ...
